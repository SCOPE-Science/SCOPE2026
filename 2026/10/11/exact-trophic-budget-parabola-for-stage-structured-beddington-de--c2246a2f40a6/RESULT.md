# Exact trophic-budget parabola for stage-structured Beddington–DeAngelis recurrence
## Finding
Consider the dimensional stage-structured predator–prey system
\[
\dot x=r x\left(1-\frac{x}{k}\right)-\frac{a xz}{1+bx+cz},\qquad
\dot y=\frac{k_1a xz}{1+bx+cz}-(\alpha+d_1)y,\qquad
\dot z=\alpha y-d_2z,
\]
with \(r,k,a,b,c,k_1,\alpha,d_1,d_2>0\). Every compactly supported invariant probability measure \(\mu\) on the nonnegative octant satisfies
\[
\int \left(x-\frac{k}{2}\right)^2\,d\mu+
\frac{k(\alpha+d_1)d_2}{r\alpha k_1}\int z\,d\mu=\frac{k^2}{4}.
\]
Writing \(\bar x=\int x\,d\mu\), \(\bar z=\int z\,d\mu\), this is equivalently
\[
\operatorname{Var}_\mu(x)+\frac{k(\alpha+d_1)d_2}{r\alpha k_1}\bar z
=\bar x(k-\bar x).
\]
In particular,
\[
\bar z\le \frac{r\alpha k_1k}{4(\alpha+d_1)d_2}.
\]
Equality can occur only when \(\mu\) is supported on an equilibrium with \(x=k/2\). Hence every non-equilibrium ergodic recurrent state, including every nonconstant periodic orbit, satisfies the mature-predator mean bound strictly.

For the source values \(r=4\), \(k=30\), \(k_1=0.1\), \(\alpha=0.1\), \(d_1=0.08\), \(d_2=0.05\),
\[
\int (x-15)^2\,d\mu+\frac{27}{4}\int z\,d\mu=225,
\qquad
\bar z<\frac{100}{3}
\]
for every non-equilibrium ergodic recurrent state. The identity is independent of \(a,b,c\), so the same budget applies to all of the source's coexisting periodic branches as capture rate or mutual interference varies.

## Assumptions and scope
The claim concerns the autonomous dimensional system (3) printed by Feng and Jiang, with all nine parameters positive and state space restricted to the nonnegative octant. The invariant measure is assumed compactly supported; this is enough to justify integration of the generator applied to the linear function used below. No assertion is made about invariant measures outside the nonnegative octant, stochastic perturbations, delayed variants, or spatial extensions.

The source proves boundedness of positive trajectories through earlier work and studies existence, multiplicity, stability, and bifurcation of periodic orbits. The present statement is an exact stationary-statistics constraint and does not alter those existence results.

## Proof
Define the weighted trophic content
\[
\Phi(x,y,z)=x+\frac{y}{k_1}+\frac{\alpha+d_1}{\alpha k_1}z.
\]
Along every classical solution, substitution of the three differential equations gives
\[
\begin{aligned}
\dot\Phi
&=r x\left(1-\frac{x}{k}\right)-\frac{a xz}{1+bx+cz}
 +\frac1{k_1}\left(\frac{k_1a xz}{1+bx+cz}-(\alpha+d_1)y\right)\
&\quad+\frac{\alpha+d_1}{\alpha k_1}(\alpha y-d_2z)\
&=r x\left(1-\frac{x}{k}\right)-\frac{(\alpha+d_1)d_2}{\alpha k_1}z.
\end{aligned}
\]
Thus both the predation flux and the immature-to-mature transfer cancel exactly.

For a compactly supported invariant probability measure \(\mu\), invariance gives \(\int \dot\Phi\,d\mu=0\). Put
\[
C=\frac{(\alpha+d_1)d_2}{\alpha k_1}>0.
\]
Then
\[
C\bar z=r\int x\left(1-\frac{x}{k}\right)d\mu.
\]
Completing the square pointwise,
\[
x\left(1-\frac{x}{k}\right)=\frac{k}{4}-\frac1k\left(x-\frac{k}{2}\right)^2,
\]
which proves
\[
\int \left(x-\frac{k}{2}\right)^2d\mu+\frac{kC}{r}\bar z=\frac{k^2}{4}.
\]
Writing \(\int x^2d\mu=\bar x^2+\operatorname{Var}_\mu(x)\) yields the equivalent variance form.

Because \(z\ge0\), the completed-square identity gives the stated upper bound on \(\bar z\). If equality holds, then \(\int(x-k/2)^2d\mu=0\), so the support of \(\mu\) lies in \(x=k/2\). The support of an invariant measure is flow-invariant. On that plane the first component of the vector field must vanish at every support point, and \(z\mapsto a(k/2)z/(1+bk/2+cz)\) is strictly increasing for \(z\ge0\). Hence \(z\) is constant on the support. The third equation then forces \(y\) to be constant there as well. The support is therefore a single equilibrium. This proves strictness for every non-equilibrium ergodic recurrent state.

## Verification
A standalone symbolic checker in `verify.py` expands the derivative of \(\Phi\), verifies exact cancellation of the predation and maturation terms, verifies the completed-square rearrangement, and evaluates the source parameter specialization with rational arithmetic. It returns `VERIFY_OK` when all exact checks pass.

At the source parameter values, \(C=9/10\), \(kC/r=27/4\), and \(rk/(4C)=100/3\). The rounded equilibrium reported near \((9.1469,14.1289,28.2579)\) is numerically consistent with the exact budget to the accuracy expected from the displayed four-decimal coordinates; that numerical consistency is only a check, not part of the proof.

## Relationship to prior work
Feng and Jiang study this exact system's positive equilibrium, Hopf bifurcations, fold bifurcations of cycles, and regimes with at least two or three limit cycles. Their full article states the model and the parameter scaling explicitly and summarizes the bifurcation conclusions, but the inspected text does not state a stationary mean/variance identity of the form above.

Khajanchi's earlier analysis of the same dimensional model proves dissipativity using the different weighted sum \(k_1x+y+z\), whose derivative retains both predator mortality terms. That estimate supplies a global absorbing bound but does not imply the exact invariant-measure parabola, the variance penalty, or the parameter-only ceiling for the mature-predator mean. Conversely, the present identity is a stationary constraint and is not a replacement for the prior boundedness theorem.

Targeted semantic searches for stage-structured Beddington–DeAngelis mean budgets, prey-variance/mature-predator identities, stationary predator-mean bounds, and weighted-biomass coboundaries did not return an equivalent statement. The closest database results concern unrelated recurrence-balance laws in other flows or stage-structured threshold dynamics, and do not imply this claim.

## Limitations
The result does not prove existence, uniqueness, stability, or period of any recurrent state. It gives only stationary first/second-moment information. The strictness statement uses nonnegative-state dynamics and compact support. No claim is made that the mature-predator ceiling is attained for a given parameter set; equality is possible only if the system actually has an equilibrium at \(x=k/2\).

Novelty assessment is necessarily literature-bounded. The closest same-system article and the motivating full paper were inspected, and targeted semantic searches found no equivalent statement, but an older source under different notation could conceivably contain the same averaged identity.

## References
1. M. Feng and J. Jiang, “A stage structured predator-prey model with periodic orbits,” *Discrete and Continuous Dynamical Systems - B* 28 (2023), 2846–2883. DOI: 10.3934/dcdsb.2022195. Earliest verified public date used here: 2022-10-14.
2. S. Khajanchi, “Dynamic behavior of a Beddington–DeAngelis type stage structured predator–prey model,” *Applied Mathematics and Computation* 244 (2014), 344–360. DOI: 10.1016/j.amc.2014.06.109.
3. P. Georgescu and Y.-H. Hsieh, “Global Dynamics of a Predator-Prey Model with Stage Structure for the Predator,” *SIAM Journal on Applied Mathematics* 67 (2007), 1379–1395. DOI: 10.1137/060670377.
