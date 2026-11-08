# A curvature law and sharp circular minimum for visibility in thin inner-parallel shells

## Finding

Let \(K\subset\mathbb R^2\) be a compact strictly convex body with \(C^3\) boundary and everywhere positive Euclidean curvature \(\kappa(s)\), parametrized by arclength \(s\in[0,P)\), where \(P\) is its perimeter. For sufficiently small \(\varepsilon>0\) form its **inner-parallel shell**
\[
S_\varepsilon=K\setminus\operatorname{int}(K\ominus\varepsilon\overline B_2),\qquad
K\ominus\varepsilon\overline B_2=\{x:x+\varepsilon\overline B_2\subseteq K\}.
\]
Draw independent area-uniform points \(X_\varepsilon,Y_\varepsilon\in S_\varepsilon\), and write \(b(S_\varepsilon)=\Pr\{[X_\varepsilon,Y_\varepsilon]\subseteq S_\varepsilon\}\) for the Beer index (straight-segment visibility probability). Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{b(S_\varepsilon)}{\sqrt\varepsilon}
=\frac{8\sqrt2}{3P^2}\int_{\partial K}\kappa(s)^{-1/2}\,ds.}
\tag{1}
\]
For each fixed perimeter \(P>0\), this coefficient has the **sharp, rigid lower bound**
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{b(S_\varepsilon)}{\sqrt\varepsilon}
\ge \frac8{3\sqrt{\pi P}},}
\tag{2}
\]
with equality if and only if \(K\) is a Euclidean disk (up to translation). Consequently the disk uniquely minimizes leading thin-shell visibility among positively curved smooth convex planar bodies of a fixed perimeter. The parameter \(\varepsilon\) denotes *Euclidean inward normal distance*, not homothetic scaling or shell area.

## Assumptions and scope

The curvature is strictly positive and continuous, and the boundary has a continuous third derivative. Both points are independent and uniform with respect to planar Lebesgue area on the shell. Visibility means containment of the *entire ambient Euclidean line segment* in the shell; contact with its boundary is allowed. For sufficiently small \(\varepsilon\) the inward normal map is injective throughout the shell. The limit is pointwise for each fixed body; no uniform estimate over degenerating families or bodies with vanishing curvature is claimed.

## Proof

**1. Exact normal-coordinate sampling.** Write \(\gamma(s)\) for a positively oriented unit-speed boundary parametrization and \(n(s)\) for its inward unit normal. Since \(\kappa(s)>0\) on a compact curve, for sufficiently small \(\varepsilon>0\),
\[
F(s,u)=\gamma(s)+u n(s),\quad 0\le u\le\varepsilon,
\]
parametrizes the shell, with area Jacobian \(1-\kappa(s)u\). In particular,
\[
|S_\varepsilon|=\int_0^P\int_0^\varepsilon(1-\kappa(s)u)\,du\,ds
=P\varepsilon-\pi\varepsilon^2,
\tag{3}
\]
using the turning-angle identity \(\int_0^P\kappa(s)\,ds=2\pi\).

**2. Localization of visible pairs.** Let \(h\) be the signed shorter arclength displacement between the boundary footpoints of two shell points. Uniform strict positive curvature gives constants \(c>0\) and \(h_0>0\) such that, for \(|h|\le h_0\), the midpoint of the corresponding *boundary* chord lies at inward distance at least \(c h^2\) from \(\partial K\). Indeed, uniformly in its basepoint, the boundary graph over the tangent line is \(\kappa(s)x^2/2+O(x^3)\), so the chord-midpoint depth is \(\kappa(s)h^2/8+O(h^3)\). For \(|h|\ge h_0\), compactness and strict convexity give a positive lower bound on midpoint depth. Perturbing both endpoints by at most \(\varepsilon\) changes their midpoint by at most \(\varepsilon\); distance to the boundary is one-Lipschitz. Therefore there is a fixed \(C=C(K)\) such that, for all sufficiently small \(\varepsilon\), a visible pair necessarily satisfies
\[
|h|\le C\sqrt\varepsilon.
\tag{4}
\]
Here and below the boundary coordinates are periodic, so there is no artificial endpoint contribution from choosing \([0,P)\).

**3. Universal local chord test.** Fix a boundary footpoint \(s\), let the second lie at \(s+\sqrt\varepsilon z\), and write the inward normal depths as \(u=\varepsilon A\), \(v=\varepsilon B\), with \(A,B\in[0,1]\). Let \(\rho(p)=\operatorname{dist}(p,\partial K)\) for \(p\in K\). Uniform local Taylor expansion of the boundary in tangent-normal coordinates shows that along the chord, at affine parameter \(t\in[0,1]\),
\[
\rho\big((1-t)F(s,\varepsilon A)+tF(s+\sqrt\varepsilon z,\varepsilon B)\big)
=\varepsilon\left[(1-t)A+tB+\frac{\kappa(s)z^2}{2}t(1-t)\right]+o(\varepsilon),
\tag{5}
\]
where the remainder divided by \(\varepsilon\) tends uniformly to zero for \(s\in[0,P]\), \(A,B,t\in[0,1]\), and bounded \(z\). The line segment stays in the shell exactly when the maximum of \(\rho\) along it is at most \(\varepsilon\), because convexity already keeps it in \(K\). Except on a parameter set of measure zero, the limiting visibility criterion is
\[
\frac{\kappa(s)z^2}{2}t(1-t)
\le (1-A)(1-t)+(1-B)t\quad\text{for every }t\in[0,1].
\tag{6}
\]
For \(p=1-A\) and \(q=1-B\), the elementary identity
\[
\min_{0<t<1}\left(\frac pt+\frac q{1-t}\right)
=(\sqrt p+\sqrt q)^2
\tag{7}
\]
(including the endpoints by continuity) makes (6) equivalent to
\[
|z|\le\sqrt{\frac2{\kappa(s)}}\big(\sqrt{1-A}+\sqrt{1-B}\big).
\tag{8}
\]

**4. Scaling of the pair integral.** Using (3) and the two normal Jacobians, write the Beer numerator as the integral over \((s,u,s',v)\) of the visibility indicator times \((1-\kappa(s)u)(1-\kappa(s')v)\). By localization (4), put \(s'=s+\sqrt\varepsilon z\), \(u=\varepsilon A\), \(v=\varepsilon B\). The normal Jacobians converge uniformly to one. The bounded \(z\)-range from (4), expansion (5), and the fact that the equality boundary in (8) has four-dimensional Lebesgue measure zero justify dominated convergence. The normalized probability divided by \(\sqrt\varepsilon\) converges to
\[
\begin{aligned}
\frac1{P^2}\int_0^P\int_0^1\int_0^1
2\sqrt{\frac2{\kappa(s)}}\big(\sqrt{1-A}+\sqrt{1-B}\big)
\,dA\,dB\,ds
&=\frac{8\sqrt2}{3P^2}\int_0^P\kappa(s)^{-1/2}\,ds,
\end{aligned}
\]
since \(\int_0^1\sqrt{1-A}\,dA=2/3\). This proves (1), with its quantifiers and normalization.

**5. Sharp optimizer.** As \(x\mapsto x^{-1/2}\) is strictly convex on \((0,\infty)\), Jensen's inequality and total turning angle give
\[
\int_0^P\kappa(s)^{-1/2}\,ds
\ge P\left(\frac1P\int_0^P\kappa(s)\,ds\right)^{-1/2}
=\frac{P^{3/2}}{\sqrt{2\pi}}.
\]
Substituting this into (1) gives (2). Equality requires constant positive curvature, hence a circle. A circle realizes equality, proving sharpness and uniqueness.

## Verification

For a disk of radius \(R\), the exact annulus visibility law is
\[
b(S_\varepsilon)=\frac{2}{\pi(1-a^2)}
\left(\arccos a-a\sqrt{1-a^2}\right),\qquad a=1-\varepsilon/R.
\]
Its expansion gives \(b(S_\varepsilon)\sim 4\sqrt2\sqrt{\varepsilon/R}/(3\pi)\), which agrees with (1) because \(P=2\pi R\) and \(\kappa=1/R\). This disk formula is a known special case, not a new contribution.

The standalone dependency-free `verify_parallel_shell.py` independently evaluates the exact disk formula, numerically integrates the curvature expression for ellipses, and draws area-uniform samples from an elliptical inner-parallel shell. It checks visibility by clipping sampled chords against 720 supporting halfplanes approximating the exact eroded ellipse. For semiaxes \((2,1)\), it obtains coefficient \(0.577437293058\ldots\), compared with the sharp same-perimeter circle bound \(0.483355522208\ldots\); at thicknesses \(0.02\) and \(0.005\) its sample estimates are respectively \(0.08115\) and \(0.0405667\), close to the first-order predictions \(0.081662\) and \(0.040831\). The finite approximation and random sampling are diagnostics, not proof of the general theorem. The script reports `INNER_PARALLEL_SHELL_TESTS_OK`.

## Relationship to prior work

Beer introduced the visibility index and studied *outer* parallel-body thickening and continuity, not the present thin **inner** parallel shells or their curvature coefficient [1]. Balko, Jelínek, Valtr and Walczak developed the Beer index and higher analogues [2], with no coefficient (1) or fixed-perimeter minimizer in the materially inspected treatment. Abrahamsen and Fredslund-Hansen supply polynomial-time Beer-index algorithms for polygons with holes [3], rather than continuous smooth-body limits. Fodor and Papvári use visibility regions near the boundary of smooth convex discs in random-polytope arguments [4]; their caps and bounds do not imply the two-independent-point, inner-normal-shell limit here.

The published note *Thin-shell convexity moments recover facet cone volumes* [5] proves that homothetic shells of facetless bodies have limiting Beer index zero. It has a different inner-shell convention and supplies no rate or curvature coefficient; (1) is a quantitative result beyond that zero-limit statement. The exact disk Beer index is also present in earlier literature and is used only as a check, not claimed as original. The novelty claimed here is the all-positively-curved-body inner-parallel-shell leading coefficient together with its sharp fixed-perimeter circular minimum, not the Beer-index definition, the tube-area formula, or the use of Jensen's inequality.

## Limitations

No second-order expansion, uniform result as curvature degenerates, result for nonsmooth or polygonal bodies, or higher-dimensional law is proved. The asymptotic concerns Euclidean inner-parallel offset shells, not general homothetic or equal-area shells. The proof is analytic; the numerical checker provides finite diagnostic evidence only. Historical priority remains provisional because indexing cannot rule out equivalent older results, and an independent audit has not been performed.

## References

1. G. A. Beer, *The index of convexity and parallel bodies*, Pacific Journal of Mathematics **53** (1974), 337–345. https://msp.org/pjm/1974/53-2/pjm-v53-n2-p03-s.pdf
2. M. Balko, V. Jelínek, P. Valtr, B. Walczak, *On the Beer index of convexity and its variants*, arXiv:1412.1769v1 (first posted 2014-12-04); later in Discrete & Computational Geometry **57** (2017), 179–214. https://arxiv.org/abs/1412.1769
3. M. Abrahamsen, V. Fredslund-Hansen, *Degree of Convexity and Expected Distances in Polygons*, arXiv:2208.07106v1 (2022). https://arxiv.org/html/2208.07106v2
4. F. Fodor, D. I. Papvári, *A Central Limit Theorem for Random Disc-Polygons in Smooth Convex Discs*, published online 2024-11-18. https://link.springer.com/article/10.1007/s00454-024-00701-6
5. *Thin-shell convexity moments recover facet cone volumes* (2026), publicly available research note: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-thin-shell-convexity-moments-recover-facet-cone-volumes--5bf5ee80e1b7
