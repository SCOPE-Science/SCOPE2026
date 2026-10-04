# Positive-quadrant coordinates for a segment from visual-angle cusp slopes

## Finding

Fix a circle and a chord \(H\) of length \(L>0\). Orient the chord from its left circle intersection to its right one and use chord coordinate \(t\in[0,L]\). For a proper subsegment with endpoints \(0<u<v<L\), let \(x\) and \(y\) be the magnitudes of the one-sided visual-angle derivatives at the two chord-circle intersections, each divided by the sine of the angle between the circle tangent and the chord at that intersection. Then
\[
x=\frac{v-u}{uv},
\qquad
y=\frac{v-u}{(L-u)(L-v)}.
\]

The map
\[
(u,v)\longmapsto(x,y)
\]
is a real-analytic diffeomorphism from
\[
\{(u,v):0<u<v<L\}
\]
onto
\[
(0,\infty)^2.
\]
Thus there is no hidden compatibility inequality between the two positive normalized endpoint cusp slopes: every positive pair occurs for exactly one subsegment of the fixed chord.

Writing
\[
m=\frac{u+v}{2},
\qquad
r=\frac{v-u}{2},
\]
the inverse is constructive. The number \(r>0\) is the unique solution of
\[
\sqrt{r^2+\frac{2r}{x}}
+
\sqrt{r^2+\frac{2r}{y}}
=L,
\]
and then
\[
m=\sqrt{r^2+\frac{2r}{x}},
\qquad
u=m-r,
\qquad
v=m+r.
\]

The Jacobian is everywhere negative:
\[
\det D(x,y)
=
-\frac{L(v-u)\bigl(L(u+v)-2uv\bigr)}
{u^2v^2(L-u)^2(L-v)^2}
<0.
\]

## Assumptions and scope

The observation curve is a circle, \(H\) is a fixed chord, and the unknown object is a single proper subsegment lying strictly inside that chord. The data are the two one-sided derivative magnitudes of the visual-angle function at the two points where the chord meets the observation circle, normalized by the corresponding tangent-chord sine factors.

The starting derivative formulas are standard in this masking-function setting and appear explicitly in work of Lukács. The new point here is the complete range description and global coordinate statement: the feasible normalized data set is the entire positive quadrant, not merely an unspecified subset on which reconstruction is unique.

## Proof

Let the left circle intersection of \(H\) have coordinate \(0\) and the right one coordinate \(L\). At the left intersection, the distances to the subsegment endpoints are \(u\) and \(v\). The one-sided visual-angle derivative formula therefore gives, after division by the tangent-chord sine factor,
\[
x=\frac1u-\frac1v=\frac{v-u}{uv}.
\]
At the right intersection, the endpoint distances are \(L-v\) and \(L-u\), so
\[
y=\frac1{L-v}-\frac1{L-u}
=\frac{v-u}{(L-u)(L-v)}.
\]
Both values are strictly positive.

Set
\[
m=\frac{u+v}{2},
\qquad
r=\frac{v-u}{2}>0.
\]
Then
\[
uv=m^2-r^2,
\qquad
(L-u)(L-v)=(L-m)^2-r^2,
\]
and hence
\[
m^2=r^2+\frac{2r}{x},
\qquad
(L-m)^2=r^2+\frac{2r}{y}.
\]
Because \(0<u<v<L\), both \(m\) and \(L-m\) are positive, so
\[
m=\sqrt{r^2+\frac{2r}{x}},
\qquad
L-m=\sqrt{r^2+\frac{2r}{y}}.
\]
Adding these equations yields
\[
\Phi_{x,y}(r)
:=
\sqrt{r^2+\frac{2r}{x}}
+
\sqrt{r^2+\frac{2r}{y}}
=L.
\]

Conversely, fix arbitrary \(x,y>0\). On \(r>0\), each square-root term in \(\Phi_{x,y}\) is strictly increasing, so \(\Phi_{x,y}\) is continuous and strictly increasing. Moreover,
\[
\lim_{r\downarrow0}\Phi_{x,y}(r)=0,
\qquad
\lim_{r\to\infty}\Phi_{x,y}(r)=\infty.
\]
Thus there is a unique \(r>0\) with \(\Phi_{x,y}(r)=L\). Define
\[
m=\sqrt{r^2+\frac{2r}{x}}.
\]
The defining equation gives
\[
L-m=\sqrt{r^2+\frac{2r}{y}}.
\]
Each square root is strictly larger than \(r\), hence
\[
m>r,
\qquad
L-m>r.
\]
Therefore
\[
0<m-r<m+r<L,
\]
so \(u=m-r\) and \(v=m+r\) form a valid proper subsegment. Substitution recovers exactly the prescribed \(x,y\). This proves surjectivity; uniqueness of \(r\), then \(m\), proves injectivity.

Direct differentiation gives
\[
\det D(x,y)
=
-\frac{L(v-u)\bigl(L(u+v)-2uv\bigr)}
{u^2v^2(L-u)^2(L-v)^2}.
\]
The numerator factor
\[
L(u+v)-2uv=u(L-v)+v(L-u)
\]
is positive on \(0<u<v<L\), so the determinant never vanishes. The forward map is real analytic, bijective, and locally analytically invertible everywhere. Its unique local inverse branches agree, giving a global real-analytic inverse. Hence it is a real-analytic diffeomorphism onto the positive quadrant.

## Verification

The derivative formulas were checked by translating the signed-coordinate formulas in the published chord-length-\(2\) normalization to coordinates \(0<u<v<L\). The inverse proof uses only monotonicity of a scalar function and strict endpoint inequalities, so it does not rely on numerical root finding.

The Jacobian was independently expanded and simplified to the displayed factorization. As a non-proof cross-check, the inverse construction was evaluated for endpoint data ranging over several orders of magnitude; substitution returned the original positive data and always produced \(0<u<v<L\).

## Relationship to prior work

Lukács proves that the two relevant endpoint derivative values determine a segment on a known chord. In the chord-length-\(2\) normalization, the paper writes the two positive rational functions of the signed endpoint coordinates and solves algebraically for those coordinates. The earlier Hungarian article gives the same injectivity theorem and an explicit segment-length expression.

Those results establish uniqueness for data already known to come from a segment. They do not state that every positive pair of normalized derivative magnitudes is feasible, identify the data range with the full positive quadrant, or formulate the endpoint-data map as a global analytic diffeomorphism with its nonvanishing Jacobian. The present result supplies exactly that range classification.

The distinction is logical as well as terminological: injectivity alone permits the image to be a proper subset of \((0,\infty)^2\). The monotone inverse equation above proves that the image is all of it.

## Limitations

The chord is assumed known and only one segment is reconstructed. The result does not solve the pairing problem for multiple unknown segments, does not treat a general observation curve, and does not provide a global noise-stability constant near the boundary of parameter space. The exact Jacobian shows where conditioning can deteriorate, but no quantitative statistical model is claimed.

The originality check was targeted rather than exhaustive. The 2017 predecessor is close prior art because it contains the same forward formulas and proves injectivity; the accepted contribution is therefore limited to the complete feasible-data classification, the global analytic-coordinate statement, and the exact Jacobian.

## References

P. Lukács, “Symmetric Masking Function of Segments,” International Electronic Journal of Geometry 13(2) (2020), 45–51, DOI 10.36890/iejg.742248.

P. Lukács, “Szakaszok takarási száma,” Polygon, Matematikai, szakdidaktikai Közlemények 24(2) (2017), 29–42.

Á. Kurusa, “Visual distinguishability of segments,” International Electronic Journal of Geometry 6(1) (2013), 56–67.
