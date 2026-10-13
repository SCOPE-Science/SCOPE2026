# Scientific review

## Correctness — PASS
For every \(n\ge2\), a prescribed set of \(s\) good edges decomposes the permutation into \(n-s\) positional blocks. The combinatorial factor \(2^{r(S)}(n-s)!\) follows from independently orienting nontrivial consecutive-value intervals and permuting the value-interval allocations. Boolean-lattice inversion exactly enforces the absence of adjacent bad edges. A three-state transfer construction independently derives the rational generating function and the recurrence. A direct permutation search, a used-symbol dynamic program, a separately coded transfer automaton, and a literal Möbius sum agree in their documented finite ranges. There is a complete all-length proof, not an extrapolation from finite evidence.

## Originality — PASS, subject to bibliographic limitations
The closest source is Buzaglo and Yaakobi's 2016 18-page paper, Section III, Definition 2, Construction 11, Theorems 13 and 15, and Lemma 14. It proves capacity \(C(1)=1/2\), a large constructed subset, and upper bounds, not exact finite-length enumeration. The 2014 preprint was also read. Classical succession-number work concerns the number of rising consecutive-value pairs, while the current statement depends on their position pattern and both signs. The full Reilly–Tanny 1979 article could not be inspected, leaving a real risk that a sufficiently multivariate theorem subsumes the recurrence; neither title matching nor search absence was used as proof of novelty. Overlap was checked against related published database hits and available prior claims.

## Value — PASS
The tolerance-one case is the smallest meaningful rank-neighbor constraint in the physical rank-modulation model introduced in the primary literature. Capacity alone is asymptotic and does not give exact alphabet sizes at usable finite block lengths. The result determines all \(n\) exactly, provides an explicit finite-state structural decomposition and an \(O(n^2)\)-arithmetic recurrence, and thereby quantifies the design space available for short-block constrained permutation coding. This is a complete natural invariant rather than a small arbitrary numerical improvement.

## Limitations and closest literature
The result does not solve optimal error-correcting codes, higher tolerance, asymmetric constraints, or efficient rank/unrank encoding. Closest complete material: Buzaglo and Yaakobi (2014; 2016), https://arxiv.org/abs/1401.4484 and DOI:10.1109/TIT.2016.2519400. Historical possible overlap: Reilly and Tanny (1979), DOI:10.1002/sapm197961173, abstract only. Scientific review is limited to the present mathematical proof and reproducible checks.

Self-review: passed. Independent audit: not yet performed.
