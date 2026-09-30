# Independent audit — 2026-09-29

Record: `2026/09/19/curvature-distortion-spider-trees--7ee8f1c6b217`  
Assigned and audited source tree: `53049755ff8ec7d510039559fe0bcbbf6bc2e90e`  
Audited repository: `SCOPE-Science/SCOPE2026` branch `main`  
Current RESULT.md blob: `071920fa75cf737b5572736ebf6f5e651efc837d`  
Disposition: **passed**

## Correctness

**independently_supported**. Xia's tree fixed-point equations reduce each long arm to a geometric progression because x_j^2=x_{j-1}x_{j+1}; the center equation gives s=rho^(ell-1)(rho+1). Summing first-edge weights yields sum h_ell(s)=1, whose left side is continuous and strictly decreasing from at least one at s=d to zero, so s_* is unique. First-edge weight increases with arm length, hence a longest arm controls distortion. Lengthening arms increases the scalar root, giving the unique fixed-(d,L) minimum and maximum patterns. Their scalar equations yield (d-1)^((L-1)/L) and (d-1)^(L-1). The bundled reconstruction checks 660 cases with maximum fixed-point residual 3.638e-12.

## Originality

**qualified_explicit_family_solution**. Xia's September 2026 paper introduces the invariant and the general finite-tree nonlinear fixed point plus suppression monotonicity. Its public abstract does not state a spider formula, and searches for spider/starlike/subdivided-star curvature-distortion formulas found no equivalent result. Novelty is therefore limited to the exact spider reduction and sharp extremals, with high concurrency risk.

## Scientific value

**meaningful_exact_family_and_extremal_law**. The result solves the new invariant on a standard infinite family, reducing an edge-dimensional nonlinear system to one scalar equation and showing exponential distortion under uniform subdivision despite only one branch vertex.

## Literature and evidence checked

- https://arxiv.org/abs/2609.12125
- https://arxiv.org/abs/2604.22449
- https://arxiv.org/abs/2603.10479
## Limitations

- Restricted to finite spider trees in the fixed-combinatorial-distance LLY convention.
- Mixed lengths are implicit through a scalar root.
- Xia's fixed-point and suppression theory are prior work.
- The invariant is very recent, so parallel-work risk is substantial.
