# The geometry of the square-zero derivation cone of a Heisenberg Lie algebra

## Finding

Let \(k\) be any field, \((V,\omega)\) a split symplectic space of dimension \(2r\) with \(r\ge 1\), and \(\mathfrak h=V\oplus kz\) the Heisenberg Lie algebra with \([v,w]=\omega(v,w)z\). Let \(X\) be the reduced affine locus of ordinary derivations \(D\) with \(D^2=0\). Then \(X\) is geometrically irreducible, is rational over \(k\), and has dimension \(r(r+2)\). The open set where the induced endomorphism of \(V=\mathfrak h/kz\) has rank \(r\) is isomorphic to a bundle over the Lagrangian Grassmannian whose fiber over \(L\) consists of nonsingular symmetric bilinear forms on \(L^*\) and functionals on \(V/L\).

When \(r=1\), the projective variety of nonzero square-zero derivations up to scaling is the smooth cubic rational normal scroll \(S(1,2)\subset \mathbb P^4_k\). The affine cone is smooth off its vertex and singular there. These statements hold also in characteristic two.

## Assumptions and scope

The symplectic form is alternating and nondegenerate in every characteristic. These are ordinary Lie derivations; there is no required compatibility with a restricted power operation. The assertion concerns the reduced locus, including its underlying reduced geometry over an algebraic closure; it does not assert that the original defining system of equations is a reduced scheme. No singular-locus classification in higher dimensions is claimed.

## Proof

The center and the derived algebra of \(\mathfrak h\) both equal \(kz\). Thus a derivation has the form \(D(v)=Av+f(v)z\), \(D(z)=\lambda z\), where \(f\in V^*\) and the Leibniz rule reads \(\omega(Av,w)+\omega(v,Aw)=\lambda\omega(v,w)\). Since \(D^2(z)=\lambda^2z\), the reduced square-zero locus is given by
\[
 A\in\mathfrak{sp}(V,\omega),\qquad A^2=0,\qquad fA=0.
\]
These conditions are also sufficient. For such an \(A\), \(U=\operatorname{im}A\) is isotropic by \(\omega(Au,Av)=-\omega(u,A^2v)=0\), and \(\ker A=U^\perp\) by skew-adjointness and dimension. In particular \(\dim U\le r\).

Over the Lagrangian Grassmannian \(\operatorname{LG}(V)\), consider the incidence variety of triples \((L,B,f)\) with \(L\) Lagrangian, \(B:V/L\to L\) symmetric under \(V/L\simeq L^*\) by the symplectic pairing, and \(f|_L=0\). Locally on the Grassmannian the \(B\) coordinates are those of an arbitrary symmetric matrix on \(L^*\); these include the diagonal entries also in characteristic two. The triples form a vector bundle of rank \(r(r+1)/2+r\). There is a map to \(X\) taking \(A\) to the composite \(V\to V/L\xrightarrow{B}L\hookrightarrow V\) and retaining \(f\).

For surjectivity on geometric points, write \(f(v)=\omega(w,v)\). Since \(fA=0\), the vector \(w\) is in \(U^\perp\), so \(U+kw\) is isotropic: in particular \(\omega(w,w)=0\). Extend this space to a Lagrangian \(L\). Now \(U\subseteq L\subseteq U^\perp=\ker A\), and \(f|_L=0\). Hence \(A\) factors through \(V/L\) to \(L\), and its skew-adjointness is exactly the symmetry of \(B\) under the indicated pairing. This argument works over each field of definition of a point. The total space of the incidence bundle is geometrically irreducible because the Lagrangian Grassmannian is; thus the map and the geometric point coverage show geometric irreducibility of the target.

Over the open set \(\operatorname{rank} A=r\), one necessarily has \(L=\operatorname{im}A\) and \(B\) nonsingular. Taking the image of a constant-rank matrix is a morphism to the Grassmannian, as seen on charts by choosing a nonvanishing maximal minor. Taking \(L=\operatorname{im}A\), the induced \(B\), and the given \(f\) defines the inverse morphism there. In particular, the open rank-\(r\) locus is a nonempty open in the indicated bundle with the nonsingularity condition. A chart of the Lagrangian Grassmannian is the set of graphs of symmetric matrices over a fixed Lagrangian complementary to another one, an affine space of dimension \(r(r+1)/2\); the incidence bundle is trivial over this chart. This proves rationality over \(k\) and gives the dimension \(r(r+1)/2+r(r+1)/2+r=r(r+2)\).

For \(r=1\), use a symplectic basis and put \(A=\left(\begin{smallmatrix}a&b\\ c&-a\end{smallmatrix}\right)\), \(f=(u,v)\). Then \(a^2+bc=au+cv=bu-av=0\). These are the minors of the matrix
\[
\begin{pmatrix} b&-a&v\\-a&-c&-u\end{pmatrix}
\]
up to signs. If the point is nonzero, the columns span a unique line \(L=k(s,t)\). Equivalently it is \(\operatorname{im}A\) if \(A\ne0\), and \(\ker f\) otherwise. For this \(L\) the projective coordinates have the form
\[
[a:b:c:u:v]=[-\alpha st:\alpha s^2:-\alpha t^2:-\beta t:\beta s].
\]
The two fiber coordinates in the incidence bundle over \(\mathbb P^1\) have bundles \(\mathcal O(-2)\) and \(\mathcal O(-1)\): the first comes from the symmetric map \(L^*\to L\), and the second from the identification of the annihilator of \(L\) with \(L\) via \(\omega\). The displayed map is the complete scroll embedding of the bundle of lines in \(\mathcal O(-2)\oplus\mathcal O(-1)\), given by the three quadratic and two linear monomials. The column-span construction gives its inverse over the nonvanishing-column charts, including characteristic two. The projective variety is therefore the smooth degree-three scroll. The affine punctured cone is the complement of the zero section in the tautological line bundle over the scroll, hence smooth. The cone spans all five affine coordinate directions (there is no linear relation among the embedding coordinates), so its vertex has tangent dimension five while the cone has dimension three.

## Relationship to prior work and verification

The exact finite-field rank spectrum of ordinary square-zero Heisenberg derivations is already given in [*Exact rank spectra of square-zero derivations of finite Heisenberg Lie algebras*](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-exact-rank-spectra-of-square-zero-derivations-of-finite-heisenbe--21c4a89e2fcd/RESULT.md). The isotropic-image parametrization is shared with that work; its finite-field counts are not a new claim here. The geometric step is to extend \(U\) to a Lagrangian while also requiring the central functional to vanish on it, thereby controlling the whole reduced locus by a single incidence bundle. Barnea and Melnikov ([arXiv:1509.06008](https://arxiv.org/abs/1509.06008)) study square-zero elements in the complex symplectic nilradical, without the functional in this incidence problem. La Rosa and Mancini ([arXiv:2301.11058](https://arxiv.org/abs/2301.11058)) describe derivation algebras; Feldvoss, Siciliano, and Weigel ([arXiv:1102.2629](https://arxiv.org/abs/1102.2629)) study outer restricted square-zero derivations. Neither the classical theory of scrolls nor the derivation normalization is asserted as new. The geometric conclusions are proved above, not inferred from finite examples.
