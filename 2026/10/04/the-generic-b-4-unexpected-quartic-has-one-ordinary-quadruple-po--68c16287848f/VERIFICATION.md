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

Run `python verify.py` with Python and SymPy available. The script uses exact rational arithmetic.

It reconstructs the explicit \(B_4\) unexpected-cone formula from the cited source, specializes the parameter to \([1:2:4:8]\), and verifies the linear change that removes the vertex coordinate. It then checks all 16 \(B_4\) base points, computes the rank of the quartic interpolation system with a quadruple point at the witness, and obtains a one-dimensional kernel.

For the plane quartic base, the script forms all three partial derivatives and computes a Gröbner basis on each standard projective patch. Each basis is \([1]\), which is an exact certificate that the base quartic is smooth over \(\mathbb C\). The remaining resolution and discrepancy assertions use the displayed intersection-theoretic calculation from RESULT.md; the script checks its numerical identities.

The exact computations establish a nonempty smooth-base parameter locus. Openness and the published generic uniqueness statement are the non-computational ingredients used to pass from the witness to the generic claim. Special parameters outside that open set are not classified.
