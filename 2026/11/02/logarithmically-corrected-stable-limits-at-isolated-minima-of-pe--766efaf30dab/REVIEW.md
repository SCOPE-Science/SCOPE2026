# Review of the isolated-minimum stable-limit theorem

## Correctness

PASS. The proof specifies the full jump generator, its symmetry, the torus projection's uniform exponential total-variation mixing, local stationary densities, finitely many Morse minima, normalizing sequence, and the Skorokhod topology. The key calculation is the nondegenerate Laplace expansion of the rescaled predictable kernel; each contributing minimizer supplies \((2\pi\alpha_0)^{d/2}\rho_i\gamma/\sqrt{\det H}\). The uniform semigroup-mixing bound gives a mean-square triangular averaging error \(O((\log n)^d/n)\), independent of the initial state. Symmetry removes drift, and semimartingale characteristic convergence gives the claimed Lévy process. The supplementary deterministic code passed 95 checks; its finite tests are not substituted for proof.

## Originality

PASS, subject to explicit priority risk. Sandrić, arXiv:2610.30342v1 (October 21, 2026), proves a zero limit under the conventional scaling for null minimum sets and asks for another scaling; the current Morse-minimum theorem gives a nonzero functional limit with explicit coefficient. Franke (2006) covers conventional scaling and its abstract was compared, but its full paper was not accessible in this review. Kuhwald–Pavlyukevich (2016) already use a logarithmic Laplace prefactor for time-periodic additive independent-increment noise; that overlap is credited. Their metastable exit-time theorem does not imply a spatially dependent regime-switching functional stable limit. No equivalent claim appeared in the accessible research and own-record comparisons; these searches do not prove global uniqueness.

## Value

PASS. This resolves a natural, explicitly identified null-minimizer case of a recent functional limit question, gives the correct nontrivial normalization, and identifies how local quadratic geometry and stationary occupation masses combine into an effective stable Lévy intensity. The scale is provably sharp among normalizations asymptotically larger or smaller by unbounded factors. Degenerate minima and more general null minimizer sets remain outside the theorem.

## Limits and closest sources

The main primary source is Sandrić (2026), whose full public HTML proof and concluding open problem were inspected. Kuhwald–Pavlyukevich (2016) was compared through accessible full-text mathematical sections. Franke (2006) was checked only at abstract level; its inaccessible original full text is a material historical-priority risk. Results elsewhere could also imply special instances. The analytical proof is self-reviewed, not independently audited.

Self-review: passed. Independent audit: not yet performed.
