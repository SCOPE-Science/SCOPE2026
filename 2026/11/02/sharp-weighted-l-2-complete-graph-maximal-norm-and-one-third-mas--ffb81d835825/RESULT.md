# Deciding sharp-bound attainment for weighted complete-graph maximal averages

## Finding

An instance is a list of at least two positive integers \(w_i\), encoded in binary. On the unit-edge complete graph with these vertex masses, set
\[
W=\sum_iw_i,\qquad (M_wf)_i=\max\bigl\{|f_i|,W^{-1}\sum_jw_j|f_j|\bigr\},\qquad \|f\|_{2,w}^2=\sum_i w_i|f_i|^2.
\]
Deciding whether \(\|M_w\|_{L^2(w)\to L^2(w)}=2/\sqrt3\) is weakly NP-complete under polynomial many-one reductions. There is a pseudo-polynomial decision algorithm using \(O(nW)\) Boolean table operations and \(O(W)\) space, where \(n\) is the number of vertices. The question concerns exact equality, not estimating the norm to a tolerance.

## Analytical input: the equality criterion

The active-set argument of González-Riquelme and Madrid, *Sharp inequalities for maximal operators on finite graphs*, [arXiv:2005.03146v3](https://arxiv.org/html/2005.03146v3), Theorem 4 and §3.1, gives a sharp bound on a counting-measure clique for each active fraction \(k/n\), before maximizing over \(k\). In the integer-weight setting a vertex of mass \(w_i\) is replaced by \(w_i\) clones and the lifted input is constant on each clone class. The per-active-fraction bound and its equality cases apply to these lifts. The clone construction is an analytical observation, not a polynomial-time step on binary input. Here is a direct derivation of the needed criterion.

Normalize the masses to sum to one and replace \(f\) by \(|f|\). A nonconstant input has a nonempty proper high set \(S=\{i: f_i>\sum_j w_jf_j\}\) in the normalized notation. If \(t\) is its normalized mass and \(A,B\) are the \(L^2\) lengths on \(S,S^c\), Cauchy–Schwarz bounds the squared mean by \((\sqrt{t}A+\sqrt{1-t}B)^2\). The squared output norm is therefore at most the quadratic form of
\[
\mathcal B(t)=\begin{pmatrix}
1+t(1-t)&(1-t)\sqrt{t(1-t)}\\
(1-t)\sqrt{t(1-t)}&(1-t)^2
\end{pmatrix}
\]
on \((A,B)\). The lower right entry of \((4/3)I-\mathcal B(t)\) is strictly positive and its determinant is \((t-1/3)^2\). Hence the squared norm ratio is at most \(4/3\) and can be equal to it only if \(t=1/3\). Constant inputs have ratio one, and compactness of the finite-dimensional unit sphere ensures that the operator norm is attained. Conversely, if \(S\) has mass \(W/3\), the input taking value \(4\) on \(S\) and \(1\) elsewhere has mean \(2\) and squared norm ratio \(4/3\). Thus the equality decision is precisely whether a subset of the original, undivided vertices has mass \(W/3\).

## Complexity proof

The subset certificate gives membership in NP by exact integer arithmetic. To reduce positive-integer SUBSET SUM, take a list \(a_1,\ldots,a_n\) of total \(A\) and a target \(0<T\le A\); trivial out-of-range targets can be mapped to fixed yes- or no-instances. Define \(L=2A+1\). Use the mass list
\[
(a_1,\ldots,a_n,\ L-T,\ 2L-A+T).
\]
All entries are positive, their total is \(3L\), and the last mass exceeds \(L\). The original masses total \(A<L\). Any subset of mass \(L\) must include the next-to-last mass and exclude the last mass, leaving exactly target \(T\) to be furnished by the original weights. Conversely, a subset of the original masses summing to \(T\) can be extended by \(L-T\) to mass \(L\). The binary encoding length of the output is polynomial in the input length.

For the pseudo-polynomial procedure, return no if \(3\) does not divide \(W\). Otherwise initialize only sum zero as attainable and, for each weight, update the attainable sums up to \(W/3\) in descending order. The target bit records exactly the desired equality. The result neither asserts hardness of approximation nor uses a graph expanded to \(W\) vertices in the reduction or the decision procedure.
