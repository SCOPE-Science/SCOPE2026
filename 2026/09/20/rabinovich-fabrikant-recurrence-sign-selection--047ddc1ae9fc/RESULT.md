# Rabinovich--Fabrikant recurrence sign selection and mean-height law

Consider the Rabinovich--Fabrikant system
\[
\dot x=y(z-1+x^2)+\gamma x,\qquad
\dot y=x(3z+1-x^2)+\gamma y,\qquad
\dot z=-2z(\alpha+xy),
\tag{RF}
\]
with \(\alpha>0\) and \(\gamma\in\mathbb R\).

## Theorem

Let
\[
q=x^2+y^2,\qquad W=q+4z.
\]

1. **Exact balance and invariant half-spaces.**
   Along every solution,
   \[
   \dot W=2\gamma q-8\alpha z.
   \tag{1}
   \]
   Moreover \(z=0\) is invariant, and a trajectory starting with \(z\ne0\)
   keeps the sign of \(z\).

2. **Compact ergodic recurrence off the invariant plane.**
   Let \(\mu\) be a compactly supported ergodic invariant probability measure
   with \(\mu(\{z=0\})=0\). Then
   \[
   \int xy\,d\mu=-\alpha,
   \tag{2}
   \]
   and
   \[
   \boxed{
   \int z\,d\mu
   =\frac{\gamma}{4\alpha}\int(x^2+y^2)\,d\mu
   =\frac{\gamma}{2}
    +\frac{\gamma}{4\alpha}\int(x+y)^2\,d\mu.}
   \tag{3}
   \]
   Equivalently,
   \[
   \int(x-y)^2\,d\mu-\int(x+y)^2\,d\mu=4\alpha.
   \tag{4}
   \]
   Hence an ergodic compact recurrent state off \(z=0\) can lie only in
   \(z>0\) when \(\gamma>0\), and only in \(z<0\) when \(\gamma<0\).
   For \(\gamma=0\) there is no such compact ergodic invariant measure.

3. **Invariant-plane recurrence.**
   On \(z=0\),
   \[
   \dot q=2\gamma q.
   \tag{5}
   \]
   Consequently, if \(\gamma\ne0\), the only compactly supported invariant
   probability measure supported on \(z=0\) is the Dirac mass at the origin.

4. **Periodic-orbit corollary.**
   Every nonconstant periodic orbit with \(\gamma\ne0\) is disjoint from
   \(z=0\), has the same sign of \(z\) as \(\gamma\), and obeys
   \[
   \langle xy\rangle=-\alpha,\qquad
   \langle z\rangle=
   \frac{\gamma}{2}
   +\frac{\gamma}{4\alpha}\langle(x+y)^2\rangle.
   \tag{6}
   \]
   The second relation is strict away from equilibria:
   \[
   \gamma>0\Longrightarrow \langle z\rangle>\gamma/2,\qquad
   \gamma<0\Longrightarrow \langle z\rangle<\gamma/2.
   \tag{7}
   \]

5. **The zero-growth slice.**
   If \(\gamma=0\), every nonconstant periodic orbit is contained in
   \(z=0\). On this plane \(q=r^2\) is constant and, with
   \(x=r\cos\theta,\ y=r\sin\theta\),
   \[
   \dot\theta=1-r^2\cos^2\theta.
   \tag{8}
   \]
   Thus the complete family of nonconstant periodic orbits is
   \[
   x^2+y^2=r^2,\qquad z=0,\qquad 0<r<1,
   \tag{9}
   \]
   with exact minimal period
   \[
   \boxed{P(r)=\frac{2\pi}{\sqrt{1-r^2}}.}
   \tag{10}
   \]
   For \(r\ge1\), zeros of the angular velocity prevent a full rotation.

6. **A global exclusion region in the physical half-space.**
   If \(\gamma<0\), then every solution with \(z(0)\ge0\) exists for all
   positive time and converges exponentially to the origin. More precisely,
   with
   \[
   \kappa=\min\{2|\gamma|,2\alpha\},
   \]
   \[
   W(t)\le W(0)e^{-\kappa t}.
   \tag{11}
   \]
   Therefore the only compact invariant set contained in \(z\ge0\) is the
   origin.

## Proof

The third equation gives
\[
z(t)=z(0)\exp\!\left[-2\int_0^t(\alpha+x(s)y(s))\,ds\right],
\]
which proves invariance of \(z=0\) and sign preservation. Direct
differentiation gives
\[
\frac d{dt}(x^2+y^2+4z)=2\gamma(x^2+y^2)-8\alpha z,
\]
proving (1).

Let \(\mu\) satisfy the hypotheses in part 2. Since \(\mu\) is ergodic and
\(\{z>0\}\), \(\{z<0\}\) are invariant, one of them has full measure.
Choose a point that is both Birkhoff-generic for the continuous observable
\(xy\) and Poincare recurrent. It has \(z(0)\ne0\). Along the orbit,
\[
\log|z(T)|-\log|z(0)|
=-2\alpha T-2\int_0^Txy\,dt.
\tag{12}
\]
For a recurrence sequence \(T_n\to\infty\), the left side divided by
\(T_n\) tends to zero, while the time average on the right converges to
\(\int xy\,d\mu\). This proves (2).

Because \(W\) is smooth and bounded on the compact support of \(\mu\),
invariance gives \(\int \dot W\,d\mu=0\). Equation (1) then gives
\[
4\alpha\int z\,d\mu=\gamma\int q\,d\mu.
\tag{13}
\]
Using
\[
q=(x+y)^2-2xy
\]
and (2) yields (3); (4) follows similarly. The sign conclusions follow
because an ergodic measure off the plane has one strict sign of \(z\), while
the right side of (3) has the sign of \(\gamma\), and has magnitude at least
\(|\gamma|/2\) when \(\gamma\ne0\). If \(\gamma=0\), (13) would force
\(\int z\,d\mu=0\), impossible for a probability measure carried by either
strict half-space.

On \(z=0\), direct differentiation gives (5). For an invariant probability
measure on that plane,
\[
0=\int\dot q\,d\mu=2\gamma\int q\,d\mu.
\]
For \(\gamma\ne0\), nonnegativity of \(q\) forces \(q=0\) almost surely,
so the measure is the Dirac mass at the origin.

A nonconstant periodic orbit defines an ergodic invariant probability
measure on the orbit, giving (6) and the sign statement. Equality in (7)
would force \(x+y\equiv0\). On that set,
\[
\frac d{dt}(x+y)=-2x(x^2-z-1).
\]
A nonconstant periodic trajectory cannot pass through \(x=y=0\), so
\(z=x^2-1\) throughout. Compatibility of this relation with (RF) forces
\(x^2\) to be constant; the resulting trajectory is an equilibrium
(\(x^2=\alpha=1+\gamma/2,\ z=\gamma/2\), when those parameters are
compatible). Thus a nonconstant periodic orbit has strict inequality.

For \(\gamma=0\), part 2 excludes periodic orbits off \(z=0\). On the
plane, \(q\) is constant. Writing \(x=r\cos\theta,\ y=r\sin\theta\) gives
(8). If \(0<r<1\), the angular velocity is positive and one revolution has
period
\[
\int_0^{2\pi}\frac{d\theta}{1-r^2\cos^2\theta}
=\frac{2\pi}{\sqrt{1-r^2}}.
\]
If \(r=1\) there are angular equilibria at \(\theta=0,\pi\); if \(r>1\)
there are four angular equilibria. Hence no circle with \(r\ge1\) is a
nonconstant periodic orbit.

Finally suppose \(\gamma<0\) and \(z\ge0\). Then \(W=q+4z\ge0\), and (1)
gives
\[
\dot W=-2|\gamma|q-8\alpha z
\le-\min\{2|\gamma|,2\alpha\}W.
\]
Gronwall proves (11). The bound keeps the trajectory in a compact set for
all positive time, so finite-time blow-up is impossible, and
\(x,y,z\to0\) exponentially. A nontrivial compact invariant set in
\(z\ge0\) would contain a bounded complete trajectory, contradicting the
strict exponential decay of \(W\) in forward time unless \(W\equiv0\).

## Context and prior literature

Rabinovich and Fabrikant introduced the model in 1979. In the conservative
case \(\gamma=\alpha=0\), they already identified
\(x^2+y^2+4z\) as an energy integral and described \(z=0\) as the boundary
of the physical half-space. The present claim is not that this polynomial
combination is new; the contribution is the dissipative balance (1) joined
with the logarithmic \(z\)-identity to obtain the recurrent-measure law,
half-space selection, exact periodic constraints, and the global
\(\gamma<0,\ z\ge0\) exclusion theorem.

Danca and Chen (2004) and Danca, Feckan, Kuznetsov and Chen (2016) study
equilibria, bifurcations, invariant manifolds and many numerically observed
attractors. The latter explicitly records the reduced-plane identity
\(\dot q=2\gamma q\). Diab, Guirao and Vera analyze periodic orbits born
from zero-Hopf points by averaging theory. Turukina (2022) numerically maps
negative dissipation-parameter regimes, and Sajjad et al. (2026) perform a
statistical numerical parameter-space study. In the inspected statements
and full texts, none gives (2)--(4), the sign-selection theorem for compact
ergodic recurrence, (6)--(10), or (11).

## Limitations

- The invariant-measure theorem assumes compact support and ergodicity.
  General compactly supported invariant measures can be handled by ergodic
  decomposition, but the displayed formula is stated componentwise.
- The exponential convergence theorem requires \(\alpha>0,\gamma<0\) and
  initial data in \(z\ge0\). It does not classify the negative-\(z\)
  half-space or regimes with \(\alpha\le0\).
- No claim is made that the historic energy expression \(x^2+y^2+4z\), the
  invariant plane \(z=0\), or the reduced-plane identity by themselves are
  new.
- Originality is to the best of our knowledge. The literature search
  emphasized the original model, major numerical/bifurcation studies,
  periodic-orbit work, negative-parameter studies, and recent statistical
  parameter scans; unindexed or differently formulated results remain a
  residual risk.

## Reproducibility

`artifacts/verify_rf_identities.py` symbolically checks the polynomial
balance, the invariant-plane radial law, the derivative of \(x+y\) on
\(y=-x\), and the zero-growth angular equation. Its recorded output is in
`artifacts/verification.txt`.

## References

1. M. I. Rabinovich and A. L. Fabrikant, *Stochastic self-modulation of
   waves in nonequilibrium media*, Sov. Phys. JETP 50(2), 311--317 (1979).
   https://www.jetp.ras.ru/cgi-bin/dn/e_050_02_0311.pdf
2. M.-F. Danca and G. Chen, *Bifurcation and chaos in a complex model of
   dissipative medium*, Int. J. Bifurcation and Chaos 14 (2004), 3409--3447.
   https://doi.org/10.1142/S0218127404011430
3. M.-F. Danca, M. Feckan, N. Kuznetsov and G. Chen, *Looking more closely
   to the Rabinovich-Fabrikant system*, Int. J. Bifurcation and Chaos 26
   (2016), 1650038. https://doi.org/10.1142/S0218127416500383
4. Z. Diab, J. L. G. Guirao and J. A. Vera, *On the periodic structure of
   the Rabinovitch-Fabrikant system* (2015).
   https://jlguirao.es/panel/archivos/on_the_periodic_structure_of_the_rabinovitch_fabrikant_system.pdf
5. L. V. Turukina, *Dynamics of the Rabinovich--Fabrikant system and its
   generalized model in the case of negative values of parameters that have
   the meaning of dissipation coefficients*, Izvestiya VUZ. Applied
   Nonlinear Dynamics 30(6) (2022), 685--701.
   https://doi.org/10.18500/0869-6632-003015
6. H. Sajjad, A. Jhangeer, M. Imran and A. R. Ansari, *Robust dynamical
   behavior identification in the Rabinovich Fabrikant system using
   statistical measures*, AIMS Mathematics 11(4) (2026), 10716--10743.
   https://doi.org/10.3934/math.2026441
