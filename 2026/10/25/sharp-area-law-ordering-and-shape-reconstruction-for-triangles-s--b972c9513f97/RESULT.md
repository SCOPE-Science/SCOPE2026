# Sharp area-law ordering and shape reconstruction for triangles sampled by boundary arclength

## Finding
Let \(K\) be any nondegenerate Euclidean triangle with side lengths \(\ell_1,\ell_2,\ell_3\), perimeter \(P\), and area \(|K|\). Let \(X_1,X_2,X_3\) be independent points uniformly distributed by arclength along the *entire boundary* of \(K\). Put
\[
Z=\frac{|\operatorname{conv}(X_1,X_2,X_3)|}{|K|},\quad p_i=\frac{\ell_i}{P},\quad e_2=\sum_{i<j}p_ip_j,\quad e_3=p_1p_2p_3.
\]
The distribution of \(Z\) is a universal three-component mixture:
\[
Z\ \overset{d}{=}\ \begin{cases}
0 &\text{with probability }q_0=1-3e_2+3e_3,\\
S=|U-V|W &\text{with probability }q_1=3e_2-9e_3,\\
R=UVW+(1-U)(1-V)(1-W) &\text{with probability }q_2=6e_3,
\end{cases}
\]
where, in each component, \(U,V,W\) are independent uniform random variables on \([0,1]\), and the component choice is independent. In particular, for \(0<t<1\),
\[
\Pr(Z\le t)=q_0+q_1\bigl(t^2-2t\log t\bigr)+q_2F_R(t),\qquad F_R(t)=\Pr(R\le t).
\]
The function \(F_R\) is universal; a completely explicit representation is given below, and its independent one-point-per-side version was determined previously by Maesumi.

**Sharp stochastic shape theorem.** If \(p\) majorizes \(p'\), then \(Z_p\) is stochastically no larger than \(Z_{p'}\), with strict inequality at *every* threshold \(0<t<1\) unless the unordered weight vectors coincide. For every nondegenerate triangle and every \(0<t<1\), writing \(A(t)=\Pr(S>t)\) and \(B(t)=\Pr(R>t)\),
\[
\boxed{\frac34 A(t)<\Pr(Z>t)\le\frac23 A(t)+\frac29B(t).}
\]
The upper equality occurs precisely for equilateral triangles. The lower bound is sharp simultaneously for all thresholds and is approached by a sequence of degenerating triangles whose normalized side lengths tend to \((1/2,1/2,0)\); it is never attained by a nondegenerate triangle.

**Shape-recovery theorem.** With \(m_k=\mathbb E[Z^k]\), the first three moments obey
\[
 m_1=\frac{e_2}{2},\qquad m_2=\frac{e_2}{6}=\frac{m_1}{3},\qquad
 m_3=\frac{3e_2}{40}-\frac{e_3}{60}.
\]
Consequently the two scalars \((m_1,m_3)\) uniquely recover the triangle up to Euclidean similarity: its unordered normalized side lengths are the three roots of
\[
 x^3-x^2+2m_1x-(9m_1-60m_3)=0.
\]
The first two moments alone cannot determine the shape because the second is always one third of the first. Alternatively, the atom \(\Pr(Z=0)=1-3e_2+3e_3\), together with the first moment, determines the shape.

For every integer \(k\ge1\), the full moment sequence is
\[
 \mathbb E[Z^k]=\frac{6(e_2-3e_3)}{(k+1)^2(k+2)}
 +\frac{6e_3}{(k+1)^3}\sum_{j=0}^{k}\binom{k}{j}^{-2}.
\]
These moments uniquely determine the distribution, because \(Z\in[0,1]\).

## Assumptions and scope
The sampling law uses actual Euclidean arclength over all three sides, not one forced point per side and not area-uniform sampling from the interior. The triangle inequalities give \(p_i>0\), \(\sum_i p_i=1\), and \(p_i<1/2\). Similarity of unlabeled triangles is exactly equivalence of unordered normalized side lengths. There are no further restrictions on angles, including obtuse or arbitrarily thin nondegenerate triangles. Probability at \(Z=0\) is positive, coming from three collinear samples on one side.

## Proof
**1. Edge-occupancy disintegration.** Each sample independently selects edge \(i\) with probability \(p_i\), then selects a uniform affine parameter on that edge. Three samples on the same edge have area zero and total mass \(\sum_i p_i^3=1-3e_2+3e_3\) by Newton's identities. Exactly two samples on edge \(i\) have total mass \(3\sum_i p_i^2(1-p_i)=3e_2-9e_3\). For these, base length fraction \(|U-V|\) and height fraction \(W\) are independent; thus the normalized triangle area has law \(S=|U-V|W\), regardless of triangle shape or which other edge contains the third point. Three distinct edges have mass \(6p_1p_2p_3=6e_3\); a barycentric determinant gives normalized area \(R=UVW+(1-U)(1-V)(1-W)\). This proves the complete mixture.

**2. Explicit component laws.** Since \(\Pr(|U-V|\in dd)=2(1-d)\,dd\),
\[
F_S(t)=\int_0^t 2(1-d)\,dd+\int_t^1\frac{2t(1-d)}{d}\,dd=t^2-2t\log t\quad(0<t<1).
\]
For \(R\), conditional on \(U=u,V=v\), its value is uniform on the interval with endpoints \(uv\) and \((1-u)(1-v)\); hence \(F_R\) is uniquely and explicitly specified by
\[
F_R(t)=\int_0^1\!\int_0^1\operatorname{clip}_{[0,1]}\left(\frac{t-\min\{uv,(1-u)(1-v)\}}{|u+v-1|}\right)\,du\,dv.
\]
On the measure-zero diagonal \(u+v=1\), interpret the integrand as the indicator of \(uv\le t\). The previously published elementary closed form (Maesumi, 2018) is
\[
F_R(t)=t-\left(3t-\tfrac12\right)\log t+
\begin{cases}
(1-4t)^{3/2}\operatorname{artanh}\sqrt{1-4t}, &0<t<1/4,\\
0, &t=1/4,\\
(4t-1)^{3/2}\left(\arctan\sqrt{4t-1}-\pi/3\right), &1/4<t<1.
\end{cases}
\]
The integral representation and the edge decomposition suffice for the novel assertions; the cited closed-form evaluation is prior work.

**3. A strict stochastic coupling.** Independently take \(U,V,W\) uniform on \([0,1]\), let \(a=(1-U)V\), \(b=U(1-V)\). Replacing \(U\) by \(1-U\) in the defining expression for \(R\) shows that \(R\) has the conditional-uniform law on \([\min(a,b),\max(a,b)]\). Consequently
\[
R\ \overset d=\ \min(a,b)+|U-V|W\ \ge\ |U-V|W=S.
\]
The inequality is almost surely strict because \(\min(a,b)>0\) almost surely. For each \(0<t<1\), there is a positive-volume open set of \((U,V,W)\) with \(S<t<R\) (choose \(U,V\) near distinct endpoints and \(W\) so that \(S\) sits just below \(t\)). Thus \(B(t)>A(t)>0\) at every interior threshold.

**4. Majorization and sharp bounds.** At fixed \(t\), the survival probability equals
\[
H_t(p)=3(e_2-3e_3)A(t)+6e_3B(t).
\]
Its symmetric polynomial derivatives satisfy, for pairwise distinct indices \(i,j,k\),
\[
(p_i-p_j)\bigl(\partial_{p_i}H_t-\partial_{p_j}H_t\bigr)
=-3(p_i-p_j)^2\bigl[A(t)(1-p_k)+2p_k(B(t)-A(t))\bigr]\le0,
\]
strictly if \(p_i\ne p_j\). Standard two-coordinate averaging (equivalently, the elementary differential criterion for Schur concavity) proves strict order under nontrivial majorization. The uniform vector \((1/3,1/3,1/3)\) is majorized by every allowed \(p\); the degenerate vector \((1/2,1/2,0)\) majorizes each allowed \(p\). Their weights yield the displayed bounds. The lower vector is approximable by actual triangles with side lengths proportional to \((1,1,\varepsilon)\), proving sharpness without asserting attainment.

**5. Moments and recovery.** Independence and the triangular law of \(|U-V|\) give \(\mathbb E[S^k]=2/[(k+1)^2(k+2)]\). Expanding \([UVW+(1-U)(1-V)(1-W)]^k\) and integrating via the beta integral gives
\[
\mathbb E[R^k]=\sum_{j=0}^k\binom kj \left(\frac{j!(k-j)!}{(k+1)!}\right)^3
=\frac{1}{(k+1)^3}\sum_{j=0}^k\binom kj^{-2}.
\]
The mixture yields the stated exact moments and the first-three identities by substituting \(k=1,2,3\). Inverting gives \(e_2=2m_1\), \(e_3=9m_1-60m_3\). The normalized sides are the unordered roots of \(x^3-x^2+e_2x-e_3\), completing exact similarity recovery. The atom alternative follows from \(q_0=1-3e_2+3e_3\).

## Verification
The accompanying standalone checker reproduces \(\mathbb E[R^k]\) for \(k=1,2,3,4\) using exact rational arithmetic, checks the first-three moment formulas and reconstruction algebra for multiple exact weight vectors, and tests the strict-coupling inequality on 100,000 reproducible triples. Independent geometric-coordinate Monte Carlo simulations (140,000 triples each for side vectors \((3,4,5)\), \((5,5,6)\), \((2,3,4)\)) reproduce three normalized area moments and the zero-area atom within stated finite-sampling tolerances. These experiments are crosschecks, not replacements for the exact analytic proof.

## Relationship to prior work
Koroleva and Nikitin (arXiv:1301.1360, first posted 2013-01-07) studied maximal areas of random polygons with vertices sampled on a circle; their support and extremal object differ from the present fixed-triangle boundary law. Pérez-Lantero (arXiv:1412.5153, first posted 2014-12-16) studied convex-hull area distributions for finite stochastic point sets, rather than three continuous arclength samples on a triangle's sides. Maesumi (arXiv:1804.11007, first posted 2018-04-30; later journal 2019) explicitly computed \(R\), the law conditional on *one point on each side*. That universal component, its moments, and its elementary CDF are not new here. The new comparison is the unconditional arclength-weighted mixture across occupancy patterns, its strict majorization ordering with sharp bounds, and inversion of side-length ratios from two scalar area moments. The distinction is between forcing edge occupancy and sampling the entire perimeter; no claim of novelty is made for the former.

## Limitations
This establishes uniqueness only up to similarity, not absolute scale or labeling of the three sides. Strict majorization applies to area ratios under arclength sampling; it says nothing about unrelated sampling measures, numbers of points, other polygons, or unnormalized areas. The lower stochastic envelope is a non-attained degenerate limit. No independent validation or exhaustive historical novelty certification has been performed. A residual risk is an equivalent statement in unindexed older geometric-probability literature; the general conditional distribution is already covered by Maesumi and is explicitly treated as prior.

## References
1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360 (first public arXiv posting 2013-01-07). https://arxiv.org/abs/1301.1360
2. P. Pérez-Lantero, *Area and Perimeter of the Convex Hull of Stochastic Points*, arXiv:1412.5153 (first public arXiv posting 2014-12-16). https://arxiv.org/abs/1412.5153
3. A. Maesumi, *Triangle Inscribed-Triangle Picking*, arXiv:1804.11007 (first public arXiv posting 2018-04-30); College Mathematics Journal 50 (2019), 364–371. https://arxiv.org/abs/1804.11007
