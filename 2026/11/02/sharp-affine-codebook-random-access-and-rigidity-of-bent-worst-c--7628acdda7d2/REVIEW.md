# Self-review

## Correctness — PASS

For all even \(m\ge2\), Walsh orthogonality gives \(\sum_aW_a^2=N^2\). Normalizing signed Walsh coefficients by their \(\ell_1\) sum constructs a valid encoder that attains identical success at each coordinate, at least \(\frac12+\frac1{2\sqrt N}\). The explicit bent quadratic has flat Walsh spectrum, and averaging the correlation of an arbitrary mixture over all coordinates proves the matching converse. Strictness of Cauchy–Schwarz separates nonbent inputs. At bent inputs, equality forces a unique inverse-Walsh vector of signed message probabilities, and saturation of the \(\ell_1\) probability constraint forces the unique distribution. The integer verifier checked all \(2^{16}\) tables at \(m=4\) as well as quadratic bent spectra in dimensions \(2,4,6,8\). The infinite claim relies on the proof, not the finite computation.

## Originality — PASS, with explicit priority risk

The April 2026 RAC paper gives a general geometric reduction and a different punctured simplex codebook, and uses Walsh orthogonality, but does not state or imply the full affine-codebook exact value without the additional extreme Walsh \(\ell_1\) calculation. The 2007 Reed–Muller list-decoding literature already knows that bent words maximize a Hamming-ball list-size invariant, a distinct function from coordinatewise stochastic recovery success. The classical sharp Walsh bound and bent characterization are **not new** and could make this RAC application a short consequence of known geometric identities. The checked literature and mathematical-record claims exposed no prior statement of the joint minimax, exact worst-case class, and unique optimal encoder; that priority risk persists, and independent verification is not claimed.

## Value — PASS

The fixed affine decoder is a canonical \(2^{m+1}\)-codeword, length-\(2^m\) random-access design. The theorem solves its global worst-case stochastic encoding problem for every even dimension, classifies *all* input adversaries exactly and proves uniqueness of the optimal encoder at each adversary. It supplies an explicit polynomial-time Fourier sampler, rather than solely an unquantified geometric reduction or a small finite table. The conclusion is not an unrestricted RAC bound, not a new bent-function characterization, and does not compare with unfixed decoder families.

## Residual scientific limitations

The numerical optimum uses classical Walsh–Hadamard convexity and bent-function facts and may have a prior unindexed equivalent formulation. A 2007 decoding source was accessible in relevant extracted portions rather than reviewed page by page. No external independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
