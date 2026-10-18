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

# Reproducibility

Run `python3 verify_fano_quartic.py` in a Python 3.10+ environment with SymPy 1.12+ available. Its JSON output is included verbatim as `verification_output.json`.

The code enumerates the complete 15-dimensional binary coefficient space of quartics excluding zero, checks every one of the seven rational points and its three partial derivatives, and retains those with three nonsingular rational points whose tangents cover the Fano plane. It obtains 448 candidates. The 168 explicitly enumerated coordinate substitutions partition them into orbits of size 84, 84, 84, 28 and 168. Each of five orbit representatives is tested for geometric singularities by reduced Gröbner bases of the dehomogenized affine Jacobian ideals in all three charts. Four representatives have unit ideals throughout; the excluded representative has a geometric singularity over the quadratic extension. This gives exactly 364 smooth equations in four projective orbits.

The program independently checks direct monomial evaluation and all three derivatives of all 448 candidate forms against precomputed bitmask evaluations. It also verifies the distinct and concurrent rational tangents for each of the four smooth orbit representatives, as well as noncollinearity of their rational points and the center-on-curve counts 252 and 112.

These checks are exhaustive for quartics over the binary field. They do not address fields of higher cardinality or algebraically closed isomorphism classes of the four representatives. The ideal tests certify absence of geometric singularities within the stated finite family; no independent external audit has been performed.
