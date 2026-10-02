# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260918-250a4af644f8`

## Correctness — PASS

The analytic estimate checks. For the normalized univalent map at a real strip point, \(g''=6(a_3-(2/3)a_2^2)\), so the sharp Fekete–Szegő inequality gives \(|g''|\le 6(1+2e^{-4})\). Correctly centering the Gaussian Taylor expansion yields phase error \(3(1+2e^{-4})\sigma^2\). The imaginary Gaussian kernel estimate together with Cauchy–Schwarz gives \(4\sigma\sqrt{\sinh(\sigma^{-2})}\) uniformly on the strip. The constructed analytic multiplier therefore has derivative modulus at most one on the target domain and a positive real component along the connecting real segment. At \(\sigma=9/14\), independent numerical evaluation gives phase error about 1.285211, attenuation exponent about 6.072639, and lower constant about 0.000649384865, which exceeds \(6.49\times10^{-4}\).

### Correctness sources

- MacMahon, arXiv:2609.20607
- Choi–Kim–Sugawa, DOI 10.2969/jmsj/05930707
- artifacts/verify_constant.py
- independent numerical evaluation

### Correctness risks

- No optimality of the universal constant is claimed.
- The theorem is restricted to simply connected planar domains.

## Originality — PASS

MacMahon's source proves the universal analytic-Lipschitz/interior-metric comparison using Gaussian straightening with a much smaller explicit constant and a coarse second-derivative bound. The sharp Fekete–Szegő coefficient theorem is classical. No inspected source combines them into the audited quantitative bound or the corrected Gaussian estimate.

### equivalent_formulations

Searches:
- arXiv:2609.20607 full text
- searches combining Fekete–Szegő, pre-Schwarzian second derivative and analytic Lipschitz metric

Evidence:
- MacMahon uses a coarse derivative estimate and does not state the audited constant.
- The Fekete–Szegő literature supplies the sharp coefficient inequality, not this metric consequence.

Reasoning:
Equivalent formulations through a universal lower bi-Lipschitz constant and through the strip-straightening attenuation were compared.

### broader_coverage

Searches:
- classical Fekete–Szegő theorem for normalized univalent functions
- MacMahon's complete metric theorem

Evidence:
- The broader source theorems provide distinct ingredients.

Reasoning:
Neither theorem alone mechanically supplies the new numerical constant; their quantitative synthesis and corrected convolution bounds are necessary.

### exact_database_or_table

Searches:
- known tables of universal analytic-Lipschitz constants

Evidence:
- No exact database/table containing the audited constant was located.

Reasoning:
The result is an analytic derived estimate rather than a pre-tabulated invariant.

### claim_vs_prior_implication

Searches:
- direct substitution of the sharp coefficient bound into MacMahon's argument

Evidence:
- After also correcting the centered Taylor term and sharpening the strip estimate, the source proof yields the audited constant.

Reasoning:
This is a new quantitative refinement, not a restatement of the source constant.

### source_inspections
- **On Simply Connected Domains Supporting an Unbounded Analytic Function with Bounded Derivative** — https://arxiv.org/abs/2609.20607. Trigger: Same metric theorem and Gaussian-straightening argument. Material read: Full accessible preprint proof material including the strip setup, derivative bounds, Gaussian convolution and universal comparison. Method: Primary full-text proof comparison. Assessment: Provides the mechanism and qualitative theorem but not the audited sharp refinement. Evidence: Its displayed second-derivative estimate is coarser and its reported explicit lower scale is vastly smaller.
- **A general approach to the Fekete–Szegő problem** — https://doi.org/10.2969/jmsj/05930707. Trigger: Sharp coefficient inequality used at parameter two-thirds. Material read: Published theorem/introduction material stating the classical sharp inequality. Method: Primary theorem comparison. Assessment: Supplies the coefficient bound only. Evidence: At the required parameter it gives \(1+2e^{-4}\), producing the sharper pre-Schwarzian estimate.
- **Assigned constant verifier** — artifacts/verify_constant.py. Trigger: Final explicit arithmetic. Material read: Complete source file. Method: Line-by-line inspection plus independent evaluation. Assessment: The decimal bound reproduces. Evidence: The independent value is approximately 0.000649384865.

### checked_sources

- https://arxiv.org/abs/2609.20607
- https://doi.org/10.2969/jmsj/05930707
- assigned RESULT.md and artifacts/verify_constant.py

### residual_risks

- The source preprint is extremely recent, so unindexed parallel quantitative work remains possible.

## Scientific value — PASS

Improving a newly introduced universal metric constant by many orders of magnitude is mathematically substantive because the gain comes from a sharp classical coefficient theorem and a corrected/sharpened analytic estimate, not parameter tuning alone. The calculation also identifies and repairs two local slips without invalidating the source theorem.

### Value sources

- MacMahon's universal comparison theorem
- sharp Fekete–Szegő inequality

### Value risks

- The resulting constant is not claimed optimal.

## Limitations

- No optimality is claimed.
- The method remains restricted to simply connected planar domains.
- Originality is best-of-knowledge for a very recent source theorem.

## Disposition

**PASSED**
