# Scientific review

## Correctness

**PASS.** The claim's exact and asymptotic assertions are proved from the explicit randomized diagonal propagation, a binomial generating-function identity, strict scalar monotonicity, an invertible scaling law at small time steps, and a Poisson limit. The positive limiting mean-square error follows from nonconstant Poisson randomness, not merely from floating-point calculation. The full verification script, extracted from the same package, performs 819 finite independent comparisons. This is finite corroboration; the general conclusion relies on the written proof. The scaling \(p_h\sim\kappa h\) is not assumed, but derived.

## Originality

**PASS with publication-priority limitations.** The closest source, Veldman–Zuazua (2021 preprint; 2022 published), contains the same basic reciprocal-probability randomized generator and general diagonal two-block model in Example 3, but optimizes the operator variance of the generator, not the worst mean-square energy of the exact random subflow. Its probability \(a/(a+b)>1/2\) differs strictly from the unique energy optimizer \(p_h<1/2\). The singular mesh-dependent choice \(p_h\sim\kappa h\), the resulting nondegenerate Poisson terminal state and the exact positive consistency defect are not implied by their fixed-probability convergence bounds. Eisenmann–Stillfjord's separate randomized backward-Euler analysis and classic coordinate-descent probability optimization have different step maps and different objectives. Actual research-record searches found closest randomized Gauss–Seidel, two-coordinate PAGE and diagonal coordinate sampling results, none with this exact model/statement. The accessible record is not a proof of unique publication priority; specialized older stochastic-semigroup literature could contain a related formulation.

## Value

**PASS.** This classification resolves a practical conflict between designing a randomized propagator for fast energy damping and using it as an accurate numerical solution. It proves an exact boundary where optimizing one natural stability metric makes the method inconsistent even though its worst-case energy reaches the true semigroup rate. The opposition to the source's generator-variance optimizer and its exact Poisson mechanism give a structural design warning, not merely a special-case routine computation.

## Scope and limitations

Only independent exact subflows of two commuting unequal dissipative modes are covered; no claim is made for noncommuting splittings, a general solver, optimal approximation error, or cost-normalized work. The mathematical claims are analytic; the finite verifier is supplementary. A complete exhaustive historical priority search and independent validation are not claimed.

Self-review: passed. Independent audit: not yet performed.
