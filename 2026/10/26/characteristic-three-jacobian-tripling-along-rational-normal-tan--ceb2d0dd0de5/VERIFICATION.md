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

# Reproducibility and limitations

The accompanying `check_tangent.py` runs with Python 3 and SymPy. Execute `python check_tangent.py` and expect a single `VERIFY_OK` message. This checks characteristic-reduced coordinate identities for \(3\le d\le11\) and primes \(2,3,5,7\), explicitly checks the quartic and its partial derivatives in characteristic three, and corroborates the exact complete-intersection and filtration Hilbert polynomial formulas. It does not enumerate all degrees or characteristics.

The general proof is the algebraic identity \(k[u,s^2,s^3]=k[u,y,z]/(z^2-y^3)\) for odd characteristics, followed by the exact Fitting-ideal derivative calculation and a two-chart nilpotent transition of weight \(-4\). The smooth tangent-direction charts exclude additional singular supports. No external certificate of independent verification is claimed.
