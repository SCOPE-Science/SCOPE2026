# Gaussian anisotropy has a sharp \(q=n\) centro-sectional phase transition
## Finding
Let \(n\ge2\), \(1\le m\le n-1\), and let \(H\) be a nonzero real symmetric \(n\times n\) matrix with \(\operatorname{tr}H=0\). For the determinant-preserving Gaussian precision path \(A_t=e^{tH}\), \(f_t(x)=\exp(-\tfrac12 x^T A_t x)\), and the centro-sectional functional \(\widetilde\Psi_{m,q}\) of Böröczky--Hu--Liu, one has, for \(q\ne0\),
\[
\widetilde\Psi_{m,q}(f_0)=(2\pi)^{mq/2},\qquad
\frac{d}{dt}\widetilde\Psi_{m,q}(f_t)\bigg|_{t=0}=0,
\]
and
\[
\frac{d^2}{dt^2}\widetilde\Psi_{m,q}(f_t)\bigg|_{t=0}
=(2\pi)^{mq/2}\frac{m(n-m)q(q-n)}{2n(n-1)(n+2)}\operatorname{tr}(H^2).
\]
For \(q=0\),
\[
\widetilde\Psi_{m,0}(f_0)=\frac m2\log(2\pi),\qquad
\frac{d}{dt}\widetilde\Psi_{m,0}(f_t)\bigg|_{t=0}=0,
\]
and
\[
\frac{d^2}{dt^2}\widetilde\Psi_{m,0}(f_t)\bigg|_{t=0}
=-\frac{m(n-m)}{2(n-1)(n+2)}\operatorname{tr}(H^2).
\]
Consequently, within the determinant-one centered Gaussian family, the isotropic Gaussian is a strict quadratic local maximum for \(q=0\) and \(0<q<n\), a strict quadratic local minimum for \(q<0\) and \(q>n\), and is quadratically degenerate at the affine exponent \(q=n\).

Thus the local anisotropy sign changes exactly at \(q=n\), independently of the section dimension \(m\). The coefficient is explicit and nonzero for every nonzero trace-free symmetric direction away from \(q=n\).

## Assumptions and scope
The Grassmannian \(G(n,m)\) carries Haar probability measure \(\nu_m\). For \(q\ne0\), the centro-sectional functional is
\[
\widetilde\Psi_{m,q}(f)=\int_{G(n,m)}\|f|_\xi\|_1^q\,d\nu_m(\xi),
\]
while for \(q=0\) it is
\[
\widetilde\Psi_{m,0}(f)=\int_{G(n,m)}\log\|f|_\xi\|_1\,d\nu_m(\xi).
\]
The Gaussian is written with a precision matrix: \(f_A(x)=\exp(-\tfrac12x^TAx)\). The path \(A_t=e^{tH}\) remains positive definite and satisfies \(\det A_t=1\) because \(\operatorname{tr}H=0\). The statement concerns the finite-dimensional manifold of centered determinant-one Gaussians; it does not assert a global extremum among all log-concave functions.

## Proof
Fix \(\xi\in G(n,m)\) and let \(U\) be an \(n\times m\) matrix with orthonormal columns spanning \(\xi\). Put \(P=UU^T\). Gaussian integration on \(\xi\) gives
\[
\|f_A|_\xi\|_1=(2\pi)^{m/2}\det(U^TAU)^{-1/2}.
\]
Set
\[
L_\xi(t)=\log\det(U^Te^{tH}U).
\]
At \(t=0\), ordinary matrix differentiation yields
\[
L_\xi'(0)=\operatorname{tr}(PH)
\]
and
\[
L_\xi''(0)=\operatorname{tr}(PH^2)-\operatorname{tr}(PHPH).
\]

It remains to average these two quantities over the Grassmannian. By orthogonal invariance, the second moment of the Haar rank-\(m\) projection has the form
\[
\mathbb E[P_{ij}P_{kl}]
=\alpha\,\delta_{ij}\delta_{kl}
+\beta(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).
\]
The identities \(\operatorname{tr}P=m\) and \(\operatorname{tr}P^2=m\) give
\[
\alpha=\frac{m(mn+m-2)}{n(n-1)(n+2)},\qquad
\beta=\frac{m(n-m)}{n(n-1)(n+2)}.
\]
For trace-free symmetric \(H\), contraction therefore gives
\[
\mathbb E(\operatorname{tr}PH)^2
=\frac{2m(n-m)}{n(n-1)(n+2)}\operatorname{tr}(H^2)
\]
and
\[
\mathbb E L_\xi''(0)
=\frac{m(n-m)}{(n-1)(n+2)}\operatorname{tr}(H^2).
\]

For \(q\ne0\), the integrand, after removing the constant \((2\pi)^{mq/2}\), is \(\exp(-qL_\xi(t)/2)\). Hence its first derivative averages to zero because \(\mathbb E P=(m/n)I\) and \(\operatorname{tr}H=0\), while its second derivative is
\[
\frac{q^2}4\mathbb E(L_\xi'(0))^2-\frac q2\mathbb E L_\xi''(0)
=\frac{m(n-m)q(q-n)}{2n(n-1)(n+2)}\operatorname{tr}(H^2).
\]
Multiplying by \((2\pi)^{mq/2}\) proves the \(q\ne0\) formula. For \(q=0\),
\[
\widetilde\Psi_{m,0}(f_t)
=\frac m2\log(2\pi)-\frac12\mathbb E L_\xi(t),
\]
which gives the stated second derivative directly. Since \(m(n-m)>0\) and \(\operatorname{tr}(H^2)>0\) for nonzero symmetric \(H\), the sign classification follows.

## Verification
The standalone checker `artifacts/verify.py` verifies with exact rational arithmetic the invariant-tensor coefficients, the two Grassmannian contractions, and the factorization of the Hessian coefficient into \(q(q-n)\) for a grid of admissible symbolic integer parameters. It was replayed from the packaged bytes and returned `VERIFY_OK`. The checker is an algebraic consistency check; the proof above, not finite testing, establishes the universal statement.

## Relationship to prior work
Böröczky, Hu, and Liu introduced the \((m,q)\) centro-sectional functionals and their variational theory in arXiv:2609.18553v1. Their paper identifies \(q=n\) with the affine-quermassintegral direction inherited from earlier functional work, but its text does not provide this determinant-one Gaussian Hessian or the all-\(q\) sign diagram. Tziotziou's arXiv:2503.21494v1 develops functional affine and dual affine quermassintegrals and records the volume-preserving invariance at the classical \(n\)-th section moment; it does not supply the \(q\)-parameter Gaussian second variation. Searches for the coefficient, Gaussian centro-sectional Hessians, Grassmannian determinant formulations, and the source identifier found no statement implying the displayed formula.

## Limitations
The result is local and second-order in Gaussian anisotropy. At \(q=n\) it proves vanishing of the quadratic form but makes no claim here about the first nonzero higher-order term or about global constancy. It also does not classify extrema outside the centered determinant-one Gaussian family. A residual literature risk is that the same Gaussian calculation may occur in an unindexed treatment of affine Grassmannian section moments, although no such source was found in the targeted searches and the checked sources do not state it.

## References
1. K. J. Böröczky, J. Hu, J. Liu, *Centro-sectional measures for log-concave functions*, arXiv:2609.18553v1, first public 2026-09-16.
2. N. Tziotziou, *Inequalities for sections and projections of log-concave functions*, arXiv:2503.21494v1; Journal of Geometric Analysis 36 (2026), Article 145.
