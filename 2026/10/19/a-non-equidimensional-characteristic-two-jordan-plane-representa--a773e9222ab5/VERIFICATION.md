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

The proof supplies the polynomial equations, irreducibility argument, Jacobian calculation, and centralizer orbit reduction valid in arbitrary characteristic-two finite fields and in their algebraic closures as stated.

Run `python jordan_plane_checker.py` in an ordinary Python 3 environment. The dependency-free program constructs every two-by-two matrix and every invertible change of basis over GF(2) and GF(4), tests all relation solutions, reconstructs every simultaneous-conjugacy orbit, and compares the resulting fiber counts against the closed formulas.

Actual full-program output: `q=2: solutions=40` with orbit-type counts `(6,4,2)`; `q=4: solutions=1216` with orbit-type counts `(20,16,12)`; terminal marker `VERIFY_JORDAN_PLANE_OK`. Its component/intersection point counts were also checked. These calculations do not certify claims over all finite fields, nor do they verify scheme-theoretic radicality or independent novelty.
