# Eight Singer pencils partition the smooth plane-filling quartics over \(\mathbf F_2\)

## Finding
Let \(k=\mathbf F_2\), and let \(V\) be the \(k\)-vector space of homogeneous quartic forms in \(k[x,y,z]\) vanishing at all seven points of \(\mathbf P^2(k)\). A *filling pencil* means a two-dimensional \(k\)-subspace \(L\subset V\), viewed as three nonzero quartics. The following classification holds.

**Theorem.** Exactly \(24\) forms in \(V\) define geometrically smooth curves. They partition uniquely into exactly **eight** two-dimensional subspaces \(L\subset V\) whose three nonzero forms are geometrically smooth. These eight pencils are in canonical bijection with the eight Singer cyclic subgroups of order \(7\) in \(\operatorname{PGL}_3(k)\). The projective group is transitive on the eight pencils, with stabilizer of order \(21\); each individual smooth filling quartic has stabilizer of order \(7\). There is **no** three-dimensional linear subspace of \(V\) with every nonzero member smooth. At each of the seven rational points, the tangent lines of the three quartics of any one of these pencils are precisely the three rational lines through that point.

Thus every smooth minimal-degree plane-filling quartic belongs to exactly one pencil with all three rational members smooth and plane-filling; the eight pencils are not claimed to have every member over \(\overline k\) smooth.

## Assumptions and scope
All curves and coordinate transformations are defined over \(k=\mathbf F_2\), while *smooth* means geometrically smooth over \(\overline{k}\). Quartic equations are counted in fixed coordinates; nonzero scalar identification is trivial over \(k\). Pencils are two-dimensional vector subspaces, not ordered pairs of generators. The eight-way classification is under \(\operatorname{PGL}_3(k)=\operatorname{GL}_3(k)\), a group of order \(168\). The binary quartics are of degree \(4\), the minimal smooth plane-filling degree. The associated curves have genus \(3\).

## Proof
**1. Matrix model and smoothness.** Put
\[
U=y^2z+yz^2,\qquad V=z^2x+zx^2,\qquad W=x^2y+xy^2.
\]
For a matrix \(A=(a_{ij})\in M_3(k)\), set
\[
F_A=(a_{11}x+a_{21}y+a_{31}z)U+(a_{12}x+a_{22}y+a_{32}z)V+(a_{13}x+a_{23}y+a_{33}z)W.
\]
Tallini's ideal-generation theorem and the normal form of Homma--Kim identify the space of filling quartics with \(M_3(k)/kI_3\), under \(A\mapsto F_A\), since its kernel consists exactly of scalar matrices. Homma--Kim's Theorem 3.2 says that \(F_A=0\) is geometrically smooth exactly when the characteristic polynomial of \(A\) is irreducible of degree \(3\). Over \(\mathbf F_2\) this is exactly
\[
\det(A)=\det(A+I_3)=1. \tag{1}
\]
There are two irreducible monic cubics over \(k\). Each irreducible matrix conjugacy class has \(168/(2^3-1)=24\) members, as its invertible centralizer is \(\mathbf F_8^\times\) of order \(7\). The \(48\) matrices satisfying (1) are paired by \(A\leftrightarrow A+I_3\), giving exactly \(24\) smooth filling forms.

**2. Eight natural pencils.** For any irreducible matrix \(A\), its centralizer algebra \(k[A]\) is an embedded copy of \(\mathbf F_8\) in \(M_3(k)\). Its quotient \(k[A]/kI_3\) is two-dimensional, with exactly three nonzero elements, all represented by matrices with irreducible cubic characteristic polynomial. Consequently this quotient gives an all-smooth filling pencil. The multiplicative group \(k[A]^\times\) is a Singer subgroup of order \(7\). There are exactly \(48/6=8\) such subgroups because all \(48\) irreducible matrices have order \(7\), and each subgroup has six nonidentity elements. Distinct Singer subgroups have disjoint nontrivial matrix-coset sets. Hence they yield eight disjoint pencils covering all \(24\) smooth filling quartics.

**3. No further pencils: a finite matrix lemma.** We prove that if \(A,B,A+B\) all satisfy (1), then \(A\) and \(B\) generate the same embedded field \(\mathbf F_8\). Conjugation by \(\operatorname{GL}_3(k)\) allows fixing the matrix
\[
A=\begin{pmatrix}0&1&1\\1&1&0\\1&0&0\end{pmatrix}.
\]
Its stabilizer on matrix cosets is the order-seven group \(H=\langle A\rangle\). The other two smooth classes in \(k[A]/kI_3\) already have smooth sum with \(A\). On the remaining \(21\) smooth classes, \(H\) has three orbits of seven: a nontrivial element of \(H\) cannot stabilize an outsider, because the order-seven subgroup of its curve stabilizer is then different. The following complete three-orbit certificate uses row-major binary matrix encoding, with bit positions \(0,\ldots,8\), and chooses the smaller integer for the equivalent pair \(B,B+I_3\):

| Representative \(B\) | Seven coset representatives in its \(H\)-orbit | \(\det(A+B)\) | \(\det(A+B+I_3)\) |
|---|---|---:|---:|
| 95 | 95, 102, 111, 115, 157, 204, 207 | 0 | 0 |
| 99 | 99, 106, 141, 142, 171, 190, 250 | 0 | 0 |
| 114 | 114, 156, 172, 226, 244, 247, 253 | 0 | 1 |

The orbit lists are computed by the explicit seven conjugations \(A^j B A^{-j}\), \(0\le j<7\); the displayed determinant pairs can be checked by ordinary three-by-three arithmetic over \(k\). As the two determinant values are invariant under conjugation by \(H\), equation (1) fails for \(A+B\) in every outsider orbit. Thus no cross-Singer pair gives a smooth third member, proving that the eight pencils exhaust the possibilities. The complete short enumeration is independently encoded in the accompanying matrix verifier.

**4. Group action, maximality, tangents.** All eight Singer groups are conjugate. A Singer normalizer has order \(168/8=21\), so the eight pencils form one projective orbit of size eight. An individual curve has stabilizer the Singer subgroup of order seven, as above (also consistent with Homma--Kim's automorphism theorem). Were a three-dimensional subspace to have all seven nonzero members smooth, one smooth form would belong to at least three distinct two-dimensional all-smooth subspaces, contradicting uniqueness. Finally, at any rational point all three members vanish; their gradients are nonzero and satisfy \(\nabla F_A+\nabla F_B=\nabla(F_A+F_B)\). Hence the three tangent covectors are distinct nonzero elements of the two-dimensional annihilator of the point. They are therefore the three rational tangent lines through that point.

A representative pencil has quartic members \(F_{94},F_{187},F_{229}\), where binary row-major encoding is as above and \(F_{94}+F_{187}=F_{229}\). Explicitly,
\[
\begin{aligned}
F_{94}={}&x^3y+x^3z+x^2y^2+x^2yz+x^2z^2+xyz^2+y^3z+yz^3,\\
F_{187}={}&x^3z+x^2y^2+x^2yz+xy^3+xy^2z+xz^3+y^3z+y^2z^2.
\end{aligned}
\]
The third equation is their sum over \(k\).

## Verification
Two independently organized exact-arithmetic checks are provided. `verify_matrices.py` exhaustively evaluates all \(512\) binary \(3\times3\) matrices, their \(256\) scalar cosets, determinant irreducibility criterion, all \(168\) invertible transformations, the eight Sylow-seven subgroups, all pairwise smooth sums, orbit sizes and stabilizers. It checks the three outsider orbits and obtains exactly \(24\) smooth quartics and eight pencils. `verify_groebner.py` independently constructs all \(255\) nonzero filling quartic equations and tests geometric smoothness using exact Gröbner bases in all three affine charts. It finds exactly \(24\) smooth equations and the same eight pencils. Both programs were run successfully from their packaged paths; the actual outputs are included. Finite enumeration is exhaustive for this finite domain, while the smoothness criterion is a published theorem and independently rechecked algebraically in the second verifier.

## Relationship to prior work
Homma and Kim (arXiv:0903.1918, Theorem 3.2 and Theorem 5.4) give a complete single-curve matrix criterion and automorphism groups for minimum-degree smooth plane-filling curves. Their results supply the starting normal form, but do not state or classify compatibility under addition of distinct smooth quartics, a partition into pencils, the eight Singer-normalizer pencils, or the no-net consequence. Asgarli and Ghioca (arXiv:2203.07169, Question 1.2 and Theorem 1.3) motivate simultaneous smoothness of every rational member of a pencil, proving a general existence theorem only under a large-field hypothesis and discussing low-degree conic examples. Asgarli and Ghioca (arXiv:2307.03072) study smooth plane-filling curves of higher degree; they do not determine this minimum-degree pencil incidence. The new input relative to the first source is the cross-Singer matrix-sum obstruction in Step 3 and its geometric consequences, not a new characterization of individual Tallini curves.

## Limitations
The result concerns the smallest field and exactly degree four, with all three **rational** members required smooth and plane-filling. Pencils may have geometrically singular members with parameter in an extension field; nothing asserts smoothness of every geometric member. The theorem does not classify arbitrary quartic pencils that are not plane-filling, or higher degrees/fields. Unindexed earlier finite-geometric classifications and equivalent matrix-spread statements remain a publication-priority risk. The derivation uses Homma--Kim's published characterization of smooth filling curves; its independent Gröbner check is an additional finite verification, not a new proof of that general theorem.

## References
1. M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups*, arXiv:0903.1918 (first posted 2009-03-11), especially Theorems 3.2 and 5.4. https://arxiv.org/abs/0903.1918
2. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169 (first posted 2022-03-14), especially Questions 1.1--1.2 and Theorem 1.3. https://arxiv.org/abs/2203.07169
3. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072 (first posted 2023-07-06), Introduction and Theorem 1.2. https://arxiv.org/abs/2307.03072
