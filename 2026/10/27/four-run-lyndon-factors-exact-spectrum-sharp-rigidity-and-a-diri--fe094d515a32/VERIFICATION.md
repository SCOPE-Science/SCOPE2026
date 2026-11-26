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

A nonsingleton binary Lyndon factor starts with 0 and ends with 1, so the factors come from two rectangle families with their intersection subtracted, or from the four-run form 0^i1^b0^c1^j. Suffixes inside the initial zero run or starting with 1 are larger. The third-run suffix starting with all c zeros decides: i>c gives a Lyndon word, i<c rules it out, and i=c gives a Lyndon word exactly for j>b. With the two singleton letters this yields the entire spectrum. Writing Z=a+c and O=b+d, the deficit ZO−L is ad+cb+a min(b,d)−2 when a<c, c(b+2d)−2 when a>=c and d<=b, and (c−1)d+(2c+1)b−2 otherwise. The first is >=2; the other two are >=1 and give equality precisely in the allowed cases with b=c=1. Balancing Z,O gives the claimed sharp maximum, the optimizer parity count, and the n=4 boundary. Summing the rectangle, excess and tie terms as geometric series and putting them over (1−z)^6(1+z)^2 gives numerator z^4(3+6z−2z^2+2z^4). The uniform lattice simplex converges by Riemann sums to the uniform Dirichlet law; the remaining singleton and tie contribution is uniformly O(1/n) after n^2 scaling. For S=A+C the independent ratios U=A/S,V=B/(1−S) are uniform, independent of Beta(2,2) S. Independent bilinear integration on the four U,V rectangles and beta moments reproduced mean 9/80, second moment 1/64 and variance 19/6400. The pole at 1 of order 6 with leading Laurent coefficient 9/4, and the lower-order pole at −1, give expectation (9/80)n^2+O(n) after dividing series coefficients by binom(n−1,3). Primitive-rotation replay agreed with all 2401 spectra tested and directly verified total coefficients and extrema through length 17.

## originality

PASS

In the strongest matched sources, unrestricted binary extrema, Christoffel factor counts, scattered subsequences, and factor counts on the three-one slice do not cover the unrestricted positive four-part composition family. The supported distinct contribution is the full length spectrum on that family, its sharp extremal loss and equality cases, and the resulting aggregate and conditional law. This is a best-of-knowledge comparison, not a priority guarantee.

## value

PASS

The first four-run host with repeated 01 transitions introduces both an overlap between two factor rectangles and a competing interior zero suffix. The exact spectrum resolves both. The resulting fixed-run extremum is substantially more informative than a global numerical bound: it finds a sharp, length-uniform defect and all extremizers. The conditional law for a natural uniform run-composition model adds a nondegenerate fluctuation statement with exact moments; neither it nor the rigidity is furnished by the neighboring fixed-weight or unrestricted models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
