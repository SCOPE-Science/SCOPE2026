# A degree-eight nearly free conic-line arrangement over a quadratic field
## Finding
Let \(s=\sqrt5\) and \(r=9+4s\). Define the smooth conic
\[
Q=(7-3s)x^2-4xy-2(3-s)xz+(7+3s)y^2-2(3+s)yz+2z^2
\]
and the reduced degree-eight curve
\[
\mathcal A:\quad F=Q\,xyz(y-z)(x-z)(x-r y)=0.
\]
Then \(\mathcal A\) is a nearly free conic-line arrangement with exponents \((4,4)\). Its singularities are exactly three nodes, three tacnodes, and six ordinary triple points. In particular, its total Tjurina number is \(36\), and \(\operatorname{mdr}(F)=4\).

This gives an explicit positive answer to the degree-eight existence case left open in Gałecka's classification of nearly free conic-line arrangements having only nodes, tacnodes, and ordinary triple points.

## Assumptions and scope
Everything is over \(\mathbb C\). The displayed arrangement is defined over the quadratic field \(\mathbb Q(\sqrt5)\). The six line components are
\[
x=0,\quad y=0,\quad z=0,\quad y-z=0,\quad x-z=0,\quad x-r y=0.
\]
The claim is only the explicit existence and verification of this degree-eight nearly free arrangement. It does not classify all degree-eight arrangements and does not address the remaining degree-nine existence question.

## Proof
Put
\[
u=\frac{3-\sqrt5}2,\qquad v=\frac{3+\sqrt5}2.
\]
Then \(uv=1\), \(r=v^3\), and \(r^2-18r+1=0\). Before adjoining the conic, the six lines have three ordinary triple points
\[
[1:0:0],\quad[0:1:0],\quad[0:0:1]
\]
and six ordinary double points
\[
[0:1:1],\ [1:0:1],\ [r:1:0],\ [1:1:1],\ [r:1:1],\ [r:1:r].
\]
No further line triple occurs because \(r\ne1\).

The conic is obtained by requiring tangency to the three coordinate lines and passage through the three pairwise intersections of the noncoordinate lines. A conic tangent to the coordinate lines can be written, after scaling, as
\[
u^2x^2+v^2y^2+w^2z^2-2uvxy-2uwxz-2vwyz=0.
\]
Taking \(w=1\) and imposing passage through \([1:1:1]\), \([r:1:1]\), and \([r:1:r]\) gives
\[
u=\frac{r+3}{3r+1},\qquad v=\frac{(r-1)^2}{2(3r+1)}
\]
and the remaining compatibility equation
\[
(r-1)^2(r^2-18r+1)=0.
\]
Choosing \(r=9+4\sqrt5\) yields the displayed \(u\), \(v\), and \(Q\) (scaled by \(2\)). The symmetric matrix of \(Q\) has determinant \(-32\), so the conic is smooth.

The restrictions to the coordinate lines are
\[
Q|_{x=0}=2(vy-z)^2,\qquad Q|_{y=0}=2(ux-z)^2,\qquad Q|_{z=0}=2(ux-vy)^2.
\]
Thus these three lines are tangent to the conic at three distinct smooth points, none of which is a singular point of the six-line arrangement. They give exactly three tacnodes. The conic also passes through \([1:1:1]\), \([r:1:1]\), and \([r:1:r]\). Each of the three noncoordinate lines meets the conic in two distinct points from this set, so every such intersection is transverse; the three points therefore become ordinary triple points consisting of two line branches and one conic branch. The conic avoids the other six singular points of the line arrangement. Bézout accounts for all line-conic intersections, hence there are no additional singularities. Consequently
\[
(n_2,t,n_3)=(3,3,6),\qquad \tau(\mathcal A)=3+3\cdot3+4\cdot6=36.
\]

For a conic-line arrangement of degree \(m\) having only these singularities, Gałecka's Proposition 4.1 gives
\[
\operatorname{mdr}(F)\ge\frac23m-2.
\]
At \(m=8\), integrality gives \(\operatorname{mdr}(F)\ge4\). Independently, exact arithmetic over \(\mathbb Q(\sqrt5)\) applied to the degree-four map
\[
S_4^3\longrightarrow S_{11},\qquad (A,B,C)\longmapsto AF_x+BF_y+CF_z
\]
produces a \(78\times45\) coefficient matrix of rank \(42\). Its kernel therefore has dimension \(3\), so a nonzero degree-four Jacobian relation exists and \(\operatorname{mdr}(F)\le4\). Hence \(\operatorname{mdr}(F)=4\).

Gałecka's Theorem 3.2 recalls the criterion that a conic-line arrangement of degree \(m\) is nearly free exactly when
\[
r^2-r(m-1)+(m-1)^2=\tau+1,
\]
where \(r=\operatorname{mdr}(F)\). Here
\[
4^2-4\cdot7+7^2=37=36+1,
\]
so \(\mathcal A\) is nearly free. Since the exponents of a nearly free degree-eight curve sum to \(8\) and the smaller exponent is \(4\), they are \((4,4)\).

## Verification
The accompanying exact-arithmetic verifier works in \(\mathbb Q(\sqrt5)\) using only rational pairs. It reconstructs \(F\), checks the conic determinant and the three perfect-square restrictions, checks the conic incidences and avoidances used in the singularity census, constructs the full degree-four Jacobian-syzygy matrix, and row-reduces it exactly to rank \(42\). It also checks the Tjurina arithmetic and the near-freeness numerical identity.

The replay establishes the finite algebraic computations used above. The lower bound on \(\operatorname{mdr}(F)\) and the numerical near-freeness criterion are imported from the cited literature, not reproved by the script.

## Relationship to prior work
Gałecka constructs examples in degrees \(3,4,5,6,7\), proves nonexistence in degrees \(10,11,12\), and explicitly states that existence remains to be decided in degrees \(8\) and \(9\). The present arrangement resolves the degree-eight existence part by an explicit example with weak combinatorics \((n_2,t,n_3)=(3,3,6)\).

Later work on constructing free curves by adjoining special lines treats broader free-curve constructions and gives degree-eight maximizing examples with different singularity types; it does not supply this degree-eight nearly free conic-line arrangement with only nodes, tacnodes, and ordinary triple points. Recent work on plus-one generated conic arrangements likewise studies a different component class and different classification problem. Targeted searches for the exact degree, singularity vector, and quadratic parameter relation did not locate a published equivalent construction.

## Limitations
The originality comparison is literature-search based rather than a mathematical proof of uniqueness. No claim is made that the displayed arrangement is the only degree-eight example, that its weak combinatorics determine near freeness, or that degree nine is settled. The exact rank computation proves existence of degree-four syzygies; the exclusion of smaller syzygies relies on the published general lower bound.

## References
1. Aleksandra Gałecka, “On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points,” arXiv:2204.13969v1, first public 29 April 2022; Boletín de la Sociedad Matemática Mexicana 28 (2022), Article 67, DOI 10.1007/s40590-022-00461-4.
2. Alexandru Dimca, Giovanna Ilardi, Piotr Pokora, and Gabriel Sticlaru, “Construction of Free Curves by Adding Lines to a Given Curve,” Results in Mathematics 79 (2024), Article 11, DOI 10.1007/s00025-023-02036-9.
3. Artur Bromboszcz, Bartosz Jarosławski, and Piotr Pokora, “On plus-one generated arrangements of plane conics,” Geometriae Dedicata 220 (2026), Article 10, DOI 10.1007/s10711-025-01063-w.
