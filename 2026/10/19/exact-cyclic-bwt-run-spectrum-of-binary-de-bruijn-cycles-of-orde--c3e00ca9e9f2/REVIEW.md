# Scientific review: exact order-five de Bruijn BWT spectrum

## Correctness — PASS

Every length-five factor corresponds to a unique edge of the four-bit de Bruijn graph. A circular word using each edge once is exactly a closed Eulerian circuit. The unique `00000` edge supplies a canonical root, and the exhaustive search enumerates all and only the \(2048\) rooted circuits. For each, full cyclic-rotation sorting defines the exact BWT; the run counter is deterministic. An independent BWT-last-column search examines all \(65536\) concatenations of sixteen permutation blocks and accepts columns precisely when the LF map is one cycle. It independently produces the same exact histogram, and all \(2048\) BWT byte strings coincide between the methods. The supplied, bounded, standard-library verifier makes this a complete finite proof, not extrapolation.

## Originality — PASS against inspected evidence

Higgins (2012) establishes the permutation-block characterization; that known step is expressly not claimed as new. Mantaci et al. (2017), Theorem 5.2, give the general-order range that specializes to \(18\le r\le30\) at order five, but not the precise histogram nor the stronger minimum \(20\). Fici–Gabory (2025) characterize generalized de Bruijn words by the BWT and develop enumeration, without the inspected order-five run-refined table. Lipták–Parmigiani's (2024) accessible presentation concerns random generation, and the full conference chapter was not obtained; a previously published enumeration therefore remains a residual risk. Indexed research-record queries and accessible prior claims were compared by implication as well as topic; none found states this table. This is a bounded originality judgment, not a mathematical proof of worldwide priority.

## Mathematical value — PASS

The six-cell distribution is a natural complete classification of BWT run-compressibility among a standard family of exhaustive five-bit coverage cycles, rather than an arbitrary substring slice. The result gives the exact achievable minimum and its multiplicity (\(38\) optimal cycles), sharpens the existing lower bound, and identifies the entire tail distribution, with mean \(195/8\) and variance \(211/64\). It provides a reproducible small-order benchmark for BWT-sensitive choice of universal cycles and for validating larger-order construction algorithms. No general theorem beyond order five is asserted, and output-bit compression is not inferred solely from run counts.

## Limits and closest sources

The principal prior comparison is Higgins, DOI 10.1016/j.tcs.2012.07.019, for the exact BWT structural characterization, followed by Mantaci et al., DOI 10.1016/j.tcs.2017.07.015, for general run bounds. Relevant additional sources are Fici–Gabory, DOI 10.4230/LIPIcs.MFCS.2025.48, and Lipták–Parmigiani, DOI 10.1007/978-3-031-55598-5_9. This is a complete finite enumeration with an executable certificate, not an analytic all-order formula. Possible equivalent unpublished tables and the uninspected full 2024 chapter remain limitations.

Self-review: passed. Independent audit: not yet performed.
