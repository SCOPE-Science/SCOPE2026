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

Run `python3 verify.py` with Python 3 and only its standard library. The script enumerates every ternary relation of a new point to the \(2n\) named parameters for \(n=1,2,3,4,5\), tests the enlarged strict relation for transitivity, and forms a bivariate count by the numbers of strict predecessors and successors. An independent binomial-coefficient construction of the asserted polynomial is then compared coefficient by coefficient. It also checks the mixed-profile and total counts, the limiting moment arithmetic, and exact large-finite coefficients for dimensions 10, 30 and 100. The expected stdout is embedded in `verification_output.txt`.

The small finite computations do not prove the identity or asymptotic theorem for arbitrary \(n\). The proof in `RESULT.md` supplies the global parameter decomposition and quantitative coupling. The checker does not assess originality and does not constitute an independent scientific audit.
