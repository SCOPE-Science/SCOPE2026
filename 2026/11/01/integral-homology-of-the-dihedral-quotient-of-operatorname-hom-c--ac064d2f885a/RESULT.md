# Integral homology of the dihedral quotient of \(\operatorname{Hom}(C_5,K_5)\)

## Finding
Let \(X=\operatorname{Hom}(C_5,K_5)\) be the Lovász graph-homomorphism complex of the five-cycle with five available colours. The dihedral group \(D_5\), of order ten, acts by rotating and reflecting the five input vertices, without permuting the colours. Let \(Y=|X|/D_5\) be the **ordinary geometric quotient**. Its integral singular homology is
\[
H_i(Y;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/2,&i=1,\\
0,&i=2,\\
\mathbb Z\oplus\mathbb Z/5,&i=3,\\
\mathbb Z/2,&i=4,\\
0,&i\ge5.
\end{cases}
\]
In particular, the quotient contains both order-two and order-five torsion. This is an exact computation of the ordinary quotient, not an assertion of a \(D_5\)-equivariant homeomorphism to a quotient of the Stiefel manifold under its standard orthogonal action.

## Assumptions and scope
Write the vertices of \(C_5\) as \(\mathbb Z/5\), and the five colours as \(\{0,1,2,3,4\}\). A cell is a tuple \((A_0,\dots,A_4)\) of nonempty subsets of the colour set, with \(A_i\cap A_{i+1}=\varnothing\) (subscripts modulo five). It is the product \(\prod_i\Delta^{A_i}\), with dimension \(\sum_i(|A_i|-1)\). The generators of \(D_5\) act on the input positions by \(r(i)=i+1\) and \(s(i)=-i\). The group does not act on the colour labels.

The action on cells is free: a nonidentity rotation fixing a cell would make all five coordinate sets equal, impossible for nonempty adjacent disjoint sets. Every reflection fixes an edge setwise and reverses its endpoints, likewise impossible for a fixed cell. Thus the geometric action is free, and the quotient inherits a finite cellular chain complex in which each orbit of cells contributes one free generator.

## Proof
Equip each simplex factor with its increasing-colour orientation and order the five factors by input vertex. The boundary of an oriented cell is
\[
\partial[A_0,\ldots,A_4]=
\sum_{i=0}^{4}\ \sum_{a\in A_i,\ |A_i|\ge2}
(-1)^{\sum_{h<i}(|A_h|-1)+\operatorname{pos}_{A_i}(a)}
[A_0,\ldots,A_i\setminus\{a\},\ldots,A_4],
\]
where \(\operatorname{pos}_{A_i}(a)\) counts the elements of \(A_i\) smaller than \(a\). When a permutation \(g\) of the input positions maps a tuple to the canonical lexicographically smallest representative of its \(D_5\)-orbit, its orientation correction is the Koszul sign
\[
(-1)^{\sum_{i<j,\ g(i)>g(j)} (|A_i|-1)(|A_j|-1)}.
\]
These formulas define the quotient boundary matrices over \(\mathbb Z\) without invoking rational approximations.

The product-cell counts in dimensions zero through five are \((1020,5700,13000,15000,8750,2070)\). Since the action is free on all cells, the quotient chain ranks are
\[
(\operatorname{rank}C_0,\ldots,\operatorname{rank}C_5)
=(102,570,1300,1500,875,207).
\]
All boundary compositions vanish, as verified directly from the resulting integer matrices. Exact unimodular row and column elimination supplies the following Smith data; an exponent means that many diagonal entries equal to one:

| Boundary | Unit entries | Remaining nonzero Smith entries | Total rank |
| --- | ---: | --- | ---: |
| \(\partial_1\) | 101 | none | 101 |
| \(\partial_2\) | 468 | \(2\) | 469 |
| \(\partial_3\) | 831 | none | 831 |
| \(\partial_4\) | 667 | \(5\) | 668 |
| \(\partial_5\) | 206 | \(2\) | 207 |

For completeness, the finite integer certificate does not merely take ranks modulo primes. At each unit entry \(u=\pm1\), an integral invertible change of basis removes one row and one column and replaces the complementary block by its Schur complement \(B_{ij}-B_{ic}B_{rj}/u\). The verifier performs every such step. After the numbers of unit pivots shown above, the residual matrix is zero or has rank exactly one: every nonzero residual column is equal, up to sign, to one fixed column, and every nonzero entry in that column is exactly \(\pm2\), \(\pm5\), or \(\pm2\), respectively. Consequently its Smith form contains exactly the displayed nonunit entry, with no untested prime factors or higher prime powers. All arithmetic is integral and exact.

The rational ranks follow from the same Smith forms. Since \(\operatorname{im}\partial_i\) is free abelian, the torsion of \(H_i\) equals the torsion of \(\operatorname{coker}\partial_{i+1}\). Together with the quotient chain ranks, this gives every group in the Finding.

## Verification
Run `python verify.py` using a standard Python 3 interpreter; no third-party packages are needed. The program independently enumerates the cells, computes the signed \(D_5\)-orbit boundaries, checks \(\partial^2=0\), and replays the unimodular reductions and residual rank-one certificates. It also repeats the construction with four colours as an external mathematical control, obtaining \(H_1\cong\mathbb Z/4\) for that quotient, consistent with its binary-dihedral covering description.

For five colours, the program prints `PENTAGON_DIHEDRAL_INTEGRAL_HOMOLOGY_OK` and the exact cell counts, unit-pivot counts, torsion factors and ranks. The file `verification_output.txt` records the completed execution. The auxiliary `modular_crosscheck.py`, recorded in `modular_output.txt`, independently checks the boundary ranks modulo 2, 5, and 7, corroborating the integral Smith data. The finite enumeration exhausts **every** quotient cell, not a truncation or sample; the proof makes no claim for a variable number of colours.

## Relationship to prior work
Babson and Kozlov introduced the general graph-homomorphism complex; Kozlov determined the integral cohomology of \(\operatorname{Hom}(C_m,K_n)\) itself. Schultz and Dover–Özaydın established nonequivariant and reflection-equivariant identifications of \(\operatorname{Hom}(C_5,K_n)\) with Stiefel manifolds. In particular, \(X\cong V_{4,2}\cong S^2\times S^3\) as spaces. These results are not claimed as new.

Dover–Özaydın explicitly ask whether an identification can be made \(D_5\)-equivariant (Question 5.6); their stated theorem treats a reflection, rather than the complete dihedral action. Neither their results nor the nonequivariant cohomology formula specifies the **integral homology of the full geometric dihedral quotient**. The new calculation is the exact quotient groups, including the order-five and order-two torsion. A later study of projective and circle quotients of Stiefel manifolds considers different specified group actions; those formulas do not directly imply the present combinatorial \(D_5\)-quotient result.

## Limitations
This is a finite computation for exactly five input vertices and five colours. It does not establish a full \(D_5\)-equivariant homeomorphism to \(V_{4,2}\) under the standard orthogonal subgroup action, determine the cohomology ring, or generalize to all \(K_n\). Priority against unindexed equivalent computations is not conclusively resolved. No independent mathematical audit has been performed.

## References
1. E. Babson and D. Kozlov, *Complexes of graph homomorphisms*, arXiv:math/0310056 (first publicly posted 2003-10-05); Israel J. Math. 152 (2006), 285–312.
2. D. Kozlov, *Cohomology of colorings of cycles*, arXiv:math/0507117 (first publicly posted 2005-07-06); American J. Math. 130 (2008), 829–857, especially Theorem 7.2.
3. C. Schultz, *Small models of graph colouring manifolds and the Stiefel manifolds Hom(C5,Kn)*, arXiv:math/0510535 (first publicly posted October 2005); J. Combin. Theory Ser. A 115 (2008), 94–104.
4. J. Dover and M. Özaydın, *Stiefel manifolds and coloring the pentagon*, arXiv:1302.2831 (first publicly posted 2013-02-12), especially Question 5.6; J. Combin. Theory Ser. A 121 (2014), 74–88.
5. D. Dasgupta, *Characteristic classes on certain quotients of Stiefel manifolds*, arXiv:2402.10521 (first publicly posted 2024-02-16), Introduction, Sections 2–3.
