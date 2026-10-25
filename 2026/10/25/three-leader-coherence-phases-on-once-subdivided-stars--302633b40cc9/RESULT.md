# Three-leader coherence phases on once-subdivided stars

## Finding

Let \(T_k\) be the unweighted tree obtained by subdividing each edge of \(K_{1,k}\) exactly once, with integer \(k\ge3\). Its vertices are a hub \(c\), intermediate vertices \(u_1,\ldots,u_k\), and leaves \(v_1,\ldots,v_k\); its edges are \(cu_i\) and \(u_iv_i\). For any three-element noise-free leader set \(S\), let \(F=V(T_k)\setminus S\), let \(L\) be the combinatorial Laplacian, and define the normalized coherence cost
\[
J_k(S)=\operatorname{tr}\bigl((L_{FF})^{-1}\bigr).
\]
For unit-covariance continuous-time white noise on the follower dynamics, total steady-state variance is \(J_k(S)/2\), so the minimizers are unchanged.

**Theorem.** Every three-leader global minimizer, and its exact objective value, is classified as follows.

| Arms | Every optimal set | Minimum \(J_k\) | Number of unordered optimum sets |
| --- | --- | --- | --- |
| \(k=3\) | All three leaves \(\{v_1,v_2,v_3\}\) | \(8/3\) | \(1\) |
| \(k=4\) | One intermediate \(u_i\) and two leaves on two *other*, distinct arms | \(27/4\) | \(12\) |
| \(k\ge5\) | Hub \(c\) and two leaves on distinct arms | \(3k-5\) | \(\binom{k}{2}\) |

In each parameter range, every nonoptimal placement orbit has strictly larger cost; nonoptimal orbits may tie with one another. In particular, hub placement first becomes optimal at exactly five arms.

## Assumptions and scope

Every edge has unit conductance. Leaders are distinct, exactly three in number, fixed and noise-free. The follower Laplacian is a principal submatrix of the original Laplacian, **not** the Laplacian of the induced follower graph: diagonal degrees retain edges to leaders. The connected original tree and nonempty leader set ensure \(L_{FF}\) is positive definite. No result is asserted for different arm lengths, weighted edges, noisy leaders, or a different leader budget.

## Proof

First suppose the hub \(c\) is a leader. A fully unselected arm has grounded follower block \(B=\begin{pmatrix}2&-1\\-1&1\end{pmatrix}\), with \(\operatorname{tr}(B^{-1})=3\). Choosing only the leaf of that arm as an additional leader leaves cost \(1/2\); choosing only the intermediate leaves cost \(1\); choosing both leaves cost \(0\). Relative to an untouched arm, these possibilities save \(5/2\), \(2\), and \(3\), respectively. With two remaining leaders and at least three arms, the unique best orbit places them at leaves on two distinct arms, saving \(5\). This gives
\[
J_{\mathrm{hub}}=3k-5.
\]
Every other hub-containing orbit is strictly worse.

Now suppose the hub is a follower. Classify each arm as \(0\) (no leaders), \(I\) (only its intermediate vertex is a leader), \(V\) (only its leaf is a leader), or \(B\) (both are leaders). Write their counts \(n_0,n_I,n_V,n_B\), so \(n_0+n_I+n_V+n_B=k\) and \(n_I+n_V+2n_B=3\). The unselected arm's follower block is \(B\) as above, with
\[
B^{-1}=\begin{pmatrix}1&1\\1&2\end{pmatrix}.
\]
An arm of type \(V\) leaves the \(1\times1\) block \((2)\), and an arm of type \(I\) leaves a disconnected follower leaf with block \((1)\). Eliminating all follower arm blocks by a Schur complement at the hub gives the positive scalar
\[
s=k-n_0-\frac{n_V}{2}=n_I+n_B+\frac{n_V}{2}>0.
\]
The block-inverse trace identity, using \(\|B^{-1}(1,0)^{\mathsf T}\|^2=2\) and \(\|(2)^{-1}\|^2=1/4\), gives **exactly**
\[
J_k(S)=3n_0+\frac{n_V}{2}+n_I+
\frac{1+2n_0+n_V/4}{n_I+n_B+n_V/2}.
\tag{1}
\]
The six possible three-leader orbit types without the hub and their resulting costs are:

| Type | Cost from (1) |
| --- | --- |
| \(III\), on three distinct arms | \((11k-23)/3\) |
| \(IIV\), on three distinct arms | \((19k-42)/5\) |
| \(IVV\), on three distinct arms | \(4k-37/4\) |
| \(VVV\), on three distinct arms | \((13k-31)/3\) |
| \(B+I\), on two distinct arms | \(4k-13/2\) |
| \(B+V\), on two distinct arms | \((13k-22)/3\) |

All six types are feasible for \(k\ge3\); the table is exhaustive because three selected non-hub vertices occupy either two arms, with both selected on one, or three arms with one selected on each. For \(k=3\), comparison with \(3k-5=4\) shows that \(VVV\) uniquely attains the minimum \(8/3\), the next-lowest cost being \(IVV=11/4\). For \(k=4\), the unique winning type is \(IVV\), with \(J=27/4\), strictly smaller than \(IIV=34/5\); all remaining orbit types, including those containing the hub, cost at least \(7\).

For every integer \(k\ge5\), subtracting the hub-containing optimum \(3k-5\) from the six no-hub costs, in the table's order, yields
\[
\frac{2k-8}{3},\quad\frac{4k-17}{5},\quad k-\frac{17}{4},\quad\frac{4k-16}{3},\quad k-\frac32,\quad\frac{4k-7}{3}.
\]
Each is strictly positive for \(k\ge5\). This proves global optimality and the complete classification. Counting symmetric choices gives respectively one triple, \(k\binom{k-1}{2}=12\) when \(k=4\), and \(\binom{k}{2}\) when \(k\ge5\). \(\square\)

## Verification

Run `python3 verify.py` with Python's standard library. The checker reconstructs the original graph Laplacians, performs exact rational Gauss–Jordan inversions, compares all ten possible orbit costs for \(3\le k\le11\), and exhaustively evaluates all three-leader sets for \(k\in\{3,4,5\}\). Expected successful summary is in `verify_output.txt`. These finite checks independently test the derivation and boundary cases; they are not used as a substitute for the symbolic proof for all integers \(k\ge3\).

## Relationship to prior work

Patterson and Bamieh (2010) formulate the grounded-Laplacian coherence objective for noise-free leader selection. Lin, Fardad and Jovanović (2013) develop general convex-relaxation and greedy approaches for leader selection, including noise-free leaders; these methods do not themselves specify the exact optimizer on every subdivided star. Fitch and Leonard (2014) derive a general joint-centrality representation and give explicit special-family results for paths and cycles. The object, trace criterion, and Schur-complement technique are established tools; the claimed addition is solely the exact three-phase placement classification and optimizer counts for the entire once-subdivided-star family.

## Limitations

This theorem is restricted to **exactly three** noise-free leaders, \(k\ge3\), two-edge arms, unit graph conductances, and inverse-grounded-Laplacian trace. It says nothing about optimal placements with other leader budgets, weighted spiders, or other objective functions. The finite computation verifies examples and algebraic identities but is not a proof of the infinite family; no independent mathematical audit has been performed. The literature comparison cannot exclude unindexed equivalent results.

## References

1. S. Patterson and B. Bamieh, *Leader Selection for Optimal Network Coherence*, IEEE CDC (2010), DOI: 10.1109/CDC.2010.5718151.
2. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, first posted 2013-02-03, https://arxiv.org/abs/1302.0450.
3. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first posted 2014-07-07, https://arxiv.org/abs/1407.1569.
4. S. Patterson, N. McGlohon, and K. Dyagilev, *Optimal \(k\)-Leader Selection for Coherence and Convergence Rate in One-Dimensional Networks*, arXiv:1604.07094 (2016); paths and cycles, not branched spiders.
