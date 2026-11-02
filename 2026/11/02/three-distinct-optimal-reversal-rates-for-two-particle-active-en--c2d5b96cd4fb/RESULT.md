# Three distinct optimal reversal rates for two-particle active encounters on a ring

## Finding

For two independent equal-speed run-and-tumble particles on a circle, the time to their first meeting has **three strictly ordered and distinct optimal reversal rates**, depending on whether one minimizes mean encounter time, encounter-time variance, or squared coefficient of variation. Let \(L,v,\lambda>0\) be circumference, individual speed, and each particle's independent Poisson direction-reversal rate, and let \(r=\lambda L/v\). Initial positions are independent uniform and initial directions independent equiprobable signs. Then

\[
\mathbb E[T]=\frac{L}{v}\frac{r^2+6r+3}{12r},\qquad
\operatorname{Var}(T)=\frac{L^2}{v^2}\frac{7r^4+60r^3+150r^2+180r+135}{720r^2}.
\]

The squared coefficient of variation is
\[
C^2(r)=\frac{7r^4+60r^3+150r^2+180r+135}{5(r^2+6r+3)^2}.
\]
Each of these functions has exactly one minimum on \(r>0\), at \(r_{\rm mean}=\sqrt3\), \(r_{\rm variance}=1.92076451528871\ldots\), and \(r_{\rm relative}=2.40678279431903\ldots\), respectively. More precisely the last two are the unique positive roots of
\[
7r^4+30r^3-90r-135=0,\qquad r^4+6r^3-30r-45=0.
\]
Thus \(0<r_{\rm mean}<r_{\rm variance}<r_{\rm relative}\). Moreover, \(C^2\) decreases from \(3\) to a minimum strictly below \(1\) and increases toward \(7/5\), revealing an intermediate sub-Poissonian-reliability window despite the nonmonotonic first-passage risk.

## Assumptions and scope

The two particles have continuous trajectories on a circle of circumference \(L\), each moving with instantaneous velocity \(\pm v\). Each direction flips at independent rate \(\lambda>0\), independently of all other randomness. Contact ends the process at the first time the positions coincide. Positions at time zero are independently Haar-uniform on the circle, with independent fair initial signs. There are no interactions prior to contact, no finite body size, no translational diffusion, and no refractory tumbling duration. Means, variances, and optima are over both initial data and subsequent random motion.

Set dimensionless separation \(x=(X_2-X_1)\bmod L\) divided by \(L\), and dimensionless time \(vt/L\). States \(A,R,F_1,F_2\) have relative velocities \(-2,+2,0,0\); the two following states have identical conditional first- and second-moment functions. Every particle flips at dimensionless rate \(r\), yielding total flip rate \(2r\).

## Proof

First-passage moments are finite at every \(r>0\): from every separation and orientation, a finite prescribed pattern of direction reversals has uniformly positive probability of producing an approaching state with a sufficient uninterrupted run to contact within a fixed finite time. Compactness of the position circle and positivity of Poisson pattern probabilities give a geometric tail on successive blocks. The killed-process backward equations therefore have unique bounded solutions, and second moments solve the Poisson hierarchy.

Write \(m_A,m_R,m_F\) for dimensionless conditional means at separation \(0<x<1\). Direct first-step analysis yields
\[
m_A=x+\frac r2x(1-x),\qquad m_R=1-x+\frac r2x(1-x),\qquad m_F=\frac12+\frac r2x(1-x)+\frac1{2r}.
\]
These formulas are also immediate from the approaching and following first-passage identities in Slowman--Evans--Blythe (2016); they are established background, not the claimed new result.

Let \(M_A,M_R,M_F\) be the corresponding conditional second moments. Reflection gives \(M_R(x)=M_A(1-x)\). The second-moment backward equations, with incoming absorbing condition \(M_A(0)=0\), are
\[
-2M_A'(x)+2r(M_F(x)-M_A(x))=-2m_A(x),
\qquad r(M_A(x)+M_R(x)-2M_F(x))=-2m_F(x).
\]
Eliminating \(M_F\) gives
\[
M_F=\tfrac12(M_A+M_R)+m_F/r,\qquad
M_A'=m_A+m_F+\tfrac r2(M_A(1-x)-M_A(x)).
\]
Now define even and odd reflected pieces \(F(x)=\frac12(M_A(x)+M_A(1-x))\), \(G(x)=\frac12(M_A(x)-M_A(1-x))\), satisfying \(F(1-x)=F(x)\), \(G(1-x)=-G(x)\). Then
\[
G'=1+rx(1-x)+\frac1{2r},\qquad
F'=x-\frac12-rG.
\]
The conditions \(G(1/2)=0\) and \(M_A(0)=0\) determine both constants. Straight polynomial integration gives the exact conditional second moment
\[
M_A(x)=\frac{x\big(r^3x^3-2r^3x^2+r^3-4r^2x^2+6r^2+3rx+9r+6\big)}{12r}.
\]
Together with \(M_R(x)=M_A(1-x)\) and \(M_F=(M_A+M_R)/2+m_F/r\), average over uniform \(x\in(0,1)\) and four equiprobable initial orientations. This yields
\[
\mathbb E[(vT/L)^2]=\frac{r^4+10r^3+30r^2+30r+15}{60r^2},
\]
and subtracting the squared mean yields the variance above.

Differentiation gives
\[
\frac{d}{dr}\left[\frac{v^2}{L^2}\operatorname{Var}(T)\right]
=\frac{7r^4+30r^3-90r-135}{360r^3},\qquad
\frac{dC^2}{dr}=\frac{24(r^4+6r^3-30r-45)}{5(r^2+6r+3)^3}.
\]
Both numerator polynomials have exactly one positive root by Descartes' rule of signs and their opposite signs at \(r=0\) and \(r\to\infty\). The mean derivative has the unique zero \(\sqrt3\). At \(\sqrt3\), the variance-derivative numerator is exactly \(-72<0\), hence \(r_{\rm variance}>\sqrt3\). At the variance minimizer the mean is strictly increasing, so differentiating \(C^2=\operatorname{Var}(T)/(\mathbb ET)^2\) shows \((C^2)'<0\). Hence \(r_{\rm relative}>r_{\rm variance}\). At \(r=2\), \(C^2=\frac{1687}{1805}<1\), while its endpoint limits are \(3\) and \(7/5\). This proves the exact ordering and sub-Poissonian window.

## Verification

The supplied `CHECKER.py` independently discretizes the killed four-orientation generator on an \(N\)-site spatial grid. It solves the linear systems \((-Q)m=\mathbf1\), \((-Q)M=2m\) and compares averaged means and second moments against the continuum formulas for four physically distinct parameter sets and three mesh resolutions each. Errors decrease by approximately a factor of two under mesh doubling, as expected for the upwind scheme. Symbolic substitution of the displayed \(M_A\) and \(M_F\) into both backward equations gives identically zero residuals, with \(M_A(0)=0\). These checks corroborate, but do not substitute for, the analytic all-rate proof.

## Relationship to prior work

Slowman, Evans and Blythe (2016), Appendix B, equations (45)--(59), obtain the approaching and following **mean** collision times for the same continuum two-particle model, including a rate-independent special mean. The first-moment formulas used here are covered by that paper; they are not originality claims. The present claim is solely the second-moment/variance formulas and the three distinct global risk-optimal reversal rates, none of which is stated in the inspected paper. Angelani, Di Leonardo and Paoluzzi (2015) analyze mean first passage for one active particle in a finite interval with forces and chemotaxis, not two-particle collision-time risk. Mercado-Vásquez and Boyer (2021) analyze variance and relative variance for a *single* active particle with a stochastic target in a reflecting interval; their geometry and generator are different, and their optimizer statements do not imply this three-rate result. Mallmin, Blythe and Evans (2018) analyze stationary spectral dynamics of two *exclusion-interacting lattice particles*, providing related machinery but not the specified continuum absorbing first-encounter moment and risk optimization.

## Limitations

The theorem concerns two equal-speed independent one-dimensional active particles, exponential independent direction flips, instantaneous point contact, and uniform independent starting configurations. It does not cover correlated motion, unequal speeds, hard-core jamming *after* contact, random initial conditions other than stated, finite-duration tumbling, or the full collision-time law. A general unpublished first-passage transform could subsume the formulas; no historical novelty or independent audit is certified. Published neighboring mean formulas remain credited to their sources.

## References

1. A. B. Slowman, M. R. Evans, R. A. Blythe, *Jamming and Attraction of Interacting Run-and-Tumble Random Walkers*, arXiv:1601.00954 (first public 2016-01-05), especially Appendix B. https://arxiv.org/abs/1601.00954
2. L. Angelani, R. Di Leonardo, M. Paoluzzi, *First-passage time of run-and-tumble particles*, arXiv:1506.08046 (first public 2015-06-26). https://arxiv.org/abs/1506.08046
3. G. Mercado-Vásquez, D. Boyer, *First hitting times between a run-and-tumble particle and a stochastically-gated target*, arXiv:2102.11787 (2021). https://arxiv.org/abs/2102.11787
4. E. Mallmin, R. A. Blythe, M. R. Evans, *Exact spectral solution of two interacting run-and-tumble particles on a ring lattice*, arXiv:1810.00813 (2018). https://arxiv.org/abs/1810.00813
