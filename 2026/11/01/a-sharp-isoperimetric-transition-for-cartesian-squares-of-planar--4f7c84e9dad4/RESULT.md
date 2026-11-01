# A sharp isoperimetric transition for Cartesian squares of planar convex bodies

## Finding
Let \(B\subset\mathbb R^2\) be any compact convex body with nonempty interior, area \(A\), and perimeter \(P\). Form its Euclidean Cartesian square \(K=B\times B\subset\mathbb R^4\), and set
\[
q=\frac{4\pi A}{P^2}\in(0,1].
\]
There is a universal constant
\[
q_*=0.8766744290496891255\ldots
\]
such that the **ordinary Euclidean Steiner polynomial** of \(K\) has four distinct negative real roots if \(q<q_*\), exactly three distinct negative real roots (one double) if \(q=q_*\), and exactly two simple negative real roots together with one nonreal conjugate pair if \(q>q_*\).

The constant is the unique zero in \((0,1)\) of
\[
\begin{aligned}
G(q)={}&108q^4+(432\pi-1776)q^3\\
 &+(540\pi^2-4536\pi+9528)q^2\\
 &+(216\pi^3-2664\pi^2+11328\pi-16384)q\\
 &+27\pi^4-204\pi^3+384\pi^2.
\end{aligned}
\]
In particular, if \(B\) is a regular \(m\)-gon, \(m\ge3\), then \(B\times B\) has four distinct real Steiner roots precisely for \(3\le m\le5\), and two real roots plus a nonreal pair for every \(m\ge6\). All real roots are negative.

## Assumptions and scope
The two factors are **the same planar body**, with the product metric induced by the orthogonal Euclidean splitting \(\mathbb R^4=\mathbb R^2\oplus\mathbb R^2\). No boundary smoothness or polygonality is required. The polynomial is the unique continuation from
\[
S_K(t)=\operatorname{vol}_4(K+t\mathbb B_4),\qquad t\ge0,
\]
to complex \(t\); the root claims concern that continuation, not signed geometric parallel sets.

## Proof
**1. Exact product polynomial.** For \(u\ge0\), the planar outer-parallel area is \(A+Pu+\pi u^2\). Its exterior distance-shell density is \(P+2\pi u\). Since squared distances to the two factors add in the orthogonal product, the four-dimensional parallel volume is
\[
\begin{aligned}
S_K(t)={}&A^2+2A(Pt+\pi t^2)\\
&+\int_{\substack{u,v\ge0\\u^2+v^2\le t^2}}
(P+2\pi u)(P+2\pi v)\,du\,dv.
\end{aligned}
\]
Using the elementary quadrant-disk integrals \(\int 1=\pi t^2/4\), \(\int u=\int v=t^3/3\), and \(\int uv=t^4/8\), this becomes
\[
S_K(t)=A^2+2APt+\left(2\pi A+\frac{\pi P^2}{4}\right)t^2
+\frac{4\pi P}{3}t^3+\frac{\pi^2}{2}t^4.
\]
Thus the polynomial depends on the base only through \(A,P\). Put \(\ell=P/(2\pi)\), \(z=t/\ell\). Then
\[
S_K(\ell z)=\pi^2\ell^4F_q(z),\qquad
F_q(z)=\frac12z^4+\frac83z^3+(\pi+2q)z^2+4qz+q^2.
\]

**2. One and only one discriminant transition.** Direct quartic discriminant expansion gives
\[
\operatorname{disc}_z F_q=\frac8{27}q^2G(q).
\]
For a checkable exact certificate that \(G'(q)<0\) throughout \([0,1]\), write its derivative in the Bernstein basis of degree three on each interval in the first column below. The maximum of all four Bernstein coefficients is strictly below the corresponding *rational* bound in the second column:

| \(q\)-interval | Strict upper bound on every Bernstein coefficient of \(G'\) |
|---|---:|
| \([0,1/2]\) | \(-44\) |
| \([1/2,3/4]\) | \(-4\) |
| \([3/4,7/8]\) | \(-1\) |
| \([7/8,1]\) | \(-3/4\) |

Each Bernstein polynomial is nonnegative and the four sum to one. These exact signs follow using rational arithmetic and the certified enclosure
\[
3.141592653589793238<\pi<3.141592653589793239,
\]
obtained from the alternating arctangent series and Machin's identity. The complete rational calculation is in `verify.py`. Moreover, \(G(0)>0\), \(G(1)<0\), and
\[
G(0.8766744)>0>G(0.8766745).
\]
Thus \(G\) has exactly one zero \(q_*\) in \((0,1)\), and that zero is simple.

**3. Root types and multiplicity.** For small positive \(q\), two roots of \(F_q\) approach the distinct negative roots of \(z^2/2+(8/3)z+\pi\). Indeed its discriminant is \(64/9-2\pi>0\). The other two obey \(z=qy+o(q)\), where \(y\) approaches one of the distinct negative roots of \(\pi y^2+4y+1\), whose discriminant is \(16-4\pi>0\). Hence \(F_q\) has four distinct negative real roots for all sufficiently small positive \(q\).

The discriminant never vanishes away from \(q_*\), so the number of real roots cannot change before the transition. Therefore four distinct real roots persist for \(0<q<q_*\). For \(q_*<q\le1\), the negative discriminant of a real quartic means exactly two distinct real roots and one nonreal conjugate pair. A simple zero of the discriminant at \(q_*\) represents one ordinary double root, not a triple root or two simultaneous double roots. The roots remain negative: \(F_q(0)=q^2>0\) and every coefficient is positive, so no nonnegative real root exists.

**4. Regular polygons.** The quotient of a regular \(m\)-gon is
\[
q_m=\frac{\pi}{m\tan(\pi/m)}.
\]
It strictly increases with \(m\ge3\), because \(x\cot x\) strictly decreases for \(0<x<\pi/2\). Exact elementary bounds yield
\[
q_5<\frac{87}{100}<q_*<\frac9{10}<q_6.
\]
For example, \(\tan(\pi/5)=\sqrt{5-2\sqrt5}\), and the left inequality follows from \(\pi<22/7\) and \(\sqrt5<22361/10000\); the right one follows from \(q_6=\pi\sqrt3/6\), \(\pi>3.14\), and \(\sqrt3>1.73\). Monotonicity completes the integer cutoff.

## Verification
Run `python verify.py` with Python 3 and SymPy installed. The standalone script proves the rational enclosure of \(\pi\) from alternating series, checks all sixteen Bernstein-coefficient signs on the four subintervals using exact rational intervals, proves the two discriminant-sign brackets, verifies the polygon cutoff by rational inequalities, and independently recomputes the quartic discriminant and product-polynomial normalization symbolically. It prints a `PASS` line only after every assertion succeeds. The analytic root-count argument above establishes all uncountably many convex bases and every positive isoperimetric quotient; finite numerical root lists are not used as a substitute for that argument.

## Relationship to prior work
The planar Steiner formula and the Cartesian-product M-multiplication theorem are classical. In particular, Katsnelson (2008, Section 12, Theorem 12.4) gives the general product polynomial identity, from which the displayed quartic coefficient formula can also be recovered. Henk and Hernández Cifre (2007) study general root-location bounds, and Henk, Hernández Cifre, and Saorín (2011) characterize the **cone of possible** four-dimensional Steiner roots using ultra-logconcavity. None of these inspected statements supplies the isoperimetric **four-versus-two real-root phase boundary for every Cartesian square** or the regular-pentagon/regular-hexagon cutoff. The contribution claimed here is exactly this sharp classification and its verified uniqueness, not the product formula or general root-cone statements themselves.

## Limitations
The conclusion is restricted to equal planar factors in an orthogonal four-dimensional Cartesian product. The analogous phase diagram for unequal factors is not claimed. The analysis does not classify root positions beyond their reality and signs. Although targeted accessible literature and research-record checks found no equivalent classification, an earlier unindexed computation or a result concealed in a more general treatment remains possible. No independent external proof audit has been performed.

## References
1. M. Henk and M. A. Hernández Cifre, *Notes on the roots of Steiner polynomials*, first public arXiv version 2007-03-13, https://arxiv.org/abs/math/0703373 .
2. V. Katsnelson, *On H. Weyl and J. Steiner Polynomials*, first public arXiv version 2008-03-16, Section 12 (Cartesian-product polynomial theorem), https://arxiv.org/abs/0803.2346 .
3. M. Henk, M. A. Hernández Cifre, and E. Saorín, *Steiner polynomials via ultra-logconcave sequences*, first public arXiv version 2011-12-20, Section 5 (four-dimensional root cone), https://arxiv.org/abs/1112.4741 .
