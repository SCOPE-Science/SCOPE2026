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

The supplied `verify.py` is standalone Python 3, requires no nonstandard packages and independently enumerates uniformly random bond orderings for sizes \(2\) through \(9\). The code computes \(a_n\) and \(b_n\) as exact rational numbers to size \(79\), compares the closed formulas for \(a_n\) and \(b_n\), and verifies covariance signs for all these finite cases. It checks a finite list of implications but is not a substitute for the analytic proof for every \(n\).

Critical paper premises: a uniform earliest bond and conditional independence of the two remaining subpaths are exact consequences of the random-priority construction. The positivity of the joint-moment remainder follows from \(e^{-u}>1-u\) at positive \(u\); the factorial equivalent follows from an explicit beta integral. No interval-length truncation is used in the proof.

Historical-priority limitations: the relevant Gerin paper was examined in its accessible full text; an earlier general adsorption multisite-correlation paper was only accessible at bibliographic/abstract level. Therefore the originality conclusion remains provisional and independent historical verification is appropriate. Independent audit status: not performed.
