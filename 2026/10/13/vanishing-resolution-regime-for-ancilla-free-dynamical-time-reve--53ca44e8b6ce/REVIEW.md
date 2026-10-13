# Review

## Correctness
PASS. The claim is obtained by keeping the source's accuracy parameter variable in its explicit Appendix C.4 bounds. The sole new asymptotic condition \(\epsilon_n^2b_n\to\infty\) forces the \(\tau=+1\) false-rejection bound to zero and also forces every accuracy-dependent soundness correction to zero. Since \(b_n\sim n\log2/(4\log n)\), this is exactly \(\epsilon_n^2n/\log n\to\infty\). The source's remaining good-event term is already \(o(1)\) uniformly in the unknown unitary and the TRS sign. Amplification then gives the stated confidence dependence.

Risk: the result inherits the source's access model and its asymptotic estimates. It does not establish a converse for shrinking gaps.

## Originality
PASS. The primary source states the no-auxiliary theorem only for fixed accuracy. Its quantitative proof was inspected through the complete adaptive-interference argument, including the parameter choice, good-event estimate, completeness bounds, soundness bound, base query count, and confidence amplification. Targeted searches for the exact source, shrinking accuracy, equivalent normalized Frobenius formulations, and the crossover scales did not locate a published statement of the sequence-level result. Earlier T-symmetry testing papers inspect a different antiunitary operator-invariance property, a distinction explicitly documented by the primary source.

Risk: a contemporaneous note or a differently indexed generic uniformization argument could contain the same consequence. The claim is therefore limited to the concrete statement supported by the inspected literature.

## Value
PASS. The result changes the operational regime rather than only a constant: it shows that an ancilla-free dynamical-TRS test can retain sub-\(2^n\) query complexity while its promised symmetry-breaking signal vanishes with system size. The normalized Frobenius formulation identifies a natural sufficient resolution scale \((\log n/n)^{1/4}\) for this protocol. This is useful when accuracy is not fixed as dimension grows and does not overstate the scale as optimal.

Self-review: passed. Independent audit: not yet performed.
