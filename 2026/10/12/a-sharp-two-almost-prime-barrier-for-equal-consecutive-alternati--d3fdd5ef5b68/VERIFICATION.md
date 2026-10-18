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

For multiplicative beta(p^a)=(p^(a+1)+(-1)^a)/(p+1), beta(m)<m when m>1 and beta(pq)=(p-1)(q-1) for distinct primes. If beta(n)=beta(n+1) and Omega(n),Omega(n+1)<=2, n+1 cannot be prime; n prime also excluded by elementary cases. Both composite force even member 2q (q odd prime), beta=q-1, and odd neighbor either r^2 or rs (odd primes); matching values with adjacency yields impossible r^2-2r+3=0 or r^2-2r+5=0, or (r-2)(s-2)=1 with r=s=3 contrary to distinctness, or (r-2)(s-2)=-1. Thus n=1 uniquely, and n=20 attains sharp multiplicity Omega(20)=3, Omega(21)=2 and beta values 12. Independently enumerated n<10000 as corroboration, not an infinite proof; actual source verify.py independently enumerates n<2 million.

## originality

PASS

Tóth established the alternating divisor function and posed the consecutive-equality question, listing the first solutions 1,20,116,...; OEIS A206368 records the same sequence. The assigned theorem is not that 20 is first numerical term but a universal theorem that no larger solution can have both numbers of at most two prime factors counted with multiplicity. No matching low-factor-complexity obstruction located after Resultary, sequence and same-author comparisons; possible unindexed elementary observation is retained.

## value

PASS

This exact first nontrivial prime-factor complexity threshold directly refines the open Diophantine equation beta(n)=beta(n+1) highlighted by Tóth; it rules out all prime/semiprime pair families rather than just extending a search table. Witness 20 makes cutoff optimal. The constraint is meaningful even without resolving infinitely many solutions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
