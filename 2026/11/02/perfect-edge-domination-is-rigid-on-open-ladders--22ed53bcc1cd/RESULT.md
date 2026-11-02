# Perfect edge domination is rigid on open ladders

## Finding

Let \(L_n=P_2\square P_n\) be the labelled two-row, \(n\)-column open ladder, \(n\ge2\). A *perfect edge dominating set* (PED set) is an edge subset \(F\subseteq E(L_n)\) such that every edge outside \(F\) is adjacent, by a shared endpoint, to **exactly one** edge of \(F\). Edges inside \(F\) are not subject to this one-neighbor restriction. Define the complete PED cardinality polynomial
\[
 Q_n(z)=\sum_{F\text{ PED}}z^{|F|}.
\]
Then, for every integer \(n\ge2\),
\[
 \boxed{Q_n(z)=z^{3n-2}+\left(2+2\mathbf1_{\{n\equiv2\pmod3\}}\right)z^n.}
\]
There are no intermediate PED cardinalities: the entire edge set is the unique maximum PED set; all proper PED sets have exactly \(n\) edges. Thus the minimum PED number is \(n\), with exactly four minimum sets if \(n\equiv2\pmod3\), and exactly two otherwise. The result classifies every PED set constructively by the finite transition graph below.

## Assumptions and scope

Graphs are finite, simple, labelled, and undirected. The two ladder rows and the left-to-right column ordering are distinguished for the description, but the number counts edge subsets, not isomorphism classes. The path \(P_n\) has \(n\) vertices, so \(L_n\) has \(2n\) vertices, \(n\) rungs, and \(2(n-1)\) horizontal edges. The definition of PED is *not* efficient edge domination: a selected edge is allowed to be adjacent to other selected edges.

Encode column \(i\) by three bits \(a_i,b_i,d_i\): \(a_i=1\) selects its vertical rung, and, for \(i<n\), \(b_i,d_i\) select respectively the upper and lower horizontal edge joining columns \(i\) and \(i+1\). Set \(b_0=d_0=b_n=d_n=0\), and put the column mask \(s_i=a_i+2b_i+4d_i\). Thus \(s_n\in\{0,1\}\). A mask has \(\mathrm{wt}(s)\) selected bits.

## Proof

**Local test.** An unselected rung in column \(i\) has precisely the adjacent selected-edge count \(b_{i-1}+b_i+d_{i-1}+d_i\). Thus
\[
 a_i=0\quad\Longrightarrow\quad b_{i-1}+b_i+d_{i-1}+d_i=1.
\]
For \(1\le i<n\), an unselected upper (respectively lower) horizontal edge has adjacent selected-edge count \(b_{i-1}+a_i+a_{i+1}+b_{i+1}\) (respectively \(d_{i-1}+a_i+a_{i+1}+d_{i+1}\)). Hence
\[
\begin{aligned}
 b_i=0&\Longrightarrow b_{i-1}+a_i+a_{i+1}+b_{i+1}=1,\\
 d_i=0&\Longrightarrow d_{i-1}+a_i+a_{i+1}+d_{i+1}=1.
\end{aligned}
\]
These are equivalent to the PED condition, edge by edge; selected edges impose no additional condition.

**Finite transition certificate.** Consider all \(64\) ordered mask-pairs \((p,c)\in\{0,\ldots,7\}^2\). Draw \((p,c)\to(c,t)\) when the displayed three local tests hold at a nonterminal column with preceding mask \(p\), present mask \(c\), and following mask \(t\). The initial state is \((0,s_1)\). A terminal state is \((p,c)\) with \(c\in\{0,1\}\) satisfying the rung test with outgoing horizontals zero; there is no horizontal edge at the last column. Thus PED sets correspond **bijectively** to paths of exactly \(n-1\) transitions from an initial state to a terminal state, with selected-edge weight \(\sum_{i=1}^n\mathrm{wt}(s_i)\).

Straight substitution in the three displayed Boolean implications, and forward/backward reachability on the \(64\)-state graph, leave exactly the following \(14\) states belonging to some initial-to-terminal walk. The table gives *all* arrows among these states; arrows into states not lying on any complete walk are deliberately omitted.

| State | Successors on complete walks |
| --- | --- |
| \((0,1)\) | none |
| \((0,2)\) | \((2,1),(2,3)\) |
| \((0,3)\) | \((3,0)\) |
| \((0,4)\) | \((4,1),(4,5)\) |
| \((0,5)\) | \((5,0)\) |
| \((0,7)\) | \((7,1),(7,7)\) |
| \((2,1)\) | none |
| \((2,3)\) | \((3,0)\) |
| \((3,0)\) | \((0,4)\) |
| \((4,1)\) | none |
| \((4,5)\) | \((5,0)\) |
| \((5,0)\) | \((0,2)\) |
| \((7,1)\) | none |
| \((7,7)\) | \((7,1),(7,7)\) |

The initial states in this table are \((0,1),(0,2),(0,3),(0,4),(0,5),(0,7)\). The terminal states are \((0,1),(2,1),(3,0),(4,1),(5,0),(7,1)\). Both lists, the reachability computation, and every arrow are independently reproducible by `verify.py`, which enumerates the entire \(64\)-state transition graph from the displayed equations; the finite table is an exact check of a finite logical implication, not extrapolation from finite ladder lengths.

**Classification of paths of arbitrary length.** Apart from the length-zero boundary case at \((0,1)\), the admissible graph has just two components:

* A branch \((0,7)\to(7,7)\to\cdots\to(7,7)\to(7,1)\), allowing zero or more \((7,7)\) loops. This is exactly the all-edge set with mask word \(7^{n-1}1\), of weight \(3n-2\).
* Four entrance states \((0,2),(0,3),(0,4),(0,5)\), feeding the directed six-cycle \((0,2)\to(2,3)\to(3,0)\to(0,4)\to(4,5)\to(5,0)\to(0,2)\), together with terminal exits \((0,2)\to(2,1)\) and \((0,4)\to(4,1)\). The corresponding periodic column-mask sequence is \(2,3,0,4,5,0\), with permissible entry phases and terminal exits determined by the table.

In the second component, adding one complete turn of the six-cycle adds exactly six columns and six selected edges. The accepted words for \(2\le n\le7\) have respective minimum-family counts \(4,2,2,4,2,2\), each of selected-edge weight \(n\). Consequently the same statement holds for all \(n\ge2\) by repeatedly adding six columns. The four allowable entry phases yield two accepted paths when \(n\equiv0\) or \(1\pmod3\), and four when \(n\equiv2\pmod3\). No other full walks exist by the complete transition table, which proves the formula.

## Verification

Execute `python verify.py` using Python 3.9+ and the standard library. It independently constructs actual ladder edge lists and checks the PED definition by direct edge-subset enumeration for \(2\le n\le7\): in total \(599184\) tested edge subsets. Separately it exhausts the \(64\) pair states and their transitions, confirms exactly the displayed \(14\)-state relevant subgraph, and compares the resulting dynamic-programming polynomial with the theorem for every \(2\le n\le160\). Its successful output is:

`VERIFY_OK direct_ladder_lengths=2..7 checked_edge_subsets=599184 finite_relevant_states=14 transfer_lengths=2..160`

The infinite assertion follows from the exact local equivalence and the finite complete transition graph, not from the length-\(160\) numerical check.

## Relationship to prior work

The PED definition, algorithmic significance, and general counting problem appear in Grippo, Lin, Moyano, and Vera's 2026 paper [1], which provides linear-time counting algorithms for generalized series-parallel and chordal graphs. A general algorithm, applied to each ladder, does not by itself state the closed two-term cardinality distribution or the three-periodic multiplicity and complete state classification here.

A 2020 paper by Chitra and Prabhavathi [2, Section 2, Theorem 2.6] specifically discusses minimum PED sets of open ladders and gives constructions. Its displayed minimum-cardinality formula differs in the \(n\equiv1\pmod3\) case; for example, the direct \(n=4\) certificate here gives two size-four PED sets whereas that formula gives ten. The complete enumeration and its proof are established here independently, not inferred from that prior statement. The older paper does not present the two-term cardinality polynomial or complete optimal-set multiplicity.

PED sets correspond to perfect dominating vertex sets of the line graph, provided *selected vertices themselves are not required to have exactly one selected neighbor*. Efficient edge domination, also called a dominating induced matching, imposes a stronger condition and must not be conflated with PED enumeration.

## Limitations

The classification is for labelled two-row **open** ladders with \(n\ge2\); it does not cover circular ladders, wider grids, or general series-parallel graphs. The 2026 algorithm paper [1] was accessible as a dated abstract, but full text could not be obtained during the comparison; undiscovered full-text examples or other historical counting formulas remain an originality risk. The 2020 conflicting minimum assertion is a documented comparison, not a premise of the proof. No independent mathematical audit is claimed.

## References

[1] L. N. Grippo, M. C. Lin, V. Moyano, and C. Vera, *Counting perfect edge dominating sets: extremal results and linear-time algorithms*, arXiv:2607.03894v1, first posted July 4, 2026, https://arxiv.org/abs/2607.03894 .

[2] S. Chitra and N. Prabhavathi, *A study of perfect edge, perfect edge covering and perfect edge vertex domination sets in graphs*, International Journal of Research and Analytical Reviews 7(1), 2020, pp. 408–415, https://www.ijrar.org/papers/IJRAR2001330.pdf .

[3] M. C. Lin, V. V. Lozin, V. Moyano, and J. Szwarcfiter, *Perfect edge domination: hard and solvable cases*, Annals of Operations Research 264 (2018), 287–305, https://doi.org/10.1007/s10479-017-2664-3 .
