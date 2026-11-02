---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Replay

Run `python3 verify_blocking_quartics.py` using Python 3 with no nonstandard packages. The last output must include `COMPLETE_BINARY_QUARTIC_BLOCKING_CENSUS_PASS`. The script asserts all ten bins, seven rational points and lines, \(168\) projective transformations, \(279\) form orbits, \(10,920\) geometrically smooth forms, \(78\) smooth orbits, \(3,888\) blocking forms, \(25\) blocking orbits, and exact reduced fraction \(162/455\).

## Exactness and limitations

Smoothness is tested over an algebraic closure by exact polynomial ideals and three projective charts, not by rational point sampling. All coefficient vectors are covered with exact group orbit enumeration. The code can be inspected independently, but no independent audit has been performed. An additional alternative Gröbner computation corroborated the figures, but is not needed to replay the supplied finite certificate. The claim is confined to degree-four forms over \(\mathbb F_2\).
