# A sharp smooth anticanonical net on the split quadric over \(\mathbf F_3\)

## Finding
Let \(S=\mathbf P^1_{\mathbf F_3}\times\mathbf P^1_{\mathbf F_3}\). There exists a three-dimensional vector space \(W\subset H^0(S,\mathcal O(2,2))\) with all thirteen rational projective members geometrically smooth; no vector space of dimension four can have this property. Thus the maximum possible vector-space dimension is exactly three (projective dimension two). Every **three-dimensional** all-smooth system has no rational base point. This last assertion concerns systems attaining the maximum dimension, not systems maximal by inclusion.

## Assumptions and scope
Coordinates are \(([s:t],[u:v])\), with \(s,t\) homogeneous coordinates on the first ruling and \(u,v\) on the second. Everything is defined over \(\mathbf F_3\). Smoothness means smoothness after extension to the algebraic closure. The assertion concerns all nonzero \(\mathbf F_3\)-linear combinations, up to \(\mathbf F_3^*\); it does not assert that every geometric member of the net is smooth.

The explicit generators of \(W\) are
\[
\begin{aligned}
F&=s^2u^2+stv^2+t^2u^2,\\
G&=s^2u^2+s^2uv+2s^2v^2+t^2uv,\\
H&=s^2u^2+2s^2uv+2stu^2+2stuv+t^2v^2.
\end{aligned}
\]
The displayed coefficients are elements of \(\mathbf F_3\).

## Proof
**Upper bound.** Fix any rational point \(P\in S(\mathbf F_3)\), and write \(\mathfrak m_P\) for the maximal ideal of the local ring. Restriction of sections of \(\mathcal O(2,2)\) to \(\operatorname{Spec}(\mathcal O_{S,P}/\mathfrak m_P^2)\) is a linear map with a three-dimensional target over \(\mathbf F_3\) (one value and two partial derivatives in local coordinates). On any subspace \(U\) of dimension at least four it has a nonzero kernel. A nonzero section in that kernel defines a divisor singular at \(P\). Thus every all-smooth \(U\) has dimension at most three.

**Attainment.** Write the coefficient vector of a bidegree-\((2,2)\) form in the order \(s^{2-i}t^i u^{2-j}v^j\) with \(0\le i,j\le2\), ordered lexicographically by \((i,j)\). The displayed generators have vectors

```
F = 1 0 0 0 0 1 1 0 0
G = 1 1 2 0 0 0 0 1 0
H = 1 2 0 2 2 0 0 0 1
```

They are independent by their last three coordinates. For each normalized \((a,b,c)\in\mathbf P^2(\mathbf F_3)\), put \(T=aF+bG+cH\) and write \(T=A(s,t)u^2+B(s,t)uv+C(s,t)v^2\). Its binary-quartic discriminant is \(\Delta_T=B^2-AC\), since \(4=1\) in \(\mathbf F_3\). The exact certificate in `verify.txt` lists all thirteen coefficient vectors. For each, dehomogenization at \(t=1\) gives a polynomial of degree at least three and coprime to its derivative. There are thus four distinct geometric roots, including the simple root at infinity in the degree-three case.

The three coefficients \(A,B,C\) cannot vanish simultaneously at a point, as that would force a multiple root of \(\Delta_T\). Over the algebraic closure the projection to the first ruling has two simple points over each nonbranch value. At a branch value, choose fiber coordinates putting the repeated root in an affine chart where the leading quadratic coefficient is a unit. Completing the square gives a local equation of the form \(y^2=g(x)\) with \(g\) vanishing to order one, so the curve is smooth there too. Separately, the exact calculation of the Jacobian ideal \((T,\partial T/\partial x,\partial T/\partial y)\) on each of four affine charts gives the unit ideal in all 52 tests. This verifies smoothness over the algebraic closure, not merely over a bounded list of finite extensions.

The divisor of a smooth \((2,2)\) section is geometrically connected by the cohomology sequence and \(H^1(S_{\overline{\mathbf F}_3},\mathcal O(-2,-2))=0\); smooth and connected implies geometrically integral. Its genus by adjunction is \((2-1)(2-1)=1\). Thus the exhibited space is an all-smooth genus-one net attaining the bound.

**Rational base points.** If a three-dimensional all-smooth \(U\) had a rational base point \(P\), the first-jet evaluation map would have zero value coordinate. Its image would have dimension at most two, forcing a nonzero member singular at \(P\), a contradiction.

## Verification
The accompanying `verify.py` (Python 3 with SymPy) enumerates the thirteen normalized combinations, checks independence, tests squarefreeness of their discriminants, and checks all 52 affine-chart Jacobian ideals. The exact discriminant coefficient vectors and the computation summary appear in `verify.txt`. The dimension bound and the rational-base-point assertion use the first-jet argument, not extrapolation from finite tests.

## Relationship to prior work
Asgarli–Ghioca formulate the all-smooth rational-member linear-system problem for projective hypersurfaces and provide small-field nets of plane conics. Asgarli–Ghioca–Reichstein establish sharp existence results for linear systems of smooth hypersurfaces in projective spaces over finitely generated fields. The first-jet dimension obstruction is the same standard principle; the upper-bound technique by itself is not claimed as new. The projective hypersurface results do not automatically imply smooth intersections with a fixed quadric, and constructions of all-smooth pencils do not by themselves imply existence of an all-smooth net.

## Limitations
The result does not enumerate or classify all nets. It concerns only \(\mathbf F_3\)-rational combinations, not smoothness of all geometric linear combinations. The base-point conclusion makes no assertion about systems maximal only by inclusion. Priority is assessed against examined sources, not every unindexed example.

## References
1. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields* (2022), arXiv:2203.07169, https://arxiv.org/abs/2203.07169.
2. S. Asgarli, D. Ghioca and Z. Reichstein, *Linear families of smooth hypersurfaces over finitely generated fields* (2022), arXiv:2207.00918, https://arxiv.org/abs/2207.00918.
