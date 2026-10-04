---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification

The proof was checked symbolically and with a separate finite replay.

The finite checker reconstructs \(H_n\) from the definition and exhaustively enumerates all permutations for \(3\le n\le7\). It confirms \(|\operatorname{Aut}(H_n)|=n\), and therefore obtains the labeled-copy counts \(8,30,144,840,5760\), matching \((n+1)!/n\). It also checks non-embeddability among the sampled distinct \(H_n\), reproducing the finite instances of the published antichain property and ending with `VERIFY_OK`.

For the general argument, the critical logical checks are: a forbidden structure of size \(j+1\) cannot affect smaller ages; at size \(n+1\), adding \(H_n\) removes precisely its single isomorphism type because equal-cardinality embeddings are onto; \(0\) is fixed by every automorphism of \(H_n\); the failures of \(R(0,\cdot,\cdot)\) form a directed \(n\)-cycle, so the automorphism group has order \(n\); and the Stirling transform preserves the first differing arity and gap because its diagonal coefficient is \(1\).

The finite replay does not prove the full theorem. The general result still depends on Koponen's published definition, antichain lemma, and Fraïssé-family construction. No independent audit has been performed.
