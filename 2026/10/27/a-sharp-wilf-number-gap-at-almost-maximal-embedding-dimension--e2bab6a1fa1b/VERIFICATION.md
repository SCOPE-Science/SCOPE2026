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

Run `python verify.py` with Python 3. The included source, without external packages, enumerates Kunz-coordinate vectors for specified bounded boxes, checking the full Kunz inequalities and obtaining Apéry representatives. It derives embedding dimension by testing sums of positive Apéry elements, and computes conductor and left count with exact integers. It checks the sharp inequality and equality classification on every \(e=m-1\) sample. The expected terminal line is `VERIFY_OK: (29223, 8098, 21)`: respectively all valid tested semigroups, near-maximal embedding-dimension semigroups, and extremal cases.

The finite computation covers only \((m,K)=(4,7),(5,6),(6,5),(7,5),(8,4),(9,4)\). No universal conclusion is inferred from this finite search. The analytical proof in `RESULT.md` establishes the theorem for all integers \(m\ge4\) and unbounded Kunz coordinates. No independent audit has been performed.
