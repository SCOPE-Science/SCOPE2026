# Review of Connected domination polynomial of crown graphs

## Correctness
**PASS.** The proof first shows that a connected dominating set must select at least two vertices from each shore: with exactly one selected vertex on one shore, domination forces its deleted mate into the set, where that mate becomes isolated. With at least two vertices on each shore, domination is automatic. Connectivity is automatic when either shore contributes at least three vertices; in the only remaining two-by-two case, disconnection occurs exactly when the two index sets coincide. These cases are exhaustive and yield the polynomial by direct counting. The finite verifier independently replays the literal definitions through \(n=8\); it is not used as an infinite proof.

## Originality
**PASS.** The 2026 initiating source defines the same connected domination polynomial and proves a lexicographic-product substitution theorem, but its inspected full text contains no crown-graph result and its explicit seed families are cycles and joins of cycles. The 2018 source gives the complete-bipartite polynomial, which is not implication-equivalent after deleting a perfect matching. Standard graph tables already give the scalar value \(\gamma_c(\operatorname{Cr}_n)=4\), so that consequence is explicitly excluded from the originality-bearing content. Targeted semantic searches for crown, matching-deleted biclique, all connected dominating sets, and the exact polynomial found no covering statement.

The principal residual risk is bibliographic rather than mathematical: an older poorly indexed paper could contain the same crown enumerator. The relevant theorem of the 2018 paper was available through indexed full-text extraction, but the full PDF could not be retrieved during this check.

## Value
**PASS.** Crown graphs are the canonical one-factor deletion of balanced complete bipartite graphs. The result gives the complete feasible-set structure, every coefficient, the exact minimum-set count, and the total connected-dominating-set count, while exhibiting exactly how one-factor deletion changes the known complete-bipartite polynomial. This is a natural infinite-family benchmark for the recently renewed study of connected domination polynomials and their roots, not a finite table entry or a routine parameter increment.

## Closest literature and limitations
The closest same-invariant sources are Shao--Zhao (2026), which develops connected-domination root theory and a substitution formula, and Mojdeh--Emadi (2018), which computes the complete-bipartite polynomial. Neither inspected statement implies the crown formula. The known scalar crown value is retained only as a consistency corollary. No claim is made for partial matching deletions or unequal shores.

Self-review: passed. Independent audit: not yet performed.
