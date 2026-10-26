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

Execute `python verify.py` in the directory containing this file, using Python 3.10 or later and no third-party packages. The verification script performs fraction-exact elimination of \(K+L\), direct evaluation of \(z^{\mathsf T}Lz\), an independent evaluation of the derived rank-one quadratic for a changing tie, and exhaustive checking of the eight corners of a small three-edge box against a 27-point rational grid.

An execution of the packaged script reported `PASS`, 1,105 exact-fraction assertions and 84 base-network configurations. It verified the four three-agent corner energies \(148/1225,16/169,199/1521,87/800\). These examples and finite checks are finite corroboration only. The universal corner guarantee follows from the symbolic rank-one identity and sequential endpoint replacement, not from testing instances. Independent audit remains unperformed.
