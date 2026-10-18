# Two-hole rigidity, sharp Horn arity, and symmetries of derangement concept lattices

## Finding

Fix an integer \(n\ge4\). Let \(D_n\) be the set of fixed-point-free permutations of \([n]\), and \(U_n=\{(i,j):i,j\in[n],\ i\ne j\}\). The formal context has objects \(D_n\), attributes \(U_n\), and incidence \(\pi I(i,j)\) when \(\pi(i)=j\). Write \(c(B)\) for attribute Galois closure: the cells possessed by every derangement extending \(B\); if no derangement extends \(B\), set \(c(B)=U_n\).

**Theorem.** An attribute set \(B\) is a partial derangement matching when no two of its cells share a first or second coordinate. For such a matching with \(k\) cells, let \(R\) and \(C\) be its unused rows and unused columns, respectively. Then:

1. If \(B\) is not a matching, \(c(B)=U_n\).
2. If \(k\le n-3\), \(c(B)=B\).
3. If \(k=n-2\) and \(R\cap C=\varnothing\), \(c(B)=B\). If instead \(R\cap C\ne\varnothing\), exactly one derangement extends \(B\), and \(c(B)\) is its complete set of \(n\) cells.
4. If \(k=n-1\), a unique completion exists precisely when the single unused row and unused column differ; in that event \(c(B)\) is the completing full derangement. Otherwise \(c(B)=U_n\).
5. If \(k=n\), then \(B\) is a full derangement and \(c(B)=B\).

Thus the closed intents are the matchings of sizes at most \(n-3\), the \((n-2)\)-matchings with disjoint unused row and column sets, the complete derangements, and \(U_n\).

Define
\[
r_{n,k}=\sum_{j=0}^{k}(-1)^j\binom nj\binom{n-j}{k-j}^{2}(k-j)!,\quad
 d_n=\sum_{j=0}^{n}(-1)^j\binom nj(n-j)!,
\]
\[
q_n=\binom n2\binom{n-2}{2}
\sum_{j=0}^{n-4}(-1)^j\binom{n-4}{j}(n-2-j)!.
\]
Then the number of formal concepts is exactly
\[
\boxed{C_n=1+\sum_{k=0}^{n-3}r_{n,k}+q_n+d_n.}
\]
Moreover the complete group of order-preserving concept-lattice automorphisms is
\[
\boxed{\operatorname{Aut}(\mathcal L_n)\cong\mathfrak S_n\times C_2.}
\]
The least possible maximal premise size among sound, complete, single-conclusion Horn implication bases (with **iterated** forward chaining) is exactly \(n-2\). One such basis comprises all pairwise conflicting cells implying the full attribute set, together with one implication from each \((n-2)\)-matching having \(R\cap C\ne\varnothing\) to its two forced completing cells.

## Assumptions and scope

All structures are finite. A partial derangement matching is a partial injective map with no fixed cells, not necessarily extendible. A formal concept is an extent-intent pair under the usual Galois connection. The lattice is equivalently the poset of closed intents ordered by inclusion (the isomorphism in the intent presentation may reverse the conventional concept order, but order automorphism groups and counts agree). A unit Horn implication \(A\to b\) has a finite premise \(A\subseteq U_n\) and singleton conclusion \(b\in U_n\). A basis is complete when repeated forward chaining produces \(c(B)\) for every initial \(B\). Replacing each multi-conclusion implication by singleton conclusions preserves the largest premise size.

## Proof

**Residual matching lemma.** For any bipartite \(m\)-by-\(m\) complete graph with \(m\ge3\), delete a partial matching \(F\) and at most one further edge \(e\) not in \(F\). A perfect matching remains. To see this by Hall's theorem, any single row has at least \(m-2\ge1\) neighbors. For any two rows, at most one column can lose both of its incident edges to those rows (the deleted matching alone has at most one deletion per column, and only one further edge is removed); hence their neighborhood has size at least \(m-1\ge2\). Every set of at least three rows has all columns as neighbors, since any column loses at most two incident edges. Hall's condition follows. The statement also holds when no further edge is deleted.

Given a partial matching \(B\) of size \(k\), possible extending derangements correspond exactly to perfect matchings in the residual complete bipartite graph on the unused row set \(R\) and column set \(C\), excluding the diagonal forbidden cells \((i,i)\) for \(i\in R\cap C\). These diagonal cells form a partial matching. If \(m=n-k\ge3\), the residual lemma shows a completion exists and each remaining permitted offdiagonal cell can be avoided by some completion. Thus no cell outside \(B\) belongs to all completions, and \(c(B)=B\). If \(m=2\), there are two unrestricted completions. When \(R\cap C\) is empty, both remain; when the intersection is nonempty, exactly one remains because the two diagonal forbidden cells (if both present) occur in the same one of the two completions. If \(m=1\), the single completion is valid exactly when its cell is offdiagonal. For \(m=0\), \(B\) is already a full derangement. Nonmatching sets cannot lie in any permutation, proving the closure classification.

For the enumerator, count all \(k\)-edge partial matchings off the diagonal. Inclusion-exclusion on forbidden diagonal cells gives \(r_{n,k}\), since after fixing \(j\) diagonal cells there are \(\binom{n-j}{k-j}^2(k-j)!\) completions to a \(k\)-matching. The full derangements number \(d_n\) is the familiar inclusion-exclusion formula. To count the surviving \((n-2)\)-matchings, first choose disjoint unused two-element row and column sets in \(\binom n2\binom{n-2}{2}\) ways. The remaining \(n-2\) rows and columns overlap in exactly \(n-4\) indices, and inclusion-exclusion over these possible diagonal cells yields the displayed formula for \(q_n\). Finally add the single top closed intent \(U_n\). Each closed matching category has a different size, so the sum is disjoint.

For automorphisms, the atoms in the closed-intent inclusion lattice are exactly its singleton cells. The join of two different atoms is the top \(U_n\) exactly when the cells conflict (share row or column): conflicting pairs cannot be realized by any permutation, whereas compatible pairs extend to a derangement or to a full-derangement closure strictly below the top, by the classification. The graph of conflicting pairs is the line graph of the crown graph \(K_{n,n}\setminus M\) with the omitted perfect matching corresponding to the diagonal. In a bipartite graph, every clique of at least three edges sharing pairwise an endpoint is a star. The maximal cliques of this line graph are therefore precisely the \(2n\) row and column stars, each of size \(n-1\ge3\). The intersection graph of these cliques recovers the two bipartition classes, with one absent cross-adjacency at each index. Its automorphisms simultaneously permute the \(n\) deleted matching pairs, possibly swapping the two sides. This is \(\mathfrak S_n\times C_2\). Any automorphism of the concept lattice induces such an atom permutation, and an order automorphism is determined by its action on atoms because every closed intent is the join of its singleton cells. Conversely, simultaneous relabeling of row and column indices and transposition of the incidence matrix preserve the derangement context and realize all these permutations, completing the classification.

For Horn arity, include every rule \(\{a,b\}\to u\) for conflicting cells \(a,b\) and each \(u\in U_n\); include, for every \((n-2)\)-matching \(B\) with intersecting unused row/column sets, the implications \(B\to u\) for both forced missing cells \(u\) of its unique completing derangement. All rules are sound by the closure classification. They are complete: consistent sets with at most \(n-3\) cells are closed, and the \((n-2)\) case follows immediately. A valid \((n-1)\)-matching with missing offdiagonal cell contains an \((n-2)\)-matching with a forced completion, giving that last cell. An \((n-1)\)-matching with missing diagonal \((i,i)\) contains a size \(n-2\) subset whose forced completing derangement conflicts with a retained cell; the conflict rules then give \(U_n\). Any initially inconsistent set already contains a conflicting pair, and full derangements are closed. Hence maximal premise size \(n-2\) suffices.

For necessity, fix distinct \(a,b\) and choose any derangement matching \(B\) of the \(n-2\) indices outside \(\{a,b\}\) (available because \(n-2\ge2\)). Its unused row and column sets both equal \(\{a,b\}\); thus its closure adds two cells. Every proper subset of \(B\) has at most \(n-3\) cells and is already closed. No sound implication with fewer than \(n-2\) premises can initiate a strict derivation from \(B\). Hence every complete iterative unit basis has a premise of size at least \(n-2\).

## Verification

Run `python3 verify_derangement_context.py` with Python 3 standard library. It independently builds derangements, partial matchings, Galois closures, inclusion-exclusion counts, and the proposed implication system. Exact direct computations for \(3\le n\le7\) return concept counts \(4,35,316,3292,36954\), respectively; the main theorem applies from \(n=4\). The \(n=4\) test additionally enumerates every subset of the twelve attributes. Automorphisms arising from simultaneous relabeling and transposition were checked directly in small instances. Such finite checks support but do not prove the unbounded statements. The group upper bound and Horn lower bound are proved above.

## Relationship to prior work

Derangements as perfect matchings of the bipartite complete graph minus a perfect matching, and their inclusion-exclusion enumeration, are classical. The partial-derangement counting machinery and full matching numbers are not claimed new. The 2022 deranged-matchings paper discusses the same underlying graph but analyzes matching counts, not the Galois closure of incidence against all perfect matchings. The 2023 hypergraph/formal-concept paper provides the generic intersection-lattice framework, not the specific two-hole closure or sharp iterative Horn arity. The claims here concern the exact fixed-point-free permutation **incidence closure lattice**, its full symmetry group, and optimal implicational premise arity; neither generic framework nor classical rook counting alone states these results.

## Limitations

No assertion of independently certified publication priority is made. Equivalent results could appear in finite constraint propagation, rook monoids, matching-geometry or lattice literature under different terminology. In particular, classical all-partial-derangement counts are not novel, and an algorithm to compute a closure from the definition is not by itself the asserted structural theorem. The group statement addresses order-preserving automorphisms of the concept lattice, not all permutations of its formal objects or incidence-preserving autotopisms. Horn complexity means least maximum premise size under iterative forward chaining, not minimum total basis size or one-pass direct bases. The case \(n=3\) is exceptional and excluded.

## References

- Bucić, Devlin, Hendon, Horne and Lund, *Perfect matchings and derangements on graphs*, arXiv:1906.05908 (2019).
- Johnston, Kayll and Palmer, *Deranged matchings: proofs and conjectures*, arXiv:2209.11319 (2022).
- Rawson, Myers, Green, Robinson and Joslyn, *Formal Concept Lattice Representations and Algorithms for Hypergraphs*, arXiv:2307.11681 (2023).
- Laradji and Umar, *Further combinatorial results for the symmetric inverse monoid*, DOI:10.12958/adm1793 (2022).
