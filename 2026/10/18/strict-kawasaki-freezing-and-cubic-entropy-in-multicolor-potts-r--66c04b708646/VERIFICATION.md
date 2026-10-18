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

The exact local swap energy was derived from the three bonds affected by exchanging two different adjacent colors. An independent direct energy recomputation in `verify_potts_kawasaki.py` agreed with this local formula and with the domain characterization on 180008 spin configurations. Newton-sum polynomial coefficients agreed with the marked singleton-domain counts for all tested lengths and colors. The checker requires Python 3 and SymPy; execute `python verify_potts_kawasaki.py`.

Proof beyond tested sizes uses the cyclic-domain bijection, a color-cycle trace identity, and the uniqueness of the positive dominant generating-function singularity. Numerical enumeration does not prove the infinite-family assertion. No independent external audit has been performed. The theorem does not address reachability probabilities of frozen states under random initial conditions.
