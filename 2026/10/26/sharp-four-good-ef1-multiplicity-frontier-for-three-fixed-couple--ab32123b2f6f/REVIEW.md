# Scientific review

## Correctness — PASS

For a \((2,1,1)\) bundle-size pattern, EF1 for nonnegative additive values reduces exactly to requiring each member of a singleton group to rank her singleton no lower than at least one good of the paired group. This establishes an ordinal reduction. Simultaneous good relabeling fixes the first agent's strict ranking, leaving exactly \(24^5\) normalized profiles, and every profile has exactly \(36\) labeled balanced candidate allocations. The included exact-integer C++ certificate covers all these cases, with no sampling; it reports minimum two and the complete histogram. A second, independently written direct-value Python checker confirms that the sharpness witness has exactly two balanced EF1 allocations and that the previously published five-good instance has none. Arbitrary ties preserve the existence guarantee via refinement of weak orders. The analytic expected-count identity \(64/9\) independently checks the histogram's first moment. This is a proof of the finite theorem through an exhaustive, mathematically complete ordinal reduction, not an extrapolation from experimental data.

## Originality — PASS (subject to publication priority)

The closest primary manuscript is Gölz and Yaghoubizade, arXiv:2508.13432v1 (2025), whose Theorem 3.3 gives a five-good nonexistence instance. Its relevant Section 3 and appendix were inspected; they do not give the exact four-good existence threshold, the sharp universal multiplicity two, or the full strict-profile distribution. The 2020 Kyropoulou–Suksompong–Voudouris fixed-group results concern two groups, while their arbitrary-group extension allows variable membership. The Bu–Li–Liu–Song–Tao double-fairness model does not imply this three-fixed-couple result. The October 2026 Deligkas–Eiben–Ganian–Goldsmith–Gründel–Wietheger complexity paper treats arbitrarily many goods and does not provide the four-good census. Targeted literature and mathematical-results-index queries identified no equivalent or stronger theorem for the same fixed-group setting. Search failure alone is not proof of novelty; the checked source implications and the remaining priority risk are recorded in AUDIT.json.

## Value — PASS

A five-good construction already disproves universal EF1 existence for three couples. Determining the adjacent four-good boundary answers the natural minimal-obstruction question rather than an arbitrary isolated numerical curiosity. The sharp two-allocation guarantee strengthens mere existence, and the full ordinal frequency law quantifies how rarely exactly two feasible outcomes remain, with limiting multiplicities impossible to infer from the five-good obstruction or group-size results. The self-contained certificate makes this exact finite classification reproducible. It makes no unsupported claim about larger item counts or new strategyproofness or efficiency axioms.

## Closest literature and residual limitations

The five-good negative example is correctly attributed to Gölz and Yaghoubizade. The classification depends on four goods and the \((2,1,1)\) pattern, and ordinal frequencies require strict independent uniform orders. External work not located by the recorded searches could establish the same claim; no independent scholarly review has been conducted.

Self-review: passed. Independent audit: not yet performed.
