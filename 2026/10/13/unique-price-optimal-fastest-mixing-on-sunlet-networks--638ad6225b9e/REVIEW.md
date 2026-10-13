# Scientific assessment: price-optimal mixing on sunlet networks

## Correctness — PASS

The proof derives the two-by-two Fourier blocks of the ordinary weighted Laplacian, with the smallest nonzero cycle eigenvalue \(4\sin^2(\pi/n)\). A sharp product constraint and arithmetic-geometric mean solve the symmetric budget problem with equality conditions; concavity of the Fiedler eigenvalue then promotes the sharp bound to all allocations. Equality of two first-harmonic Rayleigh quotients at an arbitrary optimizer forces every pendant conductance and both neighboring cycle conductances to equal their symmetric values, proving uniqueness. All parameters require \(n\ge3\), \(t>0\); disconnected boundary allocations have gap zero. The asymptotics follow from the exact formula. The standalone checker supplies exact rational identities and finite matrix comparisons but is not an infinite proof.

## Originality — PASS with remaining historical risk

Göring–Helmberg–Wappler (2005) develops general algebraic-connectivity/embedding duality; Sun–Boyd–Xiao–Diaconis (2006) gives the general fastest mixing Markov process optimization and closed forms for paths and plain cycles. Wan et al. (2008) give structural design theorems, especially for trees; the sunlet is unicyclic. Liu–Shao (2022) treats signless and normalized spectra of prescribed weighted corona graphs, not price-optimal ordinary-Laplacian allocation. Du–Zhu–Gao–Li (2022) derive a fixed-weight ordinary-Laplacian characteristic polynomial and analyze coherence rather than optimizing spectral gap by prices. These stronger general algorithms and adjacent spectral formulas were compared at the statement and objective levels. The reviewed materials did not state this arbitrary-price sunlet optimum or its uniqueness under all individual edge variations. Unindexed historical specializations and incomplete accessibility to some material are residual risks; this is not a certification of worldwide novelty.

## Value — PASS

The problem is a natural resource design on a ring with terminal users, where retaining and strengthening both ring and pendant links competes for one budget. The theorem gives a global, unique all-edge allocation, an exact value, a proof that price alone never deletes edges in this family, and the network-size/price crossover. It avoids numerical semidefinite optimization for an infinite graph family. This is more than a fixed-weight spectral-table entry or a routine finite enumeration.

## Scope and limitations

The result assumes symmetric continuous-time rates, uniform stationary masses, exactly one pendant per cycle vertex, two within-orbit price classes, and a linear budget. Discrete-time mixing and other attachment graphs are not addressed. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
