# Self-review

**Correctness — PASS.** The single final claim is the exact second-largest convex-hull area for every connected array of \(n\ge3\) unit-area regular hexagons. Gaur's published area identity and two spanning-tree bounds were read in full and their applicable hypotheses checked. The new integer-defect argument proves the forbidden top-minus-one lattice area for \(n\equiv2\pmod3\). All three congruence classes have exact attainable witnesses with analytical integer-coordinate formulas. Separate corner-hull calculations, finite exhaustive enumeration, and tree-count checks passed; finite checks are not treated as an infinite proof.

**Originality — PASS, residual priority risk.** Gaur, *The maximum area of the convex hull of a polyhex* (arXiv:2609.30310v1), proves the maximum and explicitly asks about stability and the area spectrum, but does not determine the runner-up. Kurz, *Convex hulls of polyominoes* (arXiv:math/0702786v1), gives area spectra for square cells, not regular hexagons. OEIS A399934 reports maximal areas, not the first submaximal level. Targeted mathematical findings and bibliographic searches did not reveal the present all-order exact gap. The 2015 Steffanová thesis was located by repository metadata, not inspected in full, so specialized historical overlap remains possible.

**Value — PASS.** This resolves the first natural quantitative stability question in a recently solved convex-hull extremal problem: how far below the optimum must a nonextremal arrangement fall? The sharp answer changes at \(n\equiv2\pmod3\), and explicit near-maximal families realize the gaps. Neither the full area spectrum nor near-maximizer shape classification is claimed.

**Reproducibility and scope.** See RESULT.md for the complete universal proof and verify_polyhex_runnerup.py for finite independent exact-integer checks. Hypotheses are precise; no external proof certification or independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
