---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The smooth six-branch-point cyclic 3-cover has genus four and the four given differential forms are regular. Cartier extraction for y³=g(x³) is diagonal because exponents are congruent mod 3, with A=[t^r]g^r, B=[t^r]g^{2r}, C=[t^{2r}]g^{2r}. The factorial coefficient ratios prove B=binom(4m,2m)Δ^m, and the finite-characteristic second-order ODE L_n(H_n)=0 (or an equivalent coefficient recurrence) proves C=Δ^mH_r. Independent exact multinomial arithmetic reproduced both polynomial identities for 13 primes 7≤p≤109, plus gcd(H_r,H_r′)=1 and H_r(±2)≠0. Analytically, the ODE and r<p make repeated roots away from ±2 impossible, while H_r monic degree r has exactly r geometric roots. With Δ≠0 the two B slots are never zero; diagonal semilinear Cartier stability yields p-rank/a-number (4,0) or (2,2). The quotient norm has degree a power of 3, prime to p, so its ordinary elliptic factor and Prym ranks follow. The finite-prime test supplements, not replaces, the all-prime coefficient and separability argument.

## originality

PASS

General Cartier-Manin conventions and superelliptic Jacobian theory are established. Achter–Howe explains semilinearity pitfalls, Kudo analyzes a different genus-four superspecial complete intersection, and Obus–Shaska treats characteristic-zero high-automorphism superelliptic CM settings. The inspected sources do not state the exact reduced r=(p−1)/3 smooth nonordinary parameter divisor, its two-step diagonal rank loss, or the complementary ordinary quotient and Prym invariants for this same pencil. Equivalent Legendre/Deuring polynomial or branch-cross-ratio descriptions remain a priority risk.

## value

PASS

The result gives a complete geometrically reduced nonordinary divisor, including exact multiplicities and p-rank/Prym specialization, for a natural one-parameter tame genus-four cyclic triple cover in infinitely many characteristics. The exact count is not a random small finite table and identifies a rigid rank-two degeneration forbidden for other ranks in this family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
