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

# Reproducible checks

Run `python3 verify.py` with Python 3 and no external packages. The program computes the polynomial from a matching/private-state recursion using exact integers and enumerates every possible graph on six labeled base vertices (15 potential edges, 32,768 edge masks). Its quadratic/cubic discriminants are all nonnegative. The degree histogram is \((1,191,7753,24823)\) for degrees \(0,1,2,3\); exactly 160 cases have discriminant zero, which is compatible with multiple real roots. Adding isolated base vertices only multiplies the normalized polynomial by \(3\), giving the cutoff for every base order below six.

A second procedure directly enumerates matchings of the *full triangle corona*, checks maximality by testing whether every edge touches a matched vertex, and counts by matching size. This independent construction verifies the seven-vertex subdivided-star base and all 64 four-vertex labeled bases, besides smaller examples. For \(r=3\) it obtains normalized coefficients \([1240,1068,210,12]\) and exact cubic discriminant \(-13023936\). A further finite comparison verifies the symbolic formula for \(1\le r\le8\).

Expected last line: `VERIFY_OK`. The finite enumeration addresses only the precise bounded claim; the all-arm root count is established analytically in the proof, and no external or independent mathematical certification is asserted.
