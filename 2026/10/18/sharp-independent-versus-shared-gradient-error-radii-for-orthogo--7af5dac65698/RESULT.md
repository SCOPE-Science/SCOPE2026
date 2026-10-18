# Sharp independent-versus-shared gradient-error radii for orthogonal planar Pareto descent

## Finding
Let \(a,b>0\) and let the exact gradients of two smooth objectives at a point in \(\mathbb R^2\) be \(g_1=(a,0)\) and \(g_2=(0,b)\). From approximations \(h_1,h_2\), define the minimum-norm multi-gradient \(p=\operatorname{argmin}\{\|z\|_2:z\in\operatorname{conv}\{h_1,h_2\}\}\). A step in direction \(-p\) decreases both objectives to first order exactly when both coordinates of \(p\) are positive.

**Independent perturbation radius.** For every \(\delta<\min(a,b)/2\) and every pair \(\|h_i-g_i\|_2\le\delta\), the vector \(p\) has both coordinates strictly positive. This guarantee is sharp: at \(\delta=\min(a,b)/2\), admissible approximations make at least one true directional derivative vanish, and every larger error budget permits a strict first-order increase of one objective.

**Perfectly shared perturbation radius.** If the same vector \(e\) perturbs both gradients, so that \(h_i=g_i+e\), the sharp uniform guarantee improves to \(\|e\|_2<ab/\sqrt{a^2+b^2}\). At equality a shared displacement can produce \(p=0\); at every greater budget a shared displacement can give a strict first-order increase in both objectives. The ratio of the shared-error radius to the independent-error radius lies in \([\sqrt2,2)\), with the left endpoint attained at \(a=b\). Thus the correlation geometry of gradient-estimation errors changes the sharp pointwise safety margin, even when each estimator has the same individual norm bound.

## Assumptions and scope
All computations use the Euclidean norm on \(\mathbb R^2\). Both true gradients are nonzero and mutually orthogonal, with positive orientation fixed by the chosen orthonormal basis. The projected combination is computed exactly, with all convex weights in \([0,1]\). In the independent model, each of the two errors lies in a closed Euclidean disk of radius \(\delta\); no independence in the probabilistic sense is assumed. In the shared model, the errors are identical vectors (not merely statistically correlated). The two radii are pointwise deterministic worst-case thresholds, not bounds on a full stochastic optimization trajectory.

## Proof
**Projection geometry.** Write \(h_1=(u_1,v_1)\), \(h_2=(u_2,v_2)\). The projection \(p\) onto their segment is unique and depends continuously on the two endpoints. If it lies in the relative interior and is nonzero, \(p\cdot(h_1-h_2)=0\). If \(p=h_1\), then \(p\cdot(h_2-h_1)\ge0\); if \(p=h_2\), then \(p\cdot(h_1-h_2)\ge0\). All three assertions follow by differentiating the squared norm along the segment.

**Independent perturbations.** Put \(\mu=\min(a,b)\) and assume \(\delta<\mu/2\). Each admissible endpoint pair satisfies
\[
 u_1\ge a-\delta>\delta\ge u_2,\qquad v_2\ge b-\delta>\delta\ge v_1.
\]
In particular, \(u_1>0\) and \(v_2>0\). To see that the segment projection cannot have zero first coordinate, suppose \(p=(0,y)\). If \(p=h_1\), this contradicts \(u_1>0\). If \(p=h_2\), then \(u_2=0\), \(y=v_2>0\), and \(p\cdot(h_1-h_2)=v_2(v_1-v_2)<0\), contrary to the endpoint optimality condition. If the projection is interior and \(y\ne0\), interior orthogonality gives \(v_1=v_2\), again impossible. The case \(p=0\) is excluded below. The zero-second-coordinate case is symmetric: neither endpoint can be the projection, and an interior projection \(p=(x,0)\) with \(x\ne0\) would require \(u_1=u_2\).

For completeness, the unperturbed segment is at distance \(d_0=ab/\sqrt{a^2+b^2}\) from the origin; \(d_0\ge\mu/\sqrt2>\delta\). Every convex combination of perturbed endpoints is within \(\delta\) of the same convex combination of true endpoints, hence \(\|p\|\ge d_0-\delta>0\). Continuously scale both endpoint errors from zero to their chosen values. Along this path the projection cannot have a zero coordinate. Initially the projection equals
\[
 p_0=\left(\frac{ab^2}{a^2+b^2},\frac{a^2b}{a^2+b^2}\right),
\]
which has positive coordinates. Both coordinates therefore remain positive at the final perturbation.

For sharpness, first suppose \(a\ge b\) and set \(d=b/2\). At the boundary choose \(h_1=(a,d)\) and \(h_2=(0,b-d)=(0,d)\). Both errors have norm \(d\), and \(p=h_2\) by the endpoint optimality condition. Hence \(g_1\cdot p=0\). For any \(\delta>d\), choose \(d<d'<\min(\delta,b)\) and then \(\gamma>0\) sufficiently small that \(\sqrt{(d')^2+\gamma^2}<\delta\) and
\[
 (b-d')(2d'-b)\ge\gamma(a+\gamma).
\]
With \(h_1=(a,d')\), \(h_2=(-\gamma,b-d')\), the endpoint condition shows \(p=h_2\), so \(g_1\cdot p=-a\gamma<0\). Interchange the coordinate labels when \(b>a\). Thus the independent threshold is exact, including strict ascent above it.

**Perfectly shared error.** Put \(h_1=(a+u,v)\), \(h_2=(u,b+v)\), where \(e=(u,v)\) and \(\|e\|<d_0\). Every point \(z\) of their segment satisfies \((b,a)\cdot z=ab+bu+av>0\), by Cauchy–Schwarz. If the projection is interior, its orthogonality to \(h_1-h_2=(a,-b)\) makes it a positive multiple of \((b,a)\), so both coordinates are positive. If \(p=h_1\), the endpoint condition requires \(-a(a+u)+bv\ge0\); since \(a+u\ge a-\|e\|>0\), this forces \(v>0\). If \(p=h_2\), its endpoint condition requires \(au-b(b+v)\ge0\), and \(b+v>b-\|e\|>0\) forces \(u>0\). Thus either endpoint is also strictly positive in both coordinates.

At the radius \(d_0\), take \(e=-p_0\); the translated segment contains the origin, so \(p=0\). For any larger error allowance, choose a small \(\varepsilon>0\) and \(e=-(1+\varepsilon)p_0\) inside that allowance. The projection is then \(p=-\varepsilon p_0\): the nearest point remains in the relative interior because the translated line is orthogonal to \(p_0\) and \(p_0\) is an interior point of the original segment. Both coordinates of \(p\) are negative, so both true directional derivatives \(-g_i\cdot p\) are strictly positive. The radius ratio is
\[
 \frac{d_0}{\mu/2}=\frac{2\max(a,b)}{\sqrt{a^2+b^2}}\in[\sqrt2,2).
\]
This completes the classification.

## Verification
The standalone `verify.py` uses only Python's standard `fractions` and `itertools` modules. It computes the exact nearest point of a segment, exhausts rational perturbation grids for four asymmetric or symmetric gradient pairs, verifies strict positivity below both radii, and checks rational boundary and supercritical witnesses. Run `python verify.py`. The observed output is `PASS 12983 exact-rational assertions/cases`. The proof above, rather than the finite grid, supplies the universal quantifiers.

## Relationship to prior work
The minimum-norm convex combination is classical multi-gradient descent. Zhao, You, Dao, and Peng (2026) retain that server-side combination in a federated momentum/variance-reduced method and explicitly reuse a sample across objectives, but do not classify the pointwise worst-case true-descent radius for orthogonal gradients. Huang and Chen (2026) prove regularity-dependent Lipschitz and general half-Hölder bounds for the conflict-avoidant direction; those are direction-difference estimates and do not state or imply the two sharp coordinate-sign radii without additional geometric analysis. The present result concerns how structured versus unstructured *bounded errors* change a deterministic first-order descent certificate; it neither claims to originate the projection method nor obtains stochastic convergence rates.

## Limitations
The exact radii apply to two-dimensional orthogonal true gradients, and to exact projection onto a segment. Shared errors mean identical perturbation vectors, not merely noise derived from the same input or positive correlation. Neither Euclidean error budget alone nor perfect sharing models every federated estimator. The theorem gives no uniform positive numerical stepsize for nonlinear objectives without further smoothness and lower-margin information. The stronger shared radius need not hold for distinct, correlated task errors. Prior literature may contain equivalent planar robust-projection statements under different terminology; publication priority is not independently certified.

## References
- Zhao, Y., You, C., Dao, M. N., and Peng, Z.-Y. (2026), *A Momentum-Based Variance-Reduced Algorithm for Federated Multiobjective Optimization*, arXiv:2608.22945, first version August 24, 2026, https://arxiv.org/abs/2608.22945.
- Huang, C. and Chen, L. (2026), *Regularity-Aware Stochastic MGDA with Adaptive Conflict-Avoidant Update Direction Control*, arXiv:2607.15412, https://arxiv.org/abs/2607.15412.
- Désidéri, J.-A. (2012), *Multiple-gradient descent algorithm (MGDA) for multiobjective optimization*, Comptes Rendus Mathématique 350, 313–318.
