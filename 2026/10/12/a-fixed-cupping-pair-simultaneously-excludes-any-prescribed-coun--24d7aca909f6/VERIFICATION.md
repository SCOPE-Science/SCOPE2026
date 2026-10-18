---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Let C be c.e., A,B<_T C, A≰_T B, each E_n noncomputable and ⊕_n E_n≤_T B uniformly. Define D on computable columns by D(q(0,m))=B(m), D(q(n+1,m))=E_n(m). Then D≡_T B, D≤_T C, A≰_T D, so the hypotheses of Cintioli Theorem 4.1 hold. Enumerate all requirements indexed by triples (n,e_0,e_1) and adapt the exact finite certificate rule from its Lemma 5.1: at a splitting input m use distinguished coordinate q(n+1,m) and choose a root length k greater than both current restraint and that coordinate; select the branch of output 1−γ(q(n+1,m)). This preserves finitary effective admissibility and the source safe-side invariant. On the true long root, that coordinate equals E_n(m), giving a diagonal contradiction whenever certified. If no certificate yet both X_0 and X_1 computed E_n, absence of a splitting on either side would make E_n computable, contradicting hypothesis; the safe-side protocol eventually forces certification, as in the fully read source proof. Thus each triple requirement succeeds for the same constructed X_j, and D≤_T A⊕X_j yields B≤_T A⊕X_j. The statement does not require all E_n separately to be computable from C without a uniform join, nor imply a minimal pair. No finite experiments establish infinite priority construction.

## originality

PASS

The primary Cintioli paper gives single-target avoidance and constructs two witnesses for a fixed designated column. It expressly allows a structurally admissible finite rule, and supplies the mechanism reused here; but it does not jointly meet triples (target n, two program indices) for an arbitrary countable family, nor assert one pair avoiding all such targets. A single E=⊕E_n does not suffice: avoiding the join need not avoid any individual E_n. Relative simultaneous cone-avoidance results require noncomputability relative to a base; the targets here are uniformly below B, so a base containing B makes them computable and does not cover the target setting. No directly covering countable fixed-pair statement was found; the original paper was actually read in full at critical proof points, and the residual risk is priority elsewhere.

## value

PASS

Cintioli explicitly leaves dependence of witnesses on the avoided target as the gap to stronger fixed-pair/minimality claims. This proves a nontrivial intermediate uniform statement: one pair can simultaneously avoid every degree in a prescribed countable B-computable family while both still cup A above B. The precise uniform-join hypothesis delineates applicability and gives a reusable multi-requirement diagonalization technique; it does not falsely claim a universal minimal pair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
