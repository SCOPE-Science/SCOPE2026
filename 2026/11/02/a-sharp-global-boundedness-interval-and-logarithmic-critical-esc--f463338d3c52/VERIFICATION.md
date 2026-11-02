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

The exact map and coordinate reduction can be checked by substituting \(x=s+d\) and \(y=s-d\) into the two source equations. The derivative identity \(f_a'(t)=a e^{-t^2}(1-5t^2+2t^4)\) establishes finite boundedness and vanishing tail derivative; the sign of \(1-t^2\) controls both exceptional endpoints. For any critical escaping orbit, the mean coordinate decays geometrically, yielding \(d_ns_n\to0\) and hence the scalar Gaussian increment. The clock \(H(r)=e^r/(2ar^2)\) has increments tending to one. These steps are analytical and cover infinitely many iterates.

Run `python3 verify.py` with the standard Python library. The script directly compares the original map with its coordinate form in 84 cases, checks 60 bounded interior trials, tests 12,000 iterates inside a proved invariant endpoint rectangle, checks 480 finite geometric-escape inequalities and compares critical reciprocal-clock ratios at two long observation lengths for three gains. Its output records numerical ratios below one and increasing toward the analytical limit; it does not claim to establish that limit computationally.

The numerical tests use ordinary double precision, so they cannot detect arbitrarily slow motion at very large critical amplitudes. Symbolic proof supplies the all-parameter statements. Literature priority remains conditional on the inspected sources; no external independent validation is asserted.
