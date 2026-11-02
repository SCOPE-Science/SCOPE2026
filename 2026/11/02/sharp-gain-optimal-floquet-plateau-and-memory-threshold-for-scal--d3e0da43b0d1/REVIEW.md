# Review of the sharp scalar RMSProp Floquet plateau

## Correctness — PASS

The proof starts from the stated epsilon-outside deterministic update with positive quadratic curvature and positive smoothing. The memory and position equations force every genuine two-cycle to have opposite equal positions and constant second-moment state. At that cycle the Jacobian is explicit, and the two-step matrix equals the square of a sign-conjugated Jacobian with trace \(t\) and determinant \(\beta\). The strict quadratic Schur conditions hold at every \(h>2\varepsilon/\lambda\). The scalar discriminant and monotone trace give the exact optimal-rate plateau and its transition at \(\beta=1/9\). The exact rational tests and 720 randomized parameter cases reproduce the derived identities; no finite test substitutes for the proof. At the plateau endpoints the linearization has a nontrivial Jordan block, so the spectral-radius result must not be advertised as a uniform pure \(\beta^n\) norm rate.

## Originality — PASS under examined coverage

Loh, Mireles James, Xu, and Tao (arXiv:2610.30078v1) prove the above-threshold existence and local attraction near threshold, and report one-dimensional attraction numerically. Their equations (43)–(44) already provide the general block-Jacobian and symmetry-square identity, which are not claimed as new. The contribution here is the exact **all-supercritical-gain** Schur proof and the two-step Floquet spectral phase diagram, including the critical decay factor \(1/9\), a bounded optimal-gain window below that factor, and an unbounded window above it. The broad RMSProp minimizer theorem of Dimitrieski and colleagues concerns convergence below the cycle-creation threshold. Related optimizer-cycle papers concern different update maps. Existing literature might contain unindexed equivalent results; priority is provisional.

## Mathematical value — PASS

The paper's one-dimensional numerical assertion is upgraded to a complete analytic stability classification for arbitrary gain, while the exact fastest local rate quantifies a design tradeoff that cannot be read from existence alone. With \(\beta=1/25\), the gain range \(3\le h\le8\) is exactly fastest, and increasing the gain beyond \(8\) makes the cycle converge more slowly again. The transition at \(\beta=1/9\) distinguishes finite and infinite optimal-gain ranges without arbitrary parameter slicing.

## Limits and closest sources

The result applies only to deterministic scalar quadratic RMSProp with smoothing outside the root and full-state local Floquet attraction. It does not assert global convergence to the cycle or equivalence for other epsilon conventions. Closest inspected publications are Loh et al. (2026), arXiv:2610.30078v1, and Dimitrieski et al. (2026), arXiv:2603.15823v2. The spectral-rate law has not been independently validated.

Self-review: passed. Independent audit: not yet performed.
