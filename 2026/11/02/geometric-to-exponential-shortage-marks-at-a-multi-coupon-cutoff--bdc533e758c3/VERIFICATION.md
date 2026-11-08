---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The final claim fixes iid uniform n types, deterministic m_n→∞ with m_n/log n→α∈[0,∞], quantile Q_m(b)=1/n, h=1-(m-1)/b and floor n(b+x/h) draws. The proof explicitly uses exact Poisson mass ratios p_(m-j)(u)/p_(m-1)(u)=(m-1)_(j-1)/u^(j-1). The three q regimes give point mass depth=1, geometric (1-q)q^(j-1), or h-scaled Exp(1). Integrating tail hazard, rare independent marked types after Poissonization, and squeezing monotone depth-tail counts between clock times x±δ with b h²/n→0 establishes the fixed-x marked Poisson limit and compound-Poisson transforms; it does not assert process-in-x convergence. Inspected verify.py checks exact multinomial and Gamma/Poisson finite formulas and is not substituted for asymptotic proof. Potential shortcut for gamma quantile requires a uniform moderate-deviation tail estimate; the stated m h²~2log n and h R_m→1 are consistent with the saddlepoint/gamma lower-tail asymptotics.

## originality

PASS

Best-of-knowledge PASS for the joint marked-shortage depth law and geometric/exponential phase diagram. Prior Long/Castro-Marinho cutoff/count results give the arrival or deficient-type count, not the conditional number of missing copies; relevant general marked Poisson methods do not automatically evaluate this distribution. An inaccessible or more general occupancy theorem could dominate, and full priority is not certified.

## value

PASS

The missing-copy depth and aggregate shortage are natural operational statistics distinct from merely counting incomplete coupon classes. An explicit geometric-to-exponential mark transition and compound-Poisson transform across m/log n regimes yield nontrivial estimable threshold properties, rather than a nominal rephrasing of a Gumbel completion time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
