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

The full proof is contained in RESULT.md. Exact coefficient identities use normalized weighted Bergman monomial moments. The only nonstandard approximation step is the finite-geometric decomposition with an exact relative remainder, and its omitted-tail estimate sums over every remaining row and every input coordinate. The critical beta constant follows from uniform gamma-ratio estimates and Abelian summation; the displayed limit is not extrapolated from data.

CHECK.py is a standalone finite diagnostic. It constructs partial coefficient matrices and the explicitly specified dyadic approximants for three target weights and multiple cutoffs, and verifies inequalities on the retained and omitted finite row ranges. Its large-index scalar diagnostic has a finite input cutoff and is not an exhaustive infinite-tail verification. It requires Python with NumPy and SciPy and performs no network access. The numerical checks cannot establish novelty, infinite-dimensional membership, or the limiting residue.

No independent mathematical audit has been performed. No assertion of external certification is made.
