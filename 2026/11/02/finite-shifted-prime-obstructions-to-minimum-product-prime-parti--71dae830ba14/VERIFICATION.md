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

For a finite minimum-product A, sum U <= product U and q>16M^4 force the product R of all but the largest competitor prime below M; R>M contradicts q(R-M)<=R(u-d) and R<4M², R=M yields the same A via unique factorization. Then t=q+d-u gives exactly the finite even-shift condition, with strict comparison in converse. Selberg sieve yields O_A(X/log² X) exclusions. Independently re-enumerated Δ_{3,5}={6,8} ; inspected the source’s large-prime witness without an independent primality run; finite checks are not the proof.

## originality

PASS

Qualified best-knowledge original contribution; prior tools and claimed antecedents are explicitly excluded. The exact finite shift obstruction classifies all large q; isolated primes in Campbell suffice but do not capture successful nonisolated primes.

## value

PASS

The exact finite obstruction set is a computable arithmetic classifier refining isolated-prime sufficiency; successful prime extensions have density one and precise excluded shifts. It settles the growth question in a meaningful structural way, though density one itself follows from standard sieve arguments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
