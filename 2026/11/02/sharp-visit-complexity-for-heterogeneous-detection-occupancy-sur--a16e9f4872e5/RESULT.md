# Sharp visit complexity for heterogeneous-detection occupancy surveys with unequal efforts

## Finding
Consider a closed ecological survey of sites that are either unoccupied or occupied, with no false-positive detections. Among occupied sites, the detection process has at most \(k\) distinct positive Poisson detection intensities; the mixing weights, intensities, and site-occupancy fraction are unknown. Each visit records only presence or nondetection, but its fixed positive observation duration is known and may differ from other visits.

**Sharp design theorem.** For \(k\geq1\) and positive visit durations \(d_1,\ldots,d_n\), let
\[
\mathcal T(d)=\left\{\sum_{j\in S}d_j:\varnothing\ne S\subseteq\{1,\ldots,n\}\right\}.
\]
The complete labeled binary-history distribution identifies the occupancy probability, every positive detection intensity, and all class weights (up to relabeling) **for every parameter point in the \(k\)-class model if and only if**
\[
\boxed{|\mathcal T(d)|\geq 2k.}
\]
Consequently the smallest number of visits for which any positive-duration design is globally identifying is
\[
\boxed{n_{\min}(k)=\left\lceil\log_2(2k+1)\right\rceil.}
\]
Durations proportional to \(1,2,4,\ldots,2^{n-1}\) attain the bound, and can be rescaled to **any prescribed positive total survey duration**. In contrast, when all visits have equal duration, global identification requires at least \(2k\) visits, and \(2k\) visits suffice.

For exactly two positive detection classes, three visits identify the entire model if and only if the three durations are **not all equal**. In particular, the schedules proportional to \((1,1,2)\) and \((1,1,1,1)\) are both identifying and may use the same total duration, but the schedule \((1,1,1)\) is not identifying. The statement is structural identification from an exact population distribution, not a guarantee of precise finite-sample inference.

## Assumptions and scope
A randomly chosen site has class \(0\) (unoccupied) with probability \(\alpha_0=1-\sum_{i=1}^{k}\alpha_i\in(0,1)\). For the full \(k\)-class model assume \(\alpha_i>0\) and pairwise distinct \(\lambda_i>0\) for \(i=1,\ldots,k\). Equivalently, the occupancy probability is \(\psi=\sum_i\alpha_i\in(0,1)\), and the conditional class fractions are \(\alpha_i/\psi\). Distinct positive intensities are identifiable only up to permutation. The number \(k\) is fixed or is a valid finite upper bound. Sites are independent replicates, occupancy and detection class do not change during the survey, each duration \(d_j>0\) is recorded, and conditional on class \(i\) the \(n\) visits have independent Poisson detection counts with mean \(\lambda_i d_j\). Only each visit's indicator of at least one detection is retained; there are no false positives, false negatives beyond Poisson nondetection, visit-specific latent random effects, or misrecorded durations. The theorem addresses global injectivity of the map to the complete \(2^n\)-cell binary-history distribution, not the distribution of the total number of positive visits alone.

## Proof
**1. All joint absence probabilities are Laplace samples.** Let \(Y_j\in\{0,1\}\) indicate a detection on visit \(j\). For each subset \(S\), the probability of no detections on every visit in \(S\) is
\[
F\!\left(\sum_{j\in S}d_j\right)=\alpha_0+\sum_{i=1}^k\alpha_i e^{-\lambda_i\sum_{j\in S}d_j},\qquad
F(0)=1.
\]
All \(2^n\) binary-history probabilities determine these absence probabilities by summation. Conversely inclusion-exclusion reconstructs every binary-history probability from the same absence probabilities. Thus the data and the values \(F(t)\) at \(t\in\mathcal T(d)\cup\{0\}\) contain exactly the same information.

**2. Sharp sufficiency.** Suppose two distinct parameter measures agree at \(0\) and at at least \(2k\) different positive durations. Their transform difference is an exponential polynomial with at most \(2k+1\) distinct real exponents (the fixed zero-intensity class and at most \(2k\) positive rates). A nonzero linear combination of \(L\) real exponentials with pairwise distinct exponents has at most \(L-1\) distinct real zeros. For completeness, multiply by the reciprocal of one exponential, differentiate, apply Rolle's theorem, and induct on \(L\). The difference therefore cannot have \(2k+1\) distinct zeros unless identically zero. Exponential functions with distinct exponents are linearly independent, so equal transforms imply identical atoms and weights, with the zero-rate atom specifically giving unoccupied mass. This proves global identification, including \(\psi\).

**3. Sharp necessity.** Sort the positive rates to remove label ambiguity. The full \(k\)-class parameter domain then contains a nonempty open set of dimension \(2k\): the \(k\) positive masses with sum below one and the \(k\) ordered rates. If \(m=|\mathcal T(d)|<2k\), the joint law factors continuously through only \(m\) numbers \(F(t)\), \(t\in\mathcal T(d)\). An open subset of \(\mathbb R^{2k}\) cannot have a continuous injective map into \(\mathbb R^m\) for \(m<2k\): compose such a map with the standard embedding into \(\mathbb R^{2k}\) and contradict invariance of domain, since the image would lie in a lower-dimensional affine subspace. Consequently the model is not globally identifiable. This argument is about the full open parameter family; it does not assert that every individual parameter value has a nontrivial fiber.

**4. Optimal visit count and equal-effort boundary.** Any \(n\) binary visits have at most \(2^n-1\) distinct positive subset sums, so \(2^n-1\geq2k\) is necessary. The durations \(d_j=h2^{j-1}\) have distinct subset sums \(h,2h,\ldots,(2^n-1)h\), attaining the upper bound for any \(h>0\). For a prescribed total effort \(D>0\), put \(h=D/(2^n-1)\). When all durations are equal to \(h\), the only positive subset sums are \(h,2h,\ldots,nh\); hence the exact requirement becomes \(n\geq2k\). Scaling durations by any positive constant preserves the distinct-subset-sum count, so the comparison concerns visit count at equal total survey duration, not a promised increase in statistical precision.

**5. Three-visit classification for two detection classes.** If all three durations equal \(d\), there are precisely three positive subset sums, fewer than four. If the ordered durations satisfy \(a<b\leq c\), the four sums \(a,b,a+b,a+b+c\) are strictly increasing. If \(a=b<c\), the four sums \(a,2a,a+c,2a+c\) are strictly increasing. Thus every non-equal triple has at least four distinct positive subset sums and is globally identifying.

**6. Constructive inversion when durations are binary weighted.** With \(d_j=h2^{j-1}\), write \(x_i=e^{-h\lambda_i}\in(0,1)\) and \(M_r=F(hr)\). From the observed joint law one obtains \(M_0,\ldots,M_{2k}\). The differences
\[
G_r=M_r-M_{r+1}=\sum_{i=1}^k\beta_i x_i^r,\qquad
\beta_i=\alpha_i(1-x_i)>0,
\]
are known for \(r=0,\ldots,2k-1\). The Hankel matrix \(H=(G_{r+s})_{0\leq r,s<k}\) is positive definite: \(H=V\operatorname{diag}(\beta_i)V^{\mathsf T}\), where \(V_{ri}=x_i^r\) is nonsingular. Solve
\[
H(c_0,\ldots,c_{k-1})^{\mathsf T}=-(G_k,\ldots,G_{2k-1})^{\mathsf T}.
\]
The roots of \(z^k+\sum_{j=0}^{k-1}c_jz^j\) are precisely the \(x_i\). Vandermonde inversion of \(G_0,\ldots,G_{k-1}\) gives the \(\beta_i\), then \(\alpha_i=\beta_i/(1-x_i)\), \(\alpha_0=1-\sum_i\alpha_i\), \(\psi=1-\alpha_0\), and \(\lambda_i=-\log(x_i)/h\). This is an exact algebraic recovery recipe, not a numerically stable estimator claim.

## Verification
The included standalone script `verify.py` uses exact rational arithmetic. It reconstructs Hankel recurrence coefficients and class weights for \(k=1,2,3,4\) with identifying binary visit designs; checks all binary-history probabilities and the corresponding subset-absence moments; and confirms the visit-count combinatorics for \(k=1,\ldots,10\). It constructs two distinct two-class parameter measures with identical laws under three equal visits:
\[
(\alpha_0;\ (x_i,\alpha_i)_{i=1}^2)
=\left(\frac15;\left(\frac34,\frac25\right),\left(\frac14,\frac25\right)\right)
\]
and
\[
\left(\frac{39}{250};\left(\frac45,\frac{75}{182}\right),\left(\frac9{34},\frac{4913}{11375}\right)\right),
\]
where \(x_i\) is the nondetection probability at unit effort and each population has a different occupancy probability: \(4/5\) versus \(211/250\). The unequal-duration \((1,1,2)\) design separates these laws. The general theorem and the necessity statement are proved analytically; finite tests do not establish either universal claim.

## Relationship to prior work
MacKenzie et al. (2002) introduced estimation of site occupancy under imperfect detection. MacKenzie and Royle (2005) analyzed repeat-survey designs and variance-based allocation of effort, and Royle (2006) explicitly studied heterogeneous detection as a zero-inflated binomial mixture, including nonidentifiability issues. Hwang, Stoklosa, and Chen (2022) studied heterogeneity and conditional likelihood for occupancy data and considered zero-inflated binomial models. Those models motivate the exact ecological question here. Classical finite exponential-sum uniqueness and Hankel/Prony reconstruction are used as mathematical tools and are not claimed to be new.

The specific result asserted here is the sharp **subset-sum necessary-and-sufficient condition for complete binary visit histories**, and its exact consequences for minimum visit count, equal-duration designs, arbitrary total survey effort, and the two-class three-visit boundary. The comparison is of mathematical implications rather than terminology: standard equal-effort zero-inflated binomial laws observe only \(n+1\) count categories, whereas duration-labeled binary histories at distinct efforts encode up to \(2^n\) independent cells. A sufficiently general published theorem on finite-mixture identification from arbitrary binary exposure designs could subsume this result; no such dominating statement was identified in the examined accessible materials.

## Limitations
The fixed known finite bound on the number of detection classes, independent Poisson detection over disjoint visits, stable site occupancy, known duration-proportional rate model, and absence of false positives are essential. Unknown nonparametric continuous detection heterogeneity is not identified by a finite number of binary visits. An arbitrarily small perturbation away from equal durations can restore strict identification but be exceedingly ill-conditioned; structural identifiability is not estimability, efficiency, or usable statistical power. Increasing total duration is not required for the visit-count theorem, but field logistics, effort costs, visit-specific weather and behavior, and sample size determine whether unequal visits help in practice. The result is not a claim of priority over general Prony reconstruction or of an independently audited finding.

## References
- MacKenzie, D. I., et al. (2002), *Estimating site occupancy rates when detection probabilities are less than one*, Ecology 83, 2248–2255. First published 2002-08-01. DOI: 10.1890/0012-9658(2002)083[2248:ESORWD]2.0.CO;2.
- MacKenzie, D. I., and J. A. Royle (2005), *Designing occupancy studies: general advice and allocating survey effort*, Journal of Applied Ecology 42, 1105–1114. DOI: 10.1111/j.1365-2664.2005.01098.x.
- Royle, J. A. (2006), *Site occupancy models with heterogeneous detection probabilities*, Biometrics 62, 97–102. First posted 2005-09-28. DOI: 10.1111/j.1541-0420.2005.00439.x.
- Hwang, W.-H., J. Stoklosa, and L.-F. Chen (2022), *On site occupancy models with heterogeneity*, arXiv:2204.00126, especially Section 3.
