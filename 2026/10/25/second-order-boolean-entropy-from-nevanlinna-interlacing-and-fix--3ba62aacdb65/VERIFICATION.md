---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Star-matrix Schur complement gives exact normalized Boolean transform; strict interlacing gives r+1 positive-mass simple eigenvalues. Perturbation at ±1 and tq_j gives the outer 1/n entropy term and c_j t²(log t+log|q_j|), with Σc_j=v. Exact zero of g at origin produces positive zero atom and infinite entropy. Three-atom ν_p with identical μ first four moments has full-range 1/n constant. Independent numerical eigensystem diagonalization checked four laws at multiple n and verified mass-1/(n+1) central-zero case. Numerical checks are not an asymptotic proof.

## originality

PASS

Pan gives a log(n)/n leading term and a computable particular four-point example; the all-finite-atomic explicit 1/n coefficient with arbitrary fixed-first-four-moment range is not implied by that leading asymptotic. Correctly excludes previously implied special case.

## value

PASS

A natural first omitted coefficient in a recent Boolean entropic CLT rate is classified via finite spectral interlacing; its unbounded variation at fixed first four moments rules out a moments-only next-order estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
