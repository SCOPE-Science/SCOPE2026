# An irreversible co-detection sign switch under incidence-based rarefaction

## Finding
Let \(U\) be a finite collection of \(N\ge2\) sampling units, and let \(A,B\subsetneq U\) be nonempty sets of units occupied by two designated species. For each \(m\in\{1,\ldots,N\}\), select an \(m\)-element subset of \(U\) uniformly without replacement. Denote by \(I_A(m)\) and \(I_B(m)\) the indicators that the selected units detect the respective species, and put \(C_m=\operatorname{Cov}(I_A(m),I_B(m))\).

**Irreversibility and exact criterion.** As \(m\) increases, the nonzero signs of \(C_m\), if both signs occur, are positive first and negative afterward. Strict signs of both kinds occur **if and only if** neither incidence set contains the other and
\[
N|A\cap B|>|A||B|.
\]
Thus a nonpositive one-unit co-detection association can never become positive merely by pooling additional uniformly selected units. A positive association can become negative, but cannot become positive again after doing so.

**Sharp onset.** Five sampling units are necessary and sufficient for both signs to occur. At \(N=5\), the only possibilities, up to exchange of the species and permutation of units, have incidence parameters \((|A|,|B|,|A\cap B|)=(2,2,1)\) or \((3,3,2)\). Their exact covariance sequences for \(m=1,\ldots,5\) are respectively
\[
(1/25,1/100,-1/100,0,0),\qquad (1/25,-1/100,0,0,0).
\]
These two patterns are complementary incidence sets.

**Unbounded family.** For every \(N\ge5\), take two two-unit incidence sets sharing exactly one unit. Then \(C_m>0\) for \(1\le m\le N-3\), \(C_{N-2}<0\), and \(C_{N-1}=C_N=0\). Hence the sole sign reversal can occur at arbitrarily late sampling depths.

## Assumptions and scope
The presence/absence matrix is fixed, and sampling units (for example, quadrats or survey visits) are distinct and uniformly selected without replacement. Detection is perfect at an occupied unit. No assumption of independence among species at a unit is made. The statement concerns the covariance of their **pooled-detection indicators**, not the covariance of biological occurrence processes or the spatial co-occurrence score on the full matrix. All sets are labeled for sampling; species names and unit labels do not matter to the formulas.

Set \(r=|A|\), \(s=|B|\), \(a=|A\cap B|\), and \(u=r+s-a=|A\cup B|\). Necessarily \(1\le r,s<N\) and \(\max(0,r+s-N)\le a\le\min(r,s)\). The equality and degenerate cases are included in the theorem, and signs of zero covariance are ignored when counting strict sign changes.

## Proof
**1. Exact covariance.** For \(0\le t\le N\) define
\[
q_t(m)=\frac{\binom{N-t}{m}}{\binom{N}{m}},
\]
where the numerator is zero when \(m>N-t\). This is the probability of missing every unit in a fixed occupied set of size \(t\). By inclusion–exclusion, \(\mathbb E[I_A]=1-q_r\), \(\mathbb E[I_B]=1-q_s\), and \(\mathbb E[I_AI_B]=1-q_r-q_s+q_u\). Therefore
\[
\boxed{C_m=q_u(m)-q_r(m)q_s(m).}
\]
In particular, \(C_1=(Na-rs)/N^2\).

**2. Nested sets never give a negative covariance.** If \(A\subseteq B\), then \(I_A\le I_B\) pointwise and \(I_AI_B=I_A\). Consequently \(C_m=\Pr(I_A=1)[1-\Pr(I_B=1)]\ge0\). The other inclusion direction is symmetric.

**3. Nonnested sets force a negative covariance.** Suppose \(a<\min(r,s)\), so \(u>\max(r,s)\). At sample size \(m_*=N-u+1\), no sample can miss both species, hence \(q_u(m_*)=0\). But \(m_*\le N-r\) and \(m_*\le N-s\), hence both \(q_r(m_*)\) and \(q_s(m_*)\) are positive. Thus \(C_{m_*}<0\). For \(m>N-\max(r,s)\), at least one species is detected with probability one, so \(C_m=0\).

**4. Only one direction of strict sign change is possible.** For \(0\le m\le N-u\), the joint-miss probability and the two marginal miss probabilities are positive. Put
\[
R_m=\frac{q_u(m)}{q_r(m)q_s(m)},\qquad R_0=1.
\]
Direct cancellation of successive binomial ratios gives, for \(0\le t<N-u\),
\[
\frac{R_{t+1}}{R_t}
=\frac{(N-u-t)(N-t)}{(N-r-t)(N-s-t)},
\]
and hence
\[
\frac{R_{t+1}}{R_t}-1
=\frac{a(N-t)-rs}{(N-r-t)(N-s-t)}.
\]
All denominators are positive. The numerator is nonincreasing in \(t\), so the multiplicative increments of \(R_m\) first are at least one and later at most one, with at most one change of regime. Since \(R_0=1\), the sequence can cross the level one from above to below at most once and cannot cross back. As \(\operatorname{sgn}C_m=\operatorname{sgn}(R_m-1)\) on this range, and the remaining nonzero covariances (if any) are strictly negative by step 3, the entire nonzero sign sequence has the claimed order.

For nonnested sets, \(C_1>0\) exactly when \(Na>rs\), while step 3 supplies a later negative value. If \(Na\le rs\), the first multiplier is at most one and all later multipliers also are at most one; no positive value can occur. Combined with step 2, this proves the equivalence criterion.

**5. Sharp five-unit threshold and classification.** A nonnested pair with positive \(C_1\) must have \(a\ge1\), \(r,s\ge a+1\), and \(Na>rs\ge(a+1)^2\). Therefore \(N>a+2+1/a\ge4\), so \(N\ge5\). When \(N=5\), the bounds \(r,s\le4\), \(r,s\ge a+1\), and \(5a>rs\) leave only \(a=1,r=s=2\) and \(a=2,r=s=3\), up to swapping. Substitution into the covariance identity yields the two sequences in the finding.

**6. Family at every larger scale.** Take \(r=s=2\), \(a=1\), and write \(x=N-m\). Elementary simplification gives
\[
\boxed{C_m=\frac{x(x-1)(N-x)((N-2)x-2(N-1))}{N^2(N-1)^2(N-2)}.}
\]
For \(N\ge5\), the last numerator factor is positive for integer \(x\ge3\), negative at \(x=2\), and the full expression vanishes at \(x=1,0\). This establishes the claimed sign sequence for all \(N\ge5\).

## Verification
Run `python3 verify_incidence_covariance.py` in the directory containing `verification_certificate.json`. The self-contained program uses exact Python rational arithmetic and computes co-detection covariances two independent ways: the binomial formula and exhaustive enumeration of site subsets. It evaluates every feasible overlap parameter triple with nonempty proper incidence sets and unordered species sizes for \(N=2,\ldots,10\), checking every sample depth, with 3,774 exact direct-comparison checks across 460 parameter triples. It also verifies the explicit unbounded-family polynomial and signs for \(N=5,\ldots,100\) (5,040 exact checks). The expected summary is provided in `verification_certificate.json`. The theorem for arbitrary \(N\) is proved by steps 1–6, not extrapolated from these computations.

## Relationship to prior work
Colwell, Mao, and Chang (2004) analyze sample-based species accumulation and its expectation from incidence frequencies, and Chao and collaborators' 2014 Appendix C develops incidence-based rarefaction formulas. Their formulas motivate treating a random subcollection of sampling units as the natural sampling experiment. Trejo-Barocio and Arita (2013) and Arita (2015) study co-occurrence and covariance on fixed species–site incidence matrices, including the overlap \(a\), which provides the spatial association context. The result here instead concerns covariance of **two random pooled-detection indicators** as sampling depth changes; its irreversible sign order, exact incidence-overlap criterion, and sharp five-unit onset are not consequences asserted by those cited works. The closest identified published mathematical results for occupied-box indicators and successive species discoveries concern different random variables and sampling laws.

## Limitations
The conclusion requires uniform selection of a fixed number of distinct units and perfect detection at occupied units. Nonuniform site inclusion, replacement sampling, time dependence, and false-negative observations are not covered. In a real biological system, a positive or negative pooled-detection covariance need not identify positive or negative ecological interaction; the change can arise from survey geometry alone. The result concerns two fixed species at a time and does not constrain how the total variance of multispecies richness varies. An equivalent theorem in the broader sampling or finite-population literature has not been independently ruled out.

## References
1. Colwell, R. K., Mao, C. X., and Chang, J. (2004). *Interpolating, extrapolating, and comparing incidence-based species accumulation curves*. Ecology 85:2717–2727. DOI: 10.1890/03-0557. Publicly available from October 1, 2004. Full text: https://www.robertkcolwell.org/publications/7532.pdf
2. Trejo-Barocio, P., and Arita, H. T. (2013). *The co-occurrence of species and the co-diversity of sites in neutral models of biodiversity*. PLOS ONE 8:e79918. DOI: 10.1371/journal.pone.0079918. Full text: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0079918
3. Chao, A., Gotelli, N. J., Hsieh, T. C., et al. (2014). *Rarefaction and extrapolation with Hill numbers: a framework for sampling and estimation in species diversity studies*. Ecological Monographs 84:45–67. DOI: 10.1890/13-0133.1. Appendix C: https://www.esapubs.org/archive/mono/M084/003/appendix-C.pdf
4. Arita, H. T. (2017; first online November 19, 2015). *Multisite and multispecies measures of overlap, co-occurrence, and co-diversity*. Ecography 40:709–718. DOI: 10.1111/ecog.01942. Full text: https://nsojournals.onlinelibrary.wiley.com/doi/pdf/10.1111/ecog.01942
