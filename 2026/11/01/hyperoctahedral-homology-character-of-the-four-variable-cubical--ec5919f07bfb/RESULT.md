# Hyperoctahedral homology character of the four-variable cubical two-SAT theta complex

## Finding
Let \(Q_4=\{0,1\}^4\) and let \(\mathcal H\) be the hypergraph with these sixteen vertices and the twenty-four square faces of the four-cube as hyperedges. Write \(X=\Theta(\mathcal H)\): a subset \(S\subseteq Q_4\) is a face of \(X\) precisely when it is disjoint from at least one square. The complete rational top-homology character under the signed coordinate-permutation group \(B_4=(C_2)^4\rtimes S_4\) is specified in the table below. The dimension is fifteen, and all other reduced rational homology vanishes, by the known homotopy equivalence \(X\simeq\bigvee^{15}S^6\).

An element of \(B_4\) is a coordinate permutation together with independent bit flips. Each coordinate cycle has length \(\ell\) and a parity \(\epsilon\in\{0,1\}\), the sum modulo two of its flips. A class is represented by its multiset of signed cycle pairs \((\ell,\epsilon)\). The last column is \(\operatorname{tr}(g\mid\widetilde H_6(X;\mathbb Q))\).

| Signed coordinate cycles | Elements | Top-homology trace |
| :--- | ---: | ---: |
| (1+,1+,1+,1+) | 1 | 15 |
| (1+,1+,1+,1−) | 4 | 3 |
| (1+,1+,1−,1−) | 6 | −1 |
| (1+,1+,2+) | 12 | 1 |
| (1+,1+,2−) | 12 | 1 |
| (1+,1−,1−,1−) | 4 | 3 |
| (1+,1−,2+) | 24 | 1 |
| (1+,1−,2−) | 24 | 1 |
| (1+,3+) | 32 | 0 |
| (1+,3−) | 32 | 0 |
| (1−,1−,1−,1−) | 1 | 15 |
| (1−,1−,2+) | 12 | 1 |
| (1−,1−,2−) | 12 | 1 |
| (1−,3+) | 32 | 0 |
| (1−,3−) | 32 | 0 |
| (2+,2+) | 12 | −5 |
| (2+,2−) | 24 | −1 |
| (2−,2−) | 12 | 3 |
| (4+) | 48 | −1 |
| (4−) | 48 | −1 |

Here a plus means even flip parity, not a positive integer sign. In particular, the weighted character sum over all 384 elements is zero; thus \(\widetilde H_6(X;\mathbb Q)^{B_4}=0\). The simultaneous change of all four coordinate signs is central and has character value fifteen, so it acts as the identity (finite-order rational representation). The value \(-5\) excludes any basis permuted without signs.

## Assumptions and scope
The cube is the affine Boolean cube, not its one-skeleton. Each square is obtained by selecting two variable coordinates and fixing the other two, yielding exactly \(\binom42\cdot2^2=24\) square hyperedges. All 16 cube vertices are retained. The theta complex uses the *disjoint-from-an-entire-hyperedge* convention, not the independence-complex convention. The natural action is the full coordinate hyperoctahedral group, of size \(2^4 4!=384\), and homology is reduced singular or simplicial homology with rational coefficients. The known homotopy calculation is from Conant--Thistlethwaite, Theorem 5, initially public on 5 August 2008.

## Proof
The non-equivariant input is \(X\simeq\bigvee^{15}S^6\), Conant--Thistlethwaite, Theorem 5. Hence \(H_0(X;\mathbb Q)=\mathbb Q\), \(\widetilde H_6(X;\mathbb Q)=\mathbb Q^{15}\), and all other reduced homology groups vanish. Any coordinate sign change and permutation preserves the collection of square hyperedges and therefore acts simplicially on \(X\).

For an element \(g\in B_4\), let \(O_1,\ldots,O_c\) be its vertex orbits on the sixteen points of \(Q_4\). A simplex fixed setwise by \(g\) is precisely a nonempty union \(S=\bigcup_{i\in I}O_i\). It is in \(X\) if and only if there exists one of the 24 square masks \(F\) such that \(S\cap F=\varnothing\). The orientation sign of \(g\) on that simplex equals \((-1)^{|S|-|I|}\), since each selected orbit contributes one cyclic permutation. Its signed contribution to the ordinary simplicial Lefschetz number, including the factor \((-1)^{|S|-1}\) from simplex dimension, is therefore exactly \((-1)^{|I|-1}\). Thus the *exact finite formula*

\[
L(g)=\sum_{\varnothing\ne I\subseteq\{1,\ldots,c\}}(-1)^{|I|-1}\mathbf1\!\left[\exists\,F\in\mathcal H:\ F\cap\bigcup_{i\in I}O_i=\varnothing\right]
\]

holds for every one of the 384 group elements. The Lefschetz theorem and the degree-six concentration give \(L(g)=1+\operatorname{tr}(g\mid\widetilde H_6(X;\mathbb Q))\), with the plus sign because six is even. The attached standalone program enumerates the 24 square masks, all 384 coordinate transformations, and every union of its 16-point orbits, with ordinary integer arithmetic. It evaluates the finite formula, groups transformations by their signed coordinate cycle partitions, and proves that all elements of each of the twenty classes yield precisely the values in the displayed table. This is exhaustive for the specified finite group and finite complex; no inference from a few sampled group elements is used.

The conjugacy-class sizes in the table sum to 384. Their character-weighted sum is zero; the standard averaging idempotent \(|B_4|^{-1}\sum_{g\in B_4}g\) therefore has rank zero. The central global bit-complement element lies in class \((1-,1-,1-,1-)\) and has trace equal to dimension fifteen. Since its order is two, its eigenvalues are \(\pm1\), and it must act trivially. The class \((2+,2+)\) has trace \(-5\); an unsigned permutation representation has nonnegative traces, so this representation cannot be one.

## Verification
Reproduce the exact finite calculation using `python3 verify_cube_theta_character.py`; no nonstandard libraries are required. The program reconstructs all 24 square masks and 384 group transformations, verifies class constancy, the twenty displayed traces, the group-invariant dimension, and the antipodal trace, and prints `VERIFY_OK`. A matching output transcript is supplied as `verification_cube_theta_character.txt`. The machine does *not* prove the already published homotopy equivalence; that is explicitly an external theorem and is the sole homology-concentration premise.

## Relationship to prior work
Conant and Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, Theorem 5, calculate the nonequivariant homotopy type and Euler characteristic of this exact theta complex, and Section 6 studies finite-group congruences for Euler characteristics. Their work is not claimed as novel here. The present calculation instead determines the rational representation of all 384 cubical symmetries, including the vanishing invariant subspace, antipodal kernel and negative character values. Related computations of characters for other cubical Čech and cut complexes involve different simplicial complexes and do not imply this twenty-class table.

## Limitations
The result determines rational characters, not a classification of the integral \(\mathbb Z[B_4]\)-lattice, cohomology ring, equivariant homotopy type, or fixed-point sets. A full classification of the representation into irreducible rational constituents is not asserted. No priority claim is made against an unindexed equivalent character calculation. The homotopy input is taken from the cited published theorem; the original table and its character consequences are verified by exact finite enumeration, not by a second independent human review.

## References
1. James Conant and Oliver Thistlethwaite, *Boolean formulae, hypergraphs and combinatorial topology*, arXiv:0808.0739 (first version 5 August 2008), especially Section 5.2, Theorem 5, and Section 6. https://arxiv.org/abs/0808.0739
2. Same authors, *Topology and its Applications*, DOI:10.1016/j.topol.2010.08.016 (later journal publication). https://doi.org/10.1016/j.topol.2010.08.016
