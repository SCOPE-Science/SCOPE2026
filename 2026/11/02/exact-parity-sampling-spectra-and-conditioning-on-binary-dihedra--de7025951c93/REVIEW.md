# Scientific review

## Correctness — PASS

The stated object is the union of two orthogonal regular \(2m\)-gons, with \(m\ge2\), and the Gram kernel is exactly \(U_\ell(\langle x,y\rangle)\). The Chebyshev exponential sum and the two block-circulant Fourier diagonalization give every eigenvalue with multiplicity, including zeros. Residue counts give ranks and all sharp cases of the nonzero spectral ratio. The matrix translation identity follows from a fourfold additional traversal of the allowed parity residues; it was also tested by constructing both Gram matrices directly. The checker runs with only the Python standard library and passed 8,460 exact spectral tests and 114 direct-block tests. The infinite results depend on the displayed analytical reductions, not those finite tests. No independent verification is asserted.

## Originality — PASS under bounded comparison

The closest inspected works are Lehoucq--Uzan--Weeks (arXiv:math/0202072v1, Sections 2 and 10), Rossmann (arXiv:math/0307121v1, Sections 1--3), and Weeks (arXiv:math/0502566v1, Section 13). They construct invariant quotient harmonics and classical ADE character data; those theorems do not provide the complete, all-sector finite-point sampling Gram spectrum or the exact interpolation and conditioning classifications. The orthogonal-double-polygon and dicyclic formulations were compared with the same published literature, not treated as different objects. A historical equivalent in frame theory or older prism spectral calculations remains a risk; bounded search is not a priority proof.

## Mathematical value — PASS

The family is a standard nonabelian finite subgroup realized as a highly symmetric point configuration in \(S^3\); exact-degree harmonic sampling must account for antipodal nullity, two distinct great circles, and discrete frequency aliasing. The theorem completely answers the natural finite interpolation and stability questions in every degree, displaying a nonmonotone even-degree tightness exception, a sharp full-rank transition, and the exact all-degree translation law. These distinguish the result from an isolated DFT calculation or a single small example.

## Limitations

Only the nonzero singular spectrum is conditioned; full \(4m\)-point interpolation is always impossible because of antipodal parity. The theorem is not about quotient Laplacian eigenmodes. Existing invariant-harmonic constructions are credited, and independence of the scientific review is not claimed.

Self-review: passed. Independent audit: not yet performed.
