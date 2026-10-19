# Sharp evolution-envelope dimension for ternary three-dimensional unital commutative algebras

## Finding

Fix the field \(K=\mathbb F_3\). In a fixed basis \(e_0,e_1,1\), there are precisely \(3^9=19683\) unital commutative (not necessarily associative) multiplication tables. Exactly **288** of these have minimal evolution-envelope dimension \(6\), the universal upper bound for a three-dimensional algebra. Up to unital \(K\)-algebra isomorphism, these 288 tables form **exactly two classes**, each with 144 labeled tables: one associative class (isomorphic to \(\mathbb F_{27}\)) and one nonassociative class. Moreover, attainment is **equivalent** to being a division algebra: every nonzero multiplication operator is invertible. Thus the sharp upper bound is attained even by a commutative nonassociative division algebra.

Concrete representatives, with \(e_2=1\), are determined by the columns \((e_0^2,e_0e_1,e_1^2)\):

\[
\begin{array}{c|ccc}
& e_0^2 & e_0e_1 & e_1^2\\
\text{nonassociative}&e_1&e_1+2e_2&2e_0+2e_2\\
\text{associative}&e_1&e_1+2e_2&2e_0+e_1+2e_2.
\end{array}
\]

The nonassociative representative has \((e_0^2)e_1=2e_0+2e_2\) but \(e_0(e_0e_1)=2e_0+e_1+2e_2\). Both representatives are division algebras (left multiplication by each nonzero element is invertible).

## Assumptions and scope

The algebra is three-dimensional as a vector space over \(\mathbb F_3\), commutative, bilinear, and has a prescribed identity \(e_2\); associativity is not assumed. The minimal evolution-envelope dimension is the least dimension of an evolution algebra containing the algebra as an ideal, in the sense of Costoya–Fernández Ouaridi–Viruel. Their unital-algebra reduction, valid in characteristic other than two, equates this dimension with the simultaneous Waring rank of the coordinate quadrics of the square map. The count 288 concerns structure constants relative to a **fixed unit-bearing basis**, not isomorphism classes.

## Proof

Write \(A=e_0^2\), \(B=e_0e_1\), \(C=e_1^2\), where each is an arbitrary vector in \(K^3\). This gives precisely \(3^9\) tables and every unital commutative table exactly once. Let \(a=(x,y,z)\) and write \(a^2=(f_0,f_1,f_2)\). For \(i=0,1,2\) we have
\[
f_i=A_i x^2+2B_i xy+2\delta_{i0}xz+C_i y^2+2\delta_{i1}yz+\delta_{i2}z^2.
\]
Regard each quadratic as a row vector of coefficients in the ordered monomial basis \((x^2,xy,xz,y^2,yz,z^2)\). The three rows are linearly independent: if a linear functional on the output annihilated all values of squaring, polarization would make it annihilate all products, contradicting \(A^2=A\) for a unital algebra.

For a projective linear form \(\ell=ax+by+cz\), its square is represented by
\[
s(a,b,c)=(a^2,2ab,2ac,b^2,2bc,c^2).
\]
There are exactly 13 projective linear forms over \(\mathbb F_3\). Six of their squares span the six-dimensional space of ternary quadrics: take forms \(x,y,z,x+y,x+z,y+z\). Thus every such algebra has Waring rank at most six.

Let \(U=\langle f_0,f_1,f_2\rangle\) and let \(N=U^\perp\), a three-dimensional subspace in the dual of the quadratic coefficient space. The Waring rank is at most five if and only if there is a nonzero \(n\in N\) whose associated projective ternary quadric vanishes on at least five projective points. In the forward direction, five squares spanning a space containing \(U\) have a nonzero annihilator \(n\in N\). In the reverse direction, a quadric with at least five rational zeros has five independent zero-point square vectors, so its vanishing hyperplane is spanned by five squares and contains \(U\). The latter finite geometric assertion can be verified directly on all 364 projective quadratic coefficient vectors. Their (number of zeros, dimension spanned by zero-point squares) profiles are exactly
\[
(4,3):13,\quad(7,5):78,\quad(1,1):39,\quad(4,4):234.
\]
In particular, at least five zeros necessarily means seven, and the corresponding five-square span has dimension five.

This converts the original minimization to a finite, complete rank test. Enumerate all nine structure constants in \(\mathbb F_3^9\), form \(U\) and a basis of \(N\) by Gaussian elimination, and examine all 13 projective nonzero elements of \(N\). Exactly 288 tables have no quadric in \(N\) with five or more projective zeros. By the proved criterion these, and only these, have evolution-envelope dimension six. A further exhaustive rank-three test of left multiplication by each of the 26 nonzero elements in every table proves that exactly the same 288 tables are division algebras.

For isomorphisms, a unital algebra isomorphism must fix \(1\). The invertible basis changes fixing \(e_2\) have matrices with columns \((a,b,c)^T,(d,e,f)^T,(0,0,1)^T\), where \(ae-bd\ne0\). There are \(48\cdot9=432\) such changes. Transforming the three defining product columns through every one of these basis changes partitions the 288 maximal tables into two orbits of size 144. Representatives are exactly the two tables displayed above. Direct evaluation of the associator on basis triples distinguishes them. In each representative, all 26 nonzero left multiplication maps have rank three, and the associative representative is therefore the field of 27 elements. This also proves the asserted division property and completes the isomorphism classification.

## Verification

The accompanying independent-input Python script `verify.py` requires only the Python 3 standard library. Run `python verify.py`. It enumerates all 19,683 tables, the 364 projective ternary quadrics, the 13 projective linear forms, and all 432 unit-preserving basis changes, checking Gaussian ranks, square spans, associativity, sharp-table counts and orbit representatives. It prints `VERIFY_OK` on success. The proof uses exact finite enumeration at a fixed finite field and fixed dimension; it makes no extrapolation to larger dimensions or coefficient fields.

## Relationship to prior work

Costoya, Fernández Ouaridi and Viruel establish the embedding invariant, the universal dimension bound, and the reduction to Waring rank for unital algebras, and ask whether the dimension bound is sharp. The result here is a complete **smallest nontrivial three-dimensional sharpness census over \(\mathbb F_3\)** and a classification of all extremizers. Earlier bilinear-complexity literature covers multiplication tensors of associative fields, so the associative representative and its multiplication complexity are not independently claimed as new. Work on finite commutative semifields supplies broader structural background, but the present finite-field claim is specifically the exact evolution-envelope sharpness locus among all 19,683 unital commutative tables and its two isomorphism orbits.

## Limitations

The result concerns only \(\mathbb F_3\) and dimension three. It does not classify nonunital or higher-dimensional algebras, nor claim that the two underlying division-algebra isomorphism classes were previously unknown. The equivalence to evolution-envelope dimension relies on the published unital Waring-rank theorem; the new counting and orbit assertions are verified by complete finite enumeration. A prior unindexed tensor-rank or finite-algebra census may imply the numerical classification, and independent mathematical review remains outstanding.

## References

- C. Costoya, A. Fernández Ouaridi and A. Viruel, *Commutative algebras are ideals of evolution algebras*, arXiv:2609.32784 (first public version September 26, 2026), https://arxiv.org/abs/2609.32784.
- H. Randriambololona, *Bilinear complexity of algebras and the Chudnovsky–Chudnovsky interpolation method*, arXiv:1107.0336, https://arxiv.org/abs/1107.0336.
- A. Drápal, *Commutative quasigroups and semifields from planar functions*, *Communications in Algebra* 52 (2024), 1885–1896, https://doi.org/10.1080/00927872.2023.2275392.
- M. Bläser, *A Complete Characterization of the Algebras of Minimal Bilinear Complexity*, *SIAM J. Comput.* 34 (2005), https://doi.org/10.1137/S0097539703438277.
