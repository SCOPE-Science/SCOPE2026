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
# Reproducibility and boundaries

Run `python3 verify.py` in the extracted folder. The standard-library-only verifier constructs recurrence terms exactly for each integer \(P\) from \(3\) through \(20\), all primes at most \(101\), and each index up to \(260\). It tests the complete integer Möbius-transform formula as well as the predicted odd-prime Dold classes. Expected output begins `VERIFY_OK parameter_count=18 prime_count=26 exact_transform_cells=121680`. The result was reproduced from the packaged script. This is bounded checking, not verification of the infinitely many indices or asymptotic prime density; those rely on the written argument.

The full proof specifies the ramified-prime exclusion, index-one exceptional term, binary trace valuations, higher tower factors, and exact minimum repair. No external certification or independent audit is claimed.
