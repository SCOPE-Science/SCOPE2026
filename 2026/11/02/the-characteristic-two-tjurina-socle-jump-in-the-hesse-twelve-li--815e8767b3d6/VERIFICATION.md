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

# Exact arithmetic verification

Execute `python3 verify_hesse.py` with no third-party packages. The recorded `verification_output.txt` ends in `VERIFY_OK`.

The checker reconstructs all twelve line triples over the Eisenstein integers and exhaustively computes the \(220\) determinant norms. The histogram is \(0:36,1:28,3:81,9:72,27:3\). Thus every nonzero determinant stays nonzero in characteristic away from three. Separate line enumeration over \(\mathbb F_4\) and \(\mathbb F_7\) gives nine fourfold and twelve double intersections.

For the local Tjurina ring, the checker uses the nine standard monomials \(1,v,v^2,v^3,u,uv,uv^2,uv^3,u^2\), computes the Hilbert function \((1,2,3,2,1)\), and calculates the nullity of the joint multiplication maps \((\cdot u,\cdot v)\): it is two in characteristic two and one in tested odd characteristics. The general local calculation is the symbolic derivative-and-regular-sequence proof in `RESULT.md`; finite tests are checks, not an infinite-field proof.

All assertions are for the **intrinsic** Tjurina scheme including the defining equation. No gradient-only scheme, characteristic-three degeneration, or positive-characteristic freeness assertion is verified. No external independent audit has been performed.
