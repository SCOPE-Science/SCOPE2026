# Anti-forcing spectrum of the McGee cage and a two-factor-profile obstruction

## Finding

Let \(G\) be the McGee graph, specified by the labeled LCF representation \([12,7,-7]^8\) on \(\mathbb Z/24\mathbb Z\). For a perfect matching \(M\), define its *anti-forcing number* \(\operatorname{af}(G,M)\) as the minimum cardinality of \(S\subseteq E(G)\setminus M\) such that \(G-S\) has exactly one perfect matching, namely \(M\). Define the anti-forcing polynomial \(A_G(t)=\sum_{M}t^{\operatorname{af}(G,M)}\), summing over *all* perfect matchings.

**Theorem (complete finite census).** The graph \(G\) has exactly \(60\) perfect matchings, and
\[
 A_G(t)=40t^5+20t^6.
\]
In particular its minimum anti-forcing number is \(5\), its maximum is \(6\), and its spectrum is \(\{5,6\}\). If \(\lambda(M)\) denotes the multiset of cycle lengths in the complementary spanning two-factor \(G-M\), the joint distribution is exactly:

| \(\lambda(M)\) | \(\operatorname{af}=5\) | \(\operatorname{af}=6\) | Total |
|---|---:|---:|---:|
| \((8,8,8)\) | 8 | 4 | 12 |
| \((12,12)\) | 0 | 6 | 6 |
| \((24)\) | 32 | 10 | 42 |
| **Total** | **40** | **20** | **60** |

Thus **the complementary two-factor cycle-length partition does not determine the anti-forcing number**, even within a single smallest cubic cage: both \((8,8,8)\) and \((24)\) occur at each of the two anti-forcing values. Across all matchings there are exactly \(18{,}200\) pairs \((M,S)\) with \(S\) a minimum-cardinality anti-forcing set for \(M\).

## Assumptions and scope

All graphs are finite, undirected, simple, and labeled. To construct \(G\), start with the \(24\)-cycle on labels \(0,1,\ldots,23\), and for every label \(i\), add the undirected chord between \(i\) and \(i+a_i\pmod{24}\), where \(a_i=12,7,-7\) according as \(i\equiv0,1,2\pmod3\). Duplicate descriptions of chords denote the same edge. This produces \(24\) cycle edges and \(12\) chords, hence a cubic graph with \(36\) edges. This is a standard LCF model of the McGee \((3,7)\)-cage, the unique cubic graph of girth seven on \(24\) vertices.

Every perfect matching is a set of \(12\) disjoint graph edges covering all \(24\) labels. The complement \(G-M\) has degree two everywhere, so \(\lambda(M)\) is defined. The theorem concerns exactly this graph, not every cubic cage or every graph of girth seven.

## Proof

**Reduction to a finite hitting problem.** For any perfect matching \(M\) and \(S\subseteq E(G)\setminus M\), the matching \(M\) survives the deletion of \(S\). It is the *unique* surviving perfect matching if and only if for every other perfect matching \(N\ne M\), one has \(S\cap N\ne\varnothing\). Indeed, \(N\) survives exactly when none of its edges belongs to \(S\). This direct equivalence is also consistent with the standard characterization using alternating cycles (Lei–Yeh–Zhang, Lemma 2.1).

**Complete enumeration of all matchings.** The executable `verify_exact.py` constructs the \(36\) graph edges from the stated LCF rule. It recursively chooses the smallest uncovered vertex and pairs it, in turn, with *every* currently uncovered neighbor. Every perfect matching has exactly one such sequence of choices; each returned terminal sequence covers all vertices. Sorting and deduplicating give exactly \(60\) matchings. Neither sampling nor a heuristic matching library is involved.

**Exhaustive optimization for each matching.** For a fixed \(M\), there are \(24\) candidate deletion edges outside \(M\) and \(59\) rival matchings. For each candidate edge \(e\), the verifier encodes the set of rivals containing \(e\) as a \(59\)-bit mask \(B_e\). An edge set \(S\) anti-forces \(M\) exactly when the bitwise union of the \(B_e\), for \(e\in S\), covers all \(59\) positions. The verifier checks **every** \(k\)-element subset of the \(24\) candidates for successive \(k=0,1,\ldots,6\), stopping at the first nonzero number of covers. For each \(M\) it thereby proves both the nonexistence of a smaller set and the existence of a set of the stated minimum size. Every assertion in the theorem then follows from a complete, finite count; in particular, the two-factor partitions are recomputed from the connected components of \(G-M\).

The machine-readable `certificate.json` contains every matching, its exact optimum, the number of optimal deletion sets, one explicit optimal deletion set, and its complement two-factor cycle lengths. As explicit witnesses for non-determination, matching indices \(0\) and \(4\) in that canonical enumeration both yield complementary partition \((8,8,8)\), but their anti-forcing numbers are \(6\) and \(5\), respectively. The totals of minimum deletion sets over the eight automorphism orbits are independently grouped by the second checker, with grand total \(18{,}200\).

## Verification

Run `python verify_exact.py certificate.json` in a Python 3.10+ environment with no additional packages. It reconstructs the certificate and verifies the full spectrum, refined table, and total count, by exhaustive enumeration. Its certificate file is deterministic (sorted JSON with a final newline).

For a differently structured check run `python verify_independent.py certificate.json` with NetworkX, NumPy, and SciPy installed. This verifier uses an explicit edge list, a separate matching enumerator, integer linear programming for all \(60\) optimization problems, and direct verification that every stored deletion witness eliminates every competitor. It also enumerates the \(32\) automorphisms, finding eight orbits on the perfect matchings, and checks their optimum values and certificate multiplicities.

The executed outputs are included in `verify_exact.out` and `verify_independent.out`. They are records of execution, not substitutes for the executable programs or the finite-completeness argument above.

## Relationship to prior work

The McGee cage and its LCF descriptions are classical. The anti-forcing invariant and the alternating-cycle formulation are due to existing matching literature. Lei, Yeh, and Zhang (2014), in particular, prove general anti-forcing relations and a plane-bipartite minimax theorem; those do not determine the nonbipartite McGee graph's \(60\)-matching distribution. Deng and Zhang (2016) treat extremal anti-forcing properties and even polygonal chains. Alikhani and Soltani (2017) calculate anti-forcing numbers for graph chains, coronas, and chemical graphs rather than the McGee cage.

The new statement here is the *specific complete McGee distribution*, its refinement by complementary two-factor type, and the resulting concrete failure of two-factor profile to determine anti-forcing. The general reduction to hitting rival matchings is not claimed to be new. A search for equivalent indexed results found no statement covering these numerical and structural claims; that search cannot establish absolute publication priority.

## Limitations

This is a computer-assisted **finite theorem** for one canonical cubic cage. Completeness follows from explicit exhaustive loops over all perfect matchings and all relevant deletion subsets, not extrapolation from a few examples. The result makes no claim about anti-forcing spectra of larger cages or about asymptotic behavior. An undetected equivalent result under another name or in inaccessible literature remains possible; the independently supplied verifier offers computational corroboration, not a formal external audit.

## References

1. H. Lei, Y.-N. Yeh, H. Zhang, *Anti-forcing numbers of perfect matchings of graphs*, arXiv:1406.3796v1, first publicly posted 2014-06-15, especially Lemma 2.1 and Theorem 2.2. https://arxiv.org/abs/1406.3796
2. K. Deng, H. Zhang, *Extremal anti-forcing numbers of perfect matchings of graphs*, arXiv:1607.05392v1 (2016). https://arxiv.org/abs/1607.05392
3. S. Alikhani, N. Soltani, *Anti-Forcing Number of Some Specific Graphs*, Iranian Journal of Mathematical Chemistry 8 (2017), 313–325, DOI:10.22052/IJMC.2017.60978.1235.
4. E. W. Weisstein, *McGee Graph*, MathWorld, https://mathworld.wolfram.com/McGeeGraph.html (LCF representation and classical graph parameters).
