# Five embedded double defects in the Jacobian scheme of a reciprocal quartic threefold

## Finding

Let \(k\) be an algebraically closed field of characteristic zero. In \(\mathbb P_k^4\) take the elementary-symmetric quartic hypersurface
\[
X=V(F),\qquad F=e_4(x_0,x_1,x_2,x_3,x_4)=\sum_{i=0}^{4}\prod_{j\ne i}x_j.
\]
This is the one-circuit reciprocal (Orlik--Terao) hypersurface for a generic rank-four arrangement on five labeled hyperplanes. Denote its projective Jacobian singular scheme by \(Z=\operatorname{Proj}(S/J)\), where \(S=k[x_0,\ldots,x_4]\) and \(J=(\partial F/\partial x_0,\ldots,\partial F/\partial x_4)\). Write \(Y=Z_{\mathrm{red}}\), and let \(v_i=[0:\cdots:0:1:0:\cdots:0]\) be the five coordinate vertices.

**Theorem.** The hypersurface \(X\) is geometrically integral and normal. The scheme \(Y\) is the union of the ten coordinate projective lines, with saturated ideal
\[
I=\bigl(x_ix_jx_\ell:0\le i<j<\ell\le4\bigr).
\]
Each line has a generic transverse ordinary \(A_1\) surface singularity. The quotient sheaf \(\widetilde{I/J}\) is supported *exactly* at the five vertices, and its stalk at each vertex is a two-dimensional \(k\)-vector space annihilated by the local maximal ideal. Thus \(Z\) differs from the reduced union of lines by five embedded square-zero defects, each of length \(2\), of total length \(10\). The Hilbert polynomials are
\[
P_{\mathcal O_Y}(d)=10d-5,\qquad P_{\mathcal O_Z}(d)=10d+5
\]
for all sufficiently large integers \(d\). The reduced degree and the Jacobian-scheme degree are both \(10\).

## Assumptions and scope

All assertions use characteristic zero. A projective Jacobian scheme means the coherent closed subscheme cut out by the sheafification of the homogeneous ideal of partial derivatives; the Euler identity \(4F=\sum_ix_i\partial_iF\) makes the original equation redundant. A square-zero defect refers to the ideal sheaf of \(Y\) within \(Z\): its square is zero in a neighborhood of each affected vertex, and its stalk is killed by the maximal ideal. The theorem is **not** an assertion that the affine homogeneous quotient \(I/J\) has only finitely many nonzero graded pieces before taking sheafification.

The names “coordinate lines” and “vertices” refer to fixed coordinate subspaces of \(\mathbb P^4\), not to arrangements of independently chosen lines. The statement describes the whole scheme-theoretic Jacobian support modulo the reduced locus, rather than only a set-theoretic singularity decomposition.

## Proof

**1. Irreducibility and reduced singular support.** Write \(y=(x_1,x_2,x_3,x_4)\). Then \(F=x_0e_3(y)+e_4(y)\), and \(\gcd(e_3(y),e_4(y))=1\): no coordinate \(y_j\) divides \(e_3(y)\). As a primitive degree-one polynomial in \(x_0\), \(F\) is irreducible by Gauss's lemma.

If all five coordinates are nonzero, put \(P=\prod_i x_i\). On \(F=0\), the expression \(F=P\sum_i x_i^{-1}\) yields
\[
\frac{\partial F}{\partial x_i}= -\frac{P}{x_i^2}\ne0.
\]
With precisely four nonzero coordinates, \(F\) is their nonzero product, so such a point is not on \(X\). With precisely three nonzero coordinates, the derivative in either missing coordinate is the product of the three nonzero coordinates, hence is nonzero. With at most two nonzero coordinates, every gradient component is zero. This proves \(Z_{\mathrm{red}}=Y\), the union of all \(\binom52=10\) coordinate lines. Its saturated squarefree monomial ideal is \(I\) above. Since the singular locus has dimension one in the threefold \(X\), the hypersurface is regular in codimension one. It is Cohen--Macaulay, hence normal by Serre's \(R_1+S_2\) criterion.

**2. The quadratic transverse model off vertices.** At a general point of the line spanned by \(e_0,e_1\), both \(x_0,x_1\) are units and the other three coordinates \(a,b,c\) are normal coordinates. The degree-two initial form of \(F\) in these normal directions is a nonzero unit multiple of \(ab+ac+bc\). The symmetric Hessian is nondegenerate in characteristic zero, with determinant proportional to \(2\). Thus the transverse singularity is an ordinary \(A_1\) surface double point, and its three Jacobian normal equations generate \((a,b,c)\) in the completed local ring. Therefore \(J\) and \(I\) define the same scheme on each line away from its two coordinate endpoints.

**3. Exact local Jacobian at a vertex.** Work in \(x_0=1\), with affine coordinates \(y_1,\ldots,y_4\). Put
\[
q_i=e_2(y_1,\ldots,\widehat{y_i},\ldots,y_4),\quad
Q=(q_1,q_2,q_3,q_4),\quad
K=(y_iy_j:1\le i<j\le4),\quad
\mathfrak m=(y_1,y_2,y_3,y_4).
\]
The dehomogenization of \(F\) is \(f=e_3(y)+e_4(y)\). The original five projective partial derivatives become \(e_3(y)\) and
\[
\left.\frac{\partial F}{\partial x_i}\right|_{x_0=1}=(1-y_i)q_i+e_3(y)
\qquad(1\le i\le4).
\]
Since \(3e_3(y)=\sum_i y_iq_i\) and each \(1-y_i\) is invertible in \(k[y]_{\mathfrak m}\), the local Jacobian ideal is exactly \(Q_{\mathfrak m}\). The reduced union-of-lines ideal is \(K_{\mathfrak m}\).

**4. Two missing quadratic equations, with no higher-degree defect.** Among the six squarefree quadratic monomials in \(K_2\), the four quadrics \(q_i\) are linearly independent: their coefficient matrix has rank \(4\) over \(\mathbb Q\). Thus \(\dim_k(K_2/Q_2)=6-4=2\). The degree-three component \(K_3\) has dimension \(16\), with monomial basis all cubic monomials in four variables involving at least two distinct variables. The sixteen cubic multiples \(y_jq_i\), for \(1\le i,j\le4\), have a \(16\times16\) integer coefficient matrix in this ordered monomial basis. The exact determinant is \(48\), verified by the independently replayable fraction-free determinant algorithm in `check.py`.

It follows that \(Q_3=K_3\) in characteristic zero. Multiplication by the variables shows \(Q_d=K_d\) for all \(d\ge3\), or equivalently \(\mathfrak mK\subseteq Q\). Therefore \(K/Q\) is concentrated in degree two, has length \(2\), and is annihilated by \(\mathfrak m\); furthermore \(K^2\subseteq\mathfrak mK\subseteq Q\). Localization at \(\mathfrak m\) preserves these conclusions. Permuting the five coordinates gives the same stalk structure at every \(v_i\).

**5. Global sheaf and Hilbert polynomial.** Step 2 establishes \(\widetilde{I/J}=0\) away from the vertices, and steps 3--4 give five skyscraper stalks of length \(2\). The coherent ideal sequence on \(\mathbb P^4\)
\[
0\longrightarrow\widetilde{I/J}\longrightarrow\mathcal O_Z\longrightarrow\mathcal O_Y\longrightarrow0
\]
therefore adds constant Hilbert polynomial \(10\). The homogeneous coordinate ring \(S/I\) has, in every degree \(d\ge1\), a basis of monomials supported on at most two variables. The count is five pure powers plus \(10(d-1)\) mixed monomials: \(5+10(d-1)=10d-5\). Consequently \(P_{\mathcal O_Z}(d)=10d+5\). Since the quotient is zero-dimensional, it does not alter the leading coefficient (degree) of the one-dimensional scheme.

## Verification

The standalone stdlib-only Python 3 script `check.py` independently builds the coefficient matrix of the sixteen cubic multiples \(y_jq_i\), computes its exact Bareiss determinant \(48\), and confirms the rank-four matrix of quadrics. Its finite-field consistency checks enumerate all \(781\) points of \(\mathbb P^4(\mathbb F_5)\) and \(2801\) of \(\mathbb P^4(\mathbb F_7)\), finding precisely \(45\) and \(65\) singular points, respectively, all on coordinate lines; it checks the reduced Hilbert monomial count for degrees one through nine. On successful execution it prints `VERIFY_OK`.

To reproduce: run `python3 check.py` alongside this file. Exact integer computations certify the decisive finite matrix identity. Finite-field checks do **not** establish the characteristic-zero all-point theorem, which follows from the symbolic gradient, localization and sheaf arguments above. Characteristic two and three are deliberately excluded; the determinant \(48\) would not be invertible in those characteristics.

## Relationship to prior work

Proudfoot and Speyer (2004) introduce the reciprocal-circuit ring and its defining circuit equations, covering the present quartic as a uniform one-circuit instance. Their broken-circuit Gröbner theory does not state the nilpotent local Jacobian defects computed here. Denham, Garrousian and Tohaneanu (2012) study modular decomposition and resolutions of Orlik--Terao algebras, including generic-arrangement examples; the inspected results do not compute this quartic's Jacobian scheme. The complete set-theoretic singular support for elementary symmetric hypersurfaces is covered by an elementary argument recorded by Gjergji Zaimi (2017); the ten coordinate lines are acknowledged background, **not** the new result. The proposed contribution is the five exact embedded length-two square-zero stalks and their global Hilbert-polynomial consequence.

Related recent computations of embedded Jacobian defects for unrelated quartics or Hessian hypersurfaces neither use the same equation nor imply the present local ideal equality and determinant calculation. Searches under reciprocal-plane, one-circuit Orlik--Terao, elementary-symmetric Jacobian and coordinate-lines terminology found no direct covering statement. An equivalent computation in unindexed literature or an implicit corollary of a stronger general Jacobian-scheme theorem is a genuine residual originality risk.

## Limitations

The theorem is for one specific naturally defined reciprocal quartic in characteristic zero, not for every circuit size or positive characteristic. It computes the quotient of the Jacobian singular scheme by its reduction, but not a complete minimal graded free resolution or a general family-wide singular-scheme formula. The reduced component arrangement and the generic \(A_1\) form are not claimed as newly discovered. Computations of finite fields are auxiliary, not substitutions for the local algebra proof. No independent audit or external formal certification is asserted.

## References

1. Nicholas Proudfoot and David Speyer, *A Broken Circuit Ring*, arXiv:math/0410069, initially submitted 2004-10-05. https://arxiv.org/abs/math/0410069
2. Graham Denham, Mehdi Garrousian, and Stefan Tohaneanu, *Modular decomposition of the Orlik--Terao algebra of a hyperplane arrangement*, arXiv:1211.4562, initially submitted 2012-11-19. https://arxiv.org/abs/1211.4562
3. Gjergji Zaimi, answer to *Singular locus of zero set of elementary symmetric polynomial*, 2017-03-09. https://mathoverflow.net/questions/264226/singular-locus-of-zero-set-of-elementary-symmetric-polynomial
