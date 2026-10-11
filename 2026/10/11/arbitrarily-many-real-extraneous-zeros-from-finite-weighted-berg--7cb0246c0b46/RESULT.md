# Arbitrarily many real extraneous zeros from finite weighted-Bergman zero sets
## Finding
For every \(\alpha>1\) and every integer \(N\geq1\), there is a finite conjugation-invariant set \(A\subset\mathbb D\setminus\mathbb R\) such that the reproducing kernel \(K_A(\cdot,0)\) of the zero-based invariant subspace \(I_A\subset A^2_\alpha\) has at least \(N\) distinct real extraneous zeros in \((0,1)\).

Here \(I_A=\{f\in A^2_\alpha:f(a)=0\text{ for every }a\in A\}\). A zero of \(K_A(\cdot,0)\) is extraneous when it is not a common zero of \(I_A\).

## Assumptions and scope
The space \(A^2_\alpha\) has norm
\[
\|f\|_\alpha^2=(\alpha+1)\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\alpha\,dA(z),\qquad \alpha>1.
\]
The claim is existential for each finite \(N\). No effective bound on \(|A|\), no minimum-cardinality statement, no simplicity claim, and no assertion that one fixed finite set has infinitely many extraneous zeros are made.

## Proof
Lin, Xu and Yu obtain, for each \(\alpha>1\), a limiting real kernel satisfying
\[
K_\tau(x)=e^{-s_0x}P(x)+O(e^{-bx})\qquad(x\to+\infty),
\]
where \(0<s_0<b\) and \(P\) is a nonzero real finite trigonometric sum with distinct nonzero frequencies. Their Lemma 4.3 gives \(\liminf P<0\). Applying the same lemma to \(-P\) gives \(\limsup P>0\). Hence positive and negative values of \(P\), each bounded away from zero, occur arbitrarily far to the right. Since
\[
e^{s_0x}K_\tau(x)=P(x)+O(e^{-(b-s_0)x}),
\]
the same is true for the sign of \(K_\tau\) for sufficiently large selected points.

Given \(N\geq1\), choose \(0<x_0<\cdots<x_N\) so that the signs of \(K_\tau(x_j)\) alternate. The focal paper's Theorem 4.6 gives uniform convergence \(K_h(x,0)\to K_\tau(x)\) on compact real intervals, so one sufficiently small \(h\) preserves all \(N+1\) signs. For this fixed \(h\), its Lemma 5.2 gives \(K_{h,M}(x_j,0)\to K_h(x_j,0)\) for the finite truncation kernels. One sufficiently large \(M\) therefore preserves all signs simultaneously. Conjugation invariance makes \(K_{h,M}(x,0)\) real on the real axis, so continuity gives at least one zero in each disjoint interval \((x_{j-1},x_j)\).

Set \(A=\psi(\Lambda_{h,M})\), with \(\psi(x)=\tanh(x/2)\) on the real axis. The focal paper proves that \(A\) is finite, conjugation-invariant and disjoint from \(\mathbb R\), and that
\[
K_{h,M}(x,0)=J_\alpha(x)J_\alpha(0)K_A(\psi(x),0),
\]
where the multiplier is positive for real \(x\). Thus the zeros map to \(N\) distinct points of \((0,1)\). Because \(A\cap\mathbb R=\varnothing\), the polynomial \(\prod_{a\in A}(z-a)\) belongs to \(I_A\) and is nonzero at every real point. Hence all these real kernel zeros are extraneous.

## Verification
The proof is symbolic. The nonstandard inputs inspected in the public v1 full text are the residue asymptotic above, compact-uniform convergence of \(K_h\), convergence of finite-truncation kernels, and the conformal kernel identity. No numerical experiment, finite enumeration, or computer certificate is used. Only finitely many sign probes are transferred for each prescribed \(N\).

## Relationship to prior work
The focal paper proves existence of one finite zero set with one real extraneous zero for every \(\alpha>1\). Its proof derives the oscillatory leading term \(P\) but uses only its negative side. The new step uses both signs and transfers an arbitrary finite alternating sign pattern through the same two limiting procedures. Gu and Park prove a complementary small-disk positive result for finite zero-based subspaces. Hedenmalm and Perdomo study extraneous zeros in the canonical-divisor/prescribed-curvature framework. No inspected source or database hit supplied the arbitrary finite multiplicity statement.

## Limitations
No effective truncation size is obtained. The minimum number of prescribed zeros needed to force \(N\) extraneous zeros is not determined, and simplicity is not asserted. An older equivalent theorem under canonical-divisor or extremal-function terminology remains a residual literature risk.

## References
1. Z. Lin, S. Xu, T. Yu, *The Critical Value for the Beurling-Type Theorem in Weighted Bergman Spaces*, arXiv:2609.36723v1, 29 September 2026. https://arxiv.org/abs/2609.36723
2. C. Gu, J. Park, *Finite zero-based invariant subspaces of the shift operator on reproducing kernel spaces*, Complex Variables and Elliptic Equations 67 (2022), 2519--2544. https://doi.org/10.1080/17476933.2021.1931850
3. H. Hedenmalm, Y. Perdomo, *Mean value surfaces with prescribed curvature form*, J. Math. Pures Appl. 83 (2004), 1075--1107; arXiv:math/0406344. https://arxiv.org/abs/math/0406344
