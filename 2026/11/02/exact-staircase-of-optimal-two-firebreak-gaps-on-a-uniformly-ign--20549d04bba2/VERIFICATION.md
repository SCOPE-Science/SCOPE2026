---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For N>=4, removing two distinct cycle edges yields path components of j and N-j patches. Independent Bernoulli ignition with q=1-p saves j q^j+(N-j)q^(N-j) in expectation, so B_j=N-H_j. The exact adjacent difference factorizes as q^j(1-q)[sum_{a=1}^{N-2j-2} q^a+(N-j)q^(N-2j-1)-j]; its bracket is strictly increasing from -j to positive endpoint for j<floor(N/2), hence a unique crossing r_j in (0,1). The nonstandard global argument extends j to x and writes h(x)=exp(-Nt/2)[N cosh(ty)-2y sinh(ty)], y=N/2-x,t=-log q. Derivative sign is Nt/2-1-z coth z, a strictly decreasing function of z, so the sampled H_j has no strict valley nor three consecutive equal values. A reversal or equality of adjacent thresholds would create precisely such a valley or triple tie, forcing all r_j strictly increasing and each unique globally optimal gap on (r_{j-1},r_j). Boundary N=4 and odd/even N are included. Independent exact rational checks and numerical root isolation found N=8 thresholds 0.469138898665, 0.569240819317 and 0.6; exact point checks confirm all four gaps. Finite N sample checks supplement rather than establish the all-N argument.

## originality

PASS

Qualified PASS: Finney 2001 and later wildfire-treatment optimization papers study spatial propagation, large landscapes and simulation/centrality, whereas this claim is the exact deterministic-component independent-ignition cycle model. Hwang–Rothblum generic Schur-convex partition results do not directly yield a parameter-dependent staircase since x exp(-t x) changes curvature. The explicitly ordered thresholds and no-skipped-gap theorem were not found in inspected literature, but an equivalent elementary partition theorem may exist, and a specialized 2010 paper was not read in full.

## value

PASS

Exact optimal placement across all ignition risks in a mathematically natural minimal network partition provides a complete phase diagram and excludes skipped geometries and triple ties. Although the homogeneous ring is a stylized model, the strict staircase is not merely obvious equal spacing: at high ignition probability adjacent cuts win, all intermediate gaps become uniquely best, and equal spacing is optimal only below a sharp threshold. This structural calculation is potentially reusable as a reliability/fragmentation benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
