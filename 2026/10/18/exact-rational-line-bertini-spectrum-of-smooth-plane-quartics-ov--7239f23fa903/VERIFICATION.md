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

# Verification details

The exact finite exhaustion and binary linear algebra were executed from `verify_quartic_spectrum.py` and reproduced the \(10920\) smooth curves, all eight transverse-line counts, all twenty nonzero joint \((n,t)\) counts, the \(78\) projective orbits, and the \(1+24\) transverse-free orbit decomposition. The secondary `verify_groebner.py` program executed successfully with SymPy and returned unit ideals on three affine charts for each of the \(78\) smooth representatives.

The main algebraic lemma establishes that rank \(66\) in degree ten is equivalent to geometric smoothness: the potential singular point may lie over any extension, not merely a tested finite extension. The line-restriction derivative identity likewise concerns distinct geometric intersection points. There is no assertion that finite sampling would prove an infinite statement.

To reproduce without additional packages use `python3 verify_quartic_spectrum.py`. For independent chart-based verification install SymPy and run `python3 verify_groebner.py` from the same directory.

This is a computationally exhaustive proof with explicit algebraic completeness arguments, not an independently audited certificate. Older historical publications were not comprehensively inspected; see the literature discussion for the originality limitation.
