# Parity-sharp critical counts for positive charts of Hirzebruch surfaces

## Finding
For each integer \(m\geq0\), set
\[
f_1(s,t)=1+s,\qquad f_2(s,t)=1+t+s^m t.
\]
These nonnegative-coefficient Laurent polynomials define, via the Calvo Cortes–Telen positive-chart construction, a positive Cox chart \(U_m\) of the smooth Hirzebruch surface \(\mathbb F_m\). The chart is isomorphic to \(\mathbb A^2_{\mathbb C}\). With its prescribed toric/Cox coordinate arrangement, the very affine locus \(U_m^\circ\) has integral homology
\[
H_j(U_m^\circ,\mathbb Z)\simeq
\begin{cases}
\mathbb Z,&j=0,\\
\mathbb Z^4,&j=1,\\
\mathbb Z^{4+r_m},&j=2,\\
0,&j\geq3,
\end{cases}
\qquad
r_m=\begin{cases}m,&m\text{ even},\\m-1,&m\text{ odd}.\end{cases}
\]
Consequently \(\chi(U_m^\circ)=r_m+1\). For a generic exponent vector \((a,b,c,d)\in\mathbb C^4\), the associated monomial/logarithmic master function on the very affine locus has exactly \(r_m+1\) isolated **nondegenerate** complex critical points, namely \(m+1\) for even \(m\) and \(m\) for odd \(m\). Thus the critical counts in increasing order \(m=0,1,2,3,\ldots\) are \(1,1,3,3,5,5,\ldots\), despite every ambient chart being an affine plane.

## Assumptions and scope
All schemes and topological spaces are over \(\mathbb C\), with classical complex topology used for homology. No statement about positive real critical points, arbitrary charts of \(\mathbb F_m\), or characteristic-\(p\) fibers is asserted. The exponent vector is generic in the Zariski-open sense; it is not restricted to integral exponents. The claim is about the **specified** Cox chart and its dense very affine locus, not the maximum-likelihood degree of the projectively embedded rational normal scroll.

For \(m=0\), the expression \(s^0\) means \(1\), so \(f_2=1+2t\). Put
\[
h_m(x)=x^m+(1-x)^m
\]
(with \(h_0=2\)). Here \(r_m=\deg h_m\); explicitly \(r_0=r_1=0\), \(r_m=m\) for even \(m\ge2\), and \(r_m=m-1\) for odd \(m\ge3\).

## Proof
**1. A valid positive chart on the correct toric surface.** The Newton polytopes of the two sections are the horizontal unit segment and, for \(m\ge1\), the triangle with vertices \((0,0),(0,1),(m,1)\) (for \(m=0\), the vertical unit segment). Their Minkowski sum is the lattice quadrilateral with vertices
\[
(0,0),\ (1,0),\ (m+1,1),\ (0,1).
\]
Its primitive inward normal rays, in cyclic order, are \((1,0),(0,1),(-1,m),(0,-1)\), defining the standard smooth fan of \(\mathbb F_m\). The associated divisor rows for the two summands are \((0,0,1,0)\) and \((0,0,0,1)\); the matrix in the positive-chart construction is
\[
M_m=\begin{pmatrix}
1&0&-1&0\\
0&1&m&-1\\
0&0&1&0\\
0&0&0&1
\end{pmatrix},\qquad\det M_m=1.
\]
The Newton sum has four facets, equal to \(d+k=2+2\), and all polynomial coefficients are nonnegative. Hence Assumptions 1 and 2 of Calvo Cortes–Telen and their Theorem 3.9 apply: these equations yield a positive Cox chart of \(\mathbb F_m\).

**2. The chart is an affine plane.** Write the Cox coordinates as \((u_1,u_2,u_3,u_4)\). The unimodular monomial change of variables sends
\[
(s,t,f_1^{-1},f_2^{-1})
\longmapsto
\left(\frac{s}{f_1},\frac{t f_1^m}{f_2},\frac1{f_1},\frac1{f_2}\right).
\]
The Cox homogenizations are exactly
\[
f_1^h=u_1+u_3,\qquad f_2^h=u_4+u_2(u_3^m+u_1^m).
\]
The dense-torus image therefore satisfies
\[
u_3=1-u_1,\qquad u_4=1-u_2\bigl((1-u_1)^m+u_1^m\bigr).
\]
Conversely, in the closed affine surface given by these two equations, the open locus on which \(u_1u_2u_3u_4\ne0\) is isomorphic to \(\{(s,t)\in(\mathbb C^*)^2:f_1f_2\ne0\}\), by the inverse monomial substitution \(s=u_1/u_3\), \(t=u_2u_3^m/u_4\). It is dense in the graph surface, so the closure is exactly the graph. Thus \(U_m\simeq\mathbb A^2\) with coordinates \(x=u_1\), \(y=u_2\), and
\[
U_m^\circ\simeq\{(x,y)\in\mathbb C^2:x(1-x)y(1-yh_m(x))\ne0\}. \tag{1}
\]
This argument verifies the needed ideal directly; it does not presume saturation from a proposed general statement.

**3. Distinct roots and the topology of the divisor.** If \(m\ge1\), zeros of \(h_m\) correspond under \(z=x/(1-x)\) to solutions of \(z^m=-1\), except that \(z=-1\) corresponds to no finite \(x\). For even \(m\), \(-1\) is not among these roots, yielding \(m\) distinct finite roots. For odd \(m\), it is among them and is omitted, yielding \(m-1\) distinct finite roots. The cases \(m=0,1\) are constant. Furthermore \(h_m(0)=h_m(1)=1\) for \(m\ge1\), and both values equal \(2\) when \(m=0\).

Let \(D\subset\mathbb A^2\) be the union of the four zero loci in (1). Three components are the lines \(x=0\), \(x=1\), \(y=0\); the fourth is the smooth curve \(1-yh_m(x)=0\), isomorphic to \(\mathbb A^1\) minus precisely \(r_m\) points. Exactly four distinct transverse pairwise nodes occur: the two vertical lines each meet \(y=0\) and each meet the fourth curve at \(y=1/h_m(0)\) or \(1/h_m(1)\). There are no other intersections or triple points.

Using Mayer–Vietoris for **compactly supported cohomology** of this union gives
\[
H_c^0(D;\mathbb Z)=0,\quad H_c^1(D;\mathbb Z)\simeq\mathbb Z^{r_m+4},\quad H_c^2(D;\mathbb Z)\simeq\mathbb Z^4.
\]
Indeed, the individual noncompact irreducible curves contribute \(r_m\) classes to compactly supported degree-one cohomology, while gluing them at four nodes contributes four more; their four fundamental classes give degree two. The groups are free since the relevant exact sequences extend free abelian groups by free abelian groups. Alexander duality in the one-point compactification \(\mathbb C^2\cup\{\infty\}=S^4\) gives, for \(j\ge1\),
\[
\widetilde H_j(\mathbb C^2\setminus D;\mathbb Z)\simeq H_c^{3-j}(D;\mathbb Z).
\]
The complement is connected because it is the complement of a complex curve in \(\mathbb C^2\). This proves all the homology groups and the stated Euler characteristic, including \(m=0\).

**4. Exact generic critical count.** On (1), a generic Cox monomial pulls back to the logarithmic multivalued master function
\[
L(x,y)=x^a y^b(1-x)^c(1-yh_m(x))^d.
\]
Its critical locus is well-defined by the vanishing of its logarithmic differential. With \(bd(b+d)\ne0\), the \(y\)-equation uniquely gives
\[
y=\frac{b}{(b+d)h_m(x)},\qquad 1-yh_m(x)=\frac{d}{b+d}.
\]
The remaining \(x\)-equation reduces to the **single polynomial**
\[
R_m(x)=a(1-x)h_m(x)-cxh_m(x)-bx(1-x)h_m'(x)=0.
\]
For generic \((a,b,c)\), this polynomial has degree exactly \(r_m+1\). It is generically squarefree: to see that its discriminant is not identically zero, specialize \(b=0\), choose \(a+c\ne0\), and arrange for the root of \(a-(a+c)x\) to be disjoint from the \(r_m\) distinct roots of \(h_m\). Then the specialized polynomial is squarefree; the property persists for generic nonzero \(b\). For such parameters, \(R_m(0)=a h_m(0)\ne0\), \(R_m(1)=-c h_m(1)\ne0\), and at a zero \(\xi\) of \(h_m\) we have \(R_m(\xi)=-b\xi(1-\xi)h_m'(\xi)\ne0\). Therefore all \(r_m+1\) roots lie in (1) and lift to distinct critical points. Since the derivative of the eliminated \(y\)-equation is nonzero when \(bd(b+d)h_m(x)\ne0\), squarefree roots of \(R_m\) yield nondegenerate critical points. Hence the exact critical count is \(r_m+1\), also agreeing with the signed-Euler characteristic theorem for very affine varieties.

## Verification
Run `python verify.py` (standard-library Python). The script recomputes the polynomial \(h_m\), its degree and squarefreeness, the relevant excluded-root tests and generic critical polynomial degree/squarefreeness over \(\mathbb Q\) for \(0\le m\le12\). It returns `FINITE_EXACT_CHECKS_PASS`. These are finite consistency checks; the unrestricted statements for all nonnegative integers \(m\) follow from the algebraic and topological arguments above, not the enumeration.

## Relationship to prior work
Calvo Cortes and Telen establish existence and Cox properties of positive charts of smooth projective toric varieties (Theorem 3.9) and relate scattering-equation solution numbers to the signed Euler characteristic (Section 5). Their Example 3.6 is the product-surface construction \(\mathbb P^1\times\mathbb P^1\); their multi-polynomial running example includes some related trinomial sections. The explicit Hirzebruch family, affine-plane presentation for every \(m\), integral homology profile and critical-count parity law above are not stated in the inspected relevant sections. The general Huh theorem supplies the signed-Euler interpretation, but not the evaluation of the invariant for this family.

Améndola and collaborators' Theorem 17 and Example 19 compute maximum-likelihood degrees for projectively embedded rational normal scrolls and Hirzebruch surfaces using a **single normalization polynomial** of the monomial embedding. Their formula uses scroll embedding parameters and gcds of polynomial degrees, not the four-coordinate Cox complement (1) with two separate Laurent sections. No equality of the two models is assumed or asserted.

## Limitations
The results concern the specific nonnegative-coefficient Laurent-polynomial choice, not all positive charts of \(\mathbb F_m\); changing coefficients can change the punctures and critical count. The generic complex critical points do not represent counts of real or positive critical points. The exact cohomology computation uses the complex topology of the complement. Known general machinery (Cox coordinate constructions, Alexander duality and signed Euler characteristics) is essential; the claimed contribution is the explicit family and its sharp integral topology and parity, not those general tools. There remains bibliographic risk from equivalent computations hidden in other treatments of two-polynomial complements or specific toric chart examples.

## References
1. V. Calvo Cortes and S. Telen, *Positive Charts of Toric Varieties*, arXiv:2602.16414, submitted 18 February 2026, revised 3 June 2026, Sections 3 and 5. https://arxiv.org/abs/2602.16414
2. C. Améndola, N. Bliss, I. Burke, C. R. Gibbons, M. Helmer, S. Hoşten, E. D. Nash, J. I. Rodriguez, D. Smolkin, *The Maximum Likelihood Degree of Toric Varieties*, arXiv:1703.02251, Section 4, Theorem 17 and Example 19. https://arxiv.org/abs/1703.02251
3. J. Huh, *The maximum likelihood degree of a very affine variety*, Compositio Mathematica 149 (2013), 1245–1266; arXiv:1207.0553. https://arxiv.org/abs/1207.0553
