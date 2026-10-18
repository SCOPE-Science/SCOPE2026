# Singular components and transverse quadrics of matching-zero determinant hypersurfaces

## Finding

**Theorem.** Fix an algebraically closed field \(K\) of characteristic zero. Let \(n\geq4\) and \(1\leq k\leq n\). Let \(L_{n,k}\) be the space of \(n\times n\) matrices \(A=(a_{ij})\) subject only to \(a_{11}=\cdots=a_{kk}=0\), and let \(X_{n,k}\subset\mathbb P(L_{n,k})\) be the degree-\(n\) determinant hypersurface. Put \(N=n^2-k\).

Then \(X_{n,k}\) is irreducible, normal, Cohen–Macaulay and Gorenstein. Its complete **reduced** singular locus is

\[
\operatorname{Sing}(X_{n,k})_{\mathrm{red}}=
 D_{n,k}\ \cup\ \bigcup_{i=1}^{k}H_i,
\]

where \(D_{n,k}=\{[A]:\operatorname{rank}(A)\le n-2\}\) and \(H_i=\{[A]: a_{ij}=a_{ji}=0\text{ for every }j\}\). These are exactly \(k+1\) distinct irreducible components. Inside \(X_{n,k}\), the component \(D_{n,k}\) has codimension \(3\) and degree \(n^2(n^2-1)/12\); each \(H_i\) is a linear space of codimension \(2n-3\) and degree \(1\).

At a general point of \(D_{n,k}\), the completed transverse local hypersurface is the three-dimensional ordinary quadratic cone \(uv-wz=0\). At a general point of \(H_i\), the transverse hypersurface is the ordinary nondegenerate quadratic cone \(\sum_{j=1}^{n-1}u_jv_j=0\). All these general singular points have multiplicity \(2\). The statements concern the **reduced** singular locus, not the possibly nonreduced Jacobian scheme.

## Assumptions and scope

Coordinates on \(L_{n,k}\) are the \(N\) independent entries outside a partial matching of \(k\) forbidden diagonal cells. The coordinate hyperplanes have been simultaneously permuted so that the forbidden cells are \((1,1),\ldots,(k,k)\); row and column permutations make this equivalent to any forbidden partial matching. All schemes are over \(K\); generic means a point of a nonempty Zariski-open subset of the indicated irreducible component. Codimensions stated for components are **inside the hypersurface** (ambient projective codimension is one larger).

## Proof

**1. Jacobian calculation and set-theoretic decomposition.** Let \(F(A)=\det(A)\) restricted to \(L_{n,k}\). The independent partial derivatives are precisely the cofactors \(C_{ij}(A)\) for allowed cells \((i,j)\). If \(\operatorname{rank}(A)\le n-2\), all these cofactors vanish. If \(\operatorname{rank}(A)=n-1\), the adjugate matrix has rank one: \(\operatorname{adj}(A)=uv^{\mathsf T}\) for nonzero vectors \(u,v\), with the harmless row/column index reversal arising from the cofactor convention. The gradient vanishes exactly when the support rectangle \(\operatorname{supp}(u)\times\operatorname{supp}(v)\) is contained in the forbidden partial matching. A nonempty Cartesian product contained in a matching must be the singleton \(\{(i,i)\}\) for some \(i\le k\). Hence the left and right kernels of \(A\) are both supported on the \(i\)-th coordinate, equivalently the \(i\)-th row and column vanish. Conversely, this condition makes every allowed cofactor vanish. Rank-\(n\) matrices do not lie on \(X_{n,k}\). The displayed reduced set equality follows.

**2. Irreducibility and dimension of the corank-two component.** Set \(r=n-2\ge2\). Parametrize matrices of rank at most \(r\) by \(A=UV^{\mathsf T}\), with \(U,V\) each of size \(n\times r\). For each \(i\le k\), the sole restriction on the pair of row vectors \((U_i,V_i)\) is \(U_i\cdot V_i=0\). Each polynomial \(U_i\cdot V_i\) is an irreducible, geometrically integral quadric because \(r\ge2\), and restrictions for different \(i\) involve disjoint variables. Their parameter space is irreducible of dimension \(2nr-k\). Its full-rank-pair locus is nonempty: take a partial permutation matrix of rank \(r\) supported in allowed cells, constructed below. The factorization fibers over the rank-\(r\) locus are the \(\mathrm{GL}_r\) orbits of dimension \(r^2\). Consequently the affine image \(D_{n,k}\) has dimension \(2nr-k-r^2=n^2-k-4=N-4\) and its projectivization has dimension \(N-5\). Thus it is irreducible of ambient codimension \(4\), hence codimension \(3\) inside the determinant hypersurface.

For completeness, there is an allowed rank-\(r\) partial permutation with the two unused row indices \(\{1,2\}\) and two unused column indices \(\{3,4\}\): the remaining \(r\) rows admit a bijection to the remaining \(r\) columns avoiding fixed points, since the bipartite graph of available pairs is complete minus at most one forbidden neighbor per vertex. For \(r\ge2\), Hall's condition holds (and for \(r=2\) these two index sets are disjoint). The four cells in \(\{1,2\}\times\{3,4\}\) are all free. Near this rank-\(r\) point, the four Schur-complement entries give independent transverse coordinates. The rank-\(r\) locus of \(D_{n,k}\) is therefore smooth at this point; by irreducibility, smoothness holds generically.

The standard determinantal degree formula for the corank-two locus in \(\mathbb P^{n^2-1}\) is \(\binom n2^2-n\binom n3=n^2(n^2-1)/12\). The matching-zero conditions define a linear section of the expected codimension \(k\), as the dimension calculation just proved. Its degree is consequently unchanged.

**3. Linear components.** For \(i\le k\), the row/column-zero condition comprises exactly \(2(n-1)\) independent linear equations in \(L_{n,k}\). Thus \(H_i\) is irreducible of ambient codimension \(2n-2\), and codimension \(2n-3\) in \(X_{n,k}\). It contains points with rank \(n-1\): choose the complementary \((n-1)\times(n-1)\) block to be an invertible partial-permutation matrix avoiding its forced diagonal zeros (possible since \(n-1\ge3\)). Thus \(H_i\not\subset D_{n,k}\), and the \(H_i\) are pairwise distinct and not contained in one another. Because \(D_{n,k}\) has a generic matrix without any zero row or column, it is not contained in any \(H_i\). These are all the irreducible components of the reduced singular locus.

**4. Irreducibility and normality.** The determinant polynomial is not identically zero: an invertible permutation matrix avoiding all forbidden cells exists. The singular locus computed above has ambient codimension at least \(4\). A nonconstant homogeneous polynomial with a repeated irreducible factor has a singular divisor; and if its reduced polynomial has at least two distinct factors, their projective hypersurfaces meet in codimension at most \(2\) and their intersection is singular. Both possibilities contradict the computed singular-locus codimension. Thus \(F\) is irreducible and squarefree. Being a hypersurface, \(X_{n,k}\) is Cohen–Macaulay, hence satisfies Serre's \(S_2\) condition. The singular locus has codimension at least \(3\) in \(X_{n,k}\), so \(R_1\) holds. Serre's criterion gives normality; a hypersurface is Gorenstein.

**5. Generic transverse equations.** At a rank-\(r\) smooth point of \(D_{n,k}\) where an \(r\times r\) minor is invertible, block Gaussian elimination gives \(F=\det(B)\det(S)\), with \(S\) a \(2\times2\) Schur complement. The explicit partial-permutation point above proves the four entries of \(S\) are independent normal parameters at some point; consequently the same holds on a dense open subset of \(D_{n,k}\). After multiplying by a unit and choosing transverse parameters, the equation is \(uv-wz=0\). At a rank-\(n-1\) point of \(H_i\), rearrange the matrix as \(\bigl(\begin{smallmatrix}0&\ell\\r&B\end{smallmatrix}\bigr)\) with invertible \(B\). Schur complementation yields \(F=-\det(B)\,\ell B^{-1}r\). The invertible linear change \(r\mapsto B^{-1}r\) gives the nondegenerate quadratic form \(\sum_{j=1}^{n-1}u_jv_j\), with the entries of \(B\) serving as smooth parameters. Both quadratic forms have multiplicity \(2\). This finishes the proof.

## Verification

Two standard-library exact-arithmetic scripts accompany this result: `verify/check_sparse.py` and `verify/check_transverse.py`. Run `python3 verify/check_sparse.py` and `python3 verify/check_transverse.py` from the directory containing the `verify` folder. The first checks the Jacobian-singularity criterion against the proposed rank/row-column description in \(65{,}668\) finite-field examples, including exhaustive small binary cases. The second constructs nine rank-\(n-2\) finite-field witnesses and computes rank \(4\) for the differential of the full set of corank-two minors, supporting the transverse codimension calculation. These experiments are corroboration; the infinite-family proof above is independent of finite enumeration. No tests over the characteristic-zero base field are required for the proof.

## Relationship to prior work

Boocher's work on sparse generic determinantal ideals (arXiv:1111.0279, first public version 2011-11-01) develops minimal free resolutions and explains earlier Giusti–Merle results on codimension, primeness, and Cohen–Macaulayness governed by zero rectangles. Alper–Bogart–Velasco (arXiv:1505.02205, 2015-05-08) studies general singular-codimension restrictions for determinantal representations. Neither inspected article supplies the explicit \(k+1\) reduced singular-component decomposition, degrees, and two generically different transverse quadratic forms for the partial-matching zero pattern. The full text of Giusti–Merle's 1982 chapter could not be inspected; it remains the most important literature-overlap caveat.

## Limitations

The classification is restricted to \(n\ge4\), characteristic zero, and zero patterns consisting of a partial matching. It identifies the **reduced** singular locus, rather than an embedded-component decomposition of the Jacobian ideal. It does not claim classification of nongeneric singularities or a complete scheme-theoretic resolution. The 1982 Giusti–Merle full-text access gap, and possible uncatalogued equivalent characterizations in the specialized sparse-determinantal literature, remain residual originality risks; the mathematical theorem is not independently audited.

## References

1. A. Boocher, *Free Resolutions and Sparse Determinantal Ideals*, arXiv:1111.0279, https://arxiv.org/html/1111.0279v2 (first public version 2011-11-01).
2. D. Giusti and M. Merle, *Singularités isolées et sections planes de variétés déterminantielles II*, 1982, DOI: 10.1007/BFb0071278; full text not available for inspection.
3. J. Alper, T. Bogart, M. Velasco, *A lower bound for the determinantal complexity of a hypersurface*, arXiv:1505.02205, https://arxiv.org/html/1505.02205v1 (first public version 2015-05-08).
4. W. Fulton, *Intersection Theory*, 2nd ed., Springer (1998), Thom–Porteous formula for degrees of generic determinantal varieties.
