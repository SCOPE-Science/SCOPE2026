---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For size-n multiplicity vectors x,y, correcting up to n-3 deletions is equivalent to no common 3-submultiset, i.e. I(x,y)=sum_i min(x_i,y_i)<=2. Distinct words with any multiplicity >=3 (heavy) cannot be assigned the same heavy coordinate, so at most q heavy codewords. For any two vectors with all entries <=2 (light), I(x,y)>=sum_i(x_i+y_i-2)=2n-2q>=4 when n>=q+2, so at most one light; for n>=2q+1 light words do not exist. The q pure vectors n*e_i meet the bound, and when q+2<=n<=2q the added light vector with n-q twos and 2q-n ones has sum n and intersects each pure vector by at most 2. For n=q+1 the explicit odd/even-q two-light witness yields >=q+2, proving the lower threshold sharp. Equality q heavy words forces exactly one singleton high-multiplicity coordinate for each alphabet symbol. This is a genuine all-parameter proof; independent exact pairwise intersection checks of constructions and lower-boundary witnesses for q=2..9 support it.

## originality

PASS

The previous published Resultary result settles only q=3, and binary special cases are old. Kreindel, Barouch Essayag and Zabokritskiy, arXiv:2601.05636v2, Section 4.4 Proposition 12, establish a much weaker q+binom(q,2) upper bound for n>=q+2; the theorem in this package is a uniform sharp q+1/q formula and partial optimizer structure for every alphabet size. Prior Kovačević–Tan discrete simplex work covers the model and general metric bounds, not this exact stated all-q threshold.

## value

PASS

Survivor-length-three is a particularly natural high-deletion boundary for multiset coding. Its uniform two-phase optimum, sharp n threshold, and heavy-coordinate rigidity answer an exact extremal question for every q, not merely recomputing a known ternary case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
