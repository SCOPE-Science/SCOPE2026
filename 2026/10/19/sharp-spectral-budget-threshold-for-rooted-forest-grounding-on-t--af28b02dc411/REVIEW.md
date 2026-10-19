# Scientific review

## Correctness — PASS

The claim is restricted to connected simple vertex-transitive core graphs with unit edge conductance and equal unit-price diagonal grounding. The proof establishes that each feasible grounded matrix is positive definite, so the log determinant is meaningful at every boundary point. Its Hessian is negative definite along every nonzero diagonal direction. This proves uniqueness among **all** vertexwise gain vectors, before any graph symmetry is invoked. Vertex-transitivity then forces two gain classes. The Schur complement of the pendant block gives the exact spectral determinant. The one-dimensional objective has a strictly positive derivative at the core-only endpoint, while the derivative at the leaf-only endpoint equals the decreasing resolvent expression minus the core order. The endpoint signs and strict concavity give both phases and equality at the boundary. Positive-semidefinite Laplacian comparison gives the complete-core extremum and strict threshold growth under transitivity-preserving edge addition.

The included standalone script reproduced 1,216 finite checks: independently built Laplacian determinants, exact SymPy identities, boundary and interior KKT conditions, multiple vertex-transitive core families, and unrestricted asymmetric competitors and numerical solvers. These finite checks corroborate but do not replace the proof. No positive-dimensional exhaustive graph census is claimed.

## Originality — PASS, with residual uncertainty

The closest source, Chebotarev–Shamis (arXiv:math/0602575, Theorems 5–6 and Appendix), establishes weighted rooted-forest determinant identities but does **not** optimize vertexwise grounding weights or characterize a core-dependent critical budget. Khosoussi et al. (arXiv:1604.01116, Sections 4–5) optimize a different set of edge-selection problems. Du et al. (Frontiers in Physics, 2022, Sections 3–4 and conclusion) derive corona spectra/coherence, not the determinant-maximizing diagonal gains. Liu et al. (arXiv:1804.10818) use a smallest-eigenvalue objective after grounding selected nodes, not the log-determinant variable-gain criterion. A closely related complete-bipartite grounding-allocation result concerns another graph family and neither states nor implies the vertex-transitive-corona spectral threshold or the clique extremal comparison.

published-finding corpus semantic searches for corona grounding, root-weight allocation, the exact resolvent equation and clique threshold returned no statement-equivalent result in their inspected summaries. That search absence does not prove originality; a less accessible or unindexed general determinant-design theorem might cover the claim. No such dominating implication was identified in the inspected primary texts.

## Value — PASS

The result transforms an unrestricted, continuous \(2m\)-variable optimal-design problem into an exact spectral threshold valid on **every** connected vertex-transitive core. It distinguishes two resource-allocation regimes and determines precisely when the core remains ungrounded, including a nontrivial boundary case. Strict monotonicity under transitivity-preserving edge addition and sharp complete-core extremality give a graph-structural interpretation beyond a numerical optimum. The complete-core threshold \(B=m(m-2)/2\) and four-cycle threshold \(B=8\sqrt7/7\) exhibit quantitatively distinct costs of underlying connectivity. The motivation is D-optimal grounded-Laplacian design, equivalently allocation of weights to rooted spanning forests.

## Evidence limits

The base is required to be vertex-transitive, all graph edges and grounding prices are uniform, and the middle/full-support gains generally require a uniquely defined scalar root instead of a radical formula. Finite tests are not exhaustive. Equivalent unindexed prior research remains possible. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
