# Correct threshold and endemic stability in a fractional SEIR specialization
## Finding
Sene and Mansal specialize their Caputo SEIAR system by setting
\[
\psi=0,\qquad \theta=0.
\]
The resulting four-dimensional epidemic subsystem is
\[
D^\alpha S=\Lambda-\mu S-nSI,
\]
\[
D^\alpha E=nSI-(\omega+\mu)E,
\]
\[
D^\alpha I=\omega E-(\tau+\mu)I,
\]
\[
D^\alpha R=\tau I-\mu R,
\]
with
\[
0<\alpha\le1.
\]

For this system, the exact threshold is
\[
\mathcal R_*=
\frac{n\Lambda\omega}
{\mu(\omega+\mu)(\tau+\mu)}.
\]
The paper instead prints
\[
\mathcal R_{\mathrm{src}}=
\frac{n\Lambda\omega}
{\mu^2(\omega+\tau+\mu)}.
\]
Their ratio is
\[
\frac{\mathcal R_{\mathrm{src}}}{\mathcal R_*}
=
1+\frac{\omega\tau}{\mu(\omega+\tau+\mu)}>1.
\]

The discrepancy changes invasion classification. With
\[
\mu=1,\qquad \omega=2,\qquad \tau=3,\qquad n=1,\qquad \Lambda=4,
\]
one obtains
\[
\mathcal R_*=\frac23<1
\]
but
\[
\mathcal R_{\mathrm{src}}=\frac43>1.
\]
The disease-free equilibrium is locally asymptotically stable in this example even though the printed threshold labels it supercritical.

The same corrected threshold controls biological feasibility of the endemic equilibrium. Whenever that equilibrium is feasible, its Jacobian is Hurwitz, so it is locally asymptotically stable for every commensurate Caputo order
\[
0<\alpha\le1.
\]

## Assumptions and scope
All epidemiological parameters
\[
\Lambda,\mu,n,\omega,\tau
\]
are strictly positive, and
\[
0<\alpha\le1.
\]
The result concerns only the paper's specialization
\[
\psi=0,\qquad\theta=0.
\]
It does not assert a corrected threshold for the full five-compartment model.

For a commensurate Caputo system, local asymptotic stability of a linearized equilibrium follows when every eigenvalue satisfies
\[
|\arg(\lambda)|>\frac{\alpha\pi}{2}.
\]
Every eigenvalue with strictly negative real part satisfies this condition for the stated range of \(\alpha\).

## Proof
The disease-free equilibrium is
\[
B_0=\left(\frac{\Lambda}{\mu},0,0,0\right).
\]
Its exposed-infectious Jacobian block is
\[
A_0=
\begin{pmatrix}
-(\omega+\mu)&n\Lambda/\mu\\
\omega&-(\tau+\mu)
\end{pmatrix}.
\]
Therefore
\[
\det(\lambda I-A_0)
=
\lambda^2+(\omega+\tau+2\mu)\lambda
+(\omega+\mu)(\tau+\mu)
-\frac{n\Lambda\omega}{\mu}.
\]
Defining
\[
\mathcal R_*=
\frac{n\Lambda\omega}
{\mu(\omega+\mu)(\tau+\mu)}
\]
gives
\[
\det(\lambda I-A_0)
=
\lambda^2+(\omega+\tau+2\mu)\lambda
+(\omega+\mu)(\tau+\mu)(1-\mathcal R_*).
\]
The two remaining eigenvalues of the four-dimensional Jacobian are both \(-\mu\).

If
\[
\mathcal R_*<1,
\]
the infected quadratic has positive linear and constant coefficients, hence both roots have negative real part. If
\[
\mathcal R_*>1,
\]
its constant term is negative, so one root is positive. At
\[
\mathcal R_*=1,
\]
zero is an eigenvalue.

The source's displayed nontrivial eigenvalues are equivalent to
\[
-\frac{\omega+\tau+2\mu}{2}
\pm
\frac12\sqrt{(\omega-\tau)^2+\frac{4n\Lambda\omega}{\mu}}.
\]
The plus root is negative exactly when
\[
(\omega-\tau)^2+\frac{4n\Lambda\omega}{\mu}
<
(\omega+\tau+2\mu)^2.
\]
The difference of the two squared terms is
\[
4(\omega+\mu)(\tau+\mu),
\]
so the exact condition is
\[
\frac{n\Lambda\omega}
{\mu(\omega+\mu)(\tau+\mu)}<1.
\]
Thus the algebra printed immediately before Equations (4.10)–(4.11) leads to \(\mathcal R_*\), not to the denominator printed there.

For the endemic equilibrium,
\[
S^*=\frac{(\omega+\mu)(\tau+\mu)}{n\omega},
\]
and
\[
I^*=
\frac{n\Lambda\omega-\mu(\omega+\mu)(\tau+\mu)}
{n(\omega+\mu)(\tau+\mu)}.
\]
The other nonzero infected and recovered coordinates are positive multiples of \(I^*\), so biological feasibility is equivalent to
\[
\mathcal R_*>1.
\]

Set
\[
a=\omega+\mu,\qquad b=\tau+\mu,\qquad c=nI^*>0.
\]
The recovered direction contributes the eigenvalue \(-\mu\). For the remaining three coordinates, direct determinant expansion gives
\[
p(\lambda)
=
\lambda^3+A\lambda^2+B\lambda+C,
\]
with
\[
A=\mu+c+a+b,\qquad
B=(\mu+c)(a+b),\qquad
C=abc.
\]
All are positive. Moreover,
\[
AB=(\mu+c+a+b)(\mu+c)(a+b)>abc=C,
\]
because \(\mu+c>c\) and
\[
(\mu+c+a+b)(a+b)>(a+b)^2\ge4ab>ab.
\]
The cubic Routh-Hurwitz criterion therefore places all roots in the open left half-plane. This proves local asymptotic stability of the feasible endemic equilibrium for every
\[
0<\alpha\le1.
\]

## Verification
The bundled script `verification/verify.py` symbolically reconstructs the disease-free characteristic polynomial, simplifies the source's displayed square-root inequality, derives the endemic characteristic polynomial, and verifies two exact rational witnesses.

At
\[
\mu=1,\quad\omega=2,\quad\tau=3,\quad n=1,\quad\Lambda=4,
\]
it checks
\[
\mathcal R_*=\frac23,\qquad
\mathcal R_{\mathrm{src}}=\frac43.
\]
At
\[
\Lambda=8
\]
with the other parameters unchanged, it verifies a positive endemic infectious coordinate and the Routh-Hurwitz inequalities.

The general theorem is analytic and does not rely on finite simulation.

## Relationship to prior work
The standard next-generation approach of van den Driessche and Watmough gives
\[
\mathcal R_*=
\frac{n(\Lambda/\mu)\omega}
{(\omega+\mu)(\tau+\mu)},
\]
which agrees with the direct Jacobian calculation.

The motivating paper already prints the correct disease-free eigenvalue expression, but its subsequent threshold simplification omits the cross term
\[
\omega\tau.
\]
It also states that the endemic equilibrium is locally stable when its printed reproduction number is below one, whereas the printed endemic coordinates are biologically feasible only on the corrected supercritical side.

A separate source-specific analysis has identified a component-indexing error in the paper's numerical Volterra discretization. That numerical issue neither implies nor is implied by the reproduction-number and endemic-stability correction established here.

## Limitations
The theorem is local and does not prove global stability of either equilibrium.

At
\[
\mathcal R_*=1,
\]
the disease-free equilibrium is nonhyperbolic, so linearization does not settle nonlinear asymptotic behavior.

The result concerns only the four-dimensional specialization
\[
\psi=\theta=0.
\]
No claim is made here about the correct next-generation matrix or endemic stability of the full five-dimensional SEIAR model.

## References
1. N. Sene and F. Mansal, “Investigations on the fractional SEIAR epidemic model utilizing the Caputo derivative,” Palestine Journal of Mathematics 15(1) (2026), 200–213.
2. P. van den Driessche and J. Watmough, “Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission,” Mathematical Biosciences 180 (2002), 29–48. DOI: 10.1016/S0025-5564(02)00108-6.
3. D. Matignon, “Stability Results for Fractional Differential Equations with Applications to Control Processing,” Computational Engineering in Systems Applications 2 (1996), 963–968.
