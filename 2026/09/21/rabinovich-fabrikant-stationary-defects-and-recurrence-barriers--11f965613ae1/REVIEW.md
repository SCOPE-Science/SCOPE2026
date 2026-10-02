# Review status

Mathematical audit date: 2026-10-01 UTC.

Disposition: **repaired**.

Correctness: PASS. The repaired claim is correct. Direct differentiation gives the displayed radial and energy balances. The sign decomposition is valid. For the positive compact invariant component, invariance applied to cutoff antiderivatives with derivative \(\varphi(z)\chi_\varepsilon(z)/z\) gives \(\int\varphi(z)(\alpha+xy)=0\) for every bounded continuous test function, hence the conditional law. The conditional radial identity is algebraic. A second cutoff applied to \(\log R\), together with \(|xy|/R\le1/2\), yields the logarithmic-radial identity. These are analytic statements and do not rely on the symbolic artifact.

Originality: PASS. PASS to the best of current knowledge on the repaired claim. The original package overclaimed novelty for the global off-plane mean and mean-height defect: the complete 20 September 2026 published Rabinovich--Fabrikant result already proves those identities, sign selection, and periodic-orbit consequences. The repair removes those as contributions. The earlier result does not state a conditional-in-height law or the logarithmic-radial stationary identity, and its global averages do not imply them. Resultary searches for the conditional law returned the repaired record and related but different stationary-balance results, with no earlier exact coverage located.

Scientific value: PASS. A heightwise conditional stationary law is a structural refinement of a global average: it constrains every occupied height of an arbitrary compact stationary state. The logarithmic-radial identity supplies a second independent exact stationary flux. These are natural diagnostics for a standard three-dimensional flow and are not merely a renamed global balance.

Evidence: `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.
