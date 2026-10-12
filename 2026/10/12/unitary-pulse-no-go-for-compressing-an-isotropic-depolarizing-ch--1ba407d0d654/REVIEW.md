# Self-review

## Correctness
PASS. The stated depolarizing map has the affine form \(\mathcal N_p(\rho)=\alpha\rho+(1-\alpha)I/2\), so it commutes with every unitary conjugation. An isotropic depolarizing semigroup therefore commutes exactly with each instantaneous pulse, and semigroup composition reduces any interleaved pulse sequence to the same total depolarizing evolution followed by one net unitary. Undoing that unitary leaves the uncontrolled channel exactly. The source's literal pulse average follows by linearity; a balanced Pauli average yields \(I/2\), while output-frame correction leaves \(\mathcal N_p\) unchanged term by term. The printed limit \(\lim_{f\to\infty}p\exp(-\gamma/f)=p\) is elementary and independent of the covariance proof.

## Originality
PASS with residual indexing risk. Unitary covariance of depolarizing noise and dynamical decoupling for structured baths are standard and are not claimed as new. The new claim is the exact implication for arXiv:2605.16463v1: its Appendix C compression \(p\mapsto p'<p\) is incompatible with the fixed isotropic channel that the same argument assumes. Targeted published-finding corpus searches found no source-specific correction under covariance, Pauli-twirl, dynamical-decoupling, or printed-frequency-law aliases. The closest owned record on the same preprint concerns a different post-channel LOCC optimization and does not imply the pulse/noise no-go. The inspected Uhrig paper uses an explicit \(\sigma_z\)-bosonic-bath model with memory and \(T_2\) dephasing, so it does not cover the fixed depolarizing CPTP statement.

## Value
PASS. The corrected point is the mechanism behind the paper's explicit depolarizing example, Appendix C construction, and reported dynamical-decoupling advantage. It identifies a structural modeling boundary: pulse control may alter a microscopic correlated interaction, but once the dynamics is replaced by an isotropic memoryless depolarizing map, unitary pulses cannot increase its Bloch contraction. This is a substantive constraint on any repaired separation theorem, not merely the correction of the source's high-frequency exponential limit.

## Closest literature and limitations
The primary comparison is arXiv:2605.16463v1, especially its explicit depolarizing construction and Appendix C. The closest dynamical-decoupling source is G. S. Uhrig, arXiv:quant-ph/0609203v2, which treats a structured pure-dephasing bosonic bath and finite correlation time. The result does not address correlated or anisotropic baths, error correction, enlarged encodings, or the amplitude-damping example.

Self-review: passed. Independent audit: not yet performed.
