# Exact survival–retention phase boundary for short-horizon seed-bank advantage

## Finding

Fix a proportion of safe establishment sites \(s\in(0,1)\), local parental-seed retention probability \(r\in(0,1)\), dormant-seed annual survival \(b\in(0,1]\), and germination probability \(g\in[0,1]\). For the precisely specified two-year descendant expectation \(E_2\) in the saturated-site, one-year dormancy model of Satterthwaite [1], introduce the competition ratio

\[
h=\frac{s(1-r)}r>0,\qquad b_*(h)=\frac{2h^2+6h+4}{h^2+5h+5}.
\]

**Theorem (complete short-horizon phase classification).** For each fixed \(h>0\) and \(0<b\le1\), there exists a partially dormant strategy \(0<g<1\) with \(E_2(h,b,g)>1\) **if and only if** \(b>b_*(h)\). If \(b\le b_*(h)\), every \(0\le g<1\) instead satisfies \(E_2(h,b,g)<1\); complete germination \(g=1\) gives \(E_2=1\) exactly. Moreover \(b_*(h)\) is strictly increasing on positive \(h\), with \(\lim_{h\downarrow0}b_*(h)=4/5\) and \(\lim_{h\to\infty}b_*(h)=2\). Thus \(4/5\) is the *sharp universal* dormant-seed survival floor for any two-year advantage in this model. There is no advantage for any physically allowed \(b\le1\) when

\[
h\ge\frac{\sqrt5-1}{2}.
\]

The threshold is a rigorous statement about the original model's **finite two-year expected number of mutant-occupied sites**, not about long-run invasion exponents, stable germination rates, or actual field populations.

For instance, \(s=1/20\), \(r=1/3\), \(b=9/10\), and \(g=3/4\) give \(h=1/10\), \(b_*=462/551<9/10\), and exactly
\[
E_2-1=\frac{19650205}{6450554528}>0.
\]

## Assumptions and scope

The model is Satterthwaite's [1, analytic model] saturated-lottery limit: discrete annual generations, infinitely many or sufficiently many exchangeable sites, a fraction \(s\) suitable for occupation, one adult per occupied suitable site, uniformly dispersed non-retained seeds, fixed local retention \(r\), rare mutant and nondormant resident, fecundity large enough for seed-input replacement by expected values, and at most one year of dormant carryover. Its initial condition allows the first mutant adult to arrive with previously dormant mutant sibling seeds in its home-site bank. The source's probability calculations, not its finite-site stochastic simulation or the separate no-initial-seed-bank appendix, define the present object.

Write \(t=1-g\), \(K=1+h\), and \(z=g+bt=1-(1-b)t\). All terms in the source's first analytic expression for the expected occupied mutant sites at year two reduce to

\[
 A=\frac z{z+h},\quad B=\frac{zh}{K},\quad
 D=\frac g{g+h}+\frac{gh}{K},\quad C=\frac{bt}{K+bt},
\]
\[
 E_2=A(A+B)+BD+(1-A)C.
\]

These formulas are dimensionless exact algebraic rewritings of the source's locally retained home-site establishment, new-site founding, second-generation founding and dormant recapture probabilities. In particular, the baseline \(E_2(h,b,1)=1\) is exact. The result is only about whether **there exists** a viable partial-dormancy \(g\) whose finite two-year expectation exceeds this baseline; it does not assert the maximizing \(g\) is unique.

## Proof

**1. Threshold at complete germination.** Differentiation at \(t=0\), with \(g=1-t\), gives

\[
\left.\frac{\partial E_2}{\partial t}\right|_{t=0}
=\frac h{(1+h)^3}\Big[b(h^2+5h+5)-(2h^2+6h+4)\Big].
\]

Therefore \(b>b_*(h)\) makes this derivative positive; some sufficiently small \(t>0\) has \(E_2>1\), proving the 'if' direction.

**2. Survival monotonicity.** At fixed \(h>0\), \(0<t\le1\), the expressions satisfy

\[
 A_b=\frac{th}{(z+h)^2}>0,\quad
 B_b=\frac{th}{1+h}>0,\quad
 C_b=\frac{t(1+h)}{(1+h+bt)^2}>0,
\]

while \(D\) is independent of \(b\). Since \(z=g+bt\ge bt\) and \(1+h>h\), one has \(A\ge C\). Hence

\[
\partial_b E_2=A_b(2A+B-C)+B_b(A+D)+(1-A)C_b>0.
\]

The last term is strictly positive because \(A<1\). Consequently it suffices to prove \(E_2(h,b_*(h),g)<1\) where the threshold is feasible and \(E_2(h,1,g)<1\) where it is not.

**3. Excluding all partial germination at the threshold.** Set

\[
 Q=h^2+5h+5,\quad
 U=h^2+2ht+5h+4t+5,
\]
\[
 V=h^3+h^2t+6h^2+ht+10h-t+5,
 \qquad \mathcal D=(1+h)^2(1+h-t)QUV^2.
\]

For \(h>0\), \(0\le t\le1\), the denominator \(\mathcal D\) is strictly positive. At \(b=b_*(h)\), an exact rational identity is

\[
 \mathcal D\,[1-E_2(h,b_*(h),1-t)]=h t^2 R(h,t),
\]

where \(R=\sum_{j=0}^{12}\sum_{k=0}^{4} c_{jk}h^j\binom4k t^k(1-t)^{4-k}\). The following is an exact coefficient certificate, with rows indexed by \(j=0,1,\ldots,12\) and entries by \(k=0,1,2,3,4\):

```
350, 235, 419/3, 62, 0
2750, 2165, 9941/6, 4851/4, 824
9790, 8517, 43937/6, 12429/2, 5189
20585, 76629/4, 105889/6, 64429/4, 14578
28339, 55381/2, 80299/3, 51187/2, 24219
26982, 54725/2, 54895/2, 108783/4, 26576
18378, 38363/2, 118907/6, 20226, 20333
9147, 38997/4, 20601/2, 43073/4, 11110
3355, 7237/2, 11627/3, 8237/2, 4337
896, 967, 2077/2, 4439/4, 1180
166, 177, 1129/6, 399/2, 211
19, 79/4, 41/2, 85/4, 22
1, 1, 1, 1, 1
```

All \(65\) listed coefficients are nonnegative and the last row is strictly positive. The degree-four Bernstein functions are nonnegative and sum to one on \([0,1]\). Thus \(R(h,t)>0\) for every \(h>0\) and \(0\le t\le1\), and hence \(E_2(h,b_*(h),1-t)<1\) whenever \(t>0\). The attached independent exact polynomial checker reconstructs both sides from the four displayed probabilities and verifies coefficient equality without numeric sampling.

**4. Infeasible threshold.** At \(b=1\), exact simplification yields

\[
 E_2(h,1,1-t)-1
 =\frac{h t\big[(1+h)(1-h-h^2)+t(ht-2h-1)\big]}
 {(1+h)^2(1+h-t)(1+h+t)}.
\]

For \(h\ge(\sqrt5-1)/2\), the first bracketed term is nonpositive, and \(ht-2h-1<0\) for \(0<t\le1\). Therefore \(E_2(h,1,1-t)<1\) for any \(t>0\). By monotonicity in \(b\), the same holds for every \(b<1\).

**5. Complete classification and sharp limits.** The equation \(b_*(h)=1\) is equivalent to \(h^2+h-1=0\); the unique positive root is \((\sqrt5-1)/2\). Moreover

\[
 b_*'(h)=\frac{2(2h^2+6h+5)}{(h^2+5h+5)^2}>0.
\]

For \(h<(\sqrt5-1)/2\), Step 3 followed by Step 2 proves strict failure at every \(b\le b_*(h)\); Step 1 proves existence above it. For greater \(h\), Step 4 proves failure for every admissible survival. The limiting universal value is \(\lim_{h\downarrow0}b_*(h)=4/5\). Because every \(h>0\) can arise from some \(s,r\in(0,1)\), and for each \(b>4/5\) a sufficiently small feasible \(h\) gives \(b>b_*(h)\), the floor is sharp.

## Verification

Run the included `proof_checker.py` with Python 3, using only standard-library `fractions` and `math`. It constructs exact bivariate polynomials, verifies the rational identity with \(\mathcal D\), checks the signs of all \(65\) Bernstein coefficients, and recomputes the given rational witness from the original probabilities. Execution yielded all three `PASS` lines. The checker certifies the critical nonstandard algebraic identity; the general inequality additionally follows from the displayed positive-domain and Bernstein arguments. No finite sampling is used as a substitute for an infinite proof.

## Relationship to prior work

Satterthwaite [1] derives **the exact underlying pointwise two-year formula**, identifies local seed retention and site recapture as the ecological mechanism, and reports from parameter plots that advantage fails below survival 'approximately 0.8.' The present result does **not** claim the short-horizon model or its criterion as new. It proves an explicit *necessary-and-sufficient elimination of germination probability* for every permissible safe-site fraction, seed-retention fraction and survival probability, including strict threshold equality, the universal sharp \(4/5\) bound, and a closed-form structural no-advantage boundary. These quantified global statements and a proof of their necessity were not identified in the inspected complete source. The distinction from existing pointwise formulas does not itself guarantee historical priority.

Kobayashi and Yamamura [2] study dormancy, dispersal and sib competition under a different ecological mechanism. Rees [3] treats seed timing in a distinct age/stage structure model; Pacala [4] describes neighborhood models of annuals with dormant seeds. Those adjacent results and classical rational-inequality optimization create a residual risk that a stronger published theorem implies this specialization. The claims here should be read as a precise algebraic phase classification for [1]'s stated two-year quantity, not as a new prediction of evolutionary stable strategies.

## Limitations

The established result has **no claim** about long-run fitness, evolutionary stable strategies, truly initially empty seed banks, four-year growth-ratio criteria, unsaturated habitat, finite-population fluctuations, stochastic fecundity, site correlations, or overlapping multi-year dormancy. In particular, \(E_2>1\) can be suggestive of short-horizon invader expansion but is not automatically equivalent to positive asymptotic growth. The source's pointwise probability formulas are assumed; their empirical applicability is not re-established. Existing analytic dormancy work may yield the result as a nontrivial special case through a different optimization principle, so independent historical-priority review remains necessary.

## References

1. W. H. Satterthwaite, "Competition for space can drive the evolution of dormancy in a temporally invariant environment," *Plant Ecology* 208 (2010), 167–185. First published 21 November 2009. https://doi.org/10.1007/s11258-009-9696-y.
2. Y. Kobayashi and N. Yamamura, "Evolution of Seed Dormancy Due to Sib Competition: Effect of Dispersal and Inbreeding," *Journal of Theoretical Biology* (2000). https://doi.org/10.1006/jtbi.1999.1027.
3. M. Rees, "Delayed Germination of Seeds: A Look at the Effects of Adult Longevity, the Timing of Reproduction, and Population Age/Stage Structure," *The American Naturalist* (1994). https://doi.org/10.1086/285660.
4. S. W. Pacala, "Neighborhood Models of Plant Population Dynamics. 2. Multi-Species Models of Annuals with Dormant Seeds," *The American Naturalist* (1986). https://doi.org/10.1086/284610.
