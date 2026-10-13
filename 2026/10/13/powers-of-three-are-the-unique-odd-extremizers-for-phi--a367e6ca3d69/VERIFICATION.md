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

The proof was checked algebraically at the level of definitions and boundary cases. The critical steps are: maximality forces an even non-power-of-two maximizer; the \(2\)-adic valuation of its totient forces exactly one odd prime factor and only one factor of \(2\); the ratio \(2q/(q-1)\) is at most \(3\), with equality only at \(q=3\); and powers of three make \(6n\) admissible exactly.

The included standalone script `verify.py` was replayed from the packaged path. It exactly maximizes the defining set for every odd \(n\le1000\) using the proved search cutoff \(m\le6n\), and separately tests the top-candidate divisibility criterion through odd \(n\le200000\). Its output was:

`VERIFY_OK exact_odd_n=500 exact_n_max=1000 top_candidate_odd_n=100000 top_n_max=200000`

These computations are finite consistency checks only. They do not replace the infinite proof. No independent audit has been performed.
