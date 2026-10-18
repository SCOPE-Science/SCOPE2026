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

# Reproducible verification

Run `python3 artifacts/check_heisenberg.py` with Python 3.11 or newer. No external packages are required. Its final line must be `ALL_EXACT_CHECKS_PASSED`.

The direct endomorphism-matrix test (including \(\mathbb F_4\) arithmetic) checks \((n,q)=(1,2),(1,3),(1,4),(1,5),(2,2)\) and yields exact rank profiles \((1,12,1)\), \((1,36,1)\), \((1,80,1)\), \((1,150,1)\), and \((1,240,960,1)\), with absent intermediate ranks equal to zero. It checks all matrix pairs and central coefficients in the specified parameter ranges, not just a random sample. A separate exhaustive enumeration of all \(q^9\) linear self-maps for \(n=1\), \(q=2,3,4\), uses the bracket table itself to independently verify the normal form's completeness and each rank count. Reduced-row-echelon enumeration verifies isotropic-subspace counts at \((n,q)=(2,3)\) and \((3,2)\).

The field-uniform proof follows the derivation-preserving-center normal form, the scalar idempotent split, isotropic-image characterization, and exact complement counting. The finite tests do not imply the theorem in arbitrary dimensions or extension-field sizes; those are consequences of the proof. The counts concern Lie algebra endomorphisms, not group homomorphisms. Independent audit has not been performed.
