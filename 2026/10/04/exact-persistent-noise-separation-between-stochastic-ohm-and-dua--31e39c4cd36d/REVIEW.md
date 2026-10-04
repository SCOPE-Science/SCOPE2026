# Same-model review

## Correctness

PASS. The scalar additive-noise oracle satisfies the source stochastic assumptions, and the endpoint choice \(\alpha=2/L\) gives the exact reflection \(\mathbb T=-I\). Both algorithms are linear in the starting point and independent minibatch errors, so their terminal second moments reduce to explicit coefficient sums. The Dual-OHM impulse coefficient is obtained by solving its first-difference recurrence; at reflection it becomes \(1/[2(m-1)]\) for even \(m\) and \(-1/(2m)\) for odd \(m\). The OHM coefficients telescope to magnitudes \((j+1)/N\). Independence then gives the two exact variance formulas. The odd reciprocal-square series yields the limit \(\pi^2/4-1\).

The bundled exact-rational replay reconstructs both recurrences for horizons through \(24\) and checks every coefficient. It is a consistency check only; the all-horizon statement is established algebraically.

## Originality

PASS. The primary 2026 paper was inspected in full. It proves a uniform stochastic Dual-OHM residual bound, explains that its proof accumulates only \(O(N)\) noise weights while the analogous stochastic OHM identity has \(\Theta(N^2)\) weights, and reports empirical divergence of constant-batch S-OHM. It does not state the one-dimensional reflection formulas, the exact OHM coefficient \(4/3\), or the Dual-OHM limiting constant \(\pi^2/4-1\).

The deterministic H-duality predecessor was inspected through its linear-operator appendix. Its terminal-equality theorem applies to a fixed linear operator and therefore explains the common noiseless term, but it cannot identify transfer of independent perturbations at successive oracle calls. A full stochastic Halpern paper was also inspected; it motivates increasing minibatches because direct last iterates retain noise but does not give the fixed-batch reflected-map law.

Two closest scientific-index findings were read in full. They concern persistent-noise OSGM-SGD absorption and stochastic-delay randomized Gauss--Seidel, respectively, and do not imply the present recurrence.

Residual risk remains that specialized noisy linear fixed-point literature may contain the same scalar calculation under different terminology.

## Value

PASS. The reflected endpoint is a canonical boundary of the admissible nonexpansive family. The exact formulas convert the source paper's qualitative robustness contrast into a sharp benchmark: the same persistent oracle noise gives a bounded Dual-OHM terminal floor but an OHM mean-square residual growing linearly in the horizon. The finite Dual constant tends to the natural invariant \(\pi^2/4-1\), while the OHM leading coefficient is exactly \(4/3\).

This is a boundary theorem and benchmark, not a universal worst-case result. Its mathematical value lies in separating actual stochastic noise transfer from upper-bound proof artifacts on the simplest noncontractive instance.

Same-model review: passed. Independent audit: not yet performed.
