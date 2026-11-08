# Review: a chiral-to-synchronous instability switch in a lossy four-patch population ring

## Correctness — PASS

The exact equilibrium and linearization are derived in RESULT.md, including the easily missed instantaneous reaction derivative. The four cyclic Fourier factors give an exhaustive spectral factorization. The first rotating and synchronous imaginary-axis crossing thresholds have closed forms; the alternating spatial mode always crosses later than the synchronized mode. Strict convexity of the scalar threshold comparison proves uniqueness of the positive migration crossover. The derivative of the characteristic root with respect to delay establishes destabilizing first crossings, and the second rotating branch cannot restore stability in the rotating-first regime. The proof states all parameter and linear/nonlinear boundaries. `verify.py` replayed successfully as a finite diagnostic, not as an infinite proof.

## Originality — PASS (best knowledge)

Targeted mathematical research searches, the accessible private claim ledger and primary source comparisons found no direct equivalent of the exact four-patch cyclic-migration onset classification and unique chiral-to-synchronous switch. Huang–Chen's 2023 initiating patch population theory covers small dispersal and near-extinction regimes and notes intermediate-dispersal difficulty. Liu–Shen–Chen's later homogeneous advective system has downstream boundary loss in an open chain rather than a closed directed cycle. Petit et al.'s 2015 single-species result delays migration on an undirected network, and their 2016 extension treats two species with delay in diffusion. The full 2017 Otto–Wang–Radons paper was not inspected; other unindexed equivalent results remain possible. The work does not claim to invent the general Fourier or DDE crossing method.

## Value — PASS

A minimal four-patch ecological circulation model has two genuinely different linear oscillatory-onset mechanisms. The exact transport threshold identifies which spatial pattern first becomes unstable, produces a two-frequency spectral degeneracy, and clarifies why directed cycling differs from undirected or open-ended patch movement. This is a natural full parameter classification of a model-motivated question, not an arbitrary finite calculation.

## Limitations

Only linear exponential stability and spectral instability of the positive equilibrium are established. No nonlinear bifurcation coefficient, attracting traveling wave, invariant torus, heterogeneous-parameter theorem or global basin result is proved. A negative semantic search is not a proof of worldwide originality. Details of inspected literature and remaining risks are in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
