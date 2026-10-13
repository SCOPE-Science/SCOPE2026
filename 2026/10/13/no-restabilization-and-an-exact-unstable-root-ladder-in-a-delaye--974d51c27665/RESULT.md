# No restabilization and an exact unstable-root ladder in a delayed invasive-species model

## Finding

For the rat-free equilibrium \(E_3\) in the delayed invasive-species model of Kovács and György, assume
\[
c<g,\qquad a<b,\qquad 0<h<\frac b3.
\]
The characteristic equation factors as
\[
(z-c+g)D(z,\tau)=0,
\]
where
\[
D(z,\tau)
=
z^2+az+ah+(b-2h)(z+a)e^{-z\tau}.
\]
The factor \(z-c+g\) is stable under \(c<g\).

Set
\[
B=b-2h,
\]
\[
\kappa=a(a-2h)-B^2,
\qquad
\zeta=a^2(3h-b)(b-h).
\]
Since \(0<h<b/3\),
\[
B>0,\qquad \zeta<0.
\]
The imaginary-frequency equation is
\[
\omega^4+\kappa\omega^2+\zeta=0,
\]
so it has exactly one positive solution
\[
\omega_H^2
=
\frac{-\kappa+\sqrt{\kappa^2-4\zeta}}2.
\]

Define
\[
\phi
=
\arccos\!\left(
-\frac{a^2h}{B(a^2+\omega_H^2)}
\right).
\]
Then the complete sequence of delays with imaginary characteristic roots is
\[
\boxed{
\tau_n
=
\frac{\phi+2\pi n}{\omega_H},
\qquad n=0,1,2,\ldots.
}
\]
At each \(\tau_n\), the only roots on the imaginary axis are the simple pair
\[
\pm i\omega_H.
\]

Every such crossing is from left to right. Therefore
\[
E_3
\]
is linearly asymptotically stable exactly for
\[
0\le\tau<\tau_0,
\]
loses hyperbolicity at
\[
\tau_0,
\]
and is unstable for every
\[
\tau>\tau_0.
\]
In particular, there is no restabilization at larger delay.

The result is sharper than a binary stability statement. If \(N_+(\tau)\) is the number of characteristic roots in the open right half-plane, counted with algebraic multiplicity, then
\[
N_+(\tau)=0
\]
for \(0\le\tau<\tau_0\), while
\[
N_+(\tau)=2(n+1)
\]
for
\[
\tau_n<\tau<\tau_{n+1}.
\]
At the crossing value \(\tau_n\), there are \(2n\) right-half-plane roots and the simple pair \(\pm i\omega_H\) on the boundary.

For the source's example
\[
a=0.03,\qquad b=1,\qquad h=0.1,
\]
one obtains
\[
\omega_H=0.8037274036\ldots,
\]
\[
\tau_0=1.9546057932\ldots,
\]
and the crossing spacing
\[
\tau_{n+1}-\tau_n
=
\frac{2\pi}{\omega_H}
=
7.8175576438\ldots.
\]
The first value agrees with the source's reported
\[
\tau_H\approx1.955.
\]

## Assumptions and scope

The claim concerns linear asymptotic stability of the boundary equilibrium \(E_3\) in the delayed system studied by the source.

The parameter assumptions are exactly
\[
c<g,\qquad a<b,\qquad 0<h<\frac b3,
\]
with the positive model parameters otherwise as in the source. These assumptions ensure that \(E_3\) exists, its rat-direction eigenvalue is stable, and the delay-dependent characteristic factor has a unique positive crossing frequency.

No claim is made here about orbital stability or criticality of the nonlinear periodic branches born at the crossings. The source computes a first Poincaré-Lyapunov coefficient for the first Hopf bifurcation; that nonlinear calculation is separate from the linear root-count classification proved here.

## Proof

Put
\[
B=b-2h.
\]
Under \(0<h<b/3\),
\[
B>h>0.
\]

For a purely imaginary root
\[
z=i\omega,\qquad \omega>0,
\]
the modulus condition
\[
|p(i\omega)|=|q(i\omega)|
\]
for
\[
p(z)=z^2+az+ah,
\qquad
q(z)=B(z+a)
\]
is
\[
\omega^4+\kappa\omega^2+\zeta=0.
\]
Because
\[
\zeta=a^2(3h-b)(b-h)<0,
\]
the quadratic in \(\omega^2\) has one positive and one negative root. Hence \(\omega_H\) is the unique positive crossing frequency.

Separating real and imaginary parts at \(\omega_H\) gives
\[
\cos(\omega_H\tau)
=
-\frac{a^2h}{B(a^2+\omega_H^2)}
\]
and
\[
\sin(\omega_H\tau)
=
\frac{\omega_H(a^2-ah+\omega_H^2)}
{B(a^2+\omega_H^2)}.
\]
The sine is positive. If \(a\ge h\), this is immediate. If \(a<h\), let
\[
y_0=a(h-a)>0
\]
and
\[
F(y)=y^2+\kappa y+\zeta.
\]
A direct substitution gives
\[
F(y_0)=ah(a^2-B^2)<0,
\]
because
\[
a<h<B.
\]
Since \(F(0)<0\) and \(F\) has a unique positive root
\[
\omega_H^2,
\]
we have
\[
y_0<\omega_H^2.
\]
Thus
\[
a^2-ah+\omega_H^2>0.
\]

Consequently the correct phase lies in \((0,\pi)\), and all phase repetitions are exactly
\[
\omega_H\tau_n=\phi+2\pi n.
\]
There are no other imaginary frequencies and
\[
D(0,\tau)=a(b-h)>0,
\]
so there are no zero-root crossings.

The source derives the crossing-direction criterion
\[
\operatorname{sign}\Re z'(\tau)
=
\operatorname{sign}\Phi'(\omega)
\]
at a simple imaginary crossing. Here
\[
\Phi'(\omega_H)
=
2\omega_H(2\omega_H^2+\kappa).
\]
Using the positive-root formula,
\[
2\omega_H^2+\kappa
=
\sqrt{\kappa^2-4\zeta}>0.
\]
Therefore every crossing at every \(\tau_n\) is left-to-right.

At \(\tau=0\), the equilibrium is stable under the stated assumptions, as established in the source. For a retarded characteristic equation, the finite number of roots in the open right half-plane is locally constant between imaginary-axis crossings. Each simple conjugate left-to-right crossing increases this count by two. Since the only crossings are the \(\tau_n\), the stated root-count ladder follows by induction. In particular, once the first pair crosses at \(\tau_0\), stability can never return.

## Verification

The bundled verifier reconstructs
\[
\kappa,\qquad \zeta,\qquad \omega_H,\qquad \phi,\qquad \tau_n
\]
from the source's numerical example using the printed characteristic equation.

For several crossing indices it directly evaluates
\[
D(i\omega_H,\tau_n)
\]
and checks that the residual is at floating-point roundoff. It also verifies the positive crossing-direction factor
\[
2\omega_H^2+\kappa
=
\sqrt{\kappa^2-4\zeta}
\]
and reproduces
\[
\tau_0=1.9546057932\ldots.
\]

The computation does not prove the universal statement. The proof is the exact modulus, phase, and crossing-direction argument above.

## Relationship to prior work

Kovács and György derive the same characteristic factor and show that under
\[
c<g,\qquad a<b,\qquad 0<h<\frac b3
\]
the equilibrium is stable for zero and small delay and eventually becomes unstable. Their Theorem 3.1 identifies the first Hopf value \(\tau_H\), proves a positive crossing direction there, and studies the nonlinear periodic branch. The paper does not state the complete sequence of imaginary-axis crossings, the absence of restabilization for every larger delay, or the exact number of unstable roots between crossings.

The general delay-root machinery used by the source goes back to Cooke and van den Driessche and to Boese. That theory supplies the framework for tracking roots as delay varies; the result here is the source-specific completion obtained from the special fact that this model's frequency equation has exactly one positive root and every phase repetition has the same crossing direction.

Targeted searches by DOI and title, by “stability switch”, “restabilization”, “all critical delays”, “unstable roots”, and by the explicit quasipolynomial did not locate a publication stating this complete classification for the model. The publisher currently lists no citing paper for the article.

## Limitations

The theorem is a linear spectral classification. It does not assert that every later imaginary crossing creates a stable periodic orbit, nor does it classify the nonlinear invariant sets after the first loss of equilibrium stability.

The unstable-root count uses standard spectral continuity for retarded functional differential equations; no claim is made for neutral equations.

An equivalent source-specific classification could exist under terminology not reached by the targeted searches.

## References

1. S. Kovács, S. György, “On a delayed invasive species model with harvesting,” Discrete and Continuous Dynamical Systems - B 29 (2024), 3297–3325. DOI: 10.3934/dcdsb.2024005.
2. F. G. Boese, “Stability with respect to the delay: On a paper of K. L. Cooke and P. van den Driessche,” Journal of Mathematical Analysis and Applications 228 (1998), 293–321. DOI: 10.1006/jmaa.1998.6109.
3. K. L. Cooke, P. van den Driessche, “On zeroes of some transcendental equations,” Funkcialaj Ekvacioj 29 (1986), 77–90.
