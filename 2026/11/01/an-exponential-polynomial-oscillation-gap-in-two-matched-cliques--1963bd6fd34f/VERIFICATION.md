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

# Verification record

Execute `python3 verify.py` with Python 3 and no external dependencies. The program checks the exact vertex-level majority decision against a separate set-algebra update for every initial configuration on sizes \(2\le n\le8\) (87,376 in total). It then exhausts all matched-pair population types for sizes \(2\le n\le40\), with exact multinomial weights, and compares fixed-state, two-cycle, attraction-basin, and transient counts to the closed formulas. It verifies the iterated identities at every tested state and compares exact finite masses against the claimed classifications. The recorded output is embedded as `verification_output.txt`.

The independent vertex loop and the population checker test code consistency and a large finite portion of the theorem. The proof covering every integer \(n\ge2\) is the case analysis in `RESULT.md`. Numerical tests alone do not establish a uniform statement. No external or independent scientific audit has been performed.
