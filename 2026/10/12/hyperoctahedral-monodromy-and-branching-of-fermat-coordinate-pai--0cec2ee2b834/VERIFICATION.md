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

Reconstructed p_d(U)=2 sum binom(d,2r)U^r and p_d(T^2)=v. Derivative critical roots correspond inversion-pairs of nontrivial (d-1)-st roots of unity, excluding -1; exactly m-1 distinct simple critical points, with distinct critical values 2^d/(1+r)^(d-1), all !=2. Morse polynomial monodromy S_m; simple ramification at U=0/v=2 flips a single sign and conjugation yields the full C2^m kernel, so C2 wr S_m. Smooth projective Fermat generic fiber for n>=2 makes C(v) algebraically closed in C(z_1,...,z_n), preserving Galois closure under regular base change. Sheet-stabilizer normalizer yields deck group C2. For d odd center lies on hypersurface, degree d-1=2m. Verified d=4..11 critical-value discriminant squarefree and regular v=2 independently; finite checks do not prove general case.

## originality

PASS

The point locations and d=5 plane quintic D4 are old, but the uniform binomial-Morse all-degree proof, wreath normal closures for every d>=4 and n>=2, and explicit full cycle portrait extend beyond inspected prior results. General p(T^2) wreath theorem is standard; credit only family-specific critical-value hypothesis and resulting classification. Unread Miura–Taki quartic full text and unpublished companion preserve best-of-knowledge risk.

## value

PASS

Provides a complete exact Galois-closure and ramification classification for an infinite natural Fermat family, separates projection deck C2 from much larger normal closure, and determines closures at 24 geometrically classified quartic centers. The family-specific proof of Morse property is needed to invoke general wreath principles.

The dated certificate retains the supplied scientific assessment, sources and limitations.
