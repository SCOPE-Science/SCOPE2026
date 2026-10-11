# Scientific review

## Correctness — PASS

The Fourier-zero criterion follows directly from character orthogonality. In an affine-independent four-frequency set, six of seven nonzero directions in its three-dimensional difference span are common Fourier zeros. The rank-two evaluation map for either shape of a four-point time set forces the missing seventh direction into the annihilator of that time set. The exact \(4\)-to-\(1\) complement count and \(8\)-per-coset enumeration give the global count. The boundary \(d=2\) and the triple-plane obstruction were checked separately. The actual `checker.cpp` passed 5,013 small-family comparisons using integer arithmetic. No finite check substitutes for the universal proof.

## Originality — PASS, with residual risk

The closest primary source, Ferguson–Mayeli–Sothanaphan, arXiv:1904.04487, Section 7.1, studies simultaneous *invertible* exponential bases and constructs a three-set obstruction for two-element time supports. It does not give this exact orthogonal four-point spectrum count or the affine-plane linearization. Kiss–Matolcsi–Matolcsi–Somlai, arXiv:2212.05513, studies tiling/weak tiling and spectral pairs, rather than simultaneous multiplicities. Older small-order complex-Hadamard and universal-spectra papers could contain equivalent special cases or a stronger statement; an abstract-only 2004 source could not be decisively compared in full. The literature comparison therefore supports originality without proving bibliographic uniqueness.

## Value — PASS

For arbitrary finite families of four-point binary subsets, simultaneous orthogonal spectrality can be decided by searching only two-dimensional frequency subspaces, even when the complete spectra themselves can be affine-independent. The exact multiplicative split by the joint annihilator is a structural classification and counting law rather than a scalar single-instance optimization. The three-set obstruction gives a motivated sharp pair-versus-triple example in the smallest space admitting three independent directions. Potential use includes common Fourier bases, multi-tiling cross-sections, and restricted Walsh-Hadamard matrices.

## Scope and risks

The theorem is restricted to four-element time sets over characteristic two, orthogonal rather than merely invertible bases, and families of finite size. An independent scientific audit has not been performed. Possible older equivalence through universal-spectrum theory remains a bibliographic risk; the searched results did not establish that implication.

Same-model review: passed. Independent audit: not yet performed.
