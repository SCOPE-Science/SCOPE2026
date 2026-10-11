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

# Verification

Run `python3 check_neutral_return.py` with Python 3 standard library. Output on the present package:

`FINITE_DIAGNOSTICS_PASS 309`

The tests comprise exact rational transitions and return counts at the rational angles corresponding to \(\tau=-1,0,1\), rational-arithmetic invariance of the pre-existing switching-tangent ellipse, 60 finite observations of the nonresonant \(\tau=1/2\) orbit, and 24 exact-return versus one-sided angular-hitting comparisons. The value 309 is the checker's own counter for all executed assertions, including further exact-cycle tests.

For analytical verification, inspect equation (1) in the proof and the first-return convention: a right-branch iterate with first coordinate nonpositive causes the following iterate to have second coordinate zero. The rational case follows because \(\cos(q\phi)=1\) and \(\sin(q\phi)=0\). In the irrational case, angular factorization yields precisely the two one-sided arcs. Continued-fraction convergents justify the upper bound; the badly-approximable lower bound and its contrapositive establish sharpness. The tail bound follows by integrating the inverse-distance estimates near \(x=1/2\), with uniform finite hitting away from that point.

Finite computations neither verify every irrational parameter nor prove infinite-time recurrence, so the full claims depend on the written analytic arguments and standard irrational-rotation theorems. Full-text access to Simpson (2025) was unavailable; that is a literature-priority limitation, not a proof certificate. Independent audit has not been performed.
