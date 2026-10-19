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

# Direct verification
The checked artifact is the standalone `verify.py`, executed using `python verify.py` from this package. It uses only Python's standard library and exact rational arithmetic. The run returned `PASS`: six exact-regime and congestion-monotonicity cases including boundary parameters, four strict improvement gains, exact mixed equilibrium indifferences at \(\eta=3/2\), and 400 nearby rational parameter perturbations.

The proof in `RESULT.md` reconstructs all four payoff pairs directly, checks every pure strategy profile by strict best replies, and derives the unique mixed equilibrium analytically. The program is not claimed to certify all real-valued parameters; the symbolic argument covers the full range \(\eta>0\). Robustness is a continuity statement and not an experimentally estimated radius. No independent audit has been performed.
