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
# Verification record

The analytical proof uses the exact vertex angles \((2k+1)\pi/n\), for \(k=0,\ldots,n-1\), after orienting one polygon side vertically. For a side point \((r,t)\), the farthest vertex minimizes the dot product with \((r,t)\). The odd case has the unique opposite vertex except at side endpoints; the even case has the nearest of the two opposite-side endpoints. These are exact all-\(n\) angular-ordering statements, not numerical conjectures.

The bounded companion `verify.py` checks the symbolic large-\(n\) expansions of the odd and even perimeter ratios through terms of order \(n^{-4}\), and the existing equilateral-triangle and square calibration constants. Independently of the choice made in the analytical proof, it computes the maximum over **every** polygon vertex for 51 points on a representative side for every \(3\le n\le121\), and again for orders \(201\) and \(301\). It checks the stated squared-distance profiles and exact stability defects. Running the actual packaged script produced `VERIFY_OK`, 401,880 vertex-distance comparisons, and a maximum absolute squared-distance discrepancy of \(1.3323\times10^{-15}\) for circumradius \(1\).

The numerical checks are finite diagnostic tests; the continuous-profile theorem is justified by the angle-ordering argument. The results do not establish any global perimeter extremal property among irregular polygons. Published general inequalities and the known triangle and square cases are acknowledged as prior results. Independent audit is not performed.
