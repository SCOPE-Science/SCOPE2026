# Scientific review

## Correctness — PASS

For each positive step size, every edgewise midpoint matrix is a nonnegative doubly stochastic averaging matrix with positive diagonal, and the complete tree sweep is primitive. The limiting factors are endpoint transpositions, whose product on a tree is a single cycle. The exact first-order perturbation of the ordered product is the sum of transformed incidence outer products with reciprocal-rate weights. The single-cycle Fourier eigenvectors yield the explicitly stated attenuation rates; the product identity for transformed transpositions establishes strict positivity of each nonconstant rate. Explicit transformed chords give the path and star constants. Laplacian algebraic connectivity gives the small-step ordering; the large-step coefficients give the opposite strict ordering. The accompanying checker reproduces exact and sampled consequences but does not replace the proof.

## Originality — PASS, subject to residual publication-priority uncertainty

Spiteri–Wei (arXiv:2205.06365) analyze fractional-step integrators and scalar/simultaneously diagonalizable stability, not the noncommuting edge Laplacian's singular large-step permutation law. Yu–Anderson–Mou–Liu–He–Morse (DOI:10.1109/TAC.2017.2688278) prove the *known* tree edge-order spectral invariance and explicitly cover non-half common gossip weights; their paper's fully examined path/star examples do not derive the new stiff-limit Fourier coefficients or the reversal across the physical midpoint step. Chen–Belabbas–Liu (arXiv:2102.08853) treat holonomic gossip frameworks without this parameter asymptotic. Semantic mathematical-record searches returned related positivity, consensus and cyclic-process results but no covering exact claim. Equivalent developments in overrelaxed cyclic projections remain a residual risk; no stronger novelty certification is claimed.

## Mathematical value — PASS

Tree topology changes which graph is preferable for the same complete-sweep edgewise implicit-explicit integration cost. The universal single-cycle formula quantifies slow stiff-limit mixing for every tree with arbitrary positive weights and edge ordering; the path–star reversal supplies a directly interpretable numerical-design boundary. This is not a normalization identity or an arbitrary finite enumeration. The result concerns asymptotic spectral mixing, not transient norm bounds, and asserts no unique crossover or universal graph optimum.

Self-review: passed. Independent audit: not yet performed.
