# Independent audit — 2026-10-01

## Final claim

For two iid gamma variables on a fixed-sum weight line, the quantile has the displayed equal-weight quadratic curvature, an exact transition with positive quartic critical term, and the stated endpoint derivatives and variance-gamma/McKay median rates.

## Correctness — PASS

The beta-gamma factorization gives \(Z_{1+\varepsilon}=S(1+\varepsilon V)\) with the stated symmetric beta moments. A fresh symbolic expansion of \(E[G_a(z/(1+\varepsilon V))]\), followed by implicit coefficient matching, independently reproduced \(-m(a+1-m)/(2(a+1))\) and the critical quartic coefficient \((a+1)/(2(a+3))\). Direct endpoint differentiation gives the stated one-sided derivatives. The committed numerical integrals converge to all displayed coefficients and the variance-gamma/McKay reparameterizations are consistent with the source family.

Checked sources: Gaunt and Ouimet, Bounds for the median of the generalized hyperbolic and related distributions, arXiv:2609.20212; Bock, Diaconis, Huffer and Perlman, Inequalities for linear combinations of gamma random variables, Canadian Journal of Statistics 15 (1987); Diaconis and Perlman, Bounds for tail probabilities of weighted sums of independent gamma random variables, 1988 technical report / 1990 proceedings; Yaming Yu, On the unique crossing conjecture of Diaconis and Perlman on convolutions of gamma random variables, arXiv:1607.02689; Published-findings semantic search for two-gamma quantile curvature and endpoint rates; Assigned Git package; fresh symbolic Taylor reconstruction of the quadratic and critical quartic coefficients

Residual risks: The complete Bock et al. and Diaconis--Perlman texts were not accessible through the available lawful retrieval route; their abstracts and report summaries were inspected, so an unindexed local expansion remains a residual risk.; No global quantile-crossing theorem beyond prior work is claimed.

## Originality — PASS

Best-of-knowledge originality passes for the explicit local quantile curvature, exact transition quantile, positive quartic critical term and endpoint-rate formulas. Classical majorization/crossing results compare distribution tails globally, and the 2026 source establishes median monotonicity and endpoint limits; none of the inspected statements gives these local Taylor coefficients or mechanically determines them without an additional expansion.

### Equivalent formulations

Searches: Resultary semantic search for two-gamma quantile curvature, quartic transition and endpoint derivatives; arXiv:2609.20212; Bock et al. 1987 and Diaconis--Perlman report summaries

Evidence: The exact-topic published-findings search returned the assigned result; nearby records concern different variance-gamma large-noise asymptotics.; The primary 2026 abstract states median monotonicity and bounds, while classical abstracts state tail extremality/crossing results rather than local quantile Taylor laws.

Reasoning: Tail crossing/Schur-convexity and the audited second/fourth derivatives are related but not equivalent statements.

### Broader coverage

Searches: Bock et al. weighted-gamma majorization; Diaconis--Perlman unique crossing and crossing-location bounds; Yu 2017

Evidence: These works are broader in weight-vector comparison and crossing structure.; Their accessible statements do not imply the exact local coefficient or critical quartic sign without carrying out new differentiation at the symmetric point.

Reasoning: General crossing theory constrains sign/order but does not mechanically supply the audited analytic expansion.

### Exact database or table

Searches: exact formulas `G_{2r}(2r+1)`, critical quartic coefficient, variance-gamma small-noise median coefficient and McKay endpoint rates

Evidence: No independent exact database/table entry was located.

Reasoning: Search absence is retained only as best-of-knowledge evidence.

### Claim versus prior implication

Searches: comparison with Gaunt--Ouimet median theorem and classical crossing theorems

Evidence: The median theorem fixes global monotonicity for q one half and endpoint limits; it does not state rates.; The audited formulas follow from a fresh beta-gamma perturbation expansion, not from direct parameter substitution into the prior theorems.

Reasoning: No inspected prior implication dominates the final local-expansion claim.

### Source inspections

- **Bounds for the median of the generalized hyperbolic and related distributions** — https://arxiv.org/abs/2609.20212
  Trigger: Same two-gamma family and the variance-gamma/McKay median consequences
  Material read: Abstract and bibliographic record; complete text was not retrievable during this run
  Method: Primary-source abstract inspection
  Assessment: Covers global median monotonicity and bounds but not the audited general-quantile curvature or rates in the accessible material.
  Evidence: The abstract explicitly states monotonicity for medians of the same gamma sums and derived sharp bounds.
- **Inequalities for linear combinations of gamma random variables** — https://doi.org/10.2307/3315257
  Trigger: Classical weighted-gamma tail majorization
  Material read: Publisher abstract and bibliographic page
  Method: Primary publication-page inspection
  Assessment: Covers equal-weight extremality of tails, not the explicit local quantile expansion.
  Evidence: The abstract states that upper and lower tails are smallest at equal weights.
- **Bounds for Tail Probabilities of Weighted Sums of Independent Gamma Random Variables** — https://statistics.stanford.edu/technical-reports/bounds-tail-probabilities-weighted-sums-independent-gamma-random-variables
  Trigger: Classical crossing-location theory for weighted gamma sums
  Material read: Technical-report abstract and metadata
  Method: Primary institutional-record inspection
  Assessment: Covers crossing existence/bounds in special cases, not the displayed Taylor coefficients.
  Evidence: The abstract states unique crossing in four cases and bounds/asymptotics for crossing location.

Checked sources: Gaunt and Ouimet, Bounds for the median of the generalized hyperbolic and related distributions, arXiv:2609.20212; Bock, Diaconis, Huffer and Perlman, Inequalities for linear combinations of gamma random variables, Canadian Journal of Statistics 15 (1987); Diaconis and Perlman, Bounds for tail probabilities of weighted sums of independent gamma random variables, 1988 technical report / 1990 proceedings; Yaming Yu, On the unique crossing conjecture of Diaconis and Perlman on convolutions of gamma random variables, arXiv:1607.02689; Published-findings semantic search for two-gamma quantile curvature and endpoint rates; Assigned Git package; fresh symbolic Taylor reconstruction of the quadratic and critical quartic coefficients

Residual risks: The complete Bock et al. and Diaconis--Perlman texts were not accessible through the available lawful retrieval route; their abstracts and report summaries were inspected, so an unindexed local expansion remains a residual risk.; No global quantile-crossing theorem beyond prior work is claimed.

## Scientific value — PASS

The result identifies a natural local phase transition for all quantiles in a canonical weighted-gamma family, resolves the degenerate critical point at fourth order, and converts qualitative distributional limits into explicit endpoint rates for two named families. These are motivated analytic invariants with plausible reuse in quantile comparison and approximation.

Checked sources: Gaunt and Ouimet, Bounds for the median of the generalized hyperbolic and related distributions, arXiv:2609.20212; Bock, Diaconis, Huffer and Perlman, Inequalities for linear combinations of gamma random variables, Canadian Journal of Statistics 15 (1987); Diaconis and Perlman, Bounds for tail probabilities of weighted sums of independent gamma random variables, 1988 technical report / 1990 proceedings; Yaming Yu, On the unique crossing conjecture of Diaconis and Perlman on convolutions of gamma random variables, arXiv:1607.02689; Published-findings semantic search for two-gamma quantile curvature and endpoint rates; Assigned Git package; fresh symbolic Taylor reconstruction of the quadratic and critical quartic coefficients

Residual risks: The complete Bock et al. and Diaconis--Perlman texts were not accessible through the available lawful retrieval route; their abstracts and report summaries were inspected, so an unindexed local expansion remains a residual risk.; No global quantile-crossing theorem beyond prior work is claimed.

## Limitations

- Two iid gamma summands and local parameter regimes only.
- No uniform remainder bounds or new global crossing theorem.
- Classical full texts not fully accessible remain a best-of-knowledge originality risk.

## Conclusion

Disposition: **passed**. Acceptance requires PASS on all three axes.
