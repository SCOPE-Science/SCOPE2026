# Product normalization of the unlinked-circle edge surface
## Finding
For the two unlinked unit circles in Example 3.4 of Nash–Pir–Sottile–Ying, write the stationary-bisecant curve as
\[
E:\ s^2u^2-3s^2v^2-3t^2u^2+5t^2v^2=0\subset\mathbb P^1\times\mathbb P^1.
\]
Let \(\pi_1,\pi_2:E\to\mathbb P^1\) be the projections and let \(\mathcal E\subset\mathbb P^3\) be the degree-eight edge surface swept by the corresponding stationary bisecants. Then the normalization of \(\mathcal E\) is
\[
E\times\mathbb P^1.
\]
More intrinsically, the normalization map is induced by
\[
X=\mathbb P_E\!\left(\pi_1^*\mathcal O_{\mathbb P^1}(-2)\oplus\pi_2^*\mathcal O_{\mathbb P^1}(-2)\right)\longrightarrow\mathcal E,
\]
and the two summands are isomorphic on \(E\). The elliptic curve \(E\) has
\[
j(E)=\frac{{24918016}}{{45}}.
\]
The two tautological endpoint sections of \(X\) map with degree two to the two source conics; this gives a normalization-level explanation for their generic double-curve behavior on \(\mathcal E\).

## Assumptions and scope
Work over \(\mathbb C\). The two conics are exactly those of Example 3.4, with parametrizations
\[
[s:t]\mapsto[s^2+t^2:s^2-t^2:2st:0]
\]
and
\[
[u:v]\mapsto[u^2+v^2:2u^2+4v^2:0:2uv].
\]
The source proves that the associated edge curve is irreducible of bidegree \((2,2)\), that the ruled edge surface has degree eight in this disjoint non-tangent case, and that the conics are generically double curves. The claim here concerns the normalization, the associated projective bundle, and the exact modulus of this particular elliptic ruling curve.

## Proof
Put \(A=\pi_1^*\mathcal O_{\mathbb P^1}(1)\) and \(B=\pi_2^*\mathcal O_{\mathbb P^1}(1)\). The defining equation rewrites as
\[
(s^2-3t^2)(u^2-3v^2)=4t^2v^2.
\]
Viewed as a quadratic equation in \([u:v]\), its discriminant vanishes exactly at \(s/t=\pm\sqrt3\) and \(s/t=\pm\sqrt{5/3}\), all simple. Thus the double cover \(E\to\mathbb P^1\) is smooth, so \(E\) is an elliptic curve.
On \(E\), the rational function \((s^2-3t^2)/t^2\) has a double zero at each of the two points over \(v=0\) and a double pole at each of the two points over \(t=0\). If \(A_\infty\) and \(B_\infty\) denote those two degree-two fibers, then
\[
\operatorname{div}\!\left(\frac{{s^2-3t^2}}{{t^2}}\right)=2B_\infty-2A_\infty.
\]
Hence \(A^{\otimes2}\simeq B^{\otimes2}\), and therefore
\[
\pi_1^*\mathcal O(-2)\simeq\pi_2^*\mathcal O(-2).
\]

For each \((p,q)\in E\), the corresponding ruling is the line joining the two conic points. Because each conic parametrization is quadratic, the endpoint vectors define line subbundles
\[
L_1=\pi_1^*\mathcal O(-2),\qquad L_2=\pi_2^*\mathcal O(-2)
\]
of the trivial rank-four bundle. Thus the incidence surface is \(X=\mathbb P_E(L_1\oplus L_2)\). Since \(L_1\simeq L_2\), twisting by \(L_1^{-1}\) gives
\[
X\simeq\mathbb P_E(\mathcal O_E\oplus\mathcal O_E)\simeq E\times\mathbb P^1.
\]

The map \(X\to\mathbb P^3\) is fiberwise the isomorphism onto the corresponding secant line. Its hyperplane class \(H\) satisfies \(H^2=8\): indeed \(\deg L_1=\deg L_2=-4\), so for the projective bundle of lines \(H^2=-\deg(L_1\oplus L_2)=8\). Since the image \(\mathcal E\) has degree eight, the map has generic degree one.

It remains to exclude a contracted curve. A contracted curve cannot lie in a fiber, because every fiber maps isomorphically to a line. A contracted curve dominating \(E\) would force one fixed point of \(\mathbb P^3\) to lie on every ruling. This does not occur: the three edge-curve points \((1,1),(-1,1),(1,-1)\) give rulings whose first pair meets at the second-conic point \([2:6:0:2]\), while the first and third meet at the first-conic point \([2:0:2:0]\); these points are distinct. Hence the proper map is quasi-finite, therefore finite. Being finite and birational from the smooth surface \(X\), it is the normalization of \(\mathcal E\).

For the modulus, on the affine chart \(t=v=1\) the curve is
\[
(x^2-3)(y^2-3)=4.
\]
The double cover \(E\to\mathbb P^1_x\) is branched at \(x=\pm\sqrt{{5/3}}\) and \(x=\pm\sqrt3\). One cross-ratio representative is
\[
\lambda=\frac12+\frac{{7\sqrt5}}{{30}}.
\]
Substitution into the standard four-branch-point formula
\[
j=256\frac{{(\lambda^2-\lambda+1)^3}}{{\lambda^2(\lambda-1)^2}}
\]
gives \(j(E)=24918016/45\).

## Verification
The accompanying exact checker `artifacts/verify.py` uses rational arithmetic and arithmetic in \(\mathbb Q(\sqrt5)\). It checks the bihomogeneous factor identity, the three edge-curve witness points, the linear independence needed for the two ruling intersections, and the exact simplification of the displayed \(j\)-formula to \(24918016/45\). The divisor argument and projective-bundle intersection computation are symbolic proofs recorded above rather than finite experiments.

## Relationship to prior work
Nash–Pir–Sottile–Ying compute the Example 3.4 edge curve, prove it is irreducible, identify the ruled edge surface, prove degree eight under the relevant hypotheses, and explain that the two conics are generically multiplicity-two self-intersection curves. They also give the general branch-point formula for the \(j\)-invariant of a smooth \((2,2)\)-edge curve. Their text does not identify the normalization of Example 3.4 as a trivial \(\mathbb P^1\)-bundle or give this example's exact \(j\)-value. Searches for the exact equation together with normalization/product-bundle terminology and for the exact \(j\)-value did not locate a source making the combined statement.

## Limitations
This result is specific to the explicit unlinked-circle example. It does not assert that the normalization is a product for a general pair of conics, and it does not classify the local analytic singularities of \(\mathcal E\) at special points of the double curves. The exact \(j\)-value is a consequence of the branch points; the structurally stronger part is the two-torsion line-bundle relation that trivializes the incidence normalization.

## References
Nash, E. D.; Pir, A. F.; Sottile, F.; Ying, L., *Convex Hull of Two Circles in R^3*, arXiv:1612.09382, especially Theorem 2.1, Example 3.4, Theorem 3.5, Example 3.7, and the branch-point \(j\)-formula preceding Theorem 3.10.
