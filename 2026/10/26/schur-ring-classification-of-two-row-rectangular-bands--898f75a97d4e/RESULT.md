# Schur-ring classification of two-row rectangular bands

## Finding

For every integer \(m\geq 1\), let \(R_{2,m}=\{0,1\}\times[m]\), with multiplication \((i,j)(k,l)=(i,l)\). A **semigroup Schur partition** is a partition \(\mathcal P\) of \(R_{2,m}\) such that the rational span of its block sums in \(\mathbb Q[R_{2,m}]\) is closed under multiplication; a semigroup Schur ring is the corresponding subalgebra.

**Classification and automorphic realization.** Every such partition is uniquely of exactly one of the following forms.

1. **Separated rows:** choose an ordinary set partition \(\pi\) of \([m]\); the blocks are \(\{0\}\times C\) and \(\{1\}\times C\), for each \(C\in\pi\).
2. **Balanced rows:** choose an ordinary set partition \(\pi\) of \([m]\); independently, for every \(C\in\pi\), choose either (a) the single block \(\{0,1\}\times C\), or (b), only when \(|C|\) is even, an unordered pair of complementary blocks \(X_C,Y_C\). In (b), each column has one point in each block, and each block has exactly \(|C|/2\) points in each row. Such pairs are determined by a subset \(A\subseteq C\) of size \(|C|/2\):
   \[
   X_C=(\{0\}\times A)\cup(\{1\}\times(C\setminus A)),\qquad
   Y_C=(\{0\}\times(C\setminus A))\cup(\{1\}\times A),
   \]
   with \(A\) and \(C\setminus A\) giving the same unordered pair.

These descriptions are nonoverlapping and produce every semigroup Schur partition. **Every partition in the classification is an orbit partition of a subgroup of \(\operatorname{Aut}(R_{2,m})\cong S_2\times S_m\)**; thus every semigroup Schur ring of this band is automorphic.

Let \(B_m\) be the \(m\)th Bell number and define
\[
 b_k=1+\begin{cases}\frac12\binom{k}{k/2},&k\text{ even},\\0,&k\text{ odd}.\end{cases}
 \qquad W_m=\sum_{\pi\vdash[m]}\prod_{C\in\pi}b_{|C|}.
\]
Then the complete count and the count of **non-direct-product** Schur rings are, respectively,
\[
 \boxed{\Omega(R_{2,m})=B_m+W_m},\qquad
 \boxed{\Omega(R_{2,m})-2B_m=W_m-B_m}.
\]
Writing \(I_0(2z)=\sum_{j\ge0}z^{2j}/(j!)^2\), the exponential generating function is
\[
 \boxed{\sum_{m\ge1}\Omega(R_{2,m})\frac{z^m}{m!}
 =\exp(e^z-1)\left[1+\exp\left(\frac{I_0(2z)-1}{2}\right)\right]-2.}
\]
In increasing order \(m=1,2,3,4,5,6\), the totals are \(2,5,13,48,184,881\), and the non-direct-product counts are \(0,1,3,18,80,475\).

## Assumptions and scope

The semigroup is finite and rectangular, with **exactly two** nonempty left-coordinate classes and \(m\) nonempty right-coordinate classes. All partitions are partitions of the **labeled** underlying set; an isomorphism-class quotient is not being taken. The Schur condition is the multiplication-closure condition alone, as in the semigroup definition, without imposing group inversion or a separate identity axiom. The ground coefficient field is \(\mathbb Q\); the proof also holds in characteristic zero. All formulas are exact for every positive integer \(m\).

## Proof

**Step 1: the profile lemma.** For each partition block \(X\in\mathcal P\), set
\[
 r_X(i)=\#\{j:(i,j)\in X\},\qquad
 c_X(j)=\#\{i:(i,j)\in X\}.
\]
Write \([X]=\sum_{x\in X}x\) in the semigroup algebra. The coefficient of \((i,j)\) in \([X][Y]\) is exactly \(r_X(i)c_Y(j)\), since a product lands at \((i,j)\) precisely when its left factor has first coordinate \(i\) and its right factor has second coordinate \(j\). Hence multiplication closure means these products are constant on each block \(Z\) for every \(X,Y\).

If \((i,j),(i',j')\in Z\), summing these equalities over all blocks \(Y\), using \(\sum_Yc_Y(j)=2\), gives \(r_X(i)=r_X(i')\) for every \(X\). Summing instead over all \(X\), using \(\sum_Xr_X(i)=m\), gives \(c_Y(j)=c_Y(j')\) for every \(Y\). Conversely, if each block is contained in the Cartesian product of one fiber of the row-profile map \(i\mapsto (r_X(i))_X\) and one fiber of the column-profile map \(j\mapsto(c_X(j))_X\), then all coefficients \(r_X(i)c_Y(j)\) are constant on every block, so closure holds. This proves the necessary-and-sufficient profile criterion without any enumerative assumption.

**Step 2: distinct row profiles.** If the two row profiles differ, the criterion prohibits any block from containing both rows. Thus the blocks define two partitions \(\pi_0,\pi_1\) of \([m]\). If \(C\) is a block of \(\pi_0\), its columns have identical column profiles; membership in each block of \(\pi_1\) must therefore be constant over \(C\). Hence every \(C\in\pi_0\) is contained in some block of \(\pi_1\). The reverse argument proves the converse containment, so \(\pi_0=\pi_1\). Conversely, these paired-row blocks satisfy the profile criterion. There are exactly \(B_m\) of them.

**Step 3: equal row profiles.** In this case every primitive block has as many points in row zero as in row one. Partition the columns into their common column-profile fibers \(C\). The profile criterion implies every primitive block is contained in the two-row strip over a single fiber. At every column within \(C\), the multiset of blocks occupied by the two points is identical. Therefore it is either the same block twice, forcing one full-strip block over \(C\), or two distinct blocks once each, forcing exactly two complementary one-point-per-column blocks. In the latter case, equality of row counts in each block forces \(|C|\) to be even and one of the two blocks to choose row zero on precisely half the columns. There are \(\binom{|C|}{|C|/2}/2\) unordered choices. Conversely all these constructions have equal row profiles and satisfy the profile criterion. Distinct fibers have disjoint block sets, so the fiber set partition is recovered uniquely from the resulting Schur partition. Thus there are exactly \(W_m\) balanced partitions.

**Step 4: explicit automorphic subgroups.** An automorphism of \(R_{2,m}\) is an independent permutation of the two rows and of the \(m\) columns. In the separated-row case, take the product of full symmetric groups on each column block \(C\), acting identically in the two rows. Its orbits are exactly the prescribed row blocks.

In the balanced case, within each full-strip fiber \(C\) include the whole column group \(S_C\). Within each split fiber \(C=A\sqcup B\), include \(S_A\times S_B\) as column permutations. Finally choose, simultaneously across all split fibers, a column permutation exchanging \(A\) and \(B\) bijectively in each fiber (and fixing the columns of full-strip fibers); compose this permutation with the swap of the two rows. Every generator preserves each prescribed primitive block. The column-permutation generators act transitively within each half of a split block, while the combined row swap exchanges those halves. The same generators act transitively on each full-strip block. Therefore their subgroup has exactly the prescribed orbits. This proves automorphic realization in all cases.

**Step 5: enumeration and generating function.** Each fiber of size \(k\) in the balanced case has exactly \(b_k\) independently available states, so summing over set partitions gives \(W_m\). The exponential formula for labeled set partitions gives
\[
 \sum_{m\ge0}W_m\frac{z^m}{m!}
 =\exp\!\left(\sum_{k\ge1}b_k\frac{z^k}{k!}\right)
 =\exp(e^z-1)\exp\!\left(\frac12\sum_{j\ge1}\frac{z^{2j}}{(j!)^2}\right).
\]
Adding the Bell-number series and removing the two formal empty-size contributions gives the displayed generating function for \(m\ge1\). Direct product Schur rings come from the two partitions of the two-point left-zero semigroup and each of the \(B_m\) partitions of the \(m\)-point right-zero semigroup: exactly \(2B_m\). The balanced full-strip choices account for precisely \(B_m\) of these, and the separated-row choices for the other \(B_m\), proving the non-direct-product formula. The cases are disjoint for \(m\ge1\).

## Verification

Run `python3 verify.py` using Python 3 standard library only. It explicitly enumerates every set partition on \(2m\) labeled points through \(m=5\). For \(m\le4\), it directly multiplies every pair of primitive block sums and checks coefficient constancy; for \(m=5\), it checks the independently implemented profile criterion. For all five values, it checks the separated/balanced counts and constructs subgroup generators whose orbit partitions exactly match each accepted Schur partition. The expected terminal line is `VERIFY_OK` and the checked totals are \(2,5,13,48,184\). Finite checks are not used to infer the universal classification.

## Relationship to prior work

Marrow and Misseldine [1] define semigroup Schur rings, show that automorphism orbit partitions and direct products supply Schur rings (Sections 2.1–2.2), and state the lower bound \(B_nB_m\) for rectangular bands. Their finite enumeration lists five Schur rings for the \(2\)-by-\(2\) band and thirteen for the \(2\)-by-\(3\) band (up to taking the opposite semigroup). The present classification proves the exact count and automorphic realization for **all** \(2\)-by-\(m\) bands; the two cited small counts agree. The source's general automorphic construction does not imply that every Schur partition is automorphic, and its direct-product lower bound does not determine the extra balanced-split partitions. Background work on group Schur rings and group double-coset algebras treats different multiplication laws [2,3].

## Limitations

This is not a classification of Schur rings over all rectangular bands: with three or more rows, a column fiber may carry several nontrivial block-incidence patterns, and the two-row proof no longer reduces to complementary binary splits. No unlabeled isomorphism-class count or asymptotic growth estimate for \(\Omega(R_{2,m})\) is asserted. Originality was compared with accessible indexed literature; an equivalent independent classification in unindexed work cannot be categorically excluded. The complete general argument is a written proof, not a formal-machine proof or independent audit.

## References

1. Joseph E. Marrow and Andrew Misseldine, *On Schur Rings Over Semigroups*, arXiv:2601.09940 (first posted 14 January 2026), https://arxiv.org/abs/2601.09940. Especially Sections 2.1–2.2, 5.4, 5.6 and 6.
2. Andrew Misseldine, *Enumeration Techniques on Cyclic Schur Rings*, arXiv:2112.03422 (2021), https://arxiv.org/abs/2112.03422. Group-only enumeration background.
3. Mahir Bilen Can and Julianne Rainbolt, *Double coset Schur rings and diagonal subgroups*, International Electronic Journal of Algebra (online 31 August 2026), https://doi.org/10.24330/ieja.2029225. Group-triple and double-coset context, not rectangular-band semigroup rings.
