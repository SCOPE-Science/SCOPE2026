# A near-sharp vertex-perturbation bound for planar simplex strength

## Finding

For any ordered triple \(T=(P_0,P_1,P_2)\) of points of the Euclidean plane, let \(A(T)\) be its ordinary (nonnegative) area, \(p(T)=(|P_0-P_1|+|P_1-P_2|+|P_2-P_0|)/2\) its semiperimeter, and set \(\sigma(T)=A(T)^2/p(T)^3\) when \(p(T)>0\), and \(\sigma(T)=0\) otherwise. Let \(s(T)=\operatorname{sgn}\det(P_1-P_0,P_2-P_0)\,\sigma(T)\), with zero sign at degeneracy.

**Theorem.** For any pair \(T,T'\) of ordered planar triangles having two corresponding vertices identical and the remaining vertices separated by at most \(\varepsilon\),
\[
|\sigma(T)-\sigma(T')|\le\frac{3}{32}\varepsilon,
\qquad |s(T)-s(T')|\le\frac{3}{32}\varepsilon.
\]
If all three corresponding vertices are separated by at most \(\varepsilon\), then both bounds hold with \(9\varepsilon/32\) in place of \(3\varepsilon/32\).

If \(L_*\) is the smallest universal coefficient for **one** moving vertex, then
\[
\boxed{\frac{567}{4}-\frac{2043\sqrt{13}}{52}\ \le L_*\le\frac{3}{32}}.
\]
The lower endpoint is approximately \(0.0934373889821\), the upper endpoint is \(0.09375\), and the relative gap to the upper endpoint is less than \(1/250\). The exact value of \(L_*\) is not determined.

## Assumptions and scope

All distances are Euclidean, vertex correspondences are fixed, triangles are allowed to be collinear or to have repeated vertices, and the conventions above assign strength zero to a triple of coincident points. The bounds are global; there is no lower bound on triangle altitude or edge length. Reflection changes the sign of \(s\) but not \(\sigma\). No statement about dimension above two is made.

## Proof

**1. Reduction and elliptic coordinates.** For one moving vertex, if the fixed base endpoints coincide, both strengths vanish. Otherwise scale and rigidly move the fixed endpoints to \((0,0)\) and \((1,0)\). Strength is homogeneous of degree one, hence the Euclidean apex gradient is invariant under this normalization. In the upper half-plane write the apex as \((x,y)\) with \(y>0\). Put
\[
b=\sqrt{x^2+y^2},\quad c=\sqrt{(x-1)^2+y^2},\quad u=b+c>1,\quad v=b-c,\quad |v|<1.
\]
The standard elliptic-coordinate relations and the area and semiperimeter are
\[
x=\frac{1+uv}{2},\qquad y=\frac12\sqrt{(u^2-1)(1-v^2)},\qquad
 A=\frac y2,\qquad p=\frac{u+1}{2}.
\]
Consequently
\[
\sigma(u,v)=\frac{(u-1)(1-v^2)}{2(u+1)^2}.
\]
The coordinate directions are orthogonal; their squared Euclidean scale factors are \((u^2-v^2)/(4(u^2-1))\) and \((u^2-v^2)/(4(1-v^2))\). Differentiation therefore yields the exact apex-gradient identity
\[
|\nabla_{(x,y)}\sigma|^2=
\frac{(u-1)(1-v^2)\left[(u-3)^2(1-v^2)+4(u^2-1)v^2\right]}{(u+1)^5(u^2-v^2)}.\tag{1}
\]

**2. A rational positivity certificate.** Put \(t=u-1>0\), \(w=v^2\in[0,1)\), and \(z=w/(1-w)\ge0\). Since every denominator in (1) is positive, the desired inequality \(|\nabla\sigma|^2\le9/1024\) is equivalent to
\[
P(t,z)=P_0(t)+zP_1(t)+z^2P_2(t)\ge0,
\]
where
\[
\begin{aligned}
P_0(t)&=9t^7+108t^6+549t^5+1530t^4+1496t^3+6544t^2-2800t+288,\\
P_1(t)&=(t+2)(18t^6+180t^5+729t^4+1512t^3-2440t^2+864t+144),\\
P_2(t)&=9t(t+2)^6.
\end{aligned}
\]
Here \(P_2(t)\ge0\) for \(t\ge0\). Both \(P_0(t+1/2)\) and \(P_1(t+1/2)\) have strictly positive power-series coefficients, proving positivity of the first two polynomials for \(t\ge1/2\). For \(0\le t\le1/2\), subdivide into eight intervals \([j/16,(j+1)/16]\), \(j=0,\ldots,7\). The Bernstein coefficients of degree seven, computed exactly as rational numbers for each polynomial on each interval, are all strictly positive. The smallest such coefficient for \(P_0\) is \(1718469527/469762048\), and for \(P_1\) it is \(288\). Positivity of the Bernstein basis on each interval finishes the proof of \(|\nabla\sigma|\le3/32\). An accompanying standalone exact-arithmetic checker reconstructs the expressions, intervals, and minimum coefficients; these are finite algebraic tests, not numerical inference from samples.

**3. Global and signed bounds.** In the lower half-plane the same gradient norm applies by reflection. At a collinear apex the squared-area factor vanishes at least quadratically in altitude, while \(p\ge1/2\) for the normalized nonzero base. Thus \(\sigma\) and \(s\) extend continuously with zero transverse derivative; any possible nondifferentiability of individual distance terms when the apex meets a fixed endpoint is killed by the squared-area factor. Equivalently these functions are absolutely continuous on every straight apex path and have almost-everywhere gradient norm at most \(3/32\). Integrating their directional derivatives proves both one-vertex inequalities. Moving vertices sequentially from \(T\) to \(T'\), one at a time, proves the three-vertex bound by the triangle inequality.

**4. Near-sharp witness.** Keep the unit base endpoints \((0,0)\) and \((1,0)\) fixed and consider \(P_2=(1/2,y)\), \(y>0\). Then
\[
\sigma(y)=\frac{y^2}{4\left(\frac12+\sqrt{1/4+y^2}\right)^3}.
\]
Direct differentiation at \(y=1/3\) gives
\[
\sigma'(1/3)=\frac{567}{4}-\frac{2043\sqrt{13}}{52}>0.
\]
An arbitrarily short vertical movement of this apex has strength change divided by displacement tending to the displayed derivative, proving the lower bound on \(L_*\). The same witness applies to signed strength.

## Verification

Run `python checker.py` with Python 3 and SymPy installed. The checker independently differentiates the elliptic-coordinate formula, reconstructs \(P(t,z)\), verifies every polynomial coefficient exactly, checks nonnegative shifted-power coefficients on the tail and all \(128\) strictly positive rational Bernstein coefficients on the eight subintervals, and derives the exact witness derivative. It prints `PASS` on success. The independent proof of why these finite tests suffice appears in Section 2 above.

## Relationship to prior work

Kurlin (2023) introduced simplex strength as part of continuous point-cloud isometry descriptors and established a dimension-dependent Lipschitz estimate. Anosova and Kurlin (2026), Theorem 2.8(b), provide a global bound of \(2\sqrt3\,\varepsilon\) for triangle strength when all three vertices move by at most \(\varepsilon\). The present theorem bounds the same normalized strength and signed strength by \(9\varepsilon/32\) under those hypotheses, and proves the stronger near-sharp bound for the intrinsic one-vertex perturbation problem. The contribution is the substantially improved constant and algebraic near-optimality bracket, not the definition of strength or its qualitative Lipschitz continuity.

## Limitations

The coefficient \(3/32\) is proved valid but not claimed optimal. The true one-vertex optimum lies in the displayed narrow interval; determining it exactly remains open here. The three-vertex coefficient \(9/32\) is obtained by telescoping and is not claimed sharp. No finite collection of sampled triangles alone would justify the global inequality; the rational polynomial-positivity certificate is essential. Independent validation has not been performed.

## References

1. O. Anosova and V. Kurlin, *The strength of a geometric simplex is a key ingredient in a polynomial-time classification of unordered point clouds by Lipschitz continuous invariants*, arXiv:2602.17630 (first publicly posted 2026-02-19), Theorem 2.8(b), https://arxiv.org/abs/2602.17630.
2. V. Kurlin, *The strength of a simplex is the key to a continuous isometry classification of Euclidean clouds of unlabelled points*, arXiv:2303.13486 (2023), Definition 4.1 and Theorem 4.2, https://arxiv.org/abs/2303.13486.
