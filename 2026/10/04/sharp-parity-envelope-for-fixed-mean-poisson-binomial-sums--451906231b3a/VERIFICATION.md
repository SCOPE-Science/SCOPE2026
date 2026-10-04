---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The theorem is proved analytically. The accompanying `verify_parity_envelope.py`
uses Python `Fraction` arithmetic only; it does not use floating-point
comparisons.

The checker performs three independent finite replays:

1. it exhaustively scans rational parameter grids for \(n\le6\) and verifies
   that every parity bias lies within the claimed endpoint interval;
2. for many rational means and \(n\le10\), it constructs the theorem's lower
   and upper endpoint vectors and checks the mean and bias exactly;
3. for many rational means and \(n\le12\), it constructs an extremizer for
   every feasible sign count \(r\) and verifies the corresponding \(M_r\)
   formula exactly.

Recorded replay result:

`VERIFY_OK grid_vectors=219324 endpoint_cases=4345 sign_cases=14794`

The finite replay is corroborative only. The global result for arbitrary real
parameters follows from the AM--GM proof and complement symmetry in
`RESULT.md`.

Originality was assessed separately by statement-level comparison with
classical Poisson-binomial sources and the closest retrieved public results.
Independent audit has not been performed.
