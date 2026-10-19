# Scientific review

## Correctness — PASS

The all-size identity is reconstructed from the classical forest-extension count: fixing a marked path, deleting an off-path leaf gives leaf probability \(a_n^{n-k-2}\), and deleting an endpoint leaf gives \(k a_n^{n-k-2}/(k+1)\). Their sum yields the explicit regression. Direct subtraction produces a cubic sign criterion, which proves the complete unimodal shape and the \(n^{1/3}\) maximizing scale. Comparing the regression to the Prüfer marginal expectation proves an exact positive-to-negative centered crossing and strict negative covariance for \(n\ge4\). The marked-distance law, Rayleigh moment convergence and a uniform expansion yield the covariance and correlation constants. Endpoint cases \(n=3\), \(k=1\) and \(k=n-1\) are included. The packaged script separately checks all 280,391 trees through order 8, 15,931 exact differences, 98 rational finite covariance checks, and three large-size asymptotic comparisons.

## Originality — PASS with residual risk

The counting lemma, marginal leaf law, distance law and Rayleigh scaling are established prior mathematics, so novelty is restricted to the **global conditional leaf regression**, its cubic-root peak, strict negative finite covariance and explicit global covariance constant. In the closely related published endpoint-degree/distance result, the local degree decreases stochastically along distances, whereas the new global leaf regression initially increases and peaks before the typical distance scale. This published result does not state or imply the global-leaf formula without a separate off-path-vertex analysis. Pitman's forest-enumeration report and the accessible Aldous–Pitman random-tree sections do not furnish this regression. The open-access Aldous 1990 text was also inspected in the relevant leaf and diameter sections; it gives marginal properties rather than the claimed conditional global regression. Older tree-enumeration monographs remain partly inaccessible; an implicit multivariate identity in that literature is a genuine originality risk, not negative evidence.

## Mathematical value — PASS

A global tree-shape statistic (the number of leaves) has a counterintuitive conditional response to a natural distance observable: an exact \(n^{1/3}\) peak coexists with typical distance \(n^{1/2}\) and a strictly negative unconditional covariance. The finite formula, exact switch criterion and covariance asymptotics furnish a complete interpretable dependence classification rather than an isolated or arbitrarily sliced computation.

Self-review: passed. Independent audit: not yet performed.
