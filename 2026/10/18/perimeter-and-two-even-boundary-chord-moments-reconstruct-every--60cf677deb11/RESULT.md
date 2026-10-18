# Perimeter and two even boundary-chord moments reconstruct every Euclidean triangle

## Finding

Let \(T\) be a nondegenerate Euclidean triangle with side lengths \(a,b,c\), perimeter \(L=a+b+c\), and area \(A>0\). Independently select \(X,Y\) uniformly by arclength on the entire boundary \(\partial T\), and put \(D=\|X-Y\|_2\). Set
\[
h=\frac{16A^2}{L^4}=\prod_{s\in\{a,b,c\}}\left(1-\frac{2s}{L}\right),\qquad
p=\frac{ab+bc+ca}{L^2}.
\]
The exact second and fourth moments are
\[
\boxed{M_2:=\mathbb E D^2=\frac{L^2(1-3h)}{24},\qquad
M_4:=\mathbb E D^4=\frac{L^4(3-45h+20hp)}{720}.} \tag{1}
\]
Thus the measured triple \((L,M_2,M_4)\) uniquely determines the *unordered* side-length triple, hence the triangle up to Euclidean congruence. Explicitly, recover
\[
h=\frac{1-24M_2/L^2}{3},\qquad
p=\frac{720M_4/L^4-3+45h}{20h},\qquad
q=\frac{4p-1-h}{8}; \tag{2}
\]
then the three positive roots of
\[
t^3-t^2+pt-q=0 \tag{3}
\]
are exactly \(a/L,b/L,c/L\), counted with multiplicity.

The dimensionless fourth-moment amplification \(Q=M_4/M_2^2\) obeys the sharp global inequalities
\[
\boxed{\frac85\le Q<\frac{12}5.} \tag{4}
\]
Equality on the left occurs if and only if the triangle is equilateral. The right value is an unattained supremum, approached whenever triangles degenerate at fixed perimeter.

There is also a complete fixed-perimeter-and-area refinement. Fix \(L>0\) and \(0<h<1/27\). Let \(t_-\in(0,1/3)\) and \(t_+\in(1/3,1/2)\) be the unique positive roots of \(t^2(1-2t)=h\) in these intervals, and set \(p_\pm=(1+2t_\pm-3t_\pm^2)/4\). Then
\[
\boxed{\frac{L^4(3-45h+20hp_-)}{720}\le M_4\le
\frac{L^4(3-45h+20hp_+)}{720}.} \tag{5}
\]
Both endpoints are attained **only** by the indicated isosceles shape up to relabeling: the lower extremizer has two equal longer sides, and the upper extremizer two equal shorter sides. Every intermediate value occurs. For \(h=1/27\) the sole permissible shape is equilateral and the two endpoints coincide.

## Assumptions and scope

Each of the two endpoints is chosen independently, with replacement, from normalized arclength on \(\partial T\); this is not the invariant-random-line chord model and not uniform sampling inside the triangle. The perimeter is supplied as an independent length observable in the reconstruction. Every triangle throughout has strictly positive area and satisfies strict triangle inequalities. All statements are invariant under translation, rotation and reflection; the dimensionless ratios are invariant under common scaling. The right-hand endpoint of (4) is not realized by a nondegenerate triangle. In (5) area is prescribed through \(h=16A^2/L^4\), not just its limiting value.

## Proof

**1. Direct moment computation.** Write \(u,v\) for independent uniform variables on \([0,1]\). Conditional on both points belonging to a particular side of length \(a\), their squared distance is \(a^2(u-v)^2\); elementary integration gives
\[
\mathbb E(u-v)^2=\frac16,\qquad \mathbb E(u-v)^4=\frac1{15}.
\]
Conditional on two *different* sides of respective lengths \(a,b\) meeting at a vertex opposite the third side \(c\), the cosine law gives
\[
D^2=a^2u^2+b^2v^2-(a^2+b^2-c^2)uv.
\]
Writing \(S=a^2+b^2-c^2\), two more elementary integrations yield
\[
J_2(a,b;c)=\mathbb E D^2=\frac{a^2+b^2}{12}+\frac{c^2}{4},
\]
\[
J_4(a,b;c)=\mathbb E D^4
=\frac{a^4+b^4}{5}+\frac{S^2+2a^2b^2}{9}-\frac{(a^2+b^2)S}{4}.
\]
The probability of selecting an ordered pair of sides of lengths \(a,b\) is \(ab/L^2\). Summing same-side and ordered different-side terms gives the exact identities
\[
M_2=\frac1{L^2}\left[\frac{a^4+b^4+c^4}{6}
+2\sum_{\mathrm{cyc}}abJ_2(a,b;c)\right],
\]
\[
M_4=\frac1{L^2}\left[\frac{a^6+b^6+c^6}{15}
+2\sum_{\mathrm{cyc}}abJ_4(a,b;c)\right]. \tag{6}
\]
Set \(x=1-2a/L\), \(y=1-2b/L\), \(z=1-2c/L\). Strict triangle inequalities imply \(x,y,z>0\) and \(x+y+z=1\). Heron's identity gives \(xyz=16A^2/L^4=h\). Also
\[
xy+yz+zx=4p-1.
\]
Expanding (6) into elementary symmetric polynomials, replacing \(xyz\) by \(h\) and \(xy+yz+zx\) by \(4p-1\), gives (1). The standalone symbolic checker performs this expansion directly from the four elementary one-dimensional integrals, without assuming (1).

**2. Exact reconstruction.** For a nondegenerate triangle \(h=xyz>0\), so each division in (2) is legal. Since \(a/L=(1-x)/2\) and cyclically, elementary symmetric products give
\[
\sum a/L=1,\quad
\sum_{i<j}\frac{a_i a_j}{L^2}=p,\quad
\frac{abc}{L^3}=\frac{xy+yz+zx-xyz}{8}=q.
\]
Vieta's formulas establish (3). Therefore any two triangles having equal \((L,M_2,M_4)\) have equal side multisets, and are congruent by side-side-side. No choice of orientation or labeling can be inferred from these symmetric data.

**3. Sharp global ratio bound.** From (1),
\[
Q=\frac{4(3-45h+20hp)}{5(1-3h)^2},
\]
so straightforward subtraction gives
\[
Q-\frac85=\frac{4(1-33h-18h^2+20hp)}{5(1-3h)^2},\qquad
\frac{12}5-Q=\frac{4h(27+27h-20p)}{5(1-3h)^2}. \tag{7}
\]
By arithmetic-geometric mean, \(xy+yz+zx\ge3(xyz)^{2/3}=3h^{2/3}\); therefore \(p\ge(1+3h^{2/3})/4\). The first numerator in (7) is consequently at least
\[
1-28h-18h^2+15h^{5/3}=f(u),\qquad u=3h^{1/3}\in(0,1].
\]
The polynomial \(f(u)=1-28u^3/27+5u^5/81-2u^6/81\) satisfies \(f(1)=0\) and
\[
f'(u)=-\frac{u^2}{81}(252-25u^2+12u^3)<0\quad (0<u\le1).
\]
Thus \(Q\ge8/5\), with equality only if \(u=1\), equivalently \(x=y=z=1/3\), the equilateral triangle. Also \(p\le1/3\), because normalized positive side lengths sum to one, so the second numerator in (7) is positive. Finally, if a sequence of strict triangles degenerates while maintaining a fixed perimeter, its area tends to zero, so \(h\downarrow0\), and (1) yields \(Q\to12/5\). Both constants are sharp.

**4. Complete fixed-area envelope.** At fixed \(L,h\), formula (1) is strictly increasing in \(p\). Thus maximize/minimize \(\sigma_2=xy+yz+zx\) on the level set
\[
\mathcal C_h=\{(x,y,z):x,y,z>0,\ x+y+z=1,\ xyz=h\}.
\]
For \(0<h<1/27\), this is a compact smooth curve inside the positive simplex; gradients of the two constraints are independent except at \(x=y=z\), which is excluded. Lagrange multipliers for \(\sigma_2\), in the form \(\sigma_2=(1-\sum x_i^2)/2\), imply that each coordinate solves a common quadratic equation, so any extremizer has two equal coordinates. Setting \(x=y=t\), \(z=1-2t\) gives \(t^2(1-2t)=h\), with exactly two positive roots \(t_-\in(0,1/3)\), \(t_+\in(1/3,1/2)\). The corresponding values are \(\sigma_2=2t-3t^2\). The third real root of \(t^2(1-2t)=h\) is negative and larger than \(-1/6\), so the sum of the two positive roots lies strictly between \(1/2\) and \(2/3\). Therefore
\[
(2t_+-3t_+^2)-(2t_--3t_-^2)
=(t_+-t_-)[2-3(t_++t_-)]>0.
\]
This proves (5), including distinct extremizers. Their normalized side lengths are \(((1-t)/2,(1-t)/2,t)\): at \(t_-\) the equal sides are longer, at \(t_+\) shorter. Every intermediate \(p\) occurs because \(\mathcal C_h\) is connected: it is the boundary of the compact convex superlevel set \(\{x,y,z>0:x+y+z=1,\ \log x+\log y+\log z\ge\log h\}\) in its affine plane. The equilateral case \(h=1/27\) follows directly from AM-GM.

## Verification

The included `checker.py` and `requirements.txt` are standalone. Run `python checker.py` with the declared SymPy dependency. The checker directly integrates conditional same-side/different-side distances, verifies both moment formulas as exact rational symbolic identities, checks the algebra in (7) and the derivative certificate, checks Vieta reconstruction for four exact rational side triples, and compares both moments against four independent direct geometric boundary-endpoint sampling experiments of 60,000 pairs each. Its successful terminal marker is `TRIANGLE_BOUNDARY_CHORD_MOMENTS_OK`. The universal ratio and envelope inequalities are established in the proof, not extrapolated from finite experiments. No rounding or black-box symbolic inequality solver is needed for those universal claims.

## Relationship to prior work

Bonnet, Gusakova, Thäle, and Zaporozhets (first publicly posted 2020) analyze sharp *mean distance* inequalities for random points in convex bodies; that work motivates the geometric distance observable but does not give the present fourth boundary-endpoint moment or its shape inverse. Bäsel (2021) computes moments for **area-uniform points in regular polygons**, whereas here both points are uniform by *boundary arclength* and arbitrary scalene triangles are included. A 2026 published result establishes the **second** boundary-endpoint distance moment for arbitrary triangles, which is precisely \(M_2\) in (1); it does not yield the new \(M_4\), the reconstruction from the pair, or the sharp fourth-to-second ratio. A separate published result on the fourth chord moment for parallelograms uses another body family and a boundary-versus-area amplification observable, so does not imply this triangle inverse theorem.

Gates (1982) studies recognition of triangles via **odd moments of random chord lengths** under a chord-sampling convention that cannot be established from the accessible abstract. Its abstract neither specifies two independent arclength-uniform boundary endpoints nor proves determination from the *second and fourth* moments together with perimeter. The full text was not accessible for detailed comparison, so unrecognized overlap remains a priority risk. This work makes no claim to be the first to study triangle reconstruction from a chord distribution under other sampling conventions.

## Limitations

The inverse statement requires the perimeter as data, nonzero triangle area, and the two even moments of *independent arclength-uniform endpoint distances*. It neither reconstructs orientation nor extends as stated to other polygons or invariant-line chord distributions. Exact formulas do not by themselves quantify numerical conditioning of reconstruction; in particular, recovery of \(p\) divides by \(h\), which deteriorates near degeneration. The analysis is a same-model mathematical derivation without independent external validation, and the bibliographic survey does not exclude an earlier unindexed or inaccessible equivalent formula.

## References

1. G. Bonnet, A. Gusakova, C. Thäle, D. Zaporozhets, *Sharp inequalities for the mean distance of random points in convex bodies*, arXiv:2010.03351v1 (first publicly posted 2020-10-07), https://arxiv.org/abs/2010.03351.
2. U. Bäsel, *The moments of the distance between two random points in a regular polygon*, arXiv:2101.03815v1 (first publicly posted 2021-01-11), https://arxiv.org/abs/2101.03815.
3. J. Gates, *Recognition of triangles and quadrilaterals by chord length distribution*, Journal of Applied Probability 19 (1982), 873–879, DOI:10.2307/3213843. Abstract accessible; full text not inspected.
4. *Exact second-moment boundary gap for arbitrary Euclidean triangles*, public mathematical research record (2026), record identifier d886b40f95a8.
5. *Fourth-chord moment amplification and angular phase transition for parallelograms*, public mathematical research record (2026), record identifier 45b0568cfb6e.
