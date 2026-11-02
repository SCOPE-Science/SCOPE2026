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

# Reproducible finite checks and their limits

Run `python3 verify.py` using a standard Python 3 interpreter. The verifier constructs the adjacency matrix for each rectangular rook graph directly from same-row or same-column adjacency. It enumerates all four-cell subsets and checks the original cycle definition over their permutations. It then enumerates every possible selection \(D\), forms the closed-neighborhood complement from this adjacency, and asks whether any previously reconstructed four-cycle survives. It compares every coefficient to independent row-column inclusion-exclusion and checks all optimal-set counts.

Exhaustive tests include \((m,n)=(2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5),(3,6),(3,7),(4,4),(4,5)\), with the largest graph having \(20\) vertices. Algebraic tests compare the five case formulas with polynomial coefficients for \(2\le m\le8\) and \(m\le n<m+8\). The successful execution ends with `VERIFY_OK`.

The general theorem for arbitrarily large factors is proved by the residual-rectangle lemma, not by extrapolating these finite experiments. The verification does not establish publication priority, extend the theorem to induced four-cycles, or constitute independent mathematical audit.
