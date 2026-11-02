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

Run `python3 verify.py` with standard Python 3 and no third-party dependencies. The script implements the original basis products, enumerates every linear map in the small tested dimensions and all generator images in larger dimensions, and directly tests multiplication, rank via finite-field elimination, and noninvertible composition nilpotency indices. It uses \(\mathbb F_4=\mathbb F_2[\alpha]/(\alpha^2+\alpha+1)\) for the nonprime-field cases. Successful execution ends in the exact marker `EVOLUTION_CHAIN_ENDOMORPHISM_OK`.

Exhaustive **all linear maps**: \((n,q)=(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2)\). Exhaustive **generator images**: \((n,q)=(4,3),(5,2),(5,4),(7,2)\). The expected rank classes are \(N_0=1\), \(N_1=q-1\), and \(N_r=q(q-1)\) for \(2\le r\le n\). This finite range is not an exhaustive verification of arbitrary fields or dimensions; the mathematical proof in `RESULT.md` establishes that generality. Unreduced scheme information is not asserted or checked.
