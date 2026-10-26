# A sharp rank-one Nijenhuis–Rota–Baxter boundary for \(M_n(k)\)

## Finding

Let \(k\) be any field, let \(n\ge2\), and let \(A=M_n(k)\). An **associative Nijenhuis operator** is a linear map \(N:A\to A\) satisfying
\[
N(X)N(Y)=N\bigl(N(X)Y+XN(Y)-N(XY)\bigr)
\quad(X,Y\in A).
\]
A **weight-zero Rota–Baxter operator** satisfies the same identity without the term \(-N(XY)\) inside the outer operator. Write \(\mathcal N_n^{(1)}(k)\) and \(\mathcal R_n^{(1)}(k)\) for their respective sets of **nonzero linear maps of vector-space rank one**.

**Theorem.** For every field \(k\),
\[
\mathcal R_n^{(1)}(k)\subseteq\mathcal N_n^{(1)}(k),\qquad
\mathcal R_n^{(1)}(k)=\mathcal N_n^{(1)}(k)\ \Longleftrightarrow\ n\ge3.
\]
For \(n=2\), the complete exceptional family \(\mathcal N_2^{(1)}(k)\setminus\mathcal R_2^{(1)}(k)\) consists exactly of
\[
N_{F,U}(X)=\operatorname{tr}(FX)U,
\quad F\ne0,\quad F^2=0,\quad\operatorname{rank}(U)=1,
\quad \operatorname{tr}(FU)\ne0.
\]
Each exceptional map has \(N_{F,U}^{2}=\operatorname{tr}(FU)N_{F,U}\), and thus becomes a nonzero idempotent operator after scalar normalization. The only redundancy in presentations is \((F,U)\sim(s^{-1}F,sU)\) for \(s\in k^{\times}\).

Over every finite field \(\mathbb F_q\), including fields of characteristic two,
\[
\left|\mathcal N_2^{(1)}(\mathbb F_q)\setminus\mathcal R_2^{(1)}(\mathbb F_q)\right|
=q^2(q^2-1),
\]
\[
\left|\mathcal R_2^{(1)}(\mathbb F_q)\right|=(q^2-1)(2q+1),
\qquad
\left|\mathcal N_2^{(1)}(\mathbb F_q)\right|=(q^2-1)(q+1)^2.
\]

## Assumptions and scope

The algebra is the full associative matrix algebra with ordinary multiplication; no involution, Lie bracket, or symmetrized Jordan product is used. The operator rank refers to rank as a linear transformation on the \(n^2\)-dimensional vector space \(A\), not matrix rank of its image generator. All structural statements hold over arbitrary fields with no characteristic restriction. The cardinality statements require a finite field. The zero operator is excluded throughout.

## Proof

**1. Scalar reduction.** Write an arbitrary nonzero rank-one linear operator uniquely up to nonzero reciprocal scaling as
\[
N(X)=f(X)U,\qquad U\ne0,\ f\ne0.
\]
The Nijenhuis identity becomes
\[
f(X)f(Y)U^2=
\bigl(f(X)f(UY)+f(Y)f(XU)-f(U)f(XY)\bigr)U.
\tag{1}
\]
Choosing \(X,Y\) with \(f(X)f(Y)\ne0\) shows that \(U^2=\lambda U\) for some \(\lambda\in k\). Set \(c=f(U)\). If \(c=0\), equation (1) is exactly the weight-zero Rota–Baxter identity. Conversely, if \(N\) is rank-one weight-zero Rota–Baxter, putting \(X=U\) into that identity and using \(U^2=\lambda U\) yields \(c f(UY)=0\) for every \(Y\); setting \(Y=I\) gives \(c^2=0\), hence \(c=0\). Thus every rank-one weight-zero Rota–Baxter operator is Nijenhuis, and the Nijenhuis operators not of Rota–Baxter type are precisely the ones with \(c\ne0\).

**2. The matrix-size obstruction.** Suppose \(c\ne0\). For \(X,Y\in\ker f\), equation (1) gives \(f(XY)=0\); hence \(\ker f\) is a codimension-one multiplicatively closed linear subspace of \(M_n(k)\). Use the nondegenerate matrix-trace pairing to write uniquely \(f(X)=\operatorname{tr}(FX)\) with \(F\ne0\). The bilinear form
\[
B_F(X,Y)=\operatorname{tr}(FXY)
\]
vanishes on \(\ker f\times\ker f\). Relative to a vector-space splitting \(A=kE\oplus\ker f\), its matrix has a zero block of size \((n^2-1)\times(n^2-1)\), so \(\operatorname{rank}B_F\le2\). Nondegeneracy of trace pairing identifies the left contraction of \(B_F\) with left multiplication \(X\mapsto FX\), whose rank is \(n\operatorname{rank}F\). Therefore
\[
n\operatorname{rank}F=\operatorname{rank}B_F\le2,
\]
which forces \(n=2\) and \(\operatorname{rank}F=1\). Consequently equality of the two rank-one operator sets holds for every \(n\ge3\).

**3. The exact exceptional family in size two.** The subalgebra \(\ker f\) must contain \(I\). Indeed, otherwise the projection \(A=kI\oplus\ker f\to kI\cong k\) would be a unital algebra homomorphism, impossible for the simple noncommutative algebra \(M_2(k)\). Thus \(\operatorname{tr}F=f(I)=0\). Since \(F\) has matrix rank one, \(F^2=(\operatorname{tr}F)F=0\). Over any field, a nonzero square-zero \(2\times2\) matrix is conjugate to \(E_{12}\). In that basis \(f(X)=X_{21}\); for an arbitrary \(U=(u_{ij})\), direct matrix multiplication gives
\[
f(X)f(UY)+f(Y)f(XU)-f(U)f(XY)
=(\operatorname{tr}U)f(X)f(Y).
\]
Because \(f\ne0\), equation (1) is equivalent to \(U^2=(\operatorname{tr}U)U\). Cayley–Hamilton in size two makes this equivalent to \(\det U=0\). Since \(\operatorname{tr}(FU)\ne0\), \(U\ne0\) and therefore \(\operatorname{rank}U=1\). Conversely, every pair \((F,U)\) with the four displayed conditions satisfies the Nijenhuis identity and has \(c\ne0\), so cannot be Rota–Baxter. Finally \(N^2(X)=f(X)f(U)U=cN(X)\). In particular, the explicit exceptional projection \(N(X)=X_{21}E_{21}\) exists over every field, proving that the boundary at \(n=2\) is sharp.

**4. Counting exceptional operators.** There are exactly \(q^2-1\) nonzero square-zero matrices \(F\) in \(M_2(\mathbb F_q)\): choose the one-dimensional image/kernel line in \(q+1\) ways and a nonzero map from its one-dimensional quotient to that line in \(q-1\) ways. For each such \(F\), conjugate to \(E_{12}\). The condition \(\operatorname{tr}(FU)\ne0\) on a rank-one \(U=ab^{T}\) is \(a_2b_1\ne0\). It has \(q^2(q-1)\) distinct matrix solutions (divide the \(q^2(q-1)^2\) choices of factor pairs by the \(q-1\) scalar identifications). A rank-one linear operator has exactly \(q-1\) pairs of nonzero image generators and reciprocal functionals. Thus the number of exceptional operators is
\[
\frac{(q^2-1)q^2(q-1)}{q-1}=q^2(q^2-1).
\]

**5. Counting the Rota–Baxter complement in size two independently.** With \(c=0\), the scalar identity is equivalent to the existence of \(\alpha,\beta\in k\) such that
\[
f(XU)=\alpha f(X),\quad f(UY)=\beta f(Y),\quad\alpha+\beta=\lambda.
\]
Both \(\alpha\) and \(\beta\) are eigenvalues of multiplication by \(U\), hence satisfy \(t^2=\lambda t\). No nonzero scalar matrix \(U=\lambda I\) can occur: it would require \(\alpha=\beta=\lambda\) and \(\alpha+\beta=\lambda\), contradicting \(\lambda\ne0\). Every nonzero permissible \(U\) in size two therefore has matrix rank one. Its projective image-generator line is either nilpotent (\(q+1\) lines), or contains a unique rank-one idempotent (\(q(q+1)\) lines). For a normalized nilpotent generator \(U=E_{12}\), the above equations give \(\alpha=\beta=0\), and admissible \(f\) form a one-dimensional nonzero functional space: \(q-1\) choices. For an idempotent \(U=E_{11}\), the allowable eigenvalue pairs are \((\alpha,\beta)=(0,1)\) and \((1,0)\), each giving a one-dimensional nonzero off-diagonal functional space: \(2(q-1)\) choices. Hence
\[
\left|\mathcal R_2^{(1)}(\mathbb F_q)\right|
=(q+1)(q-1)+q(q+1)2(q-1)
=(q^2-1)(2q+1).
\]
Adding the disjoint exceptional family yields the claimed Nijenhuis count.

## Verification

The standalone script `verify_rankone_nijenhuis.py` checks every rank-one linear map \(M_2(\mathbb F_q)\to M_2(\mathbb F_q)\) for \(q=2,3,4\), with each one represented exactly once by normalizing its nonzero image generator. It tests the two operator identities on every ordered pair of matrix-unit basis elements; bilinearity makes this exhaustive. The script implements \(\mathbb F_4=\mathbb F_2[a]/(a^2+a+1)\) internally, without additional libraries. Run `python3 verify_rankone_nijenhuis.py` from the directory containing that file. It prints the counts \((15,27,12)\), \((56,128,72)\), and \((135,375,240)\), respectively (Rota–Baxter, Nijenhuis, exceptional), and ends with `RANKONE_NIJENHUIS_BOUNDARY_OK`.

These finite tests support but do not replace the all-fields proof. The proof uses only matrix algebra, trace duality, and Cayley–Hamilton, with no symbolic-experiment extrapolation.

## Relationship to prior work

The associative Nijenhuis identity and its relation to deformations of associative products are classical; the contraction framework of Cariñena, Grabowski, and Marmo and Ebrahimi-Fard's construction of free associative Nijenhuis algebras supply relevant context. Bremner and Elgendy distinguish the Nijenhuis and Rota–Baxter identities in their classification of quadratic operator identities. These works establish identities and general constructions, rather than the rank-one equality threshold for full matrix algebras, its exceptional normal form, or the finite-field difference count. Classifications of Nijenhuis operators on three-dimensional associative algebras concern different base algebras: \(M_2(k)\) is four-dimensional. The result makes no assertion that the two identities coincide for operators of higher rank.

## Limitations

No classification of higher-rank Nijenhuis or Rota–Baxter operators is claimed. The finite-field formula counts rank-one operators, not conjugacy classes. Algebraic-geometric singularities or irreducible components of the full operator varieties are not determined. The claim of distinction from prior literature is based on inspected primary works and targeted searches, not on proof of absolute publication priority. Independent mathematical validation has not been performed.

## References

1. J. F. Cariñena, J. Grabowski, G. Marmo, *Contractions: Nijenhuis and Saletan tensors for general algebraic structures*, arXiv:math/0103103 (first submitted 2001-03-16), https://arxiv.org/abs/math/0103103.
2. K. Ebrahimi-Fard, *On the associative Nijenhuis Relation*, arXiv:math-ph/0302062 (first submitted 2003-02-27), https://arxiv.org/abs/math-ph/0302062.
3. M. R. Bremner, H. A. Elgendy, *A new classification of algebraic identities for linear operators on associative algebras*, arXiv:2109.04391 (2021), https://arxiv.org/abs/2109.04391.
4. *Nijenhuis Operators on 2D Pre-Lie Algebras and 3D Associative Algebras*, *Axioms* 15 (2026), article 80, https://www.mdpi.com/2075-1680/15/1/80 (scope comparison only).
