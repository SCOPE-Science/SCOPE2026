# A modulo-three edge-crossing law for affine least squares on regular polygon perimeters

## Finding
Let \(R_n\subset\mathbb R^2\) be the regular \(n\)-gon with circumradius one, \(n\ge3\), and let \(\mu_n\) be normalized arclength on its perimeter. Let \(P_n:L^2(\mu_n)\to\mathrm{Aff}(\mathbb R^2)|_{\partial R_n}\) be the real orthogonal projector onto restrictions of affine functions. Set
\[
h=\frac{2\pi}{n},\quad c=\frac6{2+\cos h},\quad k=\left\lceil\frac n3\right\rceil,
\quad b=1+c\cos(kh),\quad d=c\bigl(\cos((k-1)h)-\cos(kh)\bigr).
\]
Here \(b<0<d\). Its exact sharp endpoint norm is
\[
\boxed{\ \|P_n\|_{L^\infty(\mu_n)\to L^\infty(\mu_n)}
=1+\frac2n\left[
c\left(\frac{\sin((k-\frac12)h)}{\sin(h/2)}+\cos(kh)\right)
-(n-2k)+\frac{b^2}{d}\right].\ }
\]
Exactly the \(n\) vertices are norming evaluation points. At each vertex \(v\), all norm-attaining real inputs, up to a change of overall sign and on null sets, are the sign of \(K_n(v,\cdot)\), where
\[
K_n(x,y)=1+c\,x\cdot y.
\]
Let \(\eta_n=0\) for \(n\equiv0\pmod3\), \(\eta_n=-1\) for \(n\equiv1\pmod3\), and \(\eta_n=1\) for \(n\equiv2\pmod3\). Then
\[
\boxed{\ \|P_n\|=\frac13+\frac{2\sqrt3}{\pi}
+\frac{2\pi\sqrt3}{3n^2}
+\eta_n\frac{8\pi^2}{81n^3}+O(n^{-4}).\ }
\]
The universal positive second-order discrepancy and signed third-order modulo-three phase give the sharp first two correction orders to the rank-three Fourier projection norm on the limiting circle.

## Assumptions and scope
Each polygon edge has uniform arclength density; edges have equal length, hence each carries probability \(1/n\). The space is the three-dimensional real affine-polynomial space restricted to this closed polygonal curve, not the piecewise-affine finite-element space and not the counting-measure space on its vertices. Equality of finite-dimensional projection outputs is understood via the unique continuous affine representative. Similarity rescaling of the polygon does not change the norm. The formula includes \(n=3\) and \(n=4\); for instance \(\|P_3\|=16/9\) and \(\|P_4\|=5/3\).

## Proof
**1. Kernel and covariance.** Write the vertices as \(v_j=(\cos(jh),\sin(jh))\), for \(j=0,\ldots,n-1\), with indices modulo \(n\). Rotation symmetry gives \(\int y\,d\mu_n(y)=0\) and scalar coordinate covariance. On the edge \(y(t)=(1-t)v_j+tv_{j+1}\), direct integration yields
\[
\int_0^1 |y(t)|^2dt=\frac{2+\cos h}{3}.
\]
Consequently \(\int yy^T\,d\mu_n(y)=\frac{2+\cos h}{6}I_2\), so inversion of the Gram matrix for \(1,y_1,y_2\) gives the stated reproducing kernel \(K_n(x,y)=1+c x\cdot y\). Its evaluation norm is
\[
\Lambda_n(x)=\int_{\partial R_n}|1+c x\cdot y|\,d\mu_n(y).
\]
By convexity in \(x\), its maximum over the polygon occurs at a vertex, and by rotational symmetry all vertices have the same value. The sharp operator norm is therefore \(\Lambda_n(v_0)\).

**2. Exact sign interval.** At the vertices put \(a_j=1+c\cos(jh)\). For \(n\ge3\) the negative vertices form exactly the contiguous cyclic interval
\[
\{j:a_j<0\}=\{k,k+1,\ldots,n-k\},\qquad k=\lceil n/3\rceil.
\]
Indeed, \(kh\in[2\pi/3,\pi]\) and \(c>2\), so \(a_k<0\). For \(n\ge4\), write \((k-1)h=2\pi/3-u\), with \(h/3\le u\le h\le\pi/2\). Then
\[
6\cos((k-1)h)+2+\cos h
=-3\cos u+3\sqrt3\sin u+2+\cos h
\ge\frac{2\sqrt3}{\pi}h-\frac12h^2>0.
\]
The bounds use \(\sin u\ge2u/\pi\), \(\cos h\ge1-h^2/2\), and \(h\le\pi/2<4\sqrt3/\pi\). The case \(n=3\) follows by direct substitution. Thus \(a_{k-1}>0\), and monotonicity of cosine on \([0,\pi]\), followed by reflection, proves the exact interval. In particular all \(a_j\) are nonzero.

**3. Integrate the negative part.** Along an edge from \(v_j\) to \(v_{j+1}\), the kernel at \(v_0\) is affine in the edge parameter, with endpoint values \(a_j,a_{j+1}\). The \(n-2k\) edges with both endpoints negative contribute
\[
-\sum_{j=k}^{n-k-1}\frac{a_j+a_{j+1}}2
=c\left[\frac{\sin((k-\frac12)h)}{\sin(h/2)}+\cos(kh)\right]-(n-2k)
\]
to the sum of edgewise integrals of the negative part. This identity also holds when \(n=4\), when the sum over wholly negative edges is empty. The two crossing edges contribute a total of \(b^2/d\), by similar triangles (each crossing area is \(b^2/(2d)\)). As the integral of \(K_n(v_0,\cdot)\) is one,
\[
\Lambda_n(v_0)=1+2\int(-K_n(v_0,y))_+\,d\mu_n(y).
\]
Every edge carries mass \(1/n\), proving the formula.

**4. Strict norming-point classification.** At \(y=v_k\), the values \(K_n(v_0,v_k)=a_k<0\) and \(K_n(v_1,v_k)=a_{k-1}>0\) have opposite signs; this remains true on a positive-measure neighborhood of \(v_k\) on the perimeter. Hence for every \(0<t<1\), strict triangle inequality inside the integral gives
\[
\Lambda_n((1-t)v_0+tv_1)<(1-t)\Lambda_n(v_0)+t\Lambda_n(v_1)=\|P_n\|.
\]
Rotation covers every open polygon edge. Every point in the interior of the polygon admits a convex decomposition into all the vertices with strictly positive coefficients; the same sign disagreement forces strict inequality there too. Thus precisely the vertices are norming. Equality in \(|\int K_n(v,y)f(y)d\mu_n(y)|\le\int |K_n(v,y)|d\mu_n(y)\) forces \(f=\pm\operatorname{sgn}K_n(v,\cdot)\) almost everywhere; the zero set has zero arclength measure.

**5. Arithmetic asymptotic.** Put \(\theta=kh\) and \(\delta=k-n/3\). According to \(n\bmod3\), \(\delta\) equals \(0,2/3,1/3\), respectively. Substitute \(\theta=2\pi/3+\delta h\) into the negative-part bracket \(F(h)\) in the exact formula. Laurent expansion of the elementary sine and cosine quotients yields, for the three values of \(\delta\),
\[
F(h)=-\frac{2\pi}{3h}+\frac{2\sqrt3}{h}+\frac{\sqrt3}{6}h+
\begin{cases}0,&\delta=0,\\-h^2/81,&\delta=2/3,\\+h^2/81,&\delta=1/3\end{cases}+O(h^3).
\]
The singular factors \(b^2/d\) have removable Taylor expansions because their numerator vanishes to second order and their denominator to first order. Since \(2/n=h/\pi\), substitution of \(h=2\pi/n\) proves the stated asymptotic expansion uniformly across the three residue classes.

## Verification
The standalone `verify_regular_polygon_affine.py` independently integrates the absolute affine kernel on each edge for every \(3\le n\le110\), checks direct edge covariance, tests nonvertex evaluation points, and symbolically verifies all three Laurent expansions. Additional high-precision large-\(n\) checks test the asymptotic remainder. Run with Python 3 and `mpmath` plus `sympy`; the analytic proof, not the finite checks, establishes the universal conclusions.

## Relationship to prior work
Oswald's 2006 analysis establishes that the \(L^\infty\) norms of piecewise-linear finite-element \(L^2\) projections on certain planar triangulations grow without bound. Its spline space and two-dimensional area measure are different from the fixed three-dimensional affine space on a polygonal boundary considered here. Hangelbroek, Narcowich, Sun and Ward's 2010 manuscript establishes \(L^p\) stability of least-squares projection onto localized kernel spaces on smooth manifolds; its general stability result does not determine the norm or the edge-crossing arithmetic on regular polygon perimeters.

The published exact three-frequency Fourier projection formula on finite cyclic groups uses normalized **counting measure** on the \(n\) vertices and the discrete kernel \(1+2\cos(2\pi j/n)\). In the present continuous perimeter problem the covariance is \((2+\cos h)/6\), the kernel parameter is \(c\ne2\), and the two sign-changing edges produce a nonzero crossing-area term \(b^2/d\). The discrete result neither states nor implies the present perimeter norm or its signed cubic correction. It is, however, a natural comparison because both models tend to the same circular rank-three projection norm. Indexed and direct searches for the perimeter formula did not uncover equivalent exact coverage; absence from those searches is not proof of uniqueness.

## Limitations
The statement requires a regular planar polygon, normalized continuous perimeter arclength, real inputs, and affine rather than piecewise-affine or higher-degree approximation. It makes no claim of monotonicity in \(n\), no universal statement for irregular polygons, and no operator identity with discrete cyclic Fourier projection. The \(O(n^{-4})\) remainder is an asymptotic statement, not a uniform finite-\(n\) inequality. Equivalent unindexed literature remains a residual originality risk.

## References
1. P. Oswald, *A counterexample concerning the L2-projector onto linear spline spaces*, arXiv:math/0611573v1, publicly posted 2006-11-19, https://arxiv.org/abs/math/0611573.
2. T. Hangelbroek, F. J. Narcowich, X. Sun and J. D. Ward, *Kernel Approximation on Manifolds II: The L-infinity norm of the L2-projector*, arXiv:1005.2424v1, publicly posted 2010-05-13, https://arxiv.org/abs/1005.2424.
3. *Exact three-frequency Fourier projection norm on every cyclic group*, published research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-three-frequency-fourier-projection-norm-on-every-cyclic-gr--b176a6018242.
