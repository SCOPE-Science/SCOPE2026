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
# Reproducibility and limitations

The standalone checker `tree_temporal_verifier.py` is executable using only the Python standard library. It enumerates finite rooted tree posets, monotone endomorphisms, valuations, and temporal preimage iterations, and verifies the predicted period-budget inequality and constructive cases. The obtained output is `VERIFY_OK trees= 34 monotone_maps= 5430 valuation_tests= 168950 max_periods_seen= [(1, 1), (2, 2), (3, 3), (4, 4)] constructed_spectra_through_n=9`.

Finite enumeration supports but does not prove the unrestricted statement. Correctness for every finite tree size follows from the proof's stable-image automorphism reduction and prime-power cycle argument, plus the explicit construction. No independent assessment has been performed. The primary source does not claim this quantitative exact period spectrum. Prior equivalent work under other terminology cannot be entirely excluded.
