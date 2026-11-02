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

# Reproducibility and verification

The exact inequality is established by an analytic reduction to the overlap \(t\), use of the independently published sharp Rayleigh-product lemma, a strictly monotone cubic, and a direct attaining projection pair. The reconstruction and endpoint checks appear in `RESULT.md`. No finite computation is used to infer the general theorem.

Run `python3 verify.py`. The script uses only the Python 3 standard library. It verifies both sides directly from matrix products for eight positive spectra, with 2,200 deterministic pseudorandom pairs per spectrum, and checks the analytic root and exact projections for each case. The run produced `VERIFY_OK`.

The random tests are not exhaustive over continuous inputs and cannot independently certify the theorem. Historical originality remains subject to the incomplete inspection of Fang–Cheng's publisher text, and no independent mathematical audit has been performed.
