# Review: persistent three-switch dependence in heterogeneous occupancy

## Correctness — PASS

The object is independent allocation of exactly \(n\) labeled balls among three labeled boxes with positive fixed probabilities \((9/13,3/13,1/13)\). Exact binomial and multinomial moment calculations prove the general identity for \(\operatorname{Cov}(K,M_r)\), including the diagonal exclusion between empty and positive-frequency indicators. Direct integer evaluation verifies the fourteen strict signs at \(n=14\). For \(n=10t\), \(t\ge15\), four exact rational comparisons between maximal positive and negative integer-power bases, together with the explicit multiplicity bounds of nine and six terms, prove the alternating strict signs at \(r=t,4t,6t,9t\). The two-box boundary follows without enumeration from \(M_0M_r=0\) for \(r<n\), and \(M_n=M_0\) at \(r=n\). The open-neighborhood conclusion follows from finitely many strict polynomial inequalities. The accompanying independent multinomial-state checker passed 1,642 exact tests; all-\(t\) correctness rests on the proof, not extrapolation.

## Originality — PASS, with residual historical-priority risk

The focal March 25, 2024 multinomial-combinatorial paper develops related urn and Dirichlet-multinomial structures, not the heterogeneous exact-frequency covariance sign sequence. The inspected 2023 extended-occupancy paper concerns the marginal and conditional distribution of the number occupied in uniform bins. The closest accessible published one-switch result explicitly assumes **uniform** occupancy. Its conclusion does not mathematically imply a one-switch law for unequal probability vectors; the strict three-switch counterexample shows that generalization fails. Relevant published-result searches and accessible earlier occupancy claims were compared by model, statistics, hypotheses, and implication. Standard multinomial moment formulas could imply the example after additional calculation, but a formula alone does not state the infinite strict sign pattern and minimum-box boundary. Earlier implicit tabulations are possible, and the closest uniform published-result full text was not accessible; this is not represented as a full-document negative inspection.

## Value — PASS

Frequency-of-frequencies statistics and sample richness are central occupancy observables. The result isolates how heterogeneity defeats an exact qualitative one-switch law, not merely at a single handpicked finite order: one fixed three-category population has at least three switches at arbitrarily large sample sizes, robustly under small weight perturbations. The exact lower bound of three boxes identifies the smallest model supporting this phenomenon. This informs interpretation of richness/frequency covariances in strongly heterogeneous species/urn models without claiming wider asymptotic distributional results.

## Closest sources and limitations

Iksanov, Kabluchko, Marynych, and Wachtel, arXiv:2403.16448v1, March 25, 2024, Sections 4.1/5.1; O'Neill, *Three Distributions in the Extended Occupancy Problem*, 2023, open-access full text; an accessible published mathematical-result summary *A one-switch covariance law for occupancy richness and frequency counts*, uniform case. The result makes no novelty claim for the elementary moment formula. Intermediate large sample sizes and global maximal numbers of sign switches are not classified. Independent review has not occurred.

Self-review: passed. Independent audit: not yet performed.
