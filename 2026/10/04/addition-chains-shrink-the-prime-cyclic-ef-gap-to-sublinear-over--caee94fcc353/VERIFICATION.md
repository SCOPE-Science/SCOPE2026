---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For every distinct primes p<q, the r selected positive entries preceding p in an addition chain are distinct nonidentity residues mod p; recursive atomic R(a_j,a_k,a_i) equalities force all q-side choices to be a_i*y. Closing the chain with R(a_j,a_k,e) forces p*y=0. Since q is prime distinct from p, y=0, contradicting the named identity relation on the first move. For p+1, either truncate at a preceding p or close with R(a_j,a_k,a_0), forcing (p+1)y=y. For p-1, select the endpoint (r+1 moves) and close (p-1)y+y=0. Yao’s singleton power-evaluation bound yields l(p)<=log2(p)+O(log p/loglog p), thus n+O(n/log n) where 2^n<p<2^(n+1). Explicit small-chain arithmetic and closure cases were independently reconstructed from actual verify.py, which tests only finite instances and is not the universal proof.

## originality

PASS

The mathematical contribution is a uniform EF-game realization of arbitrary addition chains, not addition-chain asymptotics alone; Gomaa establishes n+1 lower and 2n upper for prime cyclic groups and asks to improve the gap, while Yao supplies the arithmetic lemma without EF games. Current published-finding semantic retrieval returned this item and adjacent signed-binary models, not an earlier same theorem; priority for an unindexed model-theory thesis remains possible.

## value

PASS

Replacing a universal factor-two gap by sublinear additive overhead for a natural prime-cyclic quantifier-rank comparison advances a stated descriptive-complexity problem and yields exact ranks when Lambda(p)=n+1; this is not a parameter-renaming of Gomaa’s binary construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
