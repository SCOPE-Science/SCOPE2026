# Scientific review

## Correctness

**PASS.** With an unconstrained scalar myopic follower, the best response is unique. Direct substitution gives the exact finite-horizon quartic \(G_{A,\eta}\). The reflection identity at the cost ratio \(\eta=1\) produces two and only two global minimizers precisely when \(A>2\). For unequal cost ratios, the favored-half-line derivative has exactly one positive root, establishing global uniqueness. Sign comparisons at the Schur boundary and at the two symmetric minima give the complete stability classification. The envelope theorem and a cubic stationary equation establish, respectively, the derivative jump and critical cusp. The standalone standard-library program reproduces exact identities and tests representative cases. A finite numerical sweep has not been treated as an infinite proof.

## Originality

**PASS, with residual priority risk.** The closest primary paper (Matt–Bolognani–Dörfler, arXiv:2604.27770) supplies the general scalar objective but treats explicit *optimal* incentive parameters in the long-horizon or large follower-cost limits. Its finite-horizon formula does not itself classify the multiplicity or dynamic stability of globally optimal two-stage incentive designs. Full HTML Sections II and III, including the finite-horizon objective and asymptotic propositions, were inspected. The accessible 2019 Wasa–Hirata–Uchida full-text article treats a different LEQG dynamic agency contract. Searches of mathematical publications and published-result summaries did not reveal the same sharp two-stage switching theorem. Earlier nonconvex dynamic-contract literature and standard quartic bifurcation theory could contain an equivalent presentation; novelty should be independently checked before asserting priority.

## Mathematical value

**PASS.** This is a natural complete classification at the shortest horizon where incentives affect future state costs. It demonstrates a non-robust global design decision: two equally optimal contracts can induce radically different long-run dynamics, and an arbitrarily small perturbation to the private follower-cost ratio selects opposite sides. The critical gain and exact cost derivative jump provide quantitative diagnostics not present in a statement that the scalar leader cost is merely nonconvex. The cubic-root boundary and full parameter-dependent stability phase diagram make the threshold mathematically precise. The finding is narrowly scoped and does not prescribe unstable operation.

## Closest literature and limits

Matt et al. (2026), arXiv:2604.27770, Proposition 2, is the main formula-level ancestor. Wasa et al. (2019), DOI:10.1049/iet-stg.2018.0256, is a related but structurally different contract. Feng et al. (2022), arXiv:2005.11872, was identified via its abstract; full-text priority overlap is unresolved but its BSDE and terminal-perturbation formulation differ from the current scalar fixed bilinear contract. The core claim applies only to the explicit two-period model without a stability constraint.

Self-review: passed. Independent audit: not yet performed.
