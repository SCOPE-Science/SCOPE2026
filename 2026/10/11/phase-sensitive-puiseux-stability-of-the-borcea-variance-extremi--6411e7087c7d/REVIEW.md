# Review of Phase-sensitive Puiseux stability of the Borcea variance extremizer

## Correctness

PASS. The original \(n\) roots remain at \(n\)-th roots of unity up to \(O(t)\), so their standard deviation is \(1+O(t)\). The derivative has a multiple zero of order \(n-1\) at the origin when \(t=0\). Since \(Q'(0)\ne0\), rescaling by \(\rho_t=(t|Q'(0)|/n)^{1/(n-1)}\) gives a polynomial with \(n-1\) distinct simple limiting roots; their expansions are uniform to \(O(\rho_t^2)\). A direct modulus expansion and the finite max-min operation yield the displayed angular coefficient. The \(n\) root phases form a uniform grid modulo the critical-point angular period, giving the exact range \([\cos(\pi/(n-1)),\cos(\pi/n)]\). Both endpoints are obtained by explicit linear perturbations. No finite computation is used as proof.

## Originality

PASS. The main 2026 source proves the global \(2\)-variance inequality, not the Puiseux rate of its deficit near the regular-binomial equality model. Its Section 7 estimates hypothetical normalized counterexamples near a reciprocal-mean equality parameter but does not treat derivative-root splitting of a perturbed binomial. The 2011 source conjectures global equality rigidity, but no local deficit formula. Earlier Sendov local-extremum literature uses a different normalization and does not imply the exact phase coefficient. Targeted searches for the exact perturbation, fractional exponent, Puiseux splitting, and quantitative Borcea defect did not identify an equivalent theorem.

## Value

PASS. The equality configuration \(z^n-1\) is the sharpness model in a major newly settled inequality, and its global equality classification at exponent two remains a natural structural question. The new result proves strict local stability in every direction with nonzero linear coefficient, determines the non-differentiable exponent forced by coalescing critical points, and classifies the sharp coefficient variation over all perturbation phases. This gives motivated information about the equality boundary, not just a reparameterization of the global inequality.

The result is not uniform over all perturbations, and the classical local Sendov literature may contain comparisons under different normalization; no global equality classification is claimed.

Same-model review: passed. Independent audit: not yet performed.
