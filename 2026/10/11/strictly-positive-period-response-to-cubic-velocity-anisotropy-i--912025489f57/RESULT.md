# Strictly positive period response to cubic-velocity anisotropy in a hybrid oscillator

## Finding
For each \(q>0\), consider the real cubic planar vector field
\[
\dot x=y,\qquad \dot y=-x+qy-x^2y-\beta y^3,
\]
where \(\beta\) varies near \(1\). At \(\beta=1\), the circle \(x^2+y^2=q\) is an attracting hyperbolic limit cycle whose minimal period, in the original physical time, is \(2\pi\). Denote by \(\Gamma_{q,\beta}\) its unique nearby analytic periodic continuation, and by \(T(q,\beta)\) its minimal original-time period. Then for **every** \(q>0\),
\[
\boxed{\left.\frac{\partial T(q,\beta)}{\partial\beta}\right|_{\beta=1}=\int_0^{2\pi}\sin^2\phi\,w_q(\phi)^2\,d\phi>0,}
\]
where \(w_q\) is the unique smooth \(\pi\)-periodic solution of
\[
w_q'(\phi)+2q\sin^2\phi\,w_q(\phi)=q\sin(2\phi).
\]
In particular, for each fixed \(q>0\), increasing the cubic-velocity damping coefficient \(\beta\) sufficiently slightly above \(1\) increases the physical period, and the frequency \(2\pi/T(q,\beta)\) has a strictly negative derivative there.

The response has an exact small-amplitude scale:
\[
\boxed{\left.\frac{\partial T}{\partial\beta}\right|_{\beta=1}=\frac{\pi}{16}q^2+O(q^3)\qquad(q\downarrow0).}
\]
Thus the first-order perturbation of the period is strictly positive at every positive orbit amplitude, but its coefficient vanishes quadratically in the squared radius as the Hopf threshold is approached.

## Assumptions and scope
The parameter \(q\) is a fixed **strictly positive** real number and \(\beta\) lies in a possibly \(q\)-dependent open interval containing \(1\). The continuation is locally unique among periodic orbits in a small tubular neighborhood of the circular cycle. The theorem does not assert global uniqueness of all periodic orbits for parameters away from \(1\), nor monotonicity over a finite or global range of \(\beta\). The period is measured with respect to the original time of the displayed system, without orbital time reparametrization. The small-amplitude expansion concerns the derivative at \(\beta=1\) as \(q\downarrow0\), not a joint uniform expansion for arbitrary parameter variations.

## Proof
**1. Exact polar reduction and the reference cycle.** Put \(\delta=\beta-1\), \(x=r\cos\phi\) and \(y=-r\sin\phi\), with \(r>0\) and \(\phi\) increasing clockwise. Define
\[
S(r,\phi,\delta)=-q+r^2\bigl(1+\delta\sin^2\phi\bigr).
\]
Direct substitution, with no change of the time variable, gives
\[
\dot r=-rS\sin^2\phi,\qquad
\dot\phi=1-S\sin\phi\cos\phi.
\]
For \(\delta=0\) and \(r=\sqrt q\), we have \(S=0\), hence \(\dot r=0\), \(\dot\phi=1\). Radial linearization along this orbit satisfies
\[
\dot\eta=-2q\sin^2\phi\,\eta,
\]
and its multiplier after one circuit is
\[
\rho=\exp\!\left(-2q\int_0^{2\pi}\sin^2\phi\,d\phi\right)=e^{-2\pi q}\in(0,1).
\]
The Poincaré return map is analytic near this orbit. Since \(\rho\ne1\), the analytic implicit-function theorem gives a unique local analytic continuation \(r_{q,\delta}(\phi)\) that is positive and \(2\pi\)-periodic; nearby \(\dot\phi>0\), so the orbit remains a simple one-turn cycle and its period is analytic in \(\delta\).

**2. Linearized radial graph.** Expand in \(C^1\) periodic functions:
\[
r_{q,\delta}(\phi)=\sqrt q+\delta v_q(\phi)+O_q(\delta^2).
\]
Using \(dr/d\phi=\dot r/\dot\phi\), the coefficient of \(\delta\) obeys
\[
v_q'=-\sqrt q\sin^2\phi\Bigl(2\sqrt q\,v_q+q\sin^2\phi\Bigr).
\]
Set
\[
w_q(\phi)=2\sqrt q\,v_q(\phi)+q\sin^2\phi.
\]
Then
\[
w_q'+2q\sin^2\phi\,w_q=q\sin(2\phi).
\]
Because the homogeneous multiplier on \([0,\pi]\) is \(e^{-\pi q}\ne1\), this scalar equation has exactly one \(\pi\)-periodic solution. Consequently the unique \(2\pi\)-periodic solution induced by the orbit is precisely this \(\pi\)-periodic solution. Explicitly,
\[
w_q(\phi)=\frac{q}{1-e^{-\pi q}}\int_{\phi-\pi}^{\phi}
\exp\!\left(-2q\int_s^{\phi}\sin^2u\,du\right)\sin(2s)\,ds.
\]
This is also a fully specified convergent quadrature for the derivative.

**3. Strict sign identity.** The original-time period is
\[
T(q,1+\delta)=\int_0^{2\pi}\frac{d\phi}{1-S(r_{q,\delta}(\phi),\phi,\delta)\sin\phi\cos\phi}.
\]
On the orbit \(S=\delta w_q+O_q(\delta^2)\). Therefore
\[
\left.\partial_\beta T(q,\beta)\right|_{\beta=1}
=\int_0^{2\pi}w_q\sin\phi\cos\phi\,d\phi
=\frac12\int_0^{2\pi}w_q\sin(2\phi)\,d\phi.
\]
Multiplying the differential equation for \(w_q\) by \(w_q\), integrating over \([0,2\pi]\), and using periodicity gives
\[
2q\int_0^{2\pi}\sin^2\phi\,w_q^2\,d\phi
=q\int_0^{2\pi}w_q\sin(2\phi)\,d\phi.
\]
Thus the asserted nonnegative quadratic identity holds. It is **strictly** positive: otherwise \(\sin\phi\,w_q(\phi)\) would vanish identically, hence by continuity \(w_q\equiv0\), contradicting the nonzero forcing \(q\sin2\phi\).

**4. Sharp weak-amplitude scale.** Write \(w_q=qz_q\). Then
\[
z_q'+2q\sin^2\phi\,z_q=\sin(2\phi),\qquad
\int_0^{\pi}\sin^2\phi\,z_q(\phi)\,d\phi=0.
\]
The integral condition follows by integrating the \(w_q\)-equation over a period. The explicit periodic Green-function formula in step 2 (its numerator and denominator both vanish to first order at \(q=0\), with cancellation of the zero mean forcing) ensures \(z_q\) has a smooth extension to \(q=0\) and \(z_q=z_0+O(q)\) uniformly on \([0,2\pi]\). The limiting equation and weighted mean condition are
\[
z_0'=\sin(2\phi),\qquad
\int_0^\pi\sin^2\phi\,z_0\,d\phi=0,
\]
whose unique solution is
\[
z_0(\phi)=-\frac14-\frac12\cos(2\phi).
\]
Elementary trigonometric integration now yields
\[
\int_0^{2\pi}\sin^2\phi\,z_0(\phi)^2\,d\phi=\frac{\pi}{16}.
\]
Substituting \(w_q=qz_q\) in the quadratic identity completes the proof of the \(\frac\pi{16}q^2+O(q^3)\) law.

## Verification
The accompanying standalone `verify_period.py` uses standard-library Runge–Kutta integration of the linear periodic boundary-value equation. At multiple strictly positive \(q\), it compares the two algebraically equal expressions
\[
\int_0^{2\pi}\sin^2\phi\,w_q^2\,d\phi
\quad\text{and}\quad
\frac12\int_0^{2\pi}w_q\sin(2\phi)\,d\phi
\]
and checks positivity and the predicted \(q\downarrow0\) limit numerically. These finite tests check implementation and constants but do not replace the all-parameter analytic proof.

## Relationship to prior work
Chen and Xiao's 2023 paper develops existence and uniqueness criteria for hybrid oscillators, and Chen, Wang and Zhang's 2024 paper establishes the algebraic-limit-cycle classification of the exact polynomial family above, including its \(\beta=1\), \(\alpha<0\) circular cycle after setting \(q=-\alpha\). Their existence and classification statements are credited. Chen, Tang and Xiao's 2021 work concerns global phase portraits and orbit amplitudes. The present claim instead concerns the **signed derivative of minimal period with respect to the cubic-velocity coefficient** on the dynamically continued periodic orbit, including the positive-square identity and sharp weak-amplitude coefficient. The source papers' full manuscripts were not all accessible in the consulted sources; their indexed reviews and available abstracts cannot exclude an unexamined earlier equivalent formula.

## Limitations
The result is local in the anisotropy coefficient \(\beta\) for each positive \(q\), and the neighborhood need not be uniform near \(q=0\). It does not treat finite changes of \(\beta\), possible additional limit cycles, or a global frequency law. No claim of absolute publication priority or independent validation is made. Numerical quadrature alone is not treated as a proof of strict positivity.

## References
1. H. Chen and D. Xiao, “On the existence and uniqueness of limit cycles for hybrid oscillators,” *Annali di Matematica Pura ed Applicata* 202 (2023), 2049–2071, DOI: 10.1007/s10231-023-01312-3; first published online 9 February 2023. Publisher abstract and bibliography: https://link.springer.com/article/10.1007/s10231-023-01312-3.
2. H. Chen, L. Wang and X. Zhang, “A necessary and sufficient condition on algebraic limit cycles of a hybrid van der Pol-Rayleigh oscillator,” *Journal of Differential Equations* 406 (2024), 255–275, DOI: 10.1016/j.jde.2024.06.005. Indexed mathematical review: https://portal.mardi4nfdi.de/wiki/A_necessary_and_sufficient_condition_on_algebraic_limit_cycles_of_a_hybrid_van_der_Pol-Rayleigh_oscillator.
3. H. Chen, Y. Tang and D. Xiao, “Global dynamics of hybrid van der Pol–Rayleigh oscillators,” *Physica D* 428 (2021), article 133021, DOI: 10.1016/j.physd.2021.133021.
