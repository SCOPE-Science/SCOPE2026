# Sharp cardinality of permutation families with one-symbol repair

## Finding

Let \(S_n\) be the permutations of the alphabet \(Q=\{0,\ldots,n-1\}\). A family \(\mathcal C\subseteq S_n\) has **fixed-observer symbol locality one** if for each coordinate \(i\) there are a different coordinate \(j(i)\ne i\) and a function \(\varphi_i:Q\to Q\), both independent of the stored permutation, satisfying \(\pi_i=\varphi_i(\pi_{j(i)})\) for every \(\pi\in\mathcal C\).

**Theorem.** For every integer \(m\ge1\), the maximum family sizes are
\[
A(2m,1)=2^m m!,\qquad A(2m+1,1)=(2m+1)2^{m-1}(m-1)!.
\]
The odd-length extremum is \((2m+1)(2m-2)!!\), with the even double factorial interpreted in its usual combinatorial sense. For example \(A(3,1)=3\), \(A(5,1)=10\), \(A(7,1)=56\), and \(A(9,1)=432\). Both bounds are achieved by explicit families in which each coordinate is deterministically repaired by reading one fixed other coordinate.

The even-length equality was known; the contribution is the sharp odd-length bound and construction. The refinement matters already at \(n=5\): the earlier odd-length pair-block construction produces eight permutations, while the older general bound permits fifteen; the exact optimum is ten.

## Assumptions and scope

All alphabets are labeled finite sets, all codewords are full permutations with no repeated symbols, and no information is added to the stored one-line representation. The observer \(j(i)\) and recovery map \(\varphi_i\) are fixed for each erased position, uniformly over all codewords. The statement does not apply to adaptive selection of recovery coordinates, auxiliary storage, or locality larger than one. The case \(n=1\) is excluded because no distinct observer exists.

## Proof

**Upper bound.** Fix the recovery coordinates for an arbitrary admissible nonempty family. Draw a directed arc \(i\to j(i)\) for every coordinate. This finite functional digraph has exactly one directed cycle in each weak component; because \(j(i)\ne i\), each component contains at least two vertices. Following a cycle against its arrow directions and then moving outward along incoming trees shows that the value at any chosen cycle vertex determines every coordinate value in its component. Thus one cycle-vertex value per component uniquely determines the full codeword.

Suppose the component sizes are \(s_1,\ldots,s_t\), each at least two. If they are processed in a specified order, the first component has at most \(n\) possible values for its chosen cycle vertex. After values in the first \(r\) components have been fixed, those components occupy \(s_1+\cdots+s_r\) distinct symbols because the entire word is a permutation. The next chosen cycle vertex can take at most \(n-(s_1+\cdots+s_r)\) values. Uniqueness of extension yields the bound
\[
|\mathcal C|\le \prod_{r=1}^{t}\left(n-\sum_{k<r}s_k\right).
\]
If \(n=2m\), then \(t\le m\) and each prior component occupies at least two symbols, so the product is at most \(n(n-2)\cdots2=2^m m!\).

If \(n=2m+1\), then \(t\le m\) and at least one component has size at least three. Put that component first. For every subsequent component at least two more distinct symbols are consumed. Hence
\[
|\mathcal C|\le n(n-3)(n-5)\cdots2=(2m+1)2^{m-1}(m-1)!.
\]
When \(t<m\), append the omitted factors, which are all at least two, to obtain the same upper bound. These are injection bounds: no assumption of statistical independence of different components is made.

**Even-length construction.** For \(n=2m\), partition \(Q\) into fixed two-symbol sets \(\{0,1\},\{2,3\},\ldots,\{2m-2,2m-1\}\). Take every concatenation of these \(m\) pairs, in arbitrary block order and arbitrary internal orientation. There are exactly \(m!2^m\) distinct words. The other coordinate in the same block repairs either coordinate using the globally defined involution interchanging the two symbols in every fixed pair.

**Odd-length construction.** For \(n=2m+1\), define a permutation \(f\) of \(Q\) by the cycle \(0\mapsto1\mapsto2\mapsto0\) and by transposing \(3\) with \(4\), \(5\) with \(6\), and so on, through \(2m-1\) with \(2m\). Define \(g(y)=f(y)\) on \(\{0,1,2\}\), and \(g(y)=0\) otherwise. Define an involution \(h\) fixing \(0\) and interchanging \(1\) with \(2\), \(3\) with \(4\), and so on.

For every \(r\in Q\), begin a word with the three symbols
\[
(r,f(r),g(f(r))).
\]
When \(r\in\{0,1,2\}\), these are precisely the triple \(\{0,1,2\}\). When \(r\notin\{0,1,2\}\), they consist of \(0\) and the complete \(f\)-pair containing \(r\). In either case, the unused \(2m-2\) symbols partition into exactly \(m-1\) of the fixed \(h\)-pairs \(\{1,2\},\{3,4\},\ldots,\{2m-1,2m\}\). Append all these unused pairs in arbitrary order and internal orientation. Every resulting word is a permutation; the first symbol identifies \(r\), and the ordered oriented suffix identifies the remaining choices, so there are exactly \(n2^{m-1}(m-1)!\) distinct words.

The three prefix coordinates are repaired, respectively, from coordinates two, one, and two by \(f^{-1}\), \(f\), and \(g\), using one-based indexing. Each suffix coordinate is repaired from the other coordinate of its fixed adjacent suffix pair by \(h\). All observer positions and repair maps are fixed independently of \(r\) and of the pair ordering. This gives locality one and matches the upper bound for every \(m\ge1\).

## Verification

The accompanying standalone programs `verify.py` and `verify_n5.py` were executed from their actual embedded source copies. The first constructs and checks every described codeword and every prescribed one-coordinate repair for each \(2\le n\le11\), obtaining the exact theoretical cardinalities with no duplicates. The second independently enumerates all \(4^5=1024\) fixed-observer patterns for \(n=5\), reduces them to thirteen coordinate-relabeling orbits, and certifies by exact compatibility-graph clique exclusion that eleven codewords are impossible. The theorem for arbitrary length is proved by the component counting and constructions above; finite experiments do not prove the infinite claim.

## Relationship to prior work

Raviv, Yaakobi, and Médard introduced this precise combinatorial, nonadaptive locality model. Their January 2016 full preprint (Theorem 2 and Section 4.2) proves a double-factorial upper bound, with a pair-concatenation construction obtaining equality when the length is even. The full-preprint discussion of odd lengths instead identifies a pair-concatenation family with \((n-1)!!\) codewords. For odd \(n\ge5\), neither that construction nor the general \(n!!\) upper bound implies the sharp intermediate value obtained here. In fact, the preprint's unqualified equality sentence relies on a construction requiring block length two to divide \(n\); the odd case requires a separate argument and construction.

The 2018 journal version has the same authors and title, but its entire full text was not obtained; only published metadata and abstract could be inspected. It may contain additional results beyond the accessible 2016 full preprint. A prior independent odd-length equality theorem in that edition or in unindexed literature cannot be ruled out by the available evidence.

## Limitations

This is a sharp extremal cardinality result for **fixed-observer** locality one; it is not an enumeration or isomorphism classification of every optimal family. It does not solve locality two or higher, repair using adaptively chosen coordinates, error tolerance, or encoded-storage variants. The 2018 full-text access limitation and possible unindexed prior overlap remain bibliographic risks, not gaps in the stated elementary proof.

## References

1. N. Raviv, E. Yaakobi, M. Médard, *Coding for Locality in Reconstructing Permutations*, arXiv:1601.04504, first posted 18 January 2016. Full initial manuscript accessible from the author-uploaded version at https://www.researchgate.net/publication/291229464_Coding_for_Locality_in_Reconstructing_Permutations ; conference PDF at https://arxiv.org/pdf/1601.04504 .
2. N. Raviv, E. Yaakobi, M. Médard, *Coding for locality in reconstructing permutations*, Designs, Codes and Cryptography 86 (2018), 387–418, https://doi.org/10.1007/s10623-017-0378-9 .
