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

The proof concerns strictly positive external assets t*a with fixed liabilities normalized to one, outside obligations positive in each row, and marginal total gross payments at each fixed t. The capped clearing map is an order-preserving l1 contraction because max row sum of T is below one, so the solution is unique, continuous in inputs, and nondecreasing in t and injections. On each strict default-set interval the local gain equals the relevant coordinate of (I-T_DD)^(-1)1 and is zero off D. This follows by differentiating the affine restricted clearing system, with fully solvent payments unchanged by a sufficiently small nonnegative injection. For one or two banks the default sets are nested: there is at most a constant all-default ranking, then one remaining potential winner, then no strict winner. Ties and simultaneous exits do not allow strict reentry. In the witness the all-default branch first reaches p_3=1 at 42/95; with bank 3 fully paying, the two-bank default branch reaches p_2=1 at 126/61; with only bank 1 defaulting the payment is 7/10+t/20 until t=6. Endpoint inequalities and affine continuation verify the fixed-point conditions throughout the open intervals, using uniqueness. The exact gain comparisons are (416,374,342)/105, (55,70,0)/48 and (1,0,0), hence winners 1,2,1. Above t=6 all gains are zero; no strict winner is asserted at the breakpoints. The independent rational replay /workspace/branches/84a4b2c9-7df5-47cb-a03c-ad6b9877123c/rational_replay.py also checked the affine segments, switch identities, and injections of 1/1000 in each coordinate at t=1/4,1,3. The supplied verify.py was inspected, not executed; finite evidence checks the witness, not the universal lower bound.

## originality

PASS

Credit the known pro-rata clearing model and fixed-default-set sensitivity, including small-injection targeting. The supported claim is the exact minimal bank count for strict priority reentry as all baseline assets scale proportionally while the marginal intervention is infinitesimal at every comparison point. The inspected fixed-baseline finite-budget formulation and the closest catalogue contagion result do not cover this sharply quantified assertion. Demange's identified close comparison remains an access limitation, not evidence of non-coverage or grounds for scientific failure.

## value

PASS

The theorem supplies a meaningful smallest-dimension counterexample to monotone targeting along a natural one-parameter asset improvement. An exact fully connected witness together with a universal smaller-network obstruction makes the effect structural rather than a numerical anomaly. Its value is limited to the gross-payment marginal objective and stated clearing model; it is not a claim about welfare or finite-budget policy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
