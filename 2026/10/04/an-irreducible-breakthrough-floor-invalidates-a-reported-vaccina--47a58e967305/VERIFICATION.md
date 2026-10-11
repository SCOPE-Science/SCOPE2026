---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Factoring the printed Eq. (3.1) gives the weighted-endpoint identity exactly and differentiation gives the monotonicity law. Full primary-source inspection confirms Eq. (3.1), Table 2 \(\beta_2=4.9\times10^{-7}\), and the printed \(v\approx0.023\) threshold claim. Direct high-precision substitution gives \(R_S\approx44272.53\) and \(R_V\approx2.66178>1\); therefore every convex combination is supercritical. The Figure 1 parameter statement gives \(R_0\approx3.66948\); the infected \((E,A)\) Jacobian block has negative determinant and therefore one positive eigenvalue.

## originality

PASS

The primary article explicitly reports the opposite qualitative threshold conclusion. The weighted-endpoint reformulation, irreducible breakthrough floor, corrected \((v,\beta_1)\) boundary, and Figure 1 instability were not stated in the inspected article, and targeted correction/erratum and published-result searches found no source giving this source-specific diagnosis.

## value

PASS

The correction invalidates a concrete policy threshold and a disease-free stability claim in a published epidemiological model. The endpoint decomposition also supplies the exact condition under which vaccination alone can ever cross threshold, so the result is substantively motivated despite elementary algebra.

The dated certificate retains the supplied scientific assessment, sources and limitations.
