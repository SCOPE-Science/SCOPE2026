# Scientific assessment: three-trial mean-square threshold for Gaussian orthogonal joint diagonalization

## Correctness — PASS

The claimed family and loss coincide with the actual one-random-combination and best-loss selection rule. For nonzero Gaussian weights, the squared random combination is a scalar identity, so the Frobenius energy in its eigenbasis is exactly computable. The proof derives a finite-parameter survival function for the selected loss; independent trials raise the one-trial tail to their number. Exact angular integration yields the one-trial squared mean, elliptic first mean, and the best-of-two Catalan coefficient. Tail integration, an integrable upper envelope for three or more trials, and a logarithmic endpoint comparison prove the stated squared-moment transitions; two further elementary integrals yield the exact three-trial coefficient. The deterministic optimum follows from the direct two-matrix rotation identity. Fractional-arithmetic identities, direct rotation tests, deterministic angular counts, and tail quadrature have been replayed using the embedded program. These checks corroborate, rather than replace, the proofs.

## Originality — PASS (best knowledge; priority not independently certified)

He–Kressner, arXiv:2212.07248, Algorithm 1 and the loss in equation (1.2), is the direct predecessor, and Theorems 6/8 with Section 3.4 anticipate a general inverse-power failure bound and the benefit of repetitions. The present new statement is not that randomized diagonalization or restarts work: it is the exact finite-perturbation distribution for this particular noncommuting input and a sharp, attained three-trial threshold for optimal-order mean-square *loss*, with explicit logarithmic and Catalan/\(\log 2\) coefficients. The cited general high-probability bounds do not supply these equalities, lower bounds or constants. He–Kressner arXiv:2402.16557 uses congruence diagonalization by a generalized pencil, and Li–Lu–Yu arXiv:2205.15519 uses vector-wise optimization, so their algorithms are not the same random experiment. Targeted literature and mathematical-record searches identified no equivalent exact law. Residual priority risk: an existing exact two-dimensional random-eigenbasis computation or an unstated corollary in other literature might cover the result.

## Value — PASS

The source framework is intended to turn high-probability guarantees into practical approximation accuracy. This example shows why that is not sufficient to predict expected squared loss: almost every one-shot output is of size \(\varepsilon\), but its mean square is of order \(\varepsilon\), not \(\varepsilon^2\). It identifies a precise, small, fixed restart budget that restores the optimal \(\varepsilon^2\) order, and demonstrates the irremovable logarithmic barrier with only two trials. The exact distribution supplies a diagnostic benchmark for uncertainty quantification and stress-testing implementations. The scope is intentionally restricted to the fully specified dimension-two symmetric input, and no general trial-count guarantee is asserted.

## Closest literature and limitations

The strongest predecessor is the full text of He–Kressner (arXiv:2212.07248, specifically Algorithm 1, Theorems 6/8 and Section 3.4). The rigorous generic failure bound and the observed power-law improvement with restarts are credited and not renamed as new. Other inspected nearby approaches use different diagonalization mechanisms. The benchmark does not address arbitrary symmetric families, hardware error, complex weights, or forward eigenvector accuracy. A previously unnoticed equivalent exact law remains possible; an independent originality check has not been performed.

Self-review: passed. Independent audit: not yet performed.
