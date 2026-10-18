# A sharp variation-diminishing law for richness–trait covariance under finite rarefaction

## Finding

A richness–trait association can reverse its direction as sampling effort increases, even within one fixed ecological community. Its oscillation is sharply limited by **the number of distinct species-abundance levels**, independently of the number of species or the magnitudes of their traits. The bound is attained by arbitrarily large communities. Thus the sample-size sensitivity of joint richness and community-weighted-mean analysis has an exact finite-population structural constraint.

Let \(r\) be the number of distinct positive species-abundance values. Delete all zeros from the finite sequence of covariances \(\operatorname{Cov}(K_m,T_m)\) for sample sizes \(m=2,\ldots,N-1\), and count changes of sign between consecutive remaining terms. There are at most \(\max(0,r-2)\) changes. If \(r=1\), every covariance is zero. If \(r=2\), its nonzero sign is independent of sample depth.

The stronger bound uses cumulative *abundance-weighted trait imbalances*: when distinct abundances are sorted from largest to smallest, put \(b_j=\sum_{i:a_i=\alpha_j}a_i(t_i-\mu)\) and \(B_j=\sum_{h=1}^{j}b_h\). The number of covariance sign reversals is no greater than the number of sign reversals among nonzero \(B_1,\ldots,B_{r-1}\). Both bounds are exact, not asymptotic.

If traits are nondecreasing with abundance, covariance is nonpositive at every sample depth; if traits are nonincreasing, covariance is nonnegative at every sample depth. Two or more reversals are possible only with at least four abundance levels and a correspondingly nonmonotone trait–abundance relationship.

## Assumptions and scope

Fix a finite collection of \(N\ge2\) individually distinguishable organisms assigned to \(s\ge1\) species. Species \(i\) has integer abundance \(a_i\ge1\), with \(\sum_{i=1}^s a_i=N\), and all its organisms share a fixed real trait value \(t_i\). Draw exactly \(m\) distinct organisms uniformly among the \(\binom{N}{m}\) possibilities, for \(1\le m\le N\). Let \(I_i\) be the detection indicator of species \(i\), so \(K_m=\sum_i I_i\), and let \(T_m\) be the arithmetic average of the \(m\) sampled individual traits. Hence \(\mathbb{E}[T_m]=\mu=\sum_i a_it_i/N\). This is an abundance-weighted mean in the *sample*, not an unweighted average of traits across detected species. Sampling is exchangeable without replacement and there is no detection error.

Write \(\binom{x}{k}=0\) unless \(x\ge k\ge0\) are integers. For the sole-species case, terms such as \(\binom{-1}{m-1}\) also have this zero convention. All displayed denominators are positive for the stated range.

## Proof

**Exact covariance identity.** The probability that species \(i\) is undetected is \(q_i=\binom{N-a_i}{m}/\binom{N}{m}\). When \(a_i<N\), the conditional mean trait given its absence is \(\mu_{-i}=(N\mu-a_it_i)/(N-a_i)\). Consequently,

\[\operatorname{Cov}(I_i,T_m)=q_i(\mu-\mu_{-i})=\frac{a_i(t_i-\mu)}{N}\,\frac{\binom{N-a_i-1}{m-1}}{\binom{N-1}{m-1}}.\]

When \(a_i=N\), its indicator is constant and both sides vanish. Summing over species proves

\[\boxed{\operatorname{Cov}(K_m,T_m)=\frac{1}{N\binom{N-1}{m-1}}\sum_{i=1}^s a_i(t_i-\mu)\binom{N-a_i-1}{m-1}.}\]

At \(m=1\), the numerator is \(\sum_i a_i(t_i-\mu)=0\); at \(m=N\), every binomial coefficient in the numerator vanishes.

**Variation bound.** List distinct abundance levels in *decreasing* order \(\alpha_1>\alpha_2>\cdots>\alpha_r\) and set \(n_j=N-\alpha_j-1\), giving \(n_1<n_2<\cdots<n_r\). Group the species coefficients at each level:

\[b_j=\sum_{i:a_i=\alpha_j}a_i(t_i-\mu),\qquad \sum_{j=1}^r b_j=0.\]

Set \(B_j=\sum_{\ell=1}^j b_\ell\) for \(1\le j<r\). For any \(m\ge2\), summation by parts and Pascal's identity give the exact numerator decomposition

\[\sum_{j=1}^r b_j\binom{n_j}{m-1}=-\sum_{j=1}^{r-1}B_j\sum_{h=n_j}^{n_{j+1}-1}\binom{h}{m-2}.\]

The rectangular Pascal matrix with row \(k\), column \(h\), and entry \(\binom{h}{k}\) is **totally nonnegative**: its minors are counts of suitable nonintersecting directed lattice-path families, via the standard planar-path determinant argument. (Equivalently, this is the classical total positivity of the Pascal kernel.) Summing its consecutive, disjoint, ordered columns into the intervals \([n_j,n_{j+1}-1]\) preserves total nonnegativity. Indeed, the interval-membership matrix has every minor nonnegative because its column supports are consecutive and ordered; the Cauchy–Binet formula then proves total nonnegativity of the product.

The standard variation-diminishing theorem for totally nonnegative matrices says that multiplying a real vector by such a matrix cannot increase the number of sign changes after zeros are deleted. Applying it to the displayed decomposition, and noting the denominator is positive, gives

\[\operatorname{var}(\operatorname{Cov}(K_2,T_2),\ldots,\operatorname{Cov}(K_{N-1},T_{N-1}))\le\operatorname{var}(B_1,\ldots,B_{r-1})\le\max(0,r-2).\]

For \(r=1\), all coefficients at the sole level sum to zero, so the covariance is identically zero; the bound remains valid.

**Sharpness for every number of levels.** Fix any integer \(r\ge2\) and take exactly \(r\) species with abundances \(a_i=i\), hence \(N=r(r+1)/2\). The \(r\times r\) matrix \(M_{m,i}=\binom{N-i-1}{m-1}\), with \(1\le m,i\le r\), is invertible: the row polynomials \(\binom{x}{0},\ldots,\binom{x}{r-1}\) form a basis of polynomials of degree less than \(r\), evaluated at the \(r\) distinct nodes \(N-i-1\). Solve uniquely for rational \(b_1,\ldots,b_r\) from

\[\sum_i M_{1,i}b_i=0,\qquad \sum_i M_{m,i}b_i=(-1)^m\quad(2\le m\le r).\]

The first equality says \(\sum_i b_i=0\). Assign \(t_i=c+b_i/i\), with a common constant \(c\) large enough to make every trait strictly positive. Then \(\mu=c\), and the covariance numerator equals \((-1)^m\) for \(m=2,\ldots,r\). It therefore exhibits \(r-2\) strict reversals. The proof applies to arbitrary \(r\), without extrapolation from computations.

**A concrete two-reversal community.** Take \(N=10\), abundances \((1,2,3,4)\), and positive traits \((56,1/2,181/3,28)\). The abundance-weighted population mean trait is \(\mu=35\). The four numerator coefficients in ascending abundance order are \((21,-69,76,-28)\). For sample sizes one through ten, the covariance numerator is exactly \((0,1,-1,1,55,155,181,99,21,0)\). Dividing by the positive normalization gives

\[\operatorname{Cov}(K_2,T_2)=\frac{1}{90},\quad \operatorname{Cov}(K_3,T_3)=-\frac1{360},\quad \operatorname{Cov}(K_4,T_4)=\frac1{840}.\]

These are two consecutive strict sign reversals.

**Monotone-abundance corollary.** For \(m\ge2\), the covariance identity equals the weighted covariance of \(t_i\) with the factor \(h_m(a_i)=\binom{N-a_i-1}{m-1}/\binom{N-1}{m-1}\), using weights \(a_i/N\). The function \(h_m\) is nonincreasing in abundance. The weighted two-sample rearrangement identity therefore makes the covariance nonpositive if traits are nondecreasing with abundance, and nonnegative if traits are nonincreasing. At \(m=1\), it is zero already.

## Verification

The accompanying standard-library program `verify.py` and its exact output `certificate.json` provide independent checks of the covariance formula by enumerating labeled subsets and computing moments directly, separately from the algebraic formula. There are 1,245 exact paired calculations across all 65 positive-integer abundance profiles of sizes 2 through 8 with three deterministic trait profiles each. The checker tests 195 sign-variation bounds, 1,370 monotone-trait sign inequalities, explicit strict sharpness witnesses for 2 through 8 abundance levels, and the independent 10-individual subset enumeration for the two-reversal example. All comparisons use Python `fractions.Fraction` and yield exact equalities or strict inequalities. Run `python3 verify.py` and compare its JSON output byte-for-byte with `certificate.json` (the packaged certificate records the output using a final newline). The infinite theorem rests on the proof above, not finite testing.

## Relationship to prior work

Heck, van Belle and Simberloff (1975) derived classical finite-population rarefaction mean and variance formulas for species richness, but the accessible abstract does not state the cross-covariance with sampled-individual mean traits or a sampling-depth sign-variation theorem. Paine, Baraloto and Díaz (2015) studied how functional-trait sampling intensity affects estimation accuracy; an accessible summary addresses trait-measurement error, not an exact richness–trait covariance variation bound, although its complete text was not inspected. Zelený (2016) and Hawkins and collaborators (2017) document structural associations and potential spurious correlations between assemblage richness and aggregated traits, particularly across sites. Their examined models concern assemblage comparisons, geographic co-occurrence or association bias rather than sequential fixed-community hypergeometric samples with an individual-abundance-weighted trait mean. The 2017 open-access article's introduction, methods, results and discussion were inspected.

The total-nonnegativity and variation-diminishing tools are classical, as in Pinkus (2009) and the Pascal-matrix literature; those general facts are explicitly **not** claimed as new. The specific application, exact covariance identity, cumulative-trait coefficient criterion, all-population sharpness construction and monotone-abundance consequences are the mathematical claim. The original technical literature may contain an equivalent under terms such as finite-population occupancy, hypergeometric survey covariance or trait-diversity dependence; independent bibliographic review remains necessary.

## Limitations

The analysis requires fixed species labels, fixed organism-level trait values, uniform sampling without replacement, and the mean trait weighted by the sampled **individuals**. It does not address richness covariances with presence-weighted trait averages, unknown abundances, preferential detection, or spatially clustered sampling. A sign reversal concerns population sampling variability, not ecological causation. The bound counts changes after zero covariances are removed; no claim is made about zeros themselves or about the exact location of changes. Two existing source texts were not fully accessible; this limits certainty about bibliographic novelty, not the algebraic proof. Independent scientific audit has not been performed.

## References

1. Heck, K. L., Jr., van Belle, G., and Simberloff, D. (1975), *Explicit Calculation of the Rarefaction Diversity Measurement and the Determination of Sufficient Sample Size*, Ecology 56, 1459–1461. https://doi.org/10.2307/1934716 (first publicly dated October 1, 1975).
2. Paine, C. E. T., Baraloto, C., and Díaz, S. (2015), *Optimal strategies for sampling functional traits in species-rich forests*, Functional Ecology 29, 1325–1331. https://doi.org/10.1111/1365-2435.12433.
3. Zelený, D. (2016 preprint), *Bias in community-weighted mean analysis of plant functional traits and species indicator values*. https://www.researchgate.net/publication/327821875_Bias_in_community-weighted_mean_analysis_of_plant_functional_traits_and_species_indicator_values.
4. Hawkins, B. A. et al. (2017), *Structural bias in aggregated species-level variables driven by repeated species co-occurrences*, Journal of Biogeography. https://doi.org/10.1111/jbi.12953. Author-accessible technical paper: https://borea.mnhn.fr/sites/default/files/pdfs/2017%20Hawkins%20et%20al.%20-%20Journal%20of%20Biogeography.pdf.
5. Pinkus, A. (2009), *Totally Positive Matrices*, chapter 3, Variation diminishing. https://doi.org/10.1017/CBO9780511691713.004.
6. Kersey, S. N. (2013), *Invertibility of Submatrices of Pascal's Matrix and Birkhoff Interpolation*. https://arxiv.org/abs/1303.6159.
