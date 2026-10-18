# Sharp three-season mean-abundance ordering in a Beverton–Holt population

## Finding

For any three strictly ordered positive seasonal multipliers \(0<a<b<c\) with \(abc>1\), consider \(x_{t+1}=r_{t\bmod 3}x_t/(1+x_t)\) on \(x_0>0\), with seasonal rates permuted from \(a,b,c\). The attracting positive 3-cycle's arithmetic mean is strictly larger for the cyclic class \((a,b,c)\) than for \((a,c,b)\). Let \(P=abc\), \(Q=P+ab+ac+a+bc+b+c+2\), and \(D=(1+a+ab)(1+b+ab)(1+a+ac)(1+c+ac)(1+b+bc)(1+c+bc)\). Their exact mean difference is \[(M_{abc}-M_{acb})=\frac{(b-a)(c-a)(c-b)(P-1)^2Q}{3D}>0.\] The two order classes have the same persistence threshold, \(P>1\). Every cyclic ordering of one or two seasons has the same time-average, so three is minimal. For \(a=t^{-1},b=t,c=t^3\), \(t\to\infty\), the ratio \(M_{abc}/M_{acb}\sim t/2\), showing an unbounded scheduling advantage. When \(P\le 1\), all positive trajectories tend to zero and neither order admits a positive 3-cycle.

## Assumptions and scope

For an integer period \(m\in\{1,2,3\}\), fix positive real fecundity multipliers \(r_0,\ldots,r_{m-1}>0\) and an initial abundance \(x_0>0\). Iterate the scalar density-regulated recruitment law
\[x_{t+1}=\frac{r_{t\bmod m}x_t}{1+x_t},\qquad t=0,1,2,\ldots.\]
It is important that this is fixed density dependence in the denominator: a varying \(r_t\) does not impose a fixed seasonal carrying capacity. The long-run cycle mean is the arithmetic mean of the \(m\) phases, not its geometric mean. When multipliers are all distinct, the six length-three permutations split into two classes under cyclic phase shift: \((a,b,c)\) and \((a,c,b)\). Strict comparison requires \(0<a<b<c\) and \(P=abc>1\); equality occurs for repeated multipliers. No stochastic extinction, harvesting, nonlinear inter-patch movement, or general \(m>3\) comparison is claimed.

## Proof

Define \(y_t=1/x_t\), which obeys the exact affine recurrence \(y_{t+1}=(y_t+1)/r_{t\bmod3}\). The three-step map has slope \(1/P\), where \(P=uvw\) for a season order \((u,v,w)\). When \(P>1\), this map is a strict contraction and has a unique positive fixed point, since its positive constant term is nonzero. Taking reciprocals gives the three globally attracting phase abundances
\[x_0^*=\frac{P-1}{1+u+uv},\qquad x_1^*=\frac{P-1}{1+v+vw},\qquad x_2^*=\frac{P-1}{1+w+wu}.\]
These equations can also be verified directly by substituting into each seasonal map, using \(P=uvw\). Consequently
\[M_{uvw}=\frac{P-1}3\left(\frac1{1+u+uv}+\frac1{1+v+vw}+\frac1{1+w+wu}\right).\]
Cyclic shifts permute these terms and do not affect the mean. Writing \(D=(1+a+ab)(1+b+ab)(1+a+ac)(1+c+ac)(1+b+bc)(1+c+bc)\), direct common-denominator reduction (verified by the exact symbolic polynomial identity in `verify.py`) yields
\[M_{abc}-M_{acb}=\frac{(b-a)(c-a)(c-b)(P-1)^2(P+ab+ac+a+bc+b+c+2)}{3D}.\]
Each factor on the right is positive for \(0<a<b<c\) and \(P>1\), proving the strict ranking. For periods one or two, all distinct arrangements differ only by cyclic phase shift; therefore the smallest possible order effect has length three.

When \(P=1\), the affine map on \(y\) is a positive translation, so \(y\to\infty\). For \(P<1\), its slope \(1/P>1\) and its constant term is positive, so again \(y\to\infty\) and \(x\to0\). Thus no positive attracting cycle exists in that regime, regardless of order.

For \(t>1\), choose \(a=t^{-1},b=t,c=t^3\). The common factor \((P-1)/3\) cancels in the ratio of the two means. Their reciprocal-denominator sums satisfy
\[\sum_{\mathrm{cyc}(a,b,c)}\frac1{1+u+uv}=\frac12+O(t^{-1}),\qquad \sum_{\mathrm{cyc}(a,c,b)}\frac1{1+u+uv}=t^{-1}+O(t^{-2}).\]
Therefore \(M_{abc}/M_{acb}\sim t/2\), which is unbounded.

## Verification

Execute `python verify.py` using Python 3 and SymPy. The script independently composes the three inverse-affine maps with exact rational arithmetic, derives their fixed points, checks every cyclic orbit phase for 55 increasing rational triples with \(P>1\), confirms the rational mean-difference identity, and symbolically certifies the polynomial numerator factorization. It also verifies the exact example \(a=1/2,b=2,c=8\): \(M_{abc}=1526/1235\), \(M_{acb}=1211/1100\), and the difference is \(36603/271700\). It prints `VERIFY_OK` if all checks succeed. These finite tests support but do not replace the displayed universal algebraic proof.

## Relationship to prior work

AlSharawi and Ben Haj Rhouma [1, §3, especially their period-three carrying-capacity example] explicitly demonstrate that **permuting seasonal carrying capacities** with constant intrinsic growth can change mean population, and pose extension to varying intrinsic growth among their questions. Hence the bare observation that order matters is not new. Yang and Sacker [2, §3 and Appendix B] prove general mean formulas and analyze attenuation/resonance relative to mean environmental carrying capacity for periodically varying fecundity and carrying capacities. Those formulas can be specialized to these scalar maps, but the paper does not state the universal ordering of two growth-permutation classes, exact positive Vandermonde factor, or unbounded ratio. The distinction is a sharp comparative result rather than a new general periodic-cycle solution. Allen and Kocic [3] investigate periodically/randomly varying population coefficients; their full text was unavailable, leaving an identifiable comparison risk. Al-Ghassani and AlSharawi [4] investigate permutation effects for **harvesting quotas and geometric mean**, not the same growth-rate permutation and arithmetic-mean criterion.

## Limitations

The result is specifically for three-stage recurrence with the same denominator \(1+x_t\) each season; varying density-dependence, carrying capacity, harvesting, or more seasons may alter the sign. The parameter family used for an unbounded ratio permits an unfavorable season \(a<1\). The formula does not imply general ecological benefits from rearranging seasons and does not model extinction probabilities. An equivalent statement could exist in less accessible literature; an independent literature audit remains outstanding.

## References

[1] Z. AlSharawi and M. Ben Haj Rhouma, "The Discrete Beverton-Holt Model with Periodic Harvesting in a Periodically Fluctuating Environment," *Advances in Difference Equations* (2010), article 215875. DOI: 10.1155/2010/215875. Full text: https://link.springer.com/article/10.1155/2010/215875. First public publication: 2010-03-08.

[2] Y. Yang and R. J. Sacker (Appendix A by C. Haskell), "Resonance and attenuation in the n-periodic Beverton–Holt equation," *Journal of Difference Equations and Applications* 19 (2013), 1174–1191. First online: 2012-10-09. DOI: 10.1080/10236198.2012.726988. Author-hosted text: https://dornsife.usc.edu/robert-sacker/wp-content/uploads/sites/256/2023/06/Yang-Sacker-BH.pdf.

[3] L. J. S. Allen and V. L. Kocic, "Resonance in Beverton–Holt population models with periodic and random coefficients," *Journal of Difference Equations and Applications* (2013), DOI: 10.1080/10236198.2013.854779. Only abstract and bibliographic information available for comparison.

[4] A. S. Al-Ghassani and Z. AlSharawi, "The effect of maps permutation on the global attractor of a periodic Beverton–Holt model," *Applied Mathematics and Computation* 370 (2020), DOI: 10.1016/j.amc.2019.124905. Abstract available: https://ideas.repec.org/a/eee/apmaco/v370y2020ics0096300319308975.html.
