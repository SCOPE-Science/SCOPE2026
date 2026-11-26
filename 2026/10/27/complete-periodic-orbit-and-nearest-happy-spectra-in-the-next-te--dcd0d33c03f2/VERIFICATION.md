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

A positive base-(-p) integer has odd digit length. The least with 2k+1 digits is (p^(2k)+p)/(p+1), obtained by maximizing the negative-place digits under a leading 1. For k=2 this exceeds both the published descent threshold B_p and 5(p-1)^2 (the latter difference is (p-1)(p-2)(p-3)+1). Successive lower bounds increase by (p-1)p^(2k)>2(p-1)^2 for k>=2, so all integers of at least five digits descend, independently of the cited descent theorem. At most three slots give the closed positive core [1,3(p-1)^2]; B_p has digits (p-1,p-1,p-1) and attains its upper bound after one step. Independent replay in /workspace/branches/audit_negative_core.py uses ordinary-radix expansion after translating the signed digit interval and complementing odd-place digits, and iterates the image of the whole core to stabilization (exactly the cyclic vertices in a finite functional graph). All directed cycles, witness bounds and twenty nearest-happy entries agree. Checking 2 through p^2 and -2 through -p suffices since both endpoints map to 1; successive iterates either hit 1 or repeat. The same independent replay includes p=2 through 10, directly confirming the first primitive period 17 is at -18 in increasing absolute value, unique there. Negative inputs are not periodic because the first image is nonnegative; 0 is outside the asserted positive census.

## originality

PASS

The negative-base map, descent theorem, finite-search method and the published earlier census are not novel. The evidence supports distinct exact data for the next ten bases and the earliest absolute base for period 17, not priority for the method or all-base theory.

## value

PASS

The object and the four recorded invariants are the same as in a published complete census. A contiguous continuation matters because it establishes a sharp first-base threshold, not merely a period-17 example. The full directed witness sets provide an exact baseline for questions about feasible periods, and the -19 nearest negative happy value -17 illustrates why one cannot just report the universal happy endpoint -p. No general result about larger bases or arbitrary periods is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
