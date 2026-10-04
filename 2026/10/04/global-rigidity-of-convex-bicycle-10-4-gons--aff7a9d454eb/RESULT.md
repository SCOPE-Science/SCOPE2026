# Global rigidity of convex bicycle \((10,4)\)-gons
## Finding
Let \(V_0,\ldots,V_9\) be the vertices, in cyclic order, of a nondegenerate convex equilateral decagon. Suppose that the ten fourth-neighbor diagonals \(\lvert V_iV_{{i+4}}\rvert\), with indices taken modulo \(10\), all have one common length. Then the decagon is regular.

In the terminology of bicycle polygons, every convex plane bicycle \((10,4)\)-gon is therefore a regular decagon.

## Assumptions and scope
A bicycle \((n,k)\)-gon is an equilateral \(n\)-gon whose \(k\)-diagonals all have the same length. Here only the convex, nondegenerate, planar case \((n,k)=(10,4)\) is considered. No smoothness, cyclicity, or a priori symmetry is assumed.

Write
\[
e_i=V_{{i+1}}-V_i,
\]
so every \(e_i\) has the same positive length. Choose lifted edge directions \(\theta_i\) with \(\theta_{{i+10}}=\theta_i+2\pi\), and put
\[
\alpha_i=\theta_{{i+1}}-\theta_i.
\]
Convexity gives \(0\le \alpha_i\le\pi\) and
\[
\sum_{{i=0}}^9\alpha_i=2\pi.
\]

## Proof
Tabachnikov's isosceles-trapezoid lemma for convex bicycle polygons says that, for each \(i\), the quadrilateral
\[
V_iV_{{i+1}}V_{{i+4}}V_{{i+5}}
\]
is an isosceles trapezoid whose parallel bases are \(V_iV_{{i+5}}\) and \(V_{{i+1}}V_{{i+4}}\). Its equal legs are the side vectors with directions \(\theta_i\) and \(\theta_{{i+4}}\). If \(\phi_i\) is the unoriented direction of either base, reflection symmetry of an isosceles trapezoid gives
\[
2\phi_i\equiv \theta_i+\theta_{{i+4}}\pmod{{2\pi}}.
\]
Applying the same relation to the trapezoid starting at \(i+5\), whose base \(V_{{i+5}}V_{{i+10}}\) is the same line as \(V_iV_{{i+5}}\), gives
\[
\theta_{{i+5}}+\theta_{{i+9}}\equiv\theta_i+\theta_{{i+4}}\pmod{{2\pi}}.
\]
For the chosen lifts, the difference of the two sides is
\[
\theta_{{i+5}}+\theta_{{i+9}}-\theta_i-\theta_{{i+4}}
 =2\pi+\alpha_{{i+4}}-\alpha_{{i+9}}.
\]
It is an integral multiple of \(2\pi\) and lies in \([\pi,3\pi]\), hence it equals \(2\pi\). Therefore
\[
\alpha_{{i+4}}=\alpha_{{i+9}}
\]
for every \(i\), or equivalently
\[
\alpha_{{j+5}}=\alpha_j.
\]
Thus the five-angle sum is \(\pi\), so
\[
\theta_{{i+5}}=\theta_i+\pi,
\qquad
e_{{i+5}}=-e_i.
\]
Consequently \(V_i+V_{{i+5}}\) is independent of \(i\). The decagon is centrally symmetric; let \(c\) be its center and put \(X_i=V_i-c\). Then
\[
X_{{i+5}}=-X_i.
\]
In particular,
\[
X_{{i+4}}=-X_{{i-1}}.
\]
Let \(s\) be the common side length and \(d\) the common fourth-diagonal length. For every \(i\),
\[
\lVert X_i-X_{{i-1}}\rVert=s,
\qquad
\lVert X_i+X_{{i-1}}\rVert=d.
\]
The parallelogram identity yields
\[
2\bigl(\lVert X_i\rVert^2+\lVert X_{{i-1}}\rVert^2\bigr)=s^2+d^2.
\]
Writing \(r_i=\lVert X_i\rVert^2\), we have \(r_{{i+5}}=r_i\) and
\[
r_i+r_{{i-1}}=\frac{{s^2+d^2}}2.
\]
Hence \(r_i=r_{{i-2}}\). Periods \(2\) and \(5\) are coprime, so all \(r_i\) are equal. Thus all ten vertices lie on one circle centered at \(c\).

Let \(\delta_i\) be the positive central angle from \(V_i\) to \(V_{{i+1}}\) in cyclic order. Central symmetry gives \(\delta_{{i+5}}=\delta_i\) and
\[
\sum_{{i=0}}^4\delta_i=\pi,
\]
so every \(\delta_i\) lies in \((0,\pi)\). Equal side chords on a common circle therefore have equal central angles. Since their total is \(2\pi\),
\[
\delta_i=\frac{\pi}{5}
\]
for all \(i\). The decagon is regular.

## Verification
The only non-elementary input is the isosceles-trapezoid lemma for convex bicycle polygons, inspected in the full text of Tabachnikov's paper. Every subsequent step is an exact implication: the lifted-angle congruence forces five-periodic turning angles; five-periodicity forces central symmetry; the parallelogram identity on the resulting odd five-cycle forces a common circumradius; and equal side chords then force equal central gaps.

No numerical experiment, finite enumeration, or unproved regularity assumption is used.

## Relationship to prior work
Tabachnikov introduced bicycle \((n,k)\)-gons, posed the general classification problem, and proved regularity for several parameter families, but his listed regularity cases do not include \((10,4)\). He also established the isosceles-trapezoid lemma used above.

Csikós identified an exceptional even-even set of parameters for infinitesimal rigidity. The pair \((10,4)\) belongs to that set because
\[
10\mid(4+1)\left(\frac{{10}}2-4+1\right)=10.
\]
For such parameters he proved second-order infinitesimal flexibility but third-order rigidity of the regular polygon, and asked whether the regular polygon is genuinely flexible inside the bicycle-polygon family. The theorem above answers that global question negatively for the convex \((10,4)\) case.

Connelly and Csikós classified first-order flexible regular bicycle polygons; their result concerns infinitesimal behavior at the regular configuration and does not imply the global convex theorem proved here. Later work on polygonal bicycle paths likewise studies a broader dynamical framework without supplying this \((10,4)\) global rigidity statement.

## Limitations
The theorem is restricted to convex plane bicycle \((10,4)\)-gons. It does not classify nonconvex or self-intersecting solutions, does not settle other exceptional parameter pairs, and gives no quantitative stability estimate for nearly equal side or fourth-diagonal lengths.

A residual literature risk remains that the same elementary special-case argument appears in an unindexed note or discussion not located in the checked sources.

## References
1. Serge Tabachnikov, *Tire track geometry: variations on a theme*, arXiv:math/0405445; DOI:10.1007/BF02777353.
2. Balázs Csikós, *On the rigidity of regular bicycle \((n,k)\)-gons*, DOI:10.55016/ojs/cdm.v2i1.61885.
3. Robert Connelly and Balázs Csikós, *Classification of first-order flexible regular bicycle polygons*, DOI:10.1556/SScMath.2008.1074.
4. Ian Alevy and Emmanuel Tsukerman, *Polygonal bicycle paths and the Darboux transformation*, DOI:10.2140/involve.2016.9.57.
