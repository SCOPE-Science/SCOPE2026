# A sharp inverse-power strategyproofness frontier for three agents and two facilities

## Finding

For every metric space \((X,d)\), every triple of agents with privately reported locations, and every exponent \(p\ge0\), consider the following two-facility mechanism. If at most two distinct sites are reported, open at every such site. Otherwise, write \(r_i=\min_{j\ne i}d(x_i,x_j)>0\), omit report \(i\) with probability
\[
P_i(p)=\frac{r_i^{-p}}{\sum_{j=1}^3r_j^{-p}},
\]
and place a facility at each of the other two reports.

**Theorem.** This mechanism is strategyproof in expectation on **every metric space** if and only if \(0\le p\le3\). For every \(p>3\), there is a strictly profitable unilateral deviation by one of three agents on the real line.

For the optimal universally strategyproof exponent \(p=3\), its exact worst-case ratio of expected total distance to optimal two-facility total distance is
\[
\rho_3=\frac{2+t_*^2}{2+t_*^3}=\frac{2}{3t_*}\approx1.0652744484818826,
\qquad t_*^3+6t_*=4,\quad0<t_*<1.
\]
Within the entire inverse-power family \(p\ge0\), exponent \(3\) uniquely minimizes the worst-case ratio among mechanisms strategyproof on every metric space with three agents. The word *optimal* here refers only to this parametrized family, not to all randomized two-facility mechanisms.

## Assumptions and scope

Exactly three agents are present, two facilities are allowed, and each agent's disutility is the distance from their true location to the nearest facility. The ambient metric space is arbitrary (not necessarily geodesic); reports can be any points in that metric space. Strategyproofness refers to no reduction in expected distance by a unilateral report change, with all other reports fixed. The exponent is fixed independently of reports. Degenerate profiles with at most two distinct reported positions are handled by the special clause above.

The ratio is \(\sup_{\mathrm{OPT}_2>0}\mathbb E[\mathrm{SC}]/\mathrm{OPT}_2\). When \(\mathrm{OPT}_2=0\), the mechanism has zero cost. Values of \(p\) outside \([0,3]\) are not claimed strategyproof. Nothing is claimed for more than three agents, coalition-proofness, or mechanisms outside the inverse-power family.

## Proof

**1. An analytic local inequality.** For three distinct *reported* sites labelled \(z,y_1,y_2\), set \(u=d(z,y_1)\), \(v=d(z,y_2)\), \(w=d(y_1,y_2)\), and assume \(u\le v\) by symmetry. Let \(r=u\) and \(P\) be the probability of omitting the agent reporting \(z\). Consider a differentiable variation in \(u,v\) with \(|\dot u|,|\dot v|\le1\), holding \(w\) fixed. The probability is locally Lipschitz and differentiable almost everywhere, including across changes of the nearest-neighbor relation. We prove for every \(0\le p\le3\):
\[
1-P+r\dot P\ge0. \tag{1}
\]

There are three exhaustive regions (boundary equalities follow by continuity and the almost-everywhere argument).

* If \(w\le u\le v\), then both other reports are each other's nearest neighbor. Thus \(P=(1+2(u/w)^p)^{-1}\le1/3\) and \(r\dot P=-pP(1-P)\dot u\ge-pP(1-P)\). Hence (1) follows from \(pP\le1\).
* If \(u\le w\le v\), the nearest distances are \((u,u,w)\). Writing \(Q=(u/w)^p/(2+(u/w)^p)\), the third agent's omission probability, we have \(P=(2+(u/w)^p)^{-1}\), \(Q\le1/3\), and \(r\dot P=-pPQ\dot u\ge-pPQ\). Since \(1-P=P+Q\ge P\ge3PQ\), (1) follows.
* If \(u\le v\le w\), the nearest distances are \((u,u,v)\). Let \(t=u/v\in(0,1]\), \(a=t^p\in(0,1]\), \(P=(2+a)^{-1}\), and \(Q=a/(2+a)\). Differentiation gives \(r\dot P=pPQ(t\dot v-\dot u)\ge-pPQ(1+t)\ge-6PQ\). The inequality \(6PQ\le1-P\) is equivalent to \((1+a)(2+a)\ge6a\), or \((1-a)(2-a)\ge0\). Thus (1) holds.

**2. Global strategyproofness without geodesics.** Fix an agent at true site \(x\), and other reported sites \(y_1,y_2\). If there are at most two distinct original reports, all reports are covered and truthful cost is zero. Assume all three true reports are distinct. Set \(R=\min_jd(x,y_j)>0\) and let \(x'\) be an arbitrary false report, at distance \(h=d(x,x')\). Under truthfulness the cost is \(RP(0)\le R\). If \(h\ge R\), every potential facility is at least \(R\) from \(x\), so the deviation cannot improve the expected cost. If \(0<h<R\), all reports remain distinct and when the false report is selected the agent's true cost is exactly \(h\); when it is omitted the true cost is \(R\).

Write \(a_j=d(x,y_j)\), \(b_j=d(x',y_j)\). For \(s\in[0,h]\) introduce *numerical distance interpolants* \(u_j(s)=a_j+s(b_j-a_j)/h\). They need not be realized by locations. The reverse triangle inequality gives \(|u_j'(s)|\le1\) and \(\min_j u_j(s)\ge R-s>0\); the other-report distance \(w=d(y_1,y_2)\) stays fixed. Define \(P(s)\) from these three nearest-distance weights, and \(C(s)=s+(R-s)P(s)\). This continuous, piecewise differentiable function has \(C(0)\) equal to truthful cost and \(C(h)\) equal to deviating cost. Almost everywhere,
\[
C'(s)=1-P(s)+(R-s)P'(s).
\]
When \(P'(s)\ge0\), this is nonnegative. When \(P'(s)<0\), use \(R-s\le r(s)=\min_j u_j(s)\) and (1):
\[
C'(s)\ge1-P(s)+r(s)P'(s)\ge0.
\]
Absolute continuity now gives \(C(h)\ge C(0)\), proving strategyproofness for every \(p\in[0,3]\) on any metric space.

**3. Sharp failure for every exponent above three.** Put three true locations on a line at \(-1,0,1+\varepsilon\), with \(\varepsilon>0\), and let the middle agent report \(h>0\). For \(0<h<\varepsilon/2\), her old nearest distance is \(1\), her post-report nearest distance is \(1+h\), and the other nearest distances after deviation are \(1+h\) and \(1+\varepsilon-h\). Her omission probability and true expected cost are therefore
\[
P_{\varepsilon}(h)=\left[2+\left(\frac{1+h}{1+\varepsilon-h}\right)^p\right]^{-1},\qquad
C_{\varepsilon}(h)=h+(1-h)P_{\varepsilon}(h).
\]
As \(\varepsilon\downarrow0\), the right derivative \(C_{\varepsilon}'(0)\) tends to \(\frac23-\frac{2p}{9}=\frac{2(3-p)}9\), negative whenever \(p>3\). Continuity gives a sufficiently small positive \(\varepsilon\) and then \(0<h<\varepsilon/2\) with \(C_{\varepsilon}(h)<C_{\varepsilon}(0)\). Hence no exponent \(p>3\) is universally strategyproof. This completes the sharp classification.

**4. Exact and optimally tuned welfare ratio.** In any three-distinct-report profile, choose a closest pair at distance \(a>0\). Their nearest-neighbor distances are both \(a\); the remaining one's nearest distance is \(b\ge a\). Two facilities have optimal social cost exactly \(a\), since some two agents must share a facility and the triangle inequality lower-bounds their joint cost by their mutual distance, while choosing a closest-pair endpoint and the third site attains \(a\). Put \(t=a/b\in(0,1]\). Direct expectation yields, for every \(p\ge0\),
\[
\frac{\mathbb E[\mathrm{SC}]}{\mathrm{OPT}_2}
=F_p(t)=\frac{2+t^{p-1}}{2+t^p}.
\]
Every \(t\in(0,1]\) is realized on the real line by reports \((0,t,t+1)\). At \(p=3\), differentiating \(F_3\) gives a numerator with sign \(4-6t-t^3\); it changes sign exactly once, at the unique root \(t_*\in(0,1)\), hence this is the global maximum. The stationary equation simplifies \(F_3(t_*)=2/(3t_*)\). For each fixed \(0<t<1\), the function \(F_p(t)\) is strictly decreasing in \(p\), since
\[
\frac{\partial F_p(t)}{\partial p}
=\frac{2t^{p-1}(1-t)\log t}{(2+t^p)^2}<0.
\]
For every \(p<3\), evaluating at \(t_*\) makes its worst-case ratio strictly larger than the \(p=3\) ratio. Since larger exponents are not universally strategyproof, \(3\) is the unique optimal exponent within this family.

## Verification

The accompanying `verify_inverse_power.py` performs exact rational comparisons for \(p=0,1,2,3\) on all \(5^6=15625\) labelled four-point complete graphs with integer edge weights from \(1\) through \(5\), using shortest-path metric closure. The total is \(62500\) truthful-versus-deviating comparisons, with report positions corresponding to four labelled points; none violates strategyproofness. It also checks a strict rational manipulation example for \(p=4\) using \(\varepsilon=1/100\) and \(h=1/1000\), and brackets the unique cubic root by exact rationals. Run `python3 verify_inverse_power.py` with standard-library Python. These finite checks are ancillary; they do not establish the universal quantifiers or the real-exponent boundary, which follow from the proof above.

## Relationship to prior work

Escoffier, Gourvès, Nguyen, Pascual, and Spanjaard (2011) established a strategyproof inverse-nearest-neighbor **first-power** mechanism for arbitrary populations with one omitted report. Chan, Lin, and Wang (2026, Section 4 and Theorem 3) proved the **second-power** version strategyproof for arbitrary populations, with its exact approximation ratio. These results do not imply truthfulness of the third-power rule: it is a different report-dependent probability distribution, not a fixed-probability convex mixture of the first- and second-power rules. The present theorem resolves the *full power-parameter frontier specifically for three agents* and calculates the best corresponding welfare ratio. The 2026 paper's multiple-facility section and its cited prior mechanism were compared directly; there is no claim of priority over possible unpublished or unindexed results.

## Limitations

The theorem is for exactly three agents and two facilities; the cubic exponent is not asserted strategyproof when the population is larger. Strategyproofness is individual and in expectation, not group-strategyproof. The welfare optimum is only among inverse-nearest-neighbor power rules with exponents fixed independently of profiles. A 2011 preprint was identified but its complete text was not retrieved in this review, leaving a residual priority-comparison risk despite the explicit 2026 description of its first-power contribution. Independent mathematical validation remains to be performed.

## References

1. H. Chan, J. Lin, and C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484, first submitted 2026-08-23. Full HTML, Section 4 and Theorem 3: https://arxiv.org/html/2608.22484
2. B. Escoffier, L. Gourvès, K. T. Nguyen, F. Pascual, and O. Spanjaard, *Strategy-Proof Mechanisms for Facility Location Games with Many Facilities*, Algorithmic Decision Theory (2011), pp. 67–81, DOI: 10.1007/978-3-642-24873-3_6. Open-author manuscript index: https://datamove.imag.fr/kimthang.nguyen/Papers/SP-multi-lncs.pdf
