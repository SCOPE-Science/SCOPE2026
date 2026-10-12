# Review of the contrast-driven Kitaev-dimer crossing theorem

## Correctness — PASS

The hypotheses specify the Hilbert space, Jordan–Wigner fermion operators, Hamiltonian sign, two nonnegative sitewise balanced rates, all four allowed initial Fock projectors, and precisely the two spectral degeneracies under consideration. The proof closes the exact five-operator Lindblad adjoint system, solves each damped two-component equation, and proves \(r=z_1z_2+w_1w_2\) by a conserved homogeneous linear relation. The four eigenvalues of the Hermitian parity-twisted fermionic partial time reversal then imply that the top singular gap vanishes if and only if \(z_1z_2=0\). Explicit trigonometric, polynomial-at-threshold, and hyperbolic root analysis exhaust the nonnegative-rate parameter space, including equality and boundary cases. Strict monotonicity of the first gap-closing time follows from elementary trigonometric and hyperbolic inequalities.

The packaged exact-symbolic script reproduces the Lindblad closure, the characteristic polynomial, and the quadratic relation. The direct matrix script executes 1,521 state/spectrum checks, including critical-rate and reverse-contrast examples. Neither finite testing nor the symbolic output is substituted for the all-parameter analytic argument. Every claimed finite-time zero is exhibited analytically; excluded zeros follow from strict positivity or strict monotonicity.

## Originality — PASS, with residual risk

The closest primary source is Chowdhary et al., arXiv:2610.03889v1 (2026-10-02), inspected in its accessible full HTML form, especially Sections III–IV and Appendix A.5. It proves general Gaussian parity equivalences and the invariance of clock times under **spatially uniform** balanced loss and gain. That equivalence is credited; the present theorem does not assert it as a new general fact. Its new claim instead classifies the first clocks and the disappearance of the later one for **unequal local rates while each local gain/loss pair remains balanced**, including the closed \(\arccos/\operatorname{arccosh}\) formula and the finite-earliest/infinite-latest transition. The previous uniform-rate result applies only at zero site contrast, and does not imply this bifurcation without further model-specific analysis.

Published mathematical-record searches using source names, the local-rate assumptions, the temporal exceptional point, and fermionic negativity aliases returned no statement equivalent to the specific contrast law. A prior published investigation of dissipative Kitaev entanglement crossings (Sayyad et al., arXiv:2011.10601) and PT-symmetric fermionic quenches (Starchl–Sieberer, arXiv:2304.01836) could only be compared through accessible abstracts; neither abstract states this two-site law, but that limited access remains a genuine priority risk. Search absence is not a proof of unique priority.

## Value — PASS

Spatial uniformity is a central premise of the motivating rate-invariance theorem, whereas actual open devices can have different site-specific rates even when each bath is particle-hole balanced. The exact minimal-system boundary is structurally informative: any nonzero contrast splits a previously coincident pair of entanglement clocks; a sharp contrast of \(4J\) removes the later finite crossing while the first **negativity** crossing persists and advances. The universal dependence on rate difference rather than mean damping provides an experimentally interpretable and reproducible benchmark. This is an exact all-rate phase diagram rather than a textbook parameter substitution or a numerically optimized isolated case. No extension to many sites, general dissipators, or a physical entanglement lifetime is inferred.

## Principal sources and limitations

- Chowdhary et al., *Exact Temporal Criticalities of Entanglement and Negativity in Gaussian and Non-Gaussian Dissipative Kitaev Chains*, arXiv:2610.03889v1, full HTML Sections III–IV and Appendix A.5.
- Sayyad et al., *Entanglement Spectrum Crossings Reveal non-Hermitian Dynamical Topology*, arXiv:2011.10601, abstract-level comparison only.
- Starchl and Sieberer, *Quantum Quenches in Driven-Dissipative Quadratic Fermionic Systems with Parity-Time Symmetry*, arXiv:2304.01836, abstract-level comparison only.

Residual risks are implicit-equivalent results in prior full texts not accessible during this examination, alternative normalization conventions in quantum-channel literature, and extrapolation beyond the exact dimer setting. The relevant normalization convention is fixed explicitly and checked directly. The narrow published-domain conclusion is not contingent on an inference of broader universality.

Self-review: passed. Independent audit: not yet performed.
