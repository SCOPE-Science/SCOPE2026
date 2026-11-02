# Universal finite-horizon convex-risk minimum for two dispersing habitats

## Finding

Consider two habitats with independent environmental years but possibly spatially correlated growth within each year. In the linear dispersal model defined below, the **unique dispersal fraction minimizing every strictly convex risk score of mean-normalized total abundance at every horizon of at least two years** is
\[
q_*=\frac{1}{1+s},
\]
where \(s\in(0,1]\) is the survival fraction of migrants. The same strategy minimizes every (not necessarily strict) convex expectation for every finite horizon, without any spatial-independence assumption. This is a statement about variability *after normalization by the strategy's own expected abundance*, not about maximizing absolute biomass, long-run logarithmic growth, or extinction avoidance.

More precisely, let \(U_t(q)\) be the normalized total defined below. For every integer \(t\ge0\), every \(q\in[0,1]\), and every finite convex test function \(\varphi:[0,\infty)\to\mathbb R\) for which the expectations exist,
\[
\mathbb E\,\varphi(U_t(q_*))\le\mathbb E\,\varphi(U_t(q)).
\]
If \(\Pr(G_1\ne G_2)>0\), this inequality is strict for every strictly convex \(\varphi\) with finite expectations whenever \(t\ge2\) and \(q\ne q_*\). At \(t=0,1\), every strategy gives the same normalized-abundance law. If \(G_1=G_2\) almost surely, every strategy gives the same law at all horizons.

When the environmental multipliers have finite second moments, write
\[
\mu=\mathbb E G_1,\qquad
K=\frac{\mathbb E(G_1+G_2)^2}{4\mu^2},\qquad
d=\mathbb E(G_1-G_2)^2.
\]
Then the *exact two-year excess variance* is
\[
\boxed{\operatorname{Var}U_2(q)-\operatorname{Var}U_2(q_*)
=\frac{d^2}{16\mu^4}
\left(\frac{1-(1+s)q}{1-(1-s)q}\right)^2.}
\]
At every horizon \(t\), the sharp universal variance floor is
\[
\operatorname{Var}U_t(q)\ge K^t-1,
\]
with equality for \(q=q_*\), and, when \(d>0\), strict inequality for \(q\ne q_*\) and \(t\ge2\).

## Assumptions and scope

Let \((G_{1,t},G_{2,t})_{t\ge0}\) be independent, identically distributed across integers \(t\), with an exchangeable bivariate distribution in each year:
\[
(G_{1,t},G_{2,t})\overset{d}{=}(G_{2,t},G_{1,t}),
\qquad 0<G_{i,t}<\infty\quad\text{almost surely},\quad
0<\mu=\mathbb E G_{i,t}<\infty.
\]
Spatial independence within a year is **not** required. Fix any \(0<s\le1\), any \(q\in[0,1]\), and equal strictly positive initial habitat abundances \(X_0=(x,x)^T\) with \(x>0\). The annual population update is exactly
\[
X_{t+1}=D_q\,\operatorname{diag}(G_{1,t},G_{2,t})X_t,
\qquad
D_q=\begin{pmatrix}1-q&sq\\sq&1-q\end{pmatrix}.
\]
Set \(c_q=1-q+sq>0\), \(S_t=X_{1,t}+X_{2,t}\), and
\[
U_t(q)=\frac{S_t}{2x(\mu c_q)^t}.
\]
Thus \(\mathbb EU_t(q)=1\); the denominator is the true strategy-dependent expected total, not an identical absolute scale across policies. The distributional statement uses no moment above order one. The variance statements additionally require \(\mathbb E G_1^2<\infty\).

## Proof

**1. Common normalized update.** Put \(W_t=X_{1,t}/S_t\in(0,1)\). The column sums of \(D_q\) equal \(c_q\), so
\[
S_{t+1}=c_q(G_{1,t}X_{1,t}+G_{2,t}X_{2,t}),\qquad
U_{t+1}=U_t\frac{W_tG_{1,t}+(1-W_t)G_{2,t}}{\mu}.
\]
The current environmental pair is independent of the history through year \(t-1\). Hence \(\mathbb E(U_{t+1}\mid\mathcal F_t)=U_t\), proving \(\mathbb E U_t=1\). The unique \(q_*\in[0,1]\) with equal rows of \(D_q\) solves \(1-q=sq\), giving \(q_*=1/(1+s)\). At that value all two habitat abundances are equal immediately after every annual update, and the initial abundances are equal. Therefore, defining \(V_t=(G_{1,t}+G_{2,t})/(2\mu)>0\),
\[
U_t(q_*)=\prod_{j=0}^{t-1}V_j,
\]
where the \(V_j\) are independent, identically distributed, and of mean one.

**2. The strict one-step symmetric averaging inequality.** For fixed \(y>0\), \(w\in[0,1]\), and any convex \(\varphi\), exchangeability implies
\[
\begin{aligned}
\mathbb E\varphi\!\left(\frac{y[wG_1+(1-w)G_2]}\mu\right)
&=\frac12\mathbb E\left[\varphi\!\left(\frac{y[wG_1+(1-w)G_2]}\mu\right)
+\varphi\!\left(\frac{y[(1-w)G_1+wG_2]}\mu\right)\right]\\
&\ge\mathbb E\varphi\!\left(\frac{y(G_1+G_2)}{2\mu}\right).
\end{aligned}
\]
For strictly convex \(\varphi\), the inequality is strict if \(w\ne1/2\), \(\Pr(G_1\ne G_2)>0\), and both expectations are finite. This is just pointwise convexity applied to the two exchanged allocations, not an assumption of independent habitats.

**3. Convex-order induction.** For fixed convex \(\varphi\), define
\[
(P\varphi)(y)=\mathbb E\varphi(yV_0).
\]
Because \(V_0>0\) and is independent of \(y\), \(P\varphi\) is convex. Conditional application of step 2 gives
\[
\mathbb E\varphi(U_{t+1}(q))\ge\mathbb E(P\varphi)(U_t(q)).
\]
Beginning with \(U_0(q)=U_0(q_*)=1\) and iterating this inequality with the convex functions \(P\varphi,P^2\varphi,\dots\), one obtains
\[
\mathbb E\varphi(U_t(q))\ge(P^t\varphi)(1)
=\mathbb E\varphi(U_t(q_*)).
\]
The expectation of any convex test may be handled by truncation/affine lower support where necessary; the stated finite-expectation version requires no such extension.

**4. Strictness and the exact second-year gap.** Write \(c_q^-=1-q-sq\). If \(q\ne q_*\), then \(c_q^-\ne0\). For every positive deterministic patch pair \((u,v)\), exchangeability and \(\Pr(G_1\ne G_2)>0\) imply \(\Pr(G_1u\ne G_2v)>0\): otherwise \(G_1/G_2=v/u\) almost surely, and exchangeability forces that deterministic ratio to equal its reciprocal, giving \(G_1=G_2\) almost surely. Thus, conditional on any history, \(X_{1,t+1}-X_{2,t+1}=c_q^-(G_{1,t}X_{1,t}-G_{2,t}X_{2,t})\) is nonzero with positive probability. In particular \(\Pr(W_t\ne1/2)>0\) for each \(t\ge1\). Consequently, the first inequality of step 3 is strict at every year \(t\ge1\) for strictly convex \(\varphi\), proving all claimed strictness assertions. The equality of the one-year laws follows because \(W_0=1/2\).

For finite second moments, spatial exchangeability gives \(\mathbb E[(G_1+G_2)(G_1-G_2)]=0\). For fixed \(w\),
\[
\mathbb E\left(\frac{wG_1+(1-w)G_2}{\mu}\right)^2
=K+\frac{d}{\mu^2}(w-1/2)^2.
\]
In the first year,
\[
U_1=\frac{G_{1,0}+G_{2,0}}{2\mu},\quad
W_1-\frac12=\frac{c_q^-}{c_q}\frac{G_{1,0}-G_{2,0}}{2(G_{1,0}+G_{2,0})},
\]
so \(\mathbb E U_1^2=K\) and
\[
\mathbb E\left[U_1^2(W_1-1/2)^2\right]
=\frac{(c_q^-/c_q)^2d}{16\mu^2}.
\]
Conditional second moments now yield
\[
\mathbb E U_2(q)^2=K^2+\frac{d^2}{16\mu^4}(c_q^-/c_q)^2.
\]
Subtracting the common mean-square \(1\) proves the boxed identity. At \(q_*\), \(\mathbb E U_t(q_*)^2=K^t\) by independence, and the convex-order statement applied to \(\varphi(u)=u^2\) proves the sharp floor.

## Verification

Run the self-contained exact-rational checker with `python3 check.py`. It enumerates full habitat trajectories from the original update for six exchangeable discrete environmental laws, three migrant-survival fractions, six dispersal choices, and one-, two-, and three-year horizons. It tests equal means, both tail directions of convex hinge functions at eight thresholds, strict second and third moments in nondegenerate cases, the two-year gap formula, and the explicit binary-growth example. A successful run prints `EXACT_CHECKS_PASSED 6022`. This finite enumeration corroborates formulas and selected convex functions; the induction in the Proof, not enumeration, establishes the unrestricted theorem.

For independent equiprobable habitat growth multipliers in \(\{1,3\}\), \(\mu=2\), \(K=9/8\), and \(d=2\). With \(s=1\), at two years the mean-normalized variance is exactly \(17/64\) at \(q=q_*=1/2\), versus \(9/32\) with no migration. With \(s=1/2\), the unique variance-minimizing complete-mixing fraction is \(q_*=2/3\), not \(1/2\). The minimum, \(17/64\), applies to normalized abundance; the two strategies have different expected physical abundances because migration causes mortality.

## Relationship to prior work

Morita and Yoshimura (2012) specify precisely this two-patch growth--dispersal model with migrant survival, spatial environmental correlation and independent years. Their central outputs are the stationary patch-ratio law and long-run logarithmic population growth; their well-mixed identity \(qs=1-q\) is prior art. The claim here is different: a sharp, distribution-free, every-finite-horizon *convex-order* statement about mean-normalized **total** abundance, with strict equality cases and an exact two-year variance penalty. The 2013 extension concerns many-patch growth, relative-abundance power laws and lognormal approximations, not this finite-horizon stochastic order.

Jansen and Yoshimura (1998) establish ecological risk-spreading benefits for long-run growth in sink habitats; Schreiber (2010) studies logarithmic growth and temporal correlation; and Keeling (2000) studies moments and population persistence. Their definitions, objectives and stated results do not themselves entail the present all-convex, finite-horizon risk ordering. Convexity under exchangeable averaging is classical mathematical machinery and is not claimed as an independent new general inequality. Historical equivalences in uninspected or difficult-to-retrieve literature remain possible.

## Limitations

The model requires identical marginal environmental-growth laws and exchangeability across habitats, no temporal dependence between environmental years, strictly positive growth multipliers, linear density-independent growth and a constant dispersal fraction and migrant-survival probability. The result concerns relative variability **after rescaling each strategy by its own expectation**; it does not order absolute abundances, extinction probabilities with discrete individuals, median abundance, long-run Lyapunov exponents or empirical conservation outcomes. The strict-variance identities require second moments. Distinct alternative dispersal fractions need not be ordered by convex risk: only the universal minimum at complete mixing is claimed. Historical-priority assessment is necessarily limited by accessible literature.

## References

1. S. Morita and J. Yoshimura, *Analytical Solution of Metapopulation Dynamics in Stochastic Environment*, arXiv:1207.4618, first submitted 2012-07-19; https://arxiv.org/abs/1207.4618 (primary model and comparison).
2. S. Morita and J. Yoshimura, *Analytical solution of stochastic model of risk-spreading with global coupling*, arXiv:1307.7903, first submitted 2013-07-30; https://arxiv.org/abs/1307.7903.
3. V. A. A. Jansen and J. Yoshimura, *Populations can persist in an environment consisting of sink habitats only*, PNAS 95 (1998), 3696–3698; https://pmc.ncbi.nlm.nih.gov/articles/PMC19898/.
4. S. J. Schreiber, *Interactive effects of temporal correlations, spatial heterogeneity and dispersal on population persistence*, Proc. R. Soc. B 277 (2010), 1907–1914; https://doi.org/10.1098/rspb.2009.2006.
5. M. J. Keeling, *Metapopulation moments: coupling, stochasticity and persistence*, J. Animal Ecology 69 (2000), 725–736; https://doi.org/10.1046/j.1365-2656.2000.00430.x.
