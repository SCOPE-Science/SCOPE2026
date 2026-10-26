# Scientific review

## Correctness — PASS
The precise comparison is between normalized cumulative integrals of adjacent Jacobi weight parameters at the same polynomial degree. Jacobi orthogonality fixes the factor \(2k+\beta+1\), and the classical differential and contiguous identities yield the stated exact derivative and its vanishing boundary value at zero. At roots of the original polynomial, the reduced boundary factor is negative; at its derivative roots and both endpoints it is positive. The degree of the factor is exactly \(2k\), proving a sharp root count, strict simplicity, and the required order changes for every allowed real parameter. A separate direct argument handles \(k=0\). The packaged script passed 191 finite checks, which are diagnostic rather than an infinite proof. No hidden numerical assumption is used.

## Originality — PASS, best knowledge
The relevant prior sources were compared by their mathematical implications. Greengard–Serkh (2018) develops the Zernike–Jacobi orthogonality and recurrence apparatus, but the inspected definitions, integrals and appendices do not give cumulative-square adjacent-weight crossing counts. Driver–Jordaan (2016) studies interlacing of raw Jacobi zeros, not zeros of a difference of normalized integrated squared modes. The previously known fixed-total-degree comparison \(E_{k,\beta}\ge E_{k-1,\beta+2}\) is a nonnegative squared expression with tangencies and does not imply the fixed-radial-degree shift \(\beta\mapsto\beta+1\), which has \(2k\) transverse crossings. Index searches for cumulative Jacobi energy, Zernike angular concentration, parameter shifts, and equivalent square-factor formulations produced no matching theorem. Residual risk: older unindexed connection or integrated-product identities could contain the same statement; independent priority confirmation remains necessary.

## Mathematical value — PASS
These disk/ball mode energies are canonical radial concentration invariants of the Zernike basis, including applications to orthogonal optical modes. The exact crossing number for every radial degree and continuous Jacobi parameter is a global qualitative classification, not a sample calculation. It gives sharp, explicit node/turning-point location brackets and distinguishes two natural index changes: changing angular order at fixed radial index causes complete alternating order reversals, whereas a fixed-total-degree change can cause only tangencies. No stronger spectral or general-aperture assertion is made.

## Limitations
The theorem addresses single-mode centered-aperture energies. It does not assert simultaneous diagonalization of all disk compressions, spectral ordering of arbitrary multi-mode subspaces, or an explicit closed-form formula for individual crossings. Bibliographic uniqueness has not been independently audited.

Self-review: passed. Independent audit: not yet performed.
