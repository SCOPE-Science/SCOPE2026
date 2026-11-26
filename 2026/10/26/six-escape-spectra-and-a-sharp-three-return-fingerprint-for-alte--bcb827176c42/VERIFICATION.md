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

Use the 2-bit overlapping states and delete one transition in each phase. A time-two edge has a unique intermediate state determined by its endpoints; closed length-j paths count exactly the phase-labelled 2j-periodic strings including repeats. Thus the trace determinant formula gives the symbolic zeta function. Survivor cylinder counts come from summing entries of the alternating products and multiplying by 2^(-n-2). For even n these sums are comparable to an induced norm of P^(n/2); for odd n the terminal vector M_u1 has entries in [1,2], preserving the same growth exponent. The finite-state entropy and escape formulas follow. The unpunctured matrix has rank 2, hence each deleted-edge matrix and P have rank ≤3, so the first three traces determine the full determinant by Newton identities. Independent exact reproduction checked all 64 ordered pairs (including the static pairs) and 192 cyclic word counts: class sizes 8,16,12,8,16,4, the stated six cubic denominators and all triples agree. Rational disjoint brackets and monotonicity of each cubic from 5/2 establish strict Perron ordering; the end cubics give the squares of the golden and tribonacci constants. 000:000 and 000:001 both give (3,11) but have third returns 39 and 33, proving sharpness. Replay: branches/9444d01f-7582-4398-904b-46ef7365b438/reproduce_census.py. This finite run checks the classification, not the all-time identities by itself. The zeta calculation does not claim interval endpoint periodic counts. Frozen checker and verification notes inspected, not rerun; audit/attestation/Lean were not performed in the frozen record.

## originality

PASS

The inspected primary literature supplies return/transfer methods and static or continuous moving-hole results, and one later indexed result gives the same class-C cubic for a single schedule. None of those statements or implications gives this complete equal-depth, period-two spectrum, or the optimal fingerprint within it. Credit is for that finite classification and sharpness, not the determinant method or the individual static spectra.

## value

PASS

This is a complete exact classification of a natural first moving-hole family where hole sizes and depths are held fixed and only the schedule varies. The six different rates exhibit real schedule effects, and the sharp finite return test and static/alternating spectral coincidences show exactly what short periodic data can and cannot recover. The value does not hinge on generalizing beyond this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
