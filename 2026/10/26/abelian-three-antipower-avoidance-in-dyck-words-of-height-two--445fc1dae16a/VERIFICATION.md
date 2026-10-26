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

# Reproducibility

Run `python3 verify_height2_antipower.py` using Python 3 standard library. The script generates every Dyck word of height at most two independently of the height-code parametrization for each semilength from 1 through 15, totals 32,767 words, directly checks contiguous abelian three-antipowers, computes the progression condition from even heights, and compares exact surviving-word sets to the theorem. It further checks all proposed survivors directly for semilengths 16 through 150.

Observed output: `HEIGHT_TWO_ABELIAN_ANTIPOWER_PASS lengths=1..15 total= 32767 constructive_lengths=16..150`.

The finite verifier is not an all-length proof; the all-length result follows from the bijection, exact endpoint-count criterion, and structural run lemma in RESULT.md. An independent mathematical audit has not been performed.
