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

Let v_i=alpha^(q^(is)), i mod N, N=2m. Since gcd(s,N)=1 these N rows form a K-basis. Ho Lemma 4.1 gives S0=lambda^-1 nonzero and S_r=0 for r≠0. Thus <v_i,v_j>_e is nonzero exactly when j=i−t mod N, t=e*s^{-1} mod N. The right orthogonal complement of span v_0..v_(k−1) is the complementary interval [k−t,...,N−1−t], the left complement [k+t,...,N−1+t]. Intersection with original interval has k−max(0,k−min(t,N−t))=min(k,min(t,N−t)) independent of orientation for k≤N/2. Endpoints e=0 and e=N/2 give LCD and Hermitian self-orthogonal; at k=m the latter is self-dual. Independent interval exhaustions N even up to 44, all units s, k,e; actual artifacts/verify.py also checks F9 scaled basis.

## originality

PASS

Islam–Horlemann 2022 gives the exact ordinary s=1 e-Galois profile using a self-dual basis; Ho 2026 gives scaled trace-self-dual all-q basis and generalized s but proves the Hermitian e=m endpoint. Their combined inputs lead to the explicit arbitrary e and s shifted duals and circular-distance hull formula, which is not a verbatim result of either inspected work. New general parametrized profile assessed as best-of-knowledge original, with reduction-to-known-cases acknowledged.

## value

PASS

Galois hull dimensions identify LCD, self-orthogonal and full hull twists, central invariants in rank-metric/quantum coding. The explicit dual-generator shifts give a complete uniform profile for every allowed generalized step, extending meaningful established endpoint theorems instead of merely reordering a known table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
