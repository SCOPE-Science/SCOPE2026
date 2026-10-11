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

In part \(V_i\), a zero vertex is adjacent precisely outside \(V_i\), so feasibility is exactly \(Z-z_i>0\) and \(T-t_i>0\). Fixing the set \(Q\) of zero-containing parts, the base product counts all such labelings, while the bad event for part \(i\) is absence of label two outside it. Any intersection of at least two distinct bad events has no label two anywhere, so inclusion-exclusion collapses to the displayed \((|Q|-1)C_Q\) correction. The minimum cases follow from where zeros and defenders can coexist. In particular, for a star \(K_{1,n}\) no zero labeling is feasible under the printed definition, so the minimum is \(N\), not four when \(N>4\). I independently replayed the part-count criterion on representative multipartite profiles; the repository verifier exhausts every profile through order nine.

## originality

PASS

The full founding paper was obtained and read. It introduces the same definition and gives scalar values for standard families, including Theorem 3.4 asserting \(\gamma_{rR}(K_{m,n})=4\), but it does not enumerate all functions or treat arbitrary multipartite graphs. Moreover, as printed without a non-singleton restriction, that complete-bipartite statement conflicts with the defining zero-neighbor condition on stars \(K_{1,n}\) for \(n\ge4\); the audited minimum formula correctly isolates this boundary. No checked later source supplies the arbitrary-multipartite weight enumerator.

## value

PASS

This is a natural complete classification of a standard domination variant on the canonical complete-multipartite class, with a nontrivial inclusion-exclusion enumerator for every weight. Full inspection of the founding paper also reveals that the audited formula resolves a genuine singleton-part boundary missed by its printed complete-bipartite statement, giving the result value beyond routine polynomial bookkeeping.

The dated certificate retains the supplied scientific assessment, sources and limitations.
