# All Schur partitions of two-row rectangular bands are automorphic

## Finding
For each integer \(m\ge1\), let the rectangular band \(B_m=\{0,1\}\times[m]\), where \([m]=\{1,\ldots,m\}\), have multiplication \((i,j)(k,l)=(i,l)\). A **Schur partition** is a set partition \(\mathcal P\) of \(B_m\) for which the rational vector space spanned by its block sums \(\underline X=\sum_{x\in X}x\) is closed under multiplication in the semigroup algebra \(\mathbb Q[B_m]\).

Every Schur partition is the orbit partition of some subgroup of \(\operatorname{Aut}(B_m)\cong S_2\times S_m\), and the following two disjoint forms exhaust them.

**Separated form.** Choose a set partition \(\Pi\) of \([m]\). For each \(J\in\Pi\), take the two blocks \(\{0\}\times J\) and \(\{1\}\times J\).

**Balanced form.** Choose a set partition \(\Pi\) of \([m]\). For each \(J\in\Pi\), independently choose either (a) its monochrome block \(\{0,1\}\times J\), or (b), only when \(|J|=2h\) is even, an unordered equipartition \(J=J_0\sqcup J_1\) with \(|J_0|=|J_1|=h\), creating the two blocks
\[
(\{0\}\times J_0)\cup(\{1\}\times J_1),\qquad
(\{0\}\times J_1)\cup(\{1\}\times J_0).
\]
The constructions are unique up to swapping the two halves of each paired group. Every balanced block has equally many elements in each row.

Write \(\mathscr B(m)\) for the \(m\)-th Bell number. The number of Schur partitions is exactly
\[
N_m=\mathscr B(m)+m![z^m]\exp\!\left(e^z-1+\frac12\sum_{h\ge1}\frac{z^{2h}}{(h!)^2}\right).
\]
For \(\(m=1,2,3,4\),5\) the values are \(2,5,13,48,184\). The number of partitions not arising as a direct product of Schur partitions on the left-zero and right-zero factors is \(N_m-2\mathscr B(m)\); the first three nonzero differences, at \(m=2,3,4\), are \(1,3,18\).

## Assumptions and scope
All partitions are partitions of the *labelled* \(2m\)-element semigroup, not partitions up to isomorphism. The coefficient ring \(\mathbb Q\) is essential to the proof's positive integer coefficient comparisons; no assertion about characteristic-dependent Schur subspaces over finite fields is made. The condition on Schur partitions requires multiplication closure only, not a multiplicative identity or an inverse condition, as in the semigroup convention of Marrow and Misseldine. The result includes \(m=1\); the first rectangular bands with both factors nontrivial have \(m\ge2\).

## Proof
**1. Exact multiplication criterion.** For a block \(X\in\mathcal P\), put \(r_X(i)=|X\cap(\{i\}\times[m])|\) and \(c_X(j)=|X\cap(\{0,1\}\times\{j\})|\). The coefficient of \((i,j)\) in \(\underline X\,\underline Y\) is
\[
r_X(i)c_Y(j),
\]
because a product equals \((i,j)\) precisely when its left factor has row \(i\) and its right factor has column \(j\). Consequently \(\mathcal P\) is Schur if and only if for all blocks \(X,Y,C\) the quantity \(r_X(i)c_Y(j)\) is constant as \((i,j)\) ranges through \(C\).

Summing this condition over all \(Y\) gives \(2r_X(i)=2r_X(i')\) for any two cells \((i,j),(i',j')\in C\), because \(\sum_Y c_Y(j)=2\). Similarly, summing over \(X\) gives \(mc_Y(j)=mc_Y(j')\), because \(\sum_X r_X(i)=m\). Since these are equalities of ordinary integers, the criterion is equivalent to *constancy on each block of both the complete row-incidence profile and the complete column-incidence profile*. Conversely, constancy of these two profiles immediately makes every product coefficient constant.

**2. Separated case.** There are only two possible row-incidence profiles, one for each row. If they differ, no block can meet both rows. Let \(\Pi_0,\Pi_1\) be the induced partitions of the column labels in the two rows. Within a top-row block the column profile is constant, and therefore the bottom-row block containing its column labels must be constant: \(\Pi_0\) refines \(\Pi_1\). Reversing the rows yields the opposite refinement, hence \(\Pi_0=\Pi_1\). Conversely, two copies of any one partition have the requisite profiles and are Schur. There are \(\mathscr B(m)\) possibilities.

**3. Balanced case.** If the two row-incidence profiles agree, every block \(X\) has \(r_X(0)=r_X(1)\). Name the blocks by distinct colors. Each column has the unordered multiset of the colors of its two cells. This multiset is exactly the column-incidence profile. Since this profile is constant along each color block, no color can occur in columns with different color multisets. Thus columns split uniquely into color-multiset types. A type \(\{A,A\}\) consists of columns whose two cells all belong to one color block \(A\), giving the monochrome construction. A type \(\{A,B\}\) for distinct colors assigns one cell of each color to every column. Because both color blocks are row-balanced, the numbers of columns having \(A\) in the top row and having \(B\) in the top row must agree. Its cardinality is thus \(2h\), and its pattern is exactly an unordered equipartition into two \(h\)-element halves with the complementary two blocks stated above. Conversely each displayed construction has equal row-incidence profiles and constant column-incidence profiles on every block, so it is Schur. The unique color-multiset decomposition prevents overcounting.

**4. Enumeration.** For a fixed labelled column group of size \(t\), there is one monochrome pattern, plus \(\frac12\binom{t}{t/2}\) paired patterns when \(t\) is even and positive. The exponential formula for set partitions decorated by independent group patterns gives the balanced exponential generating function
\[
\exp\left(\sum_{t\ge1}\frac{z^t}{t!}+\sum_{h\ge1}\frac12\binom{2h}{h}\frac{z^{2h}}{(2h)!}\right)
=\exp\left(e^z-1+\frac12\sum_{h\ge1}\frac{z^{2h}}{(h!)^2}\right).
\]
Adding the disjoint separated family proves the displayed count. A direct-product partition of \(\{0,1\}\times[m]\) must take the row partition either as the singleton partition (separated case) or as the indiscrete partition (all monochrome balanced case). These contribute \(2\mathscr B(m)\) distinct direct products, establishing the last assertion.

**5. Automorphic realization.** The semigroup automorphisms are exactly independent row and column permutations, \(S_2\times S_m\). For a separated partition, take the subgroup of column permutations acting as a full symmetric group separately on each part of \(\Pi\), with rows fixed. Its orbits are exactly the stated blocks. For a balanced partition, first allow full symmetric column permutations within each monochrome column group and within each of the two halves of every paired group. Add one automorphism simultaneously swapping the two rows and exchanging the two halves of every paired group by fixed bijections, while fixing columns in monochrome groups. This automorphism preserves each displayed block setwise, and together with the within-group permutations makes every displayed block a single orbit. Hence every Schur partition is automorphic.

## Verification
A standalone Python 3 verifier, `rectangular_schur_verify.py`, independently generates every set partition on \(2m\) labelled cells for \(1\le m\le4\), tests multiplication closure by explicit product coefficients, compares with the two-form classification, and constructs a subgroup of \(S_2\times S_m\) whose generated orbits equal the claimed blocks. It finds \((1,1),(2,3),(5,8),(15,33)\) separated/balanced counts, totalling \(2,5,13,48\), respectively. It also evaluates the formula at \(m=5\), yielding \(184\), without exhaustive enumeration at that size. All checks returned `VERIFY_OK`. Finite checks corroborate the general proof but do not replace it.

## Relationship to prior work
Marrow and Misseldine, *On Schur Rings Over Semigroups* (arXiv:2601.09940v1, first submitted January 14, 2026), define the semigroup-Schur notion used here, construct \(\mathscr B(n)\mathscr B(m)\) direct-product examples on rectangular bands, and report the totals \(5\) on the \(2\)-by-\(2\) band and \(13\) on the \(2\)-by-\(3\) band in their census of semigroups of order at most seven. Their discussion explicitly observes additional non-direct-product examples. The present statement classifies the entire infinite two-row family, proves that every partition is automorphic, and supplies the exact generating function. The previously tabulated totals are compatible special cases; they are not presented as new results.

## Limitations
This result does not classify Schur partitions of rectangular bands with three or more rows, of rectangular groups with nontrivial group factors, or of semigroup algebras over arbitrary positive-characteristic coefficient fields. Although the available published sources and searchable research records were compared, a preexisting equivalent classification under the vocabulary of equitable colorings, orbit partitions, or coherent configurations cannot be ruled out. No further claims beyond the specified class are asserted.

## References
1. J. E. Marrow and A. Misseldine, *On Schur Rings Over Semigroups*, arXiv:2601.09940v1 (submitted January 14, 2026), https://arxiv.org/html/2601.09940v1; especially Sections 1, 2.1–2.2, 5.4, and 5.6.
