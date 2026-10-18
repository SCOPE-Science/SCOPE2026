---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Affine F7 support normalization reduces all five-element supports to R={2,3,4,5,6}; modulation shifts a zero to (0,0). Every possible five-zero set therefore appears among C(48,4)=194580 origin-containing five-row matrices over Q(zeta7). Independently implemented exact cyclotomic determinant/cofactor algorithm enumerated all 194580: 185895 nonsingular mod29, 3225 extra nonsingular over Q(zeta7), 5415 rank-four singular (5085 forcing a coefficient zero, 330 full-support one-dimensional kernels), and 45 rank-three cases each with an essential column forcing zero. Each of 330 surviving kernel rays has exactly the selected five zeros. One witness supplies existence. Pair double counting gives 49*330/5=3234; degree-2 polynomial rigidity makes quadratic-linear character action on each five-supported ray free of orbit size 49, hence 66 orbits. Full finite census is exhaustive and exact; not a floating point sample.

## originality

PASS

Dongwei Li 2026 arXiv:2609.16030v1 abstract gives upper bound six in this case; materially inspected v2 proves general MUB total-support estimates and global minimizers, but at fixed five support its bound is weaker and the global minimum 44 does not classify the 49-total-support five-zero extremizers. Fiorentino–Weigert 2022 discusses dimension-seven overall quantum support, not this fixed-support count. Resultary hits at other groups/primes/other parabola moments do not imply same p7 invariant.

## value

PASS

Exact first nontrivial odd five-support sharp finite parabola uncertainty and full orbit census in the smallest natural field of size seven. The precise zero count and number of coefficient rays are intrinsically useful discrete invariants, not arbitrary computed slices or restated weaker general bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
