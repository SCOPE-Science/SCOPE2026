# Exact convexity gap of regular polygon vertex sets

## Finding

Let \(V_n(R)\) be the vertex set of a regular Euclidean \(n\)-gon of circumradius \(R>0\), equipped with ambient Euclidean chord distance, where \(n\ge3\). For a metric space \(X\), define
\[
\operatorname{hd}(x,y)
=
2\inf\{r:\text{there is }z\in X\text{ with }x,y\in B(z,r)\},
\]
\[
\operatorname{ld}(x,y)
=
\operatorname{hd}(x,y)-d(x,y),
\]
and
\[
\gamma(X)
=
\sup_{x,y\in X}\operatorname{ld}(x,y).
\]

Put
\[
t=\frac{\pi}{n}.
\]
Then
\[
\frac{\gamma(V_n(R))}{R}
=
\begin{cases}
2(\sqrt2-\cos t),
&n\equiv0\pmod4,\\[1mm]
2\sqrt2\bigl(\cos(t/4)-\sin(t/4)\bigr)-2\cos(3t/2),
&n\equiv1\pmod4,\\[1mm]
2\sqrt2\bigl(\cos(t/2)+\sin(t/2)\bigr)-2,
&n\equiv2\pmod4,\\[1mm]
2\sqrt2\bigl(\cos(t/4)+\sin(t/4)\bigr)-2\cos(t/2),
&n\equiv3\pmod4.
\end{cases}
\]

A maximizing pair of vertices has cyclic separation equal to the largest odd integer not exceeding
\[
\left\lfloor\frac n2\right\rfloor.
\]

Consequently,
\[
\gamma(V_n(R))
\longrightarrow
2(\sqrt2-1)R,
\]
which is the exact convexity gap of the Euclidean circle of radius \(R\).

More precisely, along the four residue classes modulo \(4\),
\[
\gamma(V_n(R))
=
2(\sqrt2-1)R
+
\begin{cases}
\displaystyle \frac{\pi^2R}{n^2}+O(n^{-4}),
&n\equiv0\pmod4,\\[2mm]
\displaystyle -\frac{\sqrt2\pi R}{2n}+O(n^{-2}),
&n\equiv1\pmod4,\\[2mm]
\displaystyle \frac{\sqrt2\pi R}{n}+O(n^{-2}),
&n\equiv2\pmod4,\\[2mm]
\displaystyle \frac{\sqrt2\pi R}{2n}+O(n^{-2}),
&n\equiv3\pmod4.
\end{cases}
\]

Thus the general Hausdorff continuity of the convexity gap hides a sharp arithmetic sampling effect: one residue class has quadratic convergence while the other three have first-order convergence with different signed leading terms.

## Assumptions and scope

The metric on \(V_n(R)\) is the ambient Euclidean distance between vertices, not shortest-path distance along polygon edges. Balls in the definitions of hyperdistance and leipodistance are metric balls inside the finite space \(V_n(R)\), so their centers must themselves be vertices.

Geller and Misiurewicz introduced the gap as a quantitative failure-of-midpoints invariant. Their circle computation gives
\[
\gamma(S_R^1)=2(\sqrt2-1)R,
\]
and their Hausdorff estimate implies continuity of \(\gamma\) under dense approximation. The present result gives the exact finite-sampling profile for the canonical regular samples of that circle.

## Proof

Index the vertices by \(\mathbb Z/n\mathbb Z\). Let
\[
\rho(i,j)
=
\min\{|i-j|,n-|i-j|\}
\]
be cyclic index distance. If
\[
0\le q\le\left\lfloor\frac n2\right\rfloor,
\]
the Euclidean chord length for cyclic separation \(q\) is
\[
d_q
=
2R\sin(qt),
\qquad
t=\frac{\pi}{n}.
\]
This is strictly increasing in \(q\) over the displayed range.

Fix vertices \(0\) and \(k\), with
\[
1\le k\le\left\lfloor\frac n2\right\rfloor.
\]
For any candidate center \(j\), let
\[
m_j
=
\max\{\rho(0,j),\rho(k,j)\}.
\]
The triangle inequality for \(\rho\) gives
\[
k
=
\rho(0,k)
\le
\rho(0,j)+\rho(j,k)
\le
2m_j.
\]
Hence
\[
m_j\ge\left\lceil\frac k2\right\rceil.
\]
Choosing a vertex nearest the midpoint of the shorter cyclic arc from \(0\) to \(k\) attains equality. Since chord length is increasing with cyclic separation,
\[
\min_j\max\{d(0,j),d(k,j)\}
=
d_{\lceil k/2\rceil}.
\]
Therefore
\[
\operatorname{hd}(0,k)
=
2d_{\lceil k/2\rceil}
\]
and the leipodistance for a pair with separation \(k\) is
\[
g_k
=
2d_{\lceil k/2\rceil}-d_k.
\]

For even separation \(k=2m\),
\[
g_{2m}
=
4R\sin(mt)-2R\sin(2mt).
\]
For the preceding odd separation,
\[
g_{2m-1}
=
4R\sin(mt)-2R\sin((2m-1)t).
\]
Whenever \(2m\le\lfloor n/2\rfloor\), both angles lie in \([0,\pi/2]\), so
\[
g_{2m-1}-g_{2m}
=
2R\bigl(\sin(2mt)-\sin((2m-1)t)\bigr)
>
0.
\]
Thus no even separation can maximize the gap.

For odd separation \(k=2m+1\), write
\[
u=(m+1)t.
\]
Then
\[
g_{2m+1}
=
4R\sin u-2R\sin(2u-t).
\]
Define
\[
F(u)=4R\sin u-2R\sin(2u-t).
\]
On the admissible odd separations one has
\[
t\le u\le 2u-t\le\frac{\pi}{2},
\]
and hence
\[
F'(u)
=
4R\bigl(\cos u-\cos(2u-t)\bigr)
\ge0,
\]
with strict inequality once \(u>t\). Therefore the odd-separation values increase strictly. The global maximum is attained at the largest odd integer
\[
k_n\le\left\lfloor\frac n2\right\rfloor.
\]

If \(k_n=2m+1\), then
\[
\gamma(V_n(R))
=
4R\sin((m+1)t)-2R\sin((2m+1)t).
\]
Substituting the appropriate terminal odd separation in the four residue classes gives the stated formulas.

Finally, Taylor expansion of those four exact expressions yields the displayed asymptotics. In particular all four subsequences converge to
\[
2(\sqrt2-1)R,
\]
the circle value computed by Geller and Misiurewicz.

## Verification

The accompanying `verify.py` constructs regular polygons directly in Cartesian coordinates. For every \(3\le n\le80\), it enumerates every unordered vertex pair and every possible vertex center, computes hyperdistance from the definition, and compares the resulting global gap with both the compact maximizing-separation formula and the four residue-class formulas.

It also checks the predicted leading asymptotic error on each residue class. The script was replayed from its packaged path and prints:

`VERIFY_OK regular-polygon convexity gap n=3..80`

The enumeration is only a finite consistency check. The theorem for all \(n\) follows from the cyclic midpoint minimization and the analytic monotonicity argument in the proof.

## Relationship to prior work

Geller and Misiurewicz introduced hyperdistance, leipodistance, and the convexity gap for general metric spaces. They computed the gap of a Euclidean sphere and proved a Hausdorff continuity bound for the gap. Their paper does not contain a regular-polygon computation; a full-text search of the accessible paper found no occurrence of “polygon.”

The sphere example gives the limiting value
\[
2(\sqrt2-1)R,
\]
while the general Hausdorff estimate gives only a coarse convergence guarantee for dense regular samples. The present result identifies the exact finite value, the extremal pair separation, and the modulo-\(4\) convergence profile.

A later paper by the same authors uses convexity gap and tryposity at infinity for sparse unbounded metric spaces. That direction does not address finite cyclic Euclidean samples.

Targeted searches for “leipodistance,” “hyperdistance,” “convexity gap,” regular polygons, finite cyclic metrics, and circle approximations did not locate an equivalent exact formula.

## Limitations

The theorem is specific to vertices equally spaced on one Euclidean circle with chord distance. It does not treat the polygonal boundary as a continuous metric subspace, intrinsic edge-path distance, irregular cyclic point sets, or higher-dimensional spherical designs.

The literature search is targeted rather than exhaustive. The terminology is recent and distinctive, which lowers alias risk, but an equivalent elementary calculation could conceivably appear under a different nonconvexity or midpoint-defect terminology.

## References

W. Geller and M. Misiurewicz, “Holes, nonconvexity, and curvature in metric spaces,” manuscript dated 2023-04-30; later published in Israel Journal of Mathematics, DOI 10.1007/s11856-026-2905-8.

W. Geller and M. Misiurewicz, “Sparse metric spaces and sparse ends,” arXiv:2606.12202, first submitted 2026-06-10.
