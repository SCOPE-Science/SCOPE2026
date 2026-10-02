# Independent mathematical audit — 2026-10-01

Record: `SCOPE-20260921-1c8863f1cbd5`

## Correctness — PASS

Central symmetry makes each error characteristic function real and even; continuity from value one plus the nowhere-zero hypothesis forces it to be strictly positive everywhere. Each observed edge difference therefore gives \(\Psi_{ij}(t)=\varphi_i(t)\varphi_j(t)\), so logarithms satisfy the unsigned-incidence system \(a_i+a_j=b_{ij}\) pointwise in \(t\). On a connected component its nullspace is one-dimensional with alternating signs exactly when the component is bipartite, and is zero when an odd cycle is present. This proves identification exactly for components containing odd cycles. The Gaussian variance shift on the two bipartition classes gives a genuine distributional alias and can preserve one absolute marginal by compensating the latent variance. Componentwise edge counting gives the exact \(m\)-edge minimum for \(m\ge3\). The same reasoning is pointwise in \(t\in\mathbb R^d\).

### Correctness sources

- assigned RESULT.md
- artifacts/verify.py
- classical three-cornered-hat variance equations
- standard unsigned-incidence rank theorem

### Correctness risks

- Characteristic-function zeros, unknown centers, asymmetric errors, dependence, and finite-sample stability are outside the theorem.

## Originality — PASS

Searches across three-cornered-hat/triple-collocation, repeated-measurement deconvolution, pairwise-difference characteristic-function literature, and current Resultary findings found no source stating the distribution-level sparse-graph criterion. Classical three-cornered-hat work identifies variances from complete triples; Kotlarski-type work uses joint repeated-measurement distributions; recent pairwise-difference characteristic-function results address different independence questions. None implies identification from only selected pairwise-difference marginals with the exact odd-cycle iff condition, Gaussian bipartite alias, and minimal \(m\)-edge design.

### equivalent_formulations

Searches:
- Resultary query: symmetric measurement errors pairwise differences odd cycle graph identification characteristic functions minimal edges
- web query: "measurement error" graph pairwise difference distributions characteristic function identification odd cycle
- web query: "pairwise difference distributions" measurement errors identification
- three-cornered-hat and triple-collocation literature

Evidence:
- Current searches return the audited theorem as the only exact odd-cycle distribution-identification match.
- Located three-cornered-hat sources operate primarily at variance/covariance level, while repeated-measurement deconvolution uses richer joint data.

Reasoning:
Variance identification, full-joint deconvolution, and marginal edge-convolution identification were treated as distinct observation regimes.

### broader_coverage

Searches:
- Gray–Allan three-cornered-hat method
- Kotlarski repeated measurements
- Nearing et al. nonparametric triple collocation
- recent pairwise-difference characteristic-function papers

Evidence:
- These frameworks are broader in some modeling directions but require different data objects and do not yield the sparse comparison-graph iff theorem.

Reasoning:
A result using complete triples or joint distributions does not dominate a theorem that characterizes exactly which sparse edge marginals suffice.

### exact_database_or_table

Searches:
- current Resultary measurement-error findings
- web sparse-comparison searches

Evidence:
- No exact graph-design database/table or theorem was located.

Reasoning:
The \(m\)-edge minimum is a theorem from graph structure, not a finite design census.

### claim_vs_prior_implication

Searches:
- claim-versus-variance three-cornered-hat and Kotlarski implications

Evidence:
- Variance equations are only second-order consequences and cannot identify arbitrary symmetric error laws.
- Kotlarski's joint characteristic function contains phase/cross information absent from separate difference marginals; the audited positivity assumption instead linearizes edge products.

Reasoning:
Neither major prior paradigm mechanically yields the final claim.

### source_inspections

- **A Method for Estimating the Frequency Stability of an Individual Oscillator** — https://doi.org/10.1109/FREQ.1974.200027. Trigger: Canonical three-cornered-hat antecedent for pairwise comparison calibration. Material read: Primary method scope and variance-equation formulation as available from the NIST-hosted paper and later reviews. Method: Observation-regime and implication comparison. Assessment: Variance-level prior art, not distribution-level coverage. Evidence: The method solves individual oscillator stability variances from pairwise difference variances.
- **On characterizing the gamma and the normal distribution** — https://projecteuclid.org/journals/pacific-journal-of-mathematics/volume-20/issue-1/On-characterizing-the-gamma-and-the-normal-distribution/pjm/1102992112.full. Trigger: Classical repeated-measurement/Kotlarski identification antecedent. Material read: Primary theorem scope and the joint-characteristic-function identification setting. Method: Data-regime comparison. Assessment: Not covering sparse marginal difference laws. Evidence: Kotlarski-type identification exploits the joint law of repeated measurements rather than only selected marginal difference laws.
- **Distance Covariance, Independence, and Pairwise Differences** — https://doi.org/10.1080/00031305.2024.2374966. Trigger: Recent characteristic-function work explicitly centered on pairwise differences and nonvanishing assumptions. Material read: Full accessible article section containing Propositions 1–2 on independence and pairwise differences. Method: Primary theorem comparison. Assessment: Not covering. Evidence: Its propositions concern when independence is preserved or recovered from differences, not decomposition of heterogeneous error laws along a comparison graph.
- **Assigned graph verifier** — artifacts/verify.py. Trigger: Rank criterion, minimum edge count, triangle reconstruction, and Gaussian alias. Material read: Complete source and saved output. Method: Exact finite corroboration. Assessment: Correct support. Evidence: It verifies unsigned-incidence ranks for every connected simple graph through six vertices and checks the analytic constructions exactly.

### checked_sources

- Gray–Allan three-cornered-hat literature
- Kotlarski repeated-measurement identification
- Nearing et al. triple collocation
- 2024 pairwise-difference characteristic-function paper
- current Resultary sparse-graph search
- assigned verifier

### residual_risks

- An equivalent convolution-factorization theorem may exist in a specialized metrology or graphical-deconvolution literature under different terminology.
- Identification may be numerically ill-conditioned when characteristic functions are small even though they are nonzero.

## Scientific value — PASS

The result gives an exact experimental-design boundary for recovering full heterogeneous error distributions from sparse pairwise comparisons: an odd cycle is both necessary and sufficient in every component, the failure mechanism is explicit even for Gaussians, and the minimum comparison budget is exact. This is a motivated structural identification theorem rather than only a variance-level restatement.

### Value sources

- classical three-cornered-hat calibration problem
- assigned distribution-level graph theorem

### Value risks

- Population identification does not by itself provide a stable finite-sample estimator.

## Limitations

- Population-level additive independent-error model only.
- Central symmetry about the known zero center and nowhere-zero characteristic functions are essential to the logarithmic inversion.
- No theorem for asymmetric errors, correlated errors, characteristic-function zeros, or nonadditive observations.
- No finite-sample stability or rate result.

## Disposition

**PASSED**
