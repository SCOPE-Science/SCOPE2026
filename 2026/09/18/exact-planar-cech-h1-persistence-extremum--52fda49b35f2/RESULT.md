# Exact planar Čech \(H_1\) persistence extremum

## Statement

Let \(P\subset\mathbb R^2\) be a finite set of \(m\ge 3\) points, and use
\(\mathbb Z_2\)-coefficients. For a nonzero interval \([b,d)\) in the
one-dimensional persistent homology of the Euclidean Čech filtration of \(P\),
write its multiplicative persistence as \(d/b\). Then

\[
\boxed{\frac d b\le \csc\frac{\pi}{m}.}
\]

The bound is sharp for every \(m\): the vertices of a regular \(m\)-gon have an
\(H_1\) interval

\[
\left[\sin\frac{\pi}{m},\,1\right)
\]

after normalizing the circumradius to \(1\). Consequently,

\[
\boxed{
\sup_{|P|=m}\Pi_1(P)=\csc\frac{\pi}{m},
}
\]

where \(\Pi_1(P)\) is the largest death-to-birth ratio in \(H_1\).

Equivalently, if \(N_\rho^{(1)}(2)\) is the least number of planar points needed
to support a Čech \(H_1\) interval of multiplicative persistence at least
\(\rho>1\), then

\[
\boxed{
N_\rho^{(1)}(2)
=
\left\lceil
\frac{\pi}{\arcsin(1/\rho)}
\right\rceil .
}
\]

Thus the asymptotic threshold \(N_\rho^{(1)}(2)\sim\pi\rho\) has an exact
finite-\(\rho\) formula in the planar one-cycle case.

## Context

Bobrowski and Skraba recently isolated the deterministic extremal problem behind
large-persistence random Čech cycles: how many points are required to support a
cycle with prescribed death-to-birth ratio? They prove, for \(1\le k<d\), the
asymptotic law

\[
N_\rho^{(k)}
\sim \mu_k^{\mathrm{cov}}\,s_k\,\rho^k
\qquad (\rho\to\infty),
\]

with \(\mathbb Z_2\)-coefficients, where the constant is governed by optimal
sphere covering. Their proof uses a sharp filling-radius inequality and a
compactness argument. In the case \(k=1,d=2\),
\(\mu_1^{\mathrm{cov}}s_1=\pi\), so their asymptotic statement gives
\(N_\rho^{(1)}(2)\sim\pi\rho\).

The theorem above determines the complete finite extremal function in this
special case. The proof uses a planar representative of a persistent class,
an exact persistence-to-filling-radius estimate, and the sharp perimeter bound
for a polygon surrounding a disk.

## Proof

### 1. Reduction to a simple planar polygon

First assume that \(P\) is in general position. Use the planar alpha filtration,
equivalently the Delaunay--Čech filtration. It has the same persistent homology
as the Čech filtration at the same radius, while its geometric one-skeleton is
planar.

Fix an interval \([b,d)\) and a scale \(t\) with

\[
b<t<d.
\]

Choose a one-cycle \(z\) in the alpha complex at scale \(t\) representing the
interval class. Over \(\mathbb Z_2\), the edge support of \(z\) decomposes into
finitely many edge-disjoint simple cycles. If every simple-cycle summand became
null before \(d\), then at the largest of their finitely many death scales their
sum would also be null, contradicting persistence of the chosen class to
\(d\). Hence one summand, denoted \(C\), survives to a scale

\[
d_C\ge d.
\]

Because the alpha one-skeleton is planar, \(C\) is a simple polygonal Jordan
curve. Let it have \(q\le m\) vertices. Every edge of the alpha complex present
at scale \(t\) has Euclidean length at most \(2t\); therefore its perimeter
satisfies

\[
L(C)\le 2qt.
\]

### 2. An exact persistence-to-filling-radius lower bound

Let \(r(C)\) be the largest radius of a Euclidean disk contained in the bounded
component of \(\mathbb R^2\setminus C\). For a Jordan polygon this is also its
Euclidean filling radius: \(C\) cannot bound inside its \(\delta\)-neighborhood
when \(\delta<r(C)\), because a point of the enclosed disk is omitted and has
winding number one; while for every \(\delta>r(C)\), the whole polygonal
interior lies in that neighborhood.

For every \(\delta>0\),

\[
B_\delta(C)
\subset
B_{\sqrt{t^2+\delta^2}}\bigl(V(C)\bigr),
\]

where \(V(C)\) is the vertex set of \(C\). Indeed, if a nearest point on \(C\)
lies in the interior of an edge, one of the two endpoints is at along-edge
distance at most half the edge length, hence at most \(t\); the perpendicular
distance is at most \(\delta\). If the nearest point is an endpoint, the claim
is immediate.

Suppose

\[
r(C)<\sqrt{d_C^2-t^2}.
\]

Choose
\[
r(C)<\delta<\sqrt{d_C^2-t^2}.
\]
Then the polygonal interior of \(C\) is contained in \(B_\delta(C)\), hence in
the union of balls of radius

\[
s=\sqrt{t^2+\delta^2}<d_C
\]

around the vertices of \(C\), and therefore in the union of radius-\(s\) balls
around \(P\). Thus \(C\) is already null-homologous before \(d_C\), a
contradiction. Consequently,

\[
\boxed{
r(C)\ge \sqrt{d_C^2-t^2}\ge \sqrt{d^2-t^2}.
}
\]

This is the exact planar version of the persistence-to-filling-radius estimate
that appears asymptotically in the recent persistent-isoperimetric argument.

### 3. The sharp polygonal filling-radius upper bound

We claim that every simple \(q\)-gon \(C\) of perimeter \(L\) satisfies

\[
r(C)\le
\frac{L}{2q\tan(\pi/q)}.
\]

Let \(K=\operatorname{conv}(C)\). Any disk contained in the interior of \(C\)
is also contained in \(K\), and

\[
\operatorname{per}(K)\le L.
\]

If a convex polygon with at most \(q\) sides contains a disk of radius \(r\),
then its perimeter is at least

\[
2qr\tan\frac{\pi}{q}.
\]

For completeness, move each supporting line inward until it is tangent to the
disk. Perimeter can only decrease. If the resulting tangent polygon has
\(h\le q\) sides and successive outward-normal angle gaps
\(\theta_1,\ldots,\theta_h\), then \(\sum_i\theta_i=2\pi\) and

\[
\operatorname{per}
=
2r\sum_{i=1}^h\tan\frac{\theta_i}{2}
\ge
2rh\tan\frac{\pi}{h}
\ge
2rq\tan\frac{\pi}{q}.
\]

The first inequality is Jensen's inequality, and
\(x\tan(\pi/x)\) is decreasing for \(x\ge3\). Applying this to \(K\) gives the
claim. Since \(L(C)\le 2qt\),

\[
\boxed{
r(C)\le t\cot\frac{\pi}{q}.
}
\]

### 4. The persistence bound

Combining the two estimates,

\[
\sqrt{d^2-t^2}
\le
t\cot\frac{\pi}{q}.
\]

Hence

\[
\frac d t
\le
\sqrt{1+\cot^2\frac{\pi}{q}}
=
\csc\frac{\pi}{q}
\le
\csc\frac{\pi}{m}.
\]

Letting \(t\downarrow b\) yields

\[
\boxed{
\frac d b\le\csc\frac{\pi}{m}.
}
\]

### 5. Removing general position

For an arbitrary \(m\)-point set \(P\), perturb the labeled points by at most
\(\varepsilon\) to obtain a general-position set \(P_\varepsilon\). The two
offset filtrations satisfy

\[
B_r(P)\subset B_{r+\varepsilon}(P_\varepsilon),
\qquad
B_r(P_\varepsilon)\subset B_{r+\varepsilon}(P),
\]

so their Čech persistence modules are \(\varepsilon\)-interleaved. For any
positive-length interval \([b,d)\) of \(P\), barcode stability gives, for all
sufficiently small \(\varepsilon\), a matched interval
\([b_\varepsilon,d_\varepsilon)\) with

\[
b_\varepsilon\to b,\qquad d_\varepsilon\to d.
\]

Applying the general-position bound to \(P_\varepsilon\) and taking
\(\varepsilon\to0\) proves the same inequality for every finite planar point
set.

### 6. Sharpness: the regular polygon

Take the vertices of a regular \(m\)-gon of circumradius \(1\). Its side length
is

\[
2\sin\frac{\pi}{m}.
\]

Thus neighboring radius-\(r\) disks first meet at

\[
b=\sin\frac{\pi}{m}.
\]

For every \(b\le r<1\), the polygonal boundary is contained in the union of the
radius-\(r\) disks, while the center of the polygon is not. By Jordan
separation, the union has a bounded complementary component and therefore
nontrivial \(H_1\). At \(r=1\), all disks contain the center, so their union is
star-shaped with respect to the center and has trivial \(H_1\). Hence the
corresponding interval is exactly

\[
\left[\sin\frac{\pi}{m},1\right),
\]

with ratio \(\csc(\pi/m)\).

### 7. Exact point threshold

A persistence ratio at least \(\rho>1\) is possible with \(m\) points if and
only if

\[
\csc\frac{\pi}{m}\ge\rho.
\]

Since \(m\ge3\) and \(\sin\) is increasing on \((0,\pi/2]\), this is equivalent
to

\[
m\ge\frac{\pi}{\arcsin(1/\rho)}.
\]

Taking the least integer proves

\[
N_\rho^{(1)}(2)
=
\left\lceil\frac{\pi}{\arcsin(1/\rho)}\right\rceil.
\]

The continuous threshold has the expansion

\[
\frac{\pi}{\arcsin(1/\rho)}
=
\pi\rho-\frac{\pi}{6\rho}
-\frac{17\pi}{360\rho^3}
+O(\rho^{-5}),
\]

which recovers and refines the leading constant \(\pi\) in the known
large-\(\rho\) asymptotic.

## Relation to prior work

Bobrowski--Skraba (2026) prove the general asymptotic point-count law and identify
sphere covering as the asymptotically optimal mechanism; their deterministic
Proposition 4.3 is asymptotic in the target persistence. Their Lemma 7.3 contains
the geometric inclusion underlying the exact lower estimate used above, but is
stated only in the form needed for the asymptotic argument.

Bobrowski--Kahle--Skraba (2017) previously obtained coarse point-count lower
bounds sufficient for order-of-growth results in random geometric complexes.
Gómez--Mémoli (2024) determine several exact persistence sets for
Vietoris--Rips filtrations, including regular configurations on circles, but
their results concern a different filtration and do not give the planar Čech
extremum over all \(m\)-point clouds. Edelsbrunner--Pach (2025) study maximum
Betti numbers of Čech complexes rather than death-to-birth extremality.

The regular-polygon barcode itself is elementary and is not claimed as new.
The contribution claimed here is the global finite extremum over all planar
\(m\)-point sets and the resulting exact inverse point threshold.

## Limitations

- The theorem concerns one-dimensional Čech persistence in the Euclidean plane.
  It does not give an exact finite formula for \(k>1\) or ambient dimension
  \(d>2\).
- The public statement is made with \(\mathbb Z_2\)-coefficients to match the
  deterministic extremal problem in the motivating work; no coefficient-field
  generalization is claimed here.
- No uniqueness classification of extremizers is claimed. Regular polygons
  attain equality, but the proof does not classify every equality case.
- The most relevant motivating preprint is exceptionally recent, so
  not-yet-indexed parallel work remains a residual originality risk.

## References

1. O. Bobrowski and P. Skraba, *A Universal Law of Large Numbers for Extreme
   Cycles in Random Čech Complexes*, arXiv:2609.19474 (2026).
   https://arxiv.org/abs/2609.19474
2. O. Bobrowski, M. Kahle, and P. Skraba, *Maximally Persistent Cycles in
   Random Geometric Complexes*, Annals of Applied Probability 27 (2017),
   2032--2060. https://doi.org/10.1214/16-AAP1232
3. M. Gómez and F. Mémoli, *Curvature Sets Over Persistence Diagrams*,
   Discrete & Computational Geometry 72 (2024), 91--180.
   https://doi.org/10.1007/s00454-024-00634-0
4. H. Edelsbrunner and J. Pach, *Maximum Betti Numbers of Čech Complexes*,
   Discrete & Computational Geometry 75 (2026), 597--624.
   https://doi.org/10.1007/s00454-025-00796-5
