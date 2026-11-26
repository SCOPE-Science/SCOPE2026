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

At the start of each flight there is at least e^(−η) probability of reaching an absorber before another reversal; the number of reversals has a geometric tail, so there is no explosion and the mean exit time is finite. Conditioning on the first reversal gives flight integral equations on the two signs with the outgoing boundary data. Their continuation term has sup norm at most 1−e^(−η); a bounded absolutely continuous solution of the backward equations satisfies those equations by the integrating-factor formula and is therefore the actual mean even for L¹ rates. In dimensionless units D'=−1 and U'=2hD, where h(t)=(L/v)λ(Lt), D=(T_+−T_-)/2 and U=(T_++T_-)/2 are scaled by v/L. Imposing U(0)=D(0) and U(1)=−D(1) gives D(t)=(1/2+m)/(1+η)−t and the stated moment formula. With left mass a, the two first moments enter with strictly negative and positive coefficients, respectively. Moving both moments toward the source in their own half-intervals gives the lower bound (1/2+η min(s,1−s))/(1+η); maximizing using the outside endpoints gives [(1+η)^2/2−2(a−η/2)^2]/(1+η). Absolute continuity forbids both equalities for η>0. A source-adjacent strip of width ε has excess ηε/[2(1+η)] above the lower endpoint in the prescribed placement; two equal endpoint strips of width ε have deficit ηε/2 below the upper endpoint, in the normalized units. Continuity along convex combinations fills the open interval. For a symmetric rate m=η/2, so U starts and ends at 1/2 and is monotone up then down. The zero-budget case is ballistic. The frozen lattice checks are finite corroboration only.

## originality

PASS

Bulk backward equations, the constant-rate two-absorber mean, and scalar optimal-rate phenomena are covered. The supported distinction is the full sharp open range over arbitrary nonnegative integrable flip-rate profiles at fixed spatial mass, including concentration placements and the symmetry obstruction. None of the inspected passages or nearest catalogue hit establishes that result; unresolved texts are named below.

## value

PASS

The fixed spatial integral is a distinct and natural design constraint. The result identifies both the best and worst possible mean and shows why neither is realized by a finite-width profile, rather than comparing a few rates. It also explains precisely why an asymmetric rate layer can beat the ballistic mean off center while reflection-symmetric rates never can. This gives a meaningful sharp baseline for transport models without imposing pointwise rate caps; rate-capped designs and other observables are not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
