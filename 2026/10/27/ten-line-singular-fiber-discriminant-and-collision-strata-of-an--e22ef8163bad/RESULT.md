# Ten-line singular-fiber discriminant and collision strata of an explicit quartic del Pezzo fibration

## Finding
For the smooth Fano fourfold of Gao's Example 7.12, the locus in the base over which the quartic del Pezzo fiber is singular is a ten-line arrangement carrying the Desargues \((10_3)\) incidence configuration. It has exactly ten triple intersections and fifteen ordinary double intersections. Fibers over the generic points of the ten lines have two ordinary nodes, fibers over the fifteen double intersections have four nodes, and fibers over the ten triple intersections split into two smooth quadric surfaces meeting along a smooth conic. A general base line therefore has ten singular fibers but twenty nodes. The smooth total fourfold has topological Euler characteristic \(24\). The binary-quintic discriminant of the defining quadric pencil is the square of the reduced ten-line equation, up to a nonzero scalar.

## Assumptions and scope
Work over \(\mathbb C\). Let \([x_0:x_1:x_2]\) and \([y_0:\cdots:y_4]\) denote homogeneous coordinates on \(\mathbb P^2\) and \(\mathbb P^4\), respectively. Define \(s=x_0+x_1+x_2\). Let \(X\) be the following smooth fourfold (smoothness is also established in Gao, Example 7.12):
\[
X=\left\{y_0^2+y_1^2+y_2^2+y_3^2-y_4^2=0,\quad
x_0y_0^2+x_1y_1^2+x_2y_2^2-sy_3^2=0\right\}
\subset\mathbb P^2\times\mathbb P^4.
\]
Write \(\pi:X\to\mathbb P^2\) for the first projection and define five linear forms
\[
(t_0,t_1,t_2,t_3,t_4)=(x_0,x_1,x_2,-s,0).
\]
For each unordered pair \(\{i,j\}\subset\{0,1,2,3,4\}\) with \(i\ne j\), put \(L_{ij}=\{t_i=t_j\}\subset\mathbb P^2\). Statements about singularities are statements about the scheme-theoretic geometric fiber, not about singularities of the smooth total space. The binary-quintic discriminant below is the discriminant of the determinant of the fiber's *pencil of quadrics*; it must not be confused with the four-line branch divisor of the different ruling-parameter double cover studied in the source paper.

## Proof
**1. Singularities occur precisely at repeated eigenvalues.** Over \(\mathbb C\), set \(z_j=y_j\) for \(0\le j\le3\) and \(z_4=\sqrt{-1}\,y_4\). The fiber \(F_x=\pi^{-1}(x)\subset\mathbb P^4\) is defined by
\[
Q_0=\sum_{i=0}^{4}z_i^2=0,\qquad Q_1=\sum_{i=0}^{4}t_i(x)z_i^2=0.
\]
Its Jacobian has rows \((2z_i)_i\) and \((2t_i z_i)_i\). Since the first row cannot vanish at a projective point, the rank drops precisely when every nonzero coordinate \(z_i\) has the same value of \(t_i(x)\). For a block \(B\) of \(m\ge2\) equal eigenvalues, the corresponding singular subscheme is the smooth quadric
\[
\left\{\sum_{i\in B}z_i^2=0\right\}\subset\mathbb P^{m-1},
\]
of dimension \(m-2\); singleton blocks contribute nothing. Conversely, every point on this quadric is singular. Consequently the fiber is smooth if and only if all five eigenvalues are distinct. The five forms are distinct pairwise as linear forms, so the reduced singular-fiber locus is exactly \(D=\bigcup_{0\le i<j\le4}L_{ij}\), a union of ten distinct lines.

The binary quintic \(\det(uQ_0+vQ_1)=\prod_{i=0}^{4}(u+v t_i)\) has root-collision discriminant
\[
\operatorname{Disc}_{u,v}(\det(uQ_0+vQ_1))=c\prod_{0\le i<j\le4}(t_i-t_j)^2,\qquad c\in\mathbb C^\times.
\]
Thus this pencil-discriminant divisor is twice the reduced ten-line arrangement; this does not assert an identification with other possible discriminant scheme conventions.

**2. The exact intersection lattice.** Any intersection of two distinct equality lines corresponds either to three equal eigenvalues (the pair equalities share an index) or to two disjoint pairs of equal eigenvalues. There are \(\binom53=10\) putative triple blocks. If the triple includes index \(4\), then three forms vanish and the remaining two are opposite nonzero values; if it does not, three of the first four forms equal \(a\ne0\), the fourth equals \(-3a\), and the fifth is zero. Each case determines a unique projective parameter and has precisely multiplicity partition \((3,1,1)\). These ten points are distinct and each lies on exactly three of the equality lines.

There are \(5\cdot3=15\) choices of two disjoint unordered pairs among five labels. If the singleton is index \(4\), the pair values are \(a,-a\) and the singleton value is zero. Otherwise, one pair contains index \(4\) and has value zero, the other pair has value \(a\), and the singleton value is \(-2a\). Each choice determines one projective point with multiplicity partition \((2,2,1)\); the fifteen points are distinct and lie on exactly two equality lines. A partition with a block of size four, or of sizes \((3,2)\), would force all five eigenvalues to vanish using \(t_0+t_1+t_2+t_3=t_4=0\), which is impossible on \(\mathbb P^2\). Therefore these are all line intersections. In particular, each of the ten lines contains three triple and three ordinary double intersection points. The incidence of a pair-labelled line with a triple-labelled point is exactly inclusion of the pair in the triple, giving the Desargues \((10_3)\) incidence pattern.

**3. Analytic geometry of the fibers.** At a parameter where exactly two eigenvalues equal \(a\), the singular locus from Step 1 is the quadric \(z_i^2+z_j^2=0\) in \(\mathbb P^1\), hence two points. Near either point, the gradient of \(Q_0\) is nonzero and eliminating one variable with \(Q_0\) gives the transverse hypersurface quadratic form
\[
\sum_{k\notin\{i,j\}}(t_k-a)u_k^2
\]
in three local variables, up to invertible coordinate changes and nonzero factors. Every coefficient is nonzero, so the germ is an ordinary surface node of type \(A_1\). The fiber is a reduced complete intersection with isolated singularities and hence is normal; connectedness of a positive-dimensional complete intersection and normality imply it is irreducible. The same argument applies to the two separate blocks at a \((2,2,1)\) parameter: two nodes arise from each pair, giving precisely four \(A_1\) singularities, with no other singular points.

At a \((3,1,1)\) parameter let \(a\) be the repeated eigenvalue, and \(b,c\) the two distinct remaining eigenvalues. If \(z_j,z_k\) are their respective coordinates, then
\[
Q_1-aQ_0=(b-a)z_j^2+(c-a)z_k^2
\]
factors as two distinct linear forms over \(\mathbb C\). Each corresponding hyperplane intersects \(Q_0\) in a smooth quadric surface in \(\mathbb P^3\): the restriction of \(Q_0\) to its four coordinate directions has rank four because \(b\ne c\). Their scheme-theoretic intersection is \(z_j=z_k=0\) together with \(\sum_{i\in B}z_i^2=0\), a smooth conic, and the two components meet transversely along it. The singular locus of this reducible fiber is exactly that conic.

**4. A general pencil in the base.** A general projective line \(\ell\subset\mathbb P^2\) avoids all twenty-five line-intersection points and crosses each of the ten distinct lines \(L_{ij}\) once. Hence \(\pi^{-1}(\ell)\to\ell\) has precisely ten singular fibers, each with two ordinary nodes, or twenty nodes counted individually. This is a special collision of critical values, distinct from the general-family statement about twenty one-node fibers for deformation type No. 2-7.

**5. Euler characteristic and an independent Chern calculation.** A smooth degree-four del Pezzo surface is the blow-up of \(\mathbb P^2\) at five points, so it has Euler characteristic \(8\). Each node decreases the Euler characteristic of the singular fiber by one relative to a smoothing, so the two-node and four-node fibers have Euler characteristics \(6\) and \(4\). Two smooth quadric surfaces glued transversely along a smooth conic have Euler characteristic \(4+4-2=6\).

The reduced ten-line union \(D\) has Euler characteristic \(10(2)-10(3-1)-15(2-1)=-15\). Thus \(e(\mathbb P^2\setminus D)=18\) and the open part of the lines with the twenty-five intersections deleted has Euler characteristic \(-40\). Additivity of Euler characteristic for the proper stratified map gives
\[
e(X)=8(18)+6(-40)+6(10)+4(15)=24.
\]
Independently, with \(h\) and \(g\) the hyperplane classes from \(\mathbb P^2\) and \(\mathbb P^4\), the normal bundle classes have bidegrees \((0,2)\) and \((1,2)\). Therefore
\[
c(T_X)=\frac{(1+h)^3(1+g)^5}{(1+2g)(1+h+2g)},\quad
c_4(T_X)=5g^4+4hg^3+4h^2g^2,
\]
and \(\int_X c_4=[h^2g^4]\bigl(2g(h+2g)c_4\bigr)=24\), using \(h^3=g^5=0\). This is an independent consistency check.

## Verification
Run \(\texttt{python3 verify\_fano\_fibers.py}\) (Python standard library only). The checker enumerates all ten equality lines as primitive integer vectors, their distinct projective intersections, every eigenvalue multiplicity partition and line incidence, and exactly computes the fourth Chern class and two versions of the total Euler characteristic. Expected output:

```
VERIFY_OK lines=10 triple_points=10 double_pair_points=15 singular_base_points=25
VERIFY_OK generic_line_fibers=10 each_two_A1 total_nodes=20
VERIFY_OK c4=5g4+4hg3+4h2g2 euler_from_Chern=24 euler_from_fibers=24
```
The infinite/complex-geometric assertions are proved in the preceding Jacobian and local normal-form arguments; the finite checker independently checks the combinatorial and Chern computations, not an infinite theorem by sampling.

## Relationship to prior work
Gao, *The geometric exceptional set for Fano threefolds*, arXiv:2610.23024v1, Examples 7.10 and 7.12, constructs this smooth Fano fourfold and proves that its arithmetic exceptional set is Zariski dense. The four-line branch arrangement \(x_0x_1x_2(x_0+x_1+x_2)=0\) there parametrizes rulings of the diagonal net: it is not the ten-line locus of singular quartic del Pezzo fibers computed here. Gao's Proposition 6.2 and Table 1 give twenty nodal singular fibers for a general member of deformation family No. 2-7; the special line sections of this explicit diagonal fourfold instead have ten distinct singular values carrying two nodes each.

The classical theory of intersections of two quadrics supplies the underlying Jacobian/eigenvalue method, so the result is not a new general singularity-classification theorem. Its new scope is the **complete exact boundary stratification of the particular explicit Fano fibration**, including reducible fibers and all twenty-five multiple intersections. Available relevant mathematical-record searches did not identify this exact profile, although undiscovered or implicit prior computations remain possible.

## Limitations
The field is \(\mathbb C\) (the arguments also work in suitable characteristic different from \(2,3,5\) after excluding degeneracies, but no such generality is claimed). The discriminant is explicitly the binary-quintic discriminant of the quadric pencil; other scheme structures on the morphism's critical-value locus are not classified. The theorem concerns Gao's specified diagonal fibration, not arbitrary quartic del Pezzo fibrations or arbitrary members of the family. Historic priority is not independently certified, and abstract-only comparisons cannot rule out every earlier implicit calculation. No claims about derived categories, arithmetic density beyond Gao's theorem, or independent auditing are made.

## References
- Runxuan Gao, *The geometric exceptional set for Fano threefolds*, arXiv:2610.23024v1 (first public version, 16 October 2026), especially Examples 7.10 and 7.12, Proposition 6.2 and Table 1; https://arxiv.org/html/2610.23024v1.
- Alexei N. Skorobogatov, *Del Pezzo surfaces of degree 4 and their relation to Kummer surfaces*, Enseign. Math. 56 (2010), 73--85; DOI 10.4171/LEM/56-1-3. Background on degree-four del Pezzo surfaces (abstract consulted).
- Igor V. Dolgachev, *Classical Algebraic Geometry: A Modern View*, discussion of intersections of quadrics and binary pencil discriminants. Background only; not used as an originality certificate.
