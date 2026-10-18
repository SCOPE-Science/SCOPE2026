# Scientific review: exact magnetic Grover revivals on complete bipartite graphs

## Correctness — PASS

The claim covers every pair of integers \(m,n\ge2\), all real single-edge magnetic phases \(\beta\), and the explicitly defined unitary Grover arc walk. The proof derives the exact determinant identity from a coisometry and a magnetic flip; evaluates the two singular values of the phase-modified all-ones bipartite block; factors the characteristic polynomial; and uses the resulting complete eigenvalue multiset to prove the rank-eight four-step defect, sharp operator/Frobenius norms, and minimal return periods. Both zero flux and maximal-flux eigenvalue collisions follow from the same polynomial identity, with unitary diagonalizability. The density/nullity of the periodic parameter set follows from strict monotonicity of the angle on a half-circle. The provided checker passed 193 counted symbolic and matrix assertions, including three exact characteristic-polynomial reconstructions; numerical checks are supporting evidence and not the proof.

## Originality — PASS, with residual risk

The closest scientific source is Sekido and Segawa, arXiv:2607.14797v1 (2026), which introduces the magnetic Grover model and studies small-perturbation effective dynamics, including balanced complete bipartite graphs. The inspected accessible full-text definitions, theorems and Section 5 do not state an arbitrary-strength characteristic polynomial, a universal eight-dimensional exact four-step defect, or a complete rational-angle revival classification for arbitrary \(K_{m,n}\). Chen, arXiv:2211.02752 (2022), treats unmagnetized bipartite-walk spectral criteria. Kubota, arXiv:2609.08315 (2026), studies unmagnetized periodic graph families. General Grover spectral mapping is acknowledged; the finite-flux rank-two evaluation and single-angle arithmetic remain graph-specific additional work. Primary and research-record searches found no directly covering statement, although this is not a uniqueness guarantee. Full text of Chen was not available in the inspected material, and a broad, unlocated weighted-walk spectral result could imply the specialization.

## Value — PASS

The motivating physics question is whether magnetic flux destroys periodic quantum return. The finding gives the exact answer for the first nontrivial dense bipartite family, without a small-flux restriction: despite \(2mn\) arc amplitudes, precisely eight modes obstruct the unperturbed four-step return. The exact fourth-step error shrinks uniformly with graph size, and dense but measure-zero tuned phases have explicit exact periods. This distinguishes exact revival, approximate revival, and size-dependent robustness quantitatively and applies to every imbalance of the part sizes, not an isolated graph or arbitrary invariant.

## Scientific limitations

Only one magnetic edge, standard Grover coin, and finite \(K_{m,n}\) with both parts at least two are covered. Multiple independent fluxes and other coin choices are unproved. The statement does not assert that no broader existing theorem can imply these specialized formulas. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
