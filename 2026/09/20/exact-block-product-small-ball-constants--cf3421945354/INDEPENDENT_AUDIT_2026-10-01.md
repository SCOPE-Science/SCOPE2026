# Independent audit — Exact constants and concentration centers for block-product anti-concentration

Audited at: 2026-10-01T18:04:30Z

Disposition: **passed**

## Correctness

**PASS** — The all-center identity follows because each block average has an even log-concave density and the product of independent even radially nonincreasing one-dimensional densities remains even and nonincreasing in absolute value. After \(T_m=-\log|A_m|\), the density factor is \(e^{-u}(c_m+g_m(u))\) with \(g_m\in L^1\); convolution expansion gives the leading and one-correction logarithmic coefficients. The product-density singularity and the \(L^p\) limit then follow from the same expansion and \(\Gamma((d-1)p+1)\). The stated \(-3/(20m)\) correction agrees with the fourth-cumulant Laplace expansion for a normalized uniform average. Boundary checks at \(d=1\) and \((m_1,m_2)=(2,2)\) are consistent.

## Originality

**PASS** — The directly motivating 2026 anti-concentration theorem gives the product profile and block-size scale only up to degree-dependent constants. Classical product-distribution work gives general Mellin/Meijer-G machinery but the inspected material does not state the exact concentration center, the block-specific leading and second logarithmic coefficients, or the normalized high-\(p\) limit for these centered block averages.

### equivalent_formulations

Searches: Resultary: block product anti-concentration exact concentration center small-ball constant Mellin convolution standardized Bates density high-p asymptotic; Springer--Thompson DOI 10.1137/0118065.
Evidence: Resultary returned the audited record itself as the nearest exact match; classical product-distribution literature treats general products through Mellin/Meijer-G representations.
Reasoning: No located equivalent formulation states this complete exact coefficient package for the canonical block-product extremizers.

### broader_coverage

Searches: arXiv:2609.19473; Resultary: related block-product/product-profile records.
Evidence: Abakumov--Friedland--Yomdin state optimal product-profile and block-size dependence only up to constants depending on the degree, and matching \(p\)-growth only up to constants.
Reasoning: The motivating theorem is broader in polynomial class but weaker in the exact constants asserted here, so it does not imply the audited exact asymptotics.

### exact_database_or_table

Searches: Resultary semantic search; Springer--Thompson 1970 bibliography/abstract.
Evidence: No exact constant/table matching \(B_{\mathbf m}\), the \(\delta_m\) correction, or the normalized high-\(p\) limit was located.
Reasoning: This is an analytic asymptotic claim rather than a known finite database entry; the relevant classical distribution literature was nevertheless checked for an exact tabulation.

### claim_vs_prior_implication

Searches: arXiv:2609.19473; DOI:10.1137/0118065.
Evidence: The source theorem leaves degree-dependent constants unspecified; the 1970 abstract gives product densities as Meijer G-functions for beta/gamma/Gaussian families.
Reasoning: Neither inspected prior statement mechanically yields the audited all-center assertion plus its exact two-term block-specific small-ball and high-\(p\) constants without additional analysis.

### Source inspections

- **Product-profile anti-concentration for block-structured multi-affine polynomials** (arXiv:2609.19473): NOT_COVERING at the stated exact-constant level; it explicitly says optimality only up to degree-dependent constants. Material read: Abstract and theorem-level statement exposed by the arXiv record. Trigger: Direct motivating source with the same block-product extremizers. Evidence: The abstract states block-product optimality up to constants depending only on \(d\), and matching density growth up to constants.
- **The Distribution of Products of Beta, Gamma and Gaussian Random Variables** (DOI:10.1137/0118065): GENERAL_METHOD_PRIOR_ART; no inspected statement gives the audited block-specific anti-concentration constants. Material read: Publisher abstract and reference list. Trigger: Classical Mellin/product-distribution prior art. Evidence: The abstract describes Meijer-G product densities and recursions.

Checked sources: arXiv:2609.19473; DOI:10.1137/0118065; Resultary published findings search.
Residual risks: The full text of older product-distribution literature was not exhaustively inspected; an equivalent asymptotic specialization may exist under Mellin-transform terminology..

## Scientific value

**PASS** — The canonical block products are the sharpness models for a recent anti-concentration theorem, so their exact concentration center, sharp leading coefficient, first correction, and exact high-\(p\) density coefficient are motivated invariants rather than an arbitrary slice. They quantify the constants hidden by the general theorem and can serve as benchmarks for any future optimal-constant result.

## Limitations

- Exact constants are for the centered block-product models, not arbitrary multi-affine polynomials.
- The second-order expansion fixes block sizes while the small-ball scale tends to zero.
- Older product-distribution literature was not exhaustively inspected; originality is best-of-knowledge.

This file records a scientific assessment only; it does not claim formal verification or expert attestation.
