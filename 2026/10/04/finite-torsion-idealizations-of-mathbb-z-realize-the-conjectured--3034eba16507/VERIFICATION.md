---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For R=Z⋉M with M finite of exponent n, (a,m) is a zero divisor exactly when gcd(a,n)>1: a common prime divisor annihilates a nonzero prime-order element of M, while gcd(a,n)=1 makes scalar multiplication by a invertible on M. Thus adjacency depends only on whether gcd(a+b,n)>1. Representatives 0,...,p-1 dominate by reduction modulo the least prime p|n. For fewer than p proposed dominators, for each prime q|n there remains a residue class modulo q avoiding all forbidden negatives; CRT combines these choices, and adding multiples of rad(n) makes the new vertex distinct without changing the avoidance. Hence no smaller set dominates. Finally Ann(0,y)=dZ⋉M for y of order d, whereas elements with nonzero integer coordinate have infinite-index annihilator; maximal proper finite-index annihilator ideals are therefore qZ⋉M for primes q|n. The mixed-prime CRT idempotent gives two zero divisors summing to a unit, so the non-ideal-zero-divisor hypothesis is met.

## originality

PASS

Chelvam--Asir formulate the domination equality as a conjecture outside their proved classes, while the later idealization paper concerns total domination under hypotheses that do not include a nonzero finite torsion module over Z. The audited ordinary-domination formula for Z⋉M is therefore not a corollary of the inspected general results. Resultary searches under idealization/trivial-extension and total-graph domination terminology returned the audited record and nearby but different domination problems, not prior coverage of this family.

## value

PASS

The domination equality answers a published conjectural bound on a natural infinite non-Artinian family lying outside the later idealization hypotheses. The exact smallest-prime formula is structural, not a finite slice, and the same argument identifies precisely the finite-index maximal annihilator ideals that make the conjectural comparison meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
