---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For agent i, filling in all indices between a coalition's extremal indices a,b leaves its range unchanged and increases its size. The strongest requirement is thus the maximum of h+z_a−z_b over a<=i<=b, which separates into two independent extrema and yields a concrete attaining block. In particular rho_i>=h>0. With d=x_(i+1)−x_i, each of the nonnegative increments of the running prefix maximum and suffix minimum is at most max(0,d−h). Hence each forbidden endpoint increases by at least min(d,h). A feasible point strictly avoids all agent locations, so in gap k the left exclusions reduce to y>=R_k and the right exclusions to y<=L_(k+1); the sentinels correctly clip the outer gaps to [0,1]. Endpoints remain allowed and coincident agents or empty gaps cause no exception. The slope 2k−n and intercept S_n−2S_k follow by expanding absolute values; testing one endpoint per nonflat gap and retaining whole flat maximizing gaps gives the exact optimum and argmax, or reports infeasibility. The scans use linear arithmetic after sorting. At alpha=2 the midpoints of n equal subintervals each give radius 1/(2n), leaving exactly n+1 isolated endpoints. The prior factor-two existence theorem extends to larger alpha by weakening all inequalities. The strict UFS comparison profile has PF optimum 31/24 and permits 37/24 under UFS, as claimed. Independent reproduction `python3 -B /workspace/review_checks.py 2` verified 1,004 rational instances using direct subset demands, all exclusion cells, and critical-point welfare. The source checker also has an auxiliary sorted endpoint sweep; the stated linear complexity is for the ordered gap scan, not that auxiliary test.

## originality

PASS

The obnoxious PF axiom and universal factor-two existence are prior results. The distinct claim is the all-alpha per-agent exact envelope, ordered gap geometry and linear after-sorting optimization with a sharp disconnectedness bound. The checked existence proof and welfare analysis for weaker notions do not give this full statement. No novelty is claimed for completing coalitions to contiguous blocks as a general technique.

## value

PASS

The complete fair region and certifying coalition demands address a natural shortcoming of a pure existence result. The sharp n+1 components demonstrate that there is genuinely linear-size set-valued output to represent, and the strict UFS/PF welfare separation shows why the established weaker optimization cannot simply be reused. The result does not claim incentives or multi-facility scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
