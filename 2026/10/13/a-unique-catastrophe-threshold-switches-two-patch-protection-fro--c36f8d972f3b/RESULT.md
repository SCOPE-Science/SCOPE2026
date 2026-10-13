# A unique catastrophe threshold switches two-patch protection from complementary to substitutable

## Finding
Consider the two-patch occupancy model below, with local disappearance rates \(x,y>0\), symmetric recolonization intensity \(c>0\), and a fully destructive regional-catastrophe intensity \(r\ge 0\). Starting with both patches occupied, let \(T(x,y;c,r)\) be the expected time until both are empty. Define \(s=x+y\), \(p=xy\), and
\[
\begin{aligned}
P(r)={}&r^4+(3c+2s)r^3+(3c^2+4cs+s^2+2p)r^2\\
 &+(c^3+2c^2s+cs^2+2sp)r+p(p-cs-2c^2).
\end{aligned}
\]
The mixed local-extinction sensitivity is
\[
\boxed{\displaystyle \frac{\partial^2 T}{\partial x\,\partial y}
=-\frac{2(c+r+x)(c+r+y)P(r)}{\big[r(c+r+s)^2+p(s+2c+r)\big]^3}.}
\]
The polynomial \(P\) is strictly increasing on \([0,\infty)\). Consequently, if \(p<cs+2c^2\), there is **exactly one** catastrophe threshold \(r_*>0\): lowering both local extinction rates has a positive complementary interaction for \(0\le r<r_*\), zero local interaction at \(r_*\), and a negative, substitutable interaction for \(r>r_*\). If \(p>cs+2c^2\), local protection is substitutable at every \(r\ge0\); if \(p=cs+2c^2\), the interaction vanishes only at \(r=0\) and is substitutable for \(r>0\).

In particular, with \(x=y=c=1\), the unique threshold is the positive root of \(r^4+7r^3+17r^2+13r-3=0\), namely \(r_*\approx0.183384113079255\). This is a genuine sign reversal for otherwise unchanged local extinction and recolonization rates.

## Assumptions and scope
The continuous-time chain has occupancy states \(11,10,01,00\). The state \(00\) is absorbing. In state \(11\), patches 1 and 2 disappear independently at rates \(x\) and \(y\), respectively. In state \(10\), patch 1 disappears at rate \(x\) and patch 2 is recolonized at rate \(c\); in state \(01\), patch 2 disappears at rate \(y\) and patch 1 is recolonized at rate \(c\). Independent regional catastrophes occur at rate \(r\), from any nonempty state to \(00\), including state \(11\). All clocks are exponential; the rates are time-homogeneous; \(x,y,c>0\), \(r\ge0\).

Conservation of patch 1 (respectively patch 2) means a small **absolute reduction** of \(x\) (respectively \(y\)), without changing the other rates. The local interaction is the mixed difference for two reductions, whose small-step sign equals \(\partial^2_{xy}T\). This is a statement about *local* marginal conservation payoffs; it does not assert the sign of arbitrary large finite interventions or the global optimization of budgets. Expected absorption times are finite even when \(r=0\) because local extinction rates are positive on this finite absorbing chain.

## Proof
Write \(T=T_{11}\), and let \(T_{10}\), \(T_{01}\) denote mean times to absorption from states \(10\), \(01\). First-step conditioning gives
\[
(c+x+r)T_{10}=1+cT,\qquad(c+y+r)T_{01}=1+cT,
\]
\[
(x+y+r)T=1+yT_{10}+xT_{01}.
\]
Solving, with \(s=x+y\) and \(p=xy\), yields
\[
T=\frac{N}{D},\qquad
N=(c+r+s)^2-p,\qquad
D=r(c+r+s)^2+p(s+2c+r).
\]
Both \(N\) and \(D\) are positive for all admissible parameters. For example, \(D\ge p(s+2c)>0\), so every differentiation below is legitimate, including at \(r=0\).

Differentiate \(N/D\) successively in \(x\) and \(y\). Applying the quotient rule twice and collecting powers of \(r\) produces exactly the displayed factorization
\[
D^3\,\partial_{xy}^2 T=-2(c+r+x)(c+r+y)P(r).
\]
This is an identity in \(x,y,c,r\), not a numerical extrapolation. The accompanying standalone checker verifies the polynomial identity coefficient by coefficient with integer arithmetic and separately checks the original backward equations on exact rational grids.

For every \(x,y,c>0\), the coefficients of \(r,r^2,r^3,r^4\) in \(P(r)\) are strictly positive. Hence \(P'(r)>0\) for \(r\ge0\), \(P(r)\to+\infty\) as \(r\to\infty\), and \(P(0)=p(p-cs-2c^2)\). By continuity and strict monotonicity: when \(p<cs+2c^2\), exactly one positive root exists, with \(P\) negative before and positive after it; when \(p\ge cs+2c^2\), no positive root exists. The strictly negative prefactor in the sensitivity identity reverses the sign of \(P\), establishing all cases and equality boundaries.

For finite small absolute reductions \(h,k>0\), the protection-interaction difference is
\[
\begin{aligned}
& T(x-h,y-k;c,r)-T(x-h,y;c,r)\\
&\quad-T(x,y-k;c,r)+T(x,y;c,r)
=\int_{x-h}^{x}\!\int_{y-k}^{y}\partial_{uv}^2T(u,v;c,r)\,dv\,du.
\end{aligned}
\]
Because \(T\) is smooth on positive rates, away from the threshold this finite difference has the same sign as the mixed derivative for all sufficiently small \(h,k\). At the threshold the leading interaction vanishes; no finite-intervention sign is asserted there.

For \(x=y=c=1\), substituting \(s=2,p=1\) gives \(P(r)=r^4+7r^3+17r^2+13r-3\). Its unique positive zero lies between \(0\) and \(1\), and exact rational evaluations in the verifier yield a positive finite protection interaction at \(r=0\) and negative one at \(r=1\).

## Verification
The standalone standard-library Python file `check_claim.py` independently defines multivariate polynomials for the backward-equation numerator, denominator and \(P\), and checks that the mixed-derivative identity is the zero polynomial after multiplication by its positive denominator. It also checks 54 rational first-step cases and independently exhibits the complementary/substitutable finite-step signs at the two witness hazard values. Run `python3 check_claim.py` from the extracted package directory; successful execution prints `VERIFY_OK formal_coefficients= 22 formal_derivative=1 first_step_cases= 54 protection_signs= 2 certificate=exact`. The general result rests on the algebraic identity and positivity proof; the finite cases are supplementary reproducibility checks.

## Relationship to prior work
Etienne and Heesterbeek (2001) developed stochastic patch-occupancy conservation rules, comparing local extinction and colonization interventions. Johst and Drechsler (2003) investigated correlated ecological disturbances and mean extinction time. Haight and Travis (online 2007) optimized habitat allocation for an individual-based simulation of metapopulation persistence, while Ross and Pollett (2010) considered management rules for metapopulations. These motivate marginal interventions and catastrophe dependence, but the explicit two-parameter mixed-extinction-rate sensitivity, its unique catastrophe-rate sign reversal, and the complete algebraic classification above were not found in the reviewed accessible material. In particular, the backward-equation method, the exact rational mean-time formula and qualitative advantages of habitat protection are **not** claimed as new.

## Limitations
The result applies to a minimal, symmetric-colonization, continuous-time Markov occupancy model started with two occupied patches. It does not establish finite-horizon persistence probabilities, consequences for three or more patches, empirical causal complementarity, or the effects of nonlinear density dependence. The mixed-sensitivity sign concerns infinitesimal reductions, not arbitrary budget changes. A closely relevant stochastic-patch-management article was accessible only by abstract; potential equivalent earlier sensitivity formulas in its inaccessible full text remain an originality risk. A relevant disturbance article was also available only in abstract.

## References
1. R. S. Etienne and J. A. P. Heesterbeek (2001), *Rules of Thumb for Conservation of Metapopulations Based on a Stochastic Winking-Patch Model*, The American Naturalist, DOI `10.1086/321986`.
2. K. Johst and M. Drechsler (first published 21 October 2003), *Are Spatially Correlated or Uncorrelated Disturbance Regimes Better for the Survival of Species?*, Oikos 103, 449–456, DOI `10.1034/j.1600-0706.2003.12770.x`.
3. R. G. Haight and L. E. Travis (first published online 15 March 2007), *Reserve Design to Maximize Species Persistence*, Environmental Modeling & Assessment 13, 243–253, DOI `10.1007/s10666-007-9088-4`.
4. J. V. Ross and P. K. Pollett (2010), *Simple Rules for Ranking and Optimally Managing Metapopulations*, Ecological Modelling, DOI `10.1016/j.ecolmodel.2010.02.016`.
