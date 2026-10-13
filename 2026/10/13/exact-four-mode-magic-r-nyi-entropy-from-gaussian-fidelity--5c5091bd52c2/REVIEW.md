# Self-review

## Correctness
**PASS.** The four-mode normal form and the equality of its parameter with fermionic Gaussian fidelity are published theorems. Gaussian-unitary invariance reduces the calculation to the vacuum/full-occupancy family. Substituting the four-mode value into the published exact convolution formula gives \(\nu_2=1-3t+3t^2/2\) with \(t=F_{\mathrm G}(1-F_{\mathrm G})\). The derivative is strictly negative for \(0\le t\le1/4\), so \(11/32\) is the exact minimum purity. A direct Majorana-convolution replay corroborates the normalization but is not used as the proof.

## Originality
**PASS.** The closest 2026 source proves a universal upper bound, explicitly leaves finite-size tightness open, and gives the cat-state value only inside a special family. Dias--Koenig supply the complete four-mode Gaussian-fidelity normal form but do not contain the later convolution entropy. Lyu--Bu study a four-qubit convolution family numerically without a global exact maximum. Exact-constant, alias, broader-coverage, and implication searches found no covering theorem. The main residual risk is a very recent or differently indexed note combining the same two ingredients.

## Value
**PASS.** The theorem answers the first nontrivial finite-size instance of an open tightness question, identifies the exact extremal orbit, and relates the order-two convolution entropy to Gaussian fidelity by a closed formula. It also proves that the universal upper bound is already strict at \(N=8\) Majoranas by an explicit gap \(\ln(1408/729)\).

## Closest literature and limitations
The closest sources are Hoshino--Matsuda--Ashida for the universal bound and special-family convolution formula, Dias--Koenig for the four-mode Gaussian-fidelity normal form, and Lyu--Bu for convolution-based non-Gaussianity measures. The theorem is restricted to positive-parity pure states of four complex fermionic modes and Rényi order two; it does not classify mixed states, higher orders, or larger systems.

Self-review: passed. Independent audit: not yet performed.
