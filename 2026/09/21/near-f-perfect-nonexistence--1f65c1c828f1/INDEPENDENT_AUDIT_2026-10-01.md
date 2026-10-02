# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260921-1f65c1c828f1`

## Correctness — PASS

The nonexistence proof is complete. Dividing the defining equation by \(n^2\) and pairing divisors with reciprocals gives a positive sum of reciprocal divisor-squares equal to \(3/n\), with exactly one reciprocal term omitted. For odd \(n\), parity forces \(n\) to be a square; a square with at least two prime factors immediately leaves a reciprocal term larger than the whole required sum, while the prime-power cases are impossible. When the exact power of two is one, the omitted-divisor alternatives reduce either to the same size contradiction or to a one-prime calculation. When \(4\mid n\), every case either contradicts a surviving \(1/4\) term or reduces to \(n\le48\); exact evaluation of the twelve multiples of four closes that finite core. The package scan through one million is corroborative only.

### Correctness sources

- assigned RESULT.md
- artifacts/verify.py and artifacts/verification.txt
- the exact divisor-sum identities in the assigned proof

### Correctness risks

- The theorem is only the \([2,3]\)-near-perfect specialization; no claim is made for general \([k,\ell]\).

## Originality — PASS

The full 2025 primary near-\(F_k\)-perfect paper was inspected. It excludes several prime-factor shapes, including prime powers and multiple two-prime families, but its concluding discussion still points to numbers with more than two prime factors as further work. It does not state global nonexistence of near \(F\)-perfect numbers. Resultary semantic searches and direct web searches for the exact equation/nonexistence statement returned the audited theorem but no stronger prior theorem.

### equivalent_formulations

Searches:
- Resultary query: near F-perfect numbers nonexistence sigma_2 equation [2,3]-near-perfect
- web query: "near F-perfect numbers do not exist"
- primary full text: https://math.colgate.edu/~integers/z86/z86.pdf

Evidence:
- The 2025 paper's Definition 4 is the same equation.
- Its theorems exclude restricted prime-factor forms, and the conclusion proposes further work for more than two prime factors rather than claiming complete nonexistence.

Reasoning:
Equivalent terminology \([2,3]\)-near-perfect, near \(F\)-perfect, and the explicit \(\sigma_2\) equation were all checked.

### broader_coverage

Searches:
- 2025 Integers paper on near \(F_k\)-perfect numbers
- arXiv/older \(F\)-perfect literature
- current Resultary number-theory findings

Evidence:
- The inspected primary paper is broader in the parameter \(k\) but narrower in arithmetic coverage for \(k=2\); it does not dominate the all-integer nonexistence theorem.

Reasoning:
Parameter-general definitions do not imply the complete \(k=2,\ell=3\) classification.

### exact_database_or_table

Searches:
- current Resultary divisor-sum findings
- web exact-equation searches

Evidence:
- No database or table establishing a complete all-\(n\) absence was found.

Reasoning:
The million-integer scan is not treated as novelty evidence or as proof of global nonexistence.

### claim_vs_prior_implication

Searches:
- claim-versus-2025 theorems by prime-factor shape

Evidence:
- Restricted exclusions for prime powers and selected two-prime families leave the many-prime cases open; the reciprocal-divisor argument closes them uniformly.

Reasoning:
The final claim is not a corollary of the inspected shape-by-shape results.

### source_inspections

- **On near \(F_k\)-perfect and deficient \(F_k\)-perfect numbers** — https://math.colgate.edu/~integers/z86/z86.pdf. Trigger: Primary source defining the exact class and giving the strongest located prior exclusions. Material read: Complete 22-page PDF, with definitions, restricted nonexistence theorems, and concluding discussion inspected; a page screenshot was also checked. Method: Primary full-text theorem and implication comparison. Assessment: NOT COVERING the global near-\(F\)-perfect nonexistence theorem. Evidence: The source excludes several factorization classes and explicitly leaves broader prime-factor configurations for future work.
- **Assigned exact verifier** — artifacts/verify.py. Trigger: Finite core and supporting census. Material read: Complete source and saved output. Method: Line-by-line inspection and independent arithmetic check. Assessment: Correct corroboration. Evidence: It exactly checks every multiple of four through 48; the larger scan is supplementary only.

### checked_sources

- 2025 Integers full text
- current Resultary near-\(F\) search
- exact-equation web searches
- assigned RESULT.md and verifier

### residual_risks

- Older divisor-sum literature may use unrelated terminology, so historical priority remains best-of-knowledge.

## Scientific value — PASS

The theorem closes the full existence question for a named divisor-sum class that previously had only factorization-specific exclusions. The reciprocal-divisor reformulation is a compact global obstruction and replaces an open-ended census by a proof with a tiny finite core.

### Value sources

- 2025 near-\(F_k\)-perfect source
- assigned reciprocal-divisor theorem

### Value risks

- The result is intentionally narrow to the classical near-\(F\) specialization.

## Limitations

- The theorem concerns only the \([2,3]\)-near-perfect specialization.
- The scan through one million is not part of the infinite proof.
- Originality is best-of-knowledge with terminology risk in older divisor-sum literature.

## Disposition

**PASSED**
