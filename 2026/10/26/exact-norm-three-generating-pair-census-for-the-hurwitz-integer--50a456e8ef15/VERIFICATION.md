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

# Verification details

`verify.py` is a standalone Python 3 standard-library program. It enumerates all \(96\) norm-three Hurwitz quaternions in doubled integral coordinates and all \(9216\) ordered pairs. For each pair it calculates the determinant of the four-element lattice \(1,x,y,xy\) in the Hurwitz basis and independently calculates the squared imaginary cross product. It checks both criteria agree and checks the exact trace-stratified and total counts. It also verifies the norm-one unit count and the resulting conjugation orbit count by the stabilizer argument. The executable returns `VERIFY_OK` only if all tests pass.

The enumeration is exhaustive for norm \(3\) because the doubled coordinates have squares summing to \(12\), hence every entry lies between \(-3\) and \(3\). It makes no statement about other norms, and does not constitute independent mathematical certification.
