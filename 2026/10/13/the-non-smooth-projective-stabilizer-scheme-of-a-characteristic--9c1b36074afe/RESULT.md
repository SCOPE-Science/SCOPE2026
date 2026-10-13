# The non-smooth projective stabilizer scheme of a characteristic-two rational quartic

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\), and let
\[
C=V(F)\subset\mathbb P^2_k,\qquad F=Y^4+XZ^3.
\]
The scheme-theoretic projective stabilizer \(G=\operatorname{Stab}_{\operatorname{PGL}_3}(C)\), which parametrizes projective transformations carrying the **closed subscheme** \(C\) to itself over arbitrary \(k\)-algebras, is represented by
\[
G\simeq \operatorname{Spec} k[b,b^{-1},v,u]/(u^4)
\]
under the matrix presentation
\[
(b,v,u)\longmapsto
\begin{pmatrix}
b^4&0&v^4\\
u&b&v\\
0&0&1
\end{pmatrix}.
\]
In these coordinates the group law (left matrix multiplied by the primed right matrix) is
\[
\begin{split}
b''&=bb',\\
u''&=u(b')^4+bu',\\
v''&=v+bv'+u(v')^4.
\end{split}
\]
In particular, \(G_{\mathrm{red}}\cong\mathbb G_a\rtimes\mathbb G_m\) has dimension \(2\), whereas \(\dim_k\operatorname{Lie}(G)=3\). The subgroup \(b=1,v=0\) is the nontrivial infinitesimal group scheme \(\alpha_4=\operatorname{Spec}k[u]/(u^4)\). The projective stabilizer is therefore **non-smooth**, with a uniform length-four nilpotent structure over its reduced underlying scheme. On the smooth chart \(Z=1\), where \(X=Y^4\) and \(t=Y\), the action is \(t\mapsto ut^4+bt+v\).

## Assumptions and scope

The statement is about the full **projective stabilizer group scheme** of the fixed embedded curve, not just \(G(k)\), and not a claim about all abstract automorphisms or about the generic fiber of the fibration. The ground field is algebraically closed of characteristic \(2\); the functor is computed on every commutative \(k\)-algebra, including nonreduced rings. All equations and functorial representations are homogeneous in \([X:Y:Z]\) and the matrix is taken modulo scalar matrices. The curve is geometrically integral: on \(Z=1\), its equation is \(X+Y^4=0\), giving a dense smooth affine line.

## Proof

**Step 1: the reduced geometric stabilizer.** The partial derivatives of \(F\) in characteristic \(2\) are \(F_X=Z^3\), \(F_Y=0\) and \(F_Z=XZ^2\). The unique singular point of \(C\) is \(P=[1:0:0]\). For any smooth point \([X:Y:Z]\), necessarily \(Z\ne0\), its tangent has equation \(ZX'+XZ'=0\) in the new homogeneous point coordinates. The intersection of all these tangents is the uniquely determined strange point \(Q=[0:1:0]\), which lies off \(C\). Hence every geometric projective stabilizer fixes both \(P\) and \(Q\). Such a matrix is triangular of the form
\[
\begin{pmatrix}
a&0&d\\0&b&v\\0&0&i
\end{pmatrix},\qquad abi\ne0.
\]
Substitution in \(F\) yields \(b^4=ai^3\) and \(v^4+di^3=0\). After normalizing \(i=1\), the geometric stabilizer is exactly \(\{(b,v,0):b\ne0\}\), acting as \(t\mapsto bt+v\). Thus the reduced group is the affine group.

**Step 2: completeness over nonreduced coefficient rings.** The stabilizer is a closed finite-type subgroup scheme of \(\operatorname{PGL}_3\). Its underlying geometric points lie in the open chart where the bottom-right entry is nonzero; this open therefore contains the whole scheme, and every matrix has a unique representative with bottom-right entry \(1\). Start with the general matrix
\[
M=\begin{pmatrix}
a&c&d\\u&b&v\\g&h&1\end{pmatrix}.
\]
In its coordinate ring \(a,b\) are units and \(c,g,h\) are nilpotent, because their values vanish at every geometric point; the coordinate ring is a finitely generated algebra over an algebraically closed field. Writing \(F(M[X:Y:Z])=\lambda F(X,Y,Z)\) and comparing the coefficients of \(X^2Z^2\), \(XYZ^2\), and \(YZ^3\), respectively, gives
\[
g(a+dg)=0,\qquad ah+cg=0,\qquad c+dh=0.
\]
Because \(a\) is a unit and \(g\) is nilpotent, \(a+dg\) is a unit. Thus \(g=0\), then \(h=0\), then \(c=0\). The four remaining coefficients \(Y^4\), \(XZ^3\), \(Z^4\), and \(X^4\) give
\[
\lambda=b^4=a,\qquad d=v^4,\qquad u^4=0.
\]
No further conditions remain. Conversely, substituting the displayed normal-form matrix gives exactly \(F(M[X:Y:Z])=b^4F(X,Y,Z)\), using \(u^4=0\). Its determinant is \(b^5\), a unit. This proves the asserted functorial isomorphism for every \(k\)-algebra and excludes any additional nonreduced stabilizer directions.

**Step 3: group law and infinitesimal structure.** Direct multiplication of normal-form matrices gives the displayed law; the first-row equality uses \((u(v')^4)^4=0\). The coordinate algebra is a free module of rank \(4\) over \(k[b,b^{-1},v]\), with basis \(1,u,u^2,u^3\). Thus its reduced scheme is \(\mathbb G_m\times\mathbb A^1\), its Krull dimension is \(2\), and the cotangent space at \((1,0,0)\) has basis \(b-1,v,u\), yielding tangent dimension \(3\). Setting \(b=1\) and \(v=0\) is closed under the multiplication rule and gives \(u''=u+u'\), hence the stated \(\alpha_4\) subgroup scheme. Its only geometric point is the identity, although it has length \(4\).

## Verification

The standalone file `verify.py` computes the polynomial substitution exactly in characteristic \(2\), verifies the matrix group law modulo \(u^4=(u')^4=0\), checks the three decisive generic coefficient identities, and exhausts all \(168\) invertible projective matrices over \(\mathbb F_2\), finding exactly the two predicted rational stabilizers. Run with `python verify.py`; it requires Python 3 and SymPy. The universal group-scheme assertion is proved by coefficient comparison above, not inferred from the finite-field enumeration. The checker was executed successfully from its supplied path.

## Relationship to prior work

Hilario and Stöhr, *Fibrations by plane quartic curves with a canonical moving singularity* (arXiv:2306.08579v1, Section 5), introduce the quartic \(Y^4+XZ^3+cX^4=0\), describe its singularity and strange tangents, and exhibit automorphisms acting transitively on the smooth locus. Those geometric facts are acknowledged as prior. The present result concerns the full group scheme of the member \(c=0\), including nilpotent transformations invisible to its geometric automorphism group.

Hilario and Schröer, *Generalizations of quasielliptic curves* (arXiv:2303.12324v1, especially Sections 5, 7 and 8), study nonreduced automorphism groups of a different hierarchy of rational cuspidal curves with numerical semigroups \(\Gamma_{p,n}\). Their low-index curves have cusp semigroup \(\langle2,3\rangle\) and arithmetic genus \(1\); the current quartic has local cusp semigroup \(\langle3,4\rangle\) and arithmetic genus \(3\). Their displayed automorphism-group theorem for that hierarchy does not directly imply the full stabilizer of this plane quartic. The explicit non-smoothness mechanism is related, not claimed as a new general principle.

The later Hilario–Stöhr classification (arXiv:2409.05464v1) concerns fibrations and their birational types, rather than giving this scheme-theoretic projective stabilizer. Their earlier arXiv:2211.16962v1 studies a different quartic pencil with equation \(Z^4+X^2Y^2+X^3Z+c(Y^4+X^2Z^2)=0\). A distinct recorded curve \(Y^4+XZ^3+X^3Z=0\) has a one-dimensional geometric translation stabilizer; it is not the quartic here, as its binary quartic section has root multiplicities \(2+1+1\) instead of \(3+1\). These are statement-level distinctions, not title-level ones.

## Limitations

This is not a calculation of the abstract automorphism group scheme of the curve, nor of all automorphism schemes for the pencil as \(c\) varies. The result is for the fixed embedded curve over characteristic \(2\); it asserts nothing about characteristic zero or a generic fibration. The exact non-smooth stabilizer is a special feature of the inseparable fourth power. No claim of exhaustive priority verification or independent auditing is made; the closest related group-scheme literature has been compared, but unindexed calculations remain possible.

## References

1. C. Hilario and K.-O. Stöhr, *Fibrations by plane quartic curves with a canonical moving singularity*, arXiv:2306.08579v1 (June 14, 2023), Section 5. https://arxiv.org/abs/2306.08579
2. C. Hilario and S. Schröer, *Generalizations of quasielliptic curves*, arXiv:2303.12324v1 (March 22, 2023), Sections 5–8. https://arxiv.org/abs/2303.12324
3. C. Hilario and K.-O. Stöhr, *Fibrations by plane projective rational quartic curves in characteristic two*, arXiv:2409.05464v1 (September 9, 2024). https://arxiv.org/abs/2409.05464
4. C. Hilario and K.-O. Stöhr, *On regular but non-smooth integral curves*, arXiv:2211.16962v1 (November 30, 2022), Section 3. https://arxiv.org/abs/2211.16962
