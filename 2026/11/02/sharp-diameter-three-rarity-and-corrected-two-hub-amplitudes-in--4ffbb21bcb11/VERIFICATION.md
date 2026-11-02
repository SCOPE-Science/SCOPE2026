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
The included `checker.py` enumerates every labelled attachment-history state to \(n=8\) with exact rational weights. It independently reconstructs which vertices have degree greater than one and which became the second hub, and compares those probabilities with the separate exact two-hub recursion. It tests the star formula and uses a floating recursion to probe the first seven asymptotic amplitudes through \(n=5000\).

To reproduce, execute `python checker.py` with standard Python 3. No additional packages are needed. Expected conclusion: `exact checks and asymptotic probes: 29`; the value of \(n\Pr(\operatorname{diam}\le3)\) at \(n=5000\) is approximately \(5.006849\).

The asymptotic theorem relies on the explicit contraction and tightness arguments in RESULT.md, not on finite enumeration. The source comparison identifies a factor omitted between the 2017 exact two-hub recurrence and its continuum approximation. Independent validation was not performed.
