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

# Reproducibility and verified limits

Run `python3 check.py` using only the Python standard library. Its exact output is included in `check_output.txt`, ending with `INCIDENCE_PROJECTION_DERIVATIONS_OK 12 EXHAUSTIVE_CONFIGURATIONS`.

The checker builds finite-poset incidence basis multiplication and lists all cocycles of every field value, then every radical-inner perturbation. It constructs each derivation matrix, checks the identity \(D^2=D\) entry by entry, computes rank by field Gaussian elimination, and matches the histogram to the Boolean-cocycle weighted count. Twelve small configurations cover chain, diamond, crown, star, disconnected and discrete posets and fields \(\mathbb F_2,\mathbb F_3,\mathbb F_4\) (including genuine extension-field arithmetic).

These finite enumerations corroborate but do not prove the universal statement. The universal proof uses derivation decomposition, nilpotent-ideal idempotent lifting inside \(\ker D\), and the exact stabilizer calculation. This is a self-review, not independent validation.
