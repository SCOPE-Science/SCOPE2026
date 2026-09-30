# Independent audit — 2026-09-29

Record: `2026/09/18/small-hole-gromov-hausdorff-cubic-asymptotic--a0d57fbb476f`  
Assigned and audited source tree: `46dea85206acb66bdd81cbbe20a44506c9bfd7a7`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `c8509dc220b5cbc2f60e119e14257d79cd0ab8d5`  
Disposition: **passed**

## Correctness

**supported**. The cubic-error asymptotic is consistent. In normal coordinates the metric is Euclidean up to O(|x|^2), so Schott's sharp Euclidean deleted-ball correspondence transports with distortion 2 c_n r + O(r^3), giving the upper bound. For the lower bound, scaling g by (h/r)^2 turns the deleted ball into fixed radius h while the sectional-curvature upper bound becomes O(r^2). Adams--Frick--Majhi--McBride Theorem 4 then gives d_GH >= alpha(n,kappa_r) r; their explicit alpha formula has alpha=c_n+O(kappa_r)=c_n+O(r^2). The fixed h chosen in the record is safely below the limiting second branch of the theorem's minimum, so the first branch applies for small r. The n=1 circle case is also correct.

## Originality

**qualified_recent_refinement**. Schott's September 2026 preprint already proves the exact Euclidean constant and a small-hole Riemannian upper statement with an arbitrary fixed multiplicative loss. The audited contribution is the matching manifold asymptotic with an O(r^3) absolute error obtained by combining quadratic normal-coordinate distortion with curvature-vanishing rescaling of the Adams--Frick--Majhi--McBride lower bound. Current searches did not locate this explicit cubic-error statement elsewhere. Because all motivating papers are very recent, the priority conclusion is necessarily narrow.

## Scientific value

**meaningful_sharp_local_refinement**. The theorem identifies the Euclidean Jung constant as the universal first-order coefficient for a geodesic-ball hole and quantifies convergence of d_GH/d_H at quadratic order. It is a useful sharp local refinement, although it does not compute a curvature-dependent cubic coefficient or prove optimality of the remainder.

## Literature and evidence checked

- https://arxiv.org/abs/2609.12625
- https://arxiv.org/abs/2309.16648
- https://arxiv.org/abs/2607.18447
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/small-hole-gromov-hausdorff-cubic-asymptotic--a0d57fbb476f
## Limitations

- The upper bound imports Schott's Euclidean deleted-ball correspondence and its bilipschitz transport estimate.
- The matching lower bound uses a global closed-manifold theorem; the local upper estimate itself is less restrictive.
- No curvature-dependent coefficient at order r^3 is identified.
- The source literature is only weeks old, so unindexed parallel work remains possible.
