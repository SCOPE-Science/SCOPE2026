# Degree-twelve duals of characteristic-two quartics with a tetrahedral singular locus

## Finding

Let \(k\) be algebraically closed of characteristic \(2\), and let
\[
P(x)=x_1x_2x_3x_4,\qquad
Q(x)=\sum_{i=1}^4 b_i x_i^2+\sum_{1\le i<j\le4}a_{ij}x_ix_j,
\qquad b_1b_2b_3b_4\ne0.
\]
Set \(X=V(P+Q^2)\subset\mathbf P_k^3\). In dual coordinates \([u_1:u_2:u_3:u_4]\), write
\[
C_i(u)=\prod_{j\ne i}u_j,\qquad
G(u)=P(u)^3+Q(C_1(u),C_2(u),C_3(u),C_4(u))^2.
\]
Then the projective dual \(X^*\subset(\mathbf P_k^3)^*\) is exactly the **reduced, irreducible degree-twelve** hypersurface \(V(G)\). The Gauss map of \(X\), and the Gauss map of \(X^*\), restrict on their dense coordinate tori to the same cubic Cremona involution \([v_i]\mapsto[C_i(v)]\); both are birational and separable.

The reduced singular locus of \(X^*\) is **exactly the six coordinate lines**
\[
\operatorname{Sing}(X^*)_{\mathrm{red}}=
\bigcup_{1\le i<j\le4}\{u_i=u_j=0\}.
\]
The hypersurface has multiplicity exactly \(4\) at the generic point of each line and exactly \(8\) at each of the four coordinate vertices. In particular \(X^*\) is nonnormal. Each coordinate-plane section has the exact equation
\[
G\big|_{u_i=0}=b_i^2\prod_{j\ne i}u_j^4,
\]
so it is four times the coordinate triangle in that plane, as a Cartier divisor. These conclusions hold for **all** six off-diagonal coefficients \(a_{ij}\), without assuming the primal quartic has twelve distinct nodes.

## Assumptions and scope

The base field is algebraically closed of characteristic exactly \(2\). The four diagonal coefficients of the arbitrary homogeneous quadric \(Q\) are nonzero; its six cross coefficients are unrestricted. The term 'multiplicity' means the order of a local equation in the regular local ring of the ambient three-dimensional projective space, at the generic point of a line or at a closed vertex. The singular-locus equality is set-theoretic (reduced), **not** a claim about the full nonreduced Jacobian scheme. A projective dual is the Zariski closure of tangent hyperplanes to the smooth locus. Coordinates are fixed so the four linear forms in the source family are coordinate forms.

## Proof

**1. Normality and a dense smooth torus.** In characteristic \(2\), all derivatives of \(Q^2\) vanish. Thus
\[
\frac{\partial(P+Q^2)}{\partial x_i}=\prod_{j\ne i}x_j=C_i(x).
\]
All partial derivatives vanish precisely when at least two coordinates vanish. On the coordinate line where only \(x_i,x_j\) may be nonzero, the restriction of the quartic is the square of
\[
b_i x_i^2+a_{ij}x_ix_j+b_jx_j^2.
\]
This homogeneous binary quadratic is nonzero because \(b_i,b_j\ne0\), and consequently has only finitely many zeros. Hence \(X\) has isolated singularities. If its quartic equation were reducible, two projective surface components would meet in a curve of singular points; if it had a multiple factor, that factor would lie in a positive-dimensional singular locus. Both are impossible. Thus \(X\) is integral, and the hypersurface Cohen–Macaulay and regular in codimension one, so normal. No coordinate hyperplane is a component. The complement of all coordinate hyperplanes is therefore a nonempty dense open set of smooth points of \(X\).

**2. The reciprocal Gauss map and the equation.** Let \(T\) be the projective coordinate torus \(\{x_1x_2x_3x_4\ne0\}\). The standard cubic Cremona map
\[
\mathcal C:T\longrightarrow T,\qquad [x_i]\longmapsto[C_i(x)]
\]
is an involution: \(C_i(C(x))=P(x)^2x_i\). On \(X\cap T\), the Gauss map is \(\mathcal C\) by step 1. Homogeneity gives the exact polynomial identity
\[
G(C(x))=P(x)^8\bigl(P(x)+Q(x)^2\bigr).
\]
Hence the image of \(X\cap T\) is precisely \(V(G)\cap T\). On \(T\), this is a smooth integral surface, since it is the Cremona image of the smooth integral surface \(X\cap T\). On the coordinate hyperplane \(u_i=0\), all \(C_j(u)\) vanish except \(C_i(u)=\prod_{j\ne i}u_j\), so
\[
G\big|_{u_i=0}=Q(0,\dots,C_i(u),\dots,0)^2=b_i^2\prod_{j\ne i}u_j^4\ne0.
\]
No coordinate hyperplane is a component of \(V(G)\). Thus every irreducible component of \(V(G)\) meets \(T\), where there is only one reduced integral component. Moreover this component is generically reduced, and has no additional boundary factors. Consequently \(G\) is reduced and irreducible of homogeneous degree \(12\), and \(X^*=V(G)\).

**3. The complete reduced singular locus and biduality.** Differentiating \(G\) gives, because the derivative of a square vanishes in characteristic \(2\) and \(3=1\) in the field,
\[
\frac{\partial G}{\partial u_i}=P(u)^2C_i(u).
\]
On \(T\), all four partial derivatives are nonzero, so every point of \(V(G)\cap T\) is smooth. On the boundary \(P(u)=0\), every partial derivative vanishes. The coordinate-plane formula from step 2 shows that a boundary point lies on \(V(G)\) if and only if at least two of its coordinates vanish. This proves the six-line singular-support classification. Since this is a divisor in the two-dimensional integral hypersurface \(X^*\), the latter is not normal. On the torus, the gradient of \(G\) again gives \(\mathcal C\), which is an isomorphism of tori; this directly verifies separable birationality and reciprocal biduality, without invoking characteristic-zero biduality conventions.

**4. Exact generic multiplicities along the six lines.** Fix distinct \(i,j\), and work at the generic point of the line \(u_i=u_j=0\), where the other two coordinates are units. Let \(s=u_i\), \(t=u_j\) be transverse local parameters. Then \(C_i\) and \(C_j\) have order one, while \(C_k\), for \(k\notin\{i,j\}\), has order two. The quadratic initial form of \(Q(C(u))\) is
\[
(u_ku_\ell)^2\bigl(b_i t^2+a_{ij}st+b_j s^2\bigr),
\qquad \{k,\ell\}=\{1,2,3,4\}\setminus\{i,j\}.
\]
It is nonzero because the coefficients of \(s^2,t^2\) are nonzero. Its square has order \(4\), whereas \(P(u)^3\) has order \(6\). Therefore the local order of \(G\) is exactly \(4\).

**5. Exact vertex multiplicities.** At the coordinate vertex \([1:0:0:0]\), work in the chart \(u_1=1\), with remaining variables \(s=u_2\), \(t=u_3\), \(v=u_4\). Here \(C_1=stv\) has order three, while \(C_2=tv\), \(C_3=sv\), and \(C_4=st\) have order two. The degree-four initial form of \(Q(C(u))\) contains the three distinct nonzero monomials
\[
b_2t^2v^2+b_3s^2v^2+b_4s^2t^2,
\]
as well as possible cross terms of degree four. None cancels these three distinct square monomials, so that initial form is nonzero. Thus \(Q(C(u))^2\) has order eight, while \(P(u)^3\) has order nine. The vertex multiplicity is exactly eight. The same argument holds at every vertex.

## Verification

The standalone script `verify_dual.py` requires only Python 3. It constructs the universal polynomial over \(\mathbb F_2\) with fourteen independent variables (four dual coordinates, four diagonal coefficients, and six off-diagonal coefficients). It checks the exact degree-twelve formula, eleven monomials, all four universal partial derivatives, the four coordinate-plane restrictions, all six transverse orders and four vertex orders, and the Cremona substitution identity. It separately exhausts the \(85\) projective points of \(\mathbf P^3(\mathbb F_4)\) for \(Q=\sum x_i^2+\sum_{i<j}x_ix_j\), finding twelve primal singular points and \(18\) points on each of the matching torus surfaces. The script prints `CHAR2_DUAL_CREMONA_DEGREE12_SIX_QUADRUPLE_EDGES_FOUR_OCTUPLE_VERTICES_PASS`. These finite tests are supplemental; steps 1–5 supply the proof over every algebraically closed characteristic-two field.

## Relationship to prior work

Catanese and Schütt, *Singularities of normal quartic surfaces III (char=2, non-supersingular)*, first posted June 7, 2022, introduce the family \(l_1l_2l_3l_4+q^2=0\) in Example 19, equation (7), and establish the existence of general twelve-node members and geometric properties of its K3 resolutions. Their Example 19 and surrounding results do not state the equation or tetrahedral singular structure of its projective **dual**. Catanese's *Singularities of normal quartic surfaces I (char=2)* studies general inequalities using Gauss maps, notably Lemma 11 on nonnormal duals of nodal quartics. Those general results support the relevance of dual nonnormality but do not imply this family's explicit degree-twelve dual, entire singular support, and sharp local multiplicities. The generic Cremona involution is standard; it is the application to the specific family and complete boundary geometry that are asserted here. All priority statements are best-knowledge comparisons rather than an exhaustive historical uniqueness certification.

## Limitations

The theorem makes no claim about the nonreduced Jacobian scheme of the dual, normalization and conductor, exceptional singularities along the coordinate lines beyond the four vertices, Picard lattices, or arithmetic over non-algebraically-closed fields. The six lines are the **entire reduced** singular set, and the local multiplicities stated are exactly at generic line points and vertices; they do not assert uniform transverse analytic type along the lines. General source theorems about duality and birational geometry may subsume parts of the method, and unindexed characteristic-two projective-duality literature remains a priority risk. Independent mathematical validation has not been performed.

## References

1. Fabrizio Catanese and Matthias Schütt, *Singularities of normal quartic surfaces III (char=2, non-supersingular)*, arXiv:2206.03295v1 (first posted June 7, 2022), especially Section 3.8, Example 19, equation (7). https://arxiv.org/abs/2206.03295
2. Fabrizio Catanese, *Singularities of normal quartic surfaces I (char=2)*, arXiv:2106.09988 (first posted June 18, 2021), especially Section 3, Lemma 11, Proposition 12 and Theorem 14. https://arxiv.org/abs/2106.09988
