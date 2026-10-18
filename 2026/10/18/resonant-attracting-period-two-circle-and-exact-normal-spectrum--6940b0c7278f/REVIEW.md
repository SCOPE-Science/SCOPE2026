# Scientific review: resonant attracting period-two circle

## Correctness

**PASS.** At synchronization, each head's softmax row is uniform and the derivative of its weighted token mean equals the average tangent perturbation; the derivative of the weights cancels by row stochasticity. The effective symmetric value matrix has opposite, equal-magnitude extreme residual eigenvalues at the stated step. Its normalized restriction to the extreme plane is a reflection, giving the entire period-two circle. The tangent mean/zero-sum decomposition diagonalizes the two-step derivative and yields every normal multiplier and multiplicity. Compactness and a uniform spectral gap below one give an invariant tubular neighborhood, exponential normal contraction, and convergent asymptotic phase. A derivative-level tangency cancellation makes the phase shift quadratic in the initial normal deviation. The checker independently evaluates the full nonlinear map for 135 random-head configurations/phases and verifies three exact-rational values. Finite tests are not used as proof.

## Originality

**PASS with bibliographic risk.** Altafini, arXiv:2610.13518v1, analyzes the same attention map, including multihead linear stability, but its principal-consensus theorem requires a strict step bound and the examined sections do not give the resonant periodic circle's full normal Floquet spectrum or nonlinear convergence to a selected periodic state. Gao–Yang–Chen, arXiv:2609.28448v1, compute stable consensus flips for a different, diagonally masked, isotropically negative value map and discuss degenerate negative eigenspaces, not a simple positive/negative extreme spectral tie. Tsuzuki–Ohki, arXiv:2512.21469v1, and classical normalized power iteration already provide the **synchronized** spectral-reflection mechanism; it is not claimed independently. A previous two-token diagonal calculation covers a stable synchronized sign-flip strictly beyond the critical step, not the critical continuum. The asserted advance is the full many-token/multihead derivative spectrum with phase-dependent disagreement modes and local nonlinear phase selection. This is supported by targeted mathematical-record and primary-paper comparisons, not by an absence-of-search-results argument. More general unindexed literature might contain an equivalent implication.

## Mathematical value

**PASS.** The exact step boundary of the motivating attention stability theorem is dynamically degenerate rather than a generic isolated period-doubling. Identifying a normally contracting continuum of two-cycles resolves what replaces strict hyperbolicity there. The complete, phase-dependent Floquet spectrum distinguishes common-mode and token-disagreement relaxation and exhibits zero linear disagreement response at phases \(\theta=\pi/4\) modulo \(\pi/2\). Universality with respect to arbitrary query/key matrices and individual head coefficients is a structural consequence of attention's row normalization, relevant to the model rather than an arbitrary parameter slice.

## Scope and limitations

The theorem is local and holds only at exact resonance, with a symmetric effective value matrix and full self-inclusive softmax. Each individual cycle has a neutral tangent direction; only the entire periodic circle attracts nearby states. The result does not describe arbitrary global basins, masked attention, positional effects, realistic layer-norm and feedforward components, or non-symmetric effective value matrices. Classical normalized-power behavior is acknowledged as prior; an equivalent full interacting-token statement may remain undiscovered in existing literature.

Self-review: passed. Independent audit: not yet performed.
