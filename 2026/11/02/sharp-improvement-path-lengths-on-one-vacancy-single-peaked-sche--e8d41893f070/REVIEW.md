# Scientific review

## Correctness
**PASS.** A monochromatic-edge potential decreases on every improvement below the half-peak boundary. At higher peaks, the vacancy's same-neighbor property becomes absorbing and each subsequent improvement removes two monochromatic edges. Symbolic constructive trajectories attain both bounds. `verify.py` provides supplementary finite exact-rational enumeration and direct path checks; finite tests are not substituted for the proof.

## Originality
**PASS (qualified).** Friedrich et al., arXiv:2302.12107v1, Theorem 2.4, cover one vacancy on rings only at peak \(1/2\); their Theorem 2.1 gives cycling counterexamples with more vacancies. The result here extends the one-vacancy finite improvement property to every peak, proves a sharp worst-case length, and identifies a peak-regime phase boundary. Swap Schelling games do not entail the jump theorem. An unidentified equivalent potential or specialized all-peaks classification remains a possible priority risk.

## Value
**PASS.** Finite improvement dynamics and tight convergence lengths on a canonical graph are meaningful because the neighboring literature shows cycles can occur on rings with additional vacant sites. The sharp regime change supplies a structural rather than arbitrary finite bound.

## Scope
Exactly one vacancy, both types present, two colors, strict improvements, the original self-included neighborhood fraction, and the original symmetric single-peak utility are essential. No claim for other graphs, multiple vacancies, heterogeneous peaks, or stochastic time averages.

Self-review: passed. Independent audit: not yet performed.
