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

# Verification of exact diffusion positivity

**Analytical checks.** The defining spectral identity \(L^2-(a+b)L+ab(I-J/n)=0\) follows from the stated three-eigenvalue hypothesis. The proof verifies the spectral projectors, derives the rational off-diagonal formula, and reduces the entire sign question to a quadratic. The critical edge ordering is proved by comparing quadratics at the first positive root. The diagonal sign follows from strictly positive scalar Padé multipliers. The strongly regular specialization uses its adjacency quadratic identity and the two nonzero Laplacian eigenvalues.

**Reproducible finite checks.** Run `python3 verify.py` with Python 3 and no external dependencies. The source file is embedded alongside this note. The actual completed run reported `VERIFY_OK 45967 exact rational identities/inequalities 17 weighted graph instances`. The test families include strongly regular primitive and imprimitive graphs, a weighted star family, and asymmetric weighted three-vertex graphs. Exact rational elimination reconstructs the rational matrix step independently in small instances; rational identities and sign tests corroborate the symbolic formulas.

**Boundaries and unverified domains.** Infinite graph order is not checked exhaustively by the code and relies on the analytical proof. The statement does not apply to graphs with four or more distinct Laplacian eigenvalues, or to arbitrary directed Markov generators. Independent mathematical audit has not been performed.
