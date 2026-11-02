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

# Verification of constant-power involution counts

Run `python checker.py` with Python 3 and no third-party libraries. The program directly enumerates all operation tables on sets of sizes one, two, and three, computes the associated transformations on ordered pairs, and tests consecutive powers until an image collapses to one point. It reports successful/total counts \(1/1\), \(4/16\), and \(2187/19683\), respectively.

Separately, the program generates all commuting transformations for each \((f,m)\) with \(1\le f\le3\) and \(0\le m\le2\). It checks the commuting equation for every generated function and directly tests powers. For example, the complete counts are \(9/27\) for \((f,m)=(3,0)\), and \(189/1323\) for \((3,2)\). The checker computes all cases directly. It also enumerates weighted rooted forests for \(1\le f\le4\) and \(1\le m\le5\), checking the Prüfer closed form without invoking that formula during enumeration. Successful execution ends in `VERIFY_OK`.

The full-dimensional statements are proved in `RESULT.md`. The tests do not establish them by induction or by exhaustive coverage beyond the printed sizes. The checker does not certify historical novelty or supply independent validation.
