---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For n=d−1, the derivative Laurent power spectrum is supported on [−n,n], a complete set of distinct residues modulo 2d−1. Its nth coefficient is q_n times the conjugate of q_0, so a competitor must have both derivative endpoint coefficients nonzero. Multiplying the common Laurent polynomial by z^n gives the product of a spectral factor and its reversed conjugate; on the admissible locus the 2n roots are distinct reciprocal-conjugate pairs. Every competitor thus chooses exactly one root from each pair. The leading-modulus change for a flip is the product of the flipped root moduli; the constant-modulus ratio is its inverse. The real polynomial equations saying a nonempty subset has modulus product one are proper in ordered root coordinates and give null sets in coefficient charts. At d=3 the nearest alias of frequency 1 is −4, outside [−3,3], and the separation only increases with d; the zeroth moment is also unaliased. After fixing the competitor phase, equality of the first moment solves for the competitor constant as αx+β. For a wrong flip |α| differs from one, so the energy equation is an actual circle equation (possibly empty or a point). For no flip the first moment forces the same constant. Locally continuous root labelings give measurable exceptional sets, and Fubini makes their planar-null sections jointly null. The argument includes nongeneric competitors, assumes indexed grid data, and does not extend the nonaliasing argument to d=2.

## originality

PASS

The supported distinct claim is almost-everywhere uniqueness for the prescribed smaller grid with only three real value-intensity statistics, and the accompanying finite circle cover of exceptional constants for each admissible derivative. This is not a minimum-sampling or universal uniqueness claim. No inspected source is shown to supply it.

## value

PASS

A deterministic paired sampling design answers a concrete part of the published generic-uniqueness question, using fewer sites than the known universal bound and retaining only three real statistics of the value measurements. The circle description identifies where the reduced design can fail and is useful independently of the a.e. conclusion. Neither optimal sampling nor robustness to noise is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
