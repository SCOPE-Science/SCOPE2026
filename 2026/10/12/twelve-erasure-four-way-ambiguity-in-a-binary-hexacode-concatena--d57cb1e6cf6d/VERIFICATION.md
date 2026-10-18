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

The outer [6,3,4] MDS property gives 45 nonzero quaternary weight-4 words and 18 weight-6, hence binary 1+45z^8+18z^12. For a binary two-plane, 2|supp|=wt(a)+wt(b)+wt(a+b)>=24; minimum supports require three words of weight 8. Partition by overlap 4,3,2 of the two four-coordinate outer supports gives 15,180,45 plane profiles respectively, each a distinct 12-mask because any 3-space support has >=14. Incidence count 45*C(10,4)+18=9468 gives 8748 masks with one nonzero supported word and 9576 with none; 240 masks have 3 supported nonzero words and four completions. Independent full finite reconstruction corroborated all counts, not extrapolated to any other code.

## originality

PASS

Jin-Fu Example 6.5 constructs the concatenation and gives its [18,6,8] parameters and usual weight distribution. These do not imply the exact 12-erasure ambiguity histogram or 6-block support profiles without a further subcode-support incidence calculation. Related code-classification and generalized-weight work may determine d2 but not the full stated profile.

## value

PASS

An exact erasure-ambiguity distribution for a natural explicit locality-two code distinguishes patterns indistinguishable by ordinary minimum distance or weight enumerator, and the block profile matters to the prescribed repair grouping.

The dated certificate retains the supplied scientific assessment, sources and limitations.
