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

The defining recurrences give child triples from (a,b,c)=(s(k),s(2k),s(2k+1)): (b,2b-a,2b+c) and (c,2c+b,2c-a). Under (m,d,e)=(a,b-a,c-a) they yield the frozen pair of child maps, preserve de=m^2+1, and start at (0,1,1). This proves the needed indexing without assuming the external tree interpretation. Summing the three quadratic observables over children and reducing de=m^2+1 independently recovers the exact four-state matrix and root state. A Cramer determinant for the third formal resolvent coordinate gives the stated numerator and denominator; the roots of the recurrence and the first four moments determine the claimed explicit formula. For the first moment, the child-pair aggregate of (d+e,m) is (3(d+e)+4m,(d+e)+2m), with trace 5, determinant 2 and m-sums 0,2 at n=0,1, giving the stated R_n. For n>=1 the squared CV is 2^n P_n/R_n^2-1. The positive leading coefficients yield the asymptotic constant 17K/4, and 2 lambda_+-alpha_+^2=1/2+sqrt(113)-(5/2)sqrt(17)>0, so subtracting 1 is asymptotically negligible. Independently evaluated all sequence values through level 12 by bottom-up scalar recurrence and matched each square sum against the symbolic transfer. The numeric bases 1.03952283129313 and 1.01956992467 agree; finiteness of this replay is not used to extend the theorem.

## originality

PASS

Sequence/tree identification, first moments and general regular-sequence spectral methods are antecedents, not credited as new. The inspected results leave a distinct explicit quadratic-row formula and strict dispersion exponent for this sequence.

## value

PASS

Dyadic levels are inherent in this published divisor-pair tree, and its mean and maximum already motivated studying fluctuations within a level. The exact second moment gives a quantitative distinction from the mean: variability relative to the mean grows exponentially, with an explicit small but strictly positive exponent. The result is useful for tests or comparisons of concentration claims for the tree and is stronger than first-order growth or recomputing a short row table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
