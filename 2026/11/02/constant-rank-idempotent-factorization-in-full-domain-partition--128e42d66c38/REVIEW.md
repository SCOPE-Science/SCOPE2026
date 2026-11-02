# Self-review

## Correctness — PASS
The three-row partition multiplication supports the explicit \(\alpha=te\) decomposition, where both \(t\) and the idempotent \(e\) retain the rank of \(\alpha\). The elementary movable-token lemma has the necessary nonempty-vacancy hypothesis \(r<n\), and each token move is implemented by a rank-\(r\) idempotent full transformation. The proof makes no unsupported extrapolation from finite tests. The standalone exhaustive verifier checks all singular elements through \(n=5\) and every proper rank-ideal closure through \(n=4\).

## Originality — PASS relative to inspected primary literature
East–Gray arXiv:2011.00663 asks whether all proper full-domain rank ideals are idempotent-generated. Carroll–East–Fresacher arXiv:2507.05497 proves that the largest singular ideal is idempotent-generated but does not assert same-rank factorizations or generation of every smaller ideal. An unrestricted partition-monoid theorem is not directly transferable to the full-domain submonoid. Actual research-record, bibliography and targeted terminology searches found no decisive equivalent, although embedding the construction into prior general normal forms remains a priority risk.

## Mathematical value — PASS
The result resolves the outstanding proper-ideal question in the positive and gives a stronger diagram-by-diagram rank-preservation property. Rank is the canonical Green-class stratification for these finite semigroups, so the proof removes a genuine generation obstruction rather than providing an arbitrary enumeration. No minimal idempotent-generator cardinalities are claimed.

## Prior-work risk and limitations
The 2025 top singular-ideal result is already known and is explicitly separated from the new lower-ideal and same-rank assertions. The general factorization result might be implicit in a broader semigroup factorization argument; independent literature review and mathematical audit are not performed.

Self-review: passed. Independent audit: not yet performed.
