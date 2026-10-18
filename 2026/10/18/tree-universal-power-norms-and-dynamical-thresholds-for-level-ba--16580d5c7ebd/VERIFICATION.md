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

# Verification and limitations

The proof is analytic. The precise normalizations are \(c_0=1\), \(A_k(f)=c_k^{-1}\sum_{|v|=k}|f(v)|\), and the outer Cesàro average \((N+1)^{-1}\sum_{k=0}^{N}A_k(f)\). Edge weights at depth \(k+1\) equal \(\gamma c_k/c_{k+1}\). The finite-depth telescope and the scalar Tonelli identities are both exact. Strict log-convexity of \(H_p(t)\) proves equality only on the matching level, and the root triangle inequality fixes the common-phase condition. All exponent quantifiers are \(p\in(1,\infty)\), \(n\in\mathbb N\) with no endpoint claim.

For reproducibility, run `python check.py` with `mpmath` available. The script evaluates finite-support Cesàro norms with exact infinite zeta tails at high precision and checks sampled sharp inequalities plus an uneven-branching telescope. It is supplementary evidence only. The infinite theorem requires the analytic steps in RESULT.md; the numerical checks cannot establish universal quantifiers.

The frequent-hypercyclicity assertion for \(|\gamma|>1\) invokes the standard published Frequent Hypercyclicity Criterion, whose hypotheses are checked explicitly. No independent audit or external formal verification has been performed. Publication priority and the inaccessible 2025 multiplier paper remain the stated scientific limitations.
