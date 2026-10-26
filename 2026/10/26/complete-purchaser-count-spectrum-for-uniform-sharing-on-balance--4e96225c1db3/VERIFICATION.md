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

# Verification of the purchaser-count classification
The proof in `RESULT.md` supplies the infinite, all-parameter argument through exact capacities, coverage inequalities, and an explicit modular nomination construction. No numerical approximation is needed in the proof.

The independent finite checker `verify_spectrum.py` enumerates all possible exact-\(k\) nomination subsets of the opposite-part nonpurchasers for each fixed number of purchasers on both sides, independently of the proof inequalities. It computes feasible count spectra for all \(35\) pairs with \(2\le n\le8\) and \(1\le k\le n\), and asserts agreement with the theorem. Executing `python3 verify_spectrum.py` returned a PASS for all pairs and the gap instances \(\mathcal E(4,3)=\{2,4\}\) and \(\mathcal E(8,7)=\{2,8\}\).

Finite verification cannot certify larger network orders. The result does not address unbalanced networks, variable capacities, nonspecialised equilibria, or arbitrary utility/welfare rankings. Independent mathematical audit has not occurred.
