# The full two-sided ideal Grassmannian of a rectangular-band algebra

## Finding

Let \(k\) be any field and let \(m,n\ge2\). Consider the rectangular band \(S_{m,n}=[m]\times[n]\), with multiplication \((i,j)(h,\ell)=(i,\ell)\), and its **nonunital** semigroup algebra \(A=k[S_{m,n}]\). A two-sided ideal here means a linear subspace \(I\le A\) satisfying \(AI\subseteq I\) and \(IA\subseteq I\); it need not contain a unit.

Write \(R=k^m\), \(C=k^n\), so that \(A=R\otimes_k C\). Denote by \(\varepsilon_R:R\to k\), \(\varepsilon_C:C\to k\) their coordinate-sum maps, and set \(R_0=\ker\varepsilon_R\), \(C_0=\ker\varepsilon_C\). Define the row- and column-sum maps
\[
\rho=\mathrm{id}_R\otimes\varepsilon_C:A\to R,
\qquad
\gamma=\varepsilon_R\otimes\mathrm{id}_C:A\to C.
\]
For any pair of subspaces \(U\le C_0\) and \(V\le R_0\), put
\[
P_{U,V}=R\otimes U+V\otimes C,
\qquad
H_{U,V}=\{X\in A:\rho(X)\in V,\ \gamma(X)\in U\}.
\]
There is a natural isomorphism
\[
H_{U,V}/P_{U,V}\cong(R_0/V)\otimes(C_0/U).
\]
**Classification.** Every proper two-sided ideal \(I\) has exactly one triple \((U,V,W)\), where \(U\le C_0\), \(V\le R_0\), and \(W\le(R_0/V)\otimes(C_0/U)\). Its members are the inverse image of \(W\) under \(H_{U,V}\twoheadrightarrow H_{U,V}/P_{U,V}\). Every such triple yields a proper ideal. The only remaining ideal is \(A\).

Writing \(u=\dim U\), \(v=\dim V\), \(w=\dim W\), the dimension is
\[
\dim I=mu+nv-uv+w,
\qquad 0\le w\le (m-1-v)(n-1-u).
\]
In particular the unique maximal proper ideal is \(J=\ker(\varepsilon_R\otimes\varepsilon_C)\), and
\[
J^2=R_0\otimes C_0,\qquad J^3=0.
\]
Thus a simple rectangular band (as a semigroup) gives a nonunital algebra with a nontrivial cubic-nilpotent radical and a rich family of vector-space ideals.

**Finite-field census.** Let \({a\brack b}_q\) denote the Gaussian binomial coefficient, including \({0\brack0}_q=1\). If \(Z_{m,n}(q;T)=\sum_{I\lhd A}T^{\dim I}\) over \(k=\mathbb F_q\), then
\[
\boxed{
Z_{m,n}(q;T)=T^{mn}
+\sum_{u=0}^{n-1}\sum_{v=0}^{m-1}
{n-1\brack u}_q{m-1\brack v}_q
T^{mu+nv-uv}
\sum_{w=0}^{(m-1-v)(n-1-u)}
{(m-1-v)(n-1-u)\brack w}_qT^w.
}
\]
All field characteristics are included. The coefficient of \(T^d\) is the exact number of distinct two-sided ideals of vector-space dimension \(d\).

**Geometry.** In the reduced ideal locus inside the Grassmannian \(\mathrm{Gr}(d,A)\), the sublocus with fixed \((u,v,w)\) is a relative Grassmannian of \(w\)-planes in the vector bundle \((R_0/\mathcal V)\otimes(C_0/\mathcal U)\) over \(\mathrm{Gr}(v,R_0)\times\mathrm{Gr}(u,C_0)\), where \(\mathcal V,\mathcal U\) are tautological subbundles. Hence each nonempty stratum is smooth and geometrically irreducible of dimension
\[
v(m-1-v)+u(n-1-u)+w\big((m-1-v)(n-1-u)-w\big).
\]
This is a statement about the locally closed reduced strata, not the smoothness or irreducibility of the total ideal scheme.

## Assumptions and scope

The integers \(m,n\) range over every pair at least two. The coefficient field \(k\) is arbitrary, with no assumption of algebraic closedness or characteristic. The algebra is the ordinary semigroup algebra of a *rectangular band*, not a group algebra, a unital algebra obtained by adjoining an identity, or the semigroup itself. All ideals are two-sided \(k\)-vector subspaces. For counts, \(k=\mathbb F_q\) with \(q\) any prime power, and every ideal is counted exactly once. A Grassmannian stratum is always understood as its reduced locally closed variety.

## Proof

**1. Multiplication and the radical.** For pure tensors, the defining product gives
\[
(r\otimes c)(r'\otimes c')
=\varepsilon_C(c)\varepsilon_R(r')\,r\otimes c'.
\]
For arbitrary \(X,Y\in A\), bilinearity yields the exact identity
\[
XY=\rho(X)\otimes\gamma(Y).
\]
Let \(\varepsilon=\varepsilon_R\otimes\varepsilon_C\). For basis elements \(e_i\otimes f_j\),
\[
(e_i\otimes f_j)X(e_h\otimes f_\ell)
=\varepsilon(X)e_i\otimes f_\ell.
\]
If an ideal contains \(X\) with \(\varepsilon(X)\ne0\), this identity puts every basis element of \(A\) in the ideal; therefore it is \(A\). Every proper ideal lies in \(J=\ker\varepsilon\), and \(J\) itself is an ideal. This proves uniqueness of the maximal proper ideal. The displayed multiplication implies \(J^2\subseteq R_0\otimes C_0\). Conversely for any \(r\in R_0\), \(c\in C_0\), choose \(r_*\in R\), \(c_*\in C\) with both coordinate sums equal to one. The two elements \(r\otimes c_*\) and \(r_*\otimes c\) belong to \(J\), and their product is \(r\otimes c\). Thus \(J^2=R_0\otimes C_0\). Its product on either side by \(J\) is zero, so \(J^3=0\).

**2. Extracting the data of a proper ideal.** Let \(I\lhd A\) be proper. Define \(V=\rho(I)\subseteq R_0\) and \(U=\gamma(I)\subseteq C_0\). For a basis element \(e_i\otimes f_j\) and \(X\in I\),
\[
(e_i\otimes f_j)X=e_i\otimes\gamma(X),\qquad
X(e_i\otimes f_j)=\rho(X)\otimes f_j.
\]
Since \(I\) is an ideal, these identities imply \(R\otimes U+V\otimes C=P_{U,V}\subseteq I\). By definition of \(U,V\), also \(I\subseteq H_{U,V}\). Conversely any vector subspace \(I\) satisfying \(P_{U,V}\subseteq I\subseteq H_{U,V}\) is a two-sided ideal, since the two displayed multiplication formulas take products into \(R\otimes U\) and \(V\otimes C\), respectively. Moreover \(\gamma(P_{U,V})=U\) and \(\rho(P_{U,V})=V\), so the data \(U,V\) recovered from any such ideal are exactly those originally prescribed.

**3. Canonical quotient and uniqueness.** Choose vectors \(r_*\in R\), \(c_*\in C\) whose coordinate sums equal one, so \(R=kr_*\oplus R_0\) and \(C=kc_*\oplus C_0\). The conditions defining \(H_{U,V}\) are equivalent to
\[
H_{U,V}=V\otimes kc_*+kr_*\otimes U+R_0\otimes C_0.
\]
At the same time,
\[
P_{U,V}=V\otimes kc_*+kr_*\otimes U
+V\otimes C_0+R_0\otimes U.
\]
Therefore \(H_{U,V}/P_{U,V}\cong(R_0/V)\otimes(C_0/U)\), induced by the natural inclusion of \(R_0\otimes C_0\) and independent of the chosen splittings. Every intermediate subspace \(P_{U,V}\subseteq I\subseteq H_{U,V}\) is the inverse image of a unique subspace \(W\) of this quotient, completing the classification and uniqueness.

**4. Dimensions, counting, and geometry.** If \(u=\dim U\), \(v=\dim V\), then \(\dim P_{U,V}=mu+nv-uv\), because \((R\otimes U)\cap(V\otimes C)=V\otimes U\). The quotient dimension is \(r=(m-1-v)(n-1-u)\), so each \(w\)-plane \(W\) gives \(\dim I=mu+nv-uv+w\). Over \(\mathbb F_q\), the choices for \(U,V,W\) number, respectively, \({n-1\brack u}_q\), \({m-1\brack v}_q\), and \({r\brack w}_q\). These choices are disjoint by uniqueness, and adding the full ideal \(A\) yields the polynomial.

For a fixed \((u,v,w)\), the assignments \(I\mapsto(\gamma(I),\rho(I))\) have constant ranks and are regular maps into the two Grassmannians. Their fibers are the \(w\)-plane Grassmannians in \((R_0/V)\otimes(C_0/U)\); conversely the inverse-image construction is algebraic in the subbundles. This identifies the locally closed reduced ideal stratum with the relative Grassmannian stated above. Grassmannians and their relative versions are smooth and geometrically irreducible here, and the usual dimension formula gives the asserted dimension.

## Verification

The included `checks/verify_rectangular_band.py` enumerates **every reduced-row-echelon subspace** of the full coefficient vector space in seven small configurations. For each subspace it checks ideal closure by directly multiplying its basis vectors by each of the original semigroup basis elements in both orders; this check does not use the classification or the row/column conditions. It independently compares the resulting dimension histogram with the Gaussian-binomial formula. It includes arithmetic in \(\mathbb F_4\) via an explicit quadratic extension representation. All seven complete enumerations agree. The output is embedded as `checks/verify_rectangular_band_output.txt`, ending in `RECTANGULAR_BAND_IDEALS_OK 7 EXHAUSTIVE_CASES`.

Exhaustive finite tests corroborate the theorem but do not prove assertions for arbitrary \(m,n,k\); that role belongs to the algebraic argument above.

## Relationship to prior work

Margolis and Steinberg's *Quivers of monoids with basic algebras* (arXiv:1101.0416v1, January 2, 2011) provides foundational semigroup-algebra representation theory. Its quiver and support-semilattice statements are not the same as a classification of **all linear two-sided ideals** of the nonunital rectangular-band algebra. The support semilattice records semigroup principal ideals, whereas the Gaussian-family ideals here are often not spanned by subsets of semigroup elements.

Munn's *The Jacobson radical of a band ring* (1989) describes radicals of general band rings; our radical identity is consistent with that established subject. The present all-ideal Grassmannian parametrization and dimension-resolved counting are additional assertions. The accessible extract does not settle whether its full text contains a stronger special-case statement, so publication-priority uncertainty remains.

Steinberg's *Quiver presentations for band algebras are defined over the integers* (arXiv:2601.06587v1) gives quiver presentations for connected bands, whose semigroup algebras are unital. The rectangular bands with both parameters at least two considered here are not connected, and that theorem does not furnish the present counting formula. General module/quiver methods remain relevant context, not independent novelty certificates.

## Limitations

Only rectangular-band semigroup algebras are classified. No claim is made for arbitrary completely simple semigroups, nontrivial Rees sandwich matrices, nonfield coefficients, one-sided ideals, or ideals of unitizations. The geometric statement covers the locally closed **reduced** dimension/rank strata; no claim is made about nilpotent scheme structure, intersections of closures, or irreducible components of the entire ideal scheme. The earlier literature has not been exhaustively verified, and an independent mathematical audit has not been performed.

## References

1. S. W. Margolis and B. Steinberg, *Quivers of monoids with basic algebras*, arXiv:1101.0416v1 (2011-01-02), https://arxiv.org/abs/1101.0416 .
2. W. D. Munn, *The Jacobson radical of a band ring*, Math. Proc. Cambridge Philos. Soc. 105 (1989), 277–283, https://doi.org/10.1017/S0305004100067761 .
3. B. Steinberg, *Quiver presentations for band algebras are defined over the integers*, arXiv:2601.06587v1, https://arxiv.org/abs/2601.06587 .
