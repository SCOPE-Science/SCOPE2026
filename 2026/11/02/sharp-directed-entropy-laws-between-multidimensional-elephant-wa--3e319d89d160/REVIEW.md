# Mathematical review

## Correctness — PASS

The full-history likelihood factors using the exact conditional law \(q_{\theta,k}(j)=1/D+\theta\Delta_k(j)/k\). The KL chain rule, uniform third-order Taylor bound on the frequency simplex, exact second-moment recurrence and its gamma/harmonic solutions, and Azuma--Hoeffding third-moment control together prove all three sharp rates with the stated constants and errors. The directional ratio follows by division and strict parameter ordering. The exact-rational finite checker independently compares path enumeration with chain KL and checks the second-moment recursion; 8,482 deterministic assertions passed. The finite tests supplement, but are not relied upon for, the infinite conclusions.

## Originality — PASS (provisional)

The most relevant recent primary text is Qin (2026), arXiv:2609.17264v1, Section 4.1: it uses full-history relative entropy with the independent uniform walk and bounds growth orders, but its inspected result does not supply exact pairwise fixed-memory constants or the complete directional ratio. Bercu and Laulin (2021), arXiv:2112.10405, Sections 2--3, derive one-dimensional path likelihood and local Fisher-information/LAN/LAMN results; those fixed-dimensional *local parameter* statements do not assert the global, fixed-separated multidirectional two-parameter theorem. The elementary conditional law, moments and likelihood calculus are explicitly credited. Search comparisons with published mathematical records did not uncover direct coverage. A general likelihood/urn entropy theorem could conceivably imply the result, and global historical uniqueness is not established.

## Mathematical value — PASS

Qin's entropy comparison leaves the sharp size of full-history information loss unspecified. This theorem supplies exact constants across all memory regimes for any pair of distinct parameters, and proves a complete, source-memory-dependent directional asymmetry classification. In particular, finite asymmetry becomes unbounded precisely when the higher reinforcement crosses criticality. The result connects the three stochastic fluctuation regimes to a directly interpretable information geometry of fully observed histories, without introducing an artificial restricted statistic.

## Sources and limitations

- S. Qin, *Cover times and ranges of elephant random walks*, arXiv:2609.17264v1 (2026), especially the conditional entropy comparison in Section 4.1.
- B. Bercu and L. Laulin, *How to estimate the memory of the Elephant Random Walk*, arXiv:2112.10405 (2021), Sections 2--3 and their likelihood/fisher-information statements.
- G. M. Schütz and S. Trimper, *Elephants can always remember*, Physical Review E 70, 045101 (2004).
- Y. Peres and S. Qin, *Transition probabilities of step-reinforced random walks*, arXiv:2604.07227 (2026), related distributional background.

The theorem treats fixed \(d\ge2\), strictly interior parameters and complete ordered increment histories. There is no claim about parameter sequences approaching each other, higher-order corrections, endpoint probabilities, or independent priority certification.

Self-review: passed. Independent audit: not yet performed.
