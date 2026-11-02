# Scientific review: a unique corridor-investment reversal in a four-patch landscape

## Correctness — PASS

For arbitrary strictly positive baseline weights, corridor efficiencies and effort, direct symbolic determinant expansion gives the stated quartics and their linear-in-eigenvalue difference. The critical sign inference is justified by Cauchy interlacing, not an unjustified comparison of characteristic-polynomial values: deleting node 3 from corridor A gives largest principal eigenvalue \(a\), hence \(\lambda_2(M_A)\leq a<\Lambda_B\). The remaining three characteristic factors evaluated at \(\Lambda_B\) are strictly positive. Perron monotonicity makes \(t\Lambda_B(t)\) strictly increasing from zero to infinity. This proves an exact all-parameter sign law, existence/uniqueness, the tie cases and both ordering directions. The accompanying `verify.py` passed 2,577 symbolic, exact-rational and numeric checks. Computation is corroboration, not the proof.

Risk: the ecological interpretation is deliberately only a symmetric landscape-eigenvalue capacity proxy, not a theorem about general stochastic persistence or asymmetric dispersal.

## Originality — PASS under the inspected literature; historical priority provisional

Hanski–Ovaskainen (2000, https://doi.org/10.1038/35008063) introduced metapopulation capacity and is foundational rather than an exact two-corridor ranking law. The accessible abstract was checked, but its full text was unavailable. Ovaskainen–Hanski (2001, https://doi.org/10.1006/tpbi.2001.1548) generalize capacity to patch networks; only publicly available abstract/metadata were inspected. Tambosi and coauthors (https://doi.org/10.1111/rec.12049) study a different restoration prioritization metric; the abstract and article metadata were available, but full technical contents were not. Milanese–Sun–Nishikawa, arXiv:1001.1431, was inspected in full (nine pages): its contribution is perturbative approximation of spectral impacts and empirical link ranking, not an exact all-effort four-vertex crossing classification. Noschese–Reichel (2025, https://doi.org/10.1002/nla.70041) was inspected through full open-access article, including its sensitivity propositions, examples and conclusions; its edge-removal sensitivity estimates do not imply the stated finite-weight uniqueness theorem. Comparisons of related research records and recoverable earlier claims found no statement that directly covers this exact alternative-edge problem.

Risk: general graph-spectral literature and inaccessible early ecological/restoration articles could independently imply this special formula. Search results are evidence of scope, never a uniqueness or priority certificate. Independent historical verification remains unperformed.

## Value — PASS

Connectivity interventions have finite, not merely infinitesimal, budgets, and managers can face two mutually exclusive corridor constructions. The classification gives a simple, sharp condition for a restoration ranking to reverse exactly once, showing when a small-budget recommendation is not appropriate for a large budget; it also rules out oscillating rankings within the defined model. The four-patch path is the smallest simple chain with *two distinct* non-existing distance-two edges, so this is a natural minimal competing-corridor geometry rather than an arbitrary parameter cut. The exact critical effort and inadmissible second algebraic root are practically interpretable. No claim is made about empirical management efficacy beyond the assumed spectral proxy.

Self-review: passed. Independent audit: not yet performed.
