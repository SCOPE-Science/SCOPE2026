---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Writing the fractional-remainder numerators as y,y,x with x congruent to -2y modulo P splits the unique Hamilton allocations into two strict regions: the small state receives the unique surplus seat for 0<y<P/3, while the two equal large states uniquely receive the two surplus seats for 2P/3<y<P. Since a=(P-c)/2, advancing one house sends y to y+a without wrap in the first region; the transition crosses to the second region exactly when y>(P+3c)/6. That inequality also keeps the small state's lower quota fixed, so it loses one seat. The integer count of residues in the open interval is the displayed ceil/floor formula. A fresh independent exact Hamilton replay over 127 primitive pairs with a<=20 matched the theorem, including (3,3,1), (7,7,2), and (9,9,1).

## originality

PASS

Janson and Linusson explicitly leave extension of their probability formula to all population vectors, particularly rational ones, open and note periodicity in the rational case. Their paper includes the anchor vector (3/7,3/7,1/7), where the small state loses on the 3-to-4 transition modulo 7, but does not give the all-(a,a,c) residue interval or exact count. Resultary found no equivalent equal-pair formula.

## value

PASS

This gives an exact infinite-family solution inside a rational regime explicitly singled out as delicate because seat changes are periodic and ties matter. The tie-independent formulation isolates convention-free losses and yields both their exact residues and frequency.

The dated certificate retains the supplied scientific assessment, sources and limitations.
