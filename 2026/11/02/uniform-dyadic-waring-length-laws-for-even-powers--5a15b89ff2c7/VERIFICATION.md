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

`verify.py` executes using Python 3 and its standard library only. It forms the residue set of \(k\)-th powers modulo \(2^n\), then uses cyclic bitset convolution to exhaustively enumerate the represented sums. This construction does not use the claimed union-of-cosets proof. It checks each represented-residue count for \(k\in\{4,6,8,10,12,14\}\), \(1\le n\le12\), and each \(1\le t\le2^{\nu_2(k)+2}\), totaling 1,056 cases. It also independently implements the published Proposition 32 fourth-power formulas for \(1\le n\le30\), \(3\le t\le15\), and compares their counts with the proposed recurrence, totaling 390 comparisons.

Expected success lines: `VERIFY_OK total=1056` and `PUBLISHED_FORMULA_COMPATIBILITY_OK comparisons=390`. The modular checks are exhaustive for their finite rings but do not directly verify the theorem's infinitely many exponents/moduli or the 2-adic Haar probability identities. Those claims depend on the exact group-theoretic proof. The 1977 historical modular Waring paper was not available in full text for priority comparison. Independent audit has not been performed.
