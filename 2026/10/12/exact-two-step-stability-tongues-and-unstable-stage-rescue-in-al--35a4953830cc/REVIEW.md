# Scientific review

## Correctness
**PASS.** The precise kick-drift-kick phase-space map has determinant one. Exact multiplication yields two factorizations of the trace relative to both parabolic edges. The two-dimensional determinant-one eigenvalue/Jordan criterion proves necessary and sufficient stability over all positive parameter pairs, including the unique \(-I\) exception. The checker tests the displayed identities independently on exact rational pairs and reproduces the rational examples. No finite sampling is used to infer the universal theorem.

## Originality
**PASS with historical risk.** Richardson–Finn (arXiv:1108.0322v1), §§1–2, explain parametric resonances from smoothly periodic prescribed timesteps by perturbative modified equations, rather than the exact all-contrast alternating velocity-Verlet Floquet classification and the separate stable-with-unstable-stage region. Skeel (1993) gives a prior qualitative counterexample for varying steps; the available original abstract does not establish the exact bidirectional full two-parameter classification. Its entire original text was inaccessible, so equivalence remains a named residual risk. These sources establish that periodic-step resonance is not new by itself; only the stated quantitative classification and exceptional boundary are assessed.

## Value
**PASS.** A natural safety question for geometric time integrators is whether stability of individual steps implies stability of their composition and whether a bad individual step always spoils a periodically repeated schedule. Both implications fail, with explicit exact witnesses and a complete sharp phase diagram. The isolated parabolic stability point further prevents an incorrect closed-inequality criterion, and the full result is applicable directly to harmonic normal modes.

## Limitations and sources
Linear harmonic oscillators only, strictly two-periodic physical steps, power boundedness rather than arbitrary-grid or nonlinear stability. Sources: Richardson–Finn (2011), arXiv:1108.0322v1; Skeel (1993), DOI 10.1007/BF01990352; Skeel–Gear (1992), DOI 10.1016/0167-2789(92)90247-K.

Self-review: passed. Independent audit: not yet performed.
