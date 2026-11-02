---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For C3(n)=binom(3n,n)/(2n+1), Legendre/Kummer yields v2=2s2(n)-s2(3n). The four previous-bit/incoming-carry states with final carry weight are exactly enumerated by T(u) and terminal (1,1,1,u); symbolic inverse verifies GF (1+z)(1-uz)/[1-(1+u)z-(1-u+u²)z²+(u+u²)z³]. Forbidden adjacent 1 bits yield zero-valuation Fibonacci F_(L+2); maximal carry paths give max L multiplicity F_(L-1). Differentiation gives mean L/2-2/3+(3+(-1)^L)/(6*2^L). Dominant transfer eigenvalue 2 has derivatives 1 and 4/3, giving variance 11L/12+O(1) and CLT via analytic spectral gap. I independently compared exact spectra up to L=11 and symbolically inverted T; this finite corroboration is not the CLT proof.

## originality

PASS

Kummer gives the individual valuations and general automata/CLTs give machinery; Aval supplies the combinatorial sequence. The fully explicit rational dyadic-histogram generating function, sharp extremal Fibonacci count, and 11/12 variance were not stated in inspected comparators, including Kauers–Krattenthaler–Müller which studies order six and 2-power orders rather than the prime-two valuation spectrum of order three.

## value

PASS

A complete explicit two-variable dyadic valuation spectrum, including sharp Fibonacci extremal multiplicities and a nonstandard Gaussian variance constant, is a useful arithmetic statistic of the natural ternary-tree counting sequence. General carry automata give a method but do not provide these exact coefficients for this specific object; the theorem is substantive exact enumeration plus asymptotics, not renaming an isolated identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
