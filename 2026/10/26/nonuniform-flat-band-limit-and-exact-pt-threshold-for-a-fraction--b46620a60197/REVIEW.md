# Review

## Correctness

**PASS.** The Bessel generating identity converts the positive kernel sum to the exact fractional symbol \(-q(k)^s\). The Bloch determinant then gives \(\lambda^2=V^2(4-q^s)^2-\gamma^2\). Since \(q\) ranges over the whole interval \([0,8]\), the minimum of \(4-q^s\) is \(4-8^s\) for \(s<2/3\); for \(s\ge2/3\), a wavevector with \(q^s=4\) gives a nonreal eigenvalue whenever \(\gamma>0\). The limit comparison follows from \(q^s\to1\) for each fixed \(q>0\) and \(0^s=0\) for all \(s>0\). The checker tests representative values only; the proof is analytic.

## Originality

**PASS.** The main contribution is not the source's already-published dispersion relation. It is the exact all-wavevector reality boundary and, especially, the correction of the stated infinite-volume zero-order band-edge interpretation. The primary square-lattice paper gives the kernel and dispersion but reports a different small-exponent band-edge limit. A related one-dimensional paper discusses noncommuting finite and infinite kernel sums but has a different operator and does not imply the two-dimensional formula. Semantic literature/database searches returned related lattice-threshold and square-lattice spectral findings, but no statement matching this operator, exact boundary, and limiting correction.

Closest literature: Molina, arXiv:2211.02796v1 / DOI 10.1103/PhysRevA.106.L040202; Molina, arXiv:2307.00375v1 / DOI 10.1103/PhysRevA.108.013515. Residual risk: the correction is an elementary consequence of the published Fourier dispersion once the infinite kernel sum is evaluated exactly, so the contribution is a focused correction rather than a broad new theory.

## Value

**PASS.** The result replaces a numerical wavevector-averaged boundary by an exact phase boundary and resolves an order-of-limits ambiguity that changes the predicted stable region as \(s\downarrow0\). In particular, gain/loss values between \(3V\) and \(4V\) cannot remain in the infinite-lattice real-spectrum phase for all sufficiently small positive \(s\), contrary to what the incorrect \(4V\)-based limiting gap would suggest. This matters for classifying stability, not just for re-expressing a known formula.

Self-review: passed. Independent audit: not yet performed.
