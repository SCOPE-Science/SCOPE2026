# Three even geodesic-distance moments recover every finite flat cylinder, sharply

## Finding
For every positive circumference \(C\) and positive height \(H\), the first three nonzero even moments of intrinsic geodesic distance between two independent uniform points of the flat lateral cylindrical surface determine \(C\) and \(H\) uniquely, with a locally smooth inverse. Two such moments do not suffice for universal identification; the exact two-to-one parameter region is calculated below.

## Assumptions and scope
Work on the metric-measure cylinder \(\mathcal C_{C,H}=(\mathbb R/C\mathbb Z)\times[0,H]\), \(C>0\), \(H>0\), equipped with the flat product length metric, including both boundary circles, and probability measure \(d\theta\,dz/(CH)\). Let \(D\) be the intrinsic shortest-path geodesic distance between two independent samples; it is **not** their distance through the ambient three-dimensional space. Write \(m_{2j}=\mathbb E[D^{2j}]\), \(U=C^2/4>0\), \(V=H^2>0\), \(s=2U+V\), and \(x=U/s\in(0,1/2)\).

The exact moment formulas are
\[
m_2=s/6,\qquad m_4=\frac{s^2}{45}(11x^2-7x+3),\qquad m_6=\frac{s^3}{420}(-32x^3+110x^2-62x+15).
\]
Given the moments, recover \(s=6m_2\), find the roots of \(11x^2-7x+3=45m_4/s^2\) lying in \((0,1/2)\), and select the unique root satisfying the third-moment formula. Then \(C=2\sqrt{sx}\), \(H=\sqrt{s(1-2x)}\).

The sharp fold statement is: if \(\rho=m_4/m_2^2\), the admissible range is \(83/55\le \rho<12/5\); there are exactly two distinct geometries realizing the prescribed first two even moments precisely when \(83/55<\rho<9/5\), and exactly one otherwise. In the two-solution region, the two roots sum to \(7/11\). These statements include the fold point and all strictly positive heights and circumferences. The inverse from the embedded two-parameter moment surface into \((C,H)\) is locally smooth everywhere.

## Proof
The shortest circular arc between two independent uniform angles has length \(X\) uniform on \([0,C/2]\). Independently, the absolute difference \(Y\) of two independent uniform heights has density \(2(H-y)/H^2\) for \(0\le y\le H\). Every lifted shortest path realizes \(D^2=X^2+Y^2\). Therefore, for each integer \(j\ge0\),
\[
\mathbb E[X^{2j}]=\frac{U^j}{2j+1},\qquad
\mathbb E[Y^{2j}]=\frac{2V^j}{(2j+1)(2j+2)}.
\]
Expanding \((X^2+Y^2)^j\) for \(j=1,2,3\) gives
\[
m_2=\frac U3+\frac V6,\quad
m_4=\frac{U^2}5+\frac{UV}9+\frac{V^2}{15},\quad
m_6=\frac{U^3}7+\frac{U^2V}{10}+\frac{UV^2}{15}+\frac{V^3}{28}.
\]
Substituting \(U=sx\) and \(V=s(1-2x)\) yields the displayed normalized formulas.

The quadratic \(q(x)=(11x^2-7x+3)/45\) is strictly convex, with critical point \(x_0=7/22\). Its minimum is \(83/1980\), its value at \(x\downarrow0\) is \(1/15\), and its value at \(x\uparrow1/2\) is \(1/20\). Consequently, the normalized ratio \(\rho=36q(x)\) has range \([83/55,12/5)\). Every pair of distinct admissible roots satisfies \(x+y=7/11\). The intersection of the admissible interval with its reflection about \(7/22\) gives two distinct roots exactly for \(83/55<\rho<9/5\). At the critical value \(83/55\), the roots coincide, while at \(9/5\) the second root reaches the forbidden endpoint \(x=1/2\).

Define \(f(x)=(-32x^3+110x^2-62x+15)/420\). Under the twin-root constraint \(y=7/11-x\), exact polynomial factorization gives
\[
f(x)-f(y)=-\frac{2(x-y)}{12705}
\left(484\left(x-\frac7{22}\right)^2+26\right).
\]
The parenthesis is strictly positive on all real arguments; hence distinct candidates have distinct sixth moments and the three moments determine the cylinder uniquely. For instance, the distinct parameter choices \((s,x)=(1,1/4)\) and \((s,x)=(1,17/44)\) both give \(m_2=1/6\) and \(m_4=31/720\), proving that two moments cannot always distinguish cylinders. Their circumferences and heights are, respectively, \((1,1/\sqrt2)\) and \((\sqrt{17/11},\sqrt{5/22})\), and their sixth moments differ.

Finally, \(q'(x)=(22x-7)/45\) vanishes only at \(x_0=7/22\), whereas \(f'(x_0)=-52/12705\ne0\). Thus the vector map \(x\mapsto(q(x),f(x))\) has nowhere-vanishing derivative, and the preceding global injectivity plus the inverse-function theorem give local smoothness of the reconstruction. Scaling back through \(s\) is smooth at every positive \(C,H\).

## Verification
The embedded `verify.py` program independently recomputes the moment polynomials, strict algebraic twin separation, derivative at the fold, an explicit two-cylinder counterexample, and two-dimensional numerical integration against the exact independent coordinate density for five positive parameter pairs. Run with `python verify.py`; the decisive source of correctness is the complete analytic proof above, not finite numerical testing.

## Relationship to prior work
Venet (2016) explicitly studies exactly this flat cylinder's product geodesic metric but his principal results concern negative-definiteness of distance-power kernels and Gaussian random fields, not moment-based inverse identification. Mémoli and Needham (2018) formally study global distance distributions as geometric invariants and inverse problems, including manifold and sphere characterizations; their applicable framework motivates the question but the inspected relevant sections do not state a three-even-moment cylindrical reconstruction or the sharp two-moment fold. Balch–Peterson–Shonkwiler (2020) derive random geodesic-distance moments on homogeneous closed three-dimensional lens spaces, not on two-dimensional flat cylinders with boundary. These comparisons concern mathematical implications, not merely title overlap. The result is distinct from Euclidean chord-distance statistics of a filled solid cylinder: both the sampled measure and metric differ.

## Limitations
Only positive, finite, constant-circumference flat product cylinders with the uniform surface-area measure are treated. The observations are exact population moments; finite-sample stability is not quantified. Local smooth inverse behavior does not imply a uniform condition number approaching degenerate height/circumference limits. Priority remains provisional because incomplete cataloguing or other terminology might conceal earlier equivalent formulas.

## References
- Nil Venet, *Nonexistence of fractional Brownian fields indexed by cylinders*, arXiv:1612.05983, first submitted 2016-12-18, https://arxiv.org/abs/1612.05983.
- Facundo Mémoli and Tom Needham, *Distance distributions and inverse problems for metric measure spaces*, arXiv:1810.09646, first submitted 2018-10-23, https://arxiv.org/html/1810.09646v5.
- Brenden Balch, Chris Peterson, Clayton Shonkwiler, *Distributions of Distances and Volumes of Balls in Homogeneous Lens Spaces*, 2020, author-hosted full text consulted; arXiv:2004.13196, https://arxiv.org/abs/2004.13196.
