# Same-model review of “A two-parameter robust cone of Sturmian-maximizing potentials”

## Correctness
**PASS.** The source proof yields the stronger pre-collapse estimate \(W_\theta(\nu,\mu_\alpha)\le A_\theta D_1+C_\theta D_2\), with both defects nonnegative. For \(G_{p,q}=p\Phi-q\Psi\), the optimization gap is exactly \(pD_1+qD_2\). The choice \(\delta_\theta(p,q)=\min\{p/A_\theta,q/C_\theta\}\) therefore gives the stated Wasserstein margin. Kantorovich duality converts that margin into strict uniqueness under any perturbation with smaller Lipschitz seminorm. The convex-cone assertion follows from superadditivity of the minimum of the two positive linear forms and the triangle inequality.

## Originality
**PASS.** The closest source, arXiv:2610.03619v1, states the diagonal potential \(\Phi-\Psi\), its Wasserstein stability estimate, and one explicit ball around that potential. It does not state the independently weighted family \(p\Phi-q\Psi\), the anisotropic radius \(\min\{p(1-\theta)^2,q/C_\theta}\), or the resulting open convex cone. Targeted searches for weighted digit-distance potentials, anisotropic Sturmian maximizing cones, and equivalent robustness formulations did not locate an implication-equivalent published statement. Earlier beta-transformation and symbolic typical-periodic-optimization work has broader but different conclusions and does not imply this quantitative cone.

## Value
**PASS.** The result identifies a structural two-parameter region of robust aperiodic optimization rather than another isolated example. It quantifies how robustness trades off between the digit-frequency and distance-to-Sturmian penalties, recovers the focal theorem on the diagonal, and exhibits an unbounded convex nonperiodic-maximizer region. This directly refines the geometry of the exceptional region responsible for failure of typical periodic optimization.

## Closest literature and limitations
The focal 2026 preprint is the decisive comparison because its proof supplies the two separate defect coefficients. The new theorem is an extraction and anisotropic extension of that mechanism, not a claim that the coefficients are best possible. General convex-analytic ergodic-optimization literature may contain abstract formulations that could subsume the cone observation under different terminology; that remains the main bibliographic risk. No claim is made on the axes \(p=0\) or \(q=0\), or for interval beta-transformations without an additional coding argument.

Same-model review: passed. Independent audit: not yet performed.
