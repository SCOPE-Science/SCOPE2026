# Rota–Baxter operators on a simple two-dimensional evolution algebra: a characteristic-\(31\) resonance

## Finding
Let \(K\) be any field and let \(E=K e_1\oplus K e_2\) be the evolution algebra with \(e_1^2=e_2\), \(e_2^2=e_1+e_2\), and \(e_1e_2=0\). Put \(P(T)=T^3-T^2-1\) and \(\mathcal T=\{t\in K:P(t)=0\}\), of cardinal \(m\le3\). A linear map \(R:E\to E\) has Rota–Baxter weight \(\lambda\in K\) when
\[
R(x)R(y)=R(R(x)y+xR(y)+\lambda xy)\quad(x,y\in E).
\]

**Nonzero weights.** For every \(\lambda\ne0\), all operators are the zero operator, \(-\lambda\operatorname{id}_E\), and, for each ordered pair \((u,v)\in\mathcal T^2\) with \(u\ne v\), the operator \(-\lambda\Pi_{u,v}\), where \(\Pi_{u,v}\) is the projection onto \(K(e_1+u e_2)\) along \(K(e_1+v e_2)\). Explicitly, in the basis \((e_1,e_2)\),
\[
-\lambda\Pi_{u,v}=
\frac{-\lambda}{u-v}
\begin{pmatrix}-v&1\\-uv&u\end{pmatrix}.
\]
There are exactly \(2+m(m-1)\) distinct operators for every nonzero weight. Every one is a *splitting* Rota–Baxter operator: \(R^2=-\lambda R\).

**Weight zero.** If \(\operatorname{char}K\ne31\), the zero map is the only weight-zero operator. If \(\operatorname{char}K=31\), the full family is the affine line
\[
R_c=c\begin{pmatrix}-11&1\\-11^2&11\end{pmatrix},\qquad c\in K,
\]
with \(R_c^2=0\). The exceptional parameter \(11\) is the repeated root of \(P\) in characteristic \(31\).

The algebra \(E\) is simple and perfect over every field. In particular, if \(K\) is algebraically closed, the count for nonzero weight is \(8\) except in characteristic \(31\), where it is \(4\). For \(K=\mathbb F_q\), the count for weight zero is \(q\) in characteristic \(31\) and \(1\) otherwise; the nonzero-weight count is \(2+m_q(m_q-1)\), where \(m_q\) counts roots of \(P\) in \(\mathbb F_q\).

## Assumptions and scope
All fields and all their characteristics are admitted, including \(2\), \(3\), and \(31\); \(\lambda\) is arbitrary. Operators need not preserve the natural basis, be diagonal, or be invertible. The algebra is commutative but nonassociative. Multiplication on arbitrary vectors follows by bilinearity from the displayed natural-basis table. No algebraic-closure assumption is used for the classification over \(K\).

## Proof

**1. Basic structure.** For \(z=x e_1+y e_2\), one has \(z^2=y^2e_1+(x^2+y^2)e_2\). Hence \(z^2=0\) implies \(z=0\), in every characteristic. A nonzero one-dimensional subalgebra has a spanning vector \(e_1+t e_2\): a spanning vector with first coordinate zero cannot have its square in its own line. The equality
\[
(e_1+t e_2)^2=t^2(e_1+t e_2)
\]
is equivalent to \(t^3-t^2-1=0\). Such a \(t\) is nonzero, and the square of every nonzero vector in its line is nonzero.

There are no nonzero proper ideals: if \(z=xe_1+ye_2\) generates a one-dimensional ideal, then \(ze_1=xe_2\) and \(ze_2=y(e_1+e_2)\) must both belong to \(Kz\). The cases \(x=0\), \(y=0\), and \(xy\ne0\) each contradict this. Therefore \(E\) is simple. Since \(e_2=e_1^2\) and \(e_1=e_2^2-e_2\), it is perfect.

Its only algebra endomorphisms are \(0\) and \(\operatorname{id}\). Indeed, simplicity makes every nonzero endomorphism invertible. To classify automorphisms, write \(F(e_1)=a e_1+c e_2\), \(F(e_2)=b e_1+d e_2\). The equation \(F(e_1)F(e_2)=0\) forces \(cd=0\), \(ab=0\). Invertibility leaves either the diagonal case \(b=c=0\) or the antidiagonal case \(a=d=0\). The latter contradicts \(F(e_1)^2=F(e_2)\); in the former the two square relations give \(d=a^2\), \(a=d^2\), \(d=d^2\), whence \(a=d=1\).

Finally, all derivations vanish. For a derivation \(D(e_1)=a e_1+c e_2\), \(D(e_2)=b e_1+d e_2\), applying it to \(e_1e_2=0\) yields \(b=c=0\); the equations for \(e_1^2=e_2\) and \(e_2^2=e_1+e_2\) then give \(d=2a\), \(a=2d\), and \(d=2d\), so \(a=d=0\). These arguments work in every characteristic.

**2. Reduction to weights zero and one.** For \(\lambda\ne0\), \(R\) has weight \(\lambda\) exactly when \(\lambda^{-1}R\) has weight one. We first classify weight one.

**3. Invertible weight-one operators.** Suppose \(R\) is invertible and has weight one. Put \(Q=R^{-1}\). Replacing \(x,y\) in the Rota–Baxter identity by \(Q(u),Q(v)\) gives
\[
Q(uv)=Q(u)v+uQ(v)+Q(u)Q(v).
\]
Thus \(F=\operatorname{id}+Q\) is an algebra endomorphism. By Step 1, \(F\) is zero or the identity. The identity would imply \(Q=0\), impossible; hence \(Q=-\operatorname{id}\) and \(R=-\operatorname{id}\).

**4. Rank-one weight-one operators.** Suppose \(R\) has rank one. Its image is a subalgebra because products \(R(x)R(y)\) belong to the image. Its kernel is a subalgebra: if \(R(x)=R(y)=0\), the weight-one identity gives \(R(xy)=0\). If image and kernel coincided in a line \(U=Ku\), choose \(v\) such that \(R(v)=u\). For \(x=u,y=v\), the identity reduces to \(R(u^2+uv)=0\). Since \(U\) is a subalgebra, \(u^2\in U=\ker R\), so \(uv\in U\). Along with \(u^2\in U\), this would make \(U\) an ideal, contrary to simplicity. Consequently image and kernel are distinct one-dimensional subalgebras: some ordered pair \((u,v)\) of distinct roots of \(P\) determines them.

Let \(z\ne0\) span the image, so \(z^2=\kappa z\) with \(\kappa\ne0\), and \(R(z)=\tau z\), with \(\tau\ne0\). Applying the weight-one identity to \((z,z)\) gives \(\tau^2\kappa=(2\tau+1)\tau\kappa\), so \(\tau=-1\). Therefore \(R\) is minus the projection onto its image along its kernel. Conversely, if \(E=U\oplus V\) with both lines subalgebras, direct expansion of the defining identity shows that \(-\Pi_U\) has weight one; the displayed projection matrix follows by solving coordinates. Adding the zero and invertible cases proves the nonzero-weight classification.

**5. Weight zero: invertible and rank-one cases.** If a weight-zero \(R\) is invertible, the same substitution as in Step 3 shows \(R^{-1}\) is a derivation, contradicting Step 1. Let a nonzero rank-one weight-zero \(R\) have image \(U=Ku\). The image is a subalgebra; let \(u^2=\kappa u\) with \(\kappa\ne0\), and write \(R(u)=\tau u\). Applying the weight-zero identity to \((u,u)\) gives \(\tau^2\kappa=2\tau^2\kappa\), hence \(\tau=0\). Thus \(\operatorname{im}R=\ker R=U\).

Write \(u=e_1+t e_2\), with \(P(t)=0\), and \(\phi(xe_1+ye_2)=y-tx\). Then every such operator has the unique form \(R=c\,u\phi\) for some \(c\in K^\times\). Since \(u^2=t^2u\) and \(ue_2=t(e_1+e_2)\), substituting the basis \((u,e_2)\) in the weight-zero identity shows that it holds precisely when
\[
t^2=2\phi(ue_2)=2t(1-t),\qquad\text{equivalently }3t=2.
\]
If \(\operatorname{char}K=2\) or \(3\), this has no solution with \(P(t)=0\). Otherwise \(t=2/3\) and \(P(2/3)=-31/27\), so a solution exists precisely in characteristic \(31\), when \(t=11\). This yields exactly the stated family, including \(c=0\). Its members square to zero because \(\phi(u)=0\).

**6. Discriminant.** The polynomial \(P(T)=T^3-T^2-1\) has integer discriminant \(-31\). In characteristic \(31\) it factors as \((T-11)^2(T-10)\), giving the two distinct one-dimensional subalgebras and their four weight-one operators over any algebraically closed field of that characteristic. In other characteristics an algebraic closure has three distinct roots and therefore eight weight-one operators.

## Verification
Run `python3 verify.py` from the directory containing this file. The standalone standard-library checker exhaustively enumerates *all four matrix entries* over \(\mathbb F_q\) for \(q=2,3,4,5,7,8,11,13,31\), for both weights zero and one, directly tests the six scalar forms of the Rota–Baxter identity, and compares the full solution sets—not just counts—with the classification. Characteristic \(31\) is explicitly tested. For \(q=4\) and \(8\), the verifier implements polynomial-basis finite-field arithmetic, not integer residues. It prints `VERIFY_OK` when every comparison succeeds.

## Relationship to prior work
Kaygorodov, Martín González and Viruel's survey (arXiv:2610.22248v1, posted 2026-10-15), Question 39, asks for graph-sensitive Rota–Baxter classifications on perfect evolution algebras. The present theorem completely handles **all linear operators, of every weight and every characteristic**, on a canonical strongly connected two-vertex example. Qaralleh, Mukhamedov and Khakimov (arXiv:2601.08669v1, 2026-01-13) classify operators on maximal-nilindex **nilpotent** evolution algebras with acyclic graphs. Their results do not apply to this simple perfect algebra. The projection characterization uses the elementary general splitting construction, but the exhaustion of all possibilities, the root count, and the characteristic-\(31\) weight-zero exception require the argument above.

## Limitations
The result is a complete set-theoretic classification for one specified simple perfect algebra, not for arbitrary perfect evolution algebras. The count records distinct linear maps over the chosen field, not nonreduced scheme multiplicities. Historical priority outside the inspected sources is not established. Exhaustive tests over finitely many fields do not independently prove the infinite-field assertion; that follows from Steps 1–6.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, 2026-10-15, Question 39, https://arxiv.org/html/2610.22248v1 .
2. I. Qaralleh, F. Mukhamedov, O. Khakimov, *Rota-Baxter operators of nilpotent evolution algebras with maximal nilindex*, arXiv:2601.08669v1, 2026-01-13, https://arxiv.org/html/2601.08669v1 .
