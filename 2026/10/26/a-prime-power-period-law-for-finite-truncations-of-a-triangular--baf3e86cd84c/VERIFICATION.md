---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On the cyclic shift module F_p[z]/(z^L-1) the map is triangular with diagonal 1,z,...,z. For L=dq, q=p^a, extension to a splitting field yields local z=lambda+b with b^q=0 at each dth root. The presence of every dth root for m>=1 gives prime-to-p order exactly d by the semisimple/unipotent decomposition. At lambda=1 put N=A-I. For k=p^e, N^k on column zero has coefficient (-1)^j binom(k-1,j-1)b^(k-j) in row j<=k: the first step must leave coordinate zero. The binomial coefficients are all units modulo p by Lucas, so row min(k,m) shows nonzero for k<m+q. For k>=m+q all such terms vanish; in positive columns Frobenius on bI-J kills all entries. On lambda!=1, B-I for the positive-index block is invertible, so the column coupling splits off and B^(dp^e)=I for k>=m+q. Raising a nontrivial p-group element to d coprime to p cannot erase the lower-bound obstruction. Thus the exact cutoff holds also when p divides L, including L=1, with m=0 identity. Compatible triangular inverses give the inverse-limit map, and finite order would bound all quotient orders. An independent direct iteration of every unit input (`python3 /workspace/reproduce.py`) verified the first identity time in 72 parameter triples, including m=0, mixed d and q, and powers of p. The frozen CHECK_OUTPUT.txt is recorded evidence only.

## originality

PASS

The triangular rule and general finite-linear-map order machinery are prior. The claim credited is the explicit least whole-configuration order in every finite spatial and coefficient truncation, with its inseparable-shift threshold. The inspected source statements do not give that threshold or make it a direct specialization without a rule-specific nilpotence calculation.

## value

PASS

The least identity time is a natural invariant for finite reversible truncations of an existing rule. The exact threshold explains the extra p-power needed when spatial shift multiplicity and coefficient depth interact, gives usable finite recurrence times and separates finite quotient periodicity from infinite order on the product limit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
