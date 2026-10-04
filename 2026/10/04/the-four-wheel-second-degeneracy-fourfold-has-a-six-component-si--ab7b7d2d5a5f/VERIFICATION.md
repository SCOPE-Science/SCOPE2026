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

Run `python3 verify.py` with SymPy. The verifier reconstructs the cyclic symmetric matrix, all distinct \(3\times3\) minors, and their Jacobian. It verifies that the four Veronese conics and two opposite diagonal lines lie in the second degeneracy variety; that representative rank-one and line points have deficient Jacobian rank; and that an explicit rank-two point off the proposed singular set has Jacobian rank \(3\), the expected codimension. It also checks \(\det(aE_{13}+bE_{24})=a^2b^2\), the exact rank dichotomy used in the conormal proof.

The symbolic replay is a consistency check for the geometric proof, not an exhaustive point enumeration. Exhaustion of the singular locus comes from the rank-stratified conormal argument in `RESULT.md`.
