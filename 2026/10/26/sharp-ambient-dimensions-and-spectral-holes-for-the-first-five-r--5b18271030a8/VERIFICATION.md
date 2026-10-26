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

## Exact checks
Run `python check_sinc.py` using SymPy. Exact rational arithmetic reconstructs the central B-spline pieces for the first five sinc powers, applies the radial Fourier dimension-walk operator, and verifies the finite polynomial identities, jump sizes, signs and obstruction witnesses. Successful execution prints `PASS`.

## Mathematical limits
The computation does not, by itself, prove positivity on every finite configuration or exclusion in even dimensions. The written proof uses Fourier uniqueness, the radial dimension-walk identity, nonnegative radial measures, and an Abel projection argument. No external independent validation has been performed.
