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

# Computational verification

The complete `verify_franklin.py` is supplied with this statement; use Python 3.9+ and run `python3 verify_franklin.py` in a directory containing that program. No third-party dependencies, downloaded data or external certificates are required.

The program enumerates the full graph and all canonical simple cycles; constructs integral oriented zero-, one- and two-dimensional cellular bases of the unordered two-particle deleted product; verifies all boundary compositions vanish; constructs all nineteen oriented cycle-product tori and verifies each is a cycle; and checks the exact nine-cycle determinant \(+1\) using the fraction-free Bareiss algorithm. It computes an integral inverse of the unit minor and reconstructs each of the nineteen full 117-coordinate torus chains from its nine basis coordinates. Partial ranks are computed by rational elimination, and unit integral minors certify saturation of all proper length-type sublattices. It also backtracks through all graph automorphisms and checks transitivity on the three torus families.

The explicit zero-based basis-column indices are `(0,1,2,4,6,8,12,13,14)` relative to the twelve square–hexagon columns followed by the four hexagon–hexagon columns. The zero-based two-cell indices are `(0,2,4,7,13,15,17,39,41)`. The program prints `VERIFY_OK_FRANKLIN_MIXED_LENGTH_INTEGRAL_TORUS_BASIS` on success.

Finite-field rank alone does not establish integral saturation; that conclusion uses the exact unit determinant and complete integer reconstruction. The checks establish only the stated graph-specific finite complex and its full second homology, not the existence or nonexistence of analogous bases for arbitrary other graphs. Independent audit has not been performed.
