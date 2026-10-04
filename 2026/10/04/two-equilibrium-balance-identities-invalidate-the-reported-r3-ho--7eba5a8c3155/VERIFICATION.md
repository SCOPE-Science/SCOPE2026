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

The claim was checked from the printed equations and numerical values, not from figure appearance alone. At every positive equilibrium, the treatment equation gives \(z^*=(b+c)/\beta\); R3 therefore requires \(z^*=3\), whereas the published R3 tuple has \(z^*=1.5\). The exact treatment residual is \(-3/50\). The prey equation independently gives \(0<x^*<K\), excluding the earlier reported \(x^*=3.36\) for \(K=1\).

`verify_equilibrium.py` replays these checks with Python's exact rational arithmetic and evaluates the complete equilibrium residual vector for the R3 tuple. It must print `VERIFY_OK`. The calculation does not attempt to locate a corrected equilibrium or recompute any characteristic roots; those remain outside the proved scope.
