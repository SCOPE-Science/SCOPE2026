---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Uppal's reduction leaves the geometric types A2 and A4 over F4; each has one geometric singularity and two or four exceptional curves, respectively, so Proposition 9.5 gives separability. In the characteristic-two double-plane model, each rational zero of the nonzero quadratic coefficient has a unique rational lift. Two such zeros suffice. The only remaining conic is the pair of conjugate lines, whose binary anisotropic form can be scaled and transformed to X²+XY+ωY² (the mixed term is nonzero and all trace-one constants are equivalent by an Artin–Schreier shift). Independently recomputed the binary evaluation rank outside its single rational zero: in different projective charts and a different coefficient basis, direct enumeration of every subset of the 20 rows found exactly the empty relation and the sum of all 20 rows. The kernel has dimension 11. The map H↦H²+QH has image in that kernel and its domain has dimension 12 with kernel {0,Q}, so its image is the full trace kernel. If no rational point lies above a point where Q≠0, all trace values equal one. Subtracting ωQ² puts the quartic in the kernel, and shifting W by H+βQ, with β²+β=ω, yields two distinct geometric factors. This contradicts geometric integrality. Any fiber where Q≠0 with trace zero has two rational points, smooth by the W derivative in the corresponding affine chart. The resulting theorem uses no enumeration of all RDP surfaces, and the bound is sharp by the cited F2 examples.

## originality

PASS

Credit resolution of the F4 gap, in particular the unresolved A2 type, and the stronger statement for any geometrically integral anisotropic-branch double plane over F4. The point theorem away from F2 and F4 and the F2 sharpness examples are prior; the A4 point conclusion separately follows from standard resolution trace bounds and should not be credited as a new independent theorem.

## value

PASS

The proof removes the remaining field-size exception apart from the genuinely sharp F2 boundary in a published RDP point theorem. Its trace-kernel factorization also gives a structural result for arbitrary integral separable double planes with the specified conic, not a finite census of presentations of the surface types. The value does not depend on claiming A4 as an independently new subcase.

The dated certificate retains the supplied scientific assessment, sources and limitations.
