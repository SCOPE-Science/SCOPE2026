# Arithmetic-rank strata and a genus-three nonordinary divisor for cyclic trigonal genus-six curves in characteristic five

## Finding
Let \(k\) be an algebraically closed field of characteristic \(5\). For \((a,b)\in k^2\), let \(C_{a,b}\) be the smooth projective model of
\[
 y^3=x^7+a x^3+b x+1.
\]
Set, with coefficients interpreted in \(\mathbb F_5\),
\[
\begin{aligned}
 D(a,b)&=2a^7-a^6b^3-a^3b^5+a^2b-2ab^4+b^7-2,\\
 H(a,b)&=a^5-2a^2b^2-b,\\
 R(z)&=1+2z^{13}-2z^6.
\end{aligned}
\]
On the open parameter set \(U=\{(a,b):D(a,b)\ne0\}\), the curve has genus \(6\). Its Jacobian's \(5\)-rank and its \(a\)-number are completely given by
\[
 f_5(C_{a,b})=\begin{cases}
 0,&a=0,\\
 0,&a\ne0,\ b=2a^{47},\ R(a^7)=0,\\
 2,&a\ne0,\ H(a,b)=0,\ b\ne 2a^{47},\\
 4,&a\ne0,\ H(a,b)\ne0,
 \end{cases}
 \qquad
 a(C_{a,b})=\begin{cases}4,&(a,b)=(0,0),\\2,&\text{otherwise}.
 \end{cases}
\]
The reduced locus of rank below \(4\) inside \(U\) is the union of the line \(a=0\) and the smooth, geometrically irreducible curve \(H=0\); these meet transversely at \((0,0)\). The smooth projective completion of \(H=0\) has genus \(3\). The rank-zero locus consists of the smooth portion of \(a=0\), together with exactly \(91\) further reduced geometric parameter points on \(H=0\), arranged in \(13\) orbits under the parameter rescaling by seventh roots of unity. The polynomial \(R(a^7)\) is squarefree, and all its roots produce smooth curves with rank zero and \(a\)-number \(2\).

## Assumptions and scope
The classification is for the displayed coefficient-marked family over an algebraic closure, **not** a classification of isomorphism classes or of all cyclic trigonal curves. In particular, the \(91\) parameters are not asserted to yield \(91\) pairwise nonisomorphic curves. The \(5\)-rank is the dimension of the stable Cartier image on \(H^0(C,\Omega_C^1)\); the \(a\)-number is the dimension of its Cartier kernel. The characteristic, equation, and discriminant-open condition are essential.

The resultant of \(f(x)=x^7+a x^3+b x+1\) and its formal derivative is \(D(a,b)\). Thus \(D\ne0\) is exactly the condition that the degree-seven branch polynomial be squarefree. Riemann--Hurwitz for the degree-three cover of \(\mathbb P^1\), ramified at its seven distinct finite roots and infinity, gives \(g=(3-1)(7-1)/2=6\).

## Proof
**Cartier blocks.** A basis of regular differentials is
\[
 V_1=\left\langle {dx\over y},{x\,dx\over y}\right\rangle,\qquad
 V_2=\left\langle {dx\over y^2},{x\,dx\over y^2},{x^2\,dx\over y^2},{x^3\,dx\over y^2}\right\rangle.
\]
Write \(\mathcal C\) for Cartier and, for a column of coefficients, \(w^{[5]}\) for componentwise fifth powers. In characteristic five it exchanges \(V_1\) and \(V_2\):
\[
 (\mathcal C|_{V_1}(w))^{[5]}=Aw,\qquad
 (\mathcal C|_{V_2}(v))^{[5]}=Bv,
\]
where the rows and columns follow the ordered bases above and
\[
 A=\begin{pmatrix}
 ab&-2a+b^3\\
 a^3-2b^2&b\\
 -2&-2a^2\\
 0&0
 \end{pmatrix},\qquad
 B=\begin{pmatrix}0&a&0&b\\0&0&1&0\end{pmatrix}.
\]
Indeed, for an input differential \(x^{i-1}dx/y^j\), choose \(j'\in\{1,2\}\) with \(5j'\equiv j\pmod 3\) and put \(n=(5j'-j)/3\). The output coefficient in position \(k\) before fifth-root extraction is the coefficient of \(x^{5k-i}\) in \(f^n\). Here \(n=3\) for \(V_1\to V_2\), and \(n=1\) for \(V_2\to V_1\). This also directly reproduces the displayed blocks.

**Stable rank.** Twice applying Cartier to \(V_1\) gives a semilinear map with
\[
 (\mathcal C^2(w))^{[25]}=Pw,\qquad
 P=B^{[5]}A=
 \begin{pmatrix}
 a^8-2a^5b^2&a^5b\\
 -2&-2a^2
 \end{pmatrix},\qquad
 \det P=-2a^5H(a,b).
\]
If \(a\ne0\) and \(H\ne0\), this has stable rank \(2\). If \(a=0\), then \(H=-b\) and, independently of \(b\), \(P=\bigl(\begin{smallmatrix}0&0\\-2&0\end{smallmatrix}\bigr)\); its second semilinear iterate is zero.

On \(H=0\) with \(a\ne0\), the matrix factors as
\[
 P=\binom{a^3b}{-2}\begin{pmatrix}1&a^2\end{pmatrix}=uv^{\mathsf T}.
\]
Its next semilinear iterate has rank \(1\) exactly when \(v^{[25]\mathsf T}u=a^3b-2a^{50}\ne0\); if that scalar vanishes, the iterate is zero. The two Cartier character spaces have equal stable dimension because Cartier bijectively permutes their stable images. Therefore the full stable rank is twice that of \(\mathcal C^2\) on \(V_1\), namely \(4\), \(2\), or \(0\) as stated. The scalar vanishes precisely at \(b=2a^{47}\). Substitution into \(H\) gives
\[
 H(a,2a^{47})=a^5R(a^7).
\]

**Exact exceptional count and smoothness.** The polynomial \(R\) has degree \(13\), constant term \(1\), and \(\gcd(R,R')=1\) in \(\mathbb F_5[z]\). Thus \(R(a^7)\) has \(91\) distinct nonzero roots in \(k\), and the substitution \(b=2a^{47}\) gives exactly that many rank-zero candidates away from \(a=0\). The exact Euclidean algorithm over \(\mathbb F_5[a]\) gives
\[
 \gcd\bigl(R(a^7),\ D(a,2a^{47})\bigr)=1,
\]
so all \(91\) are smooth parameters. Rescaling \(x\) by a seventh root of unity sends \((a,b)\mapsto(\zeta^3a,\zeta b)\) and acts freely on these \(91\) points. It therefore gives \(13\) orbits; no assertion about further isomorphisms is made.

**The \(a\)-number.** The matrix \(B\) has rank \(2\) away from \((0,0)\), and rank \(1\) at the origin. The fixed nonzero bottom row of \(A\) forces \(\operatorname{rank}(A)=1\) precisely when
\[
 H(a,b)=0,\qquad E(a,b):=b^3-2a-a^3b=0.
\]
A lexicographic Gröbner-basis calculation over \(\mathbb F_5\) gives the ideal identity
\[
 (H,E)=\bigl(b-2a^{12}-2a^5,\ a^{15}-2a^8-2a\bigr).
\]
Reducing \(D(a,2a^{12}+2a^5)\) modulo the second generator yields \(a^{14}-2a^7-2\). Hence every intersection of \(H=E=0\) except the origin is singular, and \((0,0)\) itself is smooth because \(D(0,0)=-2\). Therefore on the smooth locus \(A\) and \(B\) each have rank \(2\), except at the origin where each has rank \(1\). The Cartier rank is \(4\) or \(2\), giving the stated \(a\)-number.

**Geometry of the nonordinary divisor.** In characteristic five, \(H_a=ab^2\) and \(H_b=a^2b-1\) never vanish together; thus \(H=0\) is smooth. Setting \(Y=4a^2b+1\) and using \(H=0\) gives
\[
 Y^2=1+3a^7.
\]
This is a birational equivalence with a smooth hyperelliptic curve of genus \(3\) (the right-hand degree-seven polynomial is squarefree). In particular, \(H\) is geometrically irreducible. The line \(a=0\) meets \(H=0\) only at \((0,0)\), where \(H_b=-1\), so the intersection is transverse. Removing \(D=0\) yields the claimed divisor in \(U\).

## Verification
From the directory containing these files, run `python verify_symbolic.py` (SymPy required) and `python verify_finite_fields.py` (Python standard library only). The first independently recomputes the resultant, Cartier coefficient blocks, determinant, Gröbner eliminations, squarefreeness and discriminant coprimality for the \(91\) points. The second constructs the Cartier action by polynomial multiplication over \(\mathbb F_5\) and \(\mathbb F_{25}\), computes stable ranks through semilinear iteration, and checks squarefreeness using polynomial Euclid rather than the closed discriminant formula.

The finite-field replay finds respectively \(21\) and \(599\) smooth marked pairs. Over \(\mathbb F_5\), their \((5\text{-rank},a\text{-number})\) counts are \((0,2):3\), \((0,4):1\), \((2,2):3\), \((4,2):14\). Over \(\mathbb F_{25}\), the counts are \((0,2):23\), \((0,4):1\), \((2,2):21\), \((4,2):554\). These checks corroborate, but do not replace, the algebraically closed field proof.

## Relationship to prior work
Malmendier--Shaska (2019) supply the superelliptic cyclic-cover setting and genus calculation. Sutherland (2020) gives general coefficient formulas for Cartier--Manin blocks of superelliptic curves; the block extraction is standard and is not claimed as new. Bouw's generic cyclic-cover \(p\)-rank bounds and Lin--Mantovan--Singhal's (2023 preprint) generic Ekedahl--Oort results supply context rather than this specific stratification. The latter paper's principal theorem assumes at most five branch points and larger characteristic; here there are eight branch points and characteristic five. The contribution is the full exceptional-locus geometry, all exact rank and \(a\)-number strata, and the \(91\)-point and genus-three divisor structure for this sparse two-parameter family.

## Limitations
The coefficient family is a two-dimensional slice of all genus-six cyclic trigonal curves; no global moduli-classification claim is made. The thirteen seventh-root orbits are not asserted to be all geometric isomorphism classes of exceptional curves. The results do not determine Newton polygons or full Ekedahl--Oort types. Computations are exact, but no external independent validation has been performed. Unindexed related calculations cannot be ruled out absolutely.

## References
- A. Malmendier and T. Shaska, *From hyperelliptic to superelliptic curves*, Albanian J. Math. 13 (2019), 107--200; arXiv:1906.02373 (initial release June 6, 2019), Sections 1 and 5.
- A. V. Sutherland, *Counting points on superelliptic curves in average polynomial time*, ANTS XIV (2020), 403--422; arXiv:2004.10189 (initial release April 21, 2020), Section 2, especially Lemma 6, formula (8), and Theorem 8.
- I. Bouw, *The p-rank of ramified covers of curves*, Compos. Math. 126 (2001), 295--322, generic cyclic-cover bounds (background comparison).
- Y. Lin, E. Mantovan and D. Singhal, *Abelian covers of \(\mathbb P^1\) of \(p\)-ordinary Ekedahl--Oort type*, arXiv:2303.13350 (initial release March 23, 2023), Theorem 1.1.
