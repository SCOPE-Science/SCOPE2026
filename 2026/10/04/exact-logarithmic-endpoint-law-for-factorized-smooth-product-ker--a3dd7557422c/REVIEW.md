# Review of Exact logarithmic endpoint law for factorized smooth product kernels

## Correctness

PASS. For each one-parameter factor, compact support and \(C^1\) smoothness of the homogeneous kernel give the uniform far-field expansion
\[
T_{\Omega_i}f_i(x)
=
M_i\frac{\Omega_i(x/|x|)}{|x|^{d_i}}
+
O(|x|^{-d_i-1}).
\]
After the exact scaling \(x=t^{-1/d_i}y\), the rescaled superlevel indicators converge almost everywhere on a fixed bounded set. Polar integration gives the exact tail coefficient
\[
A_i=
\frac{|M_i|}{d_i}
\int_{S^{d_i-1}}|\Omega_i|\,d\sigma.
\]
The product operator on a tensor input is the product of the two one-parameter transforms. A separately proved product-tail lemma turns
\[
|\{|h_i|>t\}|\sim A_i/t
\]
into
\[
|\{|h_1h_2|>\lambda\}|
\sim
A_1A_2\lambda^{-1}\log(1/\lambda).
\]
The high-amplitude regions are lower order because \(h_i\in L^p\) for \(p>1\). The proof distinguishes the exact limiting statement from finite estimates and uses no numerical sampling.

The coordinate-Riesz specialization is checked by
\[
\int_{S^{d-1}}|\theta_1|\,d\sigma=2V_{d-1}.
\]

## Originality

PASS. The 2026 primary source proves \(L^p\) boundedness for \(1<p<\infty\) under product \(H^1\) angular hypotheses and separate cancellation; it does not state an endpoint distribution law. The 2025 endpoint paper proves global hyperweak \(L\log L\) bounds and recalls a double-Hilbert unit-square example whose distribution is only comparable to \(\lambda^{-1}\log(1/\lambda)\). Direct full-text inspection found no exact coefficient there.

Published-finding database searches for exact product-Riesz tails, factorized product-kernel endpoint laws, spherical-\(L^1\) tail constants, and regular-variation product formulas returned no statement covering the theorem. The closest hits concern logarithmic defects of double Hilbert transforms, strong maximal-function obstructions, and unrelated exact product small-ball constants.

Residual risk: a classical or specialized paper not surfaced by the searches may contain the same regular-variation asymptotic under different notation. The inspected modern endpoint literature does not state it, and no broader theorem found in the search implies the exact coefficient.

## Value

PASS. The motivating 2026 theorem stops at \(p>1\), while modern endpoint theory identifies \(L\log L\), rather than weak \(L^1\), as the natural global scale for product singular integrals. The accepted theorem explains this logarithm by a transparent two-tail mechanism and gives its exact leading coefficient for a structurally natural infinite class: smooth tensor kernels and compact tensor inputs with nonzero masses. This is stronger than a single numerical calibration and sharper than the known comparability example. The coordinate-Riesz corollary supplies a canonical dimension-dependent benchmark for endpoint estimates.

Same-model review: passed. Independent audit: not yet performed.
