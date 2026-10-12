# Scientific review: Small-hypercube geodesic packings and a sharp covering of \(Q_6\)

## Correctness — PASS

Every maximal \(Q_d\) geodesic has length \(d\), so elementary vertex-volume counts give upper bounds \(3,5,9\) and cover lower bound \(10\). For \(Q_4\), all \(192\) unoriented diameter paths are exhaustively generated in two independent representations; by bit-translation and coordinate symmetry, the canonical path has \(31\) disjoint partners, and every two such partners intersect, excluding three-path packings. A direct third check excludes all triples and counts \(2976\) disjoint pairs. Explicit sequences for \(Q_5\) and \(Q_6\) give five and nine disjoint maximal geodesics, respectively; the nine \(Q_6\) paths miss only vertex \(47\), and a tenth path through that vertex covers the entire cube. The supplied verify.py reconstructs all finite conditions and generated output VERIFY_OK. Exhaustive finite enumeration is valid for the finite Q4 statement; no infinite extrapolation is asserted.

## Originality — PASS

The 2022 source introduces the vertex-disjoint maximal-geodesic parameter and establishes only Cartesian-product volume bounds. The 2026 full-text preprint treats the dual diameter-geodesic covering objective but leaves \(Q_6\) between \(10\) and \(16\). The new exact Q4 obstruction, full Q4 packing polynomial, explicit sharp Q5/Q6 packings and ten-path Q6 covering are not implied by these results. Actual published-finding corpus searches for aliases, parameters, and dual covering found no equivalent statement; this negative search is not presented as proof of novelty. Some older routing/path-packing literature is inaccessible in full and remains a residual risk.

Closest inspected primary work: Manuel–Brešar–Klavžar (arXiv:2210.15325, full text, especially Lemma 2.3 and Corollary 2.8); Sharma–Guragain–Srivastava (DOI 10.13140/RG.2.2.13477.36320, full public text, Theorem 11); Anick–Ramras (arXiv:1308.4949, path edge decompositions); Goldwasser–Hansen (arXiv:2009.09037, perfect-path configuration density). The 2019 shortest-path-routing article was accessible as an abstract only, and older equivalent work remains possible. Full query- and implication-level originality comparisons are contained in `AUDIT.json`.

## Value — PASS

Hypercubes are canonical Cartesian powers, and the exact attainment of the geodesic-volume bound is a natural gap in the 2022 foundational packing result. The \(Q_4\) failure of sharpness alongside \(Q_5,Q_6\) attainment gives a genuinely structural boundary, while the exact \(Q_4\) packing enumerator and reproducible obstruction exceed a routine application of the bound. The \(Q_6\) ten-path cover closes the 2026 explicit published interval 10..16 in the first dimension beyond the small cases whose exact coverings the source considered. All results are self-contained, natural finite cases, not unsupported general asymptotic claims.

## Limitations and evidence

The numerical classification is restricted to \(Q_4\), \(Q_5\), \(Q_6\), with a verified finite exhaustive calculation at dimension four, explicit packing paths at dimensions five and six, and an explicit ten-path covering at dimension six. No independent audit or general-dimension theorem is claimed. `verify.py` is replayable using Python 3 and accompanies its actual output in `verification_output.txt`.

Self-review: passed. Independent audit: not yet performed.
