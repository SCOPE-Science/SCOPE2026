---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Pinned RESULT.md f8d4008423f15f99c7b1da9f8c7c78fafbf0fe2d develops rational Maclaurin R(z)=1+z+z^2/2+0 z^3-z^4/4+O(z^5), so at distance exactly four the first nonzero L-power is A^4 and coefficient negative. Every graph Cn n>=8 has such pair and all finite connected graphs tend to a positive stationary rank-one projection as h->infinity. For n=3..7, given exact circulant inverse entries have common positive denominator and coefficientwise nonnegative numerators; independent SymPy direct matrix inversion/multiplication confirms all small-cycle identities and positive coefficients. On C8 exact t8,4 numerator is h^4(4h^4+22h^3+17h^2-1), all other numerator factors strictly positive, pprime>0 for h>0. Independent symbolic inverse identity and root h8=0.2137579658446203 verify exact threshold. Finite certificate for small cycles is exhaustive within n<=8; not a proof of a single threshold for all n>8.

## originality

PASS

Prior work establishes general [0/2] Padé eventual positivity and diagonal [2/2] Padé nonpositivity; neither accessible statement determines the exact C8 polynomial boundary or the distance-four graph Laplacian coefficient. Same [0/2] Itkin-Kazbek full text remains unread and is a serious named priority risk, not exonerated by abstract.

## value

PASS

A sharp structural local-positivity obstruction tied to graph distance, a natural first-failing cycle size, and the exact global recovery cutoff for C8 offer precise boundaries for positivity-sensitive heat integrators; these are mathematical distinctions beyond generic stability and eventual positivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
