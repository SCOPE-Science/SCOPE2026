# Sharp tetrahedral-volume profile in the cube–octahedron intersection family

## Finding
For each real \(1\le c\le3\), let
\[
K_c=\left\{(x_1,x_2,x_3)\in[-1,1]^3:\ |x_1|+|x_2|+|x_3|\le c\right\},
\qquad M(c)=\max_{T\subseteq K_c}\operatorname{vol}_3(T),
\]
where \(T\) ranges over all tetrahedra with arbitrary vertices in \(K_c\). The exact sharp determinant profile \(D(c)=6M(c)\) is
\[
\boxed{D(c)=
\begin{cases}
2\bigl(1+(c-1)+2(c-1)^2\bigr),&1\le c\le\tfrac32,\\
8(c-1),&\tfrac32\le c\le2,\\
8\bigl(1+(c-2)^2\bigr),&2\le c\le3.
\end{cases}}
\]
The associated normalized maximal tetrahedral volume has the sharp lower envelope
\[
\boxed{\frac{M(c)}{\operatorname{vol}_3(K_c)}\ge\frac16,}
\]
with equality **precisely when** \(c=\tfrac32\), for which \(K_c\) is the regular truncated octahedron. The normalized ratio is not globally monotone: it has a second, strictly higher local minimum at \(c=2+u_*\), where \(u_*\in(0,1)\) is the unique root of \(u_*^4-16u_*+3=0\).

## Assumptions and scope
All volumes are ordinary three-dimensional Euclidean volumes, and \(K_c\) is a full-dimensional compact convex polytope for every real \(c\in[1,3]\). A tetrahedron is the convex hull of four points in \(K_c\), not necessarily vertices of the polytope. Tetrahedral volume equals one-sixth of the absolute determinant of three edge vectors. The conclusion does not concern higher-dimensional analogues or unconstrained centrally symmetric convex bodies.

## Proof
**1. Vertex reduction.** For \(1<c<2\), the vertices of \(K_c\) are precisely the 24 independently signed coordinate permutations of \((1,t,0)\), where \(t=c-1\). For \(2<c<3\), they are the 24 independently signed coordinate permutations of \((1,1,u)\), where \(u=c-2\). This follows directly by taking three independent tight supporting inequalities from the coordinate cube and the eight inequalities \(\pm x_1\pm x_2\pm x_3\le c\); coordinate-sign planes do not create additional vertices. At the endpoints, the same formulas remain exhaustive, although some of the listed formal vertices coincide.

For any four points \(p_0,p_1,p_2,p_3\), let
\[
\Delta(p_0,p_1,p_2,p_3)=\det(p_1-p_0,p_2-p_0,p_3-p_0).
\]
This signed determinant is affine separately in each argument. Writing each \(p_i\in K_c\) as a convex combination of vertices, \(\Delta\) is a convex combination of determinants of vertex quadruples. Thus the largest possible absolute tetrahedral determinant is achieved at a vertex quadruple; exact bounds for all such quadruples bound all tetrahedra.

**2. Exact polynomial upper-bound certificate.** The signed determinant of four formal vertices is a polynomial of degree at most three with integer coefficients in \(t\) or \(u\). There are \(\binom{24}{4}=10{,}626\) unordered four-vertex subsets in each parameterization. To prove the following three bounds uniformly over continuous intervals, apply the degree-three Bernstein positivity test to each signed determinant polynomial \(p\):
\[
\begin{array}{c|c|c}
\text{parameter range}&\text{bound }E&\text{vertex type}\\\hline
0\le t\le\tfrac12&2+2t+4t^2&(1,t,0)\\
\tfrac12\le t\le1&8t&(1,t,0)\\
0\le u\le1&8+8u^2&(1,1,u)
\end{array}
\]
For each interval \([a,b]\), form \(q_\pm(s)=E(a+(b-a)s)\pm p(a+(b-a)s)\). The attached `verify.py` computes the coefficients in the exact rational Bernstein expansion
\[
q_\pm(s)=\sum_{i=0}^{3}B_i^\pm\binom3i s^i(1-s)^{3-i},\qquad 0\le s\le1.
\]
It independently constructs all formal vertices and all determinant polynomials, then checks \(B_i^\pm\ge0\) for every \(i\), both signs, and every quadruple. The checker evaluates **63,756 exact polynomial nonnegativity assertions**; the number counts two signs over three parameter intervals and all 10,626 quadruples in each. Because each Bernstein basis polynomial is nonnegative on \([0,1]\), these exact finite inequalities imply \(|p|\le E\) over the *entire continuous parameter intervals*, not just sampled values. No extrapolation from a numeric grid is used.

**3. Sharpness at every parameter.** The three upper bounds are attained by the following vertex quadruples, in the displayed order:
\[
\begin{aligned}
0\le t\le\tfrac12:&\quad(-1,-t,0),\ (-t,1,0),\ (t,0,-1),\ (t,0,1),\\
\tfrac12\le t\le1:&\quad(-1,-t,0),\ (0,t,-1),\ (0,t,1),\ (1,-t,0),\\
0\le u\le1:&\quad(-1,-1,-u),\ (-1,1,u),\ (1,-u,1),\ (1,u,-1).
\end{aligned}
\]
Their signed determinants are, respectively, \(-2-2t-4t^2\), \(8t\), and \(8+8u^2\), as the checker independently verifies. Combining with step 2 establishes the stated profile for every \(c\).

**4. Polytope volumes.** For \(1\le c\le2\), start with the octahedron \(\sum|x_i|\le c\), of volume \(\frac43c^3\), and remove the six nonoverlapping caps beyond the faces of the cube; the six caps have total volume \(4(c-1)^3\). For \(2\le c\le3\), start with the cube of volume \(8\) and remove eight disjoint corner simplices, each of volume \((3-c)^3/6\). Thus
\[
\operatorname{vol}_3(K_c)=
\begin{cases}
\frac43\bigl(1+3t+3t^2-2t^3\bigr),&1\le c\le2,\quad t=c-1,\\
\frac43\bigl(6-(1-u)^3\bigr),&2\le c\le3,\quad u=c-2.
\end{cases}
\]
Writing \(F(t)=1+3t+3t^2-2t^3\), the exact normalized ratio is
\[
\frac{M(c)}{\operatorname{vol}_3(K_c)}=
\begin{cases}
\dfrac{1+t+2t^2}{4F(t)},&0\le t\le\tfrac12,\\
\dfrac{t}{F(t)},&\tfrac12\le t\le1,\\
\dfrac{1+u^2}{6-(1-u)^3},&0\le u\le1.
\end{cases}
\]
The first regime satisfies \(6(1+t+2t^2)-4F(t)=2(t+1)(2t-1)^2\ge0\), with equality only at \(t=\frac12\). The second satisfies \(6t-F(t)=(2t-1)(t^2-t+1)\ge0\), with equality only at \(t=\frac12\). In the third, \(6(1+u^2)-\bigl(6-(1-u)^3\bigr)=6u^2+(1-u)^3>0\). Hence the global normalized minimum is \(1/6\) uniquely at \(c=\tfrac32\).

**5. Additional local phase change.** Differentiating the three rational ratio expressions gives derivative signs, in their interiors, respectively equal to the signs of
\[
(2t-1)(2t^3+3t^2+6t+2),\qquad 4t^3-3t^2+1,\qquad16u-3-u^4.
\]
The first is negative for \(0<t<\frac12\), the second positive for \(\frac12<t<1\), and the third increases strictly from a negative value to a positive value on \([0,1]\). Thus \(c=2\) is a strict local maximum of the normalized ratio, followed by the unique secondary local minimum at \(c=2+u_*\) (approximately \(2.1875773752\)); that minimum is strictly larger than \(1/6\).

## Verification
Run `python3 verify.py` using Python 3 with only its standard library. A successful execution prints the two 24-vertex counts, the exact witness determinants, and `VERIFY_OK Bernstein_polynomial_inequalities= 63756`. All signed determinants are generated from formal affine coordinates, with arithmetic entirely in integers and rational numbers. Each of the three interval bounds is independently supported by a listed exact witness. This is a finite, exhaustive polynomial certificate combined with the analytic convex-combination reduction and cap-volume derivations; it is not a finite sampling argument.

## Relationship to prior work
Horváth and Lángi study maximal-volume polytopes subject to a *spherical* inscription constraint and fixed numbers of vertices; that work does not optimize tetrahedra inside the intersection \(K_c\). Akopyan and Glazyrin give structural statements for maximal simplices in centrally symmetric sets, prisms, and parallelotopes; their Corollary 2.3 ensures a maximum-volume simplex contains the center of a centrally symmetric convex body, but does not determine this profile or its minimizing parameter. Published work on illumination and graph distances for the same cube–cross-polytope intersection family concerns different extremal quantities and does not imply a determinant or volume-ratio formula. A complete historical priority guarantee is not asserted.

## Limitations
The exact profile concerns only the specified three-dimensional, centrally symmetric one-parameter family. It supplies attaining quadruples but not a classification of all maximizing tetrahedra. Exhaustive symbolic positivity is verified by a standalone checker rather than a hand-written table of 63,756 inequalities, and the integrity of that finite computation should be independently audited. No assertion about a globally minimizing convex body outside this family, or about analogous higher-dimensional transition points, is made.

## References
1. Á. G. Horváth and Zs. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496 (first submitted 26 February 2014), later *Monatshefte für Mathematik* 181 (2016), 341–354; https://arxiv.org/abs/1402.6496 .
2. A. V. Akopyan and A. A. Glazyrin, *On maximum volume simplices in polytopes*, *Periodica Mathematica Hungarica* 69 (2014), 251–256, DOI 10.1007/s10998-014-0051-2; author-hosted full text: https://users.mccme.ru/akopyan/papers/Akopyan-Glazyrin-Maximum-Volume.pdf .
