# An exact transient-depth law for \(3\times3\) random zero-sum best-response dynamics

## Finding

Let a two-player zero-sum game have payoff matrices \((A,-A)\), where the nine entries of \(A\) are independent with one common atomless real distribution. Form the directed alternating-best-response graph with row-strategy vertices \(r_i\) and column-strategy vertices \(c_j\): an edge leaves \(r_i\) for the column minimizing row \(i\) of \(A\), and an edge leaves \(c_j\) for the row maximizing column \(j\) of \(A\). Every vertex has outdegree one, almost surely.

Choose one of the six vertices independently and uniformly. Let \(T\) be the number of directed edges until its forward trajectory first enters a directed cycle (so a vertex already on a cycle has \(T=0\)). Then the **entire exact distribution** is

| \(t\) | \(\Pr(T=t)\) |
|---:|---:|
| \(0\) | \(163/280\) |
| \(1\) | \(181/630\) |
| \(2\) | \(41/360\) |
| \(3\) | \(17/1260\) |
| \(4\) | \(1/315\) |

Consequently,
\[
\mathbb E[T]=\frac{179}{315}.
\]

Let \(M\) denote the maximum such entry time among the six vertices of a sampled game. Its distribution is

| \(m\) | \(\Pr(M=m)\) |
|---:|---:|
| \(0\) | \(5/112\) |
| \(1\) | \(1909/5040\) |
| \(2\) | \(1249/2520\) |
| \(3\) | \(13/210\) |
| \(4\) | \(2/105\) |

In particular, the bound \(M\le4\) is sharp, and the maximal four-edge transient occurs with probability exactly \(2/105\). The result is independent of the underlying atomless payoff distribution. Among square games with fewer than three strategies per player, this four-edge transient is impossible.

## Assumptions and scope

The entries of \(A=(a_{ij})_{0\le i,j\le2}\) are independent and identically distributed, and ties have probability zero. Player one maximizes \(A\); player two maximizes \(-A\). The graph uses *alternating best responses* represented by an edge from a currently fixed strategy of one player to the other player's unique best response. Its vertices are six individual strategies, **not** the nine joint action profiles. All hitting times here count edges in this graph to the first recurrent vertex. They do not describe fictitious play, arbitrary asynchronous update rules or the number of payoff evaluations needed to compute a best response.

## Proof

**1. Finite rank reduction.** Because the entries are identically distributed and atomless, all \(9! =362880\) relative orders of the nine cells have equal probability. The graph depends only on this order. Define \(I_i\in\{0,1,2\}\) as the column of the minimum in row \(i\), and \(J_j\in\{0,1,2\}\) as the row of the maximum in column \(j\). The six edges are exactly \(r_i\to c_{I_i}\) and \(c_j\to r_{J_j}\). There are \(3^6=729\) candidate pairs \((I,J)\), including pairs of zero probability.

**2. An exact finite recurrence.** To a candidate \((I,J)\), associate strict inequalities on the nine labeled cells:
\[
 a_{i,I_i}<a_{i,j}\quad(j\ne I_i),\qquad
 a_{k,j}<a_{J_j,j}\quad(k\ne J_j).
\]
For each cell \(x\), let \(P_x\) be the set of its immediate predecessors under these inequalities and let \(U\) be the nine-cell ground set. Set \(L(U)=1\) and, for every proper subset \(S\subset U\), compute
\[
L(S)=\sum_{\substack{x\in U\setminus S\\P_x\subseteq S}}L(S\cup\{x\}).
\]
Induction on \(9-|S|\) proves that \(L(S)\) counts exactly the allowable completions of the increasing cell order from prefix \(S\); the recurrence also returns zero for cyclic inequalities. Thus \(L(\varnothing)\) counts precisely the rank matrices inducing \((I,J)\). Each rank matrix induces exactly one pair of maps, so summing these counts over all candidate pairs must give \(9!\). This is an exhaustive finite counting proof, not a sampling argument.

**3. Exact joint classification.** Apply the recurrence to every pair of maps, follow the induced six-vertex functional graph, and classify its directed cycle-length multiset \(\sigma\) together with maximum entry time \(M\). The resulting integer counts of relative payoff orders are:

| Directed cycle lengths \(\sigma\) | \(M\) | Number of orders |
|---|---:|---:|
| \((2)\) | \(1\) | \(9576\) |
| \((2)\) | \(2\) | \(69264\) |
| \((2)\) | \(3\) | \(22464\) |
| \((2)\) | \(4\) | \(6912\) |
| \((4)\) | \(1\) | \(127872\) |
| \((4)\) | \(2\) | \(110592\) |
| \((6)\) | \(0\) | \(15552\) |
| \((2,4)\) | \(0\) | \(648\) |

These eight integers sum to \(362880\). A cycle uses equally many row and column vertices, and a functional graph contains vertex-disjoint directed cycles. Furthermore, a zero-sum game with all distinct entries has at most one pure saddle point, hence at most one directed two-cycle. The listed cycle types are therefore exhaustive; the recurrence verifies that all eight indicated depth classes, and no others, occur.

For a game with map pair \((I,J)\), write \(d_x(I,J)\) for the distance of vertex \(x\) to its forward directed cycle. The same exact recurrence, now weighting each candidate by its number of vertices at each depth, gives
\[
\bigl(H_0,H_1,H_2,H_3,H_4\bigr)
=(1267488,625536,247968,29376,6912),
\]
where
\[
H_t=\sum_{I,J}L_{I,J}(\varnothing)\,
\bigl|\{x:d_x(I,J)=t\}\bigr|.
\]
These integers sum to \(6\cdot9!=2177280\). Dividing by \(6\cdot9!\) gives the stated distribution of \(T\); summing \(t\Pr(T=t)\) gives \(179/315\). Summing each row of the joint classification by \(M\) and dividing by \(9!\) gives the second displayed distribution.

**4. Sharpness and an independent maximal-delay count.** Every recurrent class contains at least a two-cycle. With six vertices, at most four distinct vertices can precede it in a simple directed chain, proving \(M\le4\). Equality forces a single two-cycle and a chain comprising all four remaining vertices. Such a graph is determined by its saddle cell (nine choices), which side starts the chain (two choices), and the order of the other two row and two column vertices (two choices each): exactly \(9\cdot2\cdot2\cdot2=72\) labeled candidates. For one canonical candidate,
\[
(I_0,I_1,I_2)=(0,1,2),\quad(J_0,J_1,J_2)=(0,2,0),
\]
the chain is \(r_1\to c_1\to r_2\to c_2\to r_0\leftrightarrow c_0\). The same nine-cell recurrence gives exactly \(96\) compatible strict total orders; symmetry gives \(96\) for every candidate. Therefore precisely \(72\cdot96=6912\) rank orders have \(M=4\), yielding \(6912/9!=2/105\). Exactly one of their six vertices has depth four, yielding \(\Pr(T=4)=1/315\).

An explicit realizing rank matrix is
\[
A=\begin{pmatrix}4&5&7\\1&0&6\\3&8&2\end{pmatrix}.
\]
With two strategies per player, there are only four graph vertices and at least two are on a directed cycle, so the entry time is at most two. Thus three strategies per player are the first size allowing the sharp four-edge transient.

## Verification

The included `verify.py` is a standard-library-only standalone checker. It independently constructs all \(729\) candidate pairs of row-minimum/column-maximum maps, counts each through the fully specified subset recurrence, and independently enumerates **all** \(9!\) relative payoff orders, constructing the successor graph directly for each. Both routes reproduce the eight joint counts, five vertex-depth totals, two distributions, sharp maximal-chain count and expected entry time. Run `python3 verify.py`; successful completion prints `EXACT_VERIFY_OK`. The proofs of distribution-independence and completeness are in the preceding sections, not inferred from empirical random trials.

## Relationship to prior work

Karelas, Lugosi and Zhang (October 21, 2026), Section 6, study the same random zero-sum best-response digraph. Their exact integral formula (6.4) gives probabilities of *specified cycles*, and their main results control cycle counts and longest cycle length asymptotically. Those results do not specify the vertex-to-recurrent-class entry-time distribution or the eight joint cycle/depth strata above. In particular, two graphs with the same four-cycle type can have maximum entry times one or two, so cycle-type probabilities alone do not determine the claimed distribution. Their Section 5 studies path lengths for *common-interest* games, a different payoff structure.

Heinrich, Jang, Mungo, Pangallo, Scott, Tarbush and Wiese (2023) analyze convergence under different playing sequences in random normal-form games, primarily with independent random payoff matrices for the two players. That model lacks the exact zero-sum constraint and does not establish this finite transient-depth law. Goldman's classical pure-saddle probability, as recalled in the 2026 paper, is previously known and not claimed here as new.

## Limitations

This is an exact finite-market result for three strategies per player and one common atomless payoff law. It does not give an asymptotic transient-depth law for larger games, does not address mixed-strategy equilibrium computation, and does not prove convergence to a pure Nash equilibrium: a trajectory may enter a nontrivial directed cycle. The relationship-to-literature comparison cannot exclude unindexed or otherwise inaccessible prior exact enumerations. Independent validation has not been performed.

## References

1. G. N. Karelas, G. Lugosi and R.-R. Zhang, *Cycle structure of best-response dynamics in random bimatrix games*, arXiv:2610.29153v1, October 21, 2026, https://arxiv.org/html/2610.29153v1 . Relevant sections: 1, 5 and 6.
2. T. Heinrich, Y. Jang, L. Mungo, M. Pangallo, A. Scott, B. Tarbush and S. Wiese, *Best-response dynamics, playing sequences, and convergence to equilibrium in random games*, International Journal of Game Theory 52 (2023), 703–735, https://doi.org/10.1007/s00182-023-00837-4 .
3. A. J. Goldman, *The probability of a saddlepoint*, American Mathematical Monthly 64 (1957), 729, as cited and discussed in Reference 1.
