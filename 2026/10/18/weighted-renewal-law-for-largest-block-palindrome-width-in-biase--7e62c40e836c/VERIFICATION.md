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

# Verification details

The complete proof is in `RESULT.md`. To replay the finite computations, run `python verify.py` using a standard Python interpreter. No nonstandard packages or downloaded datasets are needed.

The checker independently enumerates every word through length \(12\) for each of three binary distributions, computes its greedy shortest-border decomposition, and compares the resulting **exact rational** width probabilities against the renewal recurrence. It separately checks the ternary uniform distribution through length \(8\), validates the generalized weighted unbordered-word recursion against direct enumeration with arbitrary rational letter weights, and computes the biased example parameter through \(100\) terms.

For \(\boldsymbol\pi=(1/4,3/4)\), the scalar collision probability is \(s=5/8\); after \(100\) terms the rigorous error is at most \((5/8)^{101}/(3/8)<6.46\cdot10^{-21}\). This certifies the displayed decimal precision. The direct checker does **not** prove the infinite convergence statement: the unbounded-length theorem is established by the independent-stream renewal coupling and exponential-moment argument given in `RESULT.md`.

Expected terminal output includes `ALL_CHECKS_PASSED`. These checks are same-model reproducibility work; independent mathematical audit has not been performed.
