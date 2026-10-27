# Five resonance regimes for square-zero elements in a three-generator quantum exterior algebra

## Finding
Let \(k\) be any field, \(t\in k^\times\), and
\[
 A_t=k\langle x,y,z\rangle/(x^2,y^2,z^2,\ yx-txy,\ zx-txz,\ zy-tyz).
\]
Its radical \(J=(x,y,z)\) has dimension seven. Write uniquely
\[
 u=ax+by+cz+dxy+exz+fyz+gxyz,\qquad (a,b,c,d,e,f,g)\in k^7.
\]
The square-zero locus \(X_t=\{u\in A_t:u^2=0\}\), viewed as a *reduced* affine variety, has precisely the following five geometric regimes. In the table, component dimensions are listed with multiplicity; \(\mathbb L=[\mathbb A^1_k]\) is the affine-line class in the Grothendieck ring of varieties, and \(T_t(s)\) is the polynomial satisfying \([X_t]=T_t(\mathbb L)\).

| Field and parameter | Irreducible-component dimensions | \(T_t(s)\) |
|---|---|---|
| \(\operatorname{char}k=2,\ t=1\) | \(7\) | \(s^7\) |
| \(\operatorname{char}k=2,\ t\ne1\) | \(5,4,4\) | \(s^5+2s^4-2s^3\) |
| \(\operatorname{char}k\ne2,\ t=-1\) | \(6\) | \(s^6+s^4-s^3\) |
| \(\operatorname{char}k\ne2,\ t^2=-1\) | \(5,5,4\) | \(2s^5-s^3\) |
| \(\operatorname{char}k\ne2,\ t\ne-1,\ t^2\ne-1\) | \(4,4,4,4\) | \(4s^4-3s^3\) |

In the third regime, \(X_t\) is the irreducible split quadratic hypersurface \(af-be+cd=0\) in \(\mathbb A^7_k\). Its singular locus is the one-dimensional line \(a=b=c=d=e=f=0\). In the first regime \(X_t=\mathbb A^7_k\). In all other regimes every component is a linear affine subspace; the reduced singular locus is exactly the union of their pairwise intersections.

For every finite field \(k=\mathbb F_Q\) and every \(t\in\mathbb F_Q^\times\), \(\#X_t(\mathbb F_Q)=T_t(Q)\). More strongly, if \(\rho(u)=\dim_{\mathbb F_Q}uA_t\), the **complete regular-multiplication rank polynomial** is
\[
 \boxed{\quad\sum_{u^2=0} w^{\rho(u)}
 =1+(Q-1)w+(Q^4-Q)w^2+(T_t(Q)-Q^4)w^4.\quad}
\]
There are no square-zero elements of regular-multiplication rank three. For any field, every square-zero element with nonzero linear part has rank four, hence defines an acyclic differential \(L_u:A_t\to A_t\); those with zero linear part have rank two, one, or zero as dictated by their quadratic and cubic parts.

## Assumptions and scope
The base field is arbitrary; \(t\) must be nonzero, and the three skew-commutation constants are equal. All geometric components and their dimensions refer to the *reduced* zero locus over \(k\), or equivalently after arbitrary field extension. The formula \([X_t]=T_t(\mathbb L)\) uses the ordinary Grothendieck ring of reduced varieties over \(k\), not a possibly nonreduced defining scheme. In finite-field formulas, \(Q\) denotes field cardinality while \(t\) denotes the nonzero algebra parameter; they are unrelated variables. The assertion \(u^2=0\) forces its scalar coefficient to vanish, so the entire locus lies in \(J\).

## Proof
**PBW basis and square equations.** The ordered squarefree monomials \(1,x,y,z,xy,xz,yz,xyz\) form a basis: commutations are scalar and mutually compatible, and any monomial with a repeated generator vanishes. Expanding the square of the displayed \(u\) in this basis gives exactly
\[
 u^2=(1+t)(ab\,xy+ac\,xz+bc\,yz)
 +\bigl((1+t^2)(af+cd)+2tbe\bigr)xyz.
 \tag{1}
\]
All omitted terms have repeated generators. Thus \(X_t\) is the reduced zero set of the four displayed coefficients; in particular the cubic coordinate \(g\) is always free.

**Geometric components.** If \(\operatorname{char}k=2\) and \(t=1\), all four coefficients vanish identically and \(X_t=\mathbb A^7\). If \(\operatorname{char}k\ne2\) and \(t=-1\), the only equation reduces to \(af-be+cd=0\). This nondegenerate split six-variable quadratic form is irreducible, because a quadratic product of linear factors would have rank at most two; its gradient vanishes precisely where \(a=b=c=d=e=f=0\), giving the stated singular line.

For \(t\ne-1\), the degree-two equations require at most one of \(a,b,c\) to be nonzero. The following lists are all the maximal irreducible linear subspaces, expressed by their vanishing coordinates. Each row follows from (1) by examining the four cases \((a,b,c)=0\), only \(a\ne0\), only \(b\ne0\), or only \(c\ne0\), then taking closures.

* If \(\operatorname{char}k\ne2\) and \(t^2\ne-1\): \(a=b=c=0\); \(b=c=f=0\); \(a=c=e=0\); \(a=b=d=0\). All have dimension four.
* If \(\operatorname{char}k\ne2\) and \(t^2=-1\): \(b=c=0\), \(a=b=0\), \(a=c=e=0\), of dimensions five, five, and four. The zero-linear-part stratum belongs to the first two.
* If \(\operatorname{char}k=2\) and \(t\ne1\): \(a=c=0\), \(b=c=f=0\), \(a=b=d=0\), of dimensions five, four, and four. The zero-linear-part stratum belongs to the first.

No listed linear subspace is contained in another. They therefore are exactly the irreducible components, over any extension field. As distinct linear components are smooth individually, their reduced union is singular exactly at points belonging to two or more components (its local ring there has more than one minimal prime).

**Grothendieck classes.** In the generic odd-characteristic case the stratum \(a=b=c=0\) contributes \(\mathbb L^4\); the three nonzero-axis strata each contribute \((\mathbb L-1)\mathbb L^3\), giving \(4\mathbb L^4-3\mathbb L^3\). In the exceptional odd-characteristic fourth-root case, two nonzero-axis strata instead have four free remaining coordinates: \(\mathbb L^4+2(\mathbb L-1)\mathbb L^4+(\mathbb L-1)\mathbb L^3=2\mathbb L^5-\mathbb L^3\). In characteristic two with \(t\ne1\), the middle-axis stratum has four remaining free coordinates: \(\mathbb L^4+(\mathbb L-1)\mathbb L^4+2(\mathbb L-1)\mathbb L^3=\mathbb L^5+2\mathbb L^4-2\mathbb L^3\). When \(t=-1\) in odd characteristic, the equation is a split pairing between \((a,b,c)\) and \((f,-e,d)\). The first triple being zero contributes \(\mathbb L^3\) solutions in the other triple, while any nonzero first triple has an affine two-plane of solutions. Multiplying by the free \(g\) gives \(\mathbb L(\mathbb L^3+(\mathbb L^3-1)\mathbb L^2)=\mathbb L^6+\mathbb L^4-\mathbb L^3\). The characteristic-two commutative case is all of \(\mathbb A^7\). Specialization to finite fields proves all five point counts.

**Rank and homology.** The algebra is graded in degrees zero through three with dimensions \(1,3,3,1\). For any \(u^2=0\) with nonzero linear part \(\ell=ax+by+cz\), multiplication by \(\ell\) on consecutive graded pieces has ranks \(1,2,1\). Indeed the middle map, with columns indexed by \(x,y,z\) and rows by \(xy,xz,yz\), is
\[
 \begin{pmatrix}tb&a&0\\tc&0&a\\0&tc&b\end{pmatrix}.
 \tag{2}
\]
For \(t=-1\) in odd characteristic or \(t=1\) in characteristic two, it is exterior multiplication by a nonzero one-form and has rank two. In the remaining regimes (1) forces \(\ell\) to have only one nonzero coordinate, and (2) again has rank two. The top-degree map is nonzero whenever \(\ell\ne0\). The images of degrees zero, one, and two under \(L_u\) have distinct lowest degrees; their leading images provide four linearly independent vectors. Because \(L_u^2=0\) on an eight-dimensional space, \(\operatorname{rank}L_u\le4\), proving equality. If \(\ell=0\) and the quadratic part is nonzero, the image is the span of the quadratic part (with a possible cubic correction) and the socle \(kxyz\), hence rank two. A nonzero pure cubic has rank one, and the zero element rank zero. There are exactly \(Q^4\) elements with zero linear part: one of rank zero, \(Q-1\) of rank one, and \(Q^4-Q\) of rank two. Subtracting them from \(T_t(Q)\) gives the displayed rank polynomial. Since \(L_u^2=0\), its homology has dimension \(8-2\operatorname{rank}L_u\), and it is acyclic precisely in rank four.

## Verification
The independently implemented PBW multiplication checker `check_quantum_square_zero.py` exhaustively enumerates each of the seven coefficient coordinates over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\), using every nonzero parameter in each field. It does not decide square-zero status by equation (1): instead, it multiplies basis monomials and computes matrix ranks by field Gaussian elimination. It verified ten complete field-parameter combinations, including the primitive-fourth-root regime over \(\mathbb F_5\), the nontrivial characteristic-two deformation over \(\mathbb F_4\), and the exterior regimes over odd and even fields. The checker output ends with `QUANTUM_EXTERIOR_SQUARE_ZERO_OK 10 exhaustive field-parameter cases`. Finite checks cannot prove universal assertions; the algebraic proof above supplies them.

## Relationship to prior work
Bergh and Erdmann's 2008 preprint develops rank and support varieties for quantum complete intersections and sets out the underlying PBW presentations. Bergh, Erdmann and Jorgensen's 2019 preprint establishes the role of Jordan types of multiplication by *linear forms*, including freeness of the regular module for the standard restricted parameters. These papers explain the significance of regular multiplication ranks and already cover projectivity for their linear forms; the present finding does not claim those principles as new. The assessed new statement is the full *mixed-degree* square-zero element locus for all nonzero deformation parameters, with its five geometric transitions, Grothendieck classes, and rank-refined finite-field enumeration. Work on the first Hochschild cohomology of quantum complete intersections concerns derivations rather than this locus. No equivalent statement was located in the inspected sources or targeted searches, but publication priority is not certified.

## Limitations
The geometry concerns reduced varieties; nilpotent structure of the scheme defined by equation (1) is not computed. The theorem treats the three-generator equal-parameter quantum exterior algebra, not all multiparameter skew complete intersections or arbitrary truncation exponents. The exact finite-field formulas are unconditional mathematical consequences of (1), but no independent human audit or exhaustive historical-priority certification has been performed.

## References
1. P. A. Bergh and K. Erdmann, *The Avrunin–Scott theorem for quantum complete intersections*, arXiv:0810.3308v1 (public 18 October 2008), https://arxiv.org/abs/0810.3308.
2. P. A. Bergh, K. Erdmann and D. A. Jorgensen, *Modules of constant Jordan type over quantum complete intersections*, arXiv:1910.06714v1 (15 October 2019), https://arxiv.org/abs/1910.06714.
3. *The first Hochschild cohomology as a Lie algebra*, arXiv:1903.12145, §4.4, https://arxiv.org/abs/1903.12145.
