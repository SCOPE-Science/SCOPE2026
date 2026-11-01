# Sharp Minkowski asymmetry and golden-ratio envelope of Euclidean ball slabs

## Finding

Fix an integer \(d\ge 2\), a unit vector \(e\in\mathbb R^d\), and real numbers \(-1\le \ell<u\le1\). Let
\[
K_{\ell,u}=\{x\in\mathbb R^d:\|x\|_2\le1,\ \ell\le\langle x,e\rangle\le u\}.
\]
For a full-dimensional convex body \(K\), its Minkowski asymmetry is
\[
s(K)=\inf\{\rho\ge1:-(K-c)\subseteq \rho(K-c)\text{ for some }c\in\mathbb R^d\}.
\]
The complete profile, including **all** minimizing centers, is as follows.

If \(\ell+u=0\), then \(s(K_{\ell,u})=1\) and the unique minimizing center is the origin. If \(\ell+u>0\), let \(\sigma\) be the unique number in \((1,\varphi)\), with \(\varphi=(1+\sqrt5)/2\), satisfying
\[
(1-\ell^2)\sigma^2-2\ell(u-\ell)\sigma-(1+u^2-2\ell u)=0.\tag{1}
\]
Then \(s(K_{\ell,u})=\sigma\), and its **unique** Minkowski center is
\[
c_{\ell,u}=\frac{u+\sigma\ell}{1+\sigma}\,e.\tag{2}
\]
If \(\ell+u<0\), reflect the pair to \((-u,-\ell)\): the asymmetry is unchanged and the center is the negative of (2) for that reflected pair.

Every nondegenerate Euclidean ball slab therefore satisfies the sharp, dimension-independent bound
\[
1\le s(K_{\ell,u})<\varphi.\tag{3}
\]
The upper endpoint is the **unattained supremum**: already the caps \(K_{\ell,1}\) have strictly increasing asymmetry as \(\ell\uparrow1\), converging to \(\varphi\). At the hemisphere \(K_{0,1}\), the value is exactly \(\sqrt2\).

There is a further exact optimization for a **fixed upper cutting level** \(u\in(0,1)\) among slabs with \(-u\le\ell<u\). There exists a unique \(S_u\in(1,\varphi)\) determined by
\[
S_u(2-S_u)(S_u^2-1)=u^2.\tag{4}
\]
The sharp inequality and its unique equality case are
\[
s(K_{\ell,u})\le S_u,
\qquad
s(K_{\ell,u})=S_u\ \Longleftrightarrow\
\ell=\frac{u(S_u-1)}{S_u(2-S_u)}.\tag{5}
\]
In particular, the most asymmetric slab with a specified upper cut is generally **not** a one-sided cap or a zero-centered slab; it has a unique, explicitly prescribed second cutting level. Formula (4) reduces the optimizer to a strictly monotone quartic on \([1,\varphi]\).

## Assumptions and scope

The bodies are intersections of the closed Euclidean unit ball with two parallel, possibly redundant, halfspaces. They are full-dimensional because \(\ell<u\) and the interval intersects \((-1,1)\). The cutting levels are measured relative to the ball's center and radius. The result is invariant under invertible affine maps, hence also applies to corresponding parallel slabs of ellipsoids, after normalizing to a ball.

The reflection-dilation convention uses \(s(K)\ge1\), rather than its reciprocal \(\operatorname{sym}(K)=1/s(K)\). Values \(s=1\) correspond exactly to central symmetry.

## Proof

**1. Reduction and existence of the quadratic root.** Reflection in the hyperplane orthogonal to \(e\) sends \(K_{\ell,u}\) to \(K_{-u,-\ell}\), so assume \(\ell+u>0\). Necessarily \(-1<\ell<u\le1\). Define
\[
F_{\ell,u}(r)=(1-\ell^2)r^2-2\ell(u-\ell)r-(1+u^2-2\ell u).
\]
Then \(F_{\ell,u}(1)=\ell^2-u^2<0\). Its derivative is
\[
F'_{\ell,u}(r)=2(1-\ell^2)r-2\ell(u-\ell),
\qquad F'_{\ell,u}(1)=2(1-\ell u)>0.
\]
Thus it increases strictly for \(r\ge1\). At \(r=\varphi\), use \(\varphi^2=\varphi+1\) to obtain the exact identity
\[
F_{\ell,u}(\varphi)=\varphi(1-u^2)+\frac{(u-\ell)^2}{\varphi}>0.\tag{6}
\]
There is exactly one root \(\sigma\in(1,\varphi)\).

**2. Positive axial translation.** Put \(C=u+\sigma\ell\). If \(\ell\ge0\), clearly \(C>0\). If \(\ell<0\), the assumed \(u> -\ell\) gives \(r_0=u/(-\ell)>1\). At this value \(u+r_0\ell=0\), and direct substitution yields \(F_{\ell,u}(r_0)=r_0^2-1>0\). Since \(F\) increases on \([1,\infty)\), \(\sigma<r_0\), whence \(C>0\).

**3. Matching containment.** Take the candidate center \(c=C e/(1+\sigma)\) and write the reflected-dilated image of a point \(p\in K_{\ell,u}\) as \(q=(Ce-p)/\sigma\). Its axial coordinate obeys
\[
\frac{C-u}{\sigma}=\ell\le\langle q,e\rangle
\le\frac{C-\ell}{\sigma}\le u,
\]
where the last inequality is equivalent to \((\sigma-1)(u-\ell)\ge0\). For the ball constraint, because \(C>0\),
\[
\|Ce-p\|_2^2=\|p\|_2^2+C^2-2C\langle p,e\rangle
\le1+C^2-2C\ell=\sigma^2.\tag{7}
\]
The last equality is precisely \(F_{\ell,u}(\sigma)=0\). Thus \(q\in K_{\ell,u}\), proving \(s(K_{\ell,u})\le\sigma\).

**4. Optimality and uniqueness of the center.** Suppose \(r\in[1,\sigma]\) and \(-(K_{\ell,u}-z)\subseteq r(K_{\ell,u}-z)\). Write \((1+r)z=T e+w\), with \(w\perp e\). The uppermost point \(ue\) of the axial coordinate range implies \(T\ge u+r\ell\). On the lower circular rim, whose transverse radius is \(R=\sqrt{1-\ell^2}>0\), select the transverse unit direction opposite to \(w\). Containment in the enlarged Euclidean ball forces
\[
r^2\ge (T-\ell)^2+(R+\|w\|_2)^2.\tag{8}
\]
Because \(u+(r-1)\ell>0\) for \(1\le r\le\sigma<2\) (immediate if \(\ell\ge0\); for \(\ell<0\) use \(u> -\ell\)), the right side is at least
\[
\bigl(u+(r-1)\ell\bigr)^2+1-\ell^2.
\]
Hence \(F_{\ell,u}(r)\ge0\), impossible for \(r<\sigma\). At \(r=\sigma\), equality in (8) and (7) forces \(T=C\) and \(w=0\). Consequently (2) is the only minimizing center. The case \(\ell+u=0\) is centrally symmetric with unique center zero, while reflection handles \(\ell+u<0\).

**5. Sharp fixed-cut envelope.** For \(1<r<2\), complete the square exactly:
\[
F_{\ell,u}(r)=r(2-r)\left(\ell-\frac{u(r-1)}{r(2-r)}\right)^2
+(r^2-1)-\frac{u^2}{r(2-r)}.\tag{9}
\]
Put \(g(r)=r(2-r)(r^2-1)\). Its derivative factors as
\[
g'(r)=2(2r-1)(1+r-r^2)>0\quad(1\le r<\varphi),
\]
and \(g(1)=0\), \(g(\varphi)=1\). Thus (4) has exactly one \(S_u\in(1,\varphi)\). Substituting \(r=S_u\) into (9) gives
\[
F_{\ell,u}(S_u)=S_u(2-S_u)\left(\ell-\frac{u(S_u-1)}{S_u(2-S_u)}\right)^2\ge0.
\]
Because \(F_{\ell,u}\) increases on \([1,\infty)\), its root is at most \(S_u\), and equality holds precisely at the stated lower cut. The optimizer lies strictly between \(0\) and \(u\), since \(S_u<\varphi\). This proves (4)–(5). For \(u=1\), (6) and the cap specialization show that the supremum \(\varphi\) is approached only as the two cuts coalesce at the pole; the full-dimensional upper bound remains strict.

**6. One-sided caps and endpoint.** For \(u=1\), (1) factors by \(1-\ell\), giving
\[
(1+\ell)\sigma^2-2\ell\sigma-2=0,
\qquad
\sigma=\frac{\ell+\sqrt{\ell^2+2\ell+2}}{1+\ell},\quad -1<\ell<1.
\]
Implicit differentiation gives
\[
\frac{d\sigma}{d\ell}=
\frac{\sigma(2-\sigma)}{2(1+\ell)\sigma-2\ell}>0.
\]
Hence \(\sigma\to\varphi\) as \(\ell\uparrow1\), while \(\sigma=\sqrt2\) at \(\ell=0\). The entire-ball endpoint \((\ell,u)=(-1,1)\) is centrally symmetric and has asymmetry one.

## Verification

The accompanying `check.py` independently constructs planar convex polygons from clipped circular arcs, computes their asymmetry and centers using a linear program on all facet normals, and compares them with the formulas for fourteen slab configurations. It also checks five explicit lower-rim contact certificates, a symbolic factorization of (9), and the six fixed-cut optimizer regimes. Run with `python check.py` in an environment with Python, NumPy, SciPy, and SymPy. All checks returned `ALL_CHECKS_PASSED`. The polygonal approximations are finite diagnostics; the proof above, not the numerical calculation, establishes the universal all-dimensional statements.

## Relationship to prior work

The Minkowski center is classical. Den Hertog, Pauphilet and Soali (first public preprint January 19, 2022) give a robust-optimization characterization and exact examples for orthant norm balls and packing-type sets. Their optimization framework motivates an explicit closed-form benchmark; their table and relevant sections do not state a profile for a Euclidean ball clipped by two arbitrary parallel hyperplanes. Brandenberg, von Dichter and González Merino (arXiv first public June 20, 2023) study inequalities linking Minkowski asymmetry to symmetrizations, including a planar golden-ratio threshold for a different additional invariant. Their dimension-two implication does not yield the exact two-parameter slab profile, the all-dimensional unique-center formula or the fixed-upper-cut envelope (4)–(5). The same golden-ratio constant appears here through a direct geometric contact identity, not through a claimed improvement to their general theorem.

## Limitations

The cuts must be parallel and the ambient body an ellipsoid up to an affine transformation. Nonparallel cuts and general uniformly convex bodies are not covered. The supremum \(\varphi\) is not attained by a full-dimensional slab. No statement is made about computational optimality, perturbation robustness, or historical priority beyond the inspected sources; specialized earlier formulas may exist. The quoted checker uses polygonal discretization and is not an exhaustive proof of the continuum theorem.

## References

1. D. den Hertog, J. Pauphilet, M. Y. Soali, *Minkowski Centers via Robust Optimization: Computation and Applications*, first public at Optimization Online on January 19, 2022, https://optimization-online.org/2022/01/8768/ ; full-text https://optimization-online.org/wp-content/uploads/2022/01/Minkowski_Final-1.pdf ; *Operations Research* **72** (2024), 2135–2152.
2. R. Brandenberg, K. von Dichter, B. González Merino, *From inequalities relating symmetrizations of convex bodies to the diameter-width ratio for complete and pseudo-complete convex sets*, arXiv:2306.11460, first public June 20, 2023, https://arxiv.org/abs/2306.11460 ; the arXiv version and published article concern different general symmetry relations.
