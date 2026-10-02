# Independent audit — 2026-10-01

## Record

**Flat s-number and strict-singularity profiles of relative Toeplitz Schur multipliers**

Final claim: Every bounded relative Toeplitz Schur multiplier on the indicated Banach Schatten space over an infinite discrete group has \(a_n=c_n=d_n=b_n=\|T\|\) for every \(n\), Hausdorff measure of noncompactness and essential norm equal to \(\|T\|\), and norm distance \(\|T\|\) from the compact, finitely strictly singular, and strictly singular classes.

Disposition: **PASSED**

## Correctness — PASS

A finite near-norm block can be translated simultaneously on rows and columns into infinitely many disjoint copies while preserving both the relative pattern and the symbol. Singular values concatenate, giving an exact \(\ell_p\) or \(c_0\) subspace on which \(T\) is a scalar multiple of an isometry. This directly yields the Bernstein and strict-singularity distances; finite-codimension intersection gives Gelfand numbers, finite-rank comparison gives approximation numbers, and escaping rectangular compressions give Kolmogorov numbers and Hausdorff noncompactness. The argument also works at \(p=\infty\) because the ambient ideal is compact operators.

## Originality — PASS

Neuwirth–Ricard provide the relative Toeplitz–Schur framework and norm transference, Hladnik characterizes compact Schur multipliers on \(B(H)\), and Oikhberg studies s-numbers for elementary/restricted Schur multipliers. None of the inspected statements implies the simultaneous flat four-s-number profile or distance to the strictly singular class for this translation-invariant Schatten-space family. Hladnik's full article could not be lawfully retrieved after open-access and institutional attempts, so hidden equivalent coverage there remains an explicit risk.

Equivalent-formulation, broader-coverage, exact-database/table, and claim-versus-prior implication checks are recorded in the companion JSON audit. Source inspections distinguish material actually read from inaccessible full text.

## Scientific value — PASS

The theorem identifies a class-wide rigidity phenomenon at every finite-dimensional approximation scale, not merely noncompactness: every nonzero relative Toeplitz Schur multiplier is maximally noncompact and norm-separated from several major operator ideals. This is a natural structural fact for a standard transference class.

## Checked scientific sources

- S. Neuwirth and É. Ricard, Transfer of Fourier multipliers into Schur multipliers and sumsets in a discrete group, arXiv:1001.5332; Can. J. Math. 63 (2011).
- M. Hladnik, Compact Schur multipliers, Proc. Amer. Math. Soc. 128 (2000), DOI:10.1090/S0002-9939-00-05708-7.
- T. Oikhberg, Restricted Schur multipliers and their applications, Proc. Amer. Math. Soc. 138 (2010), DOI:10.1090/S0002-9939-10-10203-2.
- Resultary semantic search for Toeplitz Schur multipliers, classical s-numbers, strict singularity, and maximal noncompactness.

## Residual risks

- The full Hladnik 2000 article was unavailable through the lawful open-access routes inspected; an authorized institutional retrieval also returned no verified PDF. An equivalent consequence hidden in that article or older Schur-multiplier ideal literature remains possible.

## Verification boundary

The audit reconstructed the mathematical argument from the record and performed fresh logical or algebraic checks where needed. Existing package logs were treated only as reproducibility evidence. No formal proof-assistant verification or expert attestation is asserted.
