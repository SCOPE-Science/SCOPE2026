# Scientific review

## Correctness — PASS

The exact in-interval solution yields one strictly monotone implicit sampling equation, so existence and uniqueness are global. A two-input secant identity gives the mesh multiplier exactly, including its dependence on the sampling fraction and monotone activation slope. The sufficient global convergence criterion follows from a uniform absolute-value contraction; the linear activation attains its sharp boundary. For hyperbolic tangent, the strict critical contraction, cubic coefficient, inverse-square relaxation, antisymmetric two-cycle equation, and strictly stable multiplier were proved analytically. The included checker completed 2841 finite consistency assertions. These finite checks are corroboration only; the proof uses exact algebra and convergence arguments.

## Originality — PASS, with historical-priority risk

The July 2026 Oztepe–Karakoç article treats delayed conformable neural networks and proves sufficient Lyapunov stability conditions. The complete accessible primary text of Chiu (2013), particularly its model, Theorem 9 and Corollary 12, establishes sufficient global-exponential stability for impulsive and nonimpulsive advanced–retarded networks but not the sharp gain-independent scalar phase cutoff or the nonlinear supercritical orbit. The 2014 Chiu–Pinto–Jeng and 2015 Chiu–Jeng papers are exceptionally relevant; only their published abstracts and bibliographic descriptions could be inspected. The 2015 abstract advertises necessary/sufficient stability tests for scalar mixed arguments, so the linear stability boundary is **not** asserted as a new independent theorem. Their full-text inaccessibility leaves a priority risk for the stronger combined nonlinear claim. Related indexed research records were searched under the exact formulas, equivalent sample–hold descriptions, sigmoid flip cycles, and gain-uniform stability; no recorded result was found to imply this complete claim. Absence of a database hit alone is not a proof of priority.

## Mathematical value — PASS

The distinction is motivated by whether an implicitly sampled inhibitory network can tolerate arbitrarily strong gain: the exact sampling phase, not only gain magnitude, separates bounded and unbounded robustness. The same boundary also predicts whether a natural saturating activation settles, slows algebraically, or develops a stable oscillation. The full all-supercritical-gain cycle existence and stability statement adds a nonlinear structural outcome beyond a linear calculation, and the critical algebraic exponent quantifies the loss of exponential convergence.

## Closest literature and limitations

See the primary references and the structured comparison in `AUDIT.json`. The central caveat is access to the complete 2014 and 2015 papers, alongside possible special-case results in older scalar hybrid-equation literature. The work does not address multineuron systems, general oscillatory attractors, global attraction of the period-two branch, or nonmonotone activations.

Self-review: passed. Independent audit: not yet performed.
