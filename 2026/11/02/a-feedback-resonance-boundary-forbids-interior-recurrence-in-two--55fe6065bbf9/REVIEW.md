# Self-review

## Correctness — PASS

The model uses three logistic feedback equations from [1, Eqs. (8)–(10)]. Because the derivative of environmental log odds cancels the logistic prefactor, the weighted coefficients of the independent strategy fractions cancel identically and yield \(\dot{\mathcal I}=\kappa\). This is a pointwise identity on the entire admissible state domain, with no averaging or closed-orbit hypothesis. The positive denominators establish the stated nonresonance inequality. Boundedness of the log odds on compact interior environmental sets excludes compact forward invariance and recurrence; bounded one-sided environmental log odds prove the oriented boundary-neighborhood conclusion. The explicit resonance example satisfies all five equilibrium equations for every \(0<u<1\), and the payoff matrices satisfy the source's strict inequalities. Symbolic checks in `verify.py` and a high-accuracy numerical integration test reproduce these identities. The nonrecurrence conclusion applies only where all environmental coordinates stay interior, and the oriented boundary result is a union, not selection of one face.

## Originality — PASS, with documented residual risk

The nearest primary source [1] is the exact five-variable model and its Fig. 8 uses the two particular nonresonant feedback triples tested here. The full paper was read in its model equations, environmental-feedback cases, equilibrium table, oscillation discussion, and mathematical appendices. Its stability inequalities contain the same feedback combination, but its printed findings do not derive a globally exact affine log-odds drift, quantify oriented boundary entry, or eliminate every compact fully interior recurrent set in the generic asymmetric model. The earlier two-population paper [2] has one shared environmental variable rather than three; [3] and [4] analyze different feedback equations. A prior specialized invariant in an equal-feedback synchronized reduction does not imply an invariant for independent, unequal community feedbacks; the new nonzero affine slope also has no analog in that restriction. Primary literature and semantic mathematical-record comparisons have not identified a theorem implying the claim. Residual risk is an equivalent result under a different representation or in literature not indexed or fully accessible.

## Value — PASS

The originating five-dimensional work presents apparent sustained oscillatory regimes, but the exact global feedback identity shows their numerical traces cannot be compact recurrent sets strictly inside the environment cube for either of the paper's concrete feedback triples. It adds a sharp feedback-ratio boundary and a finite-time scale for entering oriented boundary neighborhoods, a structural result applicable to arbitrary admissible payoff matrices and strategy paths. The explicit fully interior equilibrium continuum on resonance shows the obstruction is not a parameter-generic triviality. It does not establish eventual convergence to a specific boundary face, a stability classification, or absence of boundary cycles.

## Closest sources and verification

[1] Betz, Fu and Masuda, arXiv:2404.17082v2, model Eqs. (5)–(10), Fig. 8, Table 2 and appendices. [2] Gong, Gao and Cao, CDC 2018, DOI:10.1109/CDC.2018.8619801. [3] Gong et al., arXiv:2205.10734. [4] Liu, Cao and Wu, arXiv:2210.10552. Exact claims and comparisons are documented in `AUDIT.json`. `verify.py` passed symbolic algebra, the symbolic equilibrium family, two exact rational source-parameter checks, and numerical trajectory integration with maximal affine-law residual \(2.96\times10^{-12}\). Independent audit is not performed.

Self-review: passed. Independent audit: not yet performed.
