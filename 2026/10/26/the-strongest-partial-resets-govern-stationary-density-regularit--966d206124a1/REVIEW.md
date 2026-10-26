# Scientific review

## Correctness — PASS

The invariant representation follows from independent exponential holding times, the Laplace law for a Brownian increment over an exponential time, and multiplicative contraction. The full-reset cusp is the derivative jump of the Laplace kernel convolved with a measure with atom \(p_0\) at zero. Under \(0<q_-\le Q\le q_+<1\), the upper characteristic-function bound is the deterministic \(q_-\) product; a lower bound costs only \(\exp(-O(y))\) for an order-\(y\) sequence of near-minimal resets. Both bounds give \(\log\phi(ae^y)/y^2\to-1/(-\log q_-)\). Fourier inversion and a positive-integrand Laplace principle yield the all-order derivative exponent \(-\log q_-\), establishing smoothness and nonanalyticity. The assumptions and boundary \(q_->0\) are essential. The finite verifier has 223 checks and is corroborative, not a replacement for the proof.

## Originality — PASS, qualified

The prior deterministic partial-reset product and stationary distribution from Di Bello et al. (2023) are explicitly credited; the moment formalism and random-affine reset framework of Assefa et al. (2026) are also credited. Kolb–Wübker (2026) treats the deterministic setting, and Ferreiro-Castilla–Utzet (2010) treat deterministic infinite Laplace convolutions. Material from their primary texts was compared for the exact high-derivative claim. None of the inspected results implies the stated dependence on the essential infimum of a *random* reset factor, or the combined cusp/high-derivative classification. Published-query and mathematical-record searches found no equivalent theorem. Generic perpetuity regularity literature could overlap implicitly and remains a priority risk; a search miss is not proof of novelty.

## Mathematical value — PASS

The two regularity mechanisms are natural and experimentally identifiable consequences of the same affine resetting model. Unlike finite moment formulas, the sharp high-derivative exponent identifies the smallest admissible contraction scale, robust to an arbitrarily small but positive probability of strongest resets. The essential-infimum fingerprint and discontinuous cusp at zero-reset mass provide a structural boundary between complete and strictly partial resets, rather than a new notation for existing moments or a finite special-case calculation.

## Closest literature and limitations

Assefa–Keller-Ressel–Palmowski, arXiv:2610.01363v1 (moment and cross-moment formalism); Di Bello et al., arXiv:2305.13722 (fixed-multiplier stationary product); Kolb–Wübker, DOI:10.1112/blms.70314 (fixed-multiplier invariant/quasistationary laws); Ferreiro-Castilla–Utzet, arXiv:1009.1543 (general deterministic Laplace convolutions). No sharp high-derivative exponent is claimed when the essential infimum is zero without an atom at zero. Neither priority nor mathematics has been independently certified.

Self-review: passed. Independent audit: not yet performed.
