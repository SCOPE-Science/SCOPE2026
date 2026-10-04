# Corrected squared-soft-threshold duals in the dual-smoothing examples
## Finding
Let \(\lambda>0\) and
\[
h_\lambda(x)=\|x\|_1+\frac{\lambda}{2}\|x\|_2^2,\qquad x\in\mathbb R^m.
\]
Define coordinatewise soft thresholding and clipping by
\[
S(y)=\operatorname{sign}(y)\odot (|y|-\mathbf 1)_+,
\qquad
C(y)=y-S(y)=\operatorname{clip}(y,[-1,1]).
\]
Then the exact Fenchel conjugate is
\[
h_\lambda^*(y)=\frac{1}{2\lambda}\|S(y)\|_2^2,
\qquad
\nabla h_\lambda^*(y)=\frac1\lambda S(y).
\]
Section 3.3 of Rogozin--Nguyen--Zenuzagh--Gasnikov, arXiv:2512.08167v1, first writes a correct prox-value identity for this conjugate but then expands it with the final residual-square term having the opposite sign. If \(\widetilde h_\lambda^*\) denotes the displayed expanded expression there, then exactly
\[
\widetilde h_\lambda^*(y)
=
h_\lambda^*(y)+\frac1\lambda\|C(y)\|_2^2.
\]
Thus the displayed expression is not merely an alternative form: it is generally unequal to the conjugate and is nonconvex. In one dimension, on the positive half-line,
\[
\widetilde h_\lambda^*(t)=
\begin{cases}
 t^2/\lambda,&0\le t\le1,\\
 (t-1)^2/(2\lambda)+1/\lambda,&t\ge1,
\end{cases}
\]
so the one-sided derivatives at \(t=1\) are \(2/\lambda\) and \(0\), a downward jump that a convex function cannot have.

Consequently, after the same harmless positive scaling by \(\lambda\) used in the paper, the regularized decentralized basis-pursuit dual should be
\[
\min_{z:\,Wz=0}
\left\{
\frac12\|S(A^{\mathsf T}z)\|_2^2-\lambda\langle z,b\rangle
\right\},
\]
and the subsequent regularized consensus example with the same \(\ell_1\)-plus-quadratic term should use
\[
\min_{z,u:\,Wu+A^{\mathsf T}z=0}
\left\{
\frac12\|S(z)\|_2^2+\lambda\langle z,b\rangle
\right\}.
\]
The abstract duality and complexity results do not require alteration: they are stated in terms of the true Fenchel conjugate rather than the erroneous expanded display.

## Assumptions and scope
The statement is finite-dimensional and assumes only \(\lambda>0\). Absolute value, sign, positive part, soft thresholding, and clipping are all applied coordinatewise. The source comparison concerns arXiv:2512.08167v1, first public on 2025-12-09. Bibliographic metadata derived from zbMATH lists MSC 90C25 first and 90C46 second; the present result is therefore assigned primary MSC 90C25.

The claim is specifically about the expanded Section 3.3 formulas obtained from \(h_\lambda^*\). It does not assert that the paper's general duality lemmas, APAPC theorem, or complexity bounds are false. It also does not assert that the inaccessible final Springer chapter retains the same display.

## Proof
Because \(h_\lambda\) is separable, it suffices to solve the scalar maximization
\[
\sup_{x\in\mathbb R}\left\{yx-|x|-\frac\lambda2x^2\right\}.
\]
If \(|y|\le1\), the subgradient condition at \(x=0\) is \(y\in[-1,1]\), hence the maximum value is \(0\). If \(y>1\), the unique maximizer satisfies \(y-1-\lambda x=0\), so \(x=(y-1)/\lambda\) and the maximum value is \((y-1)^2/(2\lambda)\). If \(y<-1\), the unique maximizer is \(x=(y+1)/\lambda\) and the value is \((|y|-1)^2/(2\lambda)\). Summing coordinates yields
\[
h_\lambda^*(y)=\frac1{2\lambda}\|S(y)\|_2^2.
\]
The gradient formula follows coordinatewise. Since soft thresholding is nonexpansive, \(\nabla h_\lambda^*\) is \(1/\lambda\)-Lipschitz, as required by conjugacy of a \(\lambda\)-strongly convex function.

For the comparison with the source display, write \(C(y)=y-S(y)\). The prox-value identity on the same source page gives
\[
h_\lambda^*(y)
=
\frac{\|y\|_2^2}{2\lambda}
-
\frac{\|S(y)\|_1}{\lambda}
-
\frac{\|C(y)\|_2^2}{2\lambda}.
\]
The displayed expansion in arXiv:2512.08167v1 has a plus sign before the last term. Subtracting the correct identity from that display gives exactly \(\lambda^{-1}\|C(y)\|_2^2\). The scalar piecewise form above follows immediately. Its left derivative at \(1\) is \(2/\lambda\) and its right derivative is \(0\); convex one-dimensional functions have nondecreasing one-sided slopes, so the printed expression is nonconvex and therefore cannot be a Fenchel conjugate.

Finally, Lemma 1 of the source writes the coupled-constraint dual as \(h_\lambda^*(A^{\mathsf T}z)-\langle z,b\rangle\) subject to \(Wz=0\), and the consensus dual as \(h_\lambda^*(z)+\langle z,b\rangle\) subject to \(Wu+A^{\mathsf T}z=0\). Substituting the exact conjugate and multiplying each objective by the positive scalar \(\lambda\) gives the two corrected displayed forms stated above.

## Verification
The accompanying `verify.py` uses exact rational arithmetic. For several positive rational \(\lambda\) and values on both sides of the threshold, it verifies the scalar optimality condition, equality between the maximizing value and \(\|S(y)\|^2/(2\lambda)\), and the exact defect
\[
\widetilde h_\lambda^*(y)-h_\lambda^*(y)=\frac{C(y)^2}{\lambda}.
\]
It also checks the exact witness \(\lambda=1,y=2\), where the printed expression equals \(3/2\) while the conjugate equals \(1/2\), and checks the one-sided derivative inequality at the threshold. The checker output is `VERIFY_OK`.

These finite checks supplement, but do not replace, the symbolic case proof above.

## Relationship to prior work
The source paper explicitly defines the relevant prox value and bases its dual-smoothing framework on the standard fact that a strongly convex function has a smooth Fenchel conjugate. Its Section 3.3 basis-pursuit calculation is therefore expected to produce a convex \(1/\lambda\)-smooth function. The correct formula is also consistent with the classical soft-thresholding proximal operator for the \(\ell_1\) norm described in the proximal-optimization literature.

Targeted searches for the paper title together with “Fenchel conjugate”, “basis pursuit”, “sign error”, “soft threshold”, and the equivalent squared-soft-threshold formulation did not locate a published erratum or an earlier source identifying this particular Section 3.3 discrepancy. The formula \(h_\lambda^*(y)=\|S(y)\|_2^2/(2\lambda)\) itself is standard convex analysis; originality claimed here is only the source-specific diagnosis, exact defect identity, nonconvexity witness, and corrected downstream dual displays.

## Limitations
The accessible full text inspected was arXiv:2512.08167v1. The Springer conference chapter corresponding to DOI 10.1007/978-3-032-15791-1_6 was bibliographically inspected, but its full text was not accessible, so it may contain a correction not present in the arXiv version. This is the main residual originality risk.

No claim is made about numerical performance of the corrected examples, about convergence under implementation errors, or about any theorem beyond the two explicit expanded examples. The correction is algebraic and exact for every finite dimension and every \(\lambda>0\).

## References
1. A. Rogozin, N. T. Nguyen, H. A. Zenuzagh, A. Gasnikov, “Dual Smoothing for Decentralized Optimization,” arXiv:2512.08167v1, 2025-12-09; Section 3.3, especially pp. 8–9.
2. A. Rogozin, N. T. Nguyen, H. A. Zenuzagh, A. Gasnikov, “Dual Smoothing for Decentralized Optimization,” in *Optimization and Applications*, LNCS 16426, pp. 76–87, 2026, DOI 10.1007/978-3-032-15791-1_6.
3. N. Parikh, S. Boyd, “Proximal Algorithms,” *Foundations and Trends in Optimization* 1(3), 2014, DOI 10.1561/2400000003.
4. P. L. Combettes, J.-C. Pesquet, “Proximal Thresholding Algorithm for Minimization over Orthonormal Bases,” *SIAM Journal on Optimization* 18(4), 2007, DOI 10.1137/060669498.
5. zbMATH Open record 8245939, surfaced through MaRDI metadata for the Springer chapter; MSC entries 90C25 and 90C46.
