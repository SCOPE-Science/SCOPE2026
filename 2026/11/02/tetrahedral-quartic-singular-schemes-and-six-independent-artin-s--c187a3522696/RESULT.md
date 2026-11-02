# Tetrahedral quartic singular schemes and six independent Artin–Schreier pairs

## Finding

Let \(k\) be an algebraically closed field of characteristic \(2\), with homogeneous coordinates \(x_1,x_2,x_3,x_4\) on \(\mathbf P^3_k\). For coefficients \(b_i\in k^\times\) and \(a_{ij}\in k\), \(1\leq i<j\leq4\), put
\[
Q=\sum_{i=1}^4 b_i x_i^2+\sum_{1\leq i<j\leq4}a_{ij}x_ix_j,
\qquad F=x_1x_2x_3x_4+Q^2,
\qquad X=V(F).
\]
This is the coordinate-tetrahedral family appearing in Catanese and Schütt's construction of twelve-nodal quartic surfaces. Write \(S=\{(i,j):a_{ij}=0\}\) and \(r=|S|\). The following conclusions hold for **every** coefficient choice satisfying \(b_1b_2b_3b_4\ne0\), not merely for a general member.

1. The quartic \(X\) is geometrically integral and normal. Its complete reduced singularity basket is
\[
\boxed{2(6-r)A_1+rA_3.}
\]
At the two distinct singularities on an edge with \(a_{ij}\ne0\), the completed local surface ring is \(k[[U,V,W]]/(UV+W^2)\). At the single singularity on an edge with \(a_{ij}=0\), it is \(k[[U,V,W]]/(UV+W^4)\). The latter is an \(A_3\) rational double point. The six coordinate hyperplanes \(a_{ij}=0\) form the entire geometric collision discriminant of the twelve general nodes; all \(2^6\) zero/nonzero patterns occur.

2. Over the ten-dimensional coefficient base
\[
B=\operatorname{Spec} k[b_1^{\pm1},\ldots,b_4^{\pm1},a_{12},\ldots,a_{34}],
\]
the relative projective singular scheme defined by \(F\) and its four partial derivatives is **finite flat of degree \(24\)**. It is the disjoint union of six relative subschemes \(Z_{ij}\) on the six coordinate edges. Each \(Z_{ij}\) is cut on its edge by \(Q^2\), hence is a relative effective Cartier divisor of degree \(4\). Its geometric local lengths are \(2+2\) when \(a_{ij}\ne0\) and \(4\) when \(a_{ij}=0\). Thus the sum of local Tjurina lengths is constantly \(24\), even though the number of support points decreases from \(12\) to \(6\).

3. On the generic open subset where all six \(a_{ij}\ne0\), the field obtained by adjoining the coordinates of **all twelve labeled singular points** has Galois group
\[
\boxed{(\mathbf Z/2\mathbf Z)^6}
\]
over the rational function field \(k(b_1,\ldots,b_4,a_{12},\ldots,a_{34})\). The action independently exchanges the two singularities on each coordinate edge. This is full six-fold elementary-abelian monodromy, not simply six separate quadratic equations.

4. If the coefficients belong to \(\mathbf F_q\), for \(q=2^m\), then the one singular point on an edge with \(a_{ij}=0\) is \(\mathbf F_q\)-rational. On an edge with \(a_{ij}\ne0\), both singular points are \(\mathbf F_q\)-rational if and only if
\[
\boxed{\operatorname{Tr}_{\mathbf F_q/\mathbf F_2}
 \left(\frac{b_i b_j}{a_{ij}^{2}}\right)=0.}
\]
Otherwise they form one conjugate degree-two pair. Consequently the number of rational geometric singular points is exactly
\[
\#\operatorname{Sing}(X)(\mathbf F_q)
=\#\{(i,j):a_{ij}=0\}
+2\#\left\{(i,j):a_{ij}\ne0,\ \operatorname{Tr}\left(\frac{b_i b_j}{a_{ij}^2}\right)=0\right\}.
\]
Here \(\operatorname{Sing}(X)(\mathbf F_q)\) refers to the underlying singular-point support, not the length of its nonreduced Jacobian scheme.

## Assumptions and scope

The characteristic is **exactly** \(2\). The four diagonal coefficients of \(Q\) are required to be nonzero; that condition excludes the coordinate vertices from \(X\) and is essential to the six-disjoint-edge decomposition. The base \(B\) is the marked-coordinate coefficient parameter space, not a coarse moduli space of quartic surfaces. The term “collision discriminant” means the locus where a pair of *geometric singular supports* on a marked coordinate edge merges, not the non-étale locus of the already nonreduced relative Jacobian scheme. The assertion about Galois monodromy concerns the function field of this marked coefficient space.

## Proof

**Step 1: the entire relative singular scheme.** In characteristic \(2\), differentiation kills every square. Thus
\[
\frac{\partial F}{\partial x_i}=\prod_{h\ne i}x_h
\qquad (i=1,2,3,4).
\]
The simultaneous vanishing locus of these four derivatives in \(\mathbf P^3\) is the union of the six coordinate lines \(L_{ij}\) on which precisely the coordinates \(x_i,x_j\) are permitted to be nonzero. Their pairwise intersections, when nonempty, are coordinate vertices. At the \(i\)-th vertex, \(F=b_i^2\ne0\). Hence the singular scheme \(V(F,F_{x_1},\ldots,F_{x_4})\) is supported away from the vertices and decomposes scheme-theoretically into six disjoint components
\[
Z_{ij}=V\bigl(x_h\ (h\notin\{i,j\}),\ (b_ix_i^2+a_{ij}x_ix_j+b_jx_j^2)^2\bigr)
\quad\text{on }L_{ij}\cong\mathbf P^1.
\]
The quadratic factor does not vanish identically on any fiber because \(b_i,b_j\) are units. Its square cuts an effective degree-four Cartier divisor on each relative \(\mathbf P^1\), finite locally free of rank four over \(B\); the support avoids the vertices because the endpoint values are units. The six components are disjoint over \(B\), proving finite flatness of rank \(6\cdot4=24\).

**Step 2: locations, local types, and completeness.** Fix an edge \(L_{ij}\) and dehomogenize by \(x_i=1\). Set \(x_j=t\), and denote the remaining coordinates by \(u,v\). Then
\[
F=tuv+Q(t,u,v)^2,
\qquad Q(t,0,0)=g(t):=b_i+a_{ij}t+b_jt^2.
\]
The roots of \(g\) are nonzero, as \(b_i,b_j\ne0\). Moreover the three local partial derivatives of \(F\) are \(uv,tv,tu\), so, at any root \(t_0\), the local Jacobian ideal is precisely \((u,v)\). The completed Tjurina algebra is therefore
\[
k[[t-t_0,u,v]]/(F,F_t,F_u,F_v)
\cong k[[t-t_0]]/(g(t)^2).
\]
If \(a_{ij}\ne0\), then \(g'(t)=a_{ij}\ne0\); it has two distinct roots, each giving \(k[[s]]/(s^2)\). More strongly, \((u,v,Q)\) are formal coordinates near either root, so the exact local equation is \(UV+W^2=0\), after setting \(U=tu\) and \(V=v\).

If \(a_{ij}=0\), then \(g(t)=b_j(t-t_0)^2\) has exactly one geometric root, giving \(k[[s]]/(s^4)\). To identify its analytic type (rather than merely its length), regard \(s=t-t_0\) as a formal parameter. The function \(F\) has no terms linear in \((u,v)\); its quadratic part in these two variables has a nondegenerate polar form because the coefficient of \(uv\) from \(tuv\) is the unit \(t_0+s\), whereas the square \(Q^2\) has zero mixed polar form. Over the complete Henselian ring \(k[[s]]\), its nondegenerate binary quadratic form is hyperbolic: it is hyperbolic modulo \(s\) because \(k\) is algebraically closed, and its isotropic directions lift by Hensel's lemma (the polar coefficient is a unit). A linear change in \((u,v)\) makes that form \(UV\). The higher terms in \((U,V)\) can then be removed successively by formal coordinate changes: every monomial of total \((U,V)\)-degree at least three is divisible by \(U\) or \(V\), so the linearization \(\delta(UV)=V\delta U+U\delta V\) eliminates each successive homogeneous degree, and the changes converge adically. The residual term is precisely \(F(s,0,0)=b_j^2s^4\); rescale \(s\) to obtain the completed equation \(UV+W^4=0\). This proves the asserted \(A_3\) type and the four-point Tjurina length.

No other singularities exist by Step 1. Every stratum specified by a subset of the six equations \(a_{ij}=0\), with the other coefficients nonzero, is nonempty (choose \(b_i=1\)). Its basket is \(2(6-r)A_1+rA_3\). A hypersurface surface in \(\mathbf P^3\) is Cohen–Macaulay. Its singular locus here is finite, so it is normal if integral; indeed a reducible or nonreduced projective quartic in \(\mathbf P^3\) would have a positive-dimensional singular locus, contrary to Step 1. It is therefore geometrically integral and normal.

**Step 3: full generic monodromy.** Work over the function field \(K=k(b_1,\ldots,b_4,a_{12},\ldots,a_{34})\). For an edge \((i,j)\), its coordinate \(t\) solves \(b_jt^2+a_{ij}t+b_i=0\). The substitution \(z=b_jt/a_{ij}\) converts the equation to the Artin–Schreier equation
\[
z^2+z=\frac{b_ib_j}{a_{ij}^2}.
\]
Adjoin the square roots \(c_i\) of the four independent \(b_i\) to make a purely inseparable field extension \(K'/K\). Over \(K'\), the displayed Artin–Schreier class is equivalent modulo \(h^2+h\) to \(c_ic_j/a_{ij}\), since \((c_ic_j/a_{ij})^2=b_ib_j/a_{ij}^2\). Any nonempty \(\mathbf F_2\)-linear combination of the six classes has, along an edge-specific divisor \(a_{ij}=0\) included in that combination, a simple pole with nonzero residue coefficient. No rational function of the form \(h^2+h\) can have an odd-order pole: a pole of order \(d>0\) in \(h\) produces one of order \(2d\). Therefore all six classes are independent in \(K'/(\operatorname{AS}K')\). Their compositum has degree \(2^6=64\) and Galois group \((\mathbf Z/2)^6\). A purely inseparable field extension cannot reduce the degree of this separable compositum, so the same conclusion holds over \(K\).

**Step 4: finite-field arithmetic.** Over \(\mathbf F_{2^m}\), \(a_{ij}=0\) makes \(g\) a quadratic in squares with a unique rational root, since squaring is bijective. If \(a_{ij}\ne0\), the Artin–Schreier equation from Step 3 is solvable over \(\mathbf F_{2^m}\) exactly when the absolute trace of its right side is zero. In the solvable case there are exactly two roots, and otherwise there is an irreducible degree-two pair. Summing edge by edge gives the formula in the Finding.

## Verification

The standalone file `verify_tetrahedral.py` performs exact computations in finite fields of characteristics two, with no third-party dependencies. It checks the **entire** set of \(2^6=64\) binary off-diagonal patterns with \(b_i=1\): enumerating every point of \(\mathbf P^3(\mathbf F_4)\), evaluating the quartic and its four partial derivatives, and comparing the resulting singular-point support with the six explicit edge quadratics. The seven counts of patterns according to the number of vanishing off-diagonal coefficients are \(1,6,15,20,15,6,1\). It separately checks the trace splitting criterion on all \(4{,}028\) triples of nonzero diagonal and arbitrary off-diagonal coefficients over \(\mathbf F_4\), \(\mathbf F_8\), and \(\mathbf F_{16}\). The successful terminal marker is `TETRAHEDRAL_CHAR2_64_SURFACES_4028_TRACE_CASES_PASS`.

The universal geometric classification, flatness, and Galois group are established by the symbolic arguments above; finite tests alone would not prove them.

## Relationship to prior work

Catanese and Schütt, *Singularities of normal quartic surfaces III* (arXiv:2206.03295, first submitted June 7, 2022), Section 3.8, Example 19, introduce the general \(\ell_1\ell_2\ell_3\ell_4+q^2\) construction, state the general twelve-node behavior, and separately discuss a special Dwork pencil with six \(A_3\) points. Their preceding *Part II* (arXiv:2110.03078, first submitted October 6, 2021) studies the characteristic-two Gauss map, Gaussian defects and singularity restrictions, including the relevant local \(A_1\) phenomenon. Dolgachev and Kondō, *Desmic quartic surfaces in arbitrary characteristic* (arXiv:2505.01033, May 2, 2025), Section 7, prove that a distinguished one-parameter characteristic-two Kummer quartic family has six \(A_3\) points. These results provide two endpoints and substantial background, but do not give the marked ten-parameter relative singular scheme, its six independent collision hyperplanes, full generic \((\mathbf Z/2)^6\) splitting-field monodromy, or the finite-field trace classification asserted here.

The result does **not** claim novelty for the existence of a twelve-node quartic, the existence of the six-\(A_3\) special family, the normal-form definition of an \(A_n\) singularity, or the Artin–Schreier criterion itself. Its contribution is the combined exact global and arithmetic classification for this natural parameter family.

## Limitations

The hypothesis \(b_i\ne0\) is essential. When some \(b_i=0\), coordinate vertices may enter the surface, the singular components can meet, and the classification is not asserted. No classification of projective-isomorphism classes or Picard lattices is claimed. The Galois group concerns marked singular points over the coefficient function field, not the étale fundamental group of a coarse moduli space. An equivalent calculation in unindexed literature remains possible. The proof and finite tests have not undergone independent external mathematical validation.

## References

1. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces II (char=2)*, arXiv:2110.03078v1, first public submission 2021-10-06. https://arxiv.org/abs/2110.03078
2. F. Catanese and M. Schütt, *Singularities of normal quartic surfaces III (char=2, non-supersingular)*, arXiv:2206.03295v1, first public submission 2022-06-07, especially Example 19. https://arxiv.org/html/2206.03295v1
3. I. Dolgachev and S. Kondō, *Desmic quartic surfaces in arbitrary characteristic*, arXiv:2505.01033v1, first public submission 2025-05-02, especially Section 7. https://arxiv.org/abs/2505.01033
4. MSC2020, category 14J17, Singularities of surfaces or higher-dimensional varieties. https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=14J28
