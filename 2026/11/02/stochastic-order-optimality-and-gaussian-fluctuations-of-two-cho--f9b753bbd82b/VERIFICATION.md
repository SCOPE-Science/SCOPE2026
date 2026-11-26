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

Four ordered offers give the 3:1 weighting of the smaller and larger continuation tails. The symmetric exit survival cone d_j≥0, d_{j+1}≤3d_j is preserved: interior differences are weighted averages, and the odd midpoint difference is (3d_{m−1}−d_m)/4, the even one 3d_{m−1}/4. The adjacent ratio comparisons at both ends, including m=1,2, close the induction from (1,0,…). Thus the same action attains every finite-horizon exit minimum. Every stage finishes a.s. even under an adaptive controller, by positive-probability blocks of forced same-direction moves. Conditional stochastic dominance and sequential quantile coupling give whole-cover dominance. Under the proposed policy history-independent folded stage laws give independence even with history-dependent symmetric tie choices. From the one-level passage decomposition, given upper-level mean e and variance v, the next lower ones are e'=(4+e)/3 and v'=v/3+(e+e')²/4, with top data (1,0) or (4/3,4/9). This gives both parity formulas; deficit sums are 57/4 and 12, giving 6n−129/4 plus the stated tail error. A common down/up Bernoulli sequence dominates the folded stages by the biased walk from 1 with the displayed generating function; no bounded third-moment or Lyapunov gap remains. In the corrected files the target identification preserves each transient state's two offers and kills exactly on exit; L=1 remains separate. No mathematical conclusion was dropped or enlarged.

## originality

PASS

The corrected attribution identifies prior coverage of the one-stage moment formulas, and narrows the originality claim to all-deadline whole-cycle cover optimality. The aggregate variance and CLT are consequences, not an independent claim of stage-moment novelty. No inspected result implies the retained all-tail comparison.

## value

PASS

A controller chosen without knowing the deadline minimizes failure at every deadline, uniformly over arbitrary nonanticipative strategies. This is stronger than an expected-time improvement and resolves a natural risk-sensitive question for cycle cover. Explicit whole-cover fluctuations quantify the selected policy. This value survives attributing all exact one-stage moments to the prior fixed-target theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
