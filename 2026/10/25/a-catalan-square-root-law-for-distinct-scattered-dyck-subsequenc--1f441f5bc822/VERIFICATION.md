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

Run `python3 verify.py` using only the standard library. It exhaustively constructs all distinct subsequences for every source word through lengths 12, 11, 11, and 10, respectively, for Bernoulli probabilities \(1/2\), \(1/3\), \(2/5\), and \(3/7\); total source words checked: 18,428. It independently computes Catalan-substituted exact rational coefficients and checks through length 90. It also verifies the exact singular radius identity, the fair-source local derivative factor \(h=3\), and the asymptotic constant algebraically. Expected stdout: `VERIFY_OK source_words=18428 probability_vectors=4 exact_coefficients_through=90`.

The proof of the full infinite result rests on the first-greedy-completion distribution, Catalan enumeration, uniqueness of the dominant branch point, and standard square-root coefficient transfer. Finite enumeration is not used as an infinite proof. No independent audit of the scientific content has been performed.
