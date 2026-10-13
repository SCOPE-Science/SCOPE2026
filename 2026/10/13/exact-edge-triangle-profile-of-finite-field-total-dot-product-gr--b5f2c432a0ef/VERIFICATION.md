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

The proof uses only finite-dimensional linear algebra plus the standard finite-field count of isotropic vectors in dimension three. The central identity is checked independently by direct graph construction: for each tested graph, every edge is enumerated, both endpoint neighborhoods are intersected, and the resulting count is compared with
\[
q^{n-r}-1-\varepsilon(x)-\varepsilon(y).
\]

The executable check covers \((q,n)=(2,3),(2,4),(3,3),(3,4),(4,3),(5,3),(7,3)\). The \(q=4\) computation uses the explicit field \(\mathbb F_4=\mathbb F_2[a]/(a^2+a+1)\), so a nonprime field is included. In dimension three it also checks the exact numbers of anisotropic-anisotropic, isotropic-anisotropic, and dependent isotropic-isotropic edges and the derived triangle count.

Expected dimension-three profiles include:

- \(q=2\): edge multiplicities \(1\) on three edges and \(0\) on six edges; one triangle total.
- \(q=3\): edge multiplicities \(2\) on forty-eight edges, \(1\) on forty-eight edges, and \(6\) on four dependent isotropic edges; fifty-six triangles total.
- \(q=4\): edge multiplicities \(3\) on two hundred seventy edges, \(2\) on one hundred eighty edges, and \(13\) on fifteen dependent isotropic edges; four hundred fifty-five triangles total.

The verifier returns `VERIFY_OK`. Finite exhaustive checks support reproducibility but do not replace the symbolic proof for arbitrary prime powers and dimensions.
