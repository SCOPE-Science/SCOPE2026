# Nonmonotone sharp two-segment Bézout profile of rounded equilateral triangles

## Finding
Let \(B\subset\mathbb R^2\) be the closed Euclidean unit disk and
\[
T=\operatorname{conv}\left\{(1,0),\left(-\frac12,\frac{\sqrt3}{2}\right),\left(-\frac12,-\frac{\sqrt3}{2}\right)\right\},\qquad K_r=T+rB\quad(r\ge0).
\]
For compact nondegenerate line segments \(L,M\) of nonparallel directions, define the restricted two-body Bézout coefficient
\[
\beta_{\rm seg}(K_r)=\sup_{L,M}\frac{\operatorname{area}(K_r)\,V_2(L,M)}{V_2(K_r,L)V_2(K_r,M)},
\]
where \(V_2\) is the standard symmetric mixed area (the coefficient of \(2st\) in \(\operatorname{area}(sA+tC)\) is \(2V_2(A,C)\)). Then
\[
\boxed{\displaystyle \beta_{\rm seg}(K_r)=\frac{\frac{3\sqrt3}{2}+6\sqrt3\,r+2\pi r^2}{(\frac32+2r)(\sqrt3+2r)}.} \tag{1}
\]
For every \(r>0\), equality is attained exactly when the two **segment** directions are perpendicular and their respective normal directions are, in either order, a minimum-width normal and a perpendicular maximum-width normal of \(T\), up to the triangle's symmetries and direction reversal. The maximizing direction pairs do not depend on \(r>0\).

The coefficient equals \(1\) at \(r=0\), increases strictly until one positive radius \(r_*\), and decreases strictly thereafter to \(\pi/2\) from above. The radius \(r_*\) is the unique positive root of
\[
\begin{aligned}
Q(r)={}&18-\frac{9\sqrt3}{2}+(6\sqrt3\pi-12\sqrt3)r\\
&+(6\pi+4\sqrt3\pi-24\sqrt3)r^2=0.
\end{aligned}
\]
In particular, \(r_*=13.2426734684\ldots\) and \(\beta_{\rm seg}(K_{r_*})=1.5729182674\ldots>\pi/2\). Thus outer parallel rounding does **not** make this sharp restricted Bézout coefficient monotone toward its disk value.

## Assumptions and scope
All geometry is Euclidean and planar; \(r\ge0\). The test sets \(L,M\) are nondegenerate line segments. Their directions may be reversed and their lengths and locations are immaterial. The coefficient is **not** claimed to be optimal when arbitrary convex test bodies, rather than segments, are admitted. At \(r=0\) the formula remains valid, but uniqueness of maximizing directions is not asserted. A minimal-area enclosing parallelogram of \(K_r\) has area \(2\operatorname{area}(K_r)/\beta_{\rm seg}(K_r)=(\frac32+2r)(\sqrt3+2r)\); this is an equivalent formulation of (1), not a second independent theorem.

## Proof
**1. Width formulation.** For a unit normal \(u\), let \(w(u)=h_T(u)+h_T(-u)\) denote the width of \(T\). Its minimum and maximum are \(a=3/2\) and \(b=\sqrt3\). The width of \(K_r\) is \(w(u)+2r\). If segments \(L,M\) have lengths \(\ell,m\) and normals \(u,v\), then the planar segment projection identity gives
\[
V_2(K_r,L)=\frac\ell2(w(u)+2r),\quad V_2(K_r,M)=\frac m2(w(v)+2r),\quad V_2(L,M)=\frac{\ell m}{2}|\det(u,v)|.
\]
Therefore the quotient equals
\[
\frac{2\operatorname{area}(K_r)|\det(u,v)|}{(w(u)+2r)(w(v)+2r)}.\tag{2}
\]

**2. Two sharp directional inequalities.** For all unit normals \(u,v\), put \(s=|\det(u,v)|\). We show
\[
 w(u)w(v)\ge ab\,s,\qquad w(u)+w(v)\ge(a+b)s.\tag{3}
\]
For the product inequality, extend \(w\) homogeneously to \(\mathbb R^2\). Its unit ball is the regular centrally symmetric hexagon with vertices on rays of arguments \(k\pi/3\) at radius \(1/a\). The bilinear map \((x,y)\mapsto\det(x,y)\) attains its maximum absolute value on two vertices of that hexagon, where it is \(\sqrt3/(2a^2)=1/(ab)\). Scaling \(u/w(u)\), \(v/w(v)\) proves the first inequality.

For the sum inequality, use dihedral symmetry and reversal of normals to take \(u=(\cos x,\sin x)\), \(0\le x\le\pi/6\), and \(v=(\cos\psi,\sin\psi)\), \(0\le\psi\le\pi\). The width of \(u\) is \(b\cos(\pi/6-x)\). If \(0\le\psi\le\pi/3\), then \(s\le\sqrt3/2\) while \(w(u)+w(v)\ge2a>(a+b)\sqrt3/2\).

If \(\pi/3\le\psi\le2\pi/3\), put \(y=\psi-\pi/2\in[-\pi/6,\pi/6]\). Then \(s=\cos(y-x)\), \(w(v)=b\cos y\), and
\[
\begin{aligned}
w(u)-a &= 2b\sin(x/2)\sin(\pi/6-x/2),\\
b(s-\cos y)&=2b\sin(x/2)\sin(y-x/2).
\end{aligned}
\]
The first right-hand side is at least the second because \(y\le\pi/6\), and sine increases on the relevant interval. Hence \(w(u)+w(v)\ge a+bs\ge(a+b)s\).

If \(2\pi/3\le\psi\le\pi\), put \(y=\psi-2\pi/3\in[0,\pi/3]\). Then \(s=\cos(\pi/6+y-x)\le\cos(\pi/6-x)=w(u)/b\). Consequently \((a+b)s\le w(u)+as\le w(u)+a\le w(u)+w(v)\). This proves the second inequality and (3).

**3. Exact optimization and equality.** Set \(t=2r\). Combining (3) and \(s\le1\) yields
\[
\begin{aligned}
 &(w(u)+t)(w(v)+t)-(a+t)(b+t)s\\
 &=[w(u)w(v)-ab s]+t[w(u)+w(v)-(a+b)s]+t^2(1-s)\ge0.\tag{4}
\end{aligned}
\]
Take \(u=(1,0)\) and \(v=(0,1)\): they are perpendicular, with \(w(u)=a\), \(w(v)=b\), so (4) is sharp. For \(r>0\), equality in (4) forces \(s=1\), and the product inequality is an equality. If \(u\) has angle \(x\in[0,\pi/6]\), then the perpendicular normal has width \(b\cos x\) while \(w(u)=b\cos(\pi/6-x)\). Their product is at least \(ab\), with equality only when \(x=0\) or \(x=\pi/6\), yielding exactly the asserted dihedral orbit. Formula (2) is therefore maximized at \(2\operatorname{area}(K_r)/[(a+2r)(b+2r)]\).

**4. Area and phase transition.** The triangle has area \(3\sqrt3/4\) and perimeter \(3\sqrt3\). Steiner's parallel-area formula gives \(\operatorname{area}(K_r)=3\sqrt3/4+3\sqrt3 r+\pi r^2\), proving (1). Differentiating (1), its derivative has the sign of \(Q(r)\) displayed above; the omitted denominator is strictly positive. Its constant and linear coefficients are positive, while the quadratic coefficient is negative. Indeed \(6\pi+4\sqrt3\pi-24\sqrt3<0\), for instance using \(\pi<22/7\), \(\sqrt3>5/3\). Thus \(Q\) has exactly one positive root, with sign positive before the root and negative afterward. The leading quadratic terms of (1) give the limiting value \(\pi/2\). Strict decrease after the maximum forces the approach from above. The stated numerical values follow by solving the quadratic, and are not used in the proof.

## Verification
The standalone `verify.py` checks the algebraic derivative, the exact width law from vertex dot products, both inequalities (3) on a reproducible angular grid, the formula and direction optimizers against an independent sampling search, and the unique positive stationary root. Run `python3 verify.py` using the Python standard library; successful output is `VERIFY_OK`. These finite checks supplement, but do not replace, the analytic directional proof for all normals or the derivative-sign argument for all radii.

## Relationship to prior work
Langharst and Wang's 2026 theorem characterizes simplices using Bézout inequalities for all convex test bodies; it does not calculate the sharp **segment-restricted** coefficient for an outer parallel body of a triangle. Soprunov and Zvavitch's 2015 work proves simplex equality and a sharp universal coefficient for planar test bodies, rather than this exact family-dependent profile. The established planar identification of a segment-test quotient with the minimum containing-parallelogram area is used explicitly here, not claimed as new.

A published exact enclosing-parallelogram theorem for centrally symmetric hexagons concerns polygonal *symmetric* bodies; the smooth rounded triangle here is nonsymmetric. Published area-optimization results on intersections of disks (regular disk triangles) concern a different body family and objective. Another published normalized Bézout-witness monotonicity result concerns balls and their intersection lenses, rather than this family. None of the inspected statements entails the nonmonotone exact profile or its radius-independent maximizing segment directions. Some older equivalent special-case calculation may be unindexed.

## Limitations
The theorem concerns only two segment test bodies and planar Euclidean outer offsets of one equilateral triangle. It does not compute the unrestricted two-body Bézout coefficient nor claim novel formulas for area of an outer parallel body or for the disk's coefficient. The small numerical overshoot above the disk value is supported by an exact strict phase transition. This calculation has not received independent scientific validation, and a priority risk remains from specialized enclosing-parallelogram literature.

## References
1. D. Langharst and S. Wang, *The Bézout inequality for mixed volumes characterizes simplices*, arXiv:2609.20380v1, first public 2026-09-17.
2. I. Soprunov and A. Zvavitch, *Bezout Inequality for Mixed volumes*, arXiv:1507.00765, first public 2015-07-02.
3. C. Saroglou, I. Soprunov, and A. Zvavitch, *Characterization of simplices via the Bézout inequality for mixed volumes*, arXiv:1512.05442.
4. *Exact enclosing-parallelogram profile and sharp affine stability for symmetric hexagons*, published research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-enclosing-parallelogram-profile-and-sharp-affine-stability--72e7e289e20b.
5. *A sharp Steiner-area phase diagram for regular disk triangles*, published research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-steiner-area-phase-diagram-for-regular-disk-triangles--3d6ed11c0577.
6. *Strict Bézout-witness monotonicity for translated Euclidean-ball lenses*, published research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-strict-b-zout-witness-monotonicity-for-translated-euclidean-ball--390b82325cd4.
