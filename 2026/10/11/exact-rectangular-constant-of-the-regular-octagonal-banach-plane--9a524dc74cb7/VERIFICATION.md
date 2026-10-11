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

The proof uses the exact octagonal norm and the support-functional characterization of Birkhoff--James orthogonality. Dihedral symmetry leaves one representative edge and its adjacent vertex.

For the edge case, the exact flat-segment length is at most \(2(\sqrt2-1)\), giving the candidate \(2\sqrt2-1\); after leaving the unit edge, the coordinate lower bound makes the quotient no larger than the greater of its edge-end value and \(\sqrt2\).

For the vertex case, the first unit-direction branch has increasing intersection value ending at \(\sqrt2\). The second branch has intersection quotient
\[
R(u)=\frac{u+1+\sqrt2}{1+\sqrt2-u},
\]
with positive derivative and endpoint value \(2\sqrt2-1\) at \(u=1/\sqrt2\).

Run `python verify_rectangular.py` to check the critical identities and signs using exact arithmetic in \(\mathbb Q(\sqrt2)\). The script is a consistency checker for the displayed algebra; it does not replace the continuum proof.

Limits: no claim is made for other regular polygons, for \(p\ne1\), or for a complete classification of all extremizers.
