# Distinct matching-edge deletion thresholds for total resistance and weighted spanning-tree design

## Finding
Let \(m\ge2\) be an integer. In the complete graph on \(2m\) labeled vertices fix a perfect matching. All matching edges cost \(P>0\) per unit conductance, and all other edges cost \(Q>0\). Choose every nonnegative edge conductance independently, subject to total price \(B>0\) and connected positive-conductance support. Two natural global design objectives are (A) minimize the sum \(\mathcal K=\sum_{i<j}R_{ij}\) of pairwise effective resistances and (D) maximize the weighted spanning-tree enumerator \(\mathcal T=\sum_{T}\prod_{e\in T}w_e\). Each has a unique *unrestricted* global optimizer.

Write \(r=P/Q\), \(k=m-1\), and
\[
r_D=\frac{2m}{2m-1},\qquad r_A=\frac{2m^2}{2m^2-2m+1}.
\]
Every optimizer gives weight \(a\) to every matching edge and weight \(b>0\) to every other edge. Let \(t=a/b\). The exact optimal ratios are
\[
t_A=\begin{cases}m\sqrt{2/r-1}-(m-1),&0<r<r_A,\\0,&r\ge r_A,\end{cases}
\qquad
 t_D=\begin{cases}2m/r-(2m-1),&0<r<r_D,\\0,&r\ge r_D.\end{cases}
\]
For either objective the corresponding weights follow uniquely from
\[
b=\frac{B}{m(Pt+2(m-1)Q)},\qquad a=tb.
\]
Their deletion thresholds are **strictly ordered** for every \(m\ge2\):
\[
1<r_D<r_A<2,\quad
r_A-r_D=\frac{2m(m-1)}{(2m-1)(2m^2-2m+1)}>0.
\]
Thus, precisely for \(r_D\le r<r_A\), the D-optimal network deletes the whole matching while the A-optimal network retains all matching edges. Both maintain every nonmatching edge.

The sharp critical-price scaling is \(r=1+\gamma/m\), with fixed real \(\gamma\), for which
\[
\lim_{m\to\infty}t_A=\max\{0,1-\gamma\},\qquad
\lim_{m\to\infty}t_D=\max\{0,1-2\gamma\}.
\]
In particular the deletion boundaries occur at distinct first-order surcharges \(\gamma=1\) and \(\gamma=1/2\).

## Assumptions and scope
All graphs are finite, undirected and loopless. Resistance uses the ordinary weighted combinatorial Laplacian and its Moore–Penrose inverse. If the positive-weight subgraph is disconnected, define \(\mathcal K=+\infty\) and \(\mathcal T=0\). The budget is an equality, with independent individual-edge decisions; no symmetry of the variables is assumed in advance. The ratio \(r\) is dimensionless. A unique optimizer is asserted for each objective, not a common optimizer across objectives.

## Proof
**1. Existence, unrestricted uniqueness and forced symmetry.** Let \(L(w)=\sum_e w_e v_ev_e^\mathsf T\), where \(v_e\) is the signed edge incidence vector. On the orthogonal complement of the constant vector, write \(H(w)=U^\mathsf TL(w)U\). For connected support, \(H\) is positive definite. The map from individual edge weights to \(H\) is injective: if two such Laplacians agree on the orthogonal complement of constants, they agree everywhere, and the negative off-diagonal entries recover each conductance. Consequently \(\operatorname{tr}H^{-1}\) is strictly convex, and \(\log\det H\) is strictly concave, in the full independent weight vector on connected feasible weights. For instance, in a nonzero symmetric matrix direction \(E\),
\[
\frac{d^2}{ds^2}\operatorname{tr}(H+sE)^{-1}\bigg|_{s=0}
=2\operatorname{tr}(H^{-1}EH^{-1}EH^{-1})>0,
\]
and
\[
\frac{d^2}{ds^2}\log\det(H+sE)\bigg|_{s=0}
=-\operatorname{tr}(H^{-1}EH^{-1}E)<0.
\]
The fixed-price simplex is compact, and a connected equal-weight allocation is feasible. Along approaches to disconnected supports \(\mathcal K\) diverges and \(\mathcal T\) vanishes, so both extrema exist and are connected. Strictness gives uniqueness even on boundary faces. The group permuting the \(m\) matched pairs and swapping their two endpoints preserves prices and both objectives, acts transitively on all matching edges and separately on all nonmatching edges. Uniqueness therefore forces exactly two weights \(a,b\). Since positive matching edges alone would leave \(m\) disconnected components, \(b>0\).

**2. Exact spectrum and objective formulas.** Put \(n=2m\). In terms of the Laplacian \(L_M\) of the unit matching,
\[
L=b(nI-J)+(a-b)L_M.
\]
Its eigenvalues are \(0\) once, \(nb\) with multiplicity \(m-1\) on pair-constant mean-zero vectors, and \(2((m-1)b+a)\) with multiplicity \(m\) on pair-antisymmetric vectors. There are \(m\) matching edges and \(2m(m-1)\) other edges; hence
\[
mPa+2m(m-1)Qb=B.
\]
The matrix-tree identity and spectral resistance identity give
\[
\mathcal K=2m\left(\frac{m-1}{2mb}+\frac{m}{2((m-1)b+a)}\right),
\]
\[
\mathcal T=\frac{(2mb)^{m-1}[2((m-1)b+a)]^m}{2m}.
\]
For \(t=a/b\ge0\) and \(k=m-1\), substitute \(b=B/[m(Pt+2kQ)]\) to obtain
\[
\mathcal K(t)=\frac{mQ}{B}(rt+2k)\left(k+\frac{m^2}{k+t}\right),
\]
\[
\mathcal T(t)=\frac{(2m)^{m-1}2^m}{2m}
\left(\frac{B}{mQ}\right)^{2m-1}
\frac{(k+t)^m}{(rt+2k)^{2m-1}}.
\]
The last expression is exact, including the prefactor, since its total degree in conductances is \(2m-1\).

**3. A-optimal threshold.** Apart from the positive constant \(mQ/B\), the derivative of \(\mathcal K\) is
\[
\frac{d}{dt}\left[(rt+2k)\left(k+\frac{m^2}{k+t}\right)\right]
=k\left[r-\frac{m^2(2-r)}{(k+t)^2}\right].
\]
If \(r\ge2\) this is positive. If \(0<r<2\), it increases strictly in \(t\), crosses zero at \(t=m\sqrt{2/r-1}-k\) when this is positive, and otherwise is nonnegative from \(t=0\). Positivity of this root is equivalent to \(r<2m^2/(m^2+k^2)=r_A\). This proves the stated unique resistance optimizer and all equality cases.

**4. D-optimal threshold.** The derivative of the log of the \(t\)-dependent factor of \(\mathcal T\) has the sign of
\[
m(rt+2k)-(2m-1)r(k+t)
=k\bigl(2m-(2m-1)r-rt\bigr).
\]
It has a unique positive zero \(t=2m/r-(2m-1)\) if and only if \(r<r_D\); otherwise the spanning-tree objective decreases from \(t=0\). At \(t\to\infty\), the tree enumerator tends to zero, and the resistance objective diverges. This establishes both global maxima/minima and their ratios.

**5. Strict disagreement and critical scaling.** Direct subtraction gives the displayed strictly positive gap, and the inequalities \(1<r_D<r_A<2\) follow for \(m\ge2\). For \(r=1+\gamma/m\), expand \(2/r-1=1-2\gamma/m+O(m^{-2})\) and \(2m/r=2m-2\gamma+O(m^{-1})\). The positive-part formulas for \(t_A,t_D\) yield the two stated limits, including thresholds. No calculation for finitely many values of \(m\) substitutes for these algebraic arguments.

## Verification
The accompanying `verify.py` is standalone Python 3 using only the standard library. It checks the displayed spectral formulas against exact rational full Laplacian inverses and spanning-tree cofactors, exact derivative identities and threshold gaps, finite candidate optimizations, strict convexity inequalities on nonsymmetric perturbations, and scaling tests. Invoke `python3 verify.py` to reproduce `VERIFICATION_OK 1131 checks`. These tests are finite corroboration; unrestricted optimality and all integer-parameter assertions follow from the proof above, not from the tests.

## Relationship to prior work
Ghosh, Boyd and Saberi (2006 conference version; 2008 extended paper) established general convexity, resistance spectral formulas and global conductance allocation, and analytically solved trees, wheels and barbell examples. These foundations are used rather than claimed as new. Klee and Stamps (2019) discuss weighted Matrix–Tree identities and edge-weight factorization, but not an optimized price-dependent matching deletion boundary. Tovar et al. (2026) discuss general marginal-price support criteria for resistance design, not the two complete-graph matching thresholds here. A separate max-pair-resistance design for a priced matching on a complete graph has a different objective and does not supply either of the two formulas proved here; a matching design on a complete bipartite graph has a different adjacency structure.

## Limitations
This is a theorem about *linear* conductance prices and a complete graph with a perfect matching distinguished; it does not classify arbitrary price assignments, nonlinear costs, network augmentation with cardinality constraints, or directed networks. The two criteria are optimized separately. Literature searching and relevant-section full-text inspection cannot prove global novelty; specialized prior matching-weight optimization may exist. Reproducible computation is not independent formal or peer certification. Independent mathematical audit has not been performed.

## References
1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006 (Kyoto, July 24–28, 2006; session TuP12.2). https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf
2. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50 (2008), 37–66. https://stanford.edu/~boyd/papers/pdf/eff_res.pdf
3. S. Klee, M. T. Stamps, *Linear algebraic techniques for weighted spanning tree enumeration* (first posted February 27, 2019). https://arxiv.org/abs/1903.03575
4. H. Tovar et al., *Cost convexity controls the architecture of resistance-optimal networks* (first posted October 2, 2026). https://arxiv.org/abs/2610.03627
