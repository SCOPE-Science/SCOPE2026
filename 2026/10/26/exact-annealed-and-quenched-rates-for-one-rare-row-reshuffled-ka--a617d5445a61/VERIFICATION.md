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

Each change of the current null line multiplies squared norm by x and consecutive projections onto the same line are idempotent. For the previous endpoint U the switch counts at first/interior/last rare-row positions are (2,2,1); for endpoint V they are (1,3,2). The interior category is empty at a=1. The current endpoint is V exactly in the last position, so the within-epoch count is 2+A_(j−1)−A_j−2A_(j−1)F_j. Starting in U sets A_0=0, and summing gives the claimed path count. The indicators for the cross-epoch last/first pattern are iid within each parity, with mean 1/m², which gives the almost-sure factor by two strong laws. Weighting the same switch cases by their equiprobable positions gives both columns of T. Its trace is x², its determinant is −x²(1−x²)/m², and strict positivity of T and the positive Perron projections give the claimed mean-square factor for the specified initial mass. For t=m⁻² and z=x⁻²>1, the rescaled Perron root y solves y(y−1)=t(z−1). The second derivative of z^(2t)−z^t−t(z−1) has sign that of (4t−2)z^t+1−t<0; its value and first derivative vanish at 1. This gives the strict lower inequality against the almost-sure factor. The characteristic polynomial at x equals x²(1−x)[1−t(1+x)]>0, proving the upper inequality. Products with the rare row at an endpoint attain squared operator norm x; interior products have squared norm x². The small-x and m=2 statements follow from the explicit roots. At a=1 the system is square rather than strictly overdetermined, but the explicit hypotheses and proof include this case. All factors are per epoch and for squared error. Independent replay: for u=(1,0), v=(4/5,3/5), apply the two integer matrices 25P_u=((0,0),(0,25)) and 25P_v=((9,−12),(−12,16)) to (0,1), for all rare-position sequences at a=1,…,4 and k=1,…,5. Checked 5694 paths and 40 endpoint expectation components against the formulas by clearing denominators and comparing modulo the first 36 primes starting at 1009. Their product exceeds the absolute difference bound 2·5^5·25^65, so agreement there is exact. The uploaded checker was read, not executed; its PASS count is a recorded finite check at another overlap, not the all-parameter proof.

## originality

PASS

The supported distinct content is the distributional multi-epoch result: the pathwise cross-boundary exponent, its almost-sure limit, the exact specialized mean-square recurrence and limit, and the strict rate comparison. Two-line projection geometry, uniform norm bounds and generic second-moment propagation are not original here.

## value

PASS

Repeated measurements plus one rare independent direction form a natural model in which dependence at epoch boundaries matters. Sharp distributional rates give a concrete benchmark for assessing uniform permutation bounds, and show that the mean-square and typical factors can differ by a divergent ratio at small overlap even when both improve on the sharp uniform bound. This is useful beyond a one-sweep calculation; it does not assert any work-normalized advantage of duplication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
