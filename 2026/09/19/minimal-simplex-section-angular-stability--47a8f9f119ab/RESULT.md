# Quantitative stability and exact Hessian for minimal central simplex sections

Let
\[
T_{n-1}=\operatorname{conv}\{e_1,\dots,e_n\}\subset\mathbb R^n,\qquad n\ge 3,
\]
and, for a unit vector \(a\perp(1,\dots,1)\), write
\[
V(a)=\operatorname{Vol}_{n-2}(T_{n-1}\cap a^\perp).
\]
Ambrus and Gárgyán proved that the global minimum of \(V\) is attained exactly by the facet-parallel sections. With
\[
a_*=\left(\sqrt{\frac{n-1}n},-\frac1{\sqrt{n(n-1)}},\dots,
-\frac1{\sqrt{n(n-1)}}\right),
\]
their minimum is
\[
V_{\min}
=\frac{\sqrt n}{(n-2)!}
\left(\frac{n-1}n\right)^{n-\frac32}.
\]

This note gives a quantitative refinement near that extremal orbit, an exact factorization on the one-positive sign chamber, and the full spherical Hessian at every facet-parallel minimizer.

## 1. Exact one-positive factorization

Assume, after permutation and changing \(a\) to \(-a\) if necessary, that
\[
a_1=s>0>a_j\qquad (2\le j\le n).
\]
Put
\[
b_j=-a_j,\qquad p_j=\frac{b_j}s.
\]
Since \(\sum_j a_j=0\),
\[
p_j>0,\qquad \sum_{j=2}^n p_j=1.
\]
Set
\[
Q=\sum_{j=2}^n p_j^2.
\]
The unit-norm condition gives \(s=(1+Q)^{-1/2}\).

Let \(X_1,\dots,X_n\) be independent \(\mathrm{Exp}(1)\) variables. The standard probabilistic section formula gives
\[
V(a)=\frac{\sqrt n}{(n-2)!}\,f_{\sum a_jX_j}(0).
\]
Writing \(W=\sum_{j=2}^n b_jX_j\), independence and the exponential density yield
\[
f_{sX_1-W}(0)
=\frac1s\,\mathbb E e^{-W/s}
=\frac1s\prod_{j=2}^n\frac1{1+p_j}.
\]
Hence
\[
\frac{V(a)}{V_{\min}}
=
\sqrt{\frac{1+Q}{1+\frac1{n-1}}}\,
\frac{\left(\frac n{n-1}\right)^{n-1}}
{\prod_{j=2}^n(1+p_j)}.
\tag{1}
\]

Let \(\theta\in[0,\pi/2)\) be the spherical angle from \(a\) to the facet normal \(a_*\) whose exceptional positive coordinate is in the same position as \(a_1\). A direct calculation gives
\[
\cos\theta
=\langle a,a_*\rangle
=
\sqrt{\frac{1+\frac1{n-1}}{1+Q}}.
\]
Therefore (1) becomes the exact factorization
\[
\boxed{
\frac{V(a)}{V_{\min}}
=
\sec\theta\,
\frac{\left(\frac n{n-1}\right)^{n-1}}
{\prod_{j=2}^n(1+p_j)}.
}
\tag{2}
\]
By AM-GM,
\[
\prod_{j=2}^n(1+p_j)
\le
\left(\frac n{n-1}\right)^{n-1},
\]
with equality only when \(p_2=\cdots=p_n=1/(n-1)\). Consequently,
\[
\boxed{
V(a)\ge V_{\min}\sec\theta.
}
\tag{3}
\]
Thus the angular deficit is controlled explicitly throughout the entire one-positive chamber, not merely infinitesimally.

For unit normals, if
\[
d=\|a-a_*\|,
\]
then \(d^2=2(1-\cos\theta)\), so (3) is equivalently
\[
\boxed{
\frac{V(a)}{V_{\min}}
\ge \frac1{1-d^2/2},
\qquad
\frac{V(a)}{V_{\min}}-1
\ge \frac{d^2}{2-d^2}.
}
\tag{4}
\]

In inverse form, if \(V(a)\le(1+\varepsilon)V_{\min}\) in this chamber, then
\[
\boxed{
\|a-a_*\|^2
\le \frac{2\varepsilon}{1+\varepsilon}.
}
\tag{5}
\]

## 2. An explicit global near-minimizer threshold

The preceding estimate can be promoted from a sign-chamber statement to a genuinely global near-minimizer statement below an explicit finite-dimensional gap.

For \(2\le m<n\), define
\[
B_{n,m}
=
\frac{
\left(\frac{m-1}m\right)^{m-\frac32}
}{
\left(\frac{n-1}n\right)^{n-\frac32}
}.
\tag{6}
\]
This is the ratio between the smallest section with exactly \(m\) nonzero coordinates and \(V_{\min}\). It follows by applying the Ambrus--Gárgyán minimum theorem in the \(m\)-coordinate face together with the probabilistic volume normalization.

For \(2\le k\le n-2\), let
\[
R_{n,k}
=
\frac{
(n-2)!\,
k^{k-\frac12}(n-k)^{n-k-\frac12}
}{
(k-1)!(n-k-1)!(n-1)^{n-\frac32}
}.
\tag{7}
\]
This is the volume ratio of the two-value critical normal having \(k\) positive and \(n-k\) negative coordinates. Formula (7) follows by convolving the two gamma densities corresponding to the positive and negative coordinate blocks.

Set
\[
\boxed{
\rho_n
=
\min\left(
\min_{2\le m<n}B_{n,m},
\;
\min_{2\le k\le n-2}R_{n,k}
\right)>1,
}
\tag{8}
\]
where the second minimum is omitted for \(n=3\). Strict positivity of the gap follows from the equality classification in the sharp minimum theorem: neither a normal with a zero coordinate nor a two-value normal with both sign multiplicities at least \(2\) is facet-parallel.

### Global stability theorem

Let \(\mathcal M\) be the finite orbit of the facet-parallel minimizer normals under coordinate permutations and multiplication by \(-1\). If
\[
V(a)<\rho_n V_{\min},
\]
then \(a\) has exactly one coordinate of one sign and all remaining coordinates of the opposite sign. Consequently, if
\[
V(a)\le(1+\varepsilon)V_{\min}
\qquad\text{with}\qquad
1+\varepsilon<\rho_n,
\]
then
\[
\boxed{
\operatorname{dist}(a,\mathcal M)^2
\le
\frac{2\varepsilon}{1+\varepsilon}.
}
\tag{9}
\]

#### Proof of the threshold assertion

Suppose instead that \(a\) lies in a sign chamber with at least two positive and at least two negative coordinates. Minimize \(V\) on the closure of that chamber.

If a minimizer lies on the boundary, at least one coordinate vanishes. If exactly \(m\) coordinates remain nonzero, the lower-dimensional sharp minimum theorem and the section-density normalization give the ratio \(B_{n,m}\ge\rho_n\).

If a minimizer lies in the interior, it is a constrained local minimum with no zero coordinates. Ambrus--Gárgyán prove that any such critical normal has at most three distinct coordinate values; they also prove that a three-value critical normal is not a local minimum within its multiplicity class. Hence an interior chamber minimizer must have exactly two coordinate values. Because both signs occur at least twice, its multiplicities are \(k,n-k\) with \(2\le k\le n-2\), and its ratio is \(R_{n,k}\ge\rho_n\).

Thus no multi-positive/multi-negative chamber contains a point with volume \(<\rho_nV_{\min}\). After changing sign if needed, every such near-minimizer lies in a one-positive chamber, where (5) applies.

## 3. Exact spherical Hessian at the minimizer

The admissible normal manifold is
\[
\mathbb S^{n-1}\cap(1,\dots,1)^\perp\cong\mathbb S^{n-2}.
\]
At \(a_*\), its tangent space is
\[
T_{a_*}
=
\left\{
v\in\mathbb R^n:
v_1=0,\;
\sum_{j=2}^n v_j=0
\right\}.
\]
Let \(v\in T_{a_*}\) be a unit vector and follow the unit-speed spherical geodesic
\[
a(t)=a_*\cos t+v\sin t.
\]
For small \(t\), this remains in the one-positive chamber. Put
\[
A=\sqrt{\frac{n-1}n},
\qquad
D=\sqrt{\frac n{n-1}}.
\]
The exact one-positive formula becomes
\[
\log f_{\sum a_j(t)X_j}(0)
=
(n-2)\log(A\cos t)
-\sum_{j=2}^n
\log(D\cos t-v_j\sin t).
\]
Because \(\sum_{j=2}^n v_j=0\), the first derivative at \(t=0\) vanishes. The second derivative is
\[
-(n-2)
+\sum_{j=2}^n
\left(1+\frac{v_j^2}{D^2}\right)
=
1+\frac{n-1}n
=
\frac{2n-1}n.
\]
The multiplicative factor between density and section volume is constant, hence
\[
\boxed{
\operatorname{Hess}_{a_*}(\log V)
=
\frac{2n-1}n\,g_{\mathbb S}.
}
\tag{10}
\]
Since \(a_*\) is critical,
\[
\boxed{
\operatorname{Hess}_{a_*}V
=
\frac{2n-1}n\,V_{\min}\,g_{\mathbb S}.
}
\tag{11}
\]
In particular, uniformly over unit tangent directions,
\[
\boxed{
\frac{V(a(t))}{V_{\min}}
=
1+\frac{2n-1}{2n}t^2+O_n(t^3).
}
\tag{12}
\]
Thus every facet-parallel minimizer is an isotropic, nondegenerate quadratic minimum of the section-volume function.

## Relation to prior work

Ambrus and Gárgyán (2026) prove the sharp global minimum and equality classification, and their critical-point analysis is used above to isolate the finite global gap in (8). Their paper does not state a quantitative near-minimizer estimate or the Hessian at a facet-parallel minimum.

Dirksen (2017) obtained a partial minimum result in a restricted sign regime. The factorization (2) supplies an independent short proof in that chamber and, more importantly, a quantitative angular strengthening. Ambrus and Gárgyán identify a gap in a different balancing step of Dirksen's argument used for his claimed low-dimensional global result; no reliance on that step is made here.

Myroshnychenko, Tang, Tatarko and Tkocz prove dimension-free stability for Webb's sharp **maximum** simplex-slicing inequality. Their stability theorem concerns the opposite extremum and does not provide stability of the recently resolved minimum.

To the best of our knowledge, the exact factorization (2) as a quantitative angular stability statement, the explicit global sublevel gap (8)--(9), and the isotropic Hessian formula (10) have not previously been stated.

## Limitations

The sharp angular inequality (3) is specific to the one-positive/one-negative sign chamber. The global statement uses the explicit threshold \(\rho_n>1\); no claim is made that this threshold is optimal. No dimension-free global stability modulus for arbitrary deficits is proved. The Hessian describes the local quadratic geometry of the minimum but does not classify higher-order terms. Because the sharp global minimum theorem is recent, differently phrased or not-yet-indexed parallel observations remain a residual originality risk.

## References

1. G. Ambrus and B. Gárgyán, *Minimal central slices of the regular simplex*, arXiv:2609.12714 (2026). https://arxiv.org/abs/2609.12714
2. H. Dirksen, *Sections of the regular simplex — Volume formulas and estimates*, Math. Nachr. 290 (2017), 2567–2584. https://doi.org/10.1002/mana.201600109
3. S. Myroshnychenko, C. Tang, K. Tatarko and T. Tkocz, *Stability of Simplex Slicing*, Discrete Comput. Geom. 76 (2026), 491–507. https://doi.org/10.1007/s00454-025-00758-x
