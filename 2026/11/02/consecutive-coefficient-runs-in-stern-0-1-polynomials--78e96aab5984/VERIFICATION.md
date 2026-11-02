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

Run `python3 verify.py` in the directory containing the standalone script, using Python 3. The computation independently derives polynomial supports via the defining recurrence and via parity of \(\binom{n-1-j}{j}\); it then enumerates maximal consecutive occupied-exponent runs and verifies the claimed histograms for every \(2\le r\le12\), plus the sharp witness \(P_5\).

The executable produces `VERIFY_OK` only after all assertions pass. Checked: 4096 polynomial supports, all run lengths at every checked index, and 11 complete dyadic-prefix histograms. These are finite tests, not proof of the infinite claim. The infinite result is proved in `RESULT.md` from the four exact overlap recurrences and Stern summation. No third-party files, external internet, or symbolic systems are necessary.

Scientific priority remains subject to broader bibliographic verification. Independent mathematical audit has not been performed.
