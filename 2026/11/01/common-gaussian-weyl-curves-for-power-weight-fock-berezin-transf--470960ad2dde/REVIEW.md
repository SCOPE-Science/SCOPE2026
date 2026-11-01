# Scientific review: common Gaussian Weyl curves for power-weight Fock Berezin transforms

## Correctness (C): PASS

The weight is probability-normalized and the monomial moments exactly reproduce the Mittag–Leffler kernel. Published sectorial asymptotics give the normalized local Gaussian density \(G_\alpha(h)=\alpha p^2\pi^{-1}e^{-\alpha p^2|h|^2}\), with \(p=m/2\). The strong rescaled limit is proved using the same paper's global Gaussian intrinsic-distance bound; the outer-region tail is explicitly controlled. Translation estimates for large compactly supported plane waves then yield one weakly null Weyl sequence working for any finite list of weight parameters. The essential-norm statement uses only bounded polynomial calculus and the fact that compact operators vanish on weakly null unit sequences. The standalone supplementary script passes 67 direct numerical checks, which are not substitutes for the proof.

## Originality (O): PASS relative to inspected material

The closest source, Borichev–Fantolini–Youssfi, arXiv:2610.33937v1 (2026-10-24), was inspected in full accessible HTML. It supplies crucial kernel estimates and proves compactness and infinite rank of commutators; it does not state a common singular approximate spectrum or a positive exact-form essential *difference* lower bound. Tian's arXiv:2610.14599v1 concerns product equality; the earlier arXiv:2510.07887v1 concerns commutativity. Actual searches for joint Weyl sequences, limit-operator Gaussian multipliers, Calkin curves, and the explicit scalar formula found no decisive covering result. Unindexed general semiclassical/limit-operator work remains a material originality risk; no independent audit or universal novelty guarantee is claimed.

## Value (V): PASS

The theorem extracts new spectral information from recently introduced compact-commutator estimates. The continuum of common approximate eigenvalue tuples yields a nontrivial family of lower bounds for all polynomial combinations, and already for pairs gives a strictly positive quantitative essential separation with a closed form. Its value is the structural distinction between nearly commuting transformations and distinct noncompact operators, rather than a routine parameter substitution.

## Scope and limitations

Only fixed exponents \(m>2\) and finitely many fixed positive parameters are covered. The exact operator essential norm, full essential spectrum, and any parameter-uniform convergence are not established. The principal external analytic inputs are kernel localization and operator boundedness from arXiv:2610.33937v1. An equivalent specialized result could exist in unindexed literature.

Self-review: passed. Independent audit: not yet performed.
