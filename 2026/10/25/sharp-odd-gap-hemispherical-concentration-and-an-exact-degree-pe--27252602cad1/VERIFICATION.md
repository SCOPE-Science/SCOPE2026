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

# Reproducibility

Run `python check_spherical_packet.py` in an environment with NumPy and SciPy. The checker independently reconstructs normalized associated-Legendre overlaps by quadrature and checks exact factorial identities, angular-order ratios, the degree-peak law, and the spectral gap formula using rational arithmetic. It reports `VERIFY_OK exact_assertions=9910 quadrature_integrals=1260 max_abs_error=2.797e-14` in the tested environment. Those finite assertions are corroborative; the proof for all \(\ell\ge0\) and all odd \(d\ge3\) is in RESULT.md.

The equality classification uses the declared Condon--Shortley phase convention. No claim of independent external validation has been made.
