# A prime-power exponent threshold for finite partial-permutation completion

## Finding

Let \(X\) be a finite nonempty set, let \(f:X\rightharpoonup X\) be an explicitly represented partial bijection, and let \(k\geq0\) be an integer written in binary. Define **bounded ternary-power completion** to ask whether there is a permutation \(\tau\in\operatorname{Sym}(X)\) which extends \(f\) and satisfies \(\tau^{3^k}=\mathrm{id}_X\). The domain cannot be enlarged.

**Theorem.** Bounded ternary-power completion is NP-complete. Hardness holds even when \(f\) is acyclic, every component is a directed path, \(k=O(\log |X|)\), and every path contains strictly between one-quarter and one-half of \(3^k\) vertices. In contrast, for each **fixed** \(k\), the problem is decidable in polynomial time. These claims are about explicit finite inputs, not the unconstrained existence of an extension on a larger carrier.

## Assumptions and scope

A partial bijection is an injective partial self-map. Each component of its graph is either a directed path, possibly a single vertex, or a directed cycle. If the graph has a cycle, that entire cycle is already forced in every permutation extending \(f\). A directed path containing \(\ell\) vertices has \(\ell-1\) prescribed edges. Every cycle of a permutation with \(\tau^{3^k}=\mathrm{id}_X\) has length in \(\{1,3,\ldots,3^k\}\). The input explicitly lists vertices and arrows; \(k\) is part of the input. No extra vertices, partial-map changes, or extra generators are allowed.

## Proof

**Structural reduction.** Each pre-existing cycle must have length in \(\{1,3,\ldots,3^k\}\), or completion is impossible. For the remaining components let \(\ell_1,\ldots,\ell_s\) be their vertex counts. An extension exists exactly when these indexed path components can be partitioned into blocks such that every block's length sum belongs to \(\{1,3,\ldots,3^k\}\). Necessity follows because prescribed path edges cannot be broken and any completed permutation cycle is assembled by joining whole paths. Conversely, for every block, join its path endpoints cyclically; the result is a permutation of exactly \(X\), respecting all specified arrows and having allowed cycle lengths.

**NP membership.** A full permutation of \(X\) is a certificate of \(O(|X|\log |X|)\) bits. Check extension arrow by arrow and compute every cycle length. Repeatedly dividing each length by \(3\) decides whether it is a power of \(3\), and the exponent is compared with \(k\). This is polynomial even when \(k\) is written in binary.

**Hardness.** Reduce from unary, strongly NP-complete 3-PARTITION with \(3m\) positive integers \(a_1,\ldots,a_{3m}\), target \(B\), total \(mB\), and strict bounds \(B/4<a_i<B/2\). Put \(Q=3^h\), the least power of \(3\) not smaller than \(B\); \(C=Q-B\); and \(P=3Q=3^{h+1}\). Define
\[
L_i=3a_i+C,\qquad\sum_{i=1}^{3m} L_i=mP.
\]
By the strict input bounds and \(C\geq0\),
\[
P/4<L_i<P/2.
\]
Construct a disjoint union of \(3m\) directed paths with respective vertex counts \(L_i\); let \(k=h+1\). This is a polynomial-time construction on unary 3-PARTITION inputs, since \(Q<3B\), \(P<9B\), and \(|X|=mP\).

If the 3-PARTITION instance is solvable, the paths corresponding to each triple of sum \(B\) have total length \(3B+3C=P\), so joining each triple into a cycle of length \(P\) supplies a valid extension.

Conversely, suppose the constructed partial map admits a permutation of exponent dividing \(P\). Because every path contains more than \(P/4\) vertices, no completed cycle can have length smaller than \(P/3\). A cycle of length \(P/3\) must contain precisely one path, and that path has length exactly \(P/3\). This equality is equivalent to \(a_i=B/3\). A cycle of length \(P\) necessarily contains **exactly three** paths: one or two cannot fill it because each has length less than \(P/2\), while four exceed it because each has length more than \(P/4\). For three paths in such a cycle, \(\sum L_i=P\) implies \(\sum a_i=B\).

Let \(s\) be the number of singleton-path cycles of size \(P/3\). Since there are \(3m\) paths in total and every remaining cycle uses exactly three paths, \(s\equiv0\pmod3\). Group the \(s\) exceptional original integers (each equal to \(B/3\)) into triples. Together with the original triples corresponding to \(P\)-cycles, this gives a valid 3-PARTITION. Thus the reduction preserves yes/no answers. Strong NP-completeness yields NP-hardness with the explicit path-size promise, establishing NP-completeness.

**Fixed exponent.** Fix \(k=K\) and put \(P=3^K\), now a constant. After checking prescribed cycles and rejecting paths longer than \(P\), record the count \(c_j\) of path components of length \(j\), for \(1\le j\le P\). There are at most \((|X|+1)^P\) possible count vectors. For each state enumerate the finitely many (depending only on \(K\)) nonnegative grouping vectors \(t=(t_1,\ldots,t_P)\) with \(\sum j t_j\in\{1,3,\ldots,P\}\), and subtract \(t\) when possible. Reachability of zero by memoized dynamic programming is polynomial in \(|X|\) for each fixed \(K\). The parameter's variability, not the number of partial maps, causes the NP-complete regime.

## Verification

A Python 3 standard-library checker, `verify.py`, directly compares the 3-PARTITION decision with independent indexed-subset cycle-packing on every admissible six-integer multiset with target \(8\le B\le48\). It also creates explicit permutations for representative positive instances and compares an independently implemented fixed-exponent count-vector dynamic program with indexed-subset packing for all multisets of at most six lengths between \(1\) and \(9\). Run `python3 verify.py` from the extracted package. The checker prints `VERIFICATION_OK` only after all assertions pass. Finite verification supplements but cannot replace the reduction proof.

## Relationship to prior work

Etedadialiabad and Gao study \(\Pi\)-extension problems for families of partial permutations and finite \(\Pi\)-group solutions, permitting a larger carrier. Their cyclic/trivial fundamental-group results establish existence on some finite extension, not the exact zero-added-vertex, exponent-bounded decision problem here. Auinger and Steinberg study general pseudovariety extension decidability; that older problem also permits a larger carrier. The 3-PARTITION reduction is a new application of the classical strongly NP-complete packing primitive to fixed-carrier ternary-power permutation completion. The structural equivalence to allowed-length packing is stated explicitly rather than treated as a separate discovery.

## Limitations

This theorem does not address multiple simultaneously prescribed partial maps, minimum enlargement beyond zero extra vertices, arbitrary prescribed permutation groups, approximability, or fine-grained parameterized complexity. The fixed-\(K\) algorithm has a degree depending on \(3^K\) and is not claimed fixed-parameter tractable. Matching prior statements hidden under alternative cycle-packing terminology remain an originality risk. The full text of the 2003 Auinger–Steinberg paper was not accessible for complete comparison; its abstract alone does not establish non-coverage. No independent external audit has been performed.

## References

1. Mahmood Etedadialiabad and Su Gao, *Extension Properties for Partial Permutations*, arXiv:2610.04870v1 (first public October 4, 2026), https://arxiv.org/html/2610.04870v1. Relevant sections: Introduction, 4.5, Theorem 4.19, and Section 4.7.
2. Karl Auinger and Benjamin Steinberg, *On the Extension Problem for Partial Permutations*, Proceedings of the American Mathematical Society 131 (2003), 2693–2703, doi:10.1090/S0002-9939-03-06860-6.
3. Michael R. Garey and David S. Johnson, *Computers and Intractability: A Guide to the Theory of NP-Completeness*, W. H. Freeman, 1979. Classical strong NP-completeness of 3-PARTITION.
4. Markus Lohrey and Andreas Rosowski, *Finding cycle types in permutation groups with few generators*, arXiv:2503.02864 (2025); the input is a generated permutation group, not a partial map to be completed.
