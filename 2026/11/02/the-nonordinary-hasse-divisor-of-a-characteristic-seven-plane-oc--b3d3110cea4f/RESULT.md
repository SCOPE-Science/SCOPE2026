# The nonordinary Hasse divisor of a characteristic-seven plane-octic pencil

## Finding
Let \(k\) be an algebraically closed field of characteristic \(7\). For \(\lambda\in k\setminus\{1,-1\}\), put
\[
 C_\lambda:\quad Y^8-X^7Z-XZ^7-\lambda(Y^2-2XZ)^4=0\quad\subset\mathbb P^2_k.
\]
Every \(C_\lambda\) is smooth of genus \(21\). Its geometric \(7\)-rank \(f\) and its \(a\)-number satisfy
\[
 (f(C_\lambda),a(C_\lambda))=
 \begin{cases}(0,21),&\lambda=0,\\(14,7),&\lambda^2=2,\\(21,0),&\lambda\ne0,\ \lambda^2\ne2.\end{cases}
\]
In particular, the two roots of \(\lambda^2=2\) in \(k\) are \(3\) and \(-3\). In the standard ordered residue-form basis of \(H^1(C_\lambda,\mathcal O_{C_\lambda})\), the characteristic-seven Hasse–Witt matrix \(H_\lambda\) satisfies the exact polynomial identity
\[
 \det H_\lambda=-\lambda^{21}(\lambda^2-2)^7\in\mathbb F_7[\lambda].
\]
Thus the determinant-defined nonordinary Cartier divisor on the smooth parameter line is \(21[0]+7[3]+7[-3]\), as an effective divisor with scheme multiplicities. The underlying nonordinary locus is exactly the three geometric parameters \(0,3,-3\). These statements concern coefficient-marked members of the displayed pencil, not a count of isomorphism classes.

## Assumptions and scope
Everything is geometric over an arbitrary algebraically closed field of characteristic \(7\). The two excluded parameter values are precisely the singular members of the displayed projective family. The \(7\)-rank means the dimension of the geometric \(7\)-torsion étale part of the Jacobian; the \(a\)-number is \(\dim_k\operatorname{Hom}(\alpha_7,J(C_\lambda))\), equivalently the nullity of the Cartier operator on regular differentials. The displayed determinant is relative to the stated monomial ordering and is therefore a specific polynomial, while its vanishing divisor is invariant under invertible basis changes.

## Proof
**Smoothness and genus.** Write \(Q=Y^2-2XZ\), \(F=Y^8-X^7Z-XZ^7-\lambda Q^4\). Direct differentiation in characteristic \(7\) yields
\[
 F_X=-Z^7+\lambda ZQ^3,\quad F_Y=Y^7-\lambda YQ^3,\quad F_Z=-X^7+\lambda XQ^3.
\]
If all partial derivatives vanish, then \(Q\ne0\), since otherwise all coordinates would vanish. Set \(c=\lambda Q^3\). Then \(c\ne0\) and \(X^7=cX,\ Y^7=cY,\ Z^7=cZ\). Consequently \(Q^7=c^2Q\), hence \(c^2=Q^6\), so \(\lambda^2=1\). Because the degree \(8\) is congruent to \(1\) modulo \(7\), Euler's identity implies \(F=0\) wherever all partials vanish. Conversely, \([0:1:0]\) is singular at \(\lambda=1\), and \([1:0:1]\) is singular at \(\lambda=-1\). Thus the smoothness assertion follows. The genus is \((8-1)(8-2)/2=21\).

**Independent quotient and \(7\)-rank.** Work on \(Z=1\) with coordinates \(x,y\). For every \(b\in\mathbb F_7\), the automorphism \((x,y)\mapsto(x+by+b^2/2,y+b)\) preserves \(Q=y^2-2x\) and the equation, and defines an order-seven action. Let \(\xi=y^2-2x\) and \(\eta=y^7-y\). These generate the invariant function field, and substituting \(x=(y^2-\xi)/2\) into \(F=0\) gives the identity
\[
 E_\lambda:\quad\eta^2=\xi^7+\xi-2\lambda\xi^4.
\]
This is a smooth genus-three hyperelliptic curve because the derivative of its right-hand side is \(1-8\lambda\xi^3=1-\lambda\xi^3\); a repeated root would simultaneously satisfy the original equation, which occurs precisely when \(\lambda^2=1\) (or follows from smoothness of the quotient away from the unique fixed point). Alternatively the quotient can be checked directly at every smooth parameter. The order-seven action has just one fixed point, the unique point \([1:0:0]\) at infinity. Thus Deuring–Shafarevich gives
\[
 f(C_\lambda)-1=7(f(E_\lambda)-1)+(7-1),\qquad f(C_\lambda)=7f(E_\lambda).
\]
Set \(a=-2\lambda\). For \(h(\xi)=\xi^7+a\xi^4+\xi\), the genus-three Hasse–Witt coefficients from \(h(\xi)^3\) give the diagonal matrix \(\operatorname{diag}(3a,a^3-a,3a)\). Its stable semilinear rank equals its rank here: the three one-dimensional diagonal subspaces are preserved by Frobenius. The rank is \(0\) when \(a=0\), \(2\) when \(a\ne0\) and \(a^2=1\), and \(3\) otherwise. Since \(a^2=4\lambda^2\) and \(4^{-1}=2\) in \(\mathbb F_7\), these cases give \(f(C_\lambda)=0,14,21\), respectively.

**Exact Cartier determinant and \(a\)-number.** Index the \(21\) monomial residue classes by triples \(u=(u_X,u_Y,u_Z)\) of nonnegative integers satisfying \(u_X+u_Y+u_Z=5\), in lexicographic order \((i,j,5-i-j)\) with increasing \(i\), then increasing \(j\). The Hasse–Witt coefficient formula on a smooth degree-eight plane curve in characteristic seven is
\[
 (H_\lambda)_{v,u}=[X^{7(u_X+1)-v_X-1}Y^{7(u_Y+1)-v_Y-1}Z^{7(u_Z+1)-v_Z-1}]\,F_\lambda^6.
\]
This follows from the standard Cartier/Frobenius residue description and fixes the normalization of the claimed determinant. Expand \(F_\lambda^6\) with the multinomial theorem over \(\mathbb F_7[\lambda]\). Entries have nonzero support only within eleven common row/column index sets (zero-based in the specified order):

| Size | Index sets | Determinants |
| --- | --- | --- |
| \(1\) | \(\{0\},\{1\},\{19\},\{20\}\) | \(\lambda\) each |
| \(2\) | \(\{2,6\},\{3,7\},\{14,16\},\{17,18\}\) | \(-\lambda^2(\lambda^2-2)\) each |
| \(3\) | \(\{4,8,11\},\{5,9,12\},\{10,13,15\}\) | \(-\lambda^3(\lambda^2-2)\) each |

The support assertion and every polynomial block determinant are exact consequences of the displayed coefficient formula; the standalone program `verify_hasse.py` builds all entries by an exhaustive finite multinomial expansion (not by numerical interpolation), finds the connected row-column support blocks and computes their polynomial determinants using recursive Laplace expansion in \(\mathbb F_7[\lambda]\). These are finite exact identities, and the program includes independent evaluations of the full matrix at every prime-field parameter. Multiplying the eleven block determinants, with their identity row/column order, gives exactly \(-\lambda^{21}(\lambda^2-2)^7\).

At \(\lambda=0\), every entry vanishes. At either root \(\lambda=\pm3\) of \(\lambda^2=2\), the four singleton blocks have rank one, each of the four \(2\)-blocks has rank one and each of the three \(3\)-blocks has rank two (in the last case the upper-left \(2\)-minor is nonzero, as checked by exact coefficient arithmetic). The total rank is \(4+4+6=14\). Everywhere else the determinant is nonzero, so rank is \(21\). Because the \(a\)-number is the nullity of the Cartier–Manin matrix, its values are \(21,7,0\) as asserted. All characteristic-seven parameters are covered because the rank-drop conditions are polynomial identities, not just checks at \(\mathbb F_7\)-points.

## Verification
Run `python3 verify_hasse.py` and `python3 verify_quotient.py` with Python 3 standard library; both programs are included alongside this document. The first computes the complete \(21\)-by-\(21\) Hasse–Witt matrix and its eleven polynomial block determinants, proves the exact determinant identity by finite symbolic expansion, and checks specialized ranks. The second checks invariance, the quotient identity, the quotient Hasse matrix, and geometric smoothness at all rational prime-field test points. The general smoothness, quotient, \(7\)-rank and Cartier claims are established algebraically above, not inferred from the finite-field tests. The programs do not certify literature originality or constitute independent external mathematical audit.

## Relationship to prior work
Borges, Korchmáros and Speziali [1] introduce the characteristic-seven invariant octic pencil, identify its symmetry and characteristic-seven quotient, and establish generic ordinarity in an appropriate general family. These definitions and antecedent results are credited, not claimed as new. Novoselov [2] provides general Cartier–Manin methods for hyperelliptic models of the quotient type. The additional claim here is the **complete geometric nonordinary stratification and scheme-multiplicity formula for the degree-\(21\) Hasse determinant of the parent octic**, together with the exact \(a\)-number at every smooth parameter; the independent quotient calculation interprets the accompanying \(7\)-ranks. Prior hyperelliptic formulas by themselves do not imply the parent curve's Cartier nullity or nonordinary divisor multiplicities.

## Limitations
The assertion is limited to characteristic \(7\), the displayed coefficient-marked pencil, and smooth parameters \(\lambda\ne\pm1\). It does not classify its members up to isomorphism, its singular members, or all Ekedahl–Oort types. The determinant multiplicity is a Hasse-section multiplicity in the chosen one-parameter family, not a geometric intersection multiplicity in a moduli space. A matching unindexed earlier explicit computation cannot be excluded; novelty is conditional on the reviewed accessible literature. Independent mathematical audit has not been performed.

## References
[1] F. Borges, G. Korchmáros and P. Speziali, *Plane curves with a large linear automorphism group in characteristic p*, arXiv:2202.05765v1 (first public 2022-02-11), https://arxiv.org/abs/2202.05765 . Full text: Sections 3, 4.8 and 8.1.

[2] R. Novoselov, *Counting points on hyperelliptic curves of type \(y^2=x^{2g+1}+ax^{g+1}+bx\)*, arXiv:1902.05992v1 (first public 2019-02-15), https://arxiv.org/abs/1902.05992 . Full text: Section 2, including Theorem 4.
