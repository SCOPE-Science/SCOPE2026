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

The unrestricted proof is in `RESULT.md`. It uses exact integer relations, a terminating reduction to an L-shaped set with exactly one representative per residue, and a reversible-last-step lemma giving the exact second representative per residue. The resulting three corner expressions are compared for the full integer range, including all small exceptional cases.

Run `python3 verify.py` from the directory containing the packaged files. The script enumerates nonnegative pairs in increasing weight order and collects the first two coefficient-pair representatives in every residue class for all parameters from 3 through 80. It checks 354,302 predicted second Apéry values, compares full arrays and all branches of the generalized Frobenius formula. One genuine execution output is embedded as `verification_output.txt`. This enumeration is finite and is not a substitute for the unrestricted proof.

No independent audit or formal certification has been performed. The same-generator Chatterjee–Narula (2025) preprint was available by abstract only and remains a bibliographic risk regarding an unreported higher-threshold result.
