# First two-unit VC–Littlestone separation in comparisons of 321-avoiding involutions

## Finding

For each integer \(1\le n\le12\), consider the class \(\mathcal C_n\) of all involutions \(\pi\in S_n\) avoiding the permutation pattern \(321\), represented by the Boolean comparison functions
\[
 h_\pi(i,j)=\mathbf1[\pi(i)>\pi(j)],\qquad 1\le i<j\le n.
\]
The exact hypothesis counts, VC dimensions, and Littlestone dimensions are as follows:

| \(n\) | \(|\mathcal C_n|\) | \(\operatorname{VCdim}\) | \(\operatorname{Ldim}\) |
| ---: | ---: | ---: | ---: |
| 1 | 1 | 0 | 0 |
| 2 | 2 | 1 | 1 |
| 3 | 3 | 1 | 1 |
| 4 | 6 | 2 | 2 |
| 5 | 10 | 2 | 2 |
| 6 | 20 | 3 | 3 |
| 7 | 35 | 3 | 4 |
| 8 | 70 | 4 | 5 |
| 9 | 126 | 4 | 5 |
| 10 | 252 | 5 | 6 |
| 11 | 462 | 5 | 7 |
| 12 | 924 | 6 | 8 |

In particular, eleven is the first size at which the **adaptive-minus-static dimension gap is at least two**:
\[
\operatorname{VCdim}(\mathcal C_{11})=5,
\qquad\operatorname{Ldim}(\mathcal C_{11})=7.
\]
The gap remains two at twelve. The cardinality bound on the Littlestone dimension is strict at both sizes: the maximum possible root split smaller branch has respectively \(126<128\) and \(252<256\) hypotheses, ruling out complete trees of depths eight and nine. Exact dimension statements for larger \(n\) are not asserted.

## Assumptions and scope

Here an involution satisfies \(\pi(\pi(i))=i\) for all indices; avoiding \(321\) means that no \(i<j<k\) satisfies \(\pi(i)>\pi(j)>\pi(k)\). All values and indices are distinct elements of \([n]\). The query domain consists of the \(\binom n2\) unordered index pairs, canonically written with \(i<j\); response one means a descent *between those positions*, not necessarily an adjacent descent. Both dimensions concern this **Boolean positional-comparison representation**. The VC dimension permits one fixed query set with all labelings; Littlestone dimension permits a different query at each node of a complete binary tree while requiring one consistent concept at each terminal leaf. All calculations are exact integer computations, not sampling.

## Proof

**Exhaustive hypothesis representation.** Every involution of \([n]\) either fixes the least unused index \(i\), or exchanges it with exactly one other unused index \(j\). Recursing on the unused indices generates all involutions once and only once. The condition of avoiding \(321\) is equivalent to requiring that, for every middle position \(j\), one cannot find both a preceding value larger than \(\pi(j)\) and a later value smaller than \(\pi(j)\). Consequently, `verify.py` enumerates exactly \(\mathcal C_n\). It computes every Boolean comparison mask from the generated permutations. The resulting counts equal the previously known \(\binom n{\lfloor n/2\rfloor}\), as an additional check, but the exhaustion does not assume that identity.

**Static classification.** A set of queries is shattered precisely when every labeling is realized by at least one generated concept. The program adds queries in strictly increasing canonical index order. At every extension it splits each existing response-pattern fiber into its two outcome fibers, accepting the extension if and only if *both* fibers are nonempty for every previous pattern. Every candidate support appears in exactly one sorted-order traversal. If a pattern fiber contains one concept, no further query can split it, allowing a sound pruning step. The program checks all such supports for all twelve sizes; its maximum cardinalities are the VC column above. In particular, the eleven- and twelve-position upper-bound traversals have respectively 27,977 and 257,991 recursive nodes. The adjacent disjoint pairs \((1,2),(3,4),\ldots\) provide shattered supports of sizes five for \(n=11\) and six for \(n=12\); `verify.py` checks them by the same exhaustive fiber criterion.

**Adaptive classification.** For a nonempty version space \(S\) of hypotheses, set \(L(S)=0\) if \(|S|=1\), and otherwise define
\[
 L(S)=\max_{q:\,S_{q,0},S_{q,1}\ne\varnothing}
 \left(1+\min\{L(S_{q,0}),L(S_{q,1})\}\right),
\]
with maximum zero if no query splits. This is exactly the complete-tree definition: a depth-\(d\) root exists precisely when some query has both children of depth at least \(d-1\). The program memoizes all subsets of the finite concept-index set and checks every query split. To beat a current lower bound \(b\), both child spaces must contain at least \(2^b\) concepts; this justifies the only cardinality pruning. It also stops upon attaining \(\lfloor\log_2|S|\rfloor\), an absolute upper bound. The resulting twelve dimensions are exactly those in the table. For eleven and twelve, the packages in `tree_certificate.json` are full-depth trees (respectively 127 and 255 internal queries) with 128 and 256 distinct terminal hypothesis witnesses; each branch is checked against the actual comparison response.

**Independent critical upper bounds.** The additional Boolean depth algorithm `upper_obstruction.py` works by a yes/no depth recurrence, rather than optimizing \(L(S)\). For eleven and twelve, it confirms that depths seven and eight respectively exist while depths eight and nine do not. In fact the nonexistence checks reduce to a stronger root-cardinality obstruction: a depth-eight tree needs \(2^7=128\) hypotheses in *each* first branch, but at eleven positions every comparison's minority side has at most 126. Similarly, a depth-nine tree at twelve positions needs 256 per first branch and every minority side has at most 252. Those maxima come from evaluating every query's exact response mask; no assumption is made that the same formula holds for arbitrarily large \(n\).

The entries below eleven show a gap at most one, establishing the claimed **first** occurrence. Since all enumerations and recurrences are over complete finite sets with sound pruning conditions, they prove the listed finite dimensions rather than estimating them.

## Verification

From this directory, run `python3 verify.py` followed by `python3 upper_obstruction.py`. The first program enumerates all involutions and filters the avoidance condition, checks counts, independently regenerates the concepts from all permutations for orders at most eight, recomputes VC and Littlestone dimensions for every order through twelve, and checks the stored complete adaptive certificates against actual response masks. The second independently uses the Boolean full-tree-existence recurrence to verify the critical depths and obstructions. `python3 make_certificate.py` can regenerate the tree certificate; the checked artifact is already included. The normal final output lines are `INVERSION_INVOLUTIONS_EXACT_CLASSIFICATION_PASS` and `INDEPENDENT_BOOLEAN_DEPTH_RECHECK_ALL_PASS`.

## Relationship to prior work

Fang, Hamaker and Troyka (first public preprint 2020-08-31) analyze pattern avoidance in involutions and give the central-binomial enumeration of ordinary \(321\)-avoiding involutions in their Theorem 1.4(a), citing earlier enumeration. They do not provide the finite positional-comparison shattering dimensions here. Guingona, Kolesnikov, Nierwinski and Soucy study VC and Littlestone dimensions of zero-set families of nontrivial linear combinations, a different set-system construction. Chase, Freitag and Reyzin establish general connections between Littlestone dimension and query learning, not the present finite model. Existing unrestricted-involution results and unrestricted pattern-avoiding-permutation results address larger but different concept classes; restriction to their intersection does not determine either invariant, nor does the known central-binomial count determine it. The theorem treats fixed positions of a self-inverse permutation, not matched-pair membership or the alternative involution-containment order.

## Limitations

Only orders \(1\) through \(12\) are classified. The classification and first-gap threshold are finite exhaustive theorems, not formulas for arbitrary order. The certificate is computational and independently replayable but has not undergone independent mathematical audit. Historical-priority risk remains for alternate codings of two-row standard Young tableaux, ballot paths, nonnesting involutions, and Boolean positional comparisons; no global uniqueness claim follows from literature searches. Other query models, exact larger-order dimensions, and general closed forms remain open here.

## References

1. J. J. Fang, Z. Hamaker, and J. M. Troyka, *On pattern avoidance in matchings and involutions*, arXiv:2009.00079 (first posted 2020-08-31), Theorem 1.4(a); Electronic Journal of Combinatorics 29 (2022), P1.39.
2. V. Guingona, A. Kolesnikov, J. Nierwinski, and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (first posted 2021-09-10), Theorem 3.10.
3. H. Chase, J. Freitag, and L. Reyzin, *Applications of Littlestone Dimension to Query Learning and to Compression*, MFCS 2024, article 42, DOI:10.4230/LIPIcs.MFCS.2024.42 (2024-08-23).
4. M. Barnabei, F. Bonetti, S. Elizalde, and M. Silimbani, *Descent sets on 321-avoiding involutions and hook decompositions of partitions*, arXiv:1401.3011 (2014); background on the established permutation class.
