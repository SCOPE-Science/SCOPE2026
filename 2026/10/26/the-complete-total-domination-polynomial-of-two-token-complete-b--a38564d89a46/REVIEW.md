# Review of the complete total-domination polynomial of two-token bicliques

## Correctness — PASS

The theorem is proved for each integer pair \(m,n\ge2\). The three configuration types exhaust all two-element subsets, and the only edges join pure and mixed types. From the explicit open neighborhoods, pure vertices are covered exactly when the selected mixed-token incidence matrix has at most one empty row and column. Mixed vertices are covered exactly when the selected pure pairs form an edge cover of at least one original class. The two necessary-and-sufficient tests yield the polynomial factorization by inclusion-exclusion. The minimal-size classification uses sharp edge-cover and incidence-matrix lower bounds, with labelled counts derived by matchings and surjections. The standalone check reconstructs token-graph adjacency and matches all polynomial coefficients for nine parameter pairs, with direct exhaustive all-subset checks for five. Finite checks do not establish the infinite theorem; the structural proof does.

## Originality — PASS, with residual historical uncertainty

Fabila-Monroy and Gómez-Galicia (arXiv:2509.16448) give ordinary token-graph domination results for stars and complete graphs. Chinman et al. (arXiv:2610.28936) give the ordinary domination number for the same biclique token graphs, but no all-size total-domination polynomial. The published total-domination polynomial framework is substantially older (Chaluvaraju–Chaitra, 2014; Hu et al., 2016). The present factorization and minimum-set census require different open-neighborhood conditions and are not obtained merely by substituting the known ordinary-domination values. Targeted search found no matching result in the checked sources or accessible research records, but non-detection cannot certify priority. The newer October 20, 2026 preprint is used for an explicit later comparison; the motivating token-graph domination source was publicly submitted September 19, 2025.

## Mathematical value — PASS

This gives every coefficient, not just the minimum, for a canonical infinite two-parameter token-graph family whose ordinary domination number already exhibits several parity and adjacency cases. It exposes a clean product of edge-cover and non-isolated bipartite-incidence enumerators, determines all minimum configurations and their multiplicities, and explains the precise zero-or-one gap with ordinary domination. The exact combinatorial decomposition can also serve as a model for further open-neighborhood enumerations.

## Boundaries and further verification

No claim is made for one-sided singleton hosts, general bipartite hosts, or higher token counts. The finite verification consists of nine coefficientwise bipartition checks and five independent exhaustive subset checks; it is not an infinite certificate. Historical priority and independent mathematical assessment remain open.

Self-review: passed. Independent audit: not yet performed.
