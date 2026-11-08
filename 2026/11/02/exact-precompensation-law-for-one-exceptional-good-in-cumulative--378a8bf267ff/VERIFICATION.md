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

For two agents with identical positive additive values in fixed order 1^a,H,1^b (H≥1 real), cumulative maximum envy after each prefix equals absolute signed bundle gap. For prescribed prefix endpoint −j, j≡a mod2, |j|≤a, the telescoping inequality |z_t|≥(1+z_t²−z_(t−1)²)/2 is sharp via alternation followed by a monotone ramp, giving prefix cost (a+j²)/2. After H, successive minimum absolute distances to the reachable parity lattice δ_t(|H−j|) are simultaneously attainable by moving toward zero and oscillating; minimization over j yields the unrestricted finite formula. For integer m with a,b≥m, the monotone suffix cost reduces j to [0,m], then completes the square to midpoint precompensation. For a=b=m=2h, explicit E*=2h+2ceil(h²/2) and E_greedy=2h+2h² give limit ratio two. Independent rational signed-walk DP matched the closed formula in 343 cases and 150 midpoint checks; finite evidence supports but does not replace the proof.

## originality

PASS

Goldberg–Robinson–Teh 2026 introduces precisely cumulative envy and supplies general dynamic programming and approximation, including special restrictions; its accessible complete arXiv HTML has been inspected for the fixed order problem and adjacent one-exceptional examples. The displayed general fixed-order real-H closed formula, integer midpoint law and explicit myopic gap were not identified in compared primary statements. A release-order optimization theorem cannot imply the optimum for a prescribed fixed order. The possibility of equivalent unindexed signed-walk scheduling identities or supplementary formulas is a residual originality risk, not ground to reject the mathematical result.

## value

PASS

An exact constructive optimizer for the first natural departure from equal-valued arrival sequences and a sharp quantified near-factor-two failure of myopic balancing isolate a genuine mechanism: creating deliberate early envy reduces later cumulative envy. This precise result could be used when scheduling irrevocable two-party resource allocations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
