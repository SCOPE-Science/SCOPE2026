# Scientific review

## Correctness
**PASS.** The Fourier decomposition is explicit for every integer alphabet size, including composite sizes; its eigenvalue multiplicities add to the matrix size. The scalar parity-sector root is shown unique in the relevant nested interval by an alternating-tail derivative bound. The finite-difference inequality proves that every remaining sector is strictly positive through the threshold. Binary-subcube nesting forbids the rest of the parameter interval. The rank follows from the exact top-sector multiplicity. The standalone checker reproduces exact rational identities and selected direct Fourier sums. All quantified conclusions follow from proof, not finite testing.

## Originality
**PASS, within bounded comparison.** The strongest overlapping earlier claim covers the binary alphabet only and only the restricted range \(0<u\le1/16\); this new claim covers all alphabet sizes and the whole admissible/forbidden interval \(0\le u\le1\), and determines the \((s-1)^n\) endpoint nullity. Feragen et al. prove all-bandwidth geodesic-space obstructions, and Jayasumana et al. formulate the generic all-bandwidth Schoenberg criterion; neither derives these precise finite-product thresholds. The closest other retrieved claims treat Hamming-shell concentration, Turán masses, and Krawtchouk projection norms, not this squared-distance kernel. An equivalent treatment in older Hamming association-scheme literature remains possible.

## Value
**PASS.** Squared intrinsic Hamming distance is a natural alternative to the ordinary Hamming/Laplacian kernel, but its exponential does not automatically preserve positive definiteness. The result provides the **sharp usable bandwidth** for every categorical alphabet without dependence on alphabet size, a nontrivial structural conclusion; the exact boundary-nullspace dimension explains a loss of covariance rank. This is a complete classification rather than a narrow numerical threshold or routine special case.

## Closest literature and limits
Feragen–Lauze–Hauberg (2014 preprint; CVPR 2015), Jayasumana et al. (2014 preprint), and an earlier restricted binary-cube cutoff were compared at the level of theorem implications. The first two do not state a finite Hamming-product criterion, while the earlier binary cutoff is subsumed only as a proper subrange and alphabet specialization. Literature comparisons are bounded; the checker is not independent validation.

Self-review: passed. Independent audit: not yet performed.
