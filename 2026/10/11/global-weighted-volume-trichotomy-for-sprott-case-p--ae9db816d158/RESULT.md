# Global weighted-volume trichotomy for Sprott case P

## Finding
For the quadratic three-dimensional Sprott case-P family
\[
\dot x=ay+z,\qquad \dot y=-x+y^2,\qquad \dot z=x+by,
\]
with arbitrary real parameters \(a,b\), define \(P=y+z\). The following rigorous global transition holds.

For \(b<0\), the set of initial data whose maximal solutions exist for all positive times **and remain bounded** has three-dimensional Lebesgue measure zero. In particular, no compact invariant set can have a basin of forward convergence of positive Lebesgue measure. This statement allows exceptional bounded trajectories, including equilibria, and makes no assertion of finite-time blowup.

For \(b=0\), every forward-bounded solution converges to \((0,0,0)\); the origin is the **only nonempty compact invariant set**, and its Dirac mass is the only compactly supported invariant probability measure. The origin has no open attracting neighborhood.

For \(b>0\), a strictly contracting smooth weighted volume exists on every positively timed flow domain; no global existence or existence of attractors is asserted. More precisely, whenever \(b\ne0\), the strictly positive density and its infinitesimal balance are
\[
\rho_b=\exp\!\left(-\frac{2(y+z)}b\right),\qquad
\nabla\!\cdot(\rho_bF)=-\frac2b\,y^2\rho_b.
\]

For every \(b\in\mathbb R\), every compactly supported invariant probability measure \(\mu\) further obeys
\[
\int y^2\,d\mu=-b\int y\,d\mu,\qquad
\operatorname{Var}_\mu(y)=-m(m+b),\quad m=\int y\,d\mu.
\]
If \(b\ne0\), the only measures attaining either endpoint of the forced interval between \(0\) and \(-b\) for \(m\) are the Dirac masses at the two equilibria \(E_0=(0,0,0)\) and \(E_b=(b^2,-b,ab)\). In particular every other compact stationary state has mean phase-volume rate \(2m\) with strictly the opposite sign to \(b\).

## Assumptions and scope
The phase space is \(\mathbb R^3\). Parameters \(a,b\) are arbitrary real numbers held constant. Solutions are maximal classical solutions of the polynomial vector field \(F\). “Forward bounded” means defined for all \(t\ge0\) and bounded on that half-line; finite-time continuation of any bounded polynomial-ODE solution is standard. “Compact invariant” means invariant under the complete, two-sided restricted flow. An invariant probability measure is invariant under every time map wherever defined; compact support ensures all times are defined on its invariant support. The Lebesgue-null assertion concerns initial states, not the measure of an invariant set or a claim about its dimension.

## Proof
**1. Two exact differential identities.** Direct differentiation of \(P=y+z\) yields
\[
\dot P=(-x+y^2)+(x+by)=y(y+b),\qquad
\nabla\!\cdot F=2y.
\]
For \(b\ne0\), taking the logarithmic derivative of the displayed density gives
\[
F\!\cdot\nabla\log\rho_b=-\frac2b\,y(y+b).
\]
Therefore \(\nabla\!\cdot(\rho_bF)=\rho_b(2y-2y(y+b)/b)=-2y^2\rho_b/b\). For the flow \(\phi_t\), Jacobi's formula consequently gives, for any time interval on which the solution exists,
\[
\frac{\rho_b(\phi_tu)\det D\phi_t(u)}{\rho_b(u)}
=\exp\!\left(-\frac2b\int_0^t y(s;u)^2\,ds\right).
\]
The determinant is positive because the flow begins at the identity and is locally a diffeomorphism.

**2. Almost-everywhere failure of forward boundedness for \(b<0\).** Fix \(R>0\) and define
\[
B_R=\{u:\phi_t(u)\text{ exists for all }t\ge0,
\ \|\phi_t(u)\|\le R\text{ for all }t\ge0\}.
\]
This is measurable: boundedness can be tested at nonnegative rational times on the open local-flow domains, with the standard continuation criterion. It lies inside the radius-\(R\) closed ball and satisfies \(\phi_T(B_R)\subset B_R\) for each \(T>0\). Let \(\nu_b=\rho_b\,d\lambda_3\); its mass on \(B_R\) is finite because the density is bounded on that ball.

Suppose \(\lambda_3(B_R)>0\). The hyperplane \(y=0\) is Lebesgue null, so \(y(0;u)\ne0\) for almost every \(u\in B_R\). Continuity implies \(\int_0^T y(t;u)^2dt>0\) for those \(u\), and the Jacobian identity has right side strictly greater than one because \(b<0\). By injectivity of each finite-time flow map and change of variables,
\[
\nu_b(\phi_T(B_R))
=\int_{B_R}\rho_b(u)\exp\!\left(-\frac2b\int_0^T y(t;u)^2dt\right)du
>\nu_b(B_R).
\]
But forward invariance gives \(\nu_b(\phi_T(B_R))\le\nu_b(B_R)\), a contradiction. Thus \(\lambda_3(B_R)=0\). Every bounded forward trajectory begins in \(B_R\) for some positive integer \(R\), so the union of these sets is Lebesgue null. If a compact invariant set had a positive-measure basin of convergence, every point of that basin would have a bounded forward orbit and would belong to this null union, impossible. For \(b>0\), the same identity gives strict weighted contraction of every positive-volume measurable set that can be flowed for a fixed positive time; the set is not required to be forward invariant.

**3. Rigidity at \(b=0\).** Here \(\dot P=y^2\ge0\). Along a bounded forward orbit \(P(t)\) is bounded and monotone, so it has a finite limit. Its compact omega-limit set is invariant and lies in \(y=0\), by the invariance principle or by integrating \(y^2\) and using uniform continuity of \(y\) on a bounded orbit. A complete orbit lying entirely in \(y=0\) must have \(x=0\) from \(\dot y=-x\), and then \(z=0\) from \(\dot x=z\). Hence the omega-limit set is the singleton origin, proving convergence.

For a bounded complete orbit, apply the same argument to the reversed-time limit sets. Its alpha-limit set also lies in \(y=0\) (integrate \(y^2\) over \(( -\infty,0]\) using boundedness and monotonicity), hence equals the origin. Thus \(P(t)\) has limit zero in both time directions. Monotonicity forces \(P(t)\equiv0\) and \(y(t)\equiv0\); the orbit is constant at the origin. Each point of a compact invariant set belongs to a bounded complete orbit, proving the compact-invariant classification. Finally, every neighborhood of the origin includes an initial state with \(P>0\), whereas such an orbit, if bounded, could not converge to the origin because \(P\) is nondecreasing. Therefore the origin has no open attracting neighborhood.

**4. Stationary laws and endpoint rigidity.** Compact support permits integrating derivatives of \(P\), \(x\), and \(z\) against an invariant probability measure. One obtains
\[
\mathbb E_\mu[y^2]+b\mathbb E_\mu[y]=0,\quad
\mathbb E_\mu[x]=\mathbb E_\mu[y^2],\quad
\mathbb E_\mu[z]=-a\mathbb E_\mu[y].
\]
With \(m=\mathbb E_\mu[y]\), the variance is \(-m(m+b)\ge0\), hence \(m\) lies in the closed interval with endpoints \(0,-b\). For nonzero \(b\), equality of the variance at either endpoint forces \(y\) constant \(\mu\)-almost everywhere. Invariance and continuity give constant \(y\) along almost every supported trajectory, hence \(x=y^2\) and \(z=-ay\) there, with \(0=y(y+b)\). These conditions identify \(E_0\) or \(E_b\), and since \(b\ne0\) they are distinct. Thus only the respective equilibrium Dirac measures attain the endpoints. If \(b=0\), the variance formula forces \(y=0\) almost surely and the same invariance argument yields the origin mass. The divergence integral equals \(2m\), proving its stated strict sign for every other compact stationary state.

## Verification
A standalone exact-symbolic checker, `checks/check_sprott_p.py`, verifies the polynomial coboundary, weighted-divergence identity, vector-field equilibria, Jacobian trace, the stationary algebraic variance identity and representative nonzero-parameter substitutions. Run it with Python 3 and SymPy using `python checks/check_sprott_p.py` after extracting the accompanying files. The measure-zero conclusion is established analytically by the positive-measure change-of-variables contradiction; it is **not** inferred from finite numerical trajectories or from the symbolic checker.

## Relationship to prior work
Sprott's 1994 article introduced case P and measured its numerical Lyapunov exponents and mean divergence at the positive parameter \(b=1\). Sprott's 2013 parameter atlas classified sampled trajectories as unbounded, equilibrium, periodic, or chaotic and explicitly identified case P as a multistability candidate. Mendes, Lainscsek and Letellier (2021) compared the topology and mean dissipation of Sprott K, O and P attractors at selected parameters. Their numerical or topological statements do not entail this theorem's parameter-uniform weighted Jacobian identity, measure-zero bounded forward basin for **every** \(a\) when \(b<0\), or complete critical classification at \(b=0\). The present result gives a rigorous parameter-sign obstruction complementary to those numerical regions. The author-paper comparisons below do not constitute an exhaustive priority certificate.

## Limitations
For \(b<0\), there remain explicit bounded exceptional trajectories (the equilibria), so the assertion is only almost everywhere. A forward-unbounded solution need not have a norm tending to infinity; some solutions may cease at finite time. Positive \(b\) guarantees weighted-volume contraction, **not** boundedness, chaotic recurrence, the existence of an attractor or a positive-measure attractor basin. Invariant measures can include mixtures of equilibrium masses and possibly other stationary states; the theorem does not classify all stationary states away from \(b=0\). The result does not assert uniqueness relative to all unindexed literature or independent proof certification.

## References
1. J. C. Sprott, “Some simple chaotic flows,” *Physical Review E* **50** (August 1994), R647–R650; DOI 10.1103/PhysRevE.50.R647; author-archived full text: https://sprott.physics.wisc.edu/pubs/paper212.pdf.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” author technical note (April 27, 2013; modified September 1, 2014), https://sprott.physics.wisc.edu/technote/regions.htm.
3. E. M. A. M. Mendes, C. Lainscsek and C. Letellier, “Diffeomorphical equivalence vs topological equivalence among Sprott systems,” *Chaos* **31** (2021), 083126, DOI 10.1063/5.0058330; freely available at https://pmc.ncbi.nlm.nih.gov/articles/PMC12640250/.
