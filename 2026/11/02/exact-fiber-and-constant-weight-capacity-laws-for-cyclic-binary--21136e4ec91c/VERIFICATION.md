---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. For binary indexed cyclic read R_ell(x)_i=sum_{j=0}^{ell-1}x_{i+j}, 1<=ell<=n, consecutive differences imply that equal reads force a_i=x_i′-x_i to satisfy a_{i+ell}=a_i; this is a class constant on each of d=gcd(n,ell) length-L=n/d residue cycles. Equality of one read imposes sum of the class constants zero. Mixed binary classes admit no nonzero shift; pure all-zero/all-one classes can be exchanged provided h of p pure classes remain ones, yielding binomial(p,h) fibers and the exact histogram. Counting mixed patterns m=2^L-2 and p+1 pure output possibilities gives A=(2^L-1)^(d-1)(2^L+d-1), singleton 2(2^L-1)^d-(2^L-2)^d, maximal fiber binom(d,floor(d/2)), injective iff d=1. Weight-refined enumeration by M(z)=(1+z)^L-1-z^L yields the displayed rational expression that is exactly a polynomial, while fixed-L/fixed-ell limits follow algebraically. L=1 corresponds to ell=n and gives n+1 total outputs; ell=1 injective. Independent enumeration confirms representative gcd classes, but unrestricted classification is from the exact difference identity.

## originality

PASS

PASS, qualified. The closest weighted-read and transverse-read papers (Chee et al. 2021/2023; Yerushalmi et al. 2024) treat linear noncyclic reads, sometimes mentioning but not solving their cyclic analogue. Existing cyclic substring-composition profiles discard output ordering, and circulant kernel/linear inverse alone does not supply binary list-size and fixed-weight output enumerators. A classical circulant tomography or binary convolution theorem might encode equivalent formulas; searches and relevant source passages do not establish coverage.

## value

PASS

PASS. Complete fibers and fixed-composition zero-error capacity give a useful exact invariant for a naturally motivated periodic version of molecular/memory read channels, with strong gcd-dependent ambiguity not present in coprime lengths. The polynomial is independently informative to constant-weight coding and is not mechanically provided by standard linear nullity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
