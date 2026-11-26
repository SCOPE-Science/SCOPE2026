---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Extraction from qB_m gives H_0=q/(1−q). If f_r(n)=[q^n]H_r, the recurrence is f_(r+1)(n)=Σ_(k=1)^(mn) f_r(k), n≥1. Independent expansion in the monomial basis gives f_3(n)=m^6 n^3/6+(m^5+m^4)n^2/4+(m^4+3m^3)n/12. Thus with s=mn the fourth coefficient polynomial is [m^6 s^2(s+1)^2+(m^5+m^4)s(s+1)(2s+1)+(m^4+3m^3)s(s+1)]/24. Converting to rising binomials yields the four frozen coefficients. For p≥5 only the linear-in-n term survives after division by p^4 and reduction modulo p; it is n/8. Convolution with B_p gives the stated normalized digit, nonzero at n=1. At m=3 the four h_j coefficients are −729,21627,−74358,59049, yielding the stated ternary numerator; the first two partition numbers normalize to 23 and 275, which are coprime. For every p, B_p is an integral formal unit with constant term one; the first four coefficient vectors of h_1 through h_4 form a unimodular matrix (determinant one). Content is therefore the gcd of the four h_j coefficients, and the last one p^10 rules out all other prime factors.

## originality

PASS

Credit the universal p^4 divisibility and extraction formalism to earlier work. At p≥5 the universal bound and the indexed all-ones residue at n=1 together already determine the exact p-part of the gcd; that archive record is catalogued later, which does not settle priority. The distinct supported contributions are the exact ternary progression factor and series, and the full all-n normalized residue for primes p≥5, with their explicit fourth-extraction calculation. The strongest inspected matches do not give these contributions.

## value

PASS

Depth five is motivated by the exceptional arithmetic at the denominator 24, not just a numerical slice. The precise ternary gain and exact entire progression series explain where the usual power fails to be sharp, while the larger-prime law answers which progression members have an additional factor. These are useful refinements beyond isolated leading units or rechecking the ordinary bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
