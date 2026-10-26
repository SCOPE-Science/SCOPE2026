# A fifteen-line singular star in the characteristic-three symmetric Burkhardt quartic

## Finding

Let \(k\) be any algebraically closed field of characteristic \(3\), let \(e_r\) denote the elementary symmetric polynomial of degree \(r\) in six variables, and form the **specified symmetric integral model**
\[
\mathcal B=V(e_1,e_4)\subset\mathbb P^5_{\mathbb Z}.
\]
Its characteristic-three fibre \(B=\mathcal B\times_{\mathbb Z} k\) is an integral normal quartic threefold and is a projective cone with vertex
\[
E=[1:1:1:1:1:1]
\]
over an integral normal quartic surface \(S\subset\mathbb P^3_k\) with **exactly fifteen ordinary double points**, all defined over \(\mathbb F_3\). Indexing the six coordinate directions by \(i\in\{0,1,2,3,4,5\}\), these nodes are the fifteen classes of \(e_i-e_j\) in the quotient vector space \(\{\sum x_i=0\}/k(1,1,1,1,1,1)\), for \(i<j\). Here \(e_i\) in a vector expression denotes the \(i\)-th coordinate basis vector, not an elementary symmetric polynomial.

In particular, the **complete reduced singular locus** of \(B\) is
\[
\operatorname{Sing}(B)_{\mathrm{red}}
 =\bigcup_{0\le i<j\le5}L_{ij},\qquad
 L_{ij}=\mathbb P\langle(1,1,1,1,1,1),\,e_i-e_j\rangle.
\]
These are fifteen distinct \(\mathbb F_3\)-lines intersecting only at \(E\). Every point of each line away from \(E\) has a transverse ordinary-double-point surface singularity. At \(E\) the multiplicity is four. No assertion is made about the potentially nonreduced structure of the full Jacobian singular scheme at \(E\).

## Assumptions and scope

All equations are coefficientwise reductions of the displayed **six-coordinate** model. This choice is material: a second familiar five-coordinate quartic equation for the characteristic-zero Burkhardt variety is not related to this equation by a coordinate change integral and invertible at \(3\). The present result is not a stable-reduction statement and is not a claim about the characteristic-three moduli space of principally polarized abelian surfaces with full etale level-three structure.

For the cone construction let \(V=\{(x_0,\ldots,x_5)\in k^6:\sum_i x_i=0\}\), let \(\mathbf 1=(1,1,1,1,1,1)\), and let \(W=V/k\mathbf 1\). Since \(6=0\) in \(k\), \(\mathbf1\in V\), and \(\dim_k W=4\). The base surface lives in \(\mathbb P(W)\).

## Proof

**1. Cone identity.** In six variables the binomial identity for elementary symmetric polynomials reads
\[
e_4(x+t\mathbf1)=e_4(x)+3t e_3(x)+6t^2e_2(x)+10t^3e_1(x)+15t^4.
\]
On \(V\) in characteristic three, every extra term vanishes. Hence \(e_4|_V\) descends to a homogeneous quartic on \(W\), and \(B\) is the projective cone over its zero locus \(S\), with vertex \(E\). The descended polynomial is not zero, since its affine chart polynomial below is nonzero.

**2. Fifteen explicit base singular points.** For any \(i<j\), the vector \(e_i-e_j\) lies in \(V\) and has just two nonzero coordinates. It satisfies \(e_4=0\), and all first partial derivatives of \(e_4\) vanish there, because each is elementary symmetric of degree three in the other five coordinates. Its class is therefore singular on \(S\). The fifteen projective classes are distinct modulo \(k\mathbf1\): a projective relation between two such sparse vectors leaves at least two coordinates where both vanish, forcing the added multiple of \(\mathbf1\) to be zero; the two unordered pairs must then agree.

**3. Geometric completeness of the singular locus.** Subtract the last coordinate times \(\mathbf1\), so that \(x_5=0\). Write the five remaining coordinates as \(z_0,\ldots,z_4\) with \(\sum_{i=0}^4 z_i=0\). Thus
\[
S=V\bigl(\textstyle\sum_{i=0}^4 z_i,\ e_4(z_0,\ldots,z_4)\bigr)\subset\mathbb P^4_k.
\]
By permutation symmetry of these five coordinates, every singular point is carried into the chart \(z_0\ne0\). In that chart put
\[
z_0=1,\quad z_1=a,\quad z_2=b,\quad z_3=c,\quad
z_4=-1-a-b-c,
\]
and let \(g(a,b,c)=e_4(1,a,b,c,-1-a-b-c)\). The affine singular scheme is the zero scheme of \(g,g_a,g_b,g_c\). A direct exact Gröbner-basis computation over \(\mathbb F_3\), in lexicographic order \(a>b>c\), yields the following **monic reduced basis**:
\[
\begin{aligned}
&a^2-ac+a-b^2+bc-b,\\
&ab-ac-b^2-b+c^2+c,\\
&ac^2-ac-bc^2+bc,\\
&b^3-b,\\
&b^2c+b^2-bc^2+b-c^2-c,\\
&c^3-c.
\end{aligned}
\]
Its leading monomials are \(a^2,ab,ac^2,b^3,b^2c,c^3\). The nine standard monomials are
\[
1,c,c^2,b,bc,bc^2,b^2,a,ac.
\]
Therefore the affine singular scheme has total length exactly nine over the algebraic closure. Direct substitution exhibits nine distinct \(\mathbb F_3\)-points, in the order \((a,b,c)\):
\[
\begin{gathered}
(0,0,0),(0,0,2),(0,2,0),\\
(1,1,1),(1,1,2),(1,2,1),\\
(2,0,0),(2,1,1),(2,2,2).
\end{gathered}
\]
Thus it is a reduced nine-point scheme, with no additional points even over any extension field. These nine are precisely those among the fifteen displayed classes having \(z_0\ne0\). By the five-coordinate permutation symmetry, the fifteen displayed classes exhaust the global singular set and each is reduced.

**4. Node type and integrality.** The determinant of the \(3\times3\) Hessian of \(g\) is \(1\in\mathbb F_3\) at each of the nine listed affine points (the computation is reproduced by `CHECK.py`). Symmetry carries this nondegeneracy to every singular point of \(S\). Since the characteristic is not two, the formal Morse lemma identifies each local completed hypersurface with an ordinary quadratic double point. In particular, \(S\) has exactly fifteen \(A_1\) points.

An irreducible-component decomposition of a reduced quartic surface in \(\mathbb P^3\) would force components to meet along a curve, and a repeated component would give a two-dimensional singular locus. Since the singular set is finite, neither is possible. Hence \(S\) is geometrically integral. It is normal by the hypersurface \(S_2\) property and regularity in codimension one. Its projective cone \(B\) is therefore geometrically integral. The cone has singular locus only the fifteen ruling lines and the vertex, hence codimension two in the threefold; the hypersurface \(S_2\) property also proves normality of \(B\).

**5. Geometry along the cone.** Away from \(E\), projection to \(S\) is a Zariski-locally trivial affine-line bundle. Therefore the singular locus off \(E\) is the inverse image of the fifteen base nodes, i.e. fifteen disjoint punctured lines, with a transversal \(A_1\) analytic germ at every point. Their projective closures meet only at the common vertex. Since the cone equation is homogeneous of degree four in the four quotient coordinates, its multiplicity at \(E\) is exactly four.

## Verification

Run `python CHECK.py` with the dependency declared in `requirements.txt`. The exact computation verifies the symmetric-function translation identity in \(\mathbb F_3\), reconstructs the stated reduced Gröbner basis for \((g,g_a,g_b,g_c)\), counts its nine standard monomials, checks all nine rational solutions and their nonzero Hessian determinants, identifies the nine visible classes among the fifteen pairs, and verifies the number of distinct base classes. As an independent low-degree sanity check it counts \(76\) rational points on the projective cone over \(\mathbb F_3\). The argument covering all algebraic extension fields is the Gröbner-basis length argument plus permutation symmetry, **not** that finite-field enumeration.

## Relationship to prior work

The six-coordinate symmetric equation is classical: see the treatment of the Burkhardt and Igusa quartics by Cheltsov–Tschinkel–Zhang, equations (1.2) and (1.3), and the Burkhardt discussion in Artebani–Dolgachev. The characteristic-zero Burkhardt quartic has 45 isolated nodes. Bruin–Nasserden's arithmetic and birational results explicitly require characteristic different from three. The present claim instead concerns the special fibre of the specific integral six-coordinate symmetric equation and gives the complete geometry of its singular locus.

The five-coordinate model written by Bruin–Nasserden as \(y_0\sum_{i=0}^4y_i^3+3y_1y_2y_3y_4\) reduces in characteristic three to \(y_0(\sum_i y_i)^3\). Its highly reducible nonreduced fibre is **not** the normal cone described above, illustrating the need to specify the integral model. The characteristic-zero Igusa quartic also has fifteen singular lines, but it is a distinct quartic member of the symmetric pencil, and those lines are not this fifteen-line star.

The full text of the 1990 article by de Jong–Shepherd-Barron–Van de Ven could not be obtained for a decisive historical comparison. Accordingly, equivalent coverage in older algebraic or modular treatments remains a genuine originality uncertainty.

## Limitations

Only the reduced singular locus of the special fibre is determined. The possibly nonreduced embedded Jacobian structure at the common vertex, integral-model comparison by blowups, semistable models, zeta function of the nodal base, and any moduli-theoretic meaning at level three in characteristic three are not established. The normality claim is about the stated special fibre, not an assertion of good or stable reduction of the characteristic-zero threefold under all integral models.

## References

- M. Artebani and I. Dolgachev, *The Hesse pencil of plane cubic curves*, arXiv:math/0611590 (first submitted 19 November 2006), especially the discussion of the Burkhardt group and quartic in Section 4. https://arxiv.org/abs/math/0611590
- N. Bruin and B. Nasserden, *Arithmetic aspects of the Burkhardt quartic threefold*, arXiv:1705.09006 (submitted 25 May 2017), especially Sections 1–2 and 4–5. https://arxiv.org/abs/1705.09006
- I. Cheltsov, Y. Tschinkel and Z. Zhang, *Equivariant geometry of the Segre cubic and the Burkhardt quartic*, *Selecta Mathematica* 31 (2025), article 7, first published December 2024; equations (1.2), (1.3) and Section 7. https://doi.org/10.1007/s00029-024-01001-w
- A. J. de Jong, N. I. Shepherd-Barron and A. van de Ven, *On the Burkhardt quartic*, *Mathematische Annalen* 286 (1990), 309–328. https://doi.org/10.1007/BF01453578 (full text not obtained).
