# Independent audit — 2026-09-29 UTC

Record: `2026/09/20/block-nuclear-qnn-regularization--c32011de94a1`  
Assigned and audited source tree: `83eba283af3ab8f218a65605c810d7852d1c9184`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `f13d757b8a22431dee8af24a7b04f4a0741e8e51`  
Disposition: **passed**

## Correctness

**independently_supported**. The block-nuclear certificate and all displayed exact families check. Every neural atom contributes ww^T of trace norm one and [w;1][w;1]^T of trace norm two, proving R>=max(||Z||_*,||M||_*/2); nuclear/operator duality with an off-diagonal norm-one test matrix gives ||M||_*/2>=||z||_2. The pure quadratic, pure linear and aligned rank-one formulas have explicit two-atom realizations. For the orthogonal rank-one family, independent symbolic substitution verifies the three-atom construction and its cost (S^2+2ST+2T^2)/(S+2T); the quadratic dual polynomial 1-2((y-r)/(1+r))^2 stays in [-1,1] on [-1,1] and returns the same objective. The example Z=diag(1,0), z=(0,1) consequently has Omega=(1+sqrt(5))/2 and exact atomic cost 5/3.

## Originality

**qualified_supported**. Bartan-Pilanci already provide the exact neural-spectrahedron/semidefinite lift for degree-two networks, and the September 2026 Rodrigues-Van Egmond-Amiri Fard paper already develops regularized lower bounds with a nuclear-norm connection. Those ingredients are prior art. Current searches did not locate the combined full-block nuclear certificate, the scalar-input l_infinity induced regularizer, or the exact orthogonal rank-one gauge formula. The contribution is therefore supported as a source-specific convex refinement and low-rank gauge calculation, not as a new neural-spectrahedron framework.

## Scientific value

**meaningful_stronger_relaxation_and_exact_slices**. The record identifies a convex certificate that simultaneously controls the quadratic and linear aggregate, quantifies the gap left by a nuclear-only relaxation, and gives exact induced regularizers on several nontrivial slices. The scalar-input collapse to a two-variable l_infinity penalty is especially concrete.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/block-nuclear-qnn-regularization--c32011de94a1
- https://arxiv.org/abs/2609.17654
- https://arxiv.org/abs/2101.02429
- https://doi.org/10.1007/s10107-024-02153-5
## Limitations

- The block-nuclear functional Omega is only a lower certificate in general dimension.
- Exact equivalence to the original network training problem requires enough width to realize the atomic decomposition.
- The result is restricted to one-output degree-two networks with unit hidden weights and l1 output-weight regularization.
- The exact low-rank formulas are elementary once the correct atomic gauge is isolated, so differently phrased convex-geometric prior art remains a modest risk.
