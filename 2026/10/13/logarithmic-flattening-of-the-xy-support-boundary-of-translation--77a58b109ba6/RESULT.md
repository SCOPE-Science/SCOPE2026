# Logarithmic flattening of the XY support boundary of translation-invariant reduced states
## Finding
Let
\[
H_0=\sigma_x\otimes\sigma_x+\sigma_y\otimes\sigma_y,
\qquad
H_1=-\sigma_x\otimes\sigma_x+\sigma_y\otimes\sigma_y,
\]
and project the translation-invariant two-site reduced-state set to
\[
\mathcal C=\left\{(a,b):a=\operatorname{tr}(\rho H_1),\ b=\operatorname{tr}(\rho H_0),\ \rho\in\operatorname{Red}_2\right\}.
\]
For the affine anisotropic XY interaction \(H_0+\gamma H_1\), Blakaj and Wolf identify the support function
\[
\epsilon(\gamma)=\min_{(a,b)\in\mathcal C}(b+\gamma a)
=-\frac1{4\pi}E\!\left(\sqrt{1-\gamma^2}\right),
\qquad -1<\gamma<1.
\]

Near the lower-boundary point exposed by \(H_0\), the boundary of \(\mathcal C\) is a graph \(b=g(a)\) with
\[
g(0)=-\frac1{4\pi}.
\]
It is \(C^2\) but not \(C^3\) at \(a=0\), and
\[
g''(a)\sim\frac{4\pi}{\log(1/|a|)}
\qquad(a\to0).
\]
Thus this projected reduced-state boundary becomes logarithmically flat at the isotropic XY point.

Equivalently,
\[
\epsilon(\gamma)
=-\frac1{4\pi}
-\frac{\gamma^2}{8\pi}\left(\log\frac4{|\gamma|}-\frac12\right)
-\frac{3\gamma^4}{64\pi}\left(\log\frac4{|\gamma|}-\frac{13}{12}\right)
+O\!\left(\gamma^6\log\frac1{|\gamma|}\right).
\]
Hence \(\epsilon\) is \(C^1\) but not \(C^2\) at \(\gamma=0\), so the analyticity assertion in Theorem 3 of the motivating paper is false on its stated interval.

The same logarithm gives a local proof of the paper's central non-semialgebraicity result. If \(\operatorname{Red}_2\) were semialgebraic, the source's Tarski--Seidenberg reduction would make \(\epsilon\) semialgebraic and therefore algebraic on some one-sided interval. Newton--Puiseux theory forbids logarithmic monomials in a local algebraic branch, contradicting the nonzero \(\gamma^2\log|\gamma|\) term.

## Assumptions and scope
The normalization of \(H_0\), \(H_1\), and \(\epsilon\) is exactly that of Eqs. (10)--(11) of Blakaj--Wolf. The planar set \(\mathcal C\) is only the two-observable linear projection of \(\operatorname{Red}_2\); no claim is made that this projection determines the full reduced-state set.

The result is local near the point exposed by \(H_0\). It does not claim that the complete elliptic-integral asymptotic is new, nor that the XY anisotropy transition is newly discovered. The contribution is the exact local boundary regularity of this reduced-state projection, the correction of the published analyticity assertion, and the resulting local semialgebraicity obstruction.

## Proof
Put
\[
k=\sqrt{1-\gamma^2},
\qquad
k'=\sqrt{1-k^2}=|\gamma|.
\]
DLMF 19.12.2 gives
\[
E(k)=1+\frac12\sum_{m=0}^{\infty}
\frac{(1/2)_m(3/2)_m}{(2)_m m!}(k')^{2m+2}
\left(\log\frac1{k'}+d(m)-\frac1{(2m+1)(2m+2)}\right),
\]
with
\[
d(0)=2\log2,
\qquad
d(m+1)=d(m)-\frac2{(2m+1)(2m+2)}.
\]
Hence
\[
E(k)=1+\frac12(k')^2\left(\log\frac4{k'}-\frac12\right)
+\frac3{16}(k')^4\left(\log\frac4{k'}-\frac{13}{12}\right)
+O\!\left((k')^6\log\frac1{k'}\right),
\]
which yields the displayed expansion for \(\epsilon\).

For \(\gamma>0\), let \(L=\log(4/\gamma)\). Then
\[
\epsilon'(\gamma)=-\frac{\gamma}{4\pi}(L-1)+O(\gamma^3L),
\]
\[
\epsilon''(\gamma)=-\frac1{4\pi}L+\frac1{2\pi}+O(\gamma^2L),
\]
and
\[
\epsilon'''(\gamma)=\frac1{4\pi\gamma}+O(\gamma L).
\]
Evenness gives the corresponding negative-side statements. Thus \(\epsilon'(0)=0\) but \(\epsilon''(\gamma)\to-\infty\).

Set
\[
a(\gamma)=\epsilon'(\gamma),
\qquad
b(\gamma)=\epsilon(\gamma)-\gamma\epsilon'(\gamma).
\]
For sufficiently small nonzero \(\gamma\), \(\epsilon''(\gamma)<0\), so \(a(\gamma)\) is strictly monotone. Differentiability of the support function fixes the first coordinate of every minimizing point as \(a(\gamma)\), and the supporting equation fixes the second as \(b(\gamma)\). Hence these exposed points form the local lower boundary, written \(b=g(a)\), with
\[
g'(a(\gamma))=-\gamma,
\qquad
g''(a(\gamma))=-\frac1{\epsilon''(\gamma)}.
\]
Moreover,
\[
|a(\gamma)|\sim\frac{|\gamma|}{4\pi}\log\frac4{|\gamma|},
\qquad
\log\frac1{|a(\gamma)|}\sim\log\frac4{|\gamma|}.
\]
Therefore
\[
g''(a)\sim\frac{4\pi}{\log(1/|a|)}\to0.
\]
Also \(g'(a)/a=-\gamma/a\to0\), so \(g''(0)=0\) and \(g\) is \(C^2\) at zero. On the punctured neighborhood,
\[
g'''(a(\gamma))
=\frac{\epsilon'''(\gamma)}{\epsilon''(\gamma)^3}
\sim-\frac{16\pi^2}{\gamma L^3}
\qquad(\gamma\downarrow0),
\]
whose magnitude diverges. Thus \(g\) is not \(C^3\).

Finally, if \(\operatorname{Red}_2\) were semialgebraic, the quantified minimization in the source would make the graph of \(\epsilon\) semialgebraic, hence piecewise algebraic. On some \((0,\delta)\), \(\epsilon\) would lie on an algebraic plane curve. Newton--Puiseux then gives a local Puiseux expansion after finite ramification, with no logarithmic monomial, contradicting the exact \(\gamma^2\log\gamma\) term.

## Verification
The accompanying `artifacts/verify.py` evaluates the exact source integral by composite Simpson quadrature at several small positive anisotropies. It confirms the two-term DLMF expansion on the predicted \(O(\gamma^6\log(1/\gamma))\) remainder scale and checks the leading dual-curvature scale.

These finite calculations are corroborative only. The infinite statements follow from the convergent DLMF expansion, exact convex duality, and Newton--Puiseux theory.

## Relationship to prior work
The motivating paper proves that semialgebraicity of \(\operatorname{Red}_d\) would force polynomial-family ground-state energies to be semialgebraic and piecewise algebraic. Its Theorem 3 then states that the anisotropic-XY energy is analytic and transcendental, using the elliptic representation above. The endpoint expansion shows that the analyticity portion is incompatible with that same formula.

The elliptic expansion itself is classical and tabulated in DLMF. Older and later XY-chain literature also treats \(\gamma=0\) as an anisotropy-transition point, so no novelty is claimed for the physical criticality. Searches for the reduced-state paper together with boundary geometry, curvature, Legendre-transform, correction, logarithmic singularity, and Puiseux language located no statement of the \(C^2\)-but-not-\(C^3\) projected-boundary law or its logarithmic flattening asymptotic.

## Limitations
The theorem describes one natural two-dimensional projection of \(\operatorname{Red}_2\), not the complete local geometry of the full reduced-state set. The quantity \(g''\) is graph-coordinate curvature in the explicitly defined observable coordinates, not an affine-invariant Euclidean curvature.

The exact special-function asymptotic and the physical anisotropy transition are prior knowledge. The scientific addition is the reduced-state boundary law and its use to correct and repair the cited argument.

## References
1. V. Blakaj and M. M. Wolf, *On the set of reduced states of translation invariant, infinite quantum systems*, Letters in Mathematical Physics 114, 28 (2024), DOI: 10.1007/s11005-024-01776-1; arXiv:2308.14585.
2. NIST Digital Library of Mathematical Functions, §19.12, especially Eq. 19.12.2.
3. E. Lieb, T. Schultz, and D. Mattis, *Two soluble models of an antiferromagnetic chain*, Annals of Physics 16 (1961), 407--466, DOI: 10.1016/0003-4916(61)90115-4.
4. M. Zhong and P. Tong, *The Ising and anisotropy phase transitions of the periodic XY model in a transverse field*, Journal of Physics A 43 (2010), 505302, DOI: 10.1088/1751-8113/43/50/505302.
5. Newton--Puiseux theorem for local branches of algebraic plane curves.
