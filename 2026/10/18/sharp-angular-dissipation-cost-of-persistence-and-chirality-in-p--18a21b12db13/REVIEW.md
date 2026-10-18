# Scientific review: sharp angular dissipation cost of persistence and chirality

## Correctness — PASS

The stationary convolution jump generator has Haar-invariant orientation law and reverses every turning increment under time reversal. Its angular jump-path entropy-production rate is therefore the Poisson event rate times the relative entropy between the turning law and its reflection. The symmetrized-law argument in `RESULT.md` is constructive, covers finite and infinite path relative entropy, and justifies the bound with Cauchy–Schwarz, a cosine-variance bound, and Jensen for the explicitly strictly convex function \(g(t)=2\sqrt t\operatorname{artanh}\sqrt t\). The atomic two-angle law attains the bound, and equality in cosine variance proves uniqueness when chirality is nonzero. A separate narrow-bump construction proves the same sharp infimum over smooth densities while preserving both moments. Unit-circle and zero-chirality endpoints are addressed separately. The 318 independently generated checks in `verify.py` pass; they support but do not replace the proof.

## Originality — PASS, with explicit literature risk

The closest model paper is Britton, Zhang, Han and Bertrand (arXiv:2608.23519v1), which gives the arbitrary turning kernel and its first-mode chirality and persistence. Inspection of its model, observables, discussion and keyword-searchable full text identifies no angular path-relative-entropy optimization or equality classification. Olsen and Löwen (arXiv:2405.14326) optimize diffusion instead of angular jump irreversibility. Shreshtha and Harris (arXiv:1903.01972) bound current precision in a one-dimensional run-and-tumble renewal model using an entropy quantity, not this exact joint first-harmonic cost. The earlier harmonic-trap entropy-production treatment of Garcia-Millan and Pruessner (2021) addresses a different spatial and orientational model. Available broad entropy-production frameworks and convex-divergence bounds may admit an implicit specialization giving this tradeoff; the risk is genuine and is not removed by a negative search. The assessed novelty is the explicitly sharp two-parameter physical bound, optimizer and smooth-density infimum, not the known entropy-production definition or the generic Jensen and Cauchy–Schwarz inequalities.

## Value — PASS

The first turning harmonic is experimentally accessible through long-time orientational relaxation and angular drift, but it does not determine the microscopic turning law or its irreversibility. The theorem solves the natural constrained design/inference problem: the lowest possible orientation-jump entropy-production rate compatible with those two observables, including a unique minimizing asymmetric turning strategy, a weak-chirality scaling law and a divergent cost at the ballistic turning boundary. The result works for all Borel turning laws, not an arbitrary selected family or a numerical slice. No new theorem on total heat or spatial entropy production is claimed.

## Scope and closest sources

Sources: Britton et al. (2026), arXiv:2608.23519; Olsen and Löwen (2024), arXiv:2405.14326; Shreshtha and Harris (2019), arXiv:1903.01972; Garcia-Millan and Pruessner (2021), DOI:10.1088/1742-5468/ac014d; Pruessner and Garcia-Millan (2025), DOI:10.1088/1361-6633/adff30. The theorem measures stationary orientation-jump relative entropy only. Its two-atom equality law may fail ergodicity for certain rational angles, but Haar remains stationary and the stationary path cost remains well-defined. All scientific coverage conclusions are subject to the residual implicit-specialization risk stated above.

Self-review: passed. Independent audit: not yet performed.
