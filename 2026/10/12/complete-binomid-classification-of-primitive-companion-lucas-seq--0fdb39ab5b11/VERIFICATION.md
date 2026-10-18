---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For coprime P,Q, V2/V1=P−2Q/P integral forces P|2 and hence |P|∈{1,2}. For P=1, V2=1−2Q coprime to V3 and Q; the [4,2] integer coefficient forces V2|2 and odd V2, so Q=0 or 1. For P=2 with Q odd, Wn=Vn/2 has W2=2−Q coprime to W3, and [4,2] forces W2|4; its oddness leaves Q=1,3. At (2,3), the exact [6,3] quotient is −161/5, excluding Q=3. Remaining Q=0,1 and Q=1 with P=2 have nonzero constant or six-periodic terms; every k-consecutive-index interval contains at least floor(k/3) multiples of three, proving all generalized coefficients integral. The same absolute-value pattern proves m|n => Vm|Vn. Sign P↦−P only changes signs. Independent arithmetic checked admissible pairs n<=30 and all short-slot exclusions in a coprime parameter box; symbolic proof is unrestricted.

## originality

PASS

Shapiro explicitly raises the general order-two binomid classification for recurrences with nonzero initial value while proving positive results primarily for zero-initial Lucas U sequences and known divisible cases. The present V0=2 coprime-parameter iff theorem gives an original necessary binomid-to-divisibility implication for that natural companion family, not merely periodic examples. Granville treats classification of divisibility recurrences, not the converse binomid necessity for primitive V; equivalent earlier special-family formulations remain possible.

## value

PASS

The primitive companion Lucas family is a canonical infinite two-parameter branch of a published explicit open question, with a sharp iff parameter list and a positive answer to binomid=>divisible within the family. Necessity of three coefficient constraints plus unrestricted periodic sufficiency is a genuine classification rather than merely naming a textbook identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
