# One-query exact hardness of one-types over height-two random-poset parameters

## Finding

Let \(\mathbb D\) be the countable homogeneous universal partial order. For a finite induced parameter poset \(P\), let \(c(P)\) count the complete nonalgebraic one-types over its individually named elements. Given a bipartite graph \(G=(A\sqcup B,E)\) with \(|A|=a\ge1\), \(|B|=b\ge1\), write \(P_G\) for the poset on \(A\sqcup B\) with \(x<y\) exactly for \(x\in A,y\in B,xy\in E\). Let \(i(G)\) count all independent vertex sets, including the empty set. Set \(k=a+b\) and form \(G^+\) by adding \(k\) isolated vertices to \(A\). Then
\[
i(G)=\left\lfloor\frac{c(P_{G^+})+1}{2^{k+1}}\right\rfloor.
\]
With an extra disjoint edge if necessary, this gives a polynomial-time reduction using **one** oracle query to \(c\) at height **exactly two**. Thus exact evaluation of \(c\) on height-two posets is \(\#\mathrm P\)-complete under polynomial-time Turing reductions. The same result holds for the total number of one-types, since its algebraic contribution is \(|P|\).

The height-two identity used in the proof is prior; the contribution is the isolated-side padding and exact extraction from a single absolute type count under the height promise.

## Assumptions and scope

The finite strict order is explicitly given. Height is measured in vertices, so height exactly two requires a strict comparability and forbids a three-element chain. The graph bipartition is specified, and isolated vertices are allowed. Counts and division are exact. On a height-one antichain of size \(n\), \(c(P)=2^{n+1}-1\) by the extension criterion below.

## Proof

**Prior counting identity.** A nonalgebraic type corresponds to a one-point extension with strict lower set \(L\) and upper set \(U\). The condition is that \(L\) is a downset, \(U\) is an upset and every \(l\in L\) satisfies \(l<u\) for every \(u\in U\). In particular, \(L\) and \(U\) are disjoint. The extension property realizes each such pair, and homogeneity puts any two realizations in the same orbit over the named parameters, so these are complete types.

The known identity (equation (3) of [2]) is
\[
c(P_G)=2i(G)+i(\overline G^{\rm bip})-2^a-2^b,
\]
where the complement is taken only across the specified bipartition. Indeed, when one of \(L,U\) is empty, their options contribute \(2i(G)-1\): downsets and upsets are in bijection with antichains, which here are independent sets of \(G\). When both sets are nonempty, the condition forces \(L\subseteq A,U\subseteq B\) with all cross pairs in \(E\); those pairs automatically meet the closure conditions. They are exactly the independent sets of \(\overline G^{\rm bip}\) that meet both sides, numbering \(i(\overline G^{\rm bip})-2^a-2^b+1\).

**One-query amplification.** Write \(H=\overline G^{\rm bip}\). Then \(i(G^+)=2^k i(G)\), whereas each new vertex is adjacent to all of \(B\) in the bipartite complement. Independent sets in that complement using no new vertex contribute \(i(H)\); those using at least one contribute \((2^k-1)2^a\), since then no member of \(B\) is allowed. The prior identity gives
\[
c(P_{G^+})=2^{k+1}i(G)+\Delta,\qquad \Delta=i(H)-2^a-2^b.
\]
The sets lying entirely on one side give \(i(H)\ge 2^a+2^b-1\); the bound \(i(H)\le 2^{a+b}\) gives \(\Delta<2^k\). Hence \(0\le\Delta+1<2^{k+1}\), proving the asserted floor extraction.

**Height and complexity.** Exact counting of independent sets in bipartite graphs is \(\#\mathrm P\)-complete under polynomial-time Turing reductions [3]. Adjoining a disjoint single edge, if required, multiplies its count by three, gives two nonempty sides, and ensures a comparability that persists after isolated padding. The size of the resulting poset and the bit lengths of all counts are polynomial in the input size. Membership in \(\#\mathrm P\) follows by guessing exactly one status per parameter (below, above, incomparable) and checking the extension criterion in polynomial time, with one accepting certificate per type. An additional tagged choice of an individual parameter counts the algebraic types if desired. For an antichain, the criterion allows only the cases with at least one empty set; there are \(2^{n+1}-1\) such pairs.

## Verification and comparison

The accompanying `verify.py` compares the prior identity against direct enumeration of one-point extensions on small instances, and verifies the padding identity, floor extraction and disjoint-edge factor. `verify_output.txt` is a recorded finite run; the general claim is proved above.

The earlier unrestricted hardness result [4] counts types on posets with a greatest element by using two queries; it does not enforce height exactly two. The local hardness result [2] uses one query to a different function, a shifted difference of two absolute counts before and after adding a comparability. Neither gives the reduction above to a single absolute count. These comparisons do not establish historical priority beyond the sources examined. The construction is not asserted to preserve bounded degree or connectedness, to be parsimonious, or to imply any approximation hardness.

## References

1. I. Dolinka and D. Mašulović, *A universality result for endomorphism monoids of some ultrahomogeneous structures*, arXiv:1009.2892v1, Lemma 3.3; Proc. Edinburgh Math. Soc. 55 (2012), 635–656.
2. [Sharp one-comparability sensitivity and local counting hardness](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-sharp-one-comparability-sensitivity-and-local-counting-hardness--9c2af418ff79/RESULT.md), proof §1, equation (3), and §4.
3. S. P. Vadhan, *The Complexity of Counting in Sparse, Regular, and Planar Graphs*, SIAM J. Comput. 31 (2001), 398–427, DOI: 10.1137/S0097539797321602.
4. [Finite-parameter 1-type counting in the random poset is #P-complete](https://github.com/Resultary/2026/blob/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1/RESULT.md).
