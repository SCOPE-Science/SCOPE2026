# Scientific review: rational sigmoid detuning

**Correctness — PASS.** The finite \(q\)-grid permutation gives an exact branchwise return displacement. The two nearest sites supply the hyperbolic-sine term with a uniform \(O(a\epsilon^2)\) return error; direct differentiation yields the multipliers. Compact-variable Euler convergence follows from a uniform local truncation error and discrete Grönwall inequality. The two outer limits follow from one dominating logistic tail on opposite sides of the grid cell, with local return contraction. The embedded code checks 12 critical- and 16 outer-scale instances; it is not a substitute for the analytic proof.

**Originality — PASS under self-review.** The closest available publication, “Singular half-grid selection and exponentially weak attraction in rational EOS maps,” derives the rational half-grid and attraction gap only with \(b=p/q\) fixed. Its statement cannot imply the parameter-dependent nonlinear slow flow or the order-one shifts at the larger exponential detuning. The motivating papers discuss rational attraction and bifurcation hopping but do not supply these crossover laws. Searches for equivalent logistic-rational-resonance and exponential-detuning formulations found no dominating result. Equivalent theory under different terminology remains possible.

**Value — PASS.** The new two-scale theorem explains why exponentially small perturbations of the rotation parameter lead first to a universal slow flow and ultimately to macroscopic phase changes while the cycle remains locally attracting. Both regimes are motivated by numerically reported hopping in the source's bifurcation diagrams, not arbitrary parameter slicing.

**Limitations and priority risk.** Fixed rotation numerator and denominator; local periodic solutions only; no global uniqueness or uniformity over growing denominator. Classical smoothing/Arnold-tongue asymptotics could contain equivalent parameter windows. The review is not independent.

Self-review: passed. Independent audit: not yet performed.
