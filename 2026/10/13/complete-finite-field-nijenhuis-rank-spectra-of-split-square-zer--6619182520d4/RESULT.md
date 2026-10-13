# Complete finite-field Nijenhuis rank spectra of split square-zero local algebras

## Finding

Let \(K\) be any field, \(n\geq 1\), and let \(A=K1\oplus V\) be the unital associative algebra with \(\dim_K V=n\) and \(V^2=0\). A linear map \(N:A\to A\) is an associative Nijenhuis operator when
\[
N(x)N(y)=N\bigl(N(x)y+xN(y)-N(xy)\bigr)\quad\text{for every }x,y\in A.
\]
It is such an operator if and only if there exist a unique scalar \(a\in K\), vector \(u\in V\), and endomorphism \(T\in\operatorname{End}_K(V)\) with
\[
N(c1+v)=ca1+cu+T(v),\qquad Tu=au.
\]
In particular, this description is valid in arbitrary characteristic, including characteristic two.

For every finite field \(K=\mathbf F_q\), define the polynomial \(\mathcal R_{n,q}(X)=\sum_N X^{\operatorname{rank}N}\), where \(N\) ranges over all Nijenhuis operators on \(A\), counted as distinct linear maps. Write the Gaussian coefficient as \({d\brack r}_q\), with value zero if \(r<0\) or \(r>d\); put \(g_r=\prod_{i=0}^{r-1}(q^r-q^i)\), including \(g_0=1\). For integers \(0\le r\le n\), set
\[
\begin{aligned}
M_r&={n\brack r}_q^2g_r,\\
A_r&={n-1\brack r}_q{n-1\brack r-1}_qg_r,\\
B_r&=q^r{n-1\brack r}_q^2g_r,\\
F_0&=0,\qquad
F_r={n-1\brack r-1}_q q^{n-1}\prod_{i=0}^{r-2}(q^{n-1}-q^i)\quad(1\le r\le n).
\end{aligned}
\]
Empty products have value one. Then the **complete rank enumerator** is
\[
\boxed{\begin{aligned}
\mathcal R_{n,q}(X)={}&\sum_{r=0}^n M_r X^r
+(q^n-1)\sum_{r=0}^n\left(A_rX^r+B_rX^{r+1}\right)\\
&+(q-1)\sum_{r=0}^n\left(M_r+(q^n-1)F_r\right)X^{r+1}.
\end{aligned}}
\]
Consequently the number of Nijenhuis operators and the number of invertible Nijenhuis operators are, respectively,
\[
\boxed{q^{n^2-n+1}(2q^n-1)}\qquad\text{and}\qquad
\boxed{2(q-1)|\operatorname{GL}_n(\mathbf F_q)|}.
\]
These formulas count labeled maps relative to the fixed algebra \(A\), not isomorphism classes.

## Assumptions and scope

The algebra is commutative, unital and split local, with radical \(V\) and radical square zero. The arbitrary-field classification requires only the field axioms. The rank distribution, the total count and the invertible count assume a finite field of order \(q\), where \(q\) is any prime power. No separability, algebraic closedness or restriction on characteristic is used. The operator rank is the ordinary \(K\)-linear rank on the \((n+1)\)-dimensional vector space \(A\). The case \(n=0\) is deliberately excluded.

## Proof

**1. Necessary and sufficient normal form.** Write
\[
N(1)=a1+u,\qquad N(v)=f(v)1+T(v)
\]
for a scalar \(a\), vector \(u\), functional \(f\in V^*\), and linear map \(T:V\to V\). For each \(v\in V\), substitute \(x=y=v\) into the Nijenhuis identity. Since \(v^2=0\), its left-hand scalar component is \(f(v)^2\), whereas the scalar component of the right-hand side is \(2f(v)^2\). Thus \(f(v)^2=0\). A field has no nonzero square-zero scalars, so \(f=0\), even in characteristic two. Substituting \(x=y=1\) now gives
\[
(a1+u)^2=N(a1+u),\quad
 a^2\cdot1+2au=a^2\cdot1+au+Tu,
\]
so \(Tu=au\). Conversely, with \(f=0\) and \(Tu=au\), the identity on the generator pairs \((1,1)\), \((1,v)\), \((v,1)\), and \((v,w)\) holds: in each pair involving an element of \(V\), the product \(V^2=0\) eliminates all remaining terms. Bilinearity proves the identity for all elements. Uniqueness is immediate from \(N(1)\) and \(N|_V\).

**2. The rank stratification.** Relative to \(K1\oplus V\), a Nijenhuis operator has column-block form
\[
N=\begin{pmatrix}a&0\\u&T\end{pmatrix},\qquad Tu=au.
\]
Fix \(r=\operatorname{rank}T\). There are \(M_r={n\brack r}_q^2g_r\) choices for \(T\): choose an \((n-r)\)-dimensional kernel, an \(r\)-dimensional image and an isomorphism from the quotient by the kernel onto the image.

If \(a=u=0\), then \(\operatorname{rank}N=r\), giving \(M_rX^r\). Suppose next that \(a=0\) and \(u\ne0\). For each fixed \(u\), the relation \(Tu=0\) requires \(u\in\ker T\). If \(u\in\operatorname{im}T\), the number of \(T\) of rank \(r\) is
\[
{n-1\brack r}_q{n-1\brack r-1}_qg_r=A_r,
\]
because its kernel contains \(u\), its image contains \(u\), and its induced quotient-to-image map is invertible. In this case the image of \(N\) equals \(\operatorname{im}T\), and \(\operatorname{rank}N=r\). If \(u\notin\operatorname{im}T\), the number is
\[
{n-1\brack r}_q\left(q^r{n-1\brack r}_q\right)g_r=B_r;
\]
indeed, \(q^r{n-1\brack r}_q\) counts the \(r\)-subspaces not containing the fixed nonzero vector \(u\). Now \(\operatorname{rank}N=r+1\). There are \(q^n-1\) choices of \(u\), giving the entire second sum.

Finally suppose \(a\ne0\). The top-left scalar entry is invertible, so always \(\operatorname{rank}N=r+1\). For \(u=0\), there are \(M_r\) choices of \(T\). For fixed \(u\ne0\), the equation \(Tu=au\) forces \(u\) into the image \(J=\operatorname{im}T\), so \(r\ge1\). Choose \(J\) in \({n-1\brack r-1}_q\) ways. Modulo \(Ku\), the map \(T\) induces a surjection
\[
V/Ku\longrightarrow J/Ku
\]
with \(\prod_{i=0}^{r-2}(q^{n-1}-q^i)\) possibilities. Each such surjection has exactly \(q^{n-1}\) linear lifts \(T\) with the prescribed \(T(u)=au\). Thus the number is \(F_r\); this also establishes the conventions at the endpoints. Multiplying by the \(q-1\) choices of \(a\) and \(q^n-1\) nonzero vectors \(u\) yields the final sum. The cases are disjoint and exhaustive, proving the polynomial.

**3. Total and invertible counts.** Sum over \(T,u\) and translate \(T\mapsto T-aI\). For each fixed scalar \(a\), the total number of pairs satisfying \(Tu=au\) is
\[
\sum_{S\in\operatorname{End}(V)}|\ker S|
=q^{n^2}+(q^n-1)q^{n(n-1)},
\]
counting separately \(u=0\) and \(u\ne0\) with \(S(u)=0\). Multiplication by \(q\) choices of \(a\) simplifies to \(q^{n^2-n+1}(2q^n-1)\).

The displayed block matrix is invertible exactly when \(a\ne0\) and \(T\) is invertible. Fix \(a\ne0\). The choice \(u=0\) admits \(|\operatorname{GL}_n|\) matrices. For each fixed nonzero \(u\), invertible \(T\) satisfying \(Tu=au\) number \(q^{n-1}|\operatorname{GL}_{n-1}|\), since the image of the distinguished basis vector is fixed and the other columns form an arbitrary invertible quotient map with free components along that vector. Since
\[
(q^n-1)q^{n-1}|\operatorname{GL}_{n-1}|=|\operatorname{GL}_n|,
\]
there are \(2|\operatorname{GL}_n|\) choices for each nonzero \(a\), as claimed.

## Verification

Run `python3 verify_nijenhuis_squarezero.py` from a directory containing the attached checker. It computes field arithmetic directly (including a representation of \(\mathbf F_4\)), derives the predicted Gaussian-coefficient distributions, and separately tests the Nijenhuis identity on all basis pairs. It exhaustively enumerates every linear map for \((n,q)=(1,2),(1,3),(2,2),(2,3),(3,2)\), and independently enumerates the normal-form parameters over \(\mathbf F_4\) for \(n=2\). The corresponding rank histograms are reported by the checker; successful completion prints `VERIFY_OK`. Exhaustive tests over these finite cases do not constitute a proof for arbitrary dimensions or fields; the proof above is algebraic.

## Relationship to prior work

Gao, Kang, Lü and collaborators, arXiv:2308.12121 (first released 23 August 2023), enumerate Nijenhuis operators on complex associative algebras of dimension three, including the algebra denoted \(C_{10}\), which is exactly the \(n=2\) specialization here. Their Theorem 4.1 and Appendix Table 4 therefore already cover the complex three-dimensional normal forms. The present result does not claim those as new: it gives a single arbitrary-field, all-dimensional structural criterion, plus a closed rank polynomial, total count, and invertible count over every finite field. Earlier work arXiv:1805.03307 analyzes graded homogeneous Nijenhuis operators on nonunital null-filiform associative algebras, which have different multiplication. The general identities in arXiv:2109.04391 do not tabulate this family's finite-field rank distribution. The counts concern Nijenhuis operators, not Rota–Baxter operators, whose defining equation is different.

Classical Gaussian counting of matrices by rank is used explicitly in the proof, rather than claimed as original. The new assertion is the complete Nijenhuis-constrained rank distribution obtained after reducing the operator identity. Searches have not excluded every potential equivalent formulation in the literature.

## Limitations

No assertion is made about arbitrary noncommutative algebras, nonsplit local algebras, algebras whose radical cube rather than its square vanishes, or automorphism-orbit classifications. No independent audit has been performed. The arbitrary-field structural classification has no finite-field restriction; the enumerator requires finite \(q\). The finite verification covers only the specified cases and cannot prove an infinite statement or establish originality.

## References

1. X. Gao et al., *Nijenhuis operators on 2D pre-Lie algebras and 3D associative algebras*, arXiv:2308.12121v3 (first publicly posted as arXiv:2308.12121v1 on 2023-08-23), Sections 2, 4, Appendix Table 4.
2. I.A. Karimjanov, I. Kaygorodov, M. Ladra, *Rota-type operators on null-filiform associative algebras*, arXiv:1805.03307v1 (2018), Sections 2–3.
3. M. R. Bremner, H. A. Elgendy, *A new classification of algebraic identities for linear operators on associative algebras*, arXiv:2109.04391v1 (2021), operator identities and structural relations.
