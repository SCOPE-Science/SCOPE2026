# Scientific review: exchangeable versus classical diagonal estimation

## Correctness — PASS

The claim is precise for real symmetric positive-definite inputs, two independent Rademacher probes in the conceptual leave-one-out XDiag estimator, four independent probes in the BKS comparator, exact arithmetic and squared Euclidean risk. The proof derives both risks from the full sign distribution. The exact rational risk uses a strictly positive denominator \(D_+D_-\). A derivative argument proves the threshold has exactly one interior root for unequal diagonals, with the equal-diagonal boundary analyzed separately. The dimension-lifting statements follow from a positive-probability event and uniform continuity across the finite Rademacher support, respectively. Standalone exact-arithmetic checks reproduced the formulas and representative risk reversals (1208 assertion families). Finite tests support but do not replace the general proof.

## Originality — PASS, with priority uncertainty

Epperly, Tropp, and Webber (arXiv:2301.07825, Section 2.4) define XDiag and present broad empirical comparisons. Epperly's subsequent 2025 dissertation (Chapter 16, especially Sections 16.2–16.4) derives the estimator again and observes empirically that BKS can outperform XDiag on flat spectra. Hallman–Ipsen–Saibaba (arXiv:2202.02887) and Baston–Nakatsukasa (arXiv:2201.10684) analyze the conventional stochastic diagonal estimator, not the present exact cross-method risk. The existing XDiag definition, the BKS estimator, and qualitative spectral-regime tradeoffs are known; none of the inspected relevant source sections gave the exact formula, cubic one-crossing phase diagram, or opposite unbounded SPD risk separations established here. Specialized unpublished or unlocated equivalent calculations remain possible; unsuccessful discovery is not proof of uniqueness.

## Mathematical value — PASS

The estimator comparison concerns the natural squared Euclidean error at equal matrix-vector cost. It supplies an exact risk criterion instead of only qualitative guidance, distinguishes spectral anisotropy from off-diagonal strength, and identifies nonuniform nearly rank-one behavior under Rademacher sketches. Arbitrarily high-dimensional positive-definite embeddings show that the rank-two calculation reveals a genuine no-dominance phenomenon rather than just a limited-size computing curiosity. This does not claim superior implementations, new complexity bounds, or an arbitrary-dimensional closed risk formula.

## Sources and limitations

Primary source readings: the full HTML presentation of *XTrace: Making the Most of Every Sample in Stochastic Trace Estimation* (especially Sections 1.2.1, 1.2.3, 2.4, 3.1, 4.4 and relevant appendix); Epperly's complete 2025 dissertation at Chapters 16.1–16.4 and its numerical plots; the relevant introductory and estimator-analysis sections of Hallman–Ipsen–Saibaba and Baston–Nakatsukasa. An additional 2025 technical exposition of XDiag and Hutch++ describes the general construction but not the precise classification. Remaining risks: incomplete coverage of other specialist literature and numerical edge cases in implementations using inverse QR factors on rank-deficient sketches. Independent replication beyond the included exact-arithmetic checker has not been carried out.

Self-review: passed. Independent audit: not yet performed.
