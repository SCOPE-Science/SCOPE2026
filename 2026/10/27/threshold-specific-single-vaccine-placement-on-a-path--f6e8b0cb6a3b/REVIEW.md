# Scientific assessment

## Correctness — PASS

The final claim is limited to one perfect vaccination on a finite path with a uniformly selected post-vaccination source and independent one-step edge transmission. Open-bond components coincide with Reed–Frost final infections. Enumerating short open components yields the exact affine source-weighted tail formula. The piecewise minimizers follow from the strict comparison \((s-1)p^s>0\); a strictly increasing discrete derivative of the pair-connectivity sum yields the mean-optimal center. For every path of at least five vertices, the two-infection and larger-outbreak tails strictly reverse the favored location. `VERIFY.py` passed 529 rational assertions and is supplemental, not an infinite proof.

## Originality — PASS, qualified

Holme's arXiv:1708.06456 calculates expectation-based node importance for continuous-time SIR on graphs through seven vertices. Chatterjee–Zehmakan's arXiv:2305.16458 studies vaccination heuristics and a degree-normalized epidemic rule. Clusella et al.'s arXiv:1604.00073 evaluates large-cluster and aggregate component-size surrogates. The inspected accessible texts do not state or imply the exact all-threshold Reed–Frost path optimizer family. Semantic searches of published mathematical abstracts and comparisons with accessible prior claims showed no directly dominating result. The full open-access journal text of Yuan et al. (PLOS ONE, 2015; DOI 10.1371/journal.pone.0115826) was inspected: its methods and results optimize mean epidemic size across two continuously mixing, mutually isolated populations, not percolation outbreak tails for a single vaccination on a path. Publication priority nonetheless remains provisional.

## Value — PASS

Final outbreak **mean**, probability of even one secondary transmission, and larger-outbreak probability are mathematically and operationally distinct criteria. A complete solution of a natural canonical contact network gives a sharp, five-vertex first conflict and shows why a uniform vaccine-site ranking cannot minimize all final-size tails. This supplies both an exact finite-population benchmark for network epidemic algorithms and a natural counterexample to inferring risk-optimality from an average-based objective.

## Limits and relationship to literature

The proof does not handle arbitrary contact graphs, temporally correlated transmission, random infectious durations, imperfect protection, or nonuniform source distributions. Continuous-time SIR, Reed–Frost and degree-normalized discrete network infection are distinct mechanisms. The checked literature does not establish global publication priority; unindexed or otherwise unavailable related work remains a risk.

Self-review: passed. Independent audit: not yet performed.
