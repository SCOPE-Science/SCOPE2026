# Scientific review: conditional compound-Poisson telegraph travel time

## Correctness
The theorem is established by the independently derived telegraph Fourier--Laplace resolvent. Dividing its weighted endpoint density by the positive Laplace endpoint marginal yields a conditional Laplace transform. Two positive integrable Lévy kernels reproduce that transform exactly, using Frullani's integral and the modified-Bessel \(I_1\) transform proved in the result. Finite jump measures justify the two compound-Poisson components, and their first two cumulants yield the conditional moment formulas. The ballistic atom agrees independently with the no-surviving-reversal joint boundary mass in the motivating paper. A source-path verification program passed 72 numerical cross-checks; they support but cannot replace the proof.

## Originality
The closest primary source, Orsingher--Marchione (arXiv:2610.15094v1), proves the complete joint law of position and killing time, so neither the joint density nor its Bayes conditional ratio is claimed as novel. The additional explicit finite compound-Poisson decomposition, separate Lévy jump laws, and endpoint-distance convolution semigroup are not stated in its inspected Sections 2--4 and Appendix A; these require the positive Bessel factorization beyond the joint-density formula. Cinque (arXiv:2202.01904) treats a different conditional telegraph setup. The literature searches returned no exact decomposition, while older transform and first-passage works create a material residual possibility of an implicit equivalent result. The separation from the available joint-density theorem must be interpreted as a structural law, not a new marginal distribution.

## Mathematical value
The posterior time needed to explain a measured final displacement is a natural inverse observable in velocity-jump transport. The result identifies an unexpected finite-jump representation rather than just a complicated Bessel conditional density, providing a direct sampling construction, a monotone coupling in observation distance, exact ballistic probabilities and linear conditional moments. These are structurally motivated and do not depend on arbitrary finite choices of parameters.

## Scope and unresolved risks
The result assumes a symmetric initial direction, equal speed magnitudes, constant surviving-switch rate, and independent exponential killing. It is not a planar or general-reversal-rate theorem. Prior exact joint-density coverage is explicitly acknowledged, and an unlocated older resolvent or bridge result could contain the same finite Lévy factorization. An external mathematical audit is still required.

Self-review: passed. Independent audit: not yet performed.
