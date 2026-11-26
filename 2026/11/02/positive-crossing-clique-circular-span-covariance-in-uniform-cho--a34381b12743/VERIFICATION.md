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

A uniformly marked and randomly oriented chord is a uniform distinct ordered endpoint pair, so the directed offset d is uniform and the remaining matching is uniform. The span is K+1 for K=min(d−1,2n−d−1). The conditional mean number of disjoint r-cliques is choose(n−1,r)/(2r−1)!!; one all-crossing pairing per 2r-set explains the denominator. For an r-clique containing the marked chord, choose r−1 endpoints on each arc and pair in the unique crossing order; the conditional probability of those pairs is 1/D_{n,r}. Multiplying the conditional expectation by K+1 and subtracting the product of the means gives the finite sum. The nonconstant profile g(k)=choose(k,r−1)choose(2n−2−k,r−1) has a zero initial range and strictly increases on its positive range (consecutive difference in the ratio numerator and denominator is (r−1)(2n−3−2k)>0 for k≤n−2). At n=r it jumps at the last atom. Positive mass on all K and the independent-copies identity certify strict covariance for every allowed n,r. For triangles, symmetry splits the weighted sum into twice the sum below d=n and its single central term; expansion in the power sums through degree five gives the polynomial in RESULT.md. Substitution with sum_d min(d,2n−d)=n² gives the stated covariance and leading n⁴/160. An independent exact enumerator in branches/d1e7a191-eba1-4837-a01b-dfb6fcb54ca2 checked all 15, 105, 945 and 10,395 matchings for n=3–6; the triangle covariances were 6/25, 32/35, 160/63 and 40/7, matching the formula. The finite replay is corroboration only; the supplied verifier was inspected, not executed.

## originality

PASS

The distinct supported content is the span mixed moment and its strict sign for all r≥3, with a triangle closed form. Earlier catalogue results cover the corresponding pairwise crossing statistic r=2 explicitly or by summing the length-class profile. Triangle versus edge counts, and clique number versus length, are not this mixed moment with total shortest endpoint-step span. Stronger higher-crossing enumeration examined concerns different statistics and gives no exact marked-span conditional profile from which this result follows mechanically. The historical assessment is bounded, not exhaustive.

## value

PASS

A natural geometric statistic and a natural intersection-graph motif statistic are coupled under the same matching. The universal strict sign for all higher cliques, including a unique maximal clique at n=r, and the exact higher-order mixed moment are useful quantities not fixed by the known pair result. The proof exposes a monotone marked-chord mechanism rather than merely computing a few cases. It does not assert stronger distributional association.

The dated certificate retains the supplied scientific assessment, sources and limitations.
