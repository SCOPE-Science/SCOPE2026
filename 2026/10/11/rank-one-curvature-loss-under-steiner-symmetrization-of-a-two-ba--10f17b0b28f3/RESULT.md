# Rank-one curvature loss under Steiner symmetrization of a two-ball lens

## Finding
Fix an integer \(n\ge 3\), radius \(R>0\), and two closed Euclidean balls \(B(c_1,R),B(c_2,R)\subset\mathbb R^n\) whose intersection \(L\) has nonempty interior. Fix any unit direction \(u\), and let \(S_uL\) denote the Steiner symmetral parallel to \(u\).

**Curvature-index theorem.** At every \(C^2\) regular boundary point of \(S_uL\), **at most one** of its \(n-1\) principal curvatures (with the positive-convex-body sign convention) is strictly less than \(1/R\). Thus at least \(n-2\) principal curvatures are at least \(1/R\). This upper bound of one deficient principal curvature cannot be replaced by zero, even for \(n=3\).

On every open mixed-fiber patch there is an exact, stronger transverse identity. Write the upper boundary as a graph \(z=h(x)\), with \(x\in\mathbb R^{n-1}\), and write \(h=(f_1+f_2)/2+C\), where \(f_i(x)=\sqrt{R^2-|x-a_i|^2}\) are the two upper spherical-cap height functions and \(C\) is constant. Set \(p_i=\nabla f_i\), \(p=(p_1+p_2)/2\), and \(W_i=\sqrt{1+|p_i|^2}\), \(W=\sqrt{1+|p|^2}\). For every nonzero horizontal tangent parameter \(v\) orthogonal to \(p_1-p_2\), the normal curvature satisfies the exact identity
\[
\kappa(v)=\frac{W_1+W_2}{2RW}\ge\frac1R.
\]
Equality holds precisely when \(p_1=p_2\). If the gradients differ, this gives a strictly positive curvature gain in all \(n-2\) transverse parameter directions. The same assertions hold for the reflected lower graph.

## Assumptions and scope
The lens is the intersection of exactly two equal-radius Euclidean balls, not an arbitrary intersection of many balls. The Steiner axis is arbitrary. A \(C^2\) regular boundary point means that \(\partial S_uL\) is locally a twice continuously differentiable embedded hypersurface there; the principal curvatures are defined in the classical sense. The exact transverse identity refers to the mixed-fiber open set with positive vertical fiber length where its two endpoints lie on distinct original spheres. At the interfaces of graph branches only the index inequality, not the displayed branch-specific identity, is asserted. Nonsmooth boundary points have no assertion of classical principal curvatures. Radius normalization and dimension are arbitrary as stated.

## Proof
First choose orthogonal coordinates \((x,z)\in\mathbb R^{n-1}\times\mathbb R\) with \(u\) in the \(z\)-direction. At a horizontal point \(x\) whose intersection with the lens is a nondegenerate vertical interval, the two balls intersect the fiber in intervals
\[
[c_{i,z}-f_i(x),\ c_{i,z}+f_i(x)],\qquad
f_i(x)=\sqrt{R^2-|x-a_i|^2},\quad a_i=\operatorname{proj}_{u^\perp}c_i.
\]
The symmetral's upper half-height is half the difference between the smaller of the two upper endpoints and the larger of the two lower endpoints. Therefore, on any branch where both endpoints come from the same original ball, its graph is a spherical cap \(h=f_i\). Where they come from distinct balls, the graph instead has the form \(h=(f_1+f_2)/2+C\), with the constant depending only on the vertical center coordinates. This exhausts open smooth branches. For a single-cap branch, all principal curvatures equal \(1/R\).

For a mixed branch define \(p_i,p,W_i,W\) as in the statement. Direct differentiation of a sphere gives the **exact Hessian identity**
\[
-D^2f_i=\frac{W_i}{R}\bigl(I+p_ip_i^{\mathsf T}\bigr).
\]
The upper graph's first fundamental form and outward-positive second fundamental form, evaluated on a parameter vector \(v\in\mathbb R^{n-1}\), are
\[
\mathrm I_h(v,v)=|v|^2+(p\cdot v)^2,\qquad
\mathrm{II}_h(v,v)=\frac{-D^2h[v,v]}{W}.
\]
Let \(H=\{v:(p_1-p_2)\cdot v=0\}\). If \(v\in H\), then \(p_1\cdot v=p_2\cdot v=p\cdot v\); hence the sphere Hessian identity implies
\[
\mathrm{II}_h(v,v)
=\frac{W_1+W_2}{2RW}\bigl(|v|^2+(p\cdot v)^2\bigr)
=\frac{W_1+W_2}{2RW}\,\mathrm I_h(v,v).
\]
The Euclidean norm is strictly convex along the affine slice \((1,p)\), so
\[
\frac{W_1+W_2}{2}\ge
\sqrt{1+\left|\frac{p_1+p_2}{2}\right|^2}=W,
\]
with equality if and only if \(p_1=p_2\). This proves the exact transverse identity and its strictness. If \(p_1\ne p_2\), \(H\) has dimension \(n-2\), so the quadratic form \(\mathrm{II}_h-R^{-1}\mathrm I_h\) is positive definite on a codimension-one subspace of the tangent space. Sylvester's inertia principle (equivalently the Courant–Fischer principle for the two positive-definite metric forms) implies the generalized eigenproblem \(\mathrm{II}_h v=\kappa\,\mathrm I_h v\) has at most one eigenvalue below \(1/R\). If \(p_1=p_2\), the two sphere Hessian identities coincide, and all curvatures equal \(1/R\).

The lower graph is the reflection of the upper graph, so its positive principal curvatures agree. At a \(C^2\) point where branch selections meet, take nearby smooth open-branch points and use continuity of the two fundamental forms: the property that at most one generalized eigenvalue lies strictly below \(1/R\) is closed under such limits. At any \(C^2\) point with vertical tangent, the same argument uses nearby positive-length graph points and continuity of the hypersurface shape operator. The branch regions and their closures exhaust the boundary, because the fiber endpoints are pointwise minima/maxima of two analytic spherical-cap expressions. This completes the universal claim.

**Sharpness.** Artstein-Avidan and Florentin's Theorem 4.6 explicitly constructs two unit balls in \(\mathbb R^3\) and a Steiner axis for which the symmetral has sectional curvature below \(1\) at a smooth mixed-fiber point. Since some normal curvature is below \(1\), its least principal curvature is below \(1\). The proved index bound therefore has equality there: exactly one principal curvature is deficient. The authors' centers are \(\pm(-0.2794,0.2451,0.36)\), with the axis along the third coordinate and the horizontal test point \((0.4154,0.7262)\). The companion numerical verification reproduces a minimum principal curvature approximately \(0.968946368\). For any \(n>3\), embed that configuration in \(\mathbb R^n\) with the extra horizontal components zero. Restricting the second fundamental form to the original three-dimensional tangent section preserves a deficient normal-curvature direction; the same index theorem then shows sharpness in every \(n\ge3\).

## Verification
A standalone Python 3 program, `verify.py`, deterministically checks \(16{,}000\) transverse quadratic-form inequalities over dimensions \(2,3,5,9\) for horizontal graph dimensions, evaluates generalized curvature at the published lens configuration, and reports `VERIFY_OK` on success. These numerical tests are consistency checks, **not** a proof of the infinite-dimensional quantifiers; the algebra above supplies the complete proof. The source's displayed decimals are treated as exact terminating decimals only for this finite numerical replay, not as a general certificate of sharpness.

## Relationship to prior work
The principal source is S. Artstein-Avidan and D. I. Florentin, *Symmetrizations of Ball-Bodies*, arXiv:2602.14090v1 (first publicly posted 2026-02-15), especially Theorem 4.1 (the all-curvatures planar preservation), Theorem 4.6 (a three-dimensional lens with lost curvature), and Proposition 4.9 (arbitrarily severe loss in at least one sectional direction). Those conclusions neither assert nor imply an upper bound on the **number** of deficient principal curvature eigenvalues in arbitrary dimensions, nor the exact transverse curvature gain. The companion full-length exposition *An in-depth study of ball-bodies*, arXiv:2505.09200, was also compared in its Steiner-symmetrization sections; no corresponding index theorem was identified there. Other nearby indexed work addresses the mean width of a symmetric lens, a global integrated quantity, rather than the local curvature spectrum. A general midpoint-graph observation underlies the proof, but the resulting sharp curvature-index restriction on the symmetral of **every** two-ball lens does not follow from the cited source conclusions alone.

## Limitations
The theorem does not say that any principal curvature is necessarily below \(1/R\), nor does it extend automatically to intersections of three or more balls, to radii that differ, or to nonsmooth principal curvatures. Its one-dimensional instability allowance is a rank restriction, not a uniform lower bound on the smallest curvature: arbitrarily low curvature in the exceptional direction remains consistent with the source examples. Exhaustive historical originality verification is impossible, so older equivalent midpoint-graph formulas may exist. Independent validation of this finding has not been performed.

## References
1. S. Artstein-Avidan and D. I. Florentin, *Symmetrizations of Ball-Bodies*, arXiv:2602.14090v1, 2026-02-15, https://arxiv.org/html/2602.14090 .
2. S. Artstein-Avidan and D. I. Florentin, *An in-depth study of ball-bodies*, arXiv:2505.09200, https://arxiv.org/abs/2505.09200 .
3. Bianchi, Gardner and Gronchi, *Symmetrization in geometry*, Advances in Mathematics 306 (2017), 51–88, https://doi.org/10.1016/j.aim.2016.10.003 .
