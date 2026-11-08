---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For 0<γ,μ<1 and transmission b_i in (0,1], the discrete SEIS disease-free infected linearization is M(b)=[[1−γ,b],[γ,1−μ]], a strictly positive 2x2 matrix. Determinant of period-k monodromy equals ∏(ad−cb_i), permutation-invariant. Direct multiplication shows traces for k=1,2,3 symmetric in b_i; for k=4 trace=a⁴+d⁴+c(a²+ad+d²)∑b_i+c²(b1b3+b2b4). With fixed determinant the Perron root strictly increases with trace, so all 24 orderings of four distinct b values yield exactly 3 classes of 8, ordered by pairing of opposite seasons via rearrangement identities. Direct rational matrix recomputation verified formula for permutations and the specific within-range example γ=μ=1/2, L=1/20, H=1: alternating trace 1861/1600, grouped trace 15/16, common det81/25600 and characteristic polynomial at one −4095/25600 versus +1681/25600. These prove distinct invasion/extinction outcomes and minimal schedule sensitivity horizon four. Conclusions only about local disease-free linearization, not nonlinear epidemics.

## originality

PASS

Best-of-knowledge original all-permutation four-season 3-class ordering and sharp shortest horizon for the stated discrete SEIS monodromy. Bacaër 2009 gives general periodic growth/reproduction matrix methods and Cushing–Ackleh 2012 general periodic matrix thresholds, but not the polynomial opposite-season pairing law or this exact local invasion reversal. Cao–Zhou 2013 and Tanaka–Aihara 2013 address periodic epidemic thresholds and schedule variation but accessible material did not establish this exact 4-season classification; inaccessible portions remain risk, not automatic failure.

## value

PASS

Season sequencing rather than only seasonal average affects invasion, with a sharp first horizon, strict parameter-independent ordering, and an exact pair of schedules having opposite threshold verdicts. These are natural mechanistic consequences of a simple discrete exposed-infectious stage model, not a generic restatement of spectral radius monotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
