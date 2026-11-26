# Independent mathematical audit

## correctness

PASS

Exact minimization in coordinate i subtracts (Ce)_i² from C-energy, so the sharp one-step mean decrease ratio is λ_min(C^(1/2)diag(p)C^(1/2)). The ordinary-coordinate contrast eigenvalue of C is β>0, and the remaining block determinant is δ=α−ms²=β+m(ρ−s²)>0. Concavity and permutation averaging reduce existence to symmetric p, and no boundary probability can be optimal. With r=q/v the transverse branch is β/(m+r); the coupled branch is ℓ/(m+r), where r=ℓ(α−ℓ)/(δ−ℓ) increases from 0 to ∞ on 0<ℓ<δ. The derivative of the coupled branch has sign (δ−(1+s)ℓ)(δ−(1−s)ℓ), hence a single peak at ℓ=δ/(1+s), r=(α+ms)/(1+s). The branch crossover occurs at ℓ=β, r=βρ/(ρ−s²). The unique symmetric optimum is at the lesser r; the order changes precisely when ms²+βs−mρ=0, with its positive root strictly inside the domain. Both formulas agree there. For any unrestricted optimum the probability sums by class equal those of the unique symmetric one. A coupled minimizing eigenvector z there gives the same Rayleigh value at the unrestricted optimum because C^(1/2)z is constant on each class. Both class entries are nonzero by the nonzero coupling. Equality forces z to be an eigenvector at both probabilities, and subtracting the equations forces equality of every probability, even at the tie. The negative inverse-sign triangle is also correct. The supplied checker was inspected, not executed; its stated assertion count agrees with a separate count of its loops, not a rerun of the checks.

## originality

PASS

The exact spectral objective and its general SDP are known. The supported distinct contribution is the analytic two-regime evaluation with unrestricted uniqueness in this family, not the objective or generic existence of optimal probabilities. There is a formula-level equivalent catalog result for a wider range in the Kaczmarz formulation, catalogued a week later; it is not evidence that the frozen statement was covered earlier. The earlier items inspected do not establish this transition and full optimizer.

## value

PASS

With identical coordinate Lipschitz constants, a practitioner using only those constants cannot tell which coordinate to sample more often or when the active error modes change. The formulas give the sharp conditional rate and the unique attainable probability law without repeatedly solving a numerical design problem. The phase boundary identifies precisely when control of the transverse errors ceases to constrain that law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
