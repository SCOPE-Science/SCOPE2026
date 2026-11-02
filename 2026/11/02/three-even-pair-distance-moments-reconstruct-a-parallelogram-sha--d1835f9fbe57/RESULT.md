# Three even pair-distance moments reconstruct a parallelogram, sharply

## Finding
Let \(P\subset\mathbb R^2\) be any nondegenerate Euclidean parallelogram. Choose \(X,Y\) independently and uniformly with respect to normalized planar area measure on \(P\), and put \(D=\|X-Y\|_2\). The three numbers
\[
m_1=\mathbb E D^2,\qquad m_2=\mathbb E D^4,\qquad m_3=\mathbb E D^6
\]
determine \(P\) up to Euclidean isometry. There is an explicit rational reconstruction of its unordered pair of squared side lengths, the absolute cosine of its edge-line angle, and its area. The first two of these moments do *not* determine all nondegenerate parallelograms: there are even continuous families of noncongruent parallelograms with the same first two moments.

More precisely, define
\[
\begin{aligned}
s&=6m_1,\\
U&=m_2-\frac{s^2}{15},\\
V&=\frac{m_3}{s}-\frac{s^2}{28},\\
p&=\frac{-2520U+2100V}{41},\\
q&=\frac{-5580U+5880V}{41}.
\end{aligned}
\]
A real triple \((m_1,m_2,m_3)\) arises from **some** nondegenerate planar parallelogram if and only if
\[
\boxed{s>0,\quad 0<p\le\frac{s^2}{4},\quad 0\le q<4p.}
\]
For such a triple, the squared side lengths are precisely the roots of
\[
\boxed{z^2-sz+p=0,}
\]
and, writing \(\varphi\in(0,\pi/2]\) for the acute angle between the *unoriented* edge lines,
\[
\boxed{\cos\varphi=\sqrt{\frac{q}{4p}},\qquad \operatorname{Area}(P)=\sqrt{p-\frac q4}.}
\]
These formulas also cover all rectangles, rhombi, and squares, without exceptional cases.

## Assumptions and scope
Here "parallelogram" means a compact convex body equal to a translate of \(\{tu+rv:0\le t,r\le1\}\), where \(u,v\in\mathbb R^2\) are nonzero and linearly independent. No coordinates, orientations, vertex labels, or prior knowledge of the area or side lengths are provided. The points \(X,Y\) are sampled independently *with replacement* by normalized two-dimensional Lebesgue area, not by boundary arclength or a random-line chord convention. Euclidean congruence includes translations and reflections; the unoriented line angle identifies obtuse and supplementary acute generating angles that describe the same translated parallelogram. All displayed moments are population expectations rather than estimates from a finite sample.

## Proof
**Step 1 (difference coordinates).** Translation is irrelevant, so use \(P=\{tu+rv:0\le t,r\le1\}\). For four independent \(\operatorname{Unif}[0,1]\) variables \(T_1,T_2,R_1,R_2\), one has
\[
X-Y=(T_1-T_2)u+(R_1-R_2)v.
\]
Put \(\xi=T_1-T_2\), \(\eta=R_1-R_2\). These are independent, symmetric, triangular variables on \([-1,1]\) with density \(1-|x|\). Direct integration gives, for every integer \(j\ge0\),
\[
\mathbb E\xi^{2j}=\mathbb E\eta^{2j}=\frac{2}{(2j+1)(2j+2)},
\qquad \mathbb E\xi^{2j+1}=\mathbb E\eta^{2j+1}=0.
\]
In particular the second, fourth, and sixth moments are \(1/6,1/15,1/28\).

**Step 2 (the three moment equations).** Set
\[
A=\|u\|^2>0,\qquad B=\|v\|^2>0,\qquad C=2\langle u,v\rangle,
\quad s=A+B,\ p=AB,\ q=C^2.
\]
Linear independence is exactly \(q<4p\). With \(Z=D^2=A\xi^2+B\eta^2+C\xi\eta\), independence and vanishing odd moments yield
\[
\begin{aligned}
\mathbb EZ&=\frac{s}{6},\\
\mathbb EZ^2&=\frac{s^2}{15}-\frac{7p}{90}+\frac q{36},\\
\mathbb EZ^3&=\frac{s^3}{28}-\frac{31sp}{420}+\frac{sq}{30}.
\end{aligned}\tag{1}
\]
To check the cubic line directly, the term without \(C\) contributes \((A^3+B^3)/28+AB(A+B)/30\), the terms with exactly two factors \(C\xi\eta\) contribute \(C^2(A+B)/30\), and terms with an odd number of those factors integrate to zero. Since \(A^3+B^3=s^3-3sp\), equation (1) follows.

The last two equations of (1), after subtracting their pure-\(s\) contributions and dividing the third by \(s\), form the linear system
\[
\begin{pmatrix}U\\V\end{pmatrix}
=\begin{pmatrix}-7/90&1/36\\-31/420&1/30\end{pmatrix}
\begin{pmatrix}p\\q\end{pmatrix}.
\]
The determinant is exactly \(-41/75600\ne0\). Inverting gives the stated formulas for \(p,q\), with \(s=6m_1\). Thus the moments uniquely recover the unordered pair \(\{A,B\}\) as roots of \(z^2-sz+p\), and also \(C^2=q\).

**Step 3 (congruence and exact feasibility).** Nondegeneracy implies \(s>0\), \(0<p\le s^2/4\) by arithmetic-geometric mean, and \(0\le q<4p\) by the strict Gram determinant. Conversely, suppose these three inequalities hold. The two roots \(A,B\) are positive, and the symmetric matrix
\[
G=\begin{pmatrix}A&\sqrt q/2\\\sqrt q/2&B\end{pmatrix}
\]
is strictly positive definite because its determinant is \(p-q/4>0\). Hence it is the Gram matrix of some independent planar vectors \(u,v\); their parallelogram produces exactly (1), so every admissible triple is realized. The Gram matrix fixes the Euclidean configuration up to an orthogonal transformation. Swapping \(u,v\) or replacing one generator by its negative changes neither the translated parallelogram's congruence class nor the recovered angle between unoriented edge lines. Therefore the reconstruction is unique up to Euclidean isometry. The area is \(\sqrt{\det G}\), and the acute edge-line cosine is \(\sqrt q/(2\sqrt p)\).

**Step 4 (two moments are insufficient).** Let two parallelograms have squared side lengths respectively
\[
(A_1,B_1)=(3/2,1/2),\qquad (A_2,B_2)=(7/5,3/5),
\]
and squared twice-inner-products respectively \(q_1=1\), \(q_2=313/250\). Both Gram matrices are positive definite. Formula (1) gives
\[
(m_{1,1},m_{2,1})=(m_{1,2},m_{2,2})=(1/3,17/72),
\]
but their squared areas are \(1/2\) and \(527/1000\), so they are not congruent. Their sixth-distance moments, \(29/120\) and \(3218/13125\), separate them. More generally, at any strictly interior parameter point \(s>0\), \(0<p<s^2/4\), \(0<q<4p\), keeping \(s\) fixed while changing \(p\) a little and setting \(q'=q+(14/5)(p'-p)\) preserves both first moments but changes the shape. Thus two moments fail on open families, proving the cutoff at three is sharp for universal reconstruction.

## Verification
The standalone standard-library script `check_distance_moments.py` independently expands \(\|u(T_1-T_2)+v(R_1-R_2)\|^{2j}\) in the **four original independent uniform coordinates** and integrates each monomial over \([0,1]^4\), without invoking the triangular-difference calculation used in the proof. It compares those exact rational integrals with equation (1), and performs the inverse reconstruction, across 62 distinct admissible rational Gram triples. It also verifies both sharpness examples and their areas using rational arithmetic. Run `python3 check_distance_moments.py`; success messages begin with `PASS:`. This is a finite algebraic cross-check, not a substitute for the universally quantified proof above.

## Relationship to prior work
Sheng (1985) gave an elementary-function expression for **every integer-order distance moment of two independent points in an arbitrary parallelogram**, and so the *forward evaluation* of the three moments above is established prior art [7]. The new claim here is specifically the **inverse** direction: that the first three even moments, without labeled axes or other data, determine the congruence class, together with the exact feasible moment-triple region and an explicit two-moment collision proving optimality of three. These are not statements in Sheng's accessible abstract, but his full paper was not available for inspection, and may contain closely related inverse consequences. The current formulas and proof are presented independently, not as a claim of priority for forward distance moments.

Tong, Ahmadi, and Pan (first public preprint 2013-11-29) developed exact two-point distance distributions via triangle chord distributions and treated a special rhombus built from two congruent triangles [1]. Mathai, Moschopoulos, and Pederzoli computed arbitrary moments for the cube and square [2]. Gates proved that triangles and quadrilaterals can be recognized using *complete* chord-distribution information, specifically a derivative of its density for quadrilaterals [3]. These give related geometric-probability and recognition tools but do not in their accessible statements supply a three-even-moment reconstruction and a sharp two-moment failure result for every nonorthogonal parallelogram.

Pure, Durrani, Tong, and Pan gave a general method to determine two-point distance PDFs for arbitrary polygons [4]. This broader forward-distribution method is acknowledged: in principle it permits moment calculations after integration, but does not itself imply uniqueness from only the first three even moments or a sharp minimality bound. Published findings on Haar-random widths of parallelograms and on fourth-power boundary/interior chord amplification likewise use different measurements [5,6]. The present statement is a *finite-moment inverse theorem*, not a claim that square, rhombus, or arbitrary-polygon distance distributions were previously unknown.

## Limitations
The theorem treats nondegenerate planar parallelograms, not all convex quadrilaterals. The inverse is based on exact population moments, and near equal side lengths the root discriminant creates square-root sensitivity; no uniform noise-robustness claim is made. Recognition via a full chord-length distribution and arbitrary-polygon forward formulas are established prior art. Some older full texts, notably Gates [3] and Sheng [7], and part of the preprint [1], were not accessible for a complete comparison, so historical priority remains provisional. Sheng already established all forward integer-order parallelogram distance moments; the inversion is elementary once the low-order equations are known, and the possibility that its sharp inverse content was implicit or explicit in that prior work is a substantial residual priority risk. No independent validation is claimed.

## References
[1] F. Tong, M. Ahmadi, J. Pan, *Random Distances Associated with Arbitrary Triangles: A Systematic Approach between Two Random Points*, arXiv:1312.2498, first public 2013-11-29. https://arxiv.org/abs/1312.2498

[2] A. M. Mathai, P. Moschopoulos, G. Pederzoli, *Distance between random points in a cube*, Statistica 59 (1999), 61–81. https://doi.org/10.6092/issn.1973-2201/1104

[3] J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, Journal of Applied Probability 19 (1982), 873–879. https://doi.org/10.2307/3213843

[4] R. Pure, S. Durrani, F. Tong, J. Pan, *Distance Distribution Between Two Random Nodes in Arbitrary Polygons*, arXiv:1903.07757, first public 2019-03-18. https://arxiv.org/abs/1903.07757

[5] *Three unlabeled width statistics reconstruct a parallelogram with sharp stability*, public research finding, 2026.

[6] *Fourth-chord moment amplification and angular phase transition for parallelograms*, public research finding, 2026.

[7] T. K. Sheng, *The distance between two random points in plane regions*, Advances in Applied Probability 17 (1985), 748–773. https://doi.org/10.2307/1427086 (publisher abstract specifies all integer-order parallelogram distance moments; full paper unavailable).
