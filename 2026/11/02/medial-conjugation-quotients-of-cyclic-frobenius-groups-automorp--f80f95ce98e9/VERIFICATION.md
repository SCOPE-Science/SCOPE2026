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
Run `python3 verify.py` with Python 3.10 or later. The script builds semidirect products over finite prime fields, computes universal medial congruences by direct finite saturation, and compares the quotient multiplication with the claimed structure. It checks finite automorphism counts and an explicit pair of inequivalent order-sixteen kernels, producing `VERIFY_OK` when successful. Its actual output includes the prime cases \((p,m)=(3,2),(5,2),(5,4),(7,2),(7,3),(7,6)\) and the eighteen-point collision. Cases with \(m=2\) check the general algebraic identity but are not part of the novel automorphism assertion. Finite computations do not prove the claimed classification for all admissible groups; the proof in `RESULT.md` handles the general case. No independent audit or external certification has occurred.
