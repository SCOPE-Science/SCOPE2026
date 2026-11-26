# Mathematical review: the second-order lattice temporal smoothing constant

## Correctness — PASS

The proof constructs the integer-lattice heat kernel, identifies the exact \(\ell^1\) and \(\ell^\infty\) convolution norm, and establishes the single sign crossing of each Bessel derivative by a Riccati argument. A discrete telescope proves sharpness, and equality in the triangle inequality characterizes the inputs that attain sharpness at a given output site. This fixed-site characterization does not exclude other inputs that attain the norm only as a supremum. Uniform Fourier kernel expansions control both the threshold locations and the oscillatory second-order error. The original verification reported 134 finite numerical assertions, which are supporting checks and not substitutes for the analytic proof.

## Originality — PASS within examined sources

*Exact switching staircase for discrete-Gaussian gradient peaks* (Resultary 14f278a0557c) already yields the all-time norm and staircase after the identity \(I_{m-1}-2I_m+I_{m+1}=2(I'_m-I_m)\) and a central-interval telescope. Its strict quadratic brackets leave room between the lower endpoint \(m^2\) and upper endpoint \(m(m+1)\), so they do not determine the constant shift from \(m^2\). Abadias et al., Theorem 4.3(iii), give the order bound \(\|\Delta G_t\|_1\lesssim t^{-1}\). Neither comparison supplies the second-order asymptotic terms established by the uniform Fourier expansion and localization of the maximizing integer. The originality assessment concerns this narrower asymptotic statement, not the antecedent identities or priority across records.

## Mathematical value — PASS

The second-order term of the sharp deterministic amplification has an entire accumulation interval rather than a numerical constant, a lattice phenomenon hidden by qualitative diffusion bounds. It gives a quantitative benchmark for the continuum approximation that depends on the phase of the diffusion scale relative to the lattice, and distinguishes the exact switch times from rounded continuum predictions.

## Scientific limitations

The model is the homogeneous one-dimensional integer lattice with the specified unnormalized generator. No higher-dimensional or arbitrary-graph result is claimed. The comparison does not certify global historical priority.
