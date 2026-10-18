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

Run `python verify_complete_graph_reset.py` with Python 3, NumPy, SciPy and SymPy. The script independently enumerates all fixed-particle-count configurations for \(3\le N\le8\), builds the unreduced continuous-time generator with a full-configuration reset, solves its stationary linear system, and checks all one-point means and 2,766 distinct-pair covariance cases at six positive rates. It separately checks the three covariance simplifications as SymPy identities. The run returned `PASS: 2766 independent finite-generator covariance comparisons plus all one-point means; 3 symbolic polynomial identities.`

A separate exact-rational finite-state matrix solve checked threshold cases \((N,k,r)=(5,3,4)\) and \((6,3,6)\) and an off-threshold case \((6,3,1)\). Critical infinite-family identities follow from the proved moment equations; no finite enumeration is being treated as an infinite proof.

# Scope of verification

All clocks use unit edge exchange rates and the single fixed reset microstate specified in the finding. The checks do not establish originality, do not address arbitrary graphs, and do not establish higher-order negative association. No independent audit has been performed.
