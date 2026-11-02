---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Every nonempty order-preserving isometry is a unique partial translation by shift a. Temporarily distinguishing 2n-1 empty maps gives a labeled shift family of 3*2^n-4 objects. For shifts a,b, surviving source positions form an interval of length L=max(0,n-w(a,b)) with w=max(0,a,a+b)-min(0,a,a+b); each common position has independent membership choices with generating factor 3+t and the remaining positions have 2-power multiplicity. Summing shifts by sign and displacement and correcting precisely 2n-2 extra empty-map labels yields the displayed all-n polynomial, including n=1. Independent direct multiplication of every ordered pair of actual partial translations through n=7 matched all coefficients (profiles recorded). Conditional on the labeled shifts the rank is exactly Bin(L,1/4). Exponentially decaying two-sided geometric shifts yield E(n-L)->64/27 and uniformly bounded fluctuations; a binomial coupling yields total variation O(n^-1/2), zero-label correction O(n2^-n), and the mean -16/27. The asymptotic proof is analytic, not inferred from finite enumeration.

## originality

PASS

Kehinde–Umar and Al-Kharousi–Kehinde–Umar count and classify individual partial isometries of finite chains (including some order-reversing variants), but the inspected statements do not give a two-independent-factor rank convolution. OEIS A183158 tabulates single-element fixed points, not rank of a composition. No Resultary or web hit claimed the exact all-n product-rank formula and limit.

## value

PASS

The monoid is a canonical finite-chain inverse semigroup whose single-element cardinalities and Green relations are studied. The full multiplication rank of two independent elements and its universal binomial approximation are new natural probabilistic/algebraic observables, and the nonzero constant mean correction records boundary geometry. The precise all-n generating polynomial is useful beyond routine single-map enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
