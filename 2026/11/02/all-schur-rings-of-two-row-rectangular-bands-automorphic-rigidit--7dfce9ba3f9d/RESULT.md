# All Schur rings of two-row rectangular bands: automorphic rigidity and an exact enumerator

## Finding
Let \(m\ge1\), and equip \(B_{2,m}=\{0,1\}\times[m]\) with the rectangular-band multiplication
\[
(i,j)(k,\ell)=(i,\ell).
\]
A **semigroup Schur ring** is the \(\mathbb Q\)-linear span of the sums of the classes of a partition \(\mathcal P\) of \(B_{2,m}\), when this span is closed under multiplication in the semigroup algebra. The definition does not impose extra identity or inversion axioms.

**Classification.** Every such partition has exactly one of the following forms.

1. **Separated rows.** Choose a set partition \(\Pi\) of \([m]\). For each \(C\in\Pi\), the two classes \(\{0\}\times C\) and \(\{1\}\times C\) are separate. There are \(\operatorname{Bell}(m)\) partitions of this form.
2. **Balanced rows.** Partition \([m]\) into column components. Each component \(C\) is independently either **monochromatic**, giving the one class \(\{0,1\}\times C\), or **paired**, in which case \(|C|=2k\ge2\) is even and an unordered equipartition \(C=C_+\sqcup C_-\), \(|C_+|=|C_-|=k\), gives exactly the two classes
\[
(\{0\}\times C_+)\cup(\{1\}\times C_-),\qquad
(\{0\}\times C_-)\cup(\{1\}\times C_+).
\]
There are no other classes or identifications.

**Automorphic realization.** Every semigroup Schur ring of \(B_{2,m}\) is the orbit algebra of a subgroup of \(\operatorname{Aut}(B_{2,m})\cong S_2\times S_m\). In particular, non-direct-product Schur rings do occur, but none is nonautomorphic.

Define \(w_s=1\) for odd positive \(s\) and
\[
w_{2k}=1+\frac12\binom{2k}{k}\quad (k\ge1).
\]
Writing \(\Pi\vdash[m]\) for a set partition of the labeled column set, the exact number of semigroup Schur rings is
\[
\boxed{\Omega_m=\operatorname{Bell}(m)+\sum_{\Pi\vdash[m]}\prod_{C\in\Pi}w_{|C|}.}
\]
Its exponential generating function, with the formal extension \(\Omega_0=2\), is
\[
\boxed{\sum_{m\ge0}\Omega_m\frac{z^m}{m!}
=\exp(e^z-1)\left[1+\exp\left(\frac12\sum_{k\ge1}\frac{z^{2k}}{(k!)^2}\right)\right].}
\]
The values for \(m=1,\ldots,9\) are
\[
2,\ 5,\ 13,\ 48,\ 184,\ 881,\ 4386,\ 25549,\ 154863.
\]

## Assumptions and scope
All partitions are of the **labeled** \(2m\)-element semigroup. Two partitions are counted separately if their blocks differ as subsets, even when an automorphism relates them. Blocks themselves have no labels. The coefficient field for the Schur algebra is \(\mathbb Q\); the same proof works over any field of characteristic zero. An automorphic Schur ring means precisely an orbit partition under a subgroup of the semigroup automorphism group, not necessarily a direct product of Schur rings on the two factors. The theorem covers all \(m\ge1\) and does not claim a comparable classification for three or more rows.

## Proof
**1. Coefficient criterion.** Let \(X\) be a block and set
\[
r_X(i)=\#\{j:(i,j)\in X\},\qquad c_X(j)=\#\{i:(i,j)\in X\}.
\]
Write \(\underline X=\sum_{x\in X}x\) in the semigroup algebra. Direct multiplication yields the exact coefficient identity
\[
[ (i,j)]\,\underline X\underline Y=r_X(i)c_Y(j)
\]
for every pair of blocks \(X,Y\), where the left side means the coefficient of the basis element \((i,j)\). Thus the block sums span a subalgebra if and only if, whenever \((i,j)\) and \((i',j')\) belong to one block, the products \(r_X(i)c_Y(j)\) and \(r_X(i')c_Y(j')\) agree for all \(X,Y\).

Sum these equalities over every block \(Y\), using \(\sum_Yc_Y(j)=2\), to obtain \(r_X(i)=r_X(i')\) for each \(X\). Summing instead over every \(X\), using \(\sum_Xr_X(i)=m\), gives \(c_Y(j)=c_Y(j')\) for every \(Y\). Conversely, equality of all these row and column profiles makes every product coefficient equal. Therefore **two cells in a common class must have identical complete row-degree and column-degree profiles**, and this condition is also sufficient.

**2. Separated rows.** If some block \(X\) has \(r_X(0)\ne r_X(1)\), the profile criterion forbids any class from meeting both rows. Since all blocks are row-contained, the column-degree profile of a column is simply the ordered pair of class names occupying that column. If two cells in one row are equivalent, their columns have identical profiles, so their opposite-row cells are also equivalent. The converse holds by exchanging the rows. Hence the two induced partitions of the columns are identical. This is precisely family 1. Conversely, its classes evidently satisfy the profile criterion.

**3. Balanced rows.** Otherwise \(r_X(0)=r_X(1)\) for every block. For each column, the column-degree profile records the unordered multiset of its two class names. If a class \(a\) occurs in two columns, the profile criterion forces their unordered class pairs to be the same. Therefore each class name has a unique partner \(b\), possibly \(b=a\), and the distinct pairs \(\{a,b\}\) partition the column set into components. In a self-paired component \(a=b\), both cells of every column lie in the unique class \(a\). For two different names \(a\ne b\), each column has one cell of each name. The row-degree equality for \(a\) forces exactly half the columns to have \(a\) in row 0 and half in row 1; hence the component has even cardinality and supplies the two classes displayed in family 2. Conversely, all blocks in family 2 have equal row-degree profiles, and columns meeting the same class have identical unordered pairs of class names, so the profile criterion proves closure. The two families are disjoint and exhaustive.

**4. Every partition is automorphic.** A permutation of the two rows and an independent permutation of the columns together form an automorphism of the rectangular band. For family 1, take the subgroup acting trivially on the rows and independently as the full symmetric group on each column block \(C\). Its orbits are exactly the specified two classes for each \(C\).

For family 2, first take the column-permutation subgroup that acts as the full symmetric group on each monochromatic component and independently as the full symmetric groups on \(C_+\) and \(C_-\) inside every paired component. Add one automorphism that swaps the two rows, fixes columns in each monochromatic component, and exchanges \(C_+\) with \(C_-\) through a chosen bijection in every paired component. The generated subgroup has one orbit on each monochromatic component and two orbits, exactly the specified classes, on each paired component. No orbit mixes different components. This proves the automorphic assertion.

**5. Enumeration.** In a column component of positive size \(s\), the monochromatic configuration contributes one choice. A paired configuration exists only for \(s=2k\), with \(\binom{2k}{k}/2\) unordered equipartitions. Thus the component weight is \(w_s\), and the labeled set-partition sum counts family 2 without repetitions. Family 1 contributes \(\operatorname{Bell}(m)\). The exponential formula for labeled assemblies of nonempty components gives
\[
\sum_{m\ge0}\left(\sum_{\Pi\vdash[m]}\prod_{C\in\Pi}w_{|C|}\right)\frac{z^m}{m!}
=\exp\left(\sum_{s\ge1}w_s\frac{z^s}{s!}\right)
=\exp\left(e^z-1+\frac12\sum_{k\ge1}\frac{z^{2k}}{(k!)^2}\right),
\]
which, after adding the Bell-number generating function, is the claimed formula. The convention at \(m=0\) is only a generating-function extension, not a zero-column semigroup.

## Verification
The standalone file `CHECK.py` uses exact integers and no external packages. Its first route tests every restricted-growth-string set partition of the \(2m\) cells directly against all products of class sums for \(1\le m\le4\). A logically separate route computes and compares complete row/column profiles through \(m=5\), visiting all \(115975\) set partitions of a ten-element set. Every accepted partition is also checked to be the orbit partition of explicitly generated row/column automorphisms. The independently calculated weighted-Bell recurrence agrees with the exact enumerations. The output `CHECK_output.txt` records family counts \((1,1), (2,3), (5,8), (15,33), (52,132)\) for \(m=1,\ldots,5\), and ends with `VERIFY_OK`. These finite enumerations corroborate but do not replace the all-\(m\) proof above.

## Relationship to prior work
Marrow and Misseldine, *On Schur Rings Over Semigroups*, arXiv:2601.09940 (initially public January 14, 2026), define the semigroup Schur-ring notion, show automorphic partitions are Schur rings (Section 2.1), and give a general direct-product construction. Their Section 2.2 explicitly supplies only the lower bound \(\operatorname{Bell}(2)\operatorname{Bell}(m)\) for these rectangular bands and warns that not all Schur rings are direct products. Section 5 records the values 5 for the \(2\times2\) case and 13 for the \(2\times3\) case. These finite counts and the general automorphic construction are prior work; the claim here is the exhaustive two-row classification, the all-\(m\) weighted enumerator, and automorphic completeness. The \(2\times2\) diagonal/off-diagonal checkerboard partition is a non-direct-product example, consistent with the paper's warning.

## Limitations
This theorem concerns **two-row rectangular bands** and semigroup Schur rings under the block-sum/subalgebra definition. No statement is made about arbitrary rectangular bands, classification up to automorphism, or positive-characteristic coefficient fields. The full literature is not exhaustively indexed, and another treatment under equivalent terminology might imply the result. Existing published small-order counts are reproduced rather than claimed as new. Independent mathematical review has not been performed.

## References
1. J. E. Marrow and A. Misseldine, *On Schur Rings Over Semigroups*, arXiv:2601.09940, initial submission January 14, 2026, https://arxiv.org/abs/2601.09940 ; readable full text https://arxiv.org/html/2601.09940 . Relevant sections: 1 (definition), 2.1–2.2 (automorphic/direct-product constructions), 5.4 and 5.6 (order-four and order-six counts), 6 (open classification context).
2. J. E. Marrow and A. Misseldine, same work, Section 2.2, specific comparison: the paper states that \(\operatorname{Bell}(n)\operatorname{Bell}(m)\) direct-product Schur rings exist on an \(n\times m\) rectangular band, and that other Schur rings can occur. This is a single source repeated here to pinpoint the closest prior assertion, not an independent publication.
