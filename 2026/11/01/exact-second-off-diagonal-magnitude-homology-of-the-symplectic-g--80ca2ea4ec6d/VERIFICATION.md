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

Run `python3 verify.py` in the directory containing `gq_constructor.py`; only Python 3 standard-library modules are needed. `verify.py` constructs both relevant length-five magnitude boundary maps over \(\mathbb F_2\), verifies the chain condition in every degree-four basis column, obtains exact mod-two ranks by bit-vector pivot elimination, and certifies both point-to-line orbit sizes by closure under explicitly constructed symplectic transvections. Reversal of magnitude chains covers the opposite endpoint ordering.

The saved run records degree-(2,3,4) dimensions (18,81,120) and differential ranks (18,63) at distance one, and dimensions (28,87,72) and ranks (28,50) at distance three. The two point-line orbits have sizes 160 and 1440. All same-side blocks vanish by odd-distance parity. The observed final line is `GQ33_MAGNITUDE_EXACT_MOD2_VERIFIED`.

This verifies the precise finite graph and mod-two coefficient field only. Independent audit: not yet performed.
