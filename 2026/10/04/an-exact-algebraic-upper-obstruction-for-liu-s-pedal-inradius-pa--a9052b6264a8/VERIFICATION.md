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

Run `python3 verify.py` with Python 3 and SymPy. The script checks exact polynomial identities only; decimal output is diagnostic.

It verifies:

- the cubic \(125z^3-81z^2+39z-11\) is strictly increasing and has a unique root in \((0,1)\);
- the positive \(u\)-root lies in \((0.6405,0.6406)\), and the induced \(v\) satisfies \(0<v<u\);
- the exact equality defect reduces to zero modulo \(125u^6-81u^4+39u^2-11\);
- the induced parameter satisfies \(27k^3-108k^2-720k-800=0\), whose discriminant is negative and whose real root lies in \((7,8)\);
- \(R-2r>0\) for the witness, so the affine defect becomes strictly negative for every larger \(k\).

The script does not attempt a global minimization over all triangles and all interior points. Therefore it certifies an exact upper obstruction, not the globally sharp value.
