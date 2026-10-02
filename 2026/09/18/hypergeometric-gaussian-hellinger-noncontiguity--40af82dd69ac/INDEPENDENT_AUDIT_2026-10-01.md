# Independent audit — Gaussian-boundary hypergeometric laws: sharp Hellinger rate and root-n noncontiguity

**Disposition: PASSED.**

## Correctness

**PASS** — The beta-precision representation gives a uniform algebraic survival tail on the logarithmic crossover windows. Splitting at squared radii \(2L+2\log L\) and \(2L+6\log L\), with \(L=\log(1/a)\), makes the central Hellinger contribution lower order and leaves tail mass \(a/(2L)\). Exact affinity tensorization then yields the iid boundary. The maximum law follows from \(nP_{a_n}(|X|>\sqrt{2y\log n})\to\kappa/(2y)\). The empirical-CDF argument below the root-n scale does not require likelihood contiguity. Independent numerical quadrature for decreasing \(a\) showed the slowly converging ratio in the direction predicted by the asymptotic; it was treated only as a sanity check.

## Originality

**PASS** — The motivating Lawford paper supplies the family, mixture representation, algebraic tails, non-DQM observation and a root-n minimum-distance theory, but the inspected full text does not state the sharp \(a/[2\log(1/a)]\) Hellinger law, the \((\log n)/n\) product boundary, or the CDF-local versus experiment-local separation. General sparse-mixture and heavy-impurity theory supplies mechanisms rather than this exact family-specific constant and implication. Resultary and targeted web searches found no earlier equivalent published SCOPE record.

## Scientific value

**PASS** — This identifies the experiment-level detection scale of a newly introduced nonregular family and exposes a substantive distinction between root-n CDF locality and likelihood/contiguity locality. The exact boundary and explicit critical maximum profile are motivated statistical structure, not an arbitrary finite computation.

## Source inspections

- **Gaussian Boundary Inference in a Hypergeometric Heavy-Tailed Family** (arXiv:2609.20393): full open-access text: mixture representation, non-DQM discussion, local-power/contiguity argument. Assessment: NOT_COVERING exact Hellinger/product boundary.
- **Optimal detection of sparse mixtures against a given null distribution** (DOI:10.1109/TIT.2014.2304295): published theorem/abstract-level comparison. Assessment: BROADER MECHANISM, NOT exact claim.
- **Extreme Value Analysis for Mixture Models with Heavy-Tailed Impurity** (DOI:10.3390/math9182208): published heavy-impurity extreme-value results. Assessment: BROADER MECHANISM, NOT exact claim.

## Originality checks

### Equivalent Formulations

Equivalent formulations would assert the same Hellinger modulus or product-affinity boundary; none was found.

Searches: Resultary: Gaussian boundary hypergeometric Hellinger detection noncontiguity; web: exact a/(2 log(1/a)) Hellinger hypergeometric Gaussian boundary.

Evidence: No earlier equivalent published record was located.

### Broader Coverage

They do not mechanically supply the beta-precision crossover calculation or its constant.

Searches: Cai and Wu sparse mixture detection; Morozova Panov heavy-tailed impurity maxima.

Evidence: These sources give general detection/extreme-value mechanisms.

### Exact Database Or Table

The claim is analytic rather than tabular.

Searches: Resultary exact-family query.

Evidence: The 2026-09-18 record itself was the only exact hit.

### Claim Vs Prior Implication

The new result requires a tail/central Hellinger decomposition and exact tensorization; it is not a parameter substitution into the source theorem.

Searches: Lawford arXiv:2609.20393 full text.

Evidence: The source states non-DQM and develops root-n minimum-distance local power; it does not derive the Hellinger boundary.

## Residual risks

- The first-order Hellinger asymptotic converges slowly numerically; correctness rests on the analytic uniform bounds, not the finite numerical check.
- A differently parameterized normal-scale-mixture theorem could contain an abstract implication not found by the targeted searches.

## Limitations

The sharp Hellinger result treats the standardized one-parameter beta-precision hypergeometric path. Plug-in location/scale, the full critical likelihood-ratio experiment, second-order Hellinger terms, and finite-sample errors are not derived. Originality remains best-of-knowledge against broader sparse-mixture and normal-scale-mixture theory.

This assessment preserves the historical same-model review as prior evidence but does not treat it as independent support for this audit.
