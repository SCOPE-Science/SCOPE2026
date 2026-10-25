---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

PASS. The indexed double-involute map reduces on the 3-periodic center vertices to a row-stochastic 3x3 matrix T. The two half-sum involutes give T_ij = rho delta_ij+(1-rho)w_j with rho=xyz/(4abc), x=b+c-a, y=c+a-b, z=a+b-c, and w=(b y^2,c z^2,a x^2)/(4abc-xyz). This fixes O=Σw_j M_j, multiplies all two independent differences by rho at every double step, and AM--GM yields 0<rho≤1/4, equality exactly x=y=z. The x=y=1,z∈(0,1] path realizes the full range.

## originality

PASS

PASS on best-of-knowledge statement comparison. Existing Minkowski involute and general discrete spectral frameworks give finite maps, limiting center or regular examples but do not state the all-skew-hexagon exact scalar rate, explicit positive three-point barycenter, sharp universal 1/4 rigidity and entire attainable range.

## value

PASS

PASS. The direct barycentric fixed point and one-eigenvalue homothety sharpen a previously iterative construction in the first nontrivial three-direction case; the 1/4 bound is sharp with a geometric rigidity theorem, a natural stability quantity and all-rate classification. It is not merely rewriting the known convergence statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
