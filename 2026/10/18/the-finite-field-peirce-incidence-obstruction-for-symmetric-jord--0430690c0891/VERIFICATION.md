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

For P=I/2+[[r,s],[s,-r]], the idempotent conic r^2+s^2=1/4 and trace orthogonality give P∘J={X=aI+[[u,v],[v,-u]]:ur+vs=a/2}. For Q=u²+v²≠0, line/conic solutions number 1+χ(Q−a²)=1+χ(−det X); Q=0 and scalars have separate, correctly handled cases. Standard nonzero-level character counts and zero-level split/aniso counts produce all four incidence fibers for each χ(−1)=±1, summing to q³. Any nontrivial terminal rank-one idempotent forces the Jordan word into P∘J, giving the one-sided excluded nonscalar counts; not a converse. Independently reconstructed every matrix/primitive-P incidence for q=3,5,7,11,13 with exact modular arithmetic and matched all displayed fibers. Field F_9 not independently rerun; general proof covers prime powers through quadratic characters.

## originality

PASS

Best-of-knowledge PASS for the full odd-finite-field terminal-Peirce incidence distribution and word-obstruction count; standard Peirce decomposition, finite conic character sums, and associative idempotent factorization are not new. The highly relevant September 2026 primary Jordan-word paper was not available in full; it is a material specific priority risk, not an automatic originality failure.

## value

PASS

The primitive-Peírce terminal-factor count κ is motivated by the last idempotent in a Jordan word. Its complete nontrivial χ(−1)-dependent fiber census yields exact large families of provably unrepresentable nonscalar matrices, a natural structural obstruction for later finite-field Jordan-word work. It does not assert sufficiency and thus avoids an unsupported full representability classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
