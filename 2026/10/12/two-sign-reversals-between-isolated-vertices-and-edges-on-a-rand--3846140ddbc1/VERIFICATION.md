---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Under fixed-n iid uniform points on the periodic unit circle, conditioning on the isolation of one designated vertex leaves n−1 independent uniforms on the single complement arc of length L=1−2r. A pair in that arc is an edge exactly when linear separation ≤r, giving q=1−max(1−r/L,0)^2. Thus Cov(I,E)=n L^(n−1)[C(n−1,2)q−C(n,2)2r], identical to formula (1). Direct algebra yields a quadratic factor P_n(r)=−4+(3n+10)r−8nr² up to r=1/3 and a linear factor for larger r; both are continuous and give negative n≤5, the n=6 two zeros r=1/4,1/3, and for n≥7 the stated one root in (0,1/3) and one root in (1/3,1/2). For r=c/n, dividing the exact formula by n gives e^(−2c)(3c²/2−2c). Independently recomputed 4,851 rational (n,r) pairs against conditional and piecewise formulas and sign ranges; experimental checks are corroboration, the conditioning plus sign algebra prove all n and radii. n=1 and r=0 or ≥1/2 deterministic and zero.

## originality

PASS

The specific finite covariance together with a sharp two-reversal phase diagram and n=6 onset is not implied by the inspected large-deviation or marginal approximation statements. The conditioning device is standard, but the interval-dependent conditional pair geometry and complete sign determination are additional exact results. Checked equivalences and direct implications, not name matching.

## value

PASS

Counts of isolated vertices and edges are natural joint observables of random geometric graphs. A sharp positive-covariance window, two sign reversals, first possible sample size and sparse-limit critical c=4/3 distinguish periodic geometric dependence from Erdős–Rényi graph dependence, and give useful finite-size information not provided by marginal limit laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
