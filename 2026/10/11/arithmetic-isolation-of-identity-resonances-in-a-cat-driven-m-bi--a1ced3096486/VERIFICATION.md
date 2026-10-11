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

# Verification and boundaries

The exact proof is in RESULT.md. The normalized determinant-one return matrix is \(U_{-\delta}BU_{\delta}B\). Direct multiplication proves its trace formula; at \(\delta\in\mathbb Z+1/2\) the conjugated factor equals \(B^{-1}\), giving identity rather than a merely parabolic return. Integer modular arithmetic verifies the four nonzero cat period-two base points, while \(\det(A^2-I)=-5\) proves their exhaustiveness. The sine quotient equals the irrational golden ratio, eliminating simultaneous resonances.

Running `python3 verify.py` prints `CHECK_OK`. The script tests base-point enumeration by exact integer arithmetic, floating-point matrix traces and sample identity returns at resonances, and the exact exponent formula numerically. The floating-point checks do not prove the all-parameter result; that rests on the exact identities in RESULT.md. No externally produced mathematical certificate or independent audit is represented.
