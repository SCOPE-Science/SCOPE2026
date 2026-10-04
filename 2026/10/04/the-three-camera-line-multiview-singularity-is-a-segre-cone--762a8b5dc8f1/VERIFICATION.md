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
The exact replay script `verify.py` constructs the dehomogenized \(4\times3\) back-projected-plane matrix, computes its maximal minors, and checks that after subtracting the third column from the first two the rank condition is exactly the vanishing of the \(2\times2\) minors of a generic \(3\times2\) matrix of six independent linear coordinates. It checks the redundancy identity for the fourth maximal minor and verifies the inverse linear coordinate map. It also checks initial coefficients of the Hilbert series against \(\binom{n+2}{2}(n+1)\).

The proof of multiplicity does not rely on finite experimentation: the projectivized cone is \(\mathbb P^2\times\mathbb P^1\) under \(\mathcal O(1,1)\), whose degree is the intersection number \((H_1+H_2)^3=3\); the Hilbert--Samuel multiplicity of the vertex of this standard graded cone equals that projective degree. The script is a consistency check for the coordinate algebra, not a substitute for this argument.

Scope limit: three cameras with linearly independent centers over \(\mathbb C\). The known uniqueness of the singular point is cited rather than reproved as a novelty claim.
