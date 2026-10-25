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

# Reproduction and limits

Run `python3 verify.py` with the Python standard library. The program independently writes the full generator on two opinion-count coordinates and solves a finite continuous-time stationary distribution with exact fractions for twelve small parameter sets, including two, three and four agents per community. It evaluates the within-/cross-pair disagreement and the mean and compares the exact results with the theorem's rational expressions. The program also checks derivative signs at numerical bracketed roots and samples the large-population convergence. Only finite cases are checked by code; the theorem for every \(m\ge2\) and all positive parameters depends on the generator proof and the Descartes-root/asymptotic arguments in RESULT.md. The ceiling identity and derivative factorization were separately checked symbolically. None of these checks is independent scientific audit.
