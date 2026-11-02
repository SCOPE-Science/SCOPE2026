# Sharp adjacent-swap convergence lengths for two-agent five-good round robin

## Finding

For two agents, five distinct goods, the alternating picking order \(1,2,1,2,1\), and any pair of strictly ordered, strictly positive, additive true utility functions, construct the **adjacent-swap improvement graph** as follows. Its vertices are pairs of complete reported rankings. From a vertex, draw an arc when one agent exchanges two consecutive positions of her own report and thereby strictly increases the total true utility of her allocated bundle under round robin. The other report is fixed.

**Exact theorem.** Every such improvement graph is acyclic. Every directed path has at most **18** arcs, and this is attained for some true preferences and arbitrary initial reports. When the initial reports must equal the two true rankings, every directed path has at most **6** arcs, and this is attained. These two constants are exact; they hold for *all* positive cardinal additive utilities consistent with the agents' respective strict rankings, not merely for one fixed normalization.

In particular, every sequence of strictly improving adjacent swaps terminates at an adjacent-swap local equilibrium, regardless of how the improving agent and improving swap are selected. This is a finite five-good result; it does not establish convergence for more goods or for unrestricted report changes.

## Assumptions and scope

Label the goods \(\{0,1,2,3,4\}\). Each agent has a strict true order \(\succ_i\) and positive additive utility \(u_i\), with \(u_i(g)>u_i(h)\) exactly when \(g\succ_i h\). The first agent selects on turns \(1,3,5\) and the second on \(2,4\). A reported ranking is any permutation of the goods, independently of the true ranking. At each turn the acting agent receives her highest ranked remaining good *according to her current report*. Only one adjacent transposition by one agent is permitted at a time. It is an admissible move only if the acting agent's **true** sum of received good values strictly increases. No change in the allocation without a change in this true utility counts as a move.

The unrestricted-start bound considers all report pairs. The truthful-start bound allows only paths beginning at \((\succ_1,\succ_2)\). Good relabeling lets us fix \(\succ_1=(0,1,2,3,4)\), with \(5!=120\) choices for \(\succ_2\).

## Proof

This is a complete finite proof by exact enumeration, backed by executable source, rather than an induction in the number of goods.

**Step 1: Exhaustive encoding.** Enumerate the \(120\) permutations lexicographically as \(P_0,\ldots,P_{119}\). The vertex set has \(120^2=14{,}400\) ordered report pairs. For each vertex, replay the five picks and store the first agent's bundle as a five-bit mask. Every vertex has eight candidate transpositions (four in each report). Therefore there are exactly \(115{,}200\) candidate directed report changes before filtering on utility.

**Step 2: Remove dependence on cardinal magnitudes.** Compare the two five-bit masks before and after *each* candidate transposition, also taking complements for the second agent. Exactly \(88{,}800\) candidates leave allocations unchanged; the other \(26{,}400\) candidates replace **exactly one** good in the deviating agent's bundle with **exactly one** other good. There is no candidate that exchanges two or more goods. These integers are exhaustively checked by `verify.cpp`, including an assertion on each nonzero transition; `crosscheck.py` independently constructs the entire transition relation and checks the one-for-one exchange property. Hence a nontrivial candidate is profitable for an agent exactly when her gained good outranks her lost good under \(\succ_i\). Strictly ordered additive utilities cannot change the sign of such a move.

**Step 3: Exhaust the true orders.** Fix \(\succ_1=(0,1,2,3,4)\), and loop over all \(120\) possibilities for \(\succ_2\). Orient a candidate as an improvement precisely by the gained/lost ranking comparison from Step 2. For each resulting digraph, depth-first visitation detects directed cycles and computes the longest path \(L(v)=\max(\{0\}\cup\{1+L(w):v\to w\})\). All \(120\) graphs are acyclic. Across the \(120\) graphs there are \(1{,}584{,}000\) improving arcs in total. The maximum over every start vertex is **18**, while the maximum over the truthful start vertex \((P_0,P_q)\) is **6**. A second implementation in `crosscheck.py` reconstructs all allocations independently and uses Kahn's topological algorithm, rather than depth-first cycle detection, reproducing all three totals and both maxima.

**Step 4: Attainment.** The enumerator prints paths with \(18\) and \(6\) profitable swaps. For the \(18\)-step witness both agents' true rankings are \((0,1,2,3,4)\), with initial *reports* \((2,3,4,1,0)\) and \((4,3,2,1,0)\). For the \(6\)-step truthful-start witness the agents' true rankings are \((0,1,2,3,4)\) and \((3,1,2,4,0)\). The supplied `WITNESSES.json` gives every intermediate report pair. A direct independent check verifies for each successive pair that exactly one adjacent swap occurred and that the deviator gained a good strictly preferred to the good she lost. Choosing \(u_i(g)=5-r_i(g)\), where \(r_i(g)\in\{0,1,2,3,4\}\) is the zero-based true rank, realizes every step with positive additive utilities. Thus neither maximum can be lowered.

Since all true preferences are reduced by relabeling, all report states and all candidate adjacent changes are enumerated, and every possible edge depends only on the true order, these finite checks cover *every* case under the assumptions.

## Verification

Run `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`, then `python3 crosscheck.py`, with the bundled files in one directory. The main verifier reports `N=14400`, `transitions_zero=88800`, `transitions_one_swap=26400`, `transitions_multiple=0`, `true_ranking_profiles=120`, `cycles=0`, `best_all=18`, `best_from_truth=6`, and `active_edges_total=1584000`. The independent checker prints `VERIFY_INDEPENDENT 14400 120 18 6 1584000`. Both use integer arithmetic only. `WITNESSES.json` contains the sharpness paths; no external input data are required. No assumption that a partial search proves acyclicity is made: the code constructs all candidate transitions and traverses every state for all true-order pairs after symmetry reduction.

## Relationship to prior work

Lucet, Surugue, Benabbou, Beynier, Maudet, and Novaro, *On the Convergence of Iterated Round Robin* (arXiv:2610.23040v1, first submitted 2026-10-16), prove adjacent-swap convergence for two agents and four goods and explicitly leave the arbitrary-number-of-goods two-agent case as a conjecture. Their guarantee for **item-preserving** swaps at every population and item count is a different restriction and does not imply the present adjacent-swap result. The five-good case is the first item count not established by their four-good adjacent-swap argument. The present result strengthens that finite boundary by supplying exact maximum path lengths from both arbitrary and truthful reports, not just termination.

Aziz, Goldberg, and Walsh, *Equilibria in Sequential Allocation* (arXiv:1705.09444, 2017), demonstrate cycling for general better-response dynamics in sequential allocation, without imposing the adjacent-transposition restriction. Their negative result therefore does not cover the specific local-dynamics graph studied here.

## Limitations

The findings are confined to precisely two agents, exactly five goods, alternating order beginning with agent one, additive consistent true utilities, and single adjacent report transpositions. An unrestricted Nash equilibrium is **not** established at termination: only the absence of a profitable adjacent swap is guaranteed. The bound of \(6\) is sharp for arbitrary strictly improving local moves from truthful reports; the theorem does **not** assert that every displayed sharpness move is the cardinally best move among all permitted adjacent swaps. The exhaustive proof is finite and does not settle the arbitrary-item conjecture. The possibility of an unindexed equivalent exact finite census or a different formulation of the same potential-game property is a residual literature risk.

## References

1. M. Lucet, H. Surugue, N. Benabbou, A. Beynier, N. Maudet, and A. Novaro, *On the Convergence of Iterated Round Robin*, arXiv:2610.23040v1 (2026-10-16). https://arxiv.org/abs/2610.23040 . Full text examined via https://www.paperpeel.com/paper/2610.23040 (Sections 2--3 and Appendix A.3).
2. H. Aziz, P. Goldberg, and T. Walsh, *Equilibria in Sequential Allocation*, arXiv:1705.09444v1 (2017). https://arxiv.org/abs/1705.09444 . Author-provided full text https://www.researchgate.net/publication/317187490_Equilibria_in_Sequential_Allocation (Introduction, model, Nash dynamics).
