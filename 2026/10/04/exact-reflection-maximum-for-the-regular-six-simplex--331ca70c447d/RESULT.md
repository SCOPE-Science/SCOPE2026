# Exact reflection maximum for the regular six-simplex

## Finding

Let \(S\subset\mathbb R^6\) be a regular six-simplex and let \(H\) be any supporting hyperplane of \(S\). Write \(S^H\) for the orthogonal reflection of \(S\) across \(H\). Then
\[
\frac{\operatorname{Vol}_6(\operatorname{conv}(S\cup S^H))}
{\operatorname{Vol}_6(S)}
\le
6+\frac{2\sqrt{511}}7.
\]
The bound is sharp. Equality holds for exactly \(42\) supporting hyperplanes.

More precisely, choose the contact vertex \(v_0\) of an equality support and put \(s_i=v_i-v_0\) for the other six vertices. If \(u\) is the inward unit normal to \(H\), then, after relabeling \(v_1,\ldots,v_6\),
\[
\frac{\langle s_1,u\rangle}{\langle s_2,u\rangle}
=
\frac{29-\sqrt{511}}{11},
\qquad
\langle s_2,u\rangle=\cdots=\langle s_6,u\rangle.
\]
Conversely, this condition determines an equality support. There are \(7\) choices for \(v_0\) and \(6\) choices for the distinguished second vertex, giving \(42\) supports.

## Assumptions and scope

Scale \(S\) so that all edges have length \(1\). Every supporting hyperplane contains an exposed face and therefore at least one vertex. Relabel a contact vertex as \(v_0\), translate it to the origin, and set \(s_i=v_i-v_0\), \(1\le i\le6\). Then
\[
\langle s_i,s_i\rangle=1,
\qquad
\langle s_i,s_j\rangle=\frac12\quad(i\ne j).
\]
Let \(H=u^\perp\), where \(u\) is the inward unit normal. Put
\[
a_i=\langle s_i,u\rangle\ge0,\qquad
A=\sum_{i=1}^6 a_i,\qquad
y_i=\frac{a_i}{A},\qquad
Q=\sum_{i=1}^6 y_i^2.
\]
The vectors \(s_i\) span \(\mathbb R^6\), so \(A>0\).

## Proof

The Gram matrix of \(s_1,\ldots,s_6\) is
\[
G=\frac12(I+J),
\qquad
G^{-1}=2I-\frac27J.
\]
Hence the unit-length condition for \(u\) is
\[
1=2\sum_{i=1}^6 a_i^2-\frac27A^2
=2A^2\left(Q-\frac17\right),
\]
and therefore
\[
A^2=\frac{1}{2\left(Q-\frac17\right)}.
\]

We next compute the reflected-hull volume directly. Let \(F_0\) be the facet opposite \(v_0\), and let \(F_i\) be the facet opposite \(v_i\). If \(s=\sum_{j=1}^6s_j\), unit outward normals are proportional to \(s\) for \(F_0\) and to \(s-7s_i\) for \(F_i\). Thus \(F_0\) is always an upper facet relative to \(u\), while \(F_i\) is upper exactly when
\[
A-7a_i>0,
\quad\text{equivalently}\quad
y_i<\frac17.
\]
Facets with equality contribute zero projected volume and may be assigned to either side.

The positive half of \(\operatorname{conv}(S\cup S^H)\) is the region between \(H\) and the upper graph of \(S\). Over the orthogonal projection of an upper facet, the height is affine, so its integral is the projected \(5\)-volume times the average of the six vertex heights. Since all facets of a regular simplex have the same \(5\)-volume, division by \(\operatorname{Vol}_6(S)\) gives
\[
R(H):=
\frac{\operatorname{Vol}_6(\operatorname{conv}(S\cup S^H))}
{\operatorname{Vol}_6(S)}
=
\frac47\left[
A^2+\sum_{i\in I}(A-7a_i)(A-a_i)
\right],
\]
where
\[
I=\left\{i:y_i<\frac17\right\}.
\]
Write \(m=|I|\), \(t=\sum_{i\in I}y_i\), and \(Q_I=\sum_{i\in I}y_i^2\). Substituting the formula for \(A^2\) yields
\[
R(H)
=
\frac{2\left(Q_I-\frac87t+\frac{m+1}{7}\right)}
{Q-\frac17}.
\]

If \(m=0\), then \(Q\ge1/6\), so \(R(H)\le12\). Assume \(1\le m\le5\). For fixed \(m\) and \(t\), the numerator depends on the \(y_i\) in \(I\) only through \(Q_I\), and is positive. The complementary square sum satisfies
\[
Q_{I^c}\ge \frac{(1-t)^2}{6-m},
\]
with equality exactly when all complementary coordinates are equal. Hence a maximizer must have equal complementary coordinates.

Now keep \(m,t\) fixed and impose that equality. As a function of \(q=Q_I\), the normalized objective is a positive constant times a quotient of the form \((q+C)/(q+D)\). Its derivative has the sign of
\[
D-C
=
\frac{(t+5-m)(7t-m-1)}{7(6-m)}\le0
\]
because \(0\le t\le m/7\). Thus the objective is nonincreasing in \(q\), so a maximizer also has equal coordinates inside \(I\). We are reduced to one variable:
\[
\frac{R(H)}{12}
=
F_m(t):=
\frac{\frac{t^2}{m}-\frac87t+\frac{m+1}{7}}
{6\left(\frac{t^2}{m}+\frac{(1-t)^2}{6-m}-\frac17\right)},
\qquad
0\le t\le\frac m7.
\]

Exact differentiation gives the following chamber maxima:
\[
\begin{array}{c|c|c}
m & \max F_m & \text{maximizing }t\\ \hline
1 & \frac12+\frac{\sqrt{511}}{42}
& \frac{35-\sqrt{511}}{119}\\[2mm]
2 & \frac5{12}+\frac{\sqrt{273}}{28}
& \frac{15}{34}-\frac{3\sqrt{273}}{238}\\[2mm]
3 & \frac13+\frac{\sqrt{154}}{21}
& \frac{10}{17}-\frac{2\sqrt{154}}{119}\\[2mm]
4 & \frac14+\frac{\sqrt{2065}}{84}
& \frac{25}{34}-\frac{\sqrt{2065}}{238}\\[2mm]
5 & \frac7{12}
& \frac57.
\end{array}
\]
For \(m=1,\ldots,4\), the derivative numerator is respectively a positive multiple of
\[
119t^2-70t+6,\quad
119t^2-105t+18,\quad
119t^2-140t+36,\quad
119t^2-175t+60,
\]
and the displayed point is the unique smaller root in the permitted interval. For \(m=5\), the derivative numerator \(119t^2-210t+90\) stays positive on \(0\le t\le5/7\).

The \(m=1\) value is the largest. It exceeds \(1\) because \(511>21^2\). It exceeds the \(m=2\) value because
\[
7+2\sqrt{511}>3\sqrt{273},
\]
which follows after squaring from \(\sqrt{511}>13\). The \(m=3,m=4,m=5\) maxima are all below \(1\). Therefore
\[
\max_H R(H)
=
12\left(\frac12+\frac{\sqrt{511}}{42}\right)
=
6+\frac{2\sqrt{511}}7.
\]

At equality \(m=1\), so one normalized pairing equals
\[
y_1=\frac{35-\sqrt{511}}{119},
\]
and the other five all equal \((1-y_1)/5\). Their ratio simplifies to
\[
\frac{y_1}{(1-y_1)/5}
=
\frac{29-\sqrt{511}}{11}.
\]
All six pairings are positive, so the supporting hyperplane contains exactly one vertex. The Gram matrix is nonsingular, hence these pairings determine a unique normal direction. Consequently each ordered pair of distinct vertices gives one equality support, and no two such ordered pairs give the same support. This proves the count \(7\cdot6=42\).

## Verification

The included `verify.py` uses exact rational arithmetic with quadratic radicals. It reconstructs every one-variable chamber function, differentiates the rational functions algebraically, verifies the four radical critical points and values, checks the \(m=5\) endpoint argument, verifies the comparison selecting \(m=1\), and checks the equality pairing ratio and final volume constant.

As a separate geometric consistency check during derivation, the equality normal was reconstructed from the Gram matrix and the convex hull of the simplex together with its reflected vertices was evaluated directly; the numerical ratio agrees with
\[
6+\frac{2\sqrt{511}}7
\]
to floating-point precision. This numerical check is not used in the proof.

## Relationship to prior work

Horváth's 2013 preprint and 2014 paper stated that the corresponding maximum for a regular \(n\)-simplex is \(2n\) in every dimension. The later correction, first made public as arXiv:1811.12399 on 2018-11-29 and published in 2019, proves the \(2n\) value only for \(n\le4\), gives the exact five-dimensional value, and explicitly poses the higher-dimensional optimization as an open problem. The result above supplies the next dimension, \(n=6\), and shows that the maximum is approximately \(12.45865974598\), strictly larger than \(12\).

The corrected paper develops a two-parameter upper-bound method. The argument here instead uses the exact upper-facet volume formula and exploits a six-dimensional chamber symmetrization: for a fixed number of upper side facets and fixed total small pairing, both pairing groups must equalize. This reduces the full spherical optimization to five elementary one-variable rational functions.

## Limitations

This result solves only the six-dimensional regular-simplex case. It does not determine the optimum for dimensions \(n\ge7\), nor does it address nonregular simplices or nonorthogonal transformations. The originality assessment searched exact constants, the six-dimensional formulation, aliases involving reflected regular simplices and supporting hyperplanes, and later references to the corrected paper; an unindexed or differently phrased prior observation remains a residual risk.

## References

1. Á. G. Horváth, *An extremal problem of regular simplices: the five-dimensional case*, Journal of Geometry 110, 17 (2019). DOI: 10.1007/s00022-019-0472-4. Earliest public version: arXiv:1811.12399, 2018-11-29.
2. Á. G. Horváth, *On an extremal problem connected with simplices*, Beiträge zur Algebra und Geometrie 55 (2014), 415–428. DOI: 10.1007/s13366-013-0151-9. arXiv:1303.3454.
