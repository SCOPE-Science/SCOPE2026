# An \(\ell_\infty\)-spaceability dichotomy for nondifferentiable Lipschitz curves
## Finding
Let \(X\) be a real or complex quasi-Banach space. Write \(\operatorname{Lip}_0([0,1],X)\) for the linear space of Lipschitz maps \(f:[0,1]\to X\) with \(f(0)=0\), equipped with the Lipschitz quasi-norm, and write \(\operatorname{LipD}_0([0,1],X)\) for those curves that are differentiable almost everywhere.

There is a sharp dichotomy. If \(X\) is isomorphic to a Banach space with the Radon--Nikodym property, then
\[
\operatorname{LipD}_0([0,1],X)=\operatorname{Lip}_0([0,1],X).
\]
If \(X\) is not isomorphic to a Banach space with the Radon--Nikodym property, then there exists a closed linear subspace \(Y\subset\operatorname{Lip}_0([0,1],X)\), isomorphic to \(\ell_\infty\), such that
\[
Y\cap\operatorname{LipD}_0([0,1],X)=\{0\}.
\]
More strongly, every nonzero member of \(Y\) is nowhere differentiable on some nondegenerate open subinterval of \([0,1]\).

## Assumptions and scope
Fix a quasi-norm on \(X\). Choose a concavity constant \(\kappa\ge1\) such that
\[
\|x+y\|\le \kappa(\|x\|+\|y\|)\qquad(x,y\in X).
\]
The source theorem characterizes the positive alternative: every Lipschitz curve from the real line to \(X\) is differentiable almost everywhere, equivalently every such curve has at least one differentiability point, if and only if \(X\) is isomorphic to a Banach space with the Radon--Nikodym property. Its negation therefore supplies a Lipschitz curve with no differentiability point.

The result concerns differentiability of vector-valued Lipschitz curves and does not assert scalar differentiability, Fréchet differentiability of maps on higher-dimensional domains, or any norm-attainment property.

## Proof
Assume first that \(X\) is not isomorphic to a Banach space with the Radon--Nikodym property. By the cited characterization there is a Lipschitz map \(F:\mathbb R\to X\) that is differentiable at no point. Restrict it to \([0,1]\) and define
\[
G(t)=F(t)-F(0)-t(F(1)-F(0)).
\]
Then \(G(0)=G(1)=0\). Subtracting an affine function does not create differentiability, so \(G\) is nowhere differentiable on \((0,1)\). Put \(L=\operatorname{Lip}(G)>0\).

For each integer \(n\ge1\), set
\[
I_n=[2^{-(n+1)},2^{-n}],\qquad \lambda_n=2^{-(n+1)},
\]
and define a rescaled copy
\[
G_n(t)=
\begin{cases}
\lambda_n G\!\left(\dfrac{t-2^{-(n+1)}}{\lambda_n}\right),&t\in I_n,\\
0,&t\notin I_n.
\end{cases}
\]
Because \(G(0)=G(1)=0\), each copy vanishes at both endpoints of its support.

For \(a=(a_n)\in\ell_\infty\), define \(T(a):[0,1]\to X\) by
\[
T(a)(t)=a_nG_n(t)\quad(t\in I_n),
\]
and \(T(a)(t)=0\) off the union of the intervals. This is well-defined at shared endpoints and is linear in \(a\).

If \(s,t\) lie in the same \(I_n\), then
\[
\|T(a)(t)-T(a)(s)\|\le L\|a\|_\infty |t-s|.
\]
If they lie in different active intervals (or one lies in the zero region), choose zero endpoints \(u,v\) between them so that the two nonzero endpoint differences have total scalar length at most \(|t-s|\). The quasi-triangle inequality gives
\[
\|T(a)(t)-T(a)(s)\|
\le \kappa L\|a\|_\infty |t-s|.
\]
Thus
\[
\operatorname{Lip}(T(a))\le \kappa L\|a\|_\infty.
\]
On the other hand, restriction to \(I_n\) has Lipschitz constant exactly \(|a_n|L\). Taking the supremum over \(n\) yields
\[
L\|a\|_\infty\le \operatorname{Lip}(T(a))\le \kappa L\|a\|_\infty.
\]
Hence \(T\) is an isomorphic linear embedding. The lower estimate and completeness of \(\ell_\infty\) imply that its range \(Y=T(\ell_\infty)\) is closed.

Finally, if \(a\ne0\), choose \(n\) with \(a_n\ne0\). On the interior of \(I_n\), difference quotients of \(T(a)\) are exactly \(a_n\) times the corresponding rescaled difference quotients of \(G\). Differentiability of \(T(a)\) at any point of that interval would therefore imply differentiability of \(G\) at the corresponding point of \((0,1)\), a contradiction. Thus every nonzero \(T(a)\) is nowhere differentiable on an open interval of positive measure and so is not in \(\operatorname{LipD}_0([0,1],X)\).

If \(X\) is isomorphic to a Banach space with the Radon--Nikodym property, the positive alternative follows directly from the cited characterization, restricted from the real line to \([0,1]\).

## Verification
The construction is deterministic and symbolic. The crucial quantitative check is the two-sided estimate
\[
L\|a\|_\infty\le \operatorname{Lip}(T(a))\le \kappa L\|a\|_\infty.
\]
The lower bound is obtained independently on each support interval; it therefore remains valid when the supremum of \((|a_n|)\) is not attained. The cross-interval upper bound uses only one application of the quasi-triangle inequality and zero values at support endpoints. Closedness follows from the lower estimate rather than from an unproved closure claim. The nondifferentiability conclusion is local on an interval and is stronger than merely failing almost-everywhere differentiability.

No finite computation, numerical experiment, or exhaustion argument is used.

## Relationship to prior work
Albiac, Ansorena and Wald prove the exact differentiability/Radon--Nikodym characterization for quasi-Banach targets and, in the negative case, thereby provide a single nowhere differentiable Lipschitz curve. They also establish that the almost-everywhere differentiable curves form a closed subspace of the based Lipschitz-curve space. Their inspected text does not state lineability or spaceability of the complement.

Related 2026 work of Choi, Jung, Lee and Roldán proves large linear structures in complements of norm-attaining classes of scalar Lipschitz functions, including isometric copies of \(\ell_\infty\) in a different complement. Daniilidis, Deville and Tapia-García use disjoint-support constructions to obtain spaceability for a different scalar Lipschitz/subdifferential pathology. Those results motivate comparison but do not imply the present vector-valued differentiability statement.

The new point is the zero-versus-closed-\(\ell_\infty\) dichotomy for the differentiability complement itself, with every nonzero vector in the constructed subspace remaining bad on an entire interval.

## Limitations
The construction does not claim that every bad Lipschitz curve belongs to such a subspace, nor that the displayed \(\ell_\infty\) copy is complemented. It also does not identify the maximal algebraic dimension of the complement. Originality searches can miss older equivalent formulations under generic lineability/spaceability terminology; this remains the principal literature risk.

## References
1. F. Albiac, J. L. Ansorena and P. Wald, *Differentiability of Lipschitz curves in p-Banach spaces*, arXiv:2609.26992v1, first public 2026-09-22.
2. G. Choi, M. Jung, H. J. Lee and Ó. Roldán, *Linear structures of norm-attaining Lipschitz functions and their complements*, Nonlinear Analysis 267 (2026), 114063, doi:10.1016/j.na.2026.114063.
3. A. Daniilidis, R. Deville and S. Tapia-García, *All convex bodies are in the subdifferential of some everywhere differentiable locally Lipschitz function*, Proceedings of the London Mathematical Society 129 (2024), e70007, doi:10.1112/plms.70007.
