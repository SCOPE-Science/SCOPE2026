---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The formal Thue–Morse product gives C(2m)=C(m)+C(m-1), C(2m+1)=-2C(m). For m>=1, C(4m)=C(m)-C(m-1) and C(4m+2)=C(m-1)-C(m); trivial coefficient bounds yield |C(4m)|<=2m+1 <=(3/5)(4m+1), with equality only m=1, whereas the 4m+2 bound is strict (including n=2). Removing trailing binary ones preserves |C(n)|/(n+1) and changes its sign; the base q=0 recovers exact Mersenne values, and base q=4 yields every three-fifths equality at n=5*2^j-1. The cross-parity indicator convolution is R=(n+1-C(n))/4, giving zero and half-density Mersenne exceptions and sharp one-tenth/two-fifths bounds elsewhere. Independently recomputed the recurrence through n=65535, direct digit-sum convolution and evil/odious pair counts for n<400, and all finite-range sharp equality indices, with agreement. These checks are not a substitute for the all-index recursion proof.

## originality

PASS

Best-of-knowledge original as the complete normalized mixed-parity representation gap and all equality families. Gawron–Miska–Ulas 2017 established the same twofold Thue–Morse convolution, binary recurrence and unnormalized dyadic-block coefficient maxima; Allouche–Shallit 2021 address same-parity sum representation identities and higher sums. Neither inspected full primary contains or implies directly the sharp normalized non-Mersenne 3/5 dichotomy plus both mixed-sum equality families. An equivalent corollary of older coefficient theory remains a priority risk.

## value

PASS

The evil/odious partition is a standard automatic-arithmetic object, and R(n) is its natural cross-class additive representation function. The exact global gap away from Mersenne indices and both infinite extremizing families give nontrivial sharp frequency information. Though the recurrence is elementary and known, the complete normalized extremizer classification is a motivated all-index invariant rather than a recomputation of a finite sequence table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
