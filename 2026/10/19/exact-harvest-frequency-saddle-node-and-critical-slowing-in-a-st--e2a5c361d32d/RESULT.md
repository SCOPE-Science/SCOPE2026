# Exact harvest-frequency saddle node and critical slowing in a strong-Allee fishery

## Finding
For the deterministic strong-Allee population flow with periodic proportional removals, the return map has a single explicitly located persistence saddle node. If the retained fraction is no larger than the biological Allee threshold, all initial stocks become extinct regardless of the recovery interval. Otherwise a closed logarithmic formula gives the unique harvest-interval cutoff: below it every stock becomes extinct, at equality there is a one-sided attracting critical stock with universal reciprocal-iteration relaxation, and above it the system is bistable with exactly two positive fixed points. No nontrivial periodic orbits of the post-harvest return map occur.

Put \(0<a<1\), \(r>0\), \(0<q<1\), \(T>0\), and let \(\phi_T\) be the time-\(T\) flow of \(\dot x=r x(1-x)(x-a)\) on \([0,1]\). Define the immediate-post-harvest return map \(P_T(x)=q\phi_T(x)\). Its iterations \(x_{n+1}=P_T(x_n)\) start at any \(x_0\in[0,1]\).

**Complete classification.** If \(q\le a\), every such orbit converges to zero for every \(T>0\). If \(a<q<1\), write
\[
 T_c=\frac1r\left[\frac{\log q}{a}+\frac{1+a}{a(1-a)}\log\!\left(\frac{1-aq}{q-a}\right)\right].
\]
Then \(T_c>0\), and for \(T<T_c\) every orbit converges to zero. At \(T=T_c\) the only positive fixed point is
\[
 x_*=\frac{q(1+a)}{1+q},\qquad \phi_{T_c}(x_*)=\frac{1+a}{1+q}.
\]
All initial conditions \(x_0<x_*\) converge to zero, \(x_0=x_*\) remain fixed, and \(x_0>x_*\) converge to \(x_*\) with the sharp critical slowing law
\[
 \lim_{n\to\infty}n(x_n-x_*)=
 \frac{2q(1-aq)(q-a)}{(1+q)^2(1+a)(1-q)}.
\]
For \(T>T_c\), exactly two positive fixed points \(x_-<x_+\) lie in \((a,q)\). The smaller is unstable and separates the basins: initial stocks \(x_0<x_-\) converge to extinction, \(x_0=x_-\) remain fixed, and \(x_0>x_-\) converge to \(x_+\), which is asymptotically stable.

## Assumptions and scope
This is a deterministic one-species model, not a stochastic population, not a state-dependent harvest policy, and not a discrete approximation to the between-harvest ODE. Each time interval has exactly length \(T\). A fixed fraction \(1-q\) of the preharvest biomass is removed instantaneously at each pulse. The state \(x_n\) denotes biomass **immediately after** a pulse. Biomass is scaled to carrying capacity one; \(a\) is the dimensionless depensation (strong-Allee) threshold. The interval and retention are fixed throughout. The result includes every boundary initial condition in \([0,1]\), excluding only degenerate parameters \(a\in\{0,1\}\), \(q\in\{0,1\}\), \(r=0\), or \(T=0\).

## Proof
Write \(f(x)=rx(1-x)(x-a)=xg(x)\) with \(g(x)=r(1-x)(x-a)\). The unique ODE flow is strictly increasing in the initial value, preserves \([0,1]\), and has equilibria \(0,a,1\). For \(x\in(0,a)\), \(\phi_T(x)<x\); for \(x\in(a,1)\), \(x<\phi_T(x)<1\). Consequently \(P_T(x)<x\) whenever \(x\le a\), except possibly \(x=0\) where equality holds, and any positive fixed point requires \(x\in(a,q)\).

When \(q\le a\), the first image of any stock satisfies \(P_T(x)\le q\le a\). The strict downward drift below or at \(a\) implies convergence to zero, the only fixed point there; even the possible equality \(P_T(1)=a\) when \(q=a\) is followed by a strict decrease.

Assume \(q>a\). On the interval \((a,1)\) define \(R_T(x)=\phi_T(x)/x\). Standard scalar-flow differentiation gives \(\partial_x\phi_T(x)=f(\phi_T(x))/f(x)\), whence
\[
 \operatorname{sgn}R_T'(x)=\operatorname{sgn}\{g(\phi_T(x))-g(x)\}
 =\operatorname{sgn}\{1+a-x-\phi_T(x)\}.
\]
The second equality uses \(g(y)-g(x)=r(y-x)(1+a-x-y)\). Because \(x+\phi_T(x)\) increases strictly with \(x\) from \(2a\) to \(2\), it crosses \(1+a\) once. Hence \(R_T\) increases strictly to a unique interior maximum and then decreases strictly. Also \(R_T(a)=R_T(1)=1\), interpreted by continuous extension. Fixed points of \(P_T\) correspond precisely to intersections \(R_T(x)=1/q\); therefore there are at most two positive fixed points.

For every fixed \(x\in(a,1)\), \(R_T(x)\) increases strictly in \(T\), and \(R_T(x)\to1/x\) as \(T\to\infty\). Consequently its maximal value \(M(T)\) increases strictly continuously from \(1\) (as \(T\downarrow0\)) to \(1/a\) (as \(T\to\infty\)). The last limit follows from \(R_T(x)<1/x\le1/a\) together with letting \(T\to\infty\) for fixed \(x>a\), then letting \(x\downarrow a\). Since \(1<1/q<1/a\), there is exactly one \(T_c\) with \(M(T_c)=1/q\). The two-intersection classification follows from strict unimodality, with no fixed point below the cutoff, a tangency at it, and exactly two above it.

At tangency put \(x=x_*\), \(y=\phi_{T_c}(x_*)\). The fixed-point equation \(qy=x\) and maximum condition \(x+y=1+a\) yield \(x_*=q(1+a)/(1+q)\), \(y_*=(1+a)/(1+q)\). Since \(a<x_*<y_*<1\), its flight time is the separation integral
\[
 T_c=\frac1r\int_{x_*}^{y_*}\frac{dz}{z(1-z)(z-a)}.
\]
A primitive of the integrand without \(1/r\) is
\[
 F(z)=-\frac{\log z}{a}+\frac{\log(z-a)}{a(1-a)}-\frac{\log(1-z)}{1-a}.
\]
Substitution of the endpoints and simplification gives the displayed formula for \(T_c\), which is positive because the integrand is positive on \([x_*,y_*]\).

For a scalar autonomous flow, twice differentiating the first-variation identity yields
\[
 \phi_T''(x)=\frac{f(y)}{f(x)^2}\bigl(f'(y)-f'(x)\bigr),\quad y=\phi_T(x).
\]
At the critical fixed point \(qf(y_*)/f(x_*)=1\), so the return-map curvature simplifies, using \(x_*+y_*=1+a\), to
\[
 P_{T_c}''(x_*)=\frac{f'(y_*)-f'(x_*)}{f(x_*)}
 =-\frac{(1+a)(1-q)}{q(1-x_*)(x_*-a)}<0.
\]
Thus for \(u_n=x_n-x_*>0\) close to zero,
\[
 u_{n+1}=u_n-cu_n^2+O(u_n^3),\quad
 c=\frac{(1+a)(1-q)}{2q(1-x_*)(x_*-a)}>0.
\]
The monotone convergence from above to \(x_*\) follows from the strict sign of \(P_{T_c}(x)-x\) away from the two fixed points. The reciprocal difference satisfies \(u_{n+1}^{-1}-u_n^{-1}\to c\), hence \(nu_n\to c^{-1}\). Substitution of \(x_*\) reduces \(c^{-1}\) to the asserted rational expression.

Finally \(P_T\) is strictly increasing on \([0,1]\), so no periodic orbit of period greater than one is possible and every forward orbit converges to a fixed point. The signs of \(P_T(x)-x\) on the three intervals between \(0,x_-,x_+\) establish the global basins and stability claims. The fixed points are simple when \(T>T_c\), making the larger attracting and the smaller repelling.

## Verification
The accompanying script `verify.py` checks the exact symbolic tangency and curvature identities, conducts 24 independently integrated flow-versus-return-map root-count comparisons at twelve admissible parameters, and tests convergence toward the reciprocal-iteration critical coefficient. Numerical tests are not a substitute for the all-parameter analytical proof.

An exact worked example is \(a=1/2\), \(q=3/4\), \(r=1\), for which
\[
 x_*=\frac9{14},\quad y_*=\frac67,\quad
 T_c=\log\left(\frac{140625}{1024}\right),\quad
 \lim_{n\to\infty}n(x_n-x_*)=\frac{10}{49}
\]
for every post-pulse initial stock \(x_0>x_*\) at the critical interval.

## Relationship to prior work
Stier and coauthors (2022) use a depensatory population-growth term of the same cubic type and study simulated state-dependent, observation-based annual fishery policies. Here the intervention is instead an exactly periodic proportional kick, and the conclusions are a closed-form, all-initial-condition deterministic threshold, two-basin classification and critical rate.

The 2020 *Theoretical Ecology* paper on threshold harvesting contrasts threshold, quota and proportional harvest in **discrete growth maps** and includes strong-Allee scenarios; it does not, in its model and conclusions inspected, give this formula for the exact continuous cubic-Allee flow between pulses. Meyer and coauthors (arXiv:2308.14167) prove broad local ODE-to-flow-kick continuation statements and illustrate **additive** kicks of a quadratic logistic population. Such general local bifurcation results explain why saddle nodes occur, but do not establish uniqueness for every positive interval, the precise global cutoff, the cubic expression, or the universal reciprocal relaxation amplitude. The claim is specifically the complete sharpened result for this explicit pulse–flow system, not a discovery of pulse harvesting or saddle-node theory.

## Limitations
The exact numerical threshold uses noise-free cubic growth, fixed pulse spacing and constant proportional retention. It does not establish stochastic survival probabilities, the economic optimality of a harvest policy, sensitivity to environmental variation or adaptive thresholds. Earlier specialist results on impulsive strong-Allee harvest systems might contain an equivalent formulation; literature searches and inspections do not constitute a mathematical proof of priority. Independent replication and literature audit have not been performed.

## References
1. Stier, A. C., et al. (2022), “Avoiding critical thresholds through effective monitoring,” *Proceedings of the Royal Society B* **289**, 20220526. DOI: 10.1098/rspb.2022.0526. Lawful full text: https://repository.library.noaa.gov/view/noaa/60179/noaa_60179_DS1.pdf.
2. “Threshold harvesting as a conservation or exploitation strategy in population management” (2020), *Theoretical Ecology*. DOI: 10.1007/s12080-020-00465-8. https://link.springer.com/article/10.1007/s12080-020-00465-8.
3. Meyer and collaborators (2023), “Continuation of fixed points and bifurcations from ODE to flow-kick disturbance models,” arXiv:2308.14167, https://arxiv.org/pdf/2308.14167.
