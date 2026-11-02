# Self-review

## Correctness — PASS

For the stated deterministic symmetric branch class and strict coexistence range, the gas first integral follows by differentiation of \(\Phi_Q(g)\), and the origin/interface normalizations reproduce the source's full stationary profiles. A monotone \(F_Q\) comparison proves exactly one sign change between the radial densities. Its integrated positive part gives the total-variation and equal-prior Bayes-risk formulas. Implicit differentiation yields the exact \(G_Q\) formula; the inequality \(0<z_a<z/a\) proves its strict monotonicity; Taylor inversion away from the fold gives the nonzero three-halves coefficient. Numeric quadrature and derivative checks were replayed from the embedded standalone program (2,180 bounded checks). No finite test is used as an infinite proof. Boundary cases \(Q=4\) and \(m\notin(1,Q/4)\) are excluded from the dichotomy; the upper fold is considered only as a one-sided limit.

## Originality — PASS, qualified

The complete Grange arXiv v2 HTML text was examined in the pertinent kinetic equations, interface matching, stationary solutions, coexistence, discussion, and appendix sections. It supplies the two profiles, their existence windows, and nonmonotone droplet half-width, not an exact interbranch optimal classifier, its total-variation maximizer, or its three-halves upper-fold singularity. The closest earlier analytical claim on this model gives full radial ordering and total-variation asymptotics versus exponential reference laws; these are explicitly acknowledged as stronger background about normalized profiles but are not themselves statements about interbranch optimal classification or its reset dependence. Broader published sources on local-reset exclusion and crowding run-and-tumble dynamics use other models; accessible abstracts were inspected without representing them as full-text exclusions. This is a mathematical consequence of previously derived exact profiles, not a new active-gas solution. Unlocated or independently audited prior derivations remain a risk.

## Value — PASS

The coexistence of a metastable gas profile and a condensed profile makes the distinguishability of two phases from one spatial observation a natural non-equilibrium diagnostic. The exact likelihood-ratio boundary provides the optimal decision rule, not just stochastic ordering. The theorem exhibits a nonmonotone classification advantage at fixed \(Q=20\) although the droplet mass increases monotonically, and it quantifies a previously unidentified upper-fold \(3/2\) singularity. These are structural, testable observability features of the source model, with a complete fixed-parameter shape classification; no new general downstream theorem is necessary for their value. The result is specialized and uses known stationary profiles; it is not a claim of new microscopic phase physics.

## Closest literature and limitations

Primary source: Grange (2026), https://arxiv.org/html/2610.26149v2 , Sections 2–5 and Appendices. Related context: Thompson et al., arXiv:1012.0786; Pelizzola et al., arXiv:2012.10993; Miron and Reuveni, arXiv:2011.08241. The result assumes the source's continuum symmetric branch class, not microscopic decorrelation or arbitrary stationary-solution uniqueness. The Bayes statement assumes equal priors. Publication priority and independent mathematical verification remain open.

Self-review: passed. Independent audit: not yet performed.
