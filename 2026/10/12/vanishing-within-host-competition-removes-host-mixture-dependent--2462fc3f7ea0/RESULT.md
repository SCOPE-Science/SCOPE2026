# Vanishing within-host competition removes host-mixture-dependent virulence switching

## Finding

Consider the nested within-host/epidemic transmission-potential model defined below. For any fixed positive natural mortality \(m\), resistant-host recovery rate \(r\), transmission scale \(k\), and competition constant \(\lambda\), there is \(c_*>0\) such that every \(0<c<c_*\) and every vulnerable-host proportion \(p\in[0,1]\) has **exactly one global maximizer** \(x_c(p)>0\) of transmission potential \(K_c(x,p)\). It satisfies the **uniform** phenotype limit

\[
\sup_{0\le p\le1}|x_c(p)-10|=O(c).
\]

Furthermore, writing \(J(z,T)=\int_0^T e^{zt}\,dt\), the associated vulnerable-host disease mortality satisfies the *host-mixture-independent* law

\[
\sup_{0\le p\le1}\left|\frac{q_c(x_c(p))}{c}-10mJ\left(\frac92,\frac1m\right)\right|=O(c),
\]

and the optimized transmission potential has the uniform asymptotic

\[
\max_{x>0}K_c(x,p)=k\left[(1-p)J\left(\frac92,\frac1{m+r}\right)+pJ\left(\frac92,\frac1m\right)\right]+O(c).
\]

For every fixed \(R>10\), all sufficiently small \(c>0\) also make \(K_c(\cdot,p)\) strictly increasing before its sole maximizer and strictly decreasing afterward **throughout** \([0,R]\), simultaneously for all \(p\in[0,1]\). Therefore the two competing local optima underlying the finite-competition host-mixture hysteresis cannot persist in any fixed, bounded biological phenotype interval as \(c\downarrow0\).

## Assumptions and scope

The pathogen phenotype is any \(x>0\), the inoculum is held fixed at \(V_c(0;x)=1\), and the within-host population obeys

\[
\frac{dV_c}{dt}=V_c\left(\frac{x}{1+\lambda cV_c}-\frac{10+x^2}{20}\right).
\]

Here \(c>0\) controls both within-host saturation and disease-induced mortality. The coefficient \(\lambda>0\) is held fixed as \(c\to0\); the motivating study uses the same type of co-scaling. The host types are resistant with proportion \(1-p\) or vulnerable with proportion \(p\). The resistant infectious duration is \(T_r=(m+r)^{-1}\). Set

\[
F_c(t,x)=\frac{xV_c(t;x)}{1+\lambda cV_c(t;x)}.
\]

The vulnerable disease mortality \(q_c(x)\ge0\) is defined by the implicit mean-replication relation

\[
q_c(x)=c\big(m+q_c(x)\big)\int_0^{1/(m+q_c(x))}F_c(t,x)\,dt.
\]

Its infectious duration is \(T_c(x)=1/(m+q_c(x))\). The epidemiological transmission potential, whose maximizer is selected in the source model when mutations may be large, is

\[
K_c(x,p)=k\left[(1-p)\int_0^{T_r}V_c(t;x)\,dt+p\int_0^{T_c(x)}V_c(t;x)\,dt\right].
\]

The theorem concerns global maximization of this specified fitness function, not coexistence, mutation-limited path dynamics, equilibria at a fixed non-small \(c\), or extinction/persistence controlled by the separate demographic birth parameter. All asymptotic constants may depend on fixed \(m,r,k,\lambda\) (and on \(R\) for the compact-interval statement) but **not** on \(p\).

## Proof

**1. The mortality equation has exactly one admissible solution.** For fixed \(x\ge0\) and \(c>0\), put \(H_c(T,x)=mT+c\int_0^TF_c(t,x)\,dt\). The within-host equation has a unique global positive solution on every finite time interval: its logarithmic growth rate is at most \(x-(10+x^2)/20\). Therefore \(F_c\ge0\) and \(\partial_T H_c=m+cF_c(T,x)>0\). The values \(H_c(0,x)=0\) and \(H_c(1/m,x)\ge1\) yield a unique \(T_c(x)\in(0,1/m]\) solving \(H_c(T_c(x),x)=1\); strict inequality holds for \(x>0\). Setting \(q_c(x)=1/T_c(x)-m\) and rearranging proves the asserted implicit relation, with no extraneous solution. This identity also gives smooth dependence on \((x,c)\) near every bounded \(x\)-interval and near \(c=0\), since \(\partial_T H_c\ge m>0\).

**2. A uniform global envelope.** Define

\[
g(x)=x-\frac{10+x^2}{20}=\frac92-\frac{(x-10)^2}{20}.
\]

For all \(x,c,t\ge0\), the within-host logarithmic derivative satisfies \(d\log V_c/dt\le g(x)\); consequently \(V_c(t;x)\le e^{g(x)t}\). Moreover \(T_c(x)\le1/m\). Hence

\[
K_c(x,p)\le K_0(x,p):=k\left[(1-p)J(g(x),T_r)+pJ(g(x),1/m)\right]
\]

for all \(x\ge0\) and all \(p\in[0,1]\). For every \(T>0\), \(J(z,T)\) is strictly increasing in \(z\), because \(\partial_zJ=\int_0^T t e^{zt}\,dt>0\). Since \(g\) has its unique maximum at \(x=10\), so does \(K_0(\cdot,p)\), for every \(p\).

**3. Uniform differentiable perturbation and uniqueness.** Fix \(R>10\). On \([0,R]\times[0,1/m]\), standard smooth dependence for the within-host ODE and the strictly positive derivative \(\partial_TH_c\) give \(V_c\to e^{g(x)t}\), \(T_c\to1/m\), and \(K_c(\cdot,p)\to K_0(\cdot,p)\) in \(C^2([0,R])\), with error \(O(c)\) uniform over \(p\in[0,1]\). To justify smoothness across \(c=0\), choose a sufficiently small real neighborhood of zero: on the given compact \((x,t)\)-set, the ODE solution stays bounded and \(1+\lambda cV_c\) remains bounded away from zero; smooth parameter dependence and the implicit-function theorem then apply.

Differentiation of the explicit limiting function gives

\[
K_0'(x,p)=k\frac{10-x}{10}\left[(1-p)\int_0^{T_r}t e^{g(x)t}\,dt+p\int_0^{1/m}t e^{g(x)t}\,dt\right].
\]

Its sign is positive for \(0\le x<10\), negative for \(x>10\), uniformly away from the trait \(10\). In addition,

\[
K_0''(10,p)=-\frac{k}{10}\left[(1-p)\int_0^{T_r}t e^{9t/2}\,dt+p\int_0^{1/m}t e^{9t/2}\,dt\right]<0,
\]

with an upper bound strictly below zero independent of \(p\). Pick any small neighborhood \((10-\delta,10+\delta)\) contained in \((0,R)\). Uniform \(C^2\) convergence makes \(K_c'\) strictly positive to its left, strictly negative to its right, and \(K_c''\) strictly negative inside the neighborhood, for all small \(c>0\) and all \(p\). Thus there is one and only one critical point in \([0,R]\), a strict maximum. Call it \(x_c(p)\).

It is also the **unique global maximizer on \((0,\infty)\)**: for \(x\ge R\), monotonic decrease of \(g(x)\) implies \(K_c(x,p)\le K_0(x,p)\le K_0(R,p)\). The limiting gap \(K_0(10,p)-K_0(R,p)>0\) has a positive minimum over \(p\in[0,1]\). Since \(K_c(10,p)\to K_0(10,p)\) uniformly, it exceeds \(K_0(R,p)\) for all sufficiently small \(c\). Therefore no trait outside \([0,R]\) is competitive. The curvature bound and \(K_c'(10,p)=O(c)\) give \(x_c(p)=10+O(c)\), uniformly in \(p\), by the mean-value theorem.

**4. Selected mortality and optimized fitness.** The defining equation yields

\[
\frac{q_c(x)}c=(m+q_c(x))\int_0^{T_c(x)}F_c(t,x)\,dt.
\]

Smooth compact-parameter dependence from Step 3 and \(q_0(x)=0\) show \(q_c(x)/c=m xJ(g(x),1/m)+O(c)\), uniformly for bounded \(x\). Substitution of \(x=x_c(p)=10+O(c)\) proves the mortality estimate. Uniform \(K_c-K_0=O(c)\) and \(x_c(p)-10=O(c)\) show \(\max_x K_c(x,p)=K_0(10,p)+O(c)\), finishing all claims.

## Verification

The independently executable standard-library script `verify.py` implements the original nonlinear within-host ODE and mortality-duration equation using fourth-order Runge–Kutta, trapezoidal integration, and scalar bisection. For \(m=1\), \(r=4\), \(k=\lambda=1\), it numerically checks the upper envelope and approaches of the maximizing phenotype and induced mortality as \(c\) decreases, alongside an exact rational verification of \(g(x)=9/2-(x-10)^2/20\). The program prints `VERIFY_OK` when these **illustrations** succeed. The proof above, not finite numerics, establishes the full continuum and the quantified asymptotics.

## Relationship to prior work

Barril and Vegué (2026, Sections 2–5, Eqs. (3), (11)–(13), Figures 1–2) derive the nested model, transmission-potential selection principle, within-host tradeoff, and host-mixture-dependent locally optimal phenotypes for particular finite parameter values. Their Appendix establishes competition and stability properties at fixed demographic rates; the article does not state the uniform weak-competition theorem or global uniqueness for all sufficiently small \(c\) and all host proportions. The fact that the initial exponential growth rate \(g(x)\) is optimized at \(x=10\) follows directly from their specified degradation function; **the new claim** is that the *global epidemiological* fitness maximizer becomes uniquely selected near that trait for every host mixture, together with a sharp mortality coefficient and exclusion of local competing optima on all fixed bounded intervals.

André and Gandon (2006) already analyze virulence evolution and immune differences between host types using infection-age structure. That paper motivates the biological context but does not directly prove the singular-limit statement for the above fixed-inoculum coupled saturation/virulence functional. No general claim that virulence tradeoffs, heterogeneous-host selection, or perturbation methods themselves are novel is made.

## Limitations

The singular limit holds with \(m,r,k,\lambda\) and inoculum fixed. It need not describe biological settings where host lifespan or inoculum diverges as \(c\to0\), nor does it provide a quantitative, biologically accessible threshold \(c_*\). It does **not** say every local maximum at arbitrarily large phenotype disappears, nor deny the finite-competition hysteresis exhibited in the source figures. The mortality limit is a perturbative theorem for this precisely specified model, not a universal virulence-evolution principle. Literature searches cannot exclude all unindexed or inaccessible related results; independent assessment has not been performed.

## References

1. C. Barril and M. Vegué, “Virulence Evolution in Host Populations with Heterogeneous Immune Responses: The Weakening of the Uncommon Weak,” *Bulletin of Mathematical Biology* **88**, article 109 (2026), first public June 9, 2026, DOI: 10.1007/s11538-026-01673-9, https://link.springer.com/article/10.1007/s11538-026-01673-9.
2. J.-B. André and S. Gandon, “Vaccination, within-host dynamics, and virulence evolution,” *Evolution* **60** (2006), 13–23, DOI: 10.1111/j.0014-3820.2006.tb01077.x, https://doi.org/10.1111/j.0014-3820.2006.tb01077.x.
