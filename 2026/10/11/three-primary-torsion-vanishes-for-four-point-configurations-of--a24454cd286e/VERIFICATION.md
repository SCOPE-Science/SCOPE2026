---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

By An Proposition5.1 the top H4 over any field is Hom_{F3[S4]}(sgn,D(a)⊗D(b)). For a,b>=7, the 4-row chessboard complex has free top homology and shellability supplies a projective chain resolution. Its V4-trivial block has (x-1)U2^- plus projective U3^+,U3^- and the three nontrivial V4 blocks are projective; careful orientation sign is included. I reconstructed the nine mod-three sign-Hom dimensions as [[1,1,1],[1,1,2],[1,2,1]] from explicit S3 module matrices. Character/multiplicity expansion matches the ordinary averaging polynomial for H4, and exact sample Betti numbers at (7,7),(7,8),(8,8) are 1911,5726,16716. UCT gives H4(F3)-rank H4(Z)=dim Tor(H3(Z),F3)=0. All parameter values rely on the universal module polynomial identity, not finite sample extrapolation.

## originality

PASS

The complete 2026 An source Theorem5.10 proves odd-prime torsion vanishing for p>=m only; its Question8.2(1) explicitly singles out first excluded case m=4,p=3. The characteristic-three modular representation calculation treats precisely that missing case, so the claimed all a,b>=7 vanishing is not implied by An’s general vanishing theorem. Resultary search found no earlier exact same case beyond audited target.

## value

PASS

Resolves an explicit natural open first-exceptional-prime case for graph-braid homology across an infinite bipartite graph family. The exact rank comparison and modular structure can serve future integral torsion investigations. Does not claim lower part sizes or other primes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
