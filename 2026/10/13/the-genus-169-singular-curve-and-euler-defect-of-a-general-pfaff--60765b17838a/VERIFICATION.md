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

The exact-integer checker `verification/check_pfaffian.py` uses the projective bundle \(\mathbb P_{\operatorname{Gr}(4,8)}(\bigwedge^2Q^*)\), its Segre class and the Grassmannian Vandermonde coefficient integral. Run with `python3 verification/check_pfaffian.py`, with only the Python standard library. The expected output is `PFAFFIAN_SINGULAR_CURVE_NUMERICS_OK`.

The checker independently evaluates \(\int_G h_{16}(x_i+x_j)=84\), \(\int_Gc_1(Q)h_{15}(x_i+x_j)=168\), and the Grassmannian degree \(24024\); it derives \(g=169\), the Euler smoothing defect \(336\), and \(\chi_{\mathrm{top}}(Y)=1312\). Generic smoothness of the curve, reduced Jacobian ideal, relative canonical bundle and six-variable quadratic normal form are established by the accompanying mathematical argument; software arithmetic alone cannot prove these infinite geometric assertions. Source-comparison risks are reported separately and no independent scholarly audit has been carried out.
