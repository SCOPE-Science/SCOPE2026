---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For the precise independent p-tremble model, each of two other ballots independently remains fixed with probability 1-p or goes to either other candidate with probability p/2. Independently enumerating all nine terminal opponent profiles with exact rational polynomial weights gives, for top-minus-middle actions at truthful (A,B,C), constant (1-2rho_i)/3; at unanimous (A,A,A), zero constant and linear coefficients (5-4rho1)/3 for voter 1 and (4-5rho_i)/3 for voters 2,3. Signs are strict on 0<rho1<1/2, 1/2<rho2,rho3<4/5. Worst ballot is strictly dominated for any p>0 by favorite, since each pivotal opponent tally has positive probability; thus only the compared actions matter. These are exact leading coefficients, so a common sufficiently small p exists per parameter triple, proving the 2-cycle of full ballots and distinct polls. For one or two voters and any m, conditioning on the other voter gives strict favorite dominance; for any N and two candidates, favorite weakly dominates pointwise and is strictly better on a positive-probability pivotal tally. Those arguments prove simultaneous minimality, not merely numerics. Independent checker confirms the six polynomial profiles at rho=(1/4,3/4,3/4). No assertion for a fixed tremble p uniformly over the full open parameter box.

## originality

PASS

The new object is an exact truthfully initiated two-cycle in the specific synchronous independent-tremble update with strictly changing public vote counts and simultaneous sharp dimensions. Prior finite examples of cycles, static trembling equilibria, and a different top-bottom response do not imply that conjunction; publication priority remains qualified.

## value

PASS

A sharp smallest-voter/candidate witness for a publicly observable changing-poll instability is a motivated boundary for the studied iterative voting rule, not just another already-known ballot cycle. Its open strict cardinal-utility region gives robustness and the proof establishes the two independent necessary dimensions. The exact phenomenon could be useful in stability and convergence modeling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
