# Mathematical review

## Correctness — PASS

The exact two-cycle difference identity is derived with both orientations of the map included. Strict monotonicity makes its left scalar product nonpositive for \(T\le2\), while the symmetric part of the model matrix makes its right scalar product strictly positive. For \(T>2\), an explicit four-dimensional closed box is shown invariant under the midpoint–difference fixed-point map, with global Lipschitz bound \(216e^{-6}<1\) for \(\alpha\ge10\). Banach contraction proves the unique box solution; quadrant bounds exclude a fixed point masquerading as a two-cycle. Reverse norm inequalities certify expansion of each Jacobian and every complex return eigenvalue. The proof establishes the infinite quantifiers; `VERIFY.py` reproduces 21 high-precision parameter cases and strict constants but is not substituted for proof.

## Originality — PASS within checked evidence

Buscarino–Famoso–Fortuna [1] explicitly define the same Euler map (equations (4)–(5)) and fixed numerical slice, then compute equilibria, attractor bifurcations, and periodic windows. Their accessible full article, including its analysis and appendices, was inspected. Its period-doubling observations do not imply the universal exclusion of primitive-two cycles through \(T=2\), nor a specific large-gain two-cycle outside attracting simulations with rigorous repulsion and localization. The closest indexed analogous period-two classifications concern distinct maps such as the rational Rulkov, cubic Duffing, and classical Tinkerbell maps, with no reduction to this specific sigmoid affine–skew map apparent. Earlier general monotonicity/contraction principles are acknowledged as proof tools rather than claimed new theorems. The evidence supports a model-specific contribution, but unindexed or unpublished equivalent calculations remain possible.

## Mathematical value — PASS

The result establishes a nonlocal, parameter-sharp no-two-cycle domain for all real states, and supplies a genuine primitive-two repeller immediately on the feasible side for sufficiently steep sigmoid activation. The contrast between nonexistence and a hidden repelling orbit is motivated by the published paper’s numerical bifurcation diagrams, which emphasize attracting motions and higher periods. The quantitative box, exponential localization and two-step spectral expansion give benchmarks for validated dynamics; the theorem does not require a global two-cycle census to be useful.

## Closest literature and limitations

[1] A. Buscarino, C. Famoso and L. Fortuna, *Nonlinear Dynamics* 111 (2023), 20361–20375, DOI 10.1007/s11071-023-08897-7, full open-access article. Exact source equations and numerical bifurcation figures were inspected, with no direct covering statement found. Related indexed classifications of different neuron and cubic maps do not imply this result merely because they also count period-two points. Residual originality risk: unindexed analyses or a stronger general criterion not found by the searches. Scientific limits: existence and hyperbolicity for \(\alpha\ge10\) only, uniqueness only in the stated box, no noise or finite precision.

Self-review: passed. Independent audit: not yet performed.
