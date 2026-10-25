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

# Reproduction

Run `python3 verify.py` with Python 3.10 or later, no external packages. The program exhausts all edge-retention states for the host graphs \(K_3\), \(C_4\), \(C_5\), \(K_4\), \(K_5\), \(Q_3\), \(K_{3,3}\), and the triangular prism. At each of \(p=1/4,1/2,3/4\), it uses exact rational weights to compute \(\mathbb{E}X_1\), \(\mathbb{E}X_2\), and \(\mathbb{E}(X_1X_2)\); all 24 resulting rational covariances agree exactly with the formula. A failing comparison raises an exception.

The proof in RESULT.md uses an exhaustive *symbolic* event-overlap classification for an arbitrary finite regular host: the number of shared closed-edge constraints is 0, 1, or 2, or there is an endpoint incompatibility. Triangle incidence counts exactly the 2-shared-edge cases. The sign root is checked by elementary quadratic algebra. The standard exponential limit gives the hypercube scaling.

Neither finite enumeration nor numerical floating-point diagnostics prove the unrestricted theorem. There has been no independent audit or external formal verification. Historical novelty remains limited to the inspected accessible literature described in RESULT.md and AUDIT.json.
