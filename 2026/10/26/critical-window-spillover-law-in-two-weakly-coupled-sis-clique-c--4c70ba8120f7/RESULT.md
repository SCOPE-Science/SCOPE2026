# Critical-window spillover law in two weakly coupled SIS clique communities

## Finding
For the discrete-time independent-infection-product SIS map on two cliques, a community which is exactly at its isolated infection threshold has an endemic infection probability of order \(\sqrt{\varepsilon}\) when transmission from a supercritical community has strength \(\varepsilon\). This is distinct from the order-\(\varepsilon\) infection of a strictly subcritical community. The transition admits an explicit finite-width crossover when the satellite's local reproduction ratio differs from one by order \(\sqrt{\varepsilon}\).

Precisely, take integers \(r>s\ge2\) and \(0<\delta<1\), and define \(\beta=\delta/(s-1)\). Let \(x_*\in(0,1)\) be the unique positive root of
\[
x=1-\bigl(1-(1-\delta)x\bigr)(1-\beta x)^{r-1}.
\]
Set
\[
q=\delta(1-\delta)+\frac{\delta^2(s-2)}{2(s-1)}>0,\qquad B=r\beta x_*>0.
\]
For every sufficiently small \(\varepsilon>0\), the coupled system specified below has a unique positive fixed point, is globally attracted to it from every nonzero infection vector, and its values are constant in each clique, \(x(\varepsilon),y(\varepsilon)\). The following regimes hold:

1. **Subcritical satellite.** If \(0<\kappa<1\) is fixed, then \(y(\varepsilon)/\varepsilon\to B/[\delta(1-\kappa)]\).
2. **Critical satellite.** If \(\kappa=1\), then \(y(\varepsilon)/\sqrt{\varepsilon}\to\sqrt{B/q}\).
3. **Supercritical satellite.** If \(1<\kappa<1/\beta\) is fixed, then \(y(\varepsilon)\to y_\kappa>0\), the unique positive isolated satellite equilibrium.
4. **Complete critical window.** For every fixed real \(c\), let \(\kappa(\varepsilon)=1+c\sqrt{\varepsilon}\). Then
\[
\lim_{\varepsilon\downarrow0}\frac{y(\varepsilon)}{\sqrt{\varepsilon}}
=Z(c)=\frac{\delta c+\sqrt{\delta^2c^2+4qB}}{2q}.
\]
In all cases \(x(\varepsilon)\to x_*\). More precisely, whenever \(\kappa(\varepsilon)\) converges to an admissible positive limit,
\[
x(\varepsilon)-x_*\sim \frac{s\beta(1-x_*)}{1-f'_r(x_*)}\,\varepsilon y(\varepsilon),
\]
where \(f_r(x)=1-(1-(1-\delta)x)(1-\beta x)^{r-1}\). The coefficient is strictly positive. Thus the feedback on the supercritical core is of order \(\varepsilon^{3/2}\) at the local critical point.

## Assumptions and scope
The network consists of a complete graph with \(r\) core vertices and another complete graph with \(s\) satellite vertices. Every core-to-satellite pair is joined by an edge. At each step a vertex independently receives infection from each infected neighbor; the transmission probability along core edges is \(\beta\), along satellite edges is \(\kappa\beta\), and along cross edges is \(\varepsilon\beta\). The probability of retaining an infection is \(1-\delta\). The state is the deterministic vector of node infection probabilities \(p\in[0,1]^{r+s}\), updated by
\[
F_i(p)=1-\bigl(1-(1-\delta)p_i\bigr)\prod_{j\sim i}(1-b_{ij}p_j).
\]
Assume \(\kappa>0\), \(\kappa\beta<1\), and \(0<\varepsilon\beta<1\). At the critical window these bounds hold for all sufficiently small positive \(\varepsilon\), for every fixed \(c\).

This is an **independent-state deterministic approximation**, not a claim of positive stationarity for the finite stochastic SIS Markov chain. The weighted-edge generalization is part of the present setup; the motivating source treats homogeneous transmission probabilities.

## Proof
**1. Global existence, uniqueness, attraction, and symmetry.** Write each coordinate as a union probability \(F_i(p)=1-\prod_{j\in\{i\}\cup N(i)}(1-a_{ij}p_j)\), with \(a_{ii}=1-\delta\) and \(a_{ij}=b_{ij}>0\) along edges. Thus \(F\) is order-preserving. For every strictly positive \(p\) and \(0<t<1\), each scalar function \(u\mapsto1-\prod_j(1-u a_{ij}p_j)\) is strictly concave for \(0\le u\le1\): its second derivative equals minus the sum of nonnegative pair products, at least one strictly positive. Consequently \(F(tp)>tF(p)\) componentwise.

The Jacobian \(DF(0)=(1-\delta)I+W\), where \(W\) is the nonnegative symmetric weighted adjacency matrix. It is irreducible when \(\varepsilon>0\), and its spectral radius is strictly larger than the isolated core's \(1-\delta+(r-1)\beta>1\). If \(v>0\) is a Perron vector, then sufficiently small multiples \(tv\) satisfy \(F(tv)>tv\). Also \(F(\mathbf1)<\mathbf1\). Iterating these two ordered bounds gives a positive fixed point. If two positive fixed points existed, scaling one down to first contact with the other and applying strict subhomogeneity would contradict fixedness. The same monotone bounds and eventual positivity of \(F(p)\) for every nonzero \(p\) prove convergence from every such initial vector. Because the fixed point is unique, permutations within each clique preserve it, hence its coordinates are constant within the cliques.

**2. Exact reduced fixed-point equations.** With clique probabilities \(x,y\), the map becomes
\[
\begin{aligned}
x&=1-\bigl(1-(1-\delta)x\bigr)(1-\beta x)^{r-1}(1-\varepsilon\beta y)^s,\\
y&=1-\bigl(1-(1-\delta)y\bigr)(1-\kappa\beta y)^{s-1}(1-\varepsilon\beta x)^r.
\end{aligned}
\]
The isolated core map \(f_r\) is strictly increasing and strictly concave, has derivative \(f'_r(0)=1-\delta+(r-1)\beta>1\), and satisfies \(f_r(1)<1\). Its unique positive fixed point is \(x_*\), with \(0<f'_r(x_*)<1\). The first coupled equation and monotonicity imply \(x(\varepsilon)\ge x_*\). As \(\varepsilon\downarrow0\), compactness forces every limit point to solve \(x=f_r(x)\), and the lower bound excludes zero. Hence \(x(\varepsilon)\to x_*\). Taylor expanding the first equation at \((x_*,\varepsilon y=0)\) gives
\[
(1-f'_r(x_*))(x-x_*)=s\beta(1-x_*)\varepsilon y+o(\varepsilon y),
\]
which proves the claimed core-feedback equivalent.

**3. Satellite limits.** At \(\varepsilon=0\), the isolated satellite map has derivative \(1+\delta(\kappa-1)\) at zero and is strictly concave. Thus it has no positive fixed point for \(\kappa\le1\), and exactly one positive fixed point \(y_\kappa\) for \(\kappa>1\). For fixed \(\kappa>1\), coupling increases the satellite update; hence \(y(\varepsilon)\ge y_\kappa\). Compactness and uniqueness then yield \(y(\varepsilon)\to y_\kappa\). For \(\kappa\le1\), and for \(\kappa(\varepsilon)\to1\), the satellite limit is zero.

The satellite fixed-point residual has the uniform small-parameter expansion, with \(\kappa\to1\), \(y\to0\), and \(x\to x_*\),
\[
0=B\varepsilon+\delta(\kappa-1)y-qy^2+o\bigl(\varepsilon+|\kappa-1|y+y^2\bigr).
\]
Indeed, the constant forcing comes from \(1-(1-\varepsilon\beta x)^r=r\beta x_*\varepsilon+o(\varepsilon)\), the linear isolated coefficient is exactly \(\delta(\kappa-1)\), and the quadratic coefficient at \(\kappa=1\) is \(-q\). When \(\kappa=1+c\sqrt{\varepsilon}\), the negative quadratic term bounds \(y=O(\sqrt{\varepsilon})\). Dividing by \(\varepsilon\), every limit point of \(y/\sqrt{\varepsilon}\) solves \(qz^2-\delta cz-B=0\); the constant \(-B<0\) excludes zero and the quadratic has exactly one positive root, \(Z(c)\). This yields the complete crossover. The critical law is the case \(c=0\). For fixed \(\kappa<1\), expanding instead with its strictly negative isolated linear coefficient gives \(0=B\varepsilon-\delta(1-\kappa)y+o(\varepsilon+y)\), proving the linear leakage law.

## Verification
`verify.py` uses only Python's standard library. It checks 53 exact rational quadratic-coefficient identities and 15 high-precision numerical comparisons across clique pairs \((3,2),(5,3),(7,4)\), fixed subcritical ratios and five-point critical-window/satellite tests (three window values and two fixed subcritical values per pair). Command: `python3 verify.py`. It prints `PASS: 53 exact coefficient identities and 15 numerical asymptotic comparisons`.

A concrete analytic example is \(r=3\), \(s=2\), \(\delta=\beta=1/2\), for which \(x_*=3-\sqrt5\), \(q=1/4\), and
\[
Z(c)=c+\sqrt{c^2+6(3-\sqrt5)}.
\]
The infinite-dimensional quantifiers over clique sizes and the asymptotics as \(\varepsilon\downarrow0\) are proved analytically; numerical tests do not certify them.

## Relationship to prior work
Dung and Phuc's 2026 article introduced a community-level spectral threshold set for the homogeneous discrete-time product SIS map and demonstrated infection spread into locally less vulnerable communities. The present result does not reassert their threshold comparison: it analyzes the positive equilibrium's *size* as a weak-link parameter vanishes and as one community crosses its isolated threshold. The added satellite multiplier \(\kappa\) explicitly describes heterogeneous transmission, a modification rather than an asserted feature of their original homogeneous model.

Bonaccorsi, Ottaviano, Mugnolo and De Pellegrini (arXiv:1412.6157, especially Sections 2–4) previously studied weakly coupled communities and equitable partitions in a continuous-time NIMFA differential equation, established a global threshold, and reduced endemic calculations to a quotient graph. Their dynamical equation is polynomial and continuous-time, not the nonlinear infection-survival *product* update considered here; their reported conclusions do not state this exact finite-discrete-product crossover profile. These literatures provide strong motivation and limit claims of originality to the specific formulas and proof above. Standard forced-transcritical intuition already suggests a square-root exponent; that general intuition is not claimed as new.

## Limitations
The conclusion concerns deterministic infection-probability recurrences, not the finite stochastic epidemic's absorbing chain or a stationary endemic distribution. The topology is two fully mixed clique communities with complete weak cross-coupling, not arbitrary sparse graphs. Bounds hold as \(\varepsilon\downarrow0\) with fixed clique sizes and parameters; no uniformity in growing \(r,s\) or in unbounded \(c\) is asserted. Existing bifurcation, near-critical epidemic, and community-mean-field literature may contain equivalent specializations under different terms; independent priority review has not been performed. Nothing is claimed about optimal public-health intervention policy.

## References
1. H. P. Dung and N. H. Phuc, *An Epidemic Threshold Set for Networks*, arXiv:2607.14048v1 (first public 2026-07-15), https://arxiv.org/abs/2607.14048 ; full legal article: https://academ.us/article/2607.14048/ . Sections 2–4.
2. S. Bonaccorsi, S. Ottaviano, D. Mugnolo and F. De Pellegrini, *Epidemic Outbreaks in Networks with Equitable or Almost-Equitable Partitions*, arXiv:1412.6157v3 (2015), https://arxiv.org/abs/1412.6157 . Sections 2–4.
3. G. T. Cantwell and C. Moore, *Threshold and quasistationary distribution for the susceptible-infectious-susceptible model on networks*, Phys. Rev. E 113, 064305 (2026), https://doi.org/10.1103/385j-2f29 . Different finite-stochastic/quasistationary formulation.
