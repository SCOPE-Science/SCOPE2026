# A characteristic-two dimension jump for weight-zero Rota–Baxter operator loci

## Finding
Let \(K\) be a field, \(V\) an \(n\)-dimensional vector space with \(n\geq1\), and \(R=K\oplus V\) the unital square-zero algebra (\(V^2=0\)). A weight-zero Rota–Baxter operator is a \(K\)-linear map \(P:R\to R\) satisfying \(P(x)P(y)=P(xP(y)+P(x)y)\) for every \(x,y\in R\).

**Classification in all characteristics.** Every such operator, and only such an operator, has the unique form
\[
P(a+u)=a v+L(u),\qquad v\in V,\quad L\in\operatorname{End}_K(V),\quad L^2=0,\quad 2L(v)=0.
\]
Thus the operator locus over fields of characteristic different from two is the closed reduced variety \(\{(L,v):L^2=0,Lv=0\}\), while in characteristic two it is \(\{L:L^2=0\}\times V\), with **no constraint on \(Lv\)**.

**Geometric phase transition.** Write \(r=\lfloor n/2\rfloor\). Over every algebraically closed field, each of these reduced operator varieties is irreducible and admits an explicit proper birational map from a smooth vector bundle over \(\operatorname{Gr}(n-r,V)\). Its dimension is
\[
\begin{cases}
(n-r)(2r+1),&\operatorname{char}K\ne2,\\
2r(n-r)+n,&\operatorname{char}K=2.
\end{cases}
\]
The characteristic-two excess is exactly \(r\). This is positive and unbounded with \(n\) for \(n\ge2\).

**Exact finite-field count.** For a prime power \(q\) let \(N_n(q)\) be the number of weight-zero Rota–Baxter operators on \(\mathbb F_q\oplus\mathbb F_q^n\). Put
\[
T_{n,s}(q)={n\brack s}_q{n-s\brack s}_q\prod_{j=0}^{s-1}(q^s-q^j),
\]
where \({a\brack b}_q\) is the Gaussian binomial coefficient and an empty product equals one. Then
\[
N_n(q)=\sum_{s=0}^{\lfloor n/2\rfloor}T_{n,s}(q)\begin{cases}q^{n-s},&q\text{ odd},\\q^n,&q\text{ even}.\end{cases}
\]
The rank-\(s\) contribution is explicitly \(T_{n,s}(q)\) times the displayed vector-fiber size. The novelty asserted is the **characteristic-sensitive identification of the operator varieties and its quantitative comparison**; the Gaussian rank count and geometric properties of square-zero matrix-pair loci are prior input, not independently claimed.

## Assumptions and scope
The algebra is the local unital algebra \(R=K[x_1,\ldots,x_n]/(x_1,\ldots,x_n)^2\), canonically \(K\oplus V\). There is no assumption that \(K\) is perfect for the operator classification or the finite-field count. Irreducibility, geometric dimension and the birational resolution statement are over algebraically closed fields; the statements refer to the reduced varieties underlying the indicated polynomial equations. No assertion about scheme-theoretic reducedness of the original Rota–Baxter equation ideal is made. The finite-field formula applies to both odd and even prime powers, without requiring algebraic closure.

## Proof
**1. Reduction of the identity, without dividing by two.** Write a putative linear operator as \(P(u)=f(u)1+L(u)\) for \(u\in V\) and \(P(1)=\alpha1+v\). Taking both arguments \(u,w\in V\), equality of scalar parts in the Rota–Baxter identity gives \(f(u)f(w)=2f(u)f(w)\); hence \(f(u)f(w)=0\). Taking \(w=u\) and using that a field has no nonzero square-zero scalars yields \(f=0\), even in characteristic two. Thus \(P(V)\subseteq V\). Now the identity at \((1,1)\), comparing scalar components, gives \(\alpha^2=2\alpha^2\), so \(\alpha=0\). Consequently \(P(a+u)=av+L(u)\) for unique \(v,L\).

For \(x=a+u\) and \(y=b+w\), both \(P(x),P(y)\) lie in the zero-product ideal \(V\), so \(P(x)P(y)=0\). Expanding the right-hand argument gives
\[
xP(y)+P(x)y=2abv+aL(w)+bL(u).
\]
Therefore the Rota–Baxter identity is equivalent to
\[
2abL(v)+aL^2(w)+bL^2(u)=0\quad\text{for all }a,b,u,w.
\]
Setting \((a,b)=(1,0),(0,1),(1,1)\) in turn shows it is equivalent to \(L^2=0\) and \(2L(v)=0\). Conversely, these conditions make the expression identically zero. Thus the classification holds over every field and gives the two characteristic branches.

**2. Square-zero rank strata.** For \(L^2=0\), \(\operatorname{im}L\subseteq\ker L\), hence \(s=\operatorname{rank}L\le r\). Fix a subspace \(W\subset V\) of dimension \(n-r\). The endomorphisms obeying \(\operatorname{im}L\subseteq W\subseteq\ker L\) are precisely the maps induced by \(\operatorname{Hom}_K(V/W,W)\), a vector space of dimension \(r(n-r)\). Every square-zero \(L\) admits such a \(W\): select any intermediate subspace between its image (dimension \(s\le r\le n-r\)) and kernel (dimension \(n-s\ge n-r\)).

**3. Smooth incidence maps and dimensions.** Let \(\mathcal S\) be the tautological bundle of rank \(n-r\) and \(\mathcal Q\) the quotient bundle of rank \(r\) on \(\operatorname{Gr}(n-r,V)\). In characteristic two, the total space of \(\operatorname{Hom}(\mathcal Q,\mathcal S)\oplus (V\times\operatorname{Gr}(n-r,V))\) maps to the operator locus by \((W,L,v)\mapsto(L,v)\). It is smooth and irreducible of dimension \(r(n-r)+r(n-r)+n=2r(n-r)+n\). The map is proper because its graph is a closed incidence subvariety in the product of a projective Grassmannian and the affine operator space, and it is surjective by step 2.

In characteristic different from two, use instead the total space of \(\operatorname{Hom}(\mathcal Q,\mathcal S)\oplus\mathcal S\). It has dimension \(r(n-r)+r(n-r)+(n-r)=(n-r)(2r+1)\) and maps by \((W,L,v)\mapsto(L,v)\). For any \(L^2=0\) and \(v\in\ker L\), a suitable \(W\) must contain \(\operatorname{im}L+Kv\) and lie in \(\ker L\). If \(s<r\), then \(\dim(\operatorname{im}L+Kv)\le s+1\le r\le n-r\); if \(s=r\) and \(n\) is odd, this dimension is at most \(r+1=n-r\); if \(s=r\) and \(n=2r\), then \(\operatorname{im}L=\ker L\) and the dimension is \(r=n-r\). Therefore this incidence map is also surjective, proper, and has irreducible smooth source.

In both characteristics the rank-\(r\) locus is nonempty, and there \(W=\ker L\) is uniquely determined; it is an open dense locus because both images are irreducible and rank-\(r\) points exist. Each incidence map is therefore birational and gives a resolution of the **reduced** variety. The dimensions follow from their source dimensions, and their difference is
\[2r(n-r)+n-(n-r)(2r+1)=r.\]

**4. Rank-by-rank point count.** For rank \(s\), choose \(U=\operatorname{im}L\), in \({n\brack s}_q\) ways; then choose \(W=\ker L\) of codimension \(s\) containing \(U\), in \({n-s\brack s}_q\) ways. The induced map \(V/W\to U\) must be an isomorphism, in \(\prod_{j=0}^{s-1}(q^s-q^j)\) ways. This proves the expression \(T_{n,s}(q)\). In odd characteristic, \(v\) lies in the \((n-s)\)-dimensional kernel, giving \(q^{n-s}\) choices. In characteristic two, \(v\) is arbitrary in \(V\), giving \(q^n\). Summing the disjoint rank strata yields the stated exact formula.

## Verification
The accompanying standalone `CHECK.py` tests the Rota–Baxter identity on basis pairs (sufficient by bilinearity) for **every** linear map \(R\to R\) in the five finite cases \((n,q)=(1,2),(1,3),(2,2),(2,3),(3,2)\), compares it with the classification, and counts operators against the formula. The corresponding verified counts are \(2,3,16,33,176\), with zero classification mismatches. This finite enumeration corroborates, but does not replace, the unrestricted algebraic proof. No computational claim is made that tests all \(n\) or fields.

## Relationship to prior work
Azhar Farooq, *Rota–Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1 (public 2026-05-15), Theorem 3.4 and §3.1, proves the characteristic-zero classification and writes the equations \(L^2=Lv=0\). That is direct prior input for the odd-characteristic geometry; its paper does **not** address characteristic two or the difference in geometric dimensions. The elementary full-characteristic reduction above is independently checked and not inferred by unjustified division by two.

Achar–Henderson, *Orbit closures in the enhanced nilpotent cone* (arXiv:0712.1079), Proposition 3.3 and Corollary 3.4, give resolutions and subspace-incidence descriptions for enhanced nilpotent orbit closures; their geometry covers the individual odd-characteristic matrix-pair incidence as a specialization. Bellamy–Boos, *The (cyclic) enhanced nilpotent cone via quiver representations* (arXiv:1609.04525; DOI 10.1007/s00229-018-1098-9), develop the corresponding quiver orbit framework. The full square-zero cone \(\{L^2=0\}\times V\), its rank geometry, and the Grassmannian technique are **not claimed new**. Neither published geometric work identifies the characteristic-sensitive weight-zero Rota–Baxter equation on \(K\oplus V\) nor supplies the resulting *comparison* of operator dimensions and counts across characteristic two.

## Limitations
The mathematical result classifies weight-zero operators only, on the specified square-zero commutative local algebras; neither general local algebras nor nonzero weights are covered. The geometry concerns underlying reduced varieties, not the potentially nonreduced original equation schemes. The rank formula for square-zero matrices and related enhanced-nilpotent geometry are classical; novelty is limited to their precise characteristic-dependent consequences for the Rota–Baxter locus. Historical priority under alternate descriptions of low-dimensional operator varieties remains a risk. The finite-field checks are small examples, not exhaustive evidence in unbounded dimension.

## References
1. A. Farooq, *Rota–Baxter Operators on Truncated Polynomial Algebras*, arXiv:2605.15670v1, 15 May 2026. https://arxiv.org/html/2605.15670v1
2. P. N. Achar and A. Henderson, *Orbit closures in the enhanced nilpotent cone*, Adv. Math. 219 (2008), 27–62; arXiv:0712.1079. https://arxiv.org/abs/0712.1079
3. G. Bellamy and M. Boos, *The (cyclic) enhanced nilpotent cone via quiver representations*, Manuscripta Math. 161 (2020), 333–362, DOI 10.1007/s00229-018-1098-9. https://link.springer.com/article/10.1007/s00229-018-1098-9
