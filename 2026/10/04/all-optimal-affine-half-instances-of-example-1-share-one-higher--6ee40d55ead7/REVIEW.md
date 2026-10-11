# Independent mathematical audit

## correctness

PASS

I inspected the assigned certificate and verifier and independently replayed the full finite classification. The construction uses \(\mathbb F_8=\mathbb F_2[z]/(z^3+z+1)\), all nine Desarguesian spread components, all 36 unordered component pairs, and all 49 nonzero normals outside each dual-spread union. For every instance the exact \(7\times95\) binary generator was formed and every message subspace was enumerated in reduced row-echelon form: 127, 2667, 11811, 11811, 2667, 127, and 1 subspaces in dimensions 1 through 7, or 29,211 per code. The full 1,764-instance replay therefore checked 51,528,204 subcode supports. Every instance matched the packaged complete spectra and hierarchy \((22,56,74,84,90,93,95)\). The dimension-one spectrum exactly reproduces the source Example 1 weight enumerator, providing an external anchor on the code construction.

## originality

PASS

The 2026 primary article was read in full at the construction, Example 1, and weight-distribution/optimization sections. It proves the ordinary weight enumerator and the outside-normal optimum \([95,7,22]_2\), but does not give generalized Hamming weights or higher-dimensional subcode-support spectra. Exact hierarchy and parameter searches in Resultary found no prior match. Generalized-Hamming-weight literature for related partial-spread codes concerns different code constructions and does not determine the support unions after this affine-half coordinate duplication.

## value

PASS

Generalized Hamming weights and full subcode-support spectra are natural invariants of a linear code and matter beyond ordinary weight distributions. The result classifies those invariants for every optimal-normal instance of a concrete current construction and discovers a nontrivial isospectrality across 1,764 codes. The exact fact is not implied by the published ordinary enumerator and is plausibly useful for later equivalence, wiretap, and support-geometry analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
