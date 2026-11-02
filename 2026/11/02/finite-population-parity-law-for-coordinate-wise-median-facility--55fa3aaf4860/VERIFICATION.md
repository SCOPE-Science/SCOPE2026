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

The proof of the real-domain theorem is given in `RESULT.md`. The independent computational identity \(\max\{|s|,|t|\}=(|s+t|+|s-t|)/2\) reduces the comparison optimum to two scalar medians in rotated coordinates. `verify.py` directly evaluates this optimum using exact rational numbers and compares it with the lower-tie-broken coordinate-wise median. It exhausts 92,368 unordered profiles with \(2\le n\le10\) on \(\{-1,0,1\}^2\), validates sharp profiles, checks 7,500 seeded variable-size integer samples, and exercises the one-agent dual certificate on 38,808 rational instances. Invoke `python verify.py` in the same directory.

The finite verification is a regression check and is not itself a proof for arbitrary real coordinates or arbitrarily large population. The displayed four-case analytic inequality and its summed certificate provide that proof. Source novelty has not been independently audited.
