# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The geometric reduction is exact: for half-exterior angles
\(x_i=(\pi-A_i)/2\), one has \(\sum x_i=\pi\),
\(s/r=\sum\tan x_i\), \(K=rs\), and the interior-angle variance is four times the \(x_i\)-variance about \(\pi/4\).

The sharp trigonometric inequality is proved globally rather than only locally. The proof treats all finite boundary points, proves blow-up when a coordinate approaches \(\pi/2\), classifies constrained interior local minima via the strict convexity of
\(\sec^2x-2c_*(x-\pi/4)\), and then checks the only possible nonregular critical family explicitly. The one-variable monotonicity argument is algebraic after the substitution \(z=\tan b\); its sign reduction uses a polynomial with exactly one positive root by Descartes' rule of signs. The limiting family gives the same constant, establishing global optimality.

No empirical computation is used as a substitute for any step of the proof.

## Originality

**PASS, to the best of our knowledge.**

The classical qualitative inequality \(s\ge4r\), equivalently \(K\ge4r^2\), and its square equality case are established prior results attributed to T. A. Ivanova. Josefsson's 2023 square-characterization compilation records the result and a Jensen proof in the same angle variables. The 2025 square-characterization update was checked as current quadrilateral context.

Gui--Hu--Li (2026) give a quantitative Pólya--Szegő theorem for tangential polygons and explicitly mention an angular Jensen deficit, but the stated quantitative target is torsional rigidity and a perimeter ratio. The located descriptions do not state the present globally sharp constant for the Ivanova semiperimeter/area deficit, nor the degenerating sharpness family.

No located source states the displayed sharp angle-variance refinement or its constant. Residual originality risk remains because the core analytic inequality could occur in older sharp Jensen/trigonometric-inequality literature under terminology unrelated to tangential quadrilaterals.

## Value

**PASS.**

The result converts a classical equality characterization of the square into a global, dimensionless, sharp stability theorem with an explicit best constant and a complete explanation of why the extremal constant is governed by a degenerate boundary configuration rather than the local Hessian at the square. The same statement simultaneously refines both semiperimeter and area forms of Ivanova's inequality.

## Limitations

- Only Euclidean convex tangential quadrilaterals are treated.
- The stability variable is angle variance; no metric-shape or side-length stability estimate is claimed.
- The optimal constant is approached at a degenerate boundary configuration and is not attained by a proper nonsquare quadrilateral.
- No claim is made for the optimal constants of general tangential \(N\)-gons.
- Originality remains to the best of our knowledge, particularly because an equivalent sharp Jensen refinement could exist under different terminology.

## Sources checked

- Martin Josefsson, *Great compilation of characterizations of squares*, International Journal of Geometry 12 (2023), no. 3, 13–37.
  https://ijgeometry.com/wp-content/uploads/2023/06/2.-13-37.pdf
- Martin Josefsson and Mario Dalcín, *150 characterizations of squares*, International Journal of Geometry 14 (2025), no. 2.
  https://ijgeometry.com/vol-14-2025-no-2-april/
- Changfeng Gui, Yeyao Hu, Qinfeng Li, *A Quantitative Pólya--Szegő Theorem for Tangential Polygons*, arXiv:2607.28768v2 (2026).
  https://arxiv.org/abs/2607.28768
- MathWorld, *Tangential Quadrilateral*, for background area/semiperimeter formulas.
  https://mathworld.wolfram.com/TangentialQuadrilateral.html
