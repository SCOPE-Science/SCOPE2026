# Self-review

## Correctness — PASS

The claim fixes every quantifier: integer order \(n\ge3\), one forbidden length-\(n\) binary word with exactly one marker, cyclic contiguous factors with multiplicity, avoidance of the forbidden edge, and allowance of repeated permitted factors. Deleting the edge creates exactly two unit degree defects; every admissible circular host is a balanced augmentation and therefore must contain a return path from the surplus-inflow prefix to the surplus-outflow suffix. An explicit two-one overlap argument rules out all paths shorter than \(n\) off the centered odd case; the centered shorter path and the off-center length-\(n\) path are each explicitly verified as forbidden-free and unique. The endpoint vertex obstruction is absolute. These imply the length formula and the unique optimum factor-multiplicity vector. The independent implementation replays graph distances, witnesses, exact cyclic factor counts and small exhaustive lower-bound checks.

## Originality — PASS, qualified

Chen–Kitaev–Sun (2019; arXiv:1908.01116) address *exact-once* universal cycles after deleting a factor: a one-word deletion generally makes such a cycle impossible. The present claim allows repeated permitted factors and determines precisely how many and which are forced. Bernardini et al. (2022; DOI 10.4230/LIPIcs.CPM.2022.12) provide general Eulerian-extension principles and recognize edge duplication, but not the centered parity formula or unique factor repetition profile. Alhakim (2022; DOI 10.1007/s10623-022-01077-5) gives restricted-factor greedy generation under no-repeat construction conditions, not the same constrained shortest repeat problem. Moreno–Matamala (2007; arXiv:0711.1695) treat allowed-language de Bruijn cycles and lexicographic generation. Generic directed postman methods can compute individual cases, so the specific formula is the substantive claimed specialization. An equivalent unlocated formulation is possible, especially under directed postman or graph-flow terminology; the conclusion is provisional pending independent literature and proof review.

## Value — PASS

The class is a minimal structured perturbation of a binary de Bruijn factor library: remove one sparse motif and insist on avoiding it while still observing every other motif. The exact formula reveals an otherwise hidden central odd-order saving of roughly half the order and proves that two endpoint motifs make complete avoidance-and-coverage impossible. The mandatory repeated factors, not just an optimum length, are uniquely determined. Such all-order structural information is relevant to constrained cyclic sequence design and test-panel construction. It is more than a routine restatement of Eulerian existence or a narrow finite census.

## Sources and limitations

Primary inspected text: Chen–Kitaev–Sun arXiv:1908.01116, full article; Bernardini et al. CPM 2022 PDF, introduction and algorithms including forbidden-edge balancing; Alhakim 2022 repository full PDF, abstract, introduction, constructions and sequence-generation conditions; Moreno–Matamala arXiv:0711.1695 article. Important residual risk: a previously published special-case min-cost Eulerization formula for one-hot deleted de Bruijn edges might already imply this theorem. This review is not independent scientific validation.

Self-review: passed. Independent audit: not yet performed.
