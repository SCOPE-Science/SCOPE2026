# Exact mean-nullcline defect and fluctuation coupling in a fear–crowding predator–prey flow

## Finding
Consider the deterministic system
\[
\dot u=\frac{ru}{1+kv}-du-au^2-\frac{puv}{1+cu},
\qquad
\dot v=-mv^2+\frac{quv}{1+cu},
\]
with \(r,d,a,p,c,m,q,k>0\). Let \(\mu\) be any invariant Borel probability measure whose support is a compact subset of \((0,\infty)^2\), and define
\[
\bar u=\int u\,d\mu,
\qquad
\bar v=\int v\,d\mu.
\]
Then
\[
m\bar v=q\int \frac{u}{1+cu}\,d\mu,
\]
and the deviation of the mean point from the predator nullcline is exactly
\[
\frac{q\bar u}{1+c\bar u}-m\bar v
=
\frac{qc}{(1+c\bar u)^2}
\int \frac{(u-\bar u)^2}{1+cu}\,d\mu.
\]
There is also an exact fluctuation identity
\[
\operatorname{Cov}_\mu\!\left(v,\frac{qu}{1+cu}\right)
=m\operatorname{Var}_\mu(v).
\]
Therefore
\[
\bar v\le \frac{q\bar u}{m(1+c\bar u)},
\qquad
m^2\operatorname{Var}_\mu(v)\le q^2\operatorname{Var}_\mu(u).
\]
Equality in the mean-nullcline inequality holds exactly when \(\mu\) is a Dirac mass at a positive equilibrium. Hence every non-equilibrium compact interior recurrent state, and in particular every positive nonconstant periodic orbit, has its mean point strictly below the predator nullcline.

## Assumptions and scope
The assertion is for the deterministic two-dimensional system printed as equation (1) in Wang, Wang and Yuan. All model parameters are positive. The measure is invariant under the complete flow and has compact support contained strictly inside the positive quadrant. This condition makes \(\log v\) and the rational observables used below continuously differentiable and bounded on the support. The result concerns deterministic compact recurrence; it does not assert an analogous identity for the paper's stochastic system, where Itô correction terms would have to be included.

The source proves positivity and boundedness for nonnegative solutions and reports parameter regimes containing stable limit cycles and equilibrium–cycle bistability, so the compact recurrent states constrained here occur naturally in the model's analyzed dynamics.

## Proof
For an invariant probability measure with compact support, the integral of the derivative of any continuously differentiable observable along the vector field is zero. Apply this first to \(\log v\). Since
\[
\frac{d}{dt}\log v=-mv+\frac{qu}{1+cu},
\]
invariance gives
\[
m\bar v=q\int \frac{u}{1+cu}\,d\mu.
\]

Set \(b=\bar u\). The pointwise algebraic identity
\[
u-b=(1+cb)\frac{u-b}{1+cu}+c\frac{(u-b)^2}{1+cu}
\]
implies, after integration and use of \(\int(u-b)\,d\mu=0\), that
\[
\int\frac{b-u}{1+cu}\,d\mu
=
\frac{c}{1+cb}\int\frac{(u-b)^2}{1+cu}\,d\mu.
\]
Because
\[
\frac{b}{1+cb}-\frac{u}{1+cu}
=
\frac{b-u}{(1+cb)(1+cu)},
\]
we obtain
\[
\frac{q b}{1+cb}-q\int\frac{u}{1+cu}\,d\mu
=
\frac{qc}{(1+cb)^2}\int\frac{(u-b)^2}{1+cu}\,d\mu.
\]
Substituting the first balance proves the mean-nullcline defect formula. Its right-hand side is nonnegative and vanishes exactly when \(u=b\) almost surely.

If \(u\) is constant on the support of an invariant measure, invariance forces the \(u\)-component of the vector field to vanish there. For fixed positive \(u\), the bracket multiplying \(u\) in the prey equation is strictly decreasing in \(v\), because its derivative with respect to \(v\) is
\[
-\frac{rk}{(1+kv)^2}-\frac{p}{1+cu}<0.
\]
Thus at most one positive \(v\) can occur, and the measure is a Dirac mass at a positive equilibrium. Conversely every positive-equilibrium Dirac mass gives equality.

Next apply invariance to the observable \(v\):
\[
0=-m\int v^2\,d\mu+\int v\frac{qu}{1+cu}\,d\mu.
\]
Combining this with \(\int qu/(1+cu)\,d\mu=m\bar v\) yields
\[
\operatorname{Cov}_\mu\!\left(v,\frac{qu}{1+cu}\right)
=m\operatorname{Var}_\mu(v).
\]
By Cauchy–Schwarz and the fact that \(u\mapsto qu/(1+cu)\) is \(q\)-Lipschitz on \((0,\infty)\),
\[
m^2\operatorname{Var}_\mu(v)
\le \operatorname{Var}_\mu\!\left(\frac{qu}{1+cu}\right)
\le q^2\operatorname{Var}_\mu(u),
\]
which proves the fluctuation bound.

## Verification
The packaged checker verifies symbolically the pointwise algebraic identity that generates the Jensen defect and the elementary covariance reduction. The critical analytic inputs are only invariance of \(\mu\), compact interior support, and positivity of parameters. For a periodic orbit, \(\mu\) may be taken as normalized time measure, so every displayed integral becomes a period average.

A direct full-text inspection of the source located the model, its positivity/boundedness theorem, the positive-equilibrium predator nullcline \(v^*=qu^*/[m(1+cu^*)]\), and the reported stable limit-cycle regimes. Text searches in that full text found no deterministic statements indexed by “average”, “covariance”, or “variance”.

## Relationship to prior work
Wang, Wang and Yuan derive the same predator nullcline for positive equilibria and analyze saddle-node, Hopf and Bogdanov–Takens bifurcations, including regimes with a stable interior limit cycle and equilibrium–cycle bistability. The identity above is different in logical scope: it constrains every compact interior invariant probability measure at finite amplitude, not merely equilibria or local Hopf branches, and gives an exact nonnegative defect measuring how oscillation moves the mean below the predator nullcline.

A 2022 spatial-memory/maturation extension by Wang, Yuan and Wang contains the same local predator crowding and Holling-II interaction terms in a delayed diffusive setting and is the predecessor cited by the source for equilibrium existence. A complete statement-level full-text comparison of that predecessor was not available, so this remains a residual literature risk. A later open-access paper reproducing that reaction structure was also checked and did not state a time-average, covariance, or variance identity of this form. Broad searches for the exact model, its DOI, periodic-orbit averages, covariance, variance, Jensen defects, and predator-nullcline mean laws did not locate a stronger statement covering the claim.

## Limitations
The result does not classify which invariant measures exist, locate or prove uniqueness of any limit cycle, or determine its amplitude or period. It does not transfer unchanged to the stochastic model. The variance inequality is a consequence of the exact covariance identity and a global Lipschitz estimate and need not be sharp. Literature searches cannot establish absolute novelty, and the incomplete full-text comparison with the closely related 2022 predecessor is the principal residual originality risk.

## References
1. C. Wang, H. Wang and S. Yuan, “Complex bifurcations and noise-induced transitions: A predation model with fear effect in prey and crowding effect in predators,” *Discrete and Continuous Dynamical Systems - B* 28 (2023), 3837–3867. DOI: 10.3934/dcdsb.2022243. Early access and online publication: 14 December 2022.
2. C. Wang, S. Yuan and H. Wang, “Spatiotemporal patterns of a diffusive prey-predator model with spatial memory and pregnancy period in an intimidatory environment,” *Journal of Mathematical Biology* 84 (2022), Article 12. DOI: 10.1007/s00285-022-01716-4.
3. H. Sun, P. Hao and J. Cao, “Dynamics analysis of a diffusive prey-taxis system with memory and maturation delays,” *Electronic Journal of Qualitative Theory of Differential Equations* 2024, No. 40, 1–20. DOI: 10.14232/ejqtde.2024.1.40.
