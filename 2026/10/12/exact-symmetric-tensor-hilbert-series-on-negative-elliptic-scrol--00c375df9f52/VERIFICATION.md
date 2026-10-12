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

# Verification details

The proof in `RESULT.md` uses an actual graded-ring isomorphism from Denisi--Höring and an exact sheaf-filtration/elliptic-Riemann--Roch calculation. The following numerical checks were performed on the included `VERIFY.py`, which uses only the Python standard library:

```
python3 VERIFY.py
VERIFY_OK: 12 degrees, weights 0..80, coefficients and boundaries
```

Checked identities: the double positive-line-bundle summation \(1+d\sum_{j=1}^k\sum_{\ell=1}^j\ell\), the closed formula \(1+d\binom{k+2}{3}\), and the rational Hilbert-series coefficient for \(1\le d\le12\) and \(0\le k\le80\); plus the first difference and the \(k=0,1\) boundaries. The quotient \(3!\) times the leading cubic coefficient equals \(d\).

**Limits:** finite integer tests do not verify every weight. The proof requires the established Denisi--Höring elementary transform/ring identification, the acyclicity of twisted line bundles under the ruling, and the Atiyah--Serre symmetric-power section count. Each needed infinite step is stated and justified or explicitly referenced. No independent external audit or certification has been performed.
