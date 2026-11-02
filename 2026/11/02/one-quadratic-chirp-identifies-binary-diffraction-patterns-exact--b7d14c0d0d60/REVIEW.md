# Scientific review

## Correctness — PASS

The claim is about the fully labelled length-\(N\) Fourier power spectrum after a single explicit unit-modulus quadratic phase mask. Direct expansion of Fourier intensities and discrete Fourier inversion recovers each complex autocorrelation lag. At odd prime length the chirp multiplies the terms in every nonzero lag by all primitive prime roots in a permuted order. If two binary autocorrelations agree, irreducibility of the cyclotomic polynomial forces the difference of all ordered-pair indicators to be constant. Equality of zero-lag energy excludes a nonzero constant. Every binary support of size at least two is determined by its nonzero-lag pair indicators. Conversely, the displayed two-point masks give identical power spectra for every composite length. The algebraic-integer norm of one nonvanishing lag difference supplies the stated separation bound. These are valid all-length proofs, not extrapolations from enumeration.

A standalone exact-arithmetic checker independently tests the claimed collision class for every binary vector at lengths \(3,5,7,11\) and explicit distinct composite witnesses at eight lengths. The checker and its limits are recorded in VERIFICATION.md.

## Originality — PASS (historical priority provisional)

The closest focal preprint, Bendory–Edidin–Gonzalez (arXiv:2301.10647v1), establishes an equivalence between unmasked finite-alphabet autocorrelation collisions and homometric partitions (with generic alphabet hypotheses), not exact uniqueness after a fixed quadratic mask. Jaming–Rathmair (arXiv:2205.08753v1) address three-mask continuous phase retrieval and different finite discretizations, not the binary one-mask prime/composite dichotomy. Earlier sparse-binary phase retrieval examines unmasked, often oversampled data. The accessible indexed description of Chen–Fannjiang's one-mask study addresses random masks, sector restrictions and iterative algorithms, not this arithmetic chirp claim.

The closest searched mathematical records concern unmasked signed four-atom Fourier collisions, a Gabor tomography system using all time-frequency shifts, and chirp phase Hessians; none implies the exact fibres of one chirp-coded diffraction pattern. No exact same-source statement was found. Search absence is not proof of priority, and the most significant residual risk is a less discoverable deterministic Fresnel-mask result. Equivalence and stronger-prior coverage were compared by the actual mathematical observation and signal class, not only title overlap.

## Mathematical value — PASS

One intensity vector from one deterministic phase-only mask is a standard minimal-measurement problem for finite-alphabet diffraction. The result completely classifies the attainable collision fibers at every prime length, achieves the information-theoretic maximum number of distinguishable binary arrays permitted by unavoidable singleton ambiguity, and proves a sharp arithmetic boundary: every composite length already has a two-point collision for any quadratic chirp. This is a structural all-length statement, not an arbitrary finite census or a routine computation. The conservative algebraic separation supplies a quantitative exact-noise margin, although it is not a practical optimal threshold.

## Scope and limits

The theorem does not address nonbinary complex signals, subsampled frequencies, nonquadratic deterministic phase masks, or optimal numerical stability. The classification is not a claim about general one-mask complex phase retrieval. Historical priority remains provisional.

Self-review: passed. Independent audit: not yet performed.
