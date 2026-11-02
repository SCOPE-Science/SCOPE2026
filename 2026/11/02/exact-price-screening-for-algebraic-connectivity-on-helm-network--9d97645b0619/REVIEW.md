# Self-review

## Correctness — PASS

The unrestricted upper bound follows from concavity of the unnormalized Laplacian's second eigenvalue and averaging over price-preserving dihedral symmetries. The quotient three-by-three and Fourier two-by-two characteristic polynomials are explicitly derived, with the smallest root selected and boundary conditions checked. After normalizing the target gap to one, two scalar inequalities are equivalent to the full spectral requirement. Linear minimization for fixed leaf conductance and strict convexity of the remaining one-variable objective establish every price regime, including the degenerate boundary. The support conclusion for all asymmetric optimizers uses preservation of each orbit's total weight by averaging, not an unsupported uniqueness assertion. `VERIFY.py` reproduces 2 symbolic polynomial identities, 2 rational threshold examples, 84 full-matrix cases and 48 asymmetric random-start comparisons. Finite computations alone do not prove the universal theorem.

## Originality — PASS on the inspected comparisons

Ghosh–Boyd (2006) provide the general concavity/symmetry machinery; their block-ring example lacks a central hub and private leaves and has different constraints. Shakeri et al. (2015) optimize only one-to-one interlayer couplings with the two layer Laplacians fixed, so their threshold does not determine the three-class price frontier here. Search terms included weighted helm Laplacian, rim suppression, price screening, algebraic connectivity optimal weights, spoke/rim/pendant graph, and corona-related mixing. The closest compared results do not logically imply the explicit helm formula, the mixed-phase root or the equal-price threshold at six rim sites. Index coverage is limited and further specialist overlap remains possible.

## Mathematical value — PASS

The helm graph is a natural wheel-with-peripheral-sensors topology. Its design has three competing edge functions: hub-to-rim access, rim circulation and leaf attachment. The result provides an exact allocation rule across every positive price ratio and a whole-class deletion threshold that depends nontrivially on cycle size; at equal prices the preferred topology changes sharply between six and seven rim vertices. The exact scalar reduction also removes the need for numerical semidefinite optimization within this family. This is a structural design classification, not a generic re-expression of the convexity method.

## Limits

Unrestricted individual optimizer uniqueness, degree-normalized or stochastic objectives, edge caps, arbitrary heterogeneous prices, and robustness to failures are not assessed. The literature search is not a proof of universal novelty; independent specialist review is outstanding.

Self-review: passed. Independent audit: not yet performed.
