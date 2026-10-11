# Scientific review: two-statistic symmetric-group Fourier sampling law

## Correctness

**PASS.** The normalization is fixed by counting-measure Schur orthogonality: the standard Fourier block is isometric to the Hilbert--Schmidt space after the factor \(\sqrt{(n-1)/n!}\). The conjugation action on its endomorphism space has four inequivalent sectors, so a full conjugacy-class orbit frame is scalar on each. The sector energies are obtained independently from the standard character, the skew-symmetric part, and the centered fixed-point indicator, with the fourth energy from the Hilbert--Schmidt norm. The boundary calculation proves exactly when all energies are positive; no genericity assumption is hidden. The packaged exact-arithmetic checker confirms all conjugacy classes for \(4\le n\le7\), but the proof, not enumeration, establishes the universal result.

## Originality

**PASS, with explicit historical risk.** Scarabotti--Tolli (arXiv:math/0701533v1, Section 3.2) contains a related ordered-pair representation decomposition; Thill--Hassibi (arXiv:1509.05739v1) provides general Fourier group-frame inner products; Beck--Ghandehari (arXiv:2203.03036v1, Theorem III.6) supplies Fourier-compatible frame constructions. Their inspected mathematical statements do not give the class-density-normalized spectrum for every conjugacy class or the necessary-and-sufficient injectivity criterion. Literature and publicly indexed mathematical-record searches for conjugacy-class sampling and permutation-matrix spans did not identify a dominating theorem. Prior results for the complete transposition class and three-cycle class are special instances; the present all-class statement covers additional cycle types and is not implied by those isolated instances. The sector-decomposition literature could conceivably contain a differently phrased equivalent orbit-norm computation, and the search is not a proof of historical novelty.

## Mathematical value

**PASS.** Conjugacy classes are canonical permutation-invariant sampling sets in nonabelian Fourier analysis. The result gives all squared singular values and an exact full-rank criterion simultaneously for every class and every \(n\ge4\). It shows that only the counts of cycles of lengths one and two influence the class-density-normalized spectral levels, while long-cycle structure affects only density. In particular it settles previously unaddressed long-cycle and mixed-cycle designs and identifies the precise sampling obstruction for every class. This structural compression and complete natural classification go beyond checking a particular parameter or routine special case.

## Closest literature, assumptions, and remaining risks

The statement concerns the standard Fourier block only, full conjugacy classes only, and counting-measure normalization. The relevant comparison is to **spatial restriction**, not to convolution by a central class sum: the latter generally has very different eigenspaces and need not imply this spectrum. A broad orbit-frame theorem is useful machinery, but its existence does not itself provide the four explicit energies without the projection computation. Full historical priority is not certified; analogous class-orbit frames or permutation-matrix span results may encode an equivalent formula. Finite computer verification remains corroborative and not exhaustive across degrees.

Same-model review: passed. Independent audit: not yet performed.
