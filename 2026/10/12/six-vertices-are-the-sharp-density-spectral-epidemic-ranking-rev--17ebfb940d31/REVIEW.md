# Self-review

## Correctness
**PASS.** At fixed vertex count, inverse average degree orders connected graphs exactly by edge count in the opposite direction, while the spectral threshold orders them by adjacency spectral radius in the opposite direction. Complete exact generation of every connected graph through five vertices shows that spectral radius never decreases when edge count increases across two different graphs at those orders. The six-vertex star-cycle witness is symbolic: \(5<6\) in edge count but \(\sqrt5>2\) in spectral radius. The persistent family follows from \(2(n-1)/n<2\) and \(\sqrt{n-1}>2\) for every \(n\ge6\). The packaged verifier returns `VERIFY_OK`.

Risk: the epidemic interpretation is mean-field, not an exact finite-state stochastic phase transition.

## Originality
**PASS.** Wang et al. already contrast inverse average connectivity with the largest-eigenvalue threshold and explicitly give the star formula. Van Mieghem et al. give the N-intertwined SIS spectral threshold. These sources own the epidemiological distinction between homogeneous and spectral summaries. The accepted claim is narrower and finite-extremal: six vertices are necessary and sufficient for opposite strict rankings among equal-order connected simple graphs, with a star-cycle witness that persists for every larger order. Targeted exact and alias searches did not locate this sharp boundary.

Risk: the witness uses standard graph spectra and could occur in an unindexed classroom or software example even though the universal minimum was not located.

## Value
**PASS.** Average degree is the canonical homogeneous contact-density summary, while spectral radius is the canonical network-sensitive mean-field epidemic summary. The theorem gives the smallest network on which “more edges” and “lower epidemic threshold” become genuinely incompatible rankings, and the all-order star-cycle family shows that the effect is structural rather than a one-off enumeration artifact.

Self-review: passed. Independent audit: not yet performed.
