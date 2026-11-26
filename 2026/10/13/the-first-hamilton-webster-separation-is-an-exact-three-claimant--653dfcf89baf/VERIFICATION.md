---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For one seat and more than one claimant all lower quotas are zero, so the Hamilton remainder winners are the maximum claimants, just as for Webster's first priorities (and one claimant is trivial). For two claimants the first exact quota is x=ha/(a+b). Under Hamilton the first allocation t ranges over all nearest integers to x. Under Webster a common positive reciprocal divisor lies in the intersection of [(t−1/2)/a,(t+1/2)/a] and [(h−t−1/2)/b,(h−t+1/2)/b]. For 0≤t≤h the upper endpoints are positive; the two cross-inequalities are exactly |t−x|≤1/2, preserving ties even for a zero allocation. For 0<p<q<r and two seats, Webster's second priority compares q to r/3. Under Hamilton, p and q have quotas below one. If the largest quota 2r/S (S=p+q+r) is below one, the two largest shares both get one. Otherwise the largest claimant has lower quota one and its remainder 2r/S−1 competes with 2q/S; equality is r=p+3q, necessarily in the one-lower-quota regime. This proves the strict cone and both stated ties. The weak-order cases omitted from the frozen symbolic minimum argument follow directly: if q=r, both methods give one seat to each top claimant or, if all claims are equal, have the same tied splits. If p=q<r, the unique largest claimant gets a seat under each method; any allocation of the other seat to a smaller claimant is tied by exchange of the equal claims. Thus no strict unique-outcome disagreement can have equal claims. In the strict integer cone p≥2 (p=1 gives an empty open integer interval), q≥p+1 and r≥3q+1. Total is at least p+4q+1≥15, with equality only at the primitive (2,3,10). The frozen verifier's minimum search starts at total 6 rather than the least weak-order total 3, so it does not by itself cover that edge case. I did not execute it. An independent bounded arithmetic check enumerated all six two-seat allocations for each of the 86 primitive weak-order triples of totals 3–15, ranking by integer-scaled remainders among lower-quota lifts for Hamilton and comparing every last awarded priority with each next unawarded priority by cross-products for Webster. Only (2,3,10) had distinct unique outcomes. The symbolic argument, not this finite check, establishes the positive-real correspondence statements.

## originality

PASS

Credit is limited to the exact first two-seat separation of the two rules: its open chamber, the exact boundary correspondences and the minimum primitive integer witness. The rules and the two-claimant reduction are background. The closest inspected literature concerns general properties and historical apportionments, and the closest indexed results concern distinct quota and paradox thresholds. No material compared establishes the claimed geometry or primitive minimum.

## value

PASS

The dimensions are determined by the two lower-dimensional coincidences, so this is not an arbitrary tiny case. The result identifies whether disagreement is robust to perturbations, which method switches at each tie, and the least integer profile demonstrating this without tie-breaking or a Webster quota violation. This provides a sharp comparator and an exact regression case for two canonical allocation rules, independent of a general classification at larger sizes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
