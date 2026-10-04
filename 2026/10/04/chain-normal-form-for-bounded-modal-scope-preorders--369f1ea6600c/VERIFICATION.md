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

The verifier exhaustively enumerates every relation on the \(n\)-element chain that already contains the chain order, for
\[
1\le n\le6.
\]

It retains exactly the transitive relations, since reflexivity is already forced by the chain order.

For each surviving relation it computes mutual-accessibility equivalence classes and checks that every class is a contiguous interval. It then reconstructs the relation from the ordered interval blocks and requires exact equality.

The observed counts are
\[
1,\ 2,\ 4,\ 8,\ 16,\ 32,
\]
matching
\[
2^{n-1}.
\]

For each relation it also computes
\[
\ell(d)=\min[d]_{\sim}
\]
and verifies
\[
d\sqsubseteq e
\quad\Longleftrightarrow\quad
\ell(d)\le e.
\]

For every current point \(d\) and every classifier value \(b\), it compares the direct bounded-modal successor set
\[
\{e:d\sqsubseteq e,\ b\le e\}
\]
with
\[
\{e:e\ge\max(\ell(d),b)\}
\]
and requires exact agreement.

Finally it independently generates the relation from every one of the
\[
2^{n-1}
\]
adjacent cut/tie bit strings and confirms that this generated set is exactly the exhaustive preorder set.

The script prints `VERIFY_OK`.

## Limits

The exhaustive computation corroborates the arbitrary-\(n\) proof. The theorem does not extrapolate from the finite replay and does not classify non-chain scope orders.
