---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For fixed active J, the enforced coordinates are exactly correct. Each unrelaxed active projection deletes only its own error coordinate. Independence at fixed probabilities w_i/sum_J w gives the exact coordinate survival factor (1-w_i/sum_J w)^k. The expected squared-error ratio is a weighted average of these factors; choosing the initial error entirely on a least-weight coordinate attains the maximum. For a fixed largest selected index j, w_j is the numerator of the score to maximize and the unique sum-minimizing choice takes the r-1 immediately preceding indices, since the weights strictly decrease. This exhausts all possible largest indices and gives every optimal active set, not necessarily a unique optimal window. Under equal weights the exchange can be nonstrict, leaving the asserted existence. Exact Frobenius residual equals the sum of the active weights, so its optimal constraint set removes the largest weights. For A_M the two candidate windows compare by M^4>(M+1)^2 (M>=2), and the shown logarithmic rate ratio follows from log(1+M^-2)~M^-2 and the optimum tending to 1/2. Independent replay: python3 /workspace/review_replay.py 3 checks all equality cases in 14212 finite integer-spectrum tests using exact rational scores. These corroborate but do not establish the universal theorem. The uploaded checker was read, not run; its path enumeration is exhaustive for its example but the arithmetic uses floats, not exact rationals. The theorem does not include computational cost of enforcing constraints, general correlated rows, or other sampling probabilities.

## originality

PASS

Best of the checked evidence: the distinct contribution is the full optimizer classification for the diagonal all-horizon problem and its exact three-coordinate accepted-iteration comparison. Norm-proportional sampling, constraint projection, the one-step spectral objective, and residual-Frobenius ID are not credited as original. An unbounded deterioration of a Frobenius selection has also been exhibited on a different six-row model; this record is not a general priority claim for that phenomenon.

## value

PASS

The complete all-horizon classification turns combinatorial constrained-row selection into a sorted sliding-window scan on a natural exactly tractable benchmark. The three-mode witness measures a failure of the motivated residual surrogate in the actual expected-error convergence exponents, which diverge in ratio even without overhead from constraint enforcement or rejected proposals. The result is elementary but resolves a useful boundary case and supplies a quantitative benchmark, not a claim about general matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
