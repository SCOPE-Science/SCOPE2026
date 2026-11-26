---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Re-audited the repaired statement. Factoring the cyclic resolvent and shifting its diagonal give the positivity criterion t*≤θ+(1−θ)P. The repaired telescoping identity for (1−P)/(1−t*) has a strictly increasing positive product in each summand and a nondecreasing ratio (1+srmax)/(1+sr_j). Its limits are 1 and rmax·Σ_j(1/r_j); hence the reciprocal gives the strictly decreasing limiting return diagonal used for the closed cutoff. For same-sum majorized rates, strict concavity of log(sx/(1+sx)) lowers P for nonpermutations while the maximum rate cannot decrease. At the finite positive crossing for the more balanced vector, the less balanced vector violates admissibility strictly. Permutations and an infinite horizon of the more balanced vector give the stated weak cases. In the new same-maximum example, the common fastest-rate product factor cancels: 3(1+2s)²<4(1+3s)(1+s) at every s>0; both horizons at θ=1/2 are finite because π_min≤1/3. Under a fixed budget, uniformity uniquely minimizes rmax for θ=0, wins strictly in the finite regime, and is the only vector with π_min=1/n at the transition. Above it continuity supplies infinitely many nonuniform optima; at θ=1 every horizon is infinite. The monotone change of variables ensures the correct unique interior uniform root, not the endpoint t=1.

## originality

PASS

Pass applies only to the repaired strict fixed-sum majorization comparison and its design consequences. The strongest same-object comparator directly covers the cutoff formula, and the broader Markov result covers the interval and stationary-mass transition; these are credited background, not new claims. None of the inspected statements compares all same-sum majorized heterogeneous directed-cycle rate vectors. The strict comparison uses the separate observation that the product factor is strictly Schur-concave while the maximum-rate factor moves in the opposite direction in the inequality; even equal-max vectors can be ordered. The uniform-budget uniqueness classification is its corollary in the finite regime and uses known stationary masses in the infinite regimes. It is not credited as a separate discovery of the stationary threshold.

## value

PASS

This is a fixed-budget design result for a natural numerical positivity constraint. It orders whole comparable rate profiles, including profiles with the same maximum rate, for which a fastest-rate-only bound misses the distinction. It identifies the unique allocation through the finite-to-infinite transition and shows exactly where uniformity loses uniqueness. This comparative consequence is useful independently of rederiving the known cyclic horizon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
