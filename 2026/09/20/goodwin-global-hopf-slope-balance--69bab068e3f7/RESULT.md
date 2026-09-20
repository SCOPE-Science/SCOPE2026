# Global Hopf-slope balance for third-order feedback cycles and the Goodwin oscillator

## Result

Consider the scalar third-order feedback equation
\[
z'''+a z''+b z'+c z=g(z),
\]
where \(g\in C^1\). Every nonconstant \(P\)-periodic \(C^3\) solution satisfies the exact identities
\[
\int_0^P (z'')^2\,dt=b\int_0^P(z')^2\,dt
\tag{1}
\]
and
\[
\boxed{
\frac{\int_0^P[-g'(z(t))](z'(t))^2\,dt}
{\int_0^P(z'(t))^2\,dt}=ab-c.}
\tag{2}
\]
Thus the derivative-energy-weighted mean feedback slope of every finite-amplitude periodic orbit is exactly the third-order Hurwitz threshold \(ab-c\).

This extends from periodic orbits to compact recurrent statistics. In first-order coordinates
\[
\dot z=v,\qquad \dot v=w,\qquad
\dot w=-aw-bv-cz+g(z),
\]
every compactly supported invariant Borel probability measure \(\mu\) obeys
\[
\int w^2\,d\mu=b\int v^2\,d\mu,
\tag{3}
\]
\[
\boxed{\int[-g'(z)]v^2\,d\mu=(ab-c)\int v^2\,d\mu.}
\tag{4}
\]
If \(\int v^2d\mu=0\), invariance forces \(\mu\) to be supported on equilibria. Hence every non-equilibrium compact invariant statistical state has the same exact weighted-slope balance.

A useful consequence for a nonconstant periodic orbit is a slope-crossing obstruction. If \(g\) is not affine with slope \(-(ab-c)\) throughout the oscillation range \([z_{\min},z_{\max}]\), then
\[
\boxed{
\min_{[z_{\min},z_{\max}]}[-g']<ab-c<
\max_{[z_{\min},z_{\max}]}[-g'].}
\tag{5}
\]
In particular, a nonlinear periodic orbit cannot remain entirely on one strict side of the local Hopf slope surface.

## Goodwin specialization

For the three-stage Goodwin negative-feedback system
\[
\dot M=\alpha_1 f(R)-\beta_1M,\qquad
\dot P=\alpha_2M-\beta_2P,\qquad
\dot R=\alpha_3P-\beta_3R,
\]
with \(\alpha_i,\beta_i>0\) and \(f\in C^1\), elimination of \(M,P\) gives
\[
(D+\beta_1)(D+\beta_2)(D+\beta_3)R=Kf(R),
\qquad K=\alpha_1\alpha_2\alpha_3.
\]
Set
\[
a_1=\beta_1+\beta_2+\beta_3,\quad
 a_2=\beta_1\beta_2+\beta_1\beta_3+\beta_2\beta_3,\quad
 a_3=\beta_1\beta_2\beta_3.
\]
Then
\[
a_1a_2-a_3=(\beta_1+\beta_2)(\beta_1+\beta_3)(\beta_2+\beta_3)=:H.
\]
Therefore every nonconstant periodic Goodwin solution satisfies
\[
\boxed{
K\frac{\int_0^P[-f'(R)]\dot R^2\,dt}
{\int_0^P\dot R^2\,dt}=H.}
\tag{6}
\]
The same equality holds for every non-equilibrium compact invariant measure, with \(\dot R^2\) as the weight.

The quantity \(H/K\) is exactly the local Hopf critical feedback slope. Indeed, the linearization at an equilibrium \(R=R_*\) has characteristic polynomial
\[
\lambda^3+a_1\lambda^2+a_2\lambda+a_3-Kf'(R_*),
\]
and the Routh--Hurwitz equality for a purely imaginary pair is
\[
K[-f'(R_*)]=a_1a_2-a_3=H,
\]
with Hopf frequency \(\sqrt{a_2}\). Thus (6) identifies an exact global finite-amplitude continuation of the same slope threshold: every periodic orbit averages the instantaneous repression slope, with derivative-energy weighting, to the local Hopf value.

For a genuinely nonlinear repression law, every periodic Goodwin orbit therefore samples repression slopes both below and above \(H/K\). This remains true for large cycles and is independent of whether the surrounding equilibrium is locally stable or unstable.

## Proof

For a periodic solution, multiply the scalar equation by \(z'\) and integrate over one period. Periodicity and integration by parts give
\[
-\int(z'')^2+b\int(z')^2=0,
\]
which is (1). Multiplication by \(z''\) gives
\[
a\int(z'')^2-c\int(z')^2
=-\int g'(z)(z')^2.
\]
Substituting (1) yields (2).

For an invariant probability measure, invariance of the compact flow implies \(\int L\phi\,d\mu=0\) for each \(C^1\) observable used below. From \(\phi=v^2/2,z^2/2\), and a primitive of \(g\),
\[
\int vw\,d\mu=\int zv\,d\mu=\int g(z)v\,d\mu=0.
\]
Applying this to \(\phi=vw\) yields (3). Next,
\[
\int zw\,d\mu=-\int v^2\,d\mu,
\qquad
\int g(z)w\,d\mu=-\int g'(z)v^2\,d\mu,
\]
from \(\phi=zv\) and \(\phi=g(z)v\). Finally \(\phi=w^2/2\), followed by (3), gives (4).

For (5), subtract \(ab-c\) from \(-g'(z(t))\) in (2). If this continuous function had one sign throughout the oscillation range, the weighted integral could vanish only if it vanished wherever \(z'\ne0\). A nonconstant solution traverses every interior value of its range with \(z'\ne0\) somewhere; continuity then forces \(g'\equiv-(ab-c)\) on the whole range. Excluding that affine case makes both strict inequalities necessary.

## Relation to prior work

Forger (2011) already derived an exact Goodwin period formula by an inner-product/integration-by-parts argument and a corresponding minimum-period bound. Those period results are prior art and are not claimed here. The first identity (1), specialized to Goodwin, is precisely the type of Sobolev-norm relation underlying that result.

Chen and Shih (2026) give the current local Hopf calculation for the same three-stage genetic negative-feedback model. Their Routh--Hurwitz equality is exactly
\[
\alpha_1 f'(R_*)=-\frac{(\beta_1+\beta_2)(\beta_2+\beta_3)(\beta_1+\beta_3)}{\alpha_2\alpha_3},
\]
which is the local threshold identified globally by (6). Their work analyzes Hopf bifurcation, period changes, and stoichiometric balance; the present claim is the exact derivative-energy-weighted slope law for arbitrary finite-amplitude periodic or compact recurrent states.

Classical Goodwin literature includes Griffith (1968), Hastings--Tyson--Webster (1977), Hastings (1977), and Tyson--Othmer (1978), while Arcak--Sontag (2006) gives global sector/secant stability criteria for cyclic feedback systems. These sources make clear that local slope thresholds, existence/stability of oscillations in important parameter regimes, and sector-based global stability are established topics. The claimed contribution is limited to the exact global weighted-slope identity (2)/(4), its slope-crossing consequence, and the identification of its Goodwin constant with the local Hopf threshold.

## Verification

`artifacts/verify_identities.py` checks the algebraic factorization \(a_1a_2-a_3=H\) symbolically and numerically integrates the Goodwin example
\[
\dot M=\frac{100}{1+R^{12}}-M,\qquad \dot P=M-P,\qquad \dot R=P-R.
\]
The recorded cycle has period approximately \(4.2039784240\); numerical quadrature gives \(\int \ddot R^2/\int\dot R^2\approx3\) and \(100\int[-f'(R)]\dot R^2/\int\dot R^2\approx8\), matching \(a_2=3\) and \(H=8\). These numerical checks corroborate but do not replace the analytic proof.

## Scientific limitations

The identities are necessary constraints; they do not by themselves prove existence, uniqueness, or stability of a periodic orbit. The slope-crossing statement is strict only when the feedback law is not affine with critical slope on the full oscillation range. The invariant-measure statement assumes compact support so that the generator identities are justified without growth-at-infinity issues.

Originality is asserted only to the best of our knowledge. The multiplier argument is short, so an equivalent identity may exist in older third-order-ODE or biochemical-control literature under different notation. Hastings (1977) was inspected in full enough to confirm its focus on uniqueness and global orbital stability for a particular Goodwin system, but not every classical source was available in full. In particular, the full texts of Hastings--Tyson--Webster (1977) and Tyson--Othmer (1978) remain material residual coverage risks.

## References

1. D. B. Forger, *Signal processing in cellular clocks*, Proc. Natl. Acad. Sci. USA **108** (2011), 4281--4285. https://doi.org/10.1073/pnas.1004720108
2. K.-W. Chen and C.-W. Shih, *Stoichiometric balance and sustained rhythms*, J. Math. Biol. **93** (2026), article 4. https://doi.org/10.1007/s00285-026-02419-w
3. J. S. Griffith, *Mathematics of cellular control processes I. Negative feedback to one gene*, J. Theor. Biol. **20** (1968), 202--208. https://doi.org/10.1016/0022-5193(68)90189-6
4. S. P. Hastings, J. J. Tyson, D. Webster, *Existence of periodic solutions for negative feedback cellular control systems*, J. Differential Equations **25** (1977), 39--64. https://doi.org/10.1016/0022-0396(77)90179-6
5. S. P. Hastings, *On the uniqueness and global asymptotic stability of periodic solutions for a third order system*, Rocky Mountain J. Math. **7** (1977), 513--538.
6. J. J. Tyson and H. G. Othmer, *The dynamics of feedback control circuits in biochemical pathways*, Prog. Theor. Biol. **5** (1978), 1--62.
7. M. Arcak and E. D. Sontag, *Diagonal stability of a class of cyclic systems and its connection with the secant criterion*, Automatica **42** (2006), 1531--1537. https://doi.org/10.1016/j.automatica.2006.04.009
