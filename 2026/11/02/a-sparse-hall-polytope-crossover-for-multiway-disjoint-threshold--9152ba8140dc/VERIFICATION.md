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

Execute `python verify.py` with NumPy in the same directory as the standalone source; compare the exact rational results, Gaussian integral values and assertion count with `verification_output.txt`. The verifier independently matches Hall's subset conditions against exhaustive witness allocations in small boxes, checks rational probability normalization and event-factorization, evaluates the critical two-event Gaussian integral, and uses seeded simulations at the predicted scale. These finite checks do **not** prove the general limiting theorem, which requires the probabilistic proof in `RESULT.md`.

The limiting-Gaussian formula uses fixed \(r\), arbitrary real offsets, sparse Bernoulli \(p_n\to0\) with \(n p_n\to\infty\), and a finite or divergent collision parameter. The computer checks are finite-size cross-checks only, do not cover all \(r\) or all \(p_n\), and cannot decide historical novelty.
