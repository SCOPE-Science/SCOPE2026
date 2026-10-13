# Universal intermediate-colonization peak in the relative variability of extinction time

## Finding

A connected finite landscape with at least two patches exhibits a universal intermediate-rate amplification of the **squared coefficient of variation of total extinction time** when colonization starts from one occupied patch. For every initial patch \(v\), the statistic

\[
C_v(\lambda)=\frac{\operatorname{Var}(T_v(\lambda))}{(\mathbb E T_v(\lambda))^2}
\]

has \(C_v(0)=1\), has derivative \(\deg_G(v)/(2\mu)>0\) at zero, and tends to \(1\) as colonization tends to infinity. Consequently, it has a finite interior global maximum strictly exceeding \(1\). In the minimal two-patch landscape, its exact profile is

\[
C_v(\lambda)=1+\frac{2r}{(r+2)^2},\qquad r=\frac{\lambda}{\mu},
\]

which peaks uniquely at \(r=2\), with value \(5/4\). The theorem asserts existence, not uniqueness, of an interior peak for general graphs.

## Assumptions and scope

Let \(G=(V,E)\) be a fixed finite, connected, simple undirected graph with \(n=|V|\ge2\). Each patch is either occupied or empty. Independently, each occupied vertex empties at rate \(\mu>0\). For every edge from an occupied vertex to an empty vertex, a colonization event occurs at rate \(\lambda\ge0\). The union of all such events defines a continuous-time Markov chain on subsets of \(V\); the empty state is absorbing. At time zero, exactly one specified vertex \(v\in V\) is occupied. Define \(T_v(\lambda)\) to be the first hitting time of the empty state. There is no immigration from outside the landscape, no heterogeneity in rates, and no simultaneous multi-patch jumps.

All moments of \(T_v(\lambda)\) are finite for each finite \(\lambda\): from every nonempty state a finite sequence of deaths has positive probability, and the transient finite-state generator is invertible. In what follows \(C_v\) always denotes the **variance of the extinction time divided by the square of its mean**. It is not a coefficient of variation of population abundance.

## Proof

**1. Rational moment equations and small-colonization expansion.** For each nonempty occupied set \(S\), write \(m_S(\lambda)=\mathbb E_S T\) and \(s_S(\lambda)=\mathbb E_S T^2\). The generator equations, with \(m_\varnothing=s_\varnothing=0\), are

\[
\begin{aligned}
&|S|\mu m_S-\mu\sum_{u\in S}m_{S\setminus\{u\}}
 +\lambda\sum_{w\notin S}b_S(w)(m_S-m_{S\cup\{w\}})=1,\\
&|S|\mu s_S-\mu\sum_{u\in S}s_{S\setminus\{u\}}
 +\lambda\sum_{w\notin S}b_S(w)(s_S-s_{S\cup\{w\}})=2m_S,
\end{aligned}
\]

where \(b_S(w)=|\{u\in S:\{u,w\}\in E\}|\). For a fixed graph these finite linear systems have rational solutions in \(\lambda\), analytic near \(\lambda=0\).

At zero colonization the initially occupied patches die independently, each after an exponential waiting time of rate \(\mu\). Thus a singleton has \(m_{\{v\}}(0)=1/\mu\), \(s_{\{v\}}(0)=2/\mu^2\), while any occupied pair has \(m_{\{u,v\}}(0)=3/(2\mu)\) and \(s_{\{u,v\}}(0)=7/(2\mu^2)\). Denote the degree of \(v\) by \(d\). Applying the backward equations only at the initial singleton gives

\[
\begin{aligned}
(\mu+d\lambda)m_{\{v\}}&=1+\lambda\sum_{u\sim v}m_{\{u,v\}},\\
(\mu+d\lambda)s_{\{v\}}&=2m_{\{v\}}+\lambda\sum_{u\sim v}s_{\{u,v\}}.
\end{aligned}
\]

Differentiation at zero yields \(m'_{\{v\}}(0)=d/(2\mu^2)\) and \(s'_{\{v\}}(0)=5d/(2\mu^3)\). Since \(C_v=s_{\{v\}}/m_{\{v\}}^2-1\),

\[
C_v(\lambda)=1+\frac{d}{2\mu}\lambda+O(\lambda^2).
\]

Connectedness and \(n\ge2\) imply \(d\ge1\), hence \(C_v(\lambda)>1\) for all sufficiently small positive \(\lambda\).

**2. High-colonization limit by full-state renewal.** Fix \(G\) and \(\mu\). Let \(F=V\) denote full occupancy. From any nonempty proper subset there is at least one occupied-empty edge, since \(G\) is connected. Therefore the total birth rate is at least \(\lambda\) and the total death rate at most \(n\mu\). Starting at any such state, the probability that the next \(n-1\) events needed to fill the graph are all births is at least

\[
p_\lambda=\left(\frac{\lambda}{\lambda+n\mu}\right)^{n-1}.
\]

(If full occupancy is reached earlier, the event has already succeeded.) The strong Markov property gives a geometric bound in blocks of \(n-1\) jumps on the number of jumps needed to hit \(\{F,\varnothing\}\). Holding times before this hit are stochastically bounded by exponentials of rate \(\lambda\), so the hitting time \(H_\lambda\) satisfies \(\sup_S\mathbb E_S H_\lambda^2=O(\lambda^{-2})\) as \(\lambda\to\infty\). The probability of hitting \(\varnothing\) before \(F\) is at most \(1-p_\lambda=O(\lambda^{-1})\), uniformly over nonempty proper starting states.

From \(F\), define one *cycle* as the holding time \(E\sim\operatorname{Exp}(n\mu)\) until the first death, followed by the excursion from the resulting nonempty proper state until hitting \(F\) again or extinction. This uses \(n\ge2\). Let \(X_\lambda\) be the cycle duration, and let \(Z_\lambda=1\) if that cycle ends in extinction. The cycles are iid by the strong Markov property. Put \(\varepsilon_\lambda=\Pr(Z_\lambda=1)\), \(a_\lambda=\mathbb E X_\lambda\), and \(b_\lambda=\mathbb E X_\lambda^2\). The preceding bounds show \(\varepsilon_\lambda\to0\), \(a_\lambda\ge1/(n\mu)\), and \(\sup_{\lambda\ge\lambda_0}b_\lambda<\infty\) for any sufficiently large \(\lambda_0\). Write \(T_F\) for extinction time from full occupancy. The first-cycle recursions give exactly

\[
\mathbb E T_F=\frac{a_\lambda}{\varepsilon_\lambda},\qquad
\mathbb E T_F^2=\frac{b_\lambda}{\varepsilon_\lambda}
+\frac{2a_\lambda\mathbb E[X_\lambda\mathbf 1_{\{Z_\lambda=0\}}]}{\varepsilon_\lambda^2}.
\]

Cauchy--Schwarz yields \(\mathbb E[X_\lambda\mathbf1_{\{Z_\lambda=1\}}]\le\sqrt{b_\lambda\varepsilon_\lambda}\to0\). After division by \((\mathbb E T_F)^2\), the first term vanishes and the second tends to \(2\). Hence \(\operatorname{Var}(T_F)/(\mathbb E T_F)^2\to1\).

For a singleton start, stop first upon hitting \(\{F,\varnothing\}\). The stopping time has second moment \(O(\lambda^{-2})\), and absorption before hitting \(F\) has probability \(O(\lambda^{-1})\). By the strong Markov property, on hitting \(F\) the remaining extinction time is an independent copy of \(T_F\). Since \(\mathbb E T_F\to\infty\), its first two moments dominate those of the initial approach. Thus \(\mathbb E T_v/\mathbb E T_F\to1\) and \(\mathbb E T_v^2/(\mathbb E T_F)^2\to2\). Therefore \(C_v(\lambda)\to1\).

**3. Interior attainment.** The rational moment equations make \(C_v\) continuous for all \(\lambda\ge0\). Its value at zero is \(1\), a small positive rate has a value strictly greater than \(1\), and its high-rate limit is \(1\). By continuity on a sufficiently large compact interval, a global maximum exceeding \(1\) is attained at some finite \(\lambda>0\).

**4. Minimal exact landscape.** For the two-vertex edge put \(r=\lambda/\mu\). Rescale time by \(\mu\). With one patch initially occupied, the two nonempty occupancy sizes are states \(1\) and \(2\), with transitions \(1\to0\) at rate \(1\), \(1\to2\) at rate \(r\), and \(2\to1\) at rate \(2\). Solving the two backward systems gives

\[
\mathbb E T=1+\frac r2,\qquad \mathbb E T^2=2+\frac{5r}{2}+\frac{r^2}{2},
\]

in time units \(\mu^{-1}\). Therefore \(C_v=1+2r/(r+2)^2\), whose derivative is \(2(2-r)/(r+2)^3\). It increases up to \(r=2\), decreases thereafter, and its maximum is \(5/4\).

## Verification

A standalone Python 3 checker, `verify_extinction_cv.py`, uses exact fractions with no third-party dependencies. Run `python3 verify_extinction_cv.py`. It evaluates the small-rate first and second moment derivatives on all labeled connected simple graphs with two through five vertices (counts \(1,4,38,728\)), checks the two-patch moment formula at seven exact rates, and independently solves additional three- and four-patch moment systems at two rates. Its expected output begins with `VERIFY_OK`. These finite checks are supplementary: the proof of the universal claim is the analytic argument above, not finite enumeration.

## Relationship to prior work

The finite contact process and its extinction time are standard; see Mountford, Mourrat, Valesin and Yao (2012) and Schapira and Valesin (2015). Their exponential extinction-time limits concern **graph order growing at a fixed infection/colonization rate**, primarily from full occupancy. The theorem here instead fixes an arbitrary graph, varies the colonization rate from zero to infinity, starts from a singleton, and derives a universal first-order coefficient plus existence of a finite interior peak in extinction-time relative variance. The large-rate renewal step is related in spirit to classical metastability, not claimed as an independently new asymptotic theory.

Drake and Griffen (2013) study source-sink fragmentation and ecological variability. Their reported coefficient of variation measures **abundance over time**, not the cross-replicate coefficient of variation of the random time to complete extinction. These different random variables cannot be substituted for one another. The explicit two-patch calculation also must not be confused with optimizing the *mean* extinction time under a directional colonization budget.

## Limitations

No universal peak location, uniqueness of peaks, or global inequality \(C_v(\lambda)\ge1\) at every positive rate is asserted for general graphs. The colonization rate is homogeneous, the graph is finite and connected, extinction is absorbing, and the initial state is a singleton. The result is theoretical and does not imply that field datasets will detect the peak or that variation of abundance has the same pattern. Any inaccessible or unindexed earlier exact finite-state calculations could narrow the novelty of the special two-patch formula.

## References

1. T. Mountford, J.-C. Mourrat, D. Valesin, and Q. Yao, *Exponential extinction time of the contact process on finite graphs*, arXiv:1203.2972v1 (public 2012-03-13), https://arxiv.org/abs/1203.2972.
2. B. Schapira and D. Valesin, *Extinction time for the contact process on general graphs*, arXiv:1509.04133v1 (public 2015-09-14), https://arxiv.org/abs/1509.04133.
3. J. M. Drake and B. D. Griffen, *Experimental demonstration of accelerated extinction in source-sink metapopulations*, Ecology and Evolution 3 (2013), 3369–3378, https://pmc.ncbi.nlm.nih.gov/articles/PMC3797484/.
