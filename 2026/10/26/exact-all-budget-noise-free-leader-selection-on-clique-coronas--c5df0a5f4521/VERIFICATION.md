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

# Verification

The standalone `verify_corona.py` uses SymPy and NumPy as declared in `requirements.txt`. From the supplied directory run `python3 verify_corona.py`. The current run printed exactly the lines in `verification_output.txt` and exited successfully.

The six symbolic identities are the exact rational expressions for the first core-leader comparison, strict convexity, and the second core-leader discrete difference. Exact rational enumeration checks every legal occupancy profile for 1,932 budgets across clique sizes 3–44, including absence of integer ties. Direct NumPy inverses check 5,432 concrete leader subsets over clique sizes 3–6, and 468 orbit representatives through clique size 8 are independently inverted in exact SymPy arithmetic. The analytical Schur-complement and inequality proof, not this finite census, establishes the theorem for all integers in scope. Numerical inversions use a tolerance of \(10^{-7}\) solely for cross-validation against exact rational values.

No external mathematical audit, generalization to arbitrary graphs, or guarantee of complete global bibliographic coverage is claimed.
