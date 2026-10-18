# Scientific review: odd/even Cartesian coherent-state tomography

## Correctness
PASS. Explicit objects are the real \(m^2\)-dimensional Hermitian matrix space and its \(m^2\) sampled rank-one evaluation functionals. The odd-order proof is independent of node placement: grid-vanishing polynomial division reduces the highest homogeneous term to a monomial-ideal condition, and the middle-coefficient matrix is invertible by a positive-definite or accretive Toeplitz integral according to parity. For even orders, a real polynomial constructed from the two node polynomials is a nonzero Hermitian kernel. A modular checker independently verifies many small orders but is not used as an infinite proof. Caveat: even-order ambiguity is proved for the linear Hermitian lift, not necessarily for pure-state phase retrieval.

## Originality
PASS subject to residual historical-priority risk. The closest inspected published literature concerns (i) existence of uniformly discrete sampling sets for infinite-dimensional STFT phase retrieval, (ii) Gabor frames and polyanalytic interpolation on cylinders, (iii) approximation for Gaussian shift-invariant signals on finite grids. These do not imply the universal odd-versus-even exact rank criterion for an \(m\)-by-\(m\) Cartesian grid on the truncated Hermitian polynomial space. Searches included the Cartesian-grid, bidegree-polynomial, coherent-state and tensor-interpolation formulations, along with published research-index comparisons. The full text of the motivating September 2026 paper was unavailable, and an unindexed equivalent polynomial-interpolation result remains possible.

## Value
PASS. At the information-theoretically minimal **linear Hermitian tomography** sample count \(m^2\), the entire family of square Cartesian grids has an exact parity obstruction that cannot be repaired by moving any nodes while retaining the grid structure. The odd-order result provides a universal sufficient design rule for finite Gaussian spectrogram tomography and the even-order construction gives explicit blind directions. This is a structural all-degree classification with a natural measurement interpretation, not a fixed numerical instance or routine coefficient substitution.

## Closest sources and limits
De Dios Pont et al., arXiv:2609.28341v1 (dated abstract; complete paper not available); Abreu--Luef--Ziyat, JFAA 31 (2025) article 68 (full HTML, sampling/interpolation and phase-retrieval scope inspected); Grohs--Liehr, Constructive Approximation 59 (2024), 61--111 (full HTML, Sections 3--4 and finite-grid approximation inspected); Grohs--Liehr--Rathmair, Rev. Mat. Iberoam. 41 (2025) (abstract only). None of the inspected claims supplies the displayed finite Hermitian rank criterion. No general lower bound on conditioning or even-order pure-signal nonuniqueness is claimed.

Self-review: passed. Independent audit: not yet performed.
