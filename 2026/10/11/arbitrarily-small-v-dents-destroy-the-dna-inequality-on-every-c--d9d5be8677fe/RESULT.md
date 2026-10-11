# Arbitrarily small V-dents destroy the DNA inequality on every \(C^2\) convex curve
## Finding
For a rectifiable closed plane curve \(\eta\), write
\[
\operatorname{{ac}}(\eta)=\frac{{\operatorname{{TC}}(\eta)}}{{L(\eta)}},
\]
where \(\operatorname{{TC}}\) is total absolute curvature and \(L\) is length. Let \(K\subset\mathbb R^2\) be a compact convex body with nonempty interior and \(C^2\) boundary \(\Gamma\), of perimeter \(p\). Then \(K\) admits arbitrarily small inward V-dents whose boundaries fail the DNA inequality.

More precisely, choose a point \(q\in\Gamma\) with positive curvature \(\kappa\). In tangent coordinates centered at \(q\), arrange that \(K\) lies locally above a graph \(y=f(x)\) with
\[
f(0)=f'(0)=0,\qquad f''(0)=\kappa>0.
\]
For sufficiently small \(t>0\), define
\[
A_t=(-t,f(-t)),\qquad B_t=(t,f(t)),\qquad X_t=(0,\kappa t^2).
\]
Replace the boundary arc from \(A_t\) to \(B_t\) through \(q\) by the two segments \(A_tX_t\) and \(X_tB_t\); call the resulting nonconvex cell \(K_t\). Then
\[
d_H(K,K_t)=O(t^2)
\]
and
\[
\operatorname{{ac}}(\partial K_t)
=
\frac{{2\pi}}{{p}}+\frac{{2\kappa}}{{p}}t+o(t).
\]
There is a fixed constant \(M>0\), depending only on \(K\), the chosen interior point, and the local dent construction, such that
\[
K_t^*=o+(1-Mt^2)(K-o)\subset K_t
\]
for all sufficiently small \(t\). Its boundary is convex and satisfies
\[
\operatorname{{ac}}(\partial K_t^*)
=
\frac{{2\pi}}{{(1-Mt^2)p}}
=
\frac{{2\pi}}{{p}}+O(t^2).
\]
Therefore \(\operatorname{{ac}}(\partial K_t^*)<\operatorname{{ac}}(\partial K_t)\) for all sufficiently small \(t\), so \(\partial K_t^*\) is a counterexample DNA inside the dented cell.

## Assumptions and scope
The outer undeformed boundary is a regular \(C^2\) convex Jordan curve. No strict-convexity or everywhere-positive-curvature hypothesis is needed: convexity gives nonnegative curvature, while total turning \(2\pi\) ensures that some point has positive curvature. The dent itself is piecewise smooth, with one reflex corner at \(X_t\) and convex corners at \(A_t\) and \(B_t\).

The conclusion is existential. It gives a specific V-dent family at a positive-curvature point and proves failure for every sufficiently small parameter in that family. It does not assert that every sufficiently small dent of a smooth convex curve fails. It also does not prove the full piecewise-smooth if-and-only-if criterion proposed by Larson.

## Proof
Because \(\Gamma\) is a \(C^2\) convex Jordan curve, its signed curvature is nonnegative and integrates to \(2\pi\). Hence a point \(q\) with \(\kappa(q)>0\) exists. In the tangent coordinates above,
\[
f(\pm t)=\frac{\kappa}{2}t^2+o(t^2),\qquad
f'(\pm t)=\pm\kappa t+o(t).
\]
The segment from \(A_t\) to \(X_t\) has slope
\[
m_-=
\frac{\kappa t^2-f(-t)}{t}
=
\frac{\kappa}{2}t+o(t),
\]
while the segment from \(X_t\) to \(B_t\) has slope
\[
m_+=
\frac{f(t)-\kappa t^2}{t}
=
-\frac{\kappa}{2}t+o(t).
\]
For small \(t\), both segments lie inside \(K\) and strictly above the removed boundary arc except at their endpoints. Thus they form a genuine inward dent. The signed turn at \(X_t\) is negative, with magnitude
\[
\beta_t
=
\arctan(m_-)-\arctan(m_+)
=
\kappa t+o(t).
\]
The turns at \(A_t\) and \(B_t\) remain positive, and the unchanged smooth part of the boundary has nonnegative curvature. Hence \(X_t\) is the only negative-turn point. The total signed turn of the simple closed dented boundary is still \(2\pi\), so replacing the negative turn by its absolute value adds twice its magnitude:
\[
\operatorname{{TC}}(\partial K_t)
=
2\pi+2\beta_t
=
2\pi+2\kappa t+o(t).
\]

The removed smooth arc has length
\[
\int_{{-t}}^t\sqrt{{1+f'(x)^2}}\,dx
=
2t+\frac{{\kappa^2}}3t^3+o(t^3).
\]
Each replacement segment has length
\[
t+\frac{{\kappa^2}}8t^3+o(t^3),
\]
so
\[
L(\partial K_t)=p-\frac{{\kappa^2}}{{12}}t^3+o(t^3)=p+O(t^3).
\]
Combining numerator and denominator gives
\[
\operatorname{{ac}}(\partial K_t)
=
\frac{{2\pi}}{{p}}+\frac{{2\kappa}}{{p}}t+o(t).
\]

It remains to place a competing DNA inside the dent. On the interval \([-t,t]\), the vertical gap between the V-shaped replacement and the removed graph is \(O(t^2)\), uniformly after the rescaling \(x=st\). Hence the removed cap is contained in a \(Ct^2\)-neighborhood of \(\partial K\) for some fixed \(C>0\), and therefore \(d_H(K,K_t)=O(t^2)\).

Choose an interior point \(o\) and \(r>0\) with the closed disk \(B(o,r)\subset\operatorname{{int}}K\). For \(0<\varepsilon<1\), set
\[
K^\varepsilon=o+(1-\varepsilon)(K-o).
\]
Convexity gives
\[
K^\varepsilon+\varepsilon r B(0,1)\subset K,
\]
so every point of \(K^\varepsilon\) is at least \(\varepsilon r\) from \(\partial K\). Choose \(M>C/r\) and put \(\varepsilon=Mt^2\). For small \(t\), the contracted body cannot meet the removed cap, hence \(K^{Mt^2}\subset K_t\).

The boundary of \(K^{Mt^2}\) is a homothetic copy of \(\Gamma\). Its total absolute curvature is \(2\pi\), and its perimeter is \((1-Mt^2)p\). Thus
\[
\operatorname{{ac}}(\partial K^{Mt^2})
=
\frac{{2\pi}}{{(1-Mt^2)p}}
=
\frac{{2\pi}}{{p}}+O(t^2).
\]
Since the dented cell's excess above \(2\pi/p\) is the positive linear term \((2\kappa/p)t\), the inner homothetic curve has strictly smaller average curvature for every sufficiently small \(t\). This is exactly a failure of the DNA inequality.

## Verification
The local Taylor calculation was checked independently at each step: the reflex angle has first-order size \(\kappa t\), the perimeter perturbation is cubic rather than linear or quadratic, and the homothetic competitor changes average curvature only at quadratic order. A direct unit-circle check with \(\kappa=1\) gives
\[
\frac{\operatorname{{ac}}(\partial K_t)-1}{t}\longrightarrow\frac1\pi,
\]
which agrees with the general coefficient \(2\kappa/p\) because the unit circle has \(p=2\pi\). This numerical check is only a sanity check; the proof is the Taylor and containment argument above.

The containment step is quantitative: the removed cap has depth \(O(t^2)\), while a homothetic contraction by \(Mt^2\) has inward clearance at least \(Mrt^2\). Taking \(Mr>C\) gives the required inclusion.

## Relationship to prior work
Lagarias and Richardson proved the DNA inequality for convex cells. Tabachnikov's exposition formulates the average-curvature inequality for convex cells and discusses its classical special cases. Larson studied nonconvex polygonal cells and classified when sufficiently small dents of a polygonal edge preserve the DNA inequality.

The decisive prior comparison is Larson's concluding remark. After stating a conjectural extension of his polygonal dent theorem to piecewise-smooth convex boundaries, he explicitly notes that it would imply failure for arbitrarily small dents of smooth convex curves and says that this corollary should be approachable by a counterexample analogous to his polygonal construction. The theorem here supplies that missing smooth-convex corollary, with a direct local construction and a homothetic interior competitor. It does not claim Larson's stronger proposed piecewise-smooth classification.

## Limitations
The dented cell is piecewise smooth rather than \(C^2\); the undeformed convex cell is \(C^2\). The theorem is local and existential: it identifies one canonical family of V-dents at a positive-curvature point. No claim is made about all possible dent shapes, about a sharp finite dent-size threshold, or about the full piecewise-smooth classification conjectured by Larson.

The originality search found no later indexed statement proving this smooth-dent corollary, but an unindexed note, thesis, or differently named treatment of average total curvature remains a residual risk. The 1997 Lagarias--Richardson full text was not available from the accessible author PDF link during comparison; its published abstract and Larson's detailed use of it establish that it concerns convex cells, not the nonconvex dent theorem proved here.

## References
1. E. Larson, *The DNA Inequality in Non-Convex Regions*, arXiv:0801.1929; *Advances in Geometry* 10 (2010), 221--248, DOI 10.1515/ADVGEOM.2010.008. Section 9 explicitly states the smooth-convex small-dent corollary as an expected consequence not proved there.
2. J. C. Lagarias and T. J. Richardson, *Convexity and the Average Curvature of Plane Curves*, *Geometriae Dedicata* 67 (1997), 1--30, DOI 10.1023/A:1004912521664.
3. S. Tabachnikov, *A Tale of a Geometric Inequality*, MASS Selecta, American Mathematical Society, 2003, 257--262.
