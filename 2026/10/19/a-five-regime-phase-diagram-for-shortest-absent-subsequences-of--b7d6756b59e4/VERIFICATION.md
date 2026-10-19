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

Run `python3 verify.py` with the standard Python 3 library. The verifier constructs all binary candidates at the predicted shortest missing length and the immediately preceding length for every \(1\le a,b,k\le6\), checks them with an independently coded greedy subsequence scan, checks a separate maximal-run embedding formula, compares the complete predicted absent-subsequence sets, and checks all cardinalities. It also checks the Fibonacci and power-of-two count formulas to \(k=69\).

Observed output:

`VERIFY_OK exhaustive_parameter_triples=216 distinct_candidate_checks=139272 all_prior_lengths_present run_embedding_equivalence five_regime_counts fibonacci_to_k69`

A finite check does not prove a formula for infinitely many parameters. The infinite proof is the exact host-run embedding lemma and its generating-function and degenerate-run consequences in RESULT.md. No independent scientific validation has been performed.
