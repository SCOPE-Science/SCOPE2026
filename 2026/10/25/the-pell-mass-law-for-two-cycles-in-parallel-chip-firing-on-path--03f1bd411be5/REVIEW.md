# Scientific review: Pell mass law for path chip-firing

## Correctness — PASS
The exact domain is ordinary parallel firing on labelled paths with nonnegative chip holdings. A two-step return forces a common total firing count in \(\{0,1,2\}\) at every vertex by the kernel of the connected Laplacian. The two constant cases produce fixed states; in the primitive case complementary firings and explicit local chip intervals give a bijection, up to time phase, with cut-edge indicators and offset vectors. The weighted path transfer matrix gives both the recurrence and explicit generating function. The Pell enumeration and mass palindrome follow algebraically; the Gaussian law follows from the analytic dominant root. Direct state simulation, a cut-and-offset enumerator, a recurrence solver and a binomial formula agree on all \(n\le10\), with extended non-simulation checks to \(n\le40\). The infinite assertions rest on proof, not simulation.

## Originality — PASS, with explicit boundaries
Jiang (2010) and Scully–Zhang–Jiang (2011, Section 4) already establish the periodic-firing principle, general two-cycle inequalities and period from chip mass on trees; this finding does not claim those as new. A full reading of the relevant preprint Section 4 showed no exact primitive-orbit count by chip total; the new result supplies that quantitative invariant with Pell and Gaussian laws. Firing-pattern work (2012 preprint) does not tabulate the path orbit count. The 2006 fixed-energy sandpile calculation uses a periodic **ring**, with a distinct periodic-orbit block enumerator; it does not give the open-path mass polynomial with degree-one endpoints. The 2020 parallel-diffusion path enumeration concerns a different local transfer rule. Searches included exact chip-firing, fixed-energy-sandpile, Pell and two-cycle orbit-count terminology, plus semantic comparisons to available research findings. The 1992 tree paper's full text could not be accessed, and equivalent unindexed enumerations cannot be excluded.

## Mathematical value — PASS
The natural conserved mass grades the attractors of a deterministic fixed-energy sandpile. The result determines the exact number of primitive periodic orbits in every mass sector for every path length, quantifies their Pell growth, and proves a nontrivial asymptotic distribution of mass under the uniform orbit measure. The bivariate transfer law is a reusable enumerative bridge from known local firing inequalities to orbit populations, rather than a mere restatement of known mass-threshold theorems.

## Review boundary
No external independent verification was performed. The 1992 full-text access gap and possible unindexed equivalences remain scientific literature risks, not substitutes for checks.

Self-review: passed. Independent audit: not yet performed.
