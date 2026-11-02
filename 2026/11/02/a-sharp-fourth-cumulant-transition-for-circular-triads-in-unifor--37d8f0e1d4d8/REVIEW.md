# Self-review

## Correctness — PASS

For every integer \(n\ge3\), the proof reduces the centered number of circular triads to \(-Q_n/4\), where \(Q_n\) is a quadratic Rademacher chaos with signed line-graph adjacency matrix \(A=B^{\mathsf T}B-2I\). The fourth-moment classification counts precisely doubled-edge and simple-four-cycle configurations, yielding \(\kappa_4(Q_n)=-2M+24S\). The incidence identity \(BB^{\mathsf T}=nI-J\) supplies the exact fourth spectral trace; the closed-walk decomposition yields \(S=n(n-1)(n-2)(n-3)(n-7)/8\). No infinite assertion is inferred from finite enumeration. The independent standard-library script passed 156 assertions, including every tournament on 3 through 6 vertices.

## Originality — PASS, with residual historical-priority risk

Direct searches for tournament circular-triad fourth cumulants, excess kurtosis, all-order moment formulas, and signed-four-cycle identities did not uncover the stated polynomial or sharp \(n=8\) transition. The closely related full 2018 paper of Bruss–Ferguson develops the classical score relation, pairwise orthogonality, tetrahedral mixed-moment supports, and a CLT, but does not give the evaluated signed four-cycle sum or exact finite-order fourth cumulant. Harris–McShane (2024) gives generating functions for fixed circular-triad counts, not this all-order moment expression. Nevertheless, Kendall–Babington Smith (1940), the classical source for circular-triad distributions, could not be read in full; its potential implicit or explicit fourth-moment information remains a priority risk. The general score representation and second moment are not claimed as new.

## Mathematical value — PASS

Circular-triad count is an established paired-comparison consistency statistic. The exact fourth cumulant distinguishes small-sample platykurtosis through seven vertices from positive excess kurtosis beginning at eight, and identifies the finite-size leading correction \(12/n\) to Gaussian excess kurtosis. The signed-four-cycle identity exhibits why cancellation changes at order seven. These are global, exact distributional properties, not arbitrary finite table entries.

## Relationship to literature and limitations

Relevant sources are B. Narayanan (2016), *Connections in randomly oriented graphs*, https://arxiv.org/abs/1609.01003; Kendall–Babington Smith (1940), https://doi.org/10.1093/biomet/31.3-4.324; Bruss–Ferguson (2018), https://www.math.ucla.edu/~tom/papers/testing.pdf; and Harris–McShane (2024), https://cs.uwaterloo.ca/journals/JIS/VOL27/McShane/mcshane1.pdf. The exact result is for unbiased independent orientations only. Historical-priority uncertainty requires external checking before any claim of publication-level novelty.

Self-review: passed. Independent audit: not yet performed.
