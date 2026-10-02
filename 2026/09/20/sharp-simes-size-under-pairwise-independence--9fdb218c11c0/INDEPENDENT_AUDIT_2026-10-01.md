# Scientific audit — 2026-10-01

## Final claim assessed

Sharp Simes size under pairwise independence for three uniform p-values

## Correctness — PASS

PASS. The Simes event depends only on the four interval labels \(A,B,C,D\) with widths \(r,r,r,1-3r\), where \(r=lpha/3\). Pairwise independence fixes all ten second factorial moments of the occupancy counts. The three displayed dual coefficient vectors were independently checked on all 20 occupancy types and give the three polynomial upper bounds. The three exchangeable count distributions were independently rechecked for normalization, all ten pair laws and their rejection polynomials. Conditional independent uniform draws inside the assigned intervals then produce exactly uniform continuous marginals while preserving pairwise independence. The branch crossings occur at \(r=1/5\) and \(r=1/4\), giving the stated \(lpha=3/5\) and \(lpha=3/4\) breakpoints. This is a finite exact certificate embedded in a complete probabilistic reduction, not a heuristic computation.

## Originality — PASS

PASS to the best of current knowledge. Simes proves exact size under mutual independence. Hommel's complete 1983 paper was inspected in full: its arbitrary-dependence sharp method uses harmonic-adjusted ordered critical levels, not the unadjusted Simes event under pairwise independence. Samuel-Cahn studies anticonservativeness under dependence classes but does not provide the pairwise-independent three-uniform envelope in its accessible statement. Ramachandra--Natarajan's complete arXiv paper gives sharp or improved bounds for single-threshold sums of pairwise-independent Bernoulli variables; it does not treat the multilevel Simes rejection event. No inspected source states or implies the assigned piecewise envelope.

### equivalent_formulations

Searches: search: Simes pairwise independent p-values exact size three; Resultary: Simes pairwise independence three uniforms sharp; search: Benjamini-Hochberg global null pairwise independence three

Evidence: No earlier exact three-variable piecewise envelope was found. Under the global null, BH rejects at least one hypothesis on exactly the Simes event, so that equivalent formulation was included.

Reasoning: The BH-global-null and Simes formulations are equivalent here; neither search produced stronger prior coverage.

### broader_coverage

Searches: DOI 10.1002/bimj.19830250502 full text; DOI 10.1093/biomet/83.4.928; arXiv:2006.00516 full text

Evidence: Hommel gives sharp arbitrary-dependence bounds for different harmonic-adjusted procedures; Ramachandra--Natarajan treat one-threshold Bernoulli sums under pairwise independence.

Reasoning: Neither broader theory mechanically gives the simultaneous three-threshold Simes event with exact uniform marginals.

### exact_database_or_table

Searches: Published-record semantic search for pairwise-independent Simes size; multiple-testing search for exact three-p-value envelope

Evidence: No tabulated critical-value result or earlier exact theorem with the three polynomial branches was located.

Reasoning: The object is an extremal distribution problem, so theorem/coupling search is the relevant exact comparison.

### claim_vs_prior_implication

Searches: Hommel 1983 Sections 3--6; Ramachandra--Natarajan 2022/2023 threshold-event bounds; Samuel-Cahn 1996 abstract

Evidence: Hommel's method 3.3 uses critical levels proportional to \(k/(nC_n)\), not \(k/n\); the pairwise-Bernoulli paper fixes one threshold \(k\) at a time rather than the union of Simes thresholds.

Reasoning: The occupancy LP and compatible continuous extremizers provide additional structure not implied by those prior results.

## Scientific value — PASS

PASS. Pairwise independence is a natural intermediate dependence model, and the theorem exactly quantifies how far a canonical multiple-testing procedure can exceed nominal level in the smallest nontrivial case. The exact sharp envelope and continuous extremizers are reusable in limited-independence multiple testing and are not a routine numerical check.

## Source inspections

- **Tests of the Overall Hypothesis for Arbitrary Dependence Structures** — https://doi.org/10.1002/bimj.19830250502. Material read: Complete eight-page primary article, including all three overall-test procedures, sharpness discussion and appendix. Assessment: ARBITRARY_DEPENDENCE_DIFFERENT_CRITICAL_LEVELS. Evidence: The sharp arbitrary-dependence procedure uses harmonic-adjusted critical levels and does not state the pairwise-independent Simes envelope.
- **Tight Probability Bounds with Pairwise Independence** — https://arxiv.org/abs/2006.00516. Material read: Complete accessible primary text, including the Bernoulli threshold formulation, exact union bound and higher-threshold sections. Assessment: SINGLE_THRESHOLD_BERNOULLI_RESULTS_NOT_SIMES_ENVELOPE. Evidence: The paper optimizes probabilities that a Bernoulli sum exceeds one fixed threshold; it does not encode the three nested Simes thresholds or continuous uniform marginal structure.
- **Is the Simes improved Bonferroni procedure conservative?** — https://doi.org/10.1093/biomet/83.4.928. Material read: Primary abstract and indexed result statement. Assessment: DEPENDENCE_CLASS_RESULTS_NOT_PAIRWISE_EXACT_ENVELOPE. Evidence: The paper studies positive/negative bivariate-normal dependence and cites attainable arbitrary-dependence bounds; the accessible statement does not give the assigned pairwise-independent piecewise law.

## Limitations and residual risks

The theorem is specific to three exactly uniform global-null p-values. It does not characterize four or more p-values, super-uniform marginals, partial-null FDR, or higher limited-independence orders. Older extremal probability/coupling formulations remain a residual originality risk.

- Older Bonferroni/coupling literature may encode the same three-variable LP under different terminology.
- The result does not extend automatically to \(m\ge4\) or to super-uniform nonuniform nulls.

## Disposition

**passed**
