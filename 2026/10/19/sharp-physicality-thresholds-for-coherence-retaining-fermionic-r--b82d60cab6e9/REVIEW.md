# Scientific review

## Correctness (C): PASS

An admissible gauge-invariant fermionic one-particle covariance is exactly a self-adjoint positive contraction \(0\le\Gamma\le I\). Its system–environment block \(z\) obeys \(z^*z\le p(1-p)I\) because \(\Gamma-\Gamma^2\ge0\). The two Schur complements of the reset output give sufficiency of \(\eta^2\le\min\{\inf\sigma(B),1-\sup\sigma(B)\}\). Rank-one projectors with arbitrary environment unit vectors, followed by \(p\to0\) or \(p\to1\), prove necessity even at non-eigenvalue spectral edges. The statewise criterion, thermal specialization and one-mode Choi eigenvalue threshold are independently derived. The current standalone checker passed 2028 explicit spectral and channel assertions. The finite checks are supporting evidence, not an infinite-dimensional proof.

## Originality (O): PASS, with documented residual risk

The exact block-reset prescription was introduced and studied for heat/coherence fixed-point behavior by Kumar–Lazarides–Ala-Nissila (2026, arXiv:2604.17152v1, Sec. II.3); that prescription is prior work. Vieira–Lazarides–Ala-Nissila (2020, arXiv:2012.04083v1, Sec. III) introduce generalized elementwise one-particle resets, without the claimed sharp physicality envelope. The March 2026 continuous-time correlation-erasing embedding (arXiv:2603.15554v1) has distinct dynamics. No same threshold, thermal spectral-edge classification or separate local Choi tier was found in the inspected relevant full texts or the checked indexed results. This does not prove exhaustive novelty: standard positive-block-matrix theory could imply the theorem as a specialized corollary, and incomplete coverage of broader Gaussian-channel classifications remains a risk.

## Value (V): PASS

The modeled interpolation parameter is nominally allowed throughout \([0,1]\), but unconditional admissibility imposes an energy-band- and temperature-dependent ceiling; for a thermal band the ceiling can be exponentially small at low temperature. This matters for interpreting reset prescriptions intended to represent fermionic states, while avoiding any assertion that a particular published trajectory is unphysical. The result supplies exact statewise criteria, sharp rank-one witnesses and a physically important separation between covariance admissibility and local complete positivity. These questions are motivated by the source model rather than an arbitrary parameter slice.

## Main qualifications

This is a statement about admissible one-particle covariances for *all* inputs; it does not establish all reset dynamics are unphysical outside the threshold. A one-mode local qubit CPTP implementation is different from a general multimode fermionic Gaussian quantum channel. No independent audit or independent validation was performed.

Self-review: passed. Independent audit: not yet performed.
