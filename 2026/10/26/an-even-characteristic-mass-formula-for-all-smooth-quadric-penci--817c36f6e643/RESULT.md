# An even-characteristic mass formula for all-smooth quadric pencils and their genus-one bases

## Finding

**Theorem.** Let \(k=\mathbf F_q\), where \(q=2^r\) and \(r\ge1\). Let \(\mathcal Q=\operatorname{Sym}^2(k^4)^*\) be the ten-dimensional vector space of homogeneous quadratic forms on a fixed four-dimensional vector space. A **pencil** means an unlabelled two-dimensional \(k\)-linear subspace \(W\le \mathcal Q\); its rational members are the \(q+1\) projective points of \(\mathbf P(W)(k)\). Call \(W\) *all-smooth* if every rational member is a geometrically smooth quadric surface in \(\mathbf P^3\). Call its **base** smooth if the scheme cut out by any basis of \(W\) is a geometrically smooth codimension-two complete intersection. Then

\[
\#\{W:W\text{ all-smooth}\}=\frac{q^{12}(q^3-1)(q-1)}2,
\]

and

\[
\#\{W:W\text{ all-smooth, base smooth}\}=\frac{q^6(q^3-1)(q-1)(q^2-1)(q^4-1)}2.
\]

Thus, among all-smooth pencils, the exact smooth-base fraction is \((1-q^{-2})(1-q^{-4})\). Every smooth base is a geometrically connected genus-one curve (of degree four in \(\mathbf P^3\)). In particular, the counts for \(q=2\) are \(14{,}336\) and \(10{,}080\); for \(q=4\) they are \(1{,}585{,}446{,}912\) and \(1{,}480{,}550{,}400\).

## Assumptions and scope

All geometric smoothness statements are after extension to an algebraic closure. All pencils are distinct linear two-spaces inside the fixed ten-dimensional space, rather than ordered bases, scalar-normalized equations, projective coordinate orbits, or isomorphism classes of genus-one curves. Only even prime powers are covered. For an all-smooth pencil, the pair of quadratic forms has no common factor: such a factor would force the polar pencil to have a singular member, as also follows from the regular-pencil normal form used below.

## Proof

**1. Polar forms.** Write \(V=k^4\). In characteristic two, polarization gives the surjective \(k\)-linear map
\[
\pi:\operatorname{Sym}^2(V^*)\longrightarrow \operatorname{Alt}^2(V^*),\qquad Q\longmapsto ((x,y)\mapsto Q(x+y)-Q(x)-Q(y)),
\]
with four-dimensional kernel consisting of the squares of linear forms. In four variables, a quadric is geometrically smooth precisely when its alternating polar form is nondegenerate. If the radical is nonzero, it has dimension at least two and the restriction of the quadratic form to that radical is a square of a linear form over an algebraic closure, hence vanishes on a nonzero radical vector. Conversely, a nondegenerate polar form has no singular projective point.

**2. Polar pencils and the Pfaffian.** Identify \(\operatorname{Alt}^2(V^*)\simeq k^6\). In suitable coordinates the Pfaffian is the split nonsingular quadratic form
\[
P(z)=z_1z_6+z_2z_5+z_3z_4.
\]
For a two-plane \(L\le k^6\), every nonzero polar form in \(L\) is nondegenerate if and only if \(P|_L\) is anisotropic. Over the finite field \(k\), this means that the binary quadratic polynomial representing \(P|_L\) is irreducible.

**3. Exact count of anisotropic polar two-planes.** The number of \(u\in k^6\) with \(P(u)=1\) is \(q^2(q^3-1)\): for three split hyperbolic pairs, the character-sum formula for each nonzero value is \(q^5-q^2\). Fix such a vector \(u\). Its nonsingular quadratic isometry group acts transitively on the norm-one vectors (or equivalently choose its standard hyperbolic coordinates), so we may write \(u=e_1+f_1\). Any \(v\) with the polar pairing \(B_P(u,v)=1\) has the unique expression
\[
v=a e_1+(a+1)f_1+z,\qquad a\in k,\quad z\in k^4,
\]
where the last four coordinates carry a split hyperbolic quadratic form \(P_4\). The restricted polynomial in the basis \((u,v)\) is \(t^2+t+P(v)\), and \(P(v)=a^2+a+P_4(z)\). It is irreducible iff \(\operatorname{Tr}_{k/\mathbf F_2}P_4(z)=1\). The additive character sum \(\sum_z(-1)^{\operatorname{Tr}P_4(z)}=q^2\) proves that there are \((q^4-q^2)/2\) such \(z\), independently of \(a\). Every anisotropic plane admits exactly \(q+1\) vectors \(u\) of Pfaffian one, and for any such \(u\) exactly \(q\) vectors \(v\) with \(B_P(u,v)=1\). Thus, dividing the count of normalized pairs \((u,v)\), the number of anisotropic polar pencils is
\[
A(q)=\frac{q^2(q^3-1)\,q(q^4-q^2)/2}{q(q+1)}=\frac{q^4(q^3-1)(q-1)}2.
\]

**4. Lifting a polar pencil.** For each fixed anisotropic plane \(L\le \operatorname{Alt}^2(V^*)\), the quadratic pencils \(W\) that map isomorphically onto \(L\) under \(\pi\) are the graphs of \(k\)-linear maps \(L\to \ker\pi\). There are \(q^{2\cdot4}=q^8\) such graphs. The fact that every nonzero polar member of \(L\) is nonsingular guarantees every rational member of each lift is geometrically smooth. Hence the first formula is \(A(q)q^8\).

**5. Normal form for a fixed anisotropic polar pencil.** Set \(K=\mathbf F_{q^2}\) and let \(\sigma:z\mapsto z^q\) be its conjugation. Let \(B_0,B_1\) be a basis of \(L\), and define \(T\) by \(B_1(x,y)=B_0(Tx,y)\). Its characteristic polynomial is the square of an irreducible separable quadratic. After extension to a splitting field, its two generalized eigenspaces each have dimension two and are mutually \(B_0\)-orthogonal and nondegenerate. On a two-dimensional alternating plane, an endomorphism that is self-adjoint and also satisfies \(B_0(Tx,x)=0\) is scalar; hence \(T\) has no nontrivial Jordan blocks and its minimal polynomial is the irreducible quadratic. The space \(V\) is therefore two-dimensional over \(K\), and the pairing is a nondegenerate alternating \(K\)-bilinear form under a trace. Choosing a symplectic \(K\)-basis \((x,y)\), the polar pencil has members
\[
B_\lambda((x,y),(x',y'))=\operatorname{Tr}_{K/k}\!\bigl(\lambda(xy'+x'y)\bigr),\qquad \lambda\in K.
\]
(The two embeddings of \(K\) in an algebraic closure interchange this form and its conjugate.) Every quadratic lift of this fixed polar pencil is uniquely parametrized by \(a,b,c,d\in K\):
\[
Q_\lambda(x,y)=\operatorname{Tr}_{K/k}\!\left(\lambda xy+(a\lambda+b\lambda^q)x^2+(c\lambda+d\lambda^q)y^2\right).
\]
Indeed, the square corrections are exactly the \(k\)-linear maps from \(K\) to the two-dimensional \(K\)-space of square coefficients; every \(k\)-linear endomorphism of \(K\) has the unique form \(\lambda\mapsto a\lambda+b\lambda^q\).

**6. Exact geometric smoothness criterion for the base.** Over an algebraic closure, the two conjugate embeddings of \(K\) produce independent coordinates \(X,Y,U,V\), and a basis of the base ideal is
\[
F_0=XY+aX^2+cY^2+b^qU^2+d^qV^2,\qquad
F_1=UV+a^qU^2+c^qV^2+bX^2+dY^2.
\]
Their gradients are \((Y,X,0,0)\) and \((0,0,V,U)\). Since they have disjoint supports, at a point of the base their Jacobian has rank below two precisely when \(X=Y=0\) or \(U=V=0\). On the first line, the equations become
\[
b^qU^2+d^qV^2=0,\qquad UV+a^qU^2+c^qV^2=0.
\]
If \(b=d=0\), there is a geometric root of the second equation and the base is singular. Otherwise the first equation specifies exactly one projective point over the algebraic closure, and substitution in the second shows that singularity occurs exactly when
\[
\Delta:=bd+(ad)^2+(cb)^2=0.
\]
The other radical line gives the conjugate condition, so the same test is necessary and sufficient for both. Thus, the base is geometrically smooth exactly when \(\Delta\ne0\). If smooth, it is the complete intersection of two quadrics, hence connected with arithmetic and geometric genus one by adjunction.

**7. Counting smooth lifts.** Let \(Q=|K|=q^2\). The pair \((b,d)=(0,0)\) never works. For each other pair, the \(K\)-linear map \((a,c)\mapsto ad+cb\) is surjective, every fiber having \(Q\) elements. Since squaring is a bijection on \(K\), the equation \(bd+(ad+cb)^2=0\) holds for precisely \(Q\) of the \(Q^2\) pairs \((a,c)\). Consequently the number of smooth-base lifts of each fixed polar pencil is
\[
(Q^2-1)(Q^2-Q)=q^8(1-q^{-2})(1-q^{-4}).
\]
Multiplying by \(A(q)\) yields the second formula, with the stated proportion.

## Verification

The dependency-free programs `verify_even_quadric_pencils.py` and `verify_base_geometry.py` check two complementary finite instances. The first exhausts the anisotropic polar two-planes (through normalized Pfaffian pairs), enumerates all \(K^4\) coefficient tuples for \(q\in\{2,4\}\), and compares the counts with both closed formulas. The second independently checks the two geometric radical lines by direct substitution, including the exceptional zero first equation. Compare program output with `expected_counts.txt` and `expected_geometry.txt`.

These programs were executed on the delivered versions and reproduce the expected outputs. Their finite cases corroborate, but do not replace, the algebraic proof for all even prime powers.

## Relationship to prior work

Asgarli and Ghioca, *Smoothness in pencils of hypersurfaces over finite fields* (public arXiv v1 dated 2022-03-14), construct pencils over even finite fields all of whose rational members are smooth, including the quadric case. The paper gives existence constructions rather than the two enumerative mass formulas here. Bhosle's *Pencils of quadrics and hyperelliptic curves in characteristic two* (1990) develops structural normal forms for regular pencils in characteristic two; this work neither claims those normal forms as new nor asserts an exhaustive originality exclusion from Bhosle's text. A previously obtained binary-field census gave \(14{,}336\) all-smooth pencils and \(10{,}080\) with smooth base for \(q=2\); those numbers are consistency checks, not newly claimed. A separate odd-characteristic pencil mass formula does not imply this even-characteristic result because alternating polar forms, Pfaffians, and inseparability behavior differ.

## Limitations

The formulas count coordinate-fixed pencils, not projective equivalence classes, curve isomorphism classes or rational-point distributions. The smooth-base statement concerns only pencils already all-smooth; a smooth complete intersection can admit singular rational members in other settings. The two programs directly check only \(q=2\) and \(q=4\); the general statement relies on the proved structural lemmas. No independent external mathematical audit has been conducted. Earlier literature not indexed or not fully accessible could contain equivalent formulas.

## References

1. A. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first posted 2022-03-14. https://arxiv.org/abs/2203.07169
2. U. N. Bhosle, *Pencils of quadrics and hyperelliptic curves in characteristic two*, Journal für die reine und angewandte Mathematik **407** (1990), 75–98. https://doi.org/10.1515/crll.1990.407.75
3. I. Dolgachev and A. Duncan, *Regular pairs of quadratic forms on odd-dimensional spaces in characteristic 2*, arXiv:1510.06803; different (odd vector) dimension from the four-variable case here. https://arxiv.org/abs/1510.06803
