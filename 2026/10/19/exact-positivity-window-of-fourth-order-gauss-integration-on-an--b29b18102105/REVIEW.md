# Scientific assessment: Exact positivity window of fourth-order Gauss integration on an eight-state directed ring

## Correctness — PASS

For the rate-one directed eight-cycle, the rational map is well defined for every nonnegative timestep and exactly conserves row and column sums. A polynomial inversion modulo the eight-cycle relation reconstructs all eight signed circulant coefficients. Four coefficients are positive for positive timesteps by coefficientwise-positive numerator polynomials; the other four factor into exact integer polynomials with one positive zero each. Descartes' rule, exact substitutions at rational timesteps and the signs of leading coefficients prove that the coefficients are simultaneously nonnegative exactly for the single closed interval bounded by the two displayed algebraic constants. The low- and high-step negative coefficients exclude the remaining positive times. The standalone verification program checks exact factorization, signed roots and direct rational matrix inversions. Numerical trials by themselves cannot establish the universal statement, which is secured by the symbolic proof.

## Originality — PASS, with residual risk

Zappavigna et al. establish diagonal Padé small-step positivity failure using a nonconservative shift; Lóczi and Ketcheson characterize general absolute-monotonicity limits. The closest published exact eight-state Markov result determines the different positivity window of an absorbing pure-birth chain, rather than the present irreducible uniform cyclic chain. Searches for Padé, fourth-order Gauss, cyclic convolution, ring CTMCs and exact transition thresholds found no matching all-step cyclic theorem. The new assertion is only the exact all-step positivity classification for this ring; small-step negativity and the minimal eight-state dimension are explicitly pre-existing. Unindexed equivalent Fourier or circulant calculations remain a residual risk, so this review is not an independent novelty certification.

## Value — PASS

The irreducible, regular eight-cycle is a canonical conservative contrast to the absorbing minimal-dimensional witness. Its exact nonnegative-step set is disconnected and features a bounded recovered interval; an exact positivity criterion is useful for choosing a stochasticity-preserving numerical step and for differentiating strong-stability/positivity restrictions from actual graph-specific behavior. The eight-state size is motivated by the sharp dimensional obstruction, not an arbitrary census entry.

## Scope and limitations

The claim treats only the homogeneous one-directional eight-cycle and the endpoint matrix, not arbitrary irreducible chains, rates, cycle sizes, floating-point rounding or internal Gauss stages. Explicit symbolic reproduction requires SymPy. The bibliographic comparison includes two readable full-text primary mathematical papers and the complete nearest published exact result; equivalent work outside accessible sources remains possible.

Self-review: passed. Independent audit: not yet performed.
