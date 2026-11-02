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

The proof is by a vector-space image calculation in the cyclic quotient algebra \(\mathbb F_q[T]/(T^n-1)\). The key lemmas are (i) that a cyclic shift has one-dimensional eigenspace for each accessible \(n\)-th root of unity, including in nonsemisimple characteristic, (ii) that a nonunit linear pencil has codimension-one image, and (iii) that the quotient of that image is an eigenline for the shift. The argument covers every integer \(n\ge4\), every prime power \(q\), and all central coordinate choices.

`verify.py` was executed from the actual package directory and produced `VERIFY_OK`. It enumerated and computed ranks using separate matrix-column construction and Gaussian elimination for eight field/size pairs: \((4,2),(4,3),(4,4),(4,5),(4,7),(5,2),(5,3),(6,2)\). The \(q=4\) case uses explicit polynomial-basis extension-field arithmetic and not integer modular arithmetic. The arithmetic oscillation coefficient was separately checked at \(q=3,9,27,81\) without exhaustive enumeration of those enormous Lie algebras. All elementary arithmetic tests passed. The computation neither verifies inaccessible literature nor replaces the proof for unbounded dimensions/field sizes.

No independent audit or external mathematical validation was performed. Possible equivalence to an older general cyclic matrix-pencil enumeration is a residual originality risk.
