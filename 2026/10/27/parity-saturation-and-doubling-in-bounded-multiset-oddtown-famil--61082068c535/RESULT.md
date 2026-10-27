# Parity saturation and doubling in bounded-multiset Oddtown families

## Finding

For positive integers \(m,n\), define \(O_m(n)\) to be the greatest possible size of a family \(\mathcal F\subseteq\{0,1,\ldots,m\}^n\) satisfying
\[
\sum_{i=1}^{n}x_i\equiv1\pmod 2\qquad(x\in\mathcal F),
\]
and
\[
I(x,y):=\sum_{i=1}^{n}\min\{x_i,y_i\}\equiv0\pmod2
\qquad(x,y\in\mathcal F,\ x\ne y).
\]
The following is a single structural and extremal statement.

**Theorem.** For all positive integers \(m,n\),
\[
O_m(n)\le\min\{mn,2^{n-1}\}.
\]
For every \(m\ge3\), the first sharp parity-pattern cases are
\[
\boxed{O_m(3)=4,\qquad O_m(4)=8.}
\]
For \(m=3,n=4\), there are exactly six labelled maximizing families, forming one orbit under permutations of the four coordinates. For every \(m\ge3\) and \(n=4a+r\ge4\), where \(a\ge1\) and \(0\le r\le3\),
\[
\boxed{O_m(n)\ge 8a+b_r,\qquad(b_0,b_1,b_2,b_3)=(0,1,2,4).}
\]
In particular \(O_m(n)\ge 2n-2\) for every \(n\ge4\). For fixed multiplicity cap three this gives the asymptotic bracket \(2n-2\le O_3(n)\le 3n\), whereas the classical one-bounded Oddtown maximum is \(n\).

## Assumptions and scope

A vector \(x\) denotes the multiplicities of a multiset on a labelled \(n\)-element ground set, with multiplicity of each element at most \(m\). Its cardinality is the sum of its coordinates. Intersection multiplicity is the coordinatewise minimum, not the product and not the intersection of supports. The pairwise condition is imposed only on distinct family members; the required odd diagonal is given separately. The count of six uses labelled coordinate positions, considers families as unordered collections, and pertains only to the exact cap \(m=3\).

## Proof

**Parity-pattern upper bound.** Associate with \(x\) its parity pattern \(p(x)=(x_i\bmod2)_{i=1}^n\). Each member has odd-weight pattern. If two different members \(x,y\) have the same parity pattern, then for each coordinate \(\min\{x_i,y_i\}\) has that same parity: the minimum of two even integers is even, and the minimum of two odd integers is odd. Hence \(I(x,y)\equiv\sum_i x_i\equiv1\pmod2\), a contradiction. Thus at most one member occupies each of the \(2^{n-1}\) odd-weight parity patterns.

**Linear-algebra upper bound.** Represent \(x\) by a binary vector on \([n]\times[m]\) that selects the first \(x_i\) positions in block \(i\). Its mod-two dot product with the representation of \(y\) is \(I(x,y)\bmod2\). The vectors representing all members therefore have identity Gram matrix over \(\mathbb F_2\): the diagonal entries are one and all off-diagonal entries zero. They are linearly independent in \(\mathbb F_2^{mn}\), giving \(|\mathcal F|\le mn\).

**Sharp small cases.** The following four vectors form a valid family at \(m=3,n=3\):

```
(0,2,1)  (1,2,0)  (2,1,2)  (3,1,1)
```

The following eight vectors form a valid family at \(m=3,n=4\):

```
(0,1,2,2)  (1,0,2,2)  (1,2,1,3)  (1,3,1,2)
(2,1,3,1)  (2,2,0,1)  (2,2,1,0)  (3,1,2,1)
```

Their diagonal sums are odd, and every distinct pair has even coordinatewise-minimum sum; the arithmetic can be checked directly or using the attached independent verifier. The first family meets the upper bound \(2^{3-1}=4\), and the second meets \(2^{4-1}=8\). Increasing the cap beyond three retains both witnesses, while the parity upper bound is cap-independent. This proves both exact values for all \(m\ge3\).

**Exhaustive classification for exactly four coordinates and cap three.** A family of size eight must contain one vector from each odd-weight parity-pattern class. There are eight such classes, each with exactly sixteen vectors from \(\{0,1,2,3\}^4\). The exhaustive recurrence in `verify.py` selects a parity class, tests each candidate compatible with all currently chosen vectors, and recurses on the remaining classes. It discards a branch only if one remaining class has no compatible candidate. Every possible full family has a unique branch in this search, so the enumeration is complete rather than a sample. It returns **six** families after **437** visited recursion nodes. The twenty-four coordinate permutations of the displayed eight-vector witness produce exactly six distinct families, and these are exactly the six found by the exhaustive recurrence. A second independent maximum-clique search on all odd vectors confirms that eight is the exact largest clique size. Thus there is one coordinate-permutation orbit of labelled maximizers. This finite conclusion is certified by the explicitly given exhaustive algorithm; it is not extrapolated to other \(m\) or \(n\).

**Disjoint-support amplification.** If \(\mathcal F\) and \(\mathcal G\) are valid families on disjoint coordinate blocks, form the union of the two families embedded by padding zeroes in the complementary block. Each embedded member retains odd total cardinality. Distinct members in the same block retain their even intersections, while members from different blocks have intersection cardinality zero. Therefore the resulting family is valid and has \(|\mathcal F|+|\mathcal G|\) members. In addition to the four- and eight-member witnesses, a one-coordinate block has the one-element family \(\{(1)\}\), and a two-coordinate block has the two-element family \(\{(1,0),(0,1)\}\). For \(n=4a+r\) with \(a\ge1\), take \(a\) copies of the eight-member four-coordinate witness and one residual block of size \(r\), using a four-member three-coordinate witness when \(r=3\). This has precisely \(8a+b_r\) members. Its least excess over \(2n-2\) is zero, proving the stated bounds.

## Verification

Run `python3 verify.py` from the same directory as this document. It requires only the Python standard library. The checker tests every pair in the explicit witnesses, performs two differently organized exhaustive finite searches for small caps, enumerates all eight-pattern extremizers by deterministic backtracking, checks the complete orbit, and checks direct-sum constructions through \(n=80\). The observed output was:

```
VERIFY_OK exact_graph_cases=6 optimal_four_coordinate_families=6 group_dfs_nodes=437 direct_sum_orders=77 max={(3, 1): 3, (3, 2): 3, (3, 3): 4, (4, 1): 4, (4, 2): 6, (4, 3): 8}
```

The unbounded assertions are proved above and do not follow from the finite tests.

## Relationship to prior work

Banerjee and Dewan determine the extremal **Eventown** problem for bounded multisets, requiring *even* self-cardinality, and characterize the extremal families. The present Oddtown problem requires *odd* self-cardinality with even distinct intersections; the Eventown maximum and classification do not imply this theorem. The traditional Berlekamp Oddtown bound for ordinary sets is recovered at cap one; its binary-embedding argument supplies the standard general linear upper bound here. An existing two-bounded analysis gives the smaller sharp value \(O_2(4)=6\), which is not claimed as new. The current contribution is parity-bound saturation at cap three, a complete small optimal-family orbit, and the resulting infinite-family size amplification. Shankar's lattice-path results involve common path edges rather than coordinatewise-minimum multiset intersections. The precise comparison and remaining priority risks are reported in the accompanying review.

## Limitations

For \(n>4\), the exact maximum \(O_3(n)\) is not determined; the construction supplies a lower bound only. The six-extremizer classification is restricted to \(m=3,n=4\), and no classification is claimed for larger caps. For \(m\ge3\), the values at \(n=3,4\) are exact, but the general lower bound need not be sharp. The finite verifier neither certifies unexamined parameters nor provides independent peer review. Historical-priority searches cannot establish absolute uniqueness.

## References

1. A. Banerjee and A. Dewan, *An Eventown Result for Multisets*, arXiv:2610.21636v1 (first public version 2026-10-15), https://arxiv.org/html/2610.21636v1.
2. E. R. Berlekamp, *On subsets with intersections of even cardinality*, Canadian Mathematical Bulletin 12 (1969), 471–474.
3. U. Shankar, *Oddtown and eventown theorems for lattice paths*, arXiv:2607.23117v1 (2026).
4. B. Sudakov and P. Vieira, *Two remarks on Eventown and Oddtown problems*, SIAM Journal on Discrete Mathematics 32 (2018), 280–295.
