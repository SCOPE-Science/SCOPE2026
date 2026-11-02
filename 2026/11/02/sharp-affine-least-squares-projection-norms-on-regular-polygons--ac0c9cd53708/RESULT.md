# Sharp affine least-squares projection norms on regular polygons and the disk-limit defect

## Finding

For every integer \(n\ge3\), let \(\mathcal G_n\) be the solid regular \(n\)-gon of circumradius one, with normalized uniform area measure. Let \(T_n\) be the real \(L^2(\mathcal G_n)\)-orthogonal projector onto affine functions. The exact attained \(L^\infty\)-operator norm has the following finite trigonometric formula, involving only one index, elementary functions, and a constant number of arithmetic operations.

Put
\[
 h=\frac{2\pi}{n},\qquad s=\frac{2+\cos h}{12},\qquad
 j=\left\lceil\frac{\arccos(-s)}h\right\rceil,
\]
\[
 a=\cos(jh),\quad b=\sin(jh),\quad
 a_-=\cos((j-1)h),\quad b_-=\sin((j-1)h),
\]
\[
 y=b_-+\frac{-s-a_-}{a-a_-}(b-b_-),\qquad
 A=\frac n2\sin h,
\]
\[
 B=\frac{(n-2j)\sin h-2sb-2y(a+s)}2,
\]
\[
 T=-2\frac{\sin((j-\frac12)h)}{\sin(h/2)}-2a,
\qquad
 M=\frac{\sin h\,T+2(a-s)(-sb-ya)+4s^2y}{6}.
\]
Then
\[
 \boxed{\|T_n\|_{L^\infty\to L^\infty}=1-\frac2A\left(B+\frac Ms\right).}
\]

The absolute kernel-row integral is maximized **exactly at the \(n\) vertices** of \(\mathcal G_n\); the sign of a maximizing row supplies an extremizing input of norm one. The sharp positivity defect for nonnegative inputs bounded by one is \((\|T_n\|-1)/2\).

For the normalized uniform disk, the corresponding affine projection norm is
\[
 L_{\mathrm{disk}}=\frac2\pi\left(\arcsin\frac14+\frac{11\sqrt{15}}{16}\right).
\]
The regular polygons satisfy the sharp second-order limiting law
\[
 \boxed{\lim_{n\to\infty}n^2\bigl(\|T_n\|-L_{\mathrm{disk}}\bigr)
 =\frac{5\pi\sqrt{15}}{12}.}
\]
In particular, the polygonal projection norms approach the disk norm from above for all sufficiently large \(n\). Examples are \(\|T_3\|=19/8\), \(\|T_4\|=233/108\), and \(\|T_6\|=361/180\). These individual small-domain cases and the disk baseline are not claimed as new by themselves.

## Assumptions and scope

The set \(\mathcal G_n\) is the convex hull of \(v_k=(\cos(kh),\sin(kh))\), \(0\le k<n\), and has area \(A=n\sin(h)/2\). Functions are real-valued, and integration uses area divided by \(A\). The operator is the canonical *orthogonal* projection onto \(\operatorname{span}\{1,x_1,x_2\}\), not interpolation, an arbitrary projection onto that range, or projection onto higher-degree polynomials. Its output is continuous, so its essential maximum norm equals its supremum on the closed polygon. The formula holds without restrictions on parity or divisibility of \(n\).

## Proof

**1. Gram matrix and kernel.** Rotational symmetry gives \(\mathbb E Y=0\) and \(\mathbb E(YY^{\mathsf T})=sI_2\). Indeed, triangulate \(\mathcal G_n\) into the congruent origin-to-edge triangles: the average squared radius in one triangle with unit vertices at mutual angle \(h\) is \((2+\cos h)/6\); the coordinate variance is half of this. The projection consequently has reproducing kernel
\[
 K_n(x,z)=1+\frac{x\cdot z}{s},\qquad
 (T_nf)(x)=\frac1A\int_{\mathcal G_n}K_n(x,z)f(z)\,dz.
\]
Thus \(\|T_n\|=\max_{x\in\mathcal G_n}A^{-1}\int|K_n(x,z)|\,dz\). The maximum exists by continuity.

**2. Strict vertex maximizers.** The displayed row integral is convex in \(x\). All vertices have equal row integrals by rotational symmetry. For distinct vertices \(u,v\), one can choose \(\epsilon>0\) small enough that \(z=-(s+\epsilon)u\) is inside the polygon and \(K_n(u,z)<0<K_n(v,z)\). This is possible because \(s\le1/4\), the inradius is \(\cos(\pi/n)\ge1/2\), and \(u\cdot v<1\). The signs persist on a positive-area neighborhood. Therefore the integral of the absolute value is strictly convex between each distinct pair of vertices. Every nonvertex point is a nontrivial convex combination of vertices and has strictly smaller row integral. For a vertex, choose \(f(z)=\operatorname{sgn}K_n(v_0,z)\); then \(\|f\|_\infty=1\) and the norm is attained.

**3. Exact negative-cap calculation.** Fix \(x=v_0=(1,0)\). The kernel is negative precisely when \(z_1<-s\). Its negative cap \(C\) is cut by the vertical line \(z_1=-s\). By the choice of \(j\), the upper intersection is \((-s,y)\) on the side from \(v_{j-1}\) to \(v_j\); the lower intersection is \((-s,-y)\). In counterclockwise order the cap vertices are these upper and lower intersections together with \(v_j,v_{j+1},\ldots,v_{n-j}\).

The shoelace area formula gives \(|C|=B\). Its first horizontal moment formula \(\int_C z_1\,dz=\frac16\sum_{\mathrm{edges}\,p\to q}(p_1+q_1)\det(p,q)\) gives \(\int_C z_1\,dz=M\). For the full-vertex arc, the trigonometric telescoping identity is
\[
 \sum_{k=j}^{n-j-1}\bigl(\cos(kh)+\cos((k+1)h)\bigr)
 =-2\frac{\sin((j-\frac12)h)}{\sin(h/2)}-2\cos(jh)=T.
\]
Consequently these area and moment quantities reduce to the formulas in the Finding. Since \(\mathbb E K_n(v_0,Y)=1\) and \(K_n(v_0,z)<0\) exactly on \(C\),
\[
 \frac1A\int_{\mathcal G_n}|K_n(v_0,z)|\,dz
 =1-\frac2A\int_C\left(1+\frac{z_1}{s}\right)dz
 =1-\frac2A\left(B+\frac Ms\right).
\]
This also proves the positivity-defect interpretation: the indicator of the negative cap attains the minimum projected value \(- (\|T_n\|-1)/2\) at \(v_0\).

**4. Sharp disk-limit coefficient.** Write \(h=2\pi/n\), and let \(\mathbb E_n,\mathbb E_D,\mathbb E_S\) denote normalized area expectation on the polygon and disk and uniform arc expectation on the circle, respectively. The radial boundary of \(\mathcal G_n\) relative to the normal to each side is \(r_n(\theta)=\cos(h/2)/\cos\theta\) for \(|\theta|\le h/2\). Its missing radial thickness has cell average \(h^2/12+O(h^4)\). For any fixed continuous function \(g\) on the disk,
\[
 \mathbb E_n g=\mathbb E_D g+\frac{h^2}{6}
 (\mathbb E_D g-\mathbb E_S g)+o(h^2).
\]
The formula follows by integrating the thin missing boundary layer, then normalizing by \(|\mathcal G_n|=\pi(1-h^2/6+O(h^4))\); continuity suffices for the Riemann-sum limit, including the absolute-value kernel.

Here \(s=1/4-h^2/24+O(h^4)\). Set \(g_t(z)=|1+z_1/t|\). The derivative in \(t\) exists almost everywhere and is dominated near \(t=1/4\). Direct integration with the disk coordinate density \(2\sqrt{1-x^2}/\pi\) yields
\[
 \mathbb E_D g_{1/4}=\frac2\pi\left(\arcsin\frac14+\frac{11\sqrt{15}}{16}\right),\quad
 \mathbb E_S g_{1/4}=\frac2\pi\left(\arcsin\frac14+\sqrt{15}\right),
\]
\[
 \mathbb E_D\left[z_1\operatorname{sgn}(1+4z_1)\right]=\frac{5\sqrt{15}}{16\pi},\quad
 \left.\frac{d}{dt}\mathbb E_Dg_t\right|_{t=1/4}
 =-\frac{5\sqrt{15}}\pi.
\]
Inserting these expressions into the geometric and parameter variations gives
\[
 \|T_n\|-L_{\mathrm{disk}}=
 h^2\left[-\frac{5\sqrt{15}}{48\pi}
 +\frac{5\sqrt{15}}{24\pi}\right]+o(h^2)
 =\frac{5\sqrt{15}}{48\pi}h^2+o(h^2),
\]
which proves the stated \(n^2\)-limit.

## Verification

The accompanying standalone Python 3 checker `verification/check_regular_polygon.py` uses only the standard library. It independently integrates the absolute affine kernel over each origin-to-edge triangle by piecewise polynomial primitives, instead of using cap shoelace moments. It compares the two formulas for each integer \(3\le n\le80\), checks the exact known small cases, samples 480 interior rows, and checks the asymptotic coefficient at three large orders. These are finite numerical corroborations, not substitutes for the proof of the all-order formula or asymptotic limit.

Run with `python3 verification/check_regular_polygon.py`. The recorded maximum discrepancy in the 78 independent row comparisons was below \(1.4\times10^{-15}\).

## Relationship to prior work

Hangelbroek, Narcowich, Sun and Ward (arXiv:1005.2424, first public 13 May 2010) establish general \(L^p\) stability principles for least-squares projections onto spaces spanned by localized kernels. Their Sections 4–5 address Gram-matrix bounds and general projector estimates, not the exact regular-polygon affine projection norm. Xu (arXiv:0802.0316, 4 February 2008) develops trigonometric Fourier approximation on hexagonal and triangular spectral domains; its Fourier projections are not the present degree-one algebraic least-squares projector. Dunkl (1987) develops orthogonal polynomial bases and expansions on a regular hexagon, a closer object-level reference, but the full text was not accessible for complete comparison. Its accessible abstract does not state the sharp \(L^\infty\) projector norm; its possible implicit coverage remains unresolved. The polygonal finite-element work of Beirão da Veiga and Mora (2011) uses local \(L^2\) affine approximation inequalities, but does not state an exact sharp regular-polygon amplification constant in its examined material.

The triangle, square, and disk special values appear or follow in previous exact-domain analyses; their independent novelty is not asserted. The proposed new information is the all-order regular-polygon formula, complete vertex-extremizer classification, and explicit sharp second-order disk-limit coefficient.

## Limitations

The theorem is for real affine \(L^2\)-orthogonal projection under uniform two-dimensional area measure, on solid regular polygons, not boundary arclength measure, higher-degree polynomial projection, general polygons, or arbitrary projection choices. It does not prove monotonicity of the exact norms over all finite \(n\), even though the leading disk-limit coefficient is positive. The inaccessible full text of Dunkl's hexagon article leaves a specific literature-priority uncertainty for that domain, and unindexed equivalent calculations cannot be excluded. Verification is computationally reproducible but is not an independent external mathematical audit.

## References

1. T. Hangelbroek, F. J. Narcowich, X. Sun, and J. D. Ward, *Kernel Approximation on Manifolds II: The \(L_\infty\)-norm of the \(L_2\)-projector*, arXiv:1005.2424 (first public 2010-05-13), https://arxiv.org/abs/1005.2424.
2. Y. Xu, *Fourier series and approximation on hexagonal and triangular domains*, arXiv:0802.0316 (first public 2008-02-04), https://arxiv.org/abs/0802.0316.
3. C. F. Dunkl, *Orthogonal Polynomials on the Hexagon*, SIAM Journal on Applied Mathematics 47 (1987), 343–351, https://doi.org/10.1137/0147022.
4. L. Beirão da Veiga and D. Mora, *A mimetic discretization of the Reissner–Mindlin plate bending problem*, Numerische Mathematik 117 (2011), 425–462, https://doi.org/10.1007/s00211-010-0358-8.
