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

For θ>−1/2 the CRP has positive probabilities on the stated support. Iterating its recurrence factors the probabilities into the half-discount coefficients and the block-creation weights. The exponential block series is 2(1−sqrt(1−z)); applying Lagrange inversion to z=u(2−u) gives the stated coefficient and the neighboring ratio R_{n,k}=2(n−k)(k+2θ)/[k(2n−k−1)]. The ratio difference has a positive denominator and a numerator proportional to H_{n,k}, affine strictly increasing in θ since the θ coefficient is 2[(n−k)(2n−k)+k(n−1)]. At θ=−1/[2(n−1)], H factors as n(k−2)[k(n−2)+n]/(n−1); thus k=2 is the sole equality and below the boundary it is the failure witness. This covers all interior k, with no test for n=1,2, and yields the stated fixed-negative-strength size bound. An independently written exact-fraction recurrence replay found agreement over n=1–80, 554 strength/size cases and 66,909 checks, including the boundary and neighbors. Replay: /workspace/branches/6824cf16-da55-4984-a1e2-40e624044285/crp_recurrence_audit.py, pilot.log, chunk_11_40.log and chunk_41_80.log. Finite cases corroborate rather than prove the classification. The frozen script was inspected, not executed.

## originality

PASS

The inspected exact Bessel coefficient theory and generalized-Stirling log-concavity results do not cover the θ-weighted block-count shape boundary; the other matching partition records treat distinct observables. The support is a statement-level comparison, not a claim of exhaustive novelty or historical priority.

## value

PASS

This is a sharp, motivated change in the finite-sample shape of a standard partition statistic in its natural half-discount case. Negative strengths remain admissible but eventually lose log-concavity; the exact size cutoff and the unique witnessing triple distinguish this from a coefficient-array calculation or a single counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
