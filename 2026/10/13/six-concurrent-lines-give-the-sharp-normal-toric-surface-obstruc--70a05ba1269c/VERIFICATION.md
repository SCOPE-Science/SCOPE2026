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
The mathematical proof depends on three explicit inputs: the functorial associated-graded surjection for a closed immersion; Artin's formula that rational surface singularities satisfy multiplicity equal to embedding dimension minus one; and Sally's theorem that Cohen--Macaulay local rings of minimal multiplicity have quadratically generated tangent-cone ideals. Normal toric surface germs in characteristic zero are cyclic quotient singularities and thus rational and Cohen--Macaulay. These classical inputs were checked against the cited primary literature.

The only finite arithmetic certificate is the determinant of the conic-evaluation matrix for six rational directions. The bundled script `verify.py` uses exact fractions, makes no external requests, and asserts that this determinant is exactly \(7\). A nonzero determinant supplies a witness for the open locus, but it is not a substitute for the general proof. To replay, run `python3 verify.py` in the directory containing the extracted file.

No independent audit, external certificate, full enumeration of configurations, or claim about positive characteristic is asserted.
