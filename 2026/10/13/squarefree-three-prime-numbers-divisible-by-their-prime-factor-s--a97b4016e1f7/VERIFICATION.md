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

For p<q<r distinct primes, S=p+q+r lies strictly in (r,qr), and if S divides the squarefree number pqr then it equals pq or pr, since the remaining divisors are outside that interval. S=pr gives q=(p-1)r-p, incompatible with q<r for p>=3; hence p=2 and r=q+2 (twin prime). S=pq gives r=pq-p-q>q, which forces p>=3. Both converse branches divide pqr, and the branches are disjoint. The bounding inequality holds even p=2,q=3. I independently factor-enumerated all squarefree three-prime n<=60000 and obtained exactly the two branch types; finite enumeration is corroboration, not proof.

## originality

PASS

Best-of-knowledge exact classification of a canonical three-prime layer of the De Koninck-Luca beta(n)|n problem. Their full primary 2005 paper proves global counting bounds and uses large-prime estimates, not the complete p<q<r two-branch divisor interval. OEIS A158804 is an exact list without this exhaustive parameterization. Natural overlap includes old examples 30,70,105 and the beta function itself; novelty is the complete iff.

## value

PASS

A natural and non-arbitrary first nontrivial three-distinct-prime support classification for a literature-studied divisibility property, separating twin prime and shifted-product prime families with an exact divisor identity. This can be used to test density and infinitude issues without pretending to solve them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
