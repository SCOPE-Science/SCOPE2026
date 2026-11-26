# Global oscillation threshold and exact critical relaxation in a three-node logistic cycle

## Finding
Consider the autonomous real ODE
\[
\dot x_i=\sigma\bigl(4(x_i-x_{i-1})\bigr)-v x_i,\qquad
\sigma(s)=\frac{1}{1+e^{-s}},\qquad i\in\mathbb Z/3\mathbb Z,\quad v\ge1.
\]
The predecessor of coordinate 1 is coordinate 3. Every real initial state has a bounded global forward solution, and the only equilibrium is \((1/(2v),1/(2v),1/(2v))\). Put \(d_i=x_i-x_{i-1}\) and \(R=\sum_i d_i^2\). Exactly synchronous solutions stay synchronous and converge exponentially for every \(v\ge1\). For every nonsynchronous start the following statements hold:

1. For \(v>3/2\), the solution converges to equilibrium and \(e^{2(v-3/2)t}R(t)\) has a finite, strictly positive limit depending on the initial state and \(v\).
2. At \(v=3/2\), the solution converges to equilibrium and \(\lim_{t\to\infty}tR(t)=1/2\).
3. For \(1\le v<3/2\), the distance from the solution to some nonconstant periodic orbit tends to zero. No uniqueness, hyperbolicity, or asymptotic phase is asserted.

The distinct contribution is the exact global transition in this one-parameter family, in particular the all-nonsynchronous orbit conclusion in the oscillatory range and the exact inverse-time law on the marginal boundary. Supercritical attraction itself follows from older general secant theory after passage to differences; the exact \(v=1\) example and numerical evidence of an attracting cycle were already given by Pokutnyi and Sadyrbaev. See below for the comparisons.

## Assumptions and scope
Time in the limits is the time in the displayed ODE, and \(v\) is fixed. The cube \([0,1/v]^3\) and the nonnegative orthant are each invariant for initial states in them; the conclusions quantify over all real initial states. The theorem concerns this exact signed, gain-four mathematical model, with identical node parameters and zero offsets.

## Proof
**Bounds and exact reduction.** The logistic forcing lies between 0 and 1, so integrating the scalar linear damping bounds each coordinate for all forward times and gives the invariance assertions. The vector field is globally Lipschitz. With \(\phi(s)=\sigma(4s)-1/2=\tfrac12\tanh(2s)\), subtracting consecutive equations gives
\[
\dot d_i=-v d_i+\phi(d_i)-\phi(d_{i-1}),\qquad \sum_i d_i=0.\tag{1}
\]
This is an autonomous planar reduction. The mean \(m=\tfrac13\sum_i x_i\) obeys \(\dot m=-vm+g(d)\), where \(g(d)=\tfrac13\sum_i\sigma(4d_i)\). For \(d=0\) this is \(\dot m=-vm+1/2\), which proves the assertion for synchronous starts.

**Unique equilibrium.** For \(s\ne0\), \(\phi(s)\) has the sign of \(s\) and \(|\phi(s)|<|s|\). Therefore \(vs-\phi(s)\) also has that sign when \(v\ge1\). At equilibrium of (1), \(v d_i-\phi(d_i)=-\phi(d_{i-1})\). A zero entry forces all entries to be zero; otherwise nonzero signs must alternate around a three-cycle, which is impossible. The mean equation at \(d=0\) now gives the unique full equilibrium.

**Exact radial identity.** Set \(\psi(s)=s-\phi(s)\), which is strictly increasing since \(\psi'(s)=\tanh^2(2s)\). Define
\[
T(d)=\sum_i d_i\psi(d_i)-\sum_i d_i\psi(d_{i-1}).
\]
The rearrangement inequality gives \(T\ge0\): pairing two strictly similarly ordered lists maximizes their sum of products. Equality for a cyclic shift requires that the shift preserve each value class, since any inverted unequal pair would strictly increase the sum upon uncrossing. A three-cycle preserves the value classes only when the triple is constant; in the plane this means \(d=0\). Using \(\sum_i d_id_{i-1}=-R/2\) on the plane, (1) yields
\[
\tfrac12\dot R=(\tfrac32-v)R-T(d).\tag{2}
\]
Nonsynchronous solutions have \(R>0\) at each finite time by uniqueness.

**Above threshold.** For \(a=v-3/2>0\), (2) gives \(R(t)\le R(0)e^{-2at}\). Since \(\psi(s)=O(s^3)\) near zero, \(T(d)/R=O(R)\) there. Thus the integral of \(T/R\) over forward time is finite, and
\[
\frac{d}{dt}\log(e^{2at}R(t))=-2T(d(t))/R(t)
\]
gives the finite positive limit. The mean equation converges to \(m=1/(2v)\) by variation of constants as its forcing tends to \(1/2\).

**At threshold.** Equation (2) is strictly dissipative off zero when \(v=3/2\). A positive limiting \(R\) would confine the solution to a compact annulus in the difference plane on which \(T\) has a positive minimum, contradicting (2). Thus \(R\to0\). The Taylor coefficient is \(\psi(s)=4s^3/3+O(s^5)\). To compute its contribution without any directional averaging, note that the three entries of \(d\) are roots of
\[
u^3-(R/2)u-d_1d_2d_3=0,
\]
since their sum is zero and their pairwise products sum to \(-R/2\). Hence \(d_i^3=(R/2)d_i+d_1d_2d_3\). Substituting into \(\sum_i d_i(d_i^3-d_{i-1}^3)\) gives exactly \(3R^2/4\). Consequently \(T(d)=R^2+O(R^3)\) uniformly as \(d\to0\), and \((1/R)'=2+O(R)\). Averaging in time yields \(tR\to1/2\), with convergence of the mean as above.

**Below threshold.** The linearization of (1) is \((1-v)I-P\) with \((Pd)_i=d_{i-1}\). Restricted to the plane, the eigenvalues of \(P\) are the two nontrivial cube roots of unity, so the eigenvalues of the flow linearization are \(3/2-v\pm i\sqrt3/2\). For \(v<3/2\), (2) and \(T=O(R^2)\) give \(\dot R\ge(3/2-v)R\) in a sufficiently small punctured disk. A nonsynchronous orbit exits that disk if started within it and cannot enter through its outward-pointing boundary. Thus its planar omega-limit set does not contain zero. It is compact and nonempty by boundedness, and there are no other equilibria. Poincaré–Bendixson gives a periodic orbit as the entire planar omega-limit set.

For a periodic difference trajectory of period \(P_0\), the stable scalar mean equation has a unique bounded entire solution, obtained by convolving its forcing with the kernel \(e^{-vs}\) on \(s\ge0\). This response is \(P_0\)-periodic; two distinct mean responses to the same forcing cannot both be bounded backwards because their difference is a nonzero multiple of \(e^{-vt}\). The full omega-limit set is compact and invariant in both time directions and projects onto the planar periodic orbit. Each of its entire trajectories must have that unique mean response over its difference trajectory. Hence the full omega-limit is contained in the periodic lift, and the distance to that lift tends to zero. This does not require selection of a phase.

## Verification
The proof computes the linearization and gives the polynomial identity for every triple of sum zero. The original standard-library `verify.py` supplies exact rational **grid** checks of the identity, sampled dissipation inequalities, and finite-time runs in three example regimes. Its linear-eigenvalue snippet inserts a formula rather than computing eigenvalues independently. These diagnostics neither certify the polynomial identity by themselves nor prove the limiting laws or periodicity.

## Relationship to prior work
Belgacem [1, §§2.3, 3.3, eqs. (9), (23)] treats the uncorrected signed weighted-sum logistic node response as well as a distinct bias-corrected formulation. The ODE here is in the uncorrected model class. Pokutnyi and Sadyrbaev [2, §3.2, eq. (21), Fig. 2] display exactly the present ODE at \(v=1\) by choosing \(k=1\) and zero thresholds; they report an attractive limit cycle numerically. Their subsequent \(v_3\)-variation fixes the other rates at 1 and adjusts thresholds, so it is not the common-rate transition considered here. The single-parameter example is credited as prior coverage, without a claim about a separate eligibility date.

Arcak and Sontag [3, §5, Corollary 3] give strict nonlinear secant stability on real state space. In (1) change the sign of \(d_2\) to put the loop into their one-negative-link form with self term \(a(s)=v s-\phi(s)\) and link term \(b(s)=\phi(s)\). For \(v>1\), \(\sup_{s\ne0} b(s)/a(s)=1/(v-1)\); the required sign conditions hold and the integral of \(b\) from zero is proper, since \(b(s)\to\pm1/2\) at the two ends. The strict three-node secant inequality is precisely \([1/(v-1)]^3<8\), or \(v>3/2\). Thus global attraction on the strict stable side is a specialization of that theorem, not an independent novelty claim. At equality the strict secant hypothesis fails; the criterion does not give the marginal amplitude or the oscillatory conclusion. Related passivity results are discussed in [4]. The present proof uses a specialized planar energy law to obtain the marginal coefficient and quantifiers on both sides of that boundary.

## Limitations
No result is stated for \(v<1\), other graph sizes or weights, delays or noise. The period, waveform, number, and hyperbolicity of the attracting periodic orbits are not classified. The result is a mathematical statement, not an experimental or physical validation. The prior-work comparison is limited to the passages inspected and does not certify historical priority.

## References
1. I. Belgacem, *A Bias-Corrected Weighted Logistic Model for Gene Regulatory Networks: Functional Equivalence with the Product-of-Logistics and Comparison with Weighted-Sum Formulations*, arXiv:2606.04709v1.
2. O. Pokutnyi and F. Sadyrbaev, *The influence of decay in dynamic models of gene regulatory networks*, arXiv:2610.18261v1, first posted October 13, 2026.
3. M. Arcak and E. D. Sontag, *Diagonal stability of a class of cyclic systems and its connection with the secant criterion*, Automatica 42 (2006), 1531–1537, DOI:10.1016/j.automatica.2006.04.009.
4. M. Arcak and E. D. Sontag, *A Passivity-Based Stability Criterion for a Class of Interconnected Systems and Applications to Biochemical Reaction Networks*, arXiv:0705.3188v1.
