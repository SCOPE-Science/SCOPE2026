# Socle detection of acyclic square-zero derivations on the characteristic-two truncated plane

## Finding
Let \(k\) be any field of characteristic \(2\), let \(A=k[x,y]/(x^2,y^2)\), and put \(z=xy\). For every \(k\)-derivation \(D:A\to A\) with \(D^2=0\), exactly one of the following holds:

1. \(D=0\); then \(\operatorname{rank}_k(D)=0\) and \(H(A,D)=A\).
2. \(D\ne0\) and \(D(z)=0\); then \(\operatorname{rank}_k(D)=1\) and the cohomology algebra \(H(A,D)=\ker D/\operatorname{im}D\) is isomorphic to \(k[\varepsilon]/(\varepsilon^2)\).
3. \(D(z)\ne0\); then \(\operatorname{rank}_k(D)=2\) and \(H(A,D)=0\).

For every finite field \(k=\mathbb F_q\) with \(q=2^e\), \(e\ge1\), the exact counts of square-zero derivations of ranks \(0,1,2\) are respectively
\[
1,\qquad (q+1)(q^2-1),\qquad q^2(q^2-1).
\]
There are no other ranks. Their total is \(q^4+q^3-q\); in particular the fraction giving acyclic differentials is
\[
\frac{q^2(q^2-1)}{q^4+q^3-q}\longrightarrow1\qquad(q\longrightarrow\infty\text{ through powers of }2).
\]
The distinguishing datum \(D(z)\) is intrinsic up to the choice of generator of the one-dimensional socle \(\operatorname{Soc}(A)=kz\).

## Assumptions and scope
The algebra is a four-dimensional, ungraded, commutative \(k\)-algebra with basis \(1,x,y,z\), relations \(x^2=y^2=0\) and \(xy=z\). A derivation is an ordinary \(k\)-linear Leibniz derivation; \(D^2\) means composition as a \(k\)-linear endomorphism. In characteristic \(2\), the square of a derivation is again a derivation. For \(D^2=0\), its image is an ideal of its kernel, so \(H(A,D)\) is a well-defined algebra. The zero algebra is admitted as the acyclic cohomology algebra. No grading-preservation or augmentation-preservation is assumed.

## Proof
**Coordinate model.** Every derivation has unique expressions
\[
D(x)=f=a_0+a_1x+a_2y+a_3z,\quad
D(y)=g=b_0+b_1x+b_2y+b_3z.
\]
Indeed, the relation \(x^2=y^2=0\) imposes no restriction because its Leibniz derivative is \(2xf\) or \(2yg\), both zero. Define
\[
\Phi(D)=\begin{pmatrix}
a_1+b_2&b_3&a_3\\
a_0&b_2&a_2\\
b_0&b_1&a_1
\end{pmatrix}.
\]
The matrix has trace zero, and its eight independent entries recover all eight coefficients. Thus \(\Phi\) is a \(k\)-linear isomorphism from \(\operatorname{Der}_k(A)\) to \(\mathfrak{sl}_3(k)\). In characteristic \(2\), \(D^2\) is a derivation; direct Leibniz expansion gives \(\Phi(D^2)=\Phi(D)^2\). For explicit verification, the coefficients of \(D^2(x)\) are
\[
(a_0a_1+b_0a_2,\ a_1^2+a_2b_1+a_3b_0,\ a_1a_2+a_3a_0+a_2b_2,\ a_2b_3+a_3b_2),
\]
and those of \(D^2(y)\) are
\[
(b_1a_0+b_2b_0,\ b_1a_1+b_2b_1+b_3b_0,\ b_1a_2+b_3a_0+b_2^2,\ b_1a_3+b_3a_1).
\]
These are precisely the eight coordinates extracted from the square of the displayed matrix. Polarizing squares also proves that \(\Phi\) respects Lie brackets; only the square identity is needed for the classification.

**Parametrization and socle criterion.** Every nonzero \(3\)-by-\(3\) matrix \(M\) with \(M^2=0\) has rank one: \(\operatorname{im}M\subseteq\ker M\) gives \(2\operatorname{rank}M\le3\), and the nonzero rank can only be one. Thus
\[
M=uv^{\mathsf T},\qquad u,v\in k^3\setminus\{0\},\quad v^{\mathsf T}u=0,
\]
unique up to \((u,v)\mapsto(cu,c^{-1}v)\) for \(c\in k^\times\). Write \(u=(u_0,u_1,u_2)\) and \(v=(v_0,v_1,v_2)\). Recovering the eight coefficients from \(\Phi(D)=uv^{\mathsf T}\) gives
\[
\begin{split}
D(x)&=u_1v_0+u_2v_2x+u_1v_2y+u_0v_2z,\\
D(y)&=u_2v_0+u_2v_1x+u_1v_1y+u_0v_1z.
\end{split}
\]
Consequently,
\[
D(z)=D(x)y+xD(y)=v_0(u_2x+u_1y+u_0z).
\]
The parenthesized vector is nonzero because \(u\ne0\); hence \(D(z)=0\) exactly when \(v_0=0\).

If \(v_0=0\), let \(h=u_2x+u_1y+u_0z\). Then \(D(x)=v_2h\), \(D(y)=v_1h\), \(D(z)=0\), and \((v_1,v_2)\ne(0,0)\). Thus \(\operatorname{im}D=kh\) and rank is one.

If \(v_0\ne0\), orthogonality \(v^{\mathsf T}u=0\) excludes \(u_1=u_2=0\), as that would force \(u_0=0\). Therefore at least one of \(D(x),D(y)\) has a nonzero constant term, while \(D(z)\ne0\) has no constant term; these two images are independent. Hence rank at least two. Since \(D^2=0\) on a four-dimensional space, rank at most two, proving equality.

**Cohomology algebras.** For nonzero rank-one \(D\), both generator images lie in the maximal ideal \(\mathfrak m=(x,y)\), so \(\operatorname{im}D\subseteq\mathfrak m\) and the unit class survives in \(H(A,D)\). Rank-nullity gives \(\dim_kH=4-2\cdot1=2\). Every element of \(\mathfrak m\) squares to zero because \(\operatorname{char}k=2\) and all basis monomials have square zero. Every class in \(H\) can be adjusted by a scalar multiple of the unit to lie in \(\mathfrak m\). Its square is therefore zero, establishing \(H\cong k[\varepsilon]/(\varepsilon^2)\). For rank-two \(D\), \(\dim_kH=4-2\cdot2=0\). For \(D=0\), \(H=A\).

**Finite-field counts.** Fix a projective covector \([v]\in\mathbf P^2(\mathbb F_q)\). For each projective choice of \(v\), the nonzero vectors \(u\in\ker(v^{\mathsf T})\) number \(q^2-1\). By normalizing \(v\) once per line, this counts each nonzero rank-one square-zero matrix exactly once. The line \(v_0=0\) has \(q+1\) projective points, while its complement has \(q^2\). Applying the proven rank criterion yields the two nonzero counts, and adding the zero derivation gives the total. The stated asymptotic follows from leading terms of the exact polynomials.

## Verification
Run `python3 check.py` using the standalone script supplied alongside this report. The script (i) exhaustively enumerates all derivations over \(\mathbb F_2\) and \(\mathbb F_4\), computes the images on \(1,x,y,xy\), tests the square-zero equation, and computes matrix rank directly; and (ii) independently enumerates the parametrized rank-one square-zero matrices over \(\mathbb F_2,\mathbb F_4,\mathbb F_8,\mathbb F_{16}\). The actual output ended in `SQUARE_ZERO_DERIVATION_RANK_OK`; observed rank counts were \((1,9,12)\) for \(q=2\) and \((1,75,240)\) for \(q=4\). The infinite-field and all-\(q\) statements are proved above, not inferred from finite experiments.

## Relationship to prior work
Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426v1 (2014), studies the same class of restricted derivation algebras but explicitly assumes characteristic greater than two and addresses regular elements/invariant theory, not square-zero differentials or their cohomology algebras. Earlier matrix nilpotent-orbit geometry, including Boos's 2012 dissertation, supplies the familiar rank-one nilpotent-matrix perspective, which is background rather than a claimed new theorem. The claimed distinct conclusion is the **intrinsic socle test for acyclicity, complete nonzero homology-algebra dichotomy, and rank-by-rank finite-field census** for this characteristic-two algebra. An independent search of relevant literature would still be needed to exclude all disguised prior formulations.

## Limitations
This statement is confined to two square-zero polynomial generators over fields of characteristic two. It classifies square-zero derivations and their ungraded cohomology algebras, not their automorphism-conjugacy classes or deformations as schemes. The matrix identification and rank-one nilpotent counts rely on classical linear algebra; their originality is not claimed. The scientific review is not an independent audit, and the possibility of an unlocated prior equivalent result remains.

## References
1. A. Premet, *Regular derivations of truncated polynomial rings*, arXiv:1405.2426v1, first public version 2014-05-10, https://arxiv.org/abs/1405.2426.
2. M. Boos, *Conjugation on varieties of nilpotent matrices*, doctoral dissertation, 2012, https://d-nb.info/1024305813/34 (background on matrix nilpotent-orbit geometry).
