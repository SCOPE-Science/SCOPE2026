# A singular crossover in John ellipsoids of one-path-defect \(K_{2,m}\) metrics

## Finding

For every integer \(m\ge 2\) and every real \(t>0\), equip the graph \(K_{2,m}\) with edge length \(t\) on both edges of one distinguished two-edge path and length \(1\) on the other \(m-1\) paths. Let \(Q_{m,t}\) be its real Lipschitz-dual unit ball in the canonical zero-sum Euclidean hyperplane. Its unique maximum-volume inscribed ellipsoid is the graph-energy ellipsoid
\[
E_{m,t}=\{x\in H:x^{\mathsf T}L_{m,t}x\le 1\},
\]
where \(L_{m,t}\) is a weighted graph Laplacian with ordinary-path edge conductance \(a\) and exceptional-path edge conductance \(b\). Define \(r=b/a\) as the unique positive solution of
\[
t^2r(m+r)=m-1+2r.
\]
Equivalently,
\[
r=\frac{2-mt^2+\sqrt{(mt^2-2)^2+4t^2(m-1)}}{2t^2},\qquad
 a=\frac{m+r}{2(m-1+r)},\qquad b=ra.
\]
Every one of the \(2m\) edge inequalities is tangent to this ellipsoid, for all \(t>0\). Its inverse quadratic form identifies the labeled graph edges and, through their effective resistances, determines their metric lengths.

Write \(d=m+1\), \(\omega_d=\pi^{d/2}/\Gamma(1+d/2)\), and let \(J_m(t)\) be the intrinsic Euclidean \(d\)-volume of \(E_{m,t}\). Then
\[
J_m(t)=\frac{\omega_d}{\sqrt{(m+2)2^{m-1}a^{m+1}r(m-1+r)}}.
\]
The normalized response \(R_m(t)=J_m(t)/J_m(1)\), with \(a_0=(m+1)/(2m)\), satisfies
\[
R_m(t)=\left[\left(\frac{a_0}{a}\right)^{m+1}\frac{m}{r(m-1+r)}\right]^{1/2}.
\]
For each fixed \(t>0\),
\[
\lim_{m\to\infty}R_m(t)=t,
\]
but, for each fixed integer \(m\ge2\),
\[
R_m(t)\sim \frac{(m+1)^{(m+1)/2}}{2m^{m/2}}t^2\qquad(t\downarrow0).
\]
The crossover occurs on the scale \(t=c/\sqrt m\), with every fixed \(c>0\). Put
\[
\rho(c)=\frac{2-c^2+\sqrt{c^4+4}}{2c^2}.
\]
Then
\[
\lim_{m\to\infty}\sqrt m R_m(c/\sqrt m)
=\frac{\exp\!\left(\rho(c)/(2(1+\rho(c)))\right)}{\sqrt{\rho(c)(1+\rho(c))}}.
\]
The limiting crossover function behaves as \(e^{1/2}c^2/2\) at \(c\downarrow0\) and as \(c\) at \(c\to\infty\).

## Assumptions and scope

Let the vertex set be \(V=\{u,v,w_0,\ldots,w_{m-1}\}\), with edges \(uw_i\) and \(vw_i\). Both edges incident with \(w_0\) have length \(t\); all others have length \(1\). There are no other edges. Each assigned edge is strictly shorter than any alternative path joining its endpoints: for example, an alternative to an exceptional edge has length at least \(t+2\). Thus these are exactly the irredundant constraints of the shortest-path Lipschitz ball. Set
\[
H=\{x\in\mathbb R^V:\sum_{z\in V}x_z=0\},\quad
Q_{m,t}=\{x\in H:|x_u-x_{w_0}|,|x_v-x_{w_0}|\le t,
\ |x_u-x_{w_i}|,|x_v-x_{w_i}|\le1\ (1\le i<m)\}.
\]
All volumes and determinants use the Euclidean inner product inherited by \(H\), not anchored-coordinate Lebesgue measure. The inverse of \(L_{m,t}\) always means its inverse on \(H\), equivalently the Moore--Penrose inverse on \(\mathbb R^V\). The coefficient \(b\) denotes conductance rather than metric length; the latter is \(t\).

## Proof

**1. Tree polynomial.** For arbitrary positive path conductances \(g_0,\ldots,g_{m-1}\), assign both edges of path \(i\) conductance \(g_i\). A spanning tree contains the two edges on exactly one path, and one of two edges on every other path. By enumerating the possible connecting paths, its total conductance polynomial is
\[
\tau(g)=2^{m-1}\left(\prod_{i=0}^{m-1}g_i\right)\left(\sum_{i=0}^{m-1}g_i\right).
\]
For the corresponding Laplacian \(L(g)\), the matrix-tree theorem gives \(\det_H L(g)=|V|\tau(g)=(m+2)\tau(g)\).

**2. Exact edge effective resistances.** The derivative identity \(\partial_{g_e}\log\tau= (e_p-e_q)^{\mathsf T}L(g)^+(e_p-e_q)\) holds for an individual edge \(e=pq\). Exchanging the two hubs swaps the two equal-conductance edges on every path, so the two resistances on path \(i\) coincide. Differentiating the expression above along simultaneous variation of these two edges gives
\[
\mathcal R_i=\frac1{2g_i}+\frac1{2\sum_j g_j}.
\]
Choose \(g_0=b=ra\) and \(g_i=a\) for \(i\ge1\). Then
\[
\mathcal R_{\mathrm{ord}}=\frac1{2a}\left(1+\frac1{m-1+r}\right)=1
\]
by the stated formula for \(a\), while
\[
\mathcal R_{\mathrm{exc}}=\frac{m-1+2r}{r(m+r)}=t^2.
\]
For fixed \(t>0\), the equation \(t^2r^2+(mt^2-2)r-(m-1)=0\) has precisely one positive root, so both \(a,b\) are strictly positive and uniquely specified.

**3. Optimal ellipsoid certificate.** A centered ellipsoid in \(H\) has the form \(E(S)=\{x:x^{\mathsf T}S^{-1}x\le1\}\), where \(S\) is positive definite on \(H\). It lies in \(Q_{m,t}\) if and only if \((e_p-e_q)^{\mathsf T}S(e_p-e_q)\le \ell_{pq}^2\) for every edge. The determinant \(\det_H S\) is proportional to the squared Euclidean ellipsoid volume. Its logarithm is strictly concave. At \(S=L_{m,t}^+\), step 2 verifies every constraint with equality, and
\[
 S^{-1}=L_{m,t}=\sum_{pq\in E}g_{pq}(e_p-e_q)(e_p-e_q)^{\mathsf T},\qquad g_{pq}>0.
\]
These positive edge conductances are precisely the Lagrange multipliers giving the vanishing gradient of \(\log\det_H S\) under the active edge constraints. More explicitly, concavity of \(\log\det\) yields, for any feasible \(T\),
\[
\log\det_H T-\log\det_H S\le
\operatorname{tr}_H\bigl(S^{-1}(T-S)\bigr)
=\sum_{pq}g_{pq}\bigl((e_p-e_q)^{\mathsf T}T(e_p-e_q)-\ell_{pq}^2\bigr)\le0.
\]
Strict concavity forces equality only for \(T=S\). The polytope \(Q_{m,t}\) is centrally symmetric, so uniqueness of its John ellipsoid forces its center to be zero. The displayed centered solution is therefore globally optimal among all inscribed ellipsoids, not merely symmetry-invariant ones. Every edge facet is tangent by step 2.

**4. Volume and reconstruction.** Substituting the conductances into step 1 yields
\[
\det_H L_{m,t}=(m+2)2^{m-1}a^{m+1}r(m-1+r),
\]
which proves the volume formula. Since \(S^{-1}=L_{m,t}\) is a weighted Laplacian with strictly positive edge weights, its negative off-diagonal entries identify exactly the labeled edges. For each recovered edge \(pq\), its metric length is \(\sqrt{(e_p-e_q)^{\mathsf T}S(e_p-e_q)}\), because all its facets contact the ellipsoid. In particular, the metric defect is recovered without knowing \(t\) beforehand. Equivalently, the conductance ratio \(r=b/a\) recovers it through \(t^2=(m-1+2r)/(r(m+r))\). This relation is strictly decreasing in \(r>0\), with \(r=1\) exactly when \(t=1\).

**5. Three asymptotic regimes.** At \(t=1\), the root is \(r=1\) and \(a_0=(m+1)/(2m)\). The ratio formula in the finding follows by dividing the determinants. For fixed positive \(t\), divide the defining quadratic by \(m\) to see \(r\to t^{-2}\). The exact ratio
\[
\frac a{a_0}=\frac{m(m+r)}{m(m+r)+r-1}
\]
has logarithm \(O(m^{-2})\), so \(R_m(t)\to t\).

For fixed \(m\), the positive root has expansion \(r=2/t^2-(m+1)/2+O(t^2)\) as \(t\downarrow0\). Hence \(a\to1/2\) and \(\det_H L_{m,t}\sim (m+2)t^{-4}\). Meanwhile \(\det_H L_{m,1}=(m+2)(m+1)^{m+1}/(4m^m)\), proving the quadratic small-\(t\) response.

Finally put \(t=c/\sqrt m\). Substituting \(r=m\rho+o(m)\) into its quadratic gives \(c^2\rho^2+(c^2-2)\rho-1=0\), whose unique positive solution is \(\rho(c)\). As \(m\to\infty\),
\[
\left(\frac a{a_0}\right)^{m+1}\to
\exp\left(-\frac{\rho}{1+\rho}\right),\quad
\frac{r(m-1+r)}{m^2}\to\rho(1+\rho).
\]
Inserting these limits into the exact ratio proves the crossover formula. Direct expansion of the positive quadratic root gives \(\rho(c)\sim2/c^2\) for small \(c\) and \(\rho(c)\sim1/c^2\) for large \(c\), and consequently the two limiting behaviors of the crossover function.

## Verification

The included `checker.py` independently assembles the actual graph Laplacians and computes pseudoinverse quadratic forms, positive eigenvalue products, and contact equalities for \(m=2,\ldots,15\) and nine values of \(t\), for 126 total parameter configurations. It also enumerates spanning trees directly for seven ordinary graphs. All tests passed. Separately, numerical evaluations at the critical scale \(t=c/\sqrt m\) for several \(c\) and \(m\) corroborated the limiting formula. These finite computations do not replace the analytical proof in steps 1--5.

## Relationship to prior work

Dilworth--Kutzarova--Ostrovskii develop finite-metric Lipschitz-free and cycle-space frameworks, including the edge-quotient representation. Suliman--Weinstein analyze graph \(\ell_\infty\)-Lewis weights, the effective-resistance gradient, and the general D-optimal ellipsoid design problem. These ingredients motivate the certificate method but do not, in the inspected material, supply the present one-path-defect formula, its all-facet tangency statement, labeled metric recovery, or the singular crossover law. Existing formulas for other graph families or for graphical zonotopes concern different polytopes and do not imply this claim. This is a claim of a graph-specific formula, not a new general ellipsoid optimality principle.

## Limitations

The metric family has precisely one exceptional two-edge path, whose two edges share the same length. The result does not classify arbitrary heterogeneous theta metrics, nor does it claim that every graph-metric Lipschitz ball has an all-edge-contact John ellipsoid. The proof is mathematical and the finite checker is corroborative only. Originality comparisons leave residual risk from unindexed equivalent formulations and published records for which full text was inaccessible. Independent scientific validation has not been performed.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814v1, first public July 10, 2018 (background on finite graph-metric transportation spaces).
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1, first public May 21, 2023; primary MSC2020 46B04.
3. A. Suliman, O. Weinstein, *Infinite Lewis Weights in Spectral Graph Theory*, arXiv:2302.05966v1, first public February 12, 2023 (general graph D-optimality and ellipsoid framework).
