# Sharp full-vertex shadows of right regular polygonal pyramids

## Finding
For every integer \(n\ge5\) and real height \(h>0\), let \(P_{n,h}\subset\mathbb R^3\) be the right pyramid with unit-circumradius regular \(n\)-gon base in \(z=0\) and apex \((0,0,h)\). Sample an unoriented orthographic projection plane by Haar measure, and let \(p_n(h)\) be the probability that all \(n+1\) vertices of \(P_{n,h}\) remain vertices of the projected convex hull.

Put
\[
 c=\cos(\pi/n),\quad s=\sin(\pi/n),\quad q=\cos(2\pi/n),\quad d=c/q,
\]
where \(q>0\), and define
\[
 D_n(x)=(1+q+2x)\sqrt{x+d^2}+2(cd+x)\sqrt{x+1}.
\]
Then the **exact probability** is
\[
 \boxed{p_n(h)=\frac n\pi\arctan\!\left(\frac{2s(d-c)h}{D_n(h^2)}\right).}
\]
For each \(n\ge5\), there is exactly one optimal height \(h_n>0\); \(p_n\) increases strictly on \((0,h_n)\), decreases strictly on \((h_n,\infty)\), and tends to zero at both endpoints. The number \(x_n=h_n^2\) is the unique positive solution of
\[
 \boxed{
 \frac{4x^2+2d^2x-(1+q)d^2}{\sqrt{x+d^2}}
 +\frac{4x^2+2x-2cd}{\sqrt{x+1}}=0.}
\]
The sharp many-sided laws are
\[
 \boxed{\lim_{n\to\infty}h_n=\frac1{\sqrt2},\qquad
 \lim_{n\to\infty}n^2p_n(h_n)=\frac{2\pi^2}{3\sqrt3}.}
\]
For the regular hexagonal base, the optimum simplifies exactly to
\[
 \boxed{h_6=\sqrt{\frac35},\qquad p_6(h_6)=\frac6\pi\arctan\frac{\sqrt2}{22}.}
\]

## Assumptions and scope
The base is a regular Euclidean polygon of circumradius one; multiplying all base lengths and the height by the same positive factor does not change the probability. Projection directions are uniform on the sphere, with opposite vectors defining the same projection plane. Statements are almost sure: directions causing coincident projected vertices or collinearities form measure-zero sets. For \(n=3\) or \(n=4\), the key one-edge visibility regions are unbounded, so those dimensions are deliberately excluded; the theorem makes no claim about their optimal heights.

## Proof
**Step 1: Reduce a three-dimensional shadow to a planar point addition.** Write the base as \(B_n\subset\mathbb R^2\), with vertices \((\cos(2\pi j/n),\sin(2\pi j/n))\). For a unit viewing vector \(u=(u_x,u_y,u_z)\) with \(u_z\ne0\), the restriction of orthogonal projection along \(u\) to the base plane is an invertible linear map onto the projection plane. Under that identification, the apex projects to
\[
 Q=-\frac h{u_z}(u_x,u_y)\in\mathbb R^2.
\]
Consequently, the shadow has \(n+1\) extreme vertices precisely when the planar hull \(\operatorname{conv}(B_n\cup\{Q\})\) contains all original polygon vertices plus \(Q\) as extreme points.

A base edge with outward unit normal \(v_j\) is visible from \(Q\) exactly when \(Q\cdot v_j>c\), since every base side has support number \(c=\cos(\pi/n)\). The visible edges form a single consecutive boundary chain for an exterior point. If zero sides are visible, \(Q\) is inside and adds no vertex. If exactly one side is visible, \(Q\) adds one vertex without suppressing any polygon vertex. If at least two sides are visible, their common intermediate vertex or vertices cease to be extreme. Thus the event of interest is **exactly one violated side-support inequality**.

**Step 2: Identify its exact planar cells.** Rotate so a selected side has outward normal \((1,0)\). Its endpoints are \((c,\pm s)\). The corresponding one-visible-side region is the open triangle with those endpoints and third vertex \((d,0)\), where \(d=c/q\) and \(q=\cos(2\pi/n)>0\). Indeed, the selected inequality reads \(X>c\); the two neighboring nonviolated inequalities read
\[
 qX\pm\sin(2\pi/n)Y<c.
\]
Their intersection is just that triangle. Each of the other support inequalities holds throughout the triangle: it holds at both original base vertices, and at \((d,0)\) because \(d\cos(2\pi k/n)\le dq=c\) for every nonzero index modulo \(n\); use convexity. Different rotated triangles have disjoint interiors. This positive-area triangular-cell mechanism begins precisely at \(n=5\).

**Step 3: Integrate the viewing directions.** On either hemisphere, the change of variables from \(u\) to \(Q\) has the two-dimensional Cauchy density
\[
 f_h(X,Y)=\frac{h}{2\pi\bigl(h^2+X^2+Y^2\bigr)^{3/2}}.
\]
Hence \(p_n(h)\) is \(n\) times the integral of this density over one of the triangles. That integral is the triangle's solid angle \(\Omega\), viewed from \((0,0,h)\), divided by \(2\pi\).

For the triangle with vertices \((c,s,0)\), \((c,-s,0)\), \((d,0,0)\), the three vectors from \((0,0,h)\) have lengths \(\sqrt{1+h^2}\), \(\sqrt{1+h^2}\), \(\sqrt{d^2+h^2}\). Their absolute scalar triple product is \(2s(d-c)h\). The sum of the triple product of lengths and the three dot-product-times-opposite-length terms equals
\[
 (1+q+2h^2)\sqrt{d^2+h^2}+2(cd+h^2)\sqrt{1+h^2}=D_n(h^2).
\]
The standard spherical-triangle identity \(\Omega=2\arctan(\lvert\det\rvert/\text{denominator})\), with positive denominator here, proves the displayed exact expression for \(p_n(h)\). The same identity can be checked independently by the elementary surface integral \(\Omega=\int_T h(h^2+X^2+Y^2)^{-3/2}\,dX\,dY\).

**Step 4: Prove global uniqueness without numerical optimization.** With \(x=h^2\), maximizing \(p_n(h)\) is equivalent to maximizing \(\sqrt x/D_n(x)\). For positive \(a,b,t\), define \(G(x)=(a+bx)\sqrt{x+t}\). Direct differentiation gives
\[
 2xG'(x)-G(x)=\frac{2bx^2+btx-at}{\sqrt{x+t}},
\]
and the derivative of the right-hand side equals
\[
 \frac{3bx^2+\frac92 btx+bt^2+\frac12at}{(x+t)^{3/2}}>0
 \qquad(x\ge0).
\]
Now \(D_n=G_1+G_2\) with \((a,b,t)=(1+q,2,d^2)\) and \((2cd,2,1)\). It follows that \(H_n(x)=2xD_n'(x)-D_n(x)\) is strictly increasing on \([0,\infty)\), is negative at zero, and tends to positive infinity. Its displayed radical expression has one positive zero \(x_n\), and \(\sqrt{x}/D_n(x)\) has derivative with sign \(-H_n(x)\). Thus the global maximizer exists, is unique, and has the asserted strict monotonicity. The formula also immediately gives \(p_n(h)\to0\) as \(h\to0\) and \(h\to\infty\).

**Step 5: Exact benchmark and many-sided asymptotics.** For \(n=6\), substitute \(c=\sqrt3/2\), \(s=1/2\), \(q=1/2\), and \(d=\sqrt3\). Direct substitution shows \(H_6(3/5)=0\); uniqueness establishes \(x_6=3/5\). Simplifying the solid-angle ratio at this height gives \(\sqrt2/22\).

As \(n\to\infty\), the defining constants tend to \(c=q=d=1\), and \(H_n(x)\) tends uniformly on compact \(x\)-intervals to
\[
 4(2x-1)\sqrt{x+1}.
\]
For all \(n\ge5\), the zero of \(H_n\) lies in a fixed compact positive interval (for example, \(H_n(0)<0\) and \(H_n(10)>0\), using \(d\le\cos(\pi/5)/\cos(2\pi/5)<3\)). Strict monotonicity therefore yields \(x_n\to1/2\). Finally, with \(\beta=\pi/n\), elementary Taylor expansions give
\[
 s(d-c)\sim2\beta^3,\qquad
 D_n(x)\longrightarrow4(1+x)^{3/2}.
\]
Using \(\arctan z\sim z\) and \(h_n\to1/\sqrt2\) in the exact probability formula proves the stated constant \(2\pi^2/(3\sqrt3)\).

## Verification
Run `python CHECK.py` using Python 3.10 or newer. The script independently computes triangle solid angles from raw vectors, reconstructs 21,000 projected hulls using a two-dimensional convex-hull algorithm, compares their vertex classifications against polygon support inequalities, checks the exact hexagonal benchmark numerically, and evaluates the asymptotic limit. These finite tests are supporting calculations; the universal claims are proved by the preceding convex-geometric and derivative arguments.

## Relationship to prior work
Glisse and Lazard (2007) analyze expected silhouette complexity of approximating polyhedral surfaces and prove upper bounds, not an exact all-vertex probability or optimal height for a fixed regular pyramid. Glisse, Lazard, Michel, and Pouget (2016) study maxima of silhouettes for Poisson random polytopes, not the present deterministic family with a random projection direction. Böröczky and Henk (1997) obtain expected face-count asymptotics for regular simplices and cross-polytopes rather than an all-vertex probability for variable-height polygonal pyramids. Van Oosterom and Strackee's 1983 solid-angle identity is a standard evaluation tool and by itself does not classify the one-visible-side projection regions or optimize their integrated probabilities. A published exact five-vertex shadow theorem for right rectangular pyramids covers quadrilateral bases, whose one-visible-edge regions are unbounded; it neither covers the triangular-cell regime \(n\ge5\) nor implies the unique height and sharp inverse-square limit here.

## Limitations
This theorem concerns orthographic projections, Haar-uniform directions, a centered apex, and regular planar bases of fixed circumradius. It gives the probability that **all** vertices appear, not the complete law of lesser silhouette sizes. Uncentered apices, other bases, and perspective projections remain outside the claim. Establishing complete historical priority would require checking additional specialized projection literature. The result has received no independent mathematical validation.

## References
1. M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, public preprint dated 14 February 2007, arXiv:cs/0702087, https://arxiv.org/abs/cs/0702087.
2. M. Glisse, S. Lazard, J. Michel, and M. Pouget, *Silhouette of a random polytope*, Journal of Computational Geometry 7 (2016), 86–99, https://doi.org/10.20382/jocg.v7i1a5.
3. A. van Oosterom and J. Strackee, *The Solid Angle of a Plane Triangle*, IEEE Transactions on Biomedical Engineering 30 (1983), 125–126, https://doi.org/10.1109/TBME.1983.325207.
4. K. Böröczky Jr. and M. Henk, *Random Projections of Regular Polytopes*, preprint SC 97-21 (May 1997), https://page.math.tu-berlin.de/~henk/preprints/boeroeczky%20henk%26random%20projections%20of%20regular%20polytopes.pdf.
