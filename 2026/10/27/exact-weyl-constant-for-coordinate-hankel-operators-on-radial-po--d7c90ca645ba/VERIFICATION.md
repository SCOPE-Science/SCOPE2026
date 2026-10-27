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

# Verification and reproducibility

The exact moment formula and diagonalization appear in `RESULT.md` and are the core proof, not empirical assumptions. The accompanying `CHECKER.py`, runnable with `python3 CHECKER.py`, tests three uniformly separated directions of degree shells at degree 2000 for three representative parameter pairs and checks the \((m,d)=(2,2)\) beta-polynomial integral by exact rational arithmetic. The checker was executed successfully before this report was assembled. These finite checks do not establish asymptotics; the proof uses a uniform gamma-ratio estimate and a measure-zero-boundary lattice Riemann sum. The counting theorem, inversion, compactness and Dixmier-trace conclusion rely on those analytic steps. No third-party certification or independent audit has been performed.
