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

In the independent exponential realization of first arrivals, the minimum arrival time of a suffix is independent of its entire rank order: the minimum is independent of the winner, and the residual race conditional on the winner is independent of the minimum time. Thus the event that clock i beats the minimum over j>i is independent of the later suffix record-value events. This proves the Bernoulli-sum law with the stated hazards; the certain top letter contributes one, exactly canceling removal of the initial record. The coupling agrees once letter d appears, giving the TV bound. Independent exact weighted-word enumeration gives (1182,494,52)/12^3 and (2596,1309,186,5)/8^4, with discriminants −455/746496 and −61127/274877906944. These are not Poisson–binomial; the signs persist in open subsets of the positive simplex. Horizons at most two have at most one new record. The distinct hazards in both examples give simple negative limiting PGF roots. Coefficient convergence implies sign changes at the ends of disjoint negative intervals around all d−1 roots for every sufficiently large n; the degree bound and normalization at one then give the Bernoulli factors. This argument does not cover repeated limiting roots. The uploaded verifier was inspected, not run.

## originality

PASS

Credit the infinite-record law and PGF criterion to known work and treat generic recovery as a short consequence of known independence plus the top-letter coupling and root stability. The supported distinct finding is the earliest-horizon strict record-count obstruction, its four-draw counterpart, and the precise contrast with eventual recovery for the same laws. The closest indexed three-draw result concerns occupancy, not records.

## value

PASS

The two small witnesses answer a natural finite analogue of independent eventual record-value indicators. Failure already at the first horizon where it can occur, stability of the counterexamples in the probability simplex, and exact eventual recovery of the same laws explain why a limiting independence claim cannot be read as a fixed-time one. The contribution does not require a time bound or a classification at repeated hazards.

The dated certificate retains the supplied scientific assessment, sources and limitations.
