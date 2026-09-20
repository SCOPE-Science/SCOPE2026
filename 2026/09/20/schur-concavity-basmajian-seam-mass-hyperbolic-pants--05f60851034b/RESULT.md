# Schur-concavity of Basmajian seam mass on hyperbolic pairs of pants

## Statement

Let \(P\) be a compact hyperbolic pair of pants with geodesic boundary components of lengths
\[
\ell_1,\ell_2,\ell_3>0,\qquad L=\ell_1+\ell_2+\ell_3.
\]
For \(\{i,j,k\}=\{1,2,3\}\), let \(d_i\) be the seam joining the \(j\)-th and \(k\)-th boundary components: the unique shortest geodesic arc perpendicular to both. Define the **seam Basmajian mass**
\[
\mathcal B_{\rm seam}(P)
=
2\sum_{i=1}^3\log\coth\frac{d_i}{2}.
\]
Each summand is the ordinary two-dimensional Basmajian contribution of that orthogeodesic.

Then
\[
\boxed{
\mathcal B_{\rm seam}
=
3\log\cosh\frac L4
-\sum_{i=1}^3
\log\cosh\!\left(\frac L4-\frac{\ell_i}{2}\right)
}
\tag{1}
\]
and equivalently
\[
\boxed{
\mathcal B_{\rm seam}
=
\log
\frac{4\cosh^3(L/4)}
{\cosh(L/4)+\sum_{i=1}^3\cosh(\ell_i-L/4)}
}.
\tag{2}
\]

For fixed \(L\), \(\mathcal B_{\rm seam}\) is a **strictly Schur-concave** symmetric function of the cuff-length vector. Thus if two positive triples \(\boldsymbol\ell,\boldsymbol\lambda\) have the same sum and
\(\boldsymbol\ell\) majorizes \(\boldsymbol\lambda\), then
\[
\mathcal B_{\rm seam}(\boldsymbol\ell)
\le
\mathcal B_{\rm seam}(\boldsymbol\lambda),
\]
with equality only when the triples differ by a permutation.

Consequently the exact fixed-\(L\) range is
\[
\boxed{
0<\mathcal B_{\rm seam}
\le
3\log\frac{\cosh(L/4)}{\cosh(L/12)}
}
\tag{3}
\]
and every value in this interval occurs. The upper endpoint is attained exactly by the equal-cuff pair of pants
\[
\ell_1=\ell_2=\ell_3=L/3.
\]
The lower endpoint is an infimum, approached when the cuff vector tends to a permutation of \((L,0,0)\).

A further sharp global consequence is
\[
\boxed{\mathcal B_{\rm seam}(P)<\frac L2.}
\tag{4}
\]
The constant \(1/2\) cannot be lowered uniformly over all compact hyperbolic pairs of pants: for equal cuffs and \(L\to\infty\),
\[
\frac{\mathcal B_{\rm seam}}{L}\longrightarrow \frac12.
\]

## Context

A hyperbolic pair of pants is determined by its three geodesic boundary lengths, and cutting along its three seams produces two congruent right-angled hexagons.  The right-angled-hexagon cosine law is classical; standard references include Buser and Ratcliffe.

Basmajian's identity expresses total geodesic boundary length as a sum over the orthospectrum.  In dimension two an orthogeodesic of length \(d\) contributes \(2\log\coth(d/2)\).  The quantity above isolates the contribution of the three inter-cuff seams.  It is not the full Basmajian sum.

The new point claimed here, to the best of our knowledge, is the closed seam-mass formula together with its strict majorization law, complete fixed-total-boundary range, and the sharp universal one-half bound for this three-seam contribution.

## Proof

Put
\[
a_i=\frac{\ell_i}{2},
\qquad
s=\frac{a_1+a_2+a_3}{2}=\frac L4.
\]
The right-angled-hexagon cosine law gives, for \(\{i,j,k\}=\{1,2,3\}\),
\[
\cosh d_i
=
\frac{\cosh a_i+\cosh a_j\cosh a_k}
{\sinh a_j\sinh a_k}.
\]
Using \(\tanh^2(d/2)=(\cosh d-1)/(\cosh d+1)\),
\[
\tanh^2\frac{d_i}{2}
=
\frac{\cosh a_i+\cosh(a_j-a_k)}
{\cosh a_i+\cosh(a_j+a_k)}.
\]
The sum-to-product formula now gives
\[
\tanh^2\frac{d_i}{2}
=
\frac{\cosh(s-a_j)\cosh(s-a_k)}
{\cosh s\,\cosh(s-a_i)}.
\tag{5}
\]
Multiplying (5) for \(i=1,2,3\) yields
\[
\prod_{i=1}^3\tanh^2\frac{d_i}{2}
=
\frac{\prod_{i=1}^3\cosh(s-a_i)}{\cosh^3s}.
\]
Since
\[
\mathcal B_{\rm seam}
=
-2\log\prod_i\tanh\frac{d_i}{2},
\]
equation (1) follows.

For (2), use
\[
4\cosh x\cosh y\cosh z
=
\cosh(x+y+z)
+\cosh(x+y-z)
+\cosh(x-y+z)
+\cosh(-x+y+z)
\]
with \(x=s-a_1,\ y=s-a_2,\ z=s-a_3\).  Their sum is \(s\), and the other three signed sums are \(2a_i-s=\ell_i-L/4\). Hence
\[
4\prod_i\cosh(s-a_i)
=
\cosh(L/4)+\sum_i\cosh(\ell_i-L/4),
\]
which gives (2).

Now fix \(L\).  The function
\[
g_L(t)=\cosh(t-L/4)
\]
is strictly convex. Therefore
\[
\sum_{i=1}^3 g_L(\ell_i)
\]
is strictly Schur-convex on the plane \(\ell_1+\ell_2+\ell_3=L\). Formula (2) is a fixed positive numerator divided by a strictly increasing function of this Schur-convex sum, followed by a logarithm. Thus \(\mathcal B_{\rm seam}\) is strictly Schur-concave.

The equal triple \((L/3,L/3,L/3)\) is majorized by every other fixed-sum triple, so it uniquely maximizes the seam mass. Substitution gives the upper endpoint in (3). On the closed simplex \(\ell_i\ge0\), a vertex such as \((L,0,0)\) majorizes every point; substituting it into (2) and using
\[
\cosh(3x)+3\cosh x=4\cosh^3x
\]
gives seam mass \(0\).  For strictly positive cuffs each Basmajian summand is positive, so \(0\) is not attained. Continuity along, for example,
\[
(L-2t,t,t),\qquad 0<t\le L/3,
\]
shows that every value in (3) occurs.

Finally, for the equal-cuff maximizer,
\[
\begin{aligned}
\mathcal B_{\max}(L)
&=
3\left(\log\cosh\frac L4-\log\cosh\frac L{12}\right)\\
&=
\frac L2
+
3\log\frac{1+e^{-L/2}}{1+e^{-L/6}}
<
\frac L2,
\end{aligned}
\]
because \(e^{-L/2}<e^{-L/6}\). Since every pair of pants has seam mass at most \(\mathcal B_{\max}(L)\), (4) follows. The same expression shows
\[
\mathcal B_{\max}(L)
=
\frac L2-3e^{-L/6}+O(e^{-L/3}),
\]
so the constant \(1/2\) is sharp.

For short total boundary,
\[
\mathcal B_{\max}(L)
=
\frac{L^2}{12}
-\frac{5L^4}{5184}
+\frac{91L^6}{5598720}
+O(L^8).
\]

## Reproducibility

`artifacts/verify_seam_mass.py` evaluates the seam lengths from the classical right-angled-hexagon cosine law, separately evaluates (2), and checks agreement and the fixed-\(L\) extremal inequalities on deterministic sample data. It uses only the Python standard library.

## Limitations

- The theorem concerns compact hyperbolic pairs of pants with three positive geodesic boundary lengths. Cusps enter only as limiting boundary points of the parameter simplex.
- The quantity is only the Basmajian contribution of the three inter-cuff seams, not the full orthospectrum sum and not the Luo--Tan pants measure.
- The result does not state that individual seam lengths are Schur-monotone.
- Originality is to the best of our knowledge. The formulas are elementary consequences of classical hexagon trigonometry, so an equivalent statement under different orthospectral or right-angled-hexagon notation could exist in older literature.

## Literature comparison

Buser's 1992 monograph and Ratcliffe's treatment supply the classical right-angled-hexagon and pair-of-pants geometry used in the proof. Basmajian's 1993 paper introduced the orthospectrum identity. Bridgeman--Tan's survey explains the Basmajian summands geometrically in terms of orthogonal projections.

Doan--Parlier--Tan's *Measuring pants* (2023) studies monotonicity and convexity of the **Luo--Tan** pants measures as functions of boundary lengths. That is a different identity and different summand from the three-seam Basmajian mass treated here.

Basmajian--Parlier--Tan (2025) develops families of identities based on prime orthogeodesics and concave cores. Current searches of its title/abstract together with the present exact formulas, majorization language, equal-cuff extremum, and fixed-total-boundary seam contribution did not locate the theorem above. The full range of older orthospectral folklore is not exhaustively searchable, so this remains a substantive residual originality risk.

The original Basmajian article was identified and its bibliographic record checked; the exact two-dimensional summand was cross-checked in later survey literature. The complete original article text was not directly inspected in this review.

## References

1. Peter Buser, *Geometry and Spectra of Compact Riemann Surfaces*, Birkhäuser, 1992; reprint DOI: https://doi.org/10.1007/978-0-8176-4992-0
2. John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 2nd ed., Springer, 2006. DOI: https://doi.org/10.1007/978-0-387-47322-2
3. Ara Basmajian, “The Orthogonal Spectrum of a Hyperbolic Manifold,” *American Journal of Mathematics* 115 (1993), 1139–1159. DOI: https://doi.org/10.2307/2375068
4. Martin Bridgeman and Ser Peow Tan, “Identities on hyperbolic manifolds,” in *Handbook of Teichmüller Theory*, Vol. V (2016), 19–53. DOI: https://doi.org/10.4171/160-1/2
5. Nhat Minh Doan, Hugo Parlier, Ser Peow Tan, “Measuring pants,” *Transactions of the American Mathematical Society* 376 (2023), 5281–5306. DOI: https://doi.org/10.1090/tran/8893
6. Ara Basmajian, Hugo Parlier, Ser Peow Tan, “Prime orthogeodesics, concave cores and families of identities on hyperbolic surfaces,” *Advances in Mathematics* 460 (2025), 110026. DOI: https://doi.org/10.1016/j.aim.2024.110026
