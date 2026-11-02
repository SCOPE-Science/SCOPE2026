# Scientific review: unique optimal interior-trap absorption

## Correctness — PASS

The statement fixes the infinite chain, dissipator normalization \(H=J(S+S^*)-i\eta P_0\), and point-source distance. Its eventual absorption is an absolutely convergent positive time integral. The exact scalar Laplace transform follows from the free-lattice Green function and the rank-one resolvent formula. Since the trap amplitude is square integrable by the norm-dissipation identity, Plancherel applies to its boundary values. Splitting inside and outside the continuous spectral band proves the stated exact absorption formula. Strict distance decrease follows from the positive exterior contribution; the first two inverse-distance terms follow from a justified small-\(u\) Laplace expansion. The elementary band integral evaluates to the stated three-case form. Its derivative is strictly negative for normalized coupling at least one, and below one its sign is controlled by a power series with one negative constant and otherwise strictly positive coefficients; hence the optimum is unique. The high-precision optimum, quadrature identities and finite-time lattice simulations replay with `verify.py`.

Risk: The numerical checks do not certify all parameter choices; global claims rest on explicit analytic inequalities. The long-distance remainder is fixed-parameter, not uniform across singular coupling limits.

## Originality — PASS, with priority qualification

Longhi's accessible main preprint establishes positive survival for finite sets of coherent traps but does not state the exact single-trap starting-distance law or the global remote-source loss-strength optimum. Riberi gives a fully explicit **boundary** absorber kernel, with reciprocal loss-strength duality and the maximum at normalized coupling one; it does not state or imply the different **interior full-line** formula and its unique optimum at \(1.225741123666\ldots\) from its uniform half-line result. Earlier absorbing quantum walks predominantly involve discrete-time coined walks or measurement protocols. The use of rank-one resolvents itself is known. Direct searches of previous comparable claims and mathematical records did not find the present combined exact geometry-sensitive optimization classification.

Risk: A separately hosted supplement to Longhi's main article could not be inspected; undiscovered equivalent interior-defect formulas or general scattering theory may subsume the claim. Publication priority is not certified.

## Mathematical value — PASS

The loss strength is a controllable physical design parameter and the eventual fraction of remote particles captured is a natural asymptotic transport efficiency. A complete sharp optimizer addresses a non-obvious competition between weak capture and Zeno reflection. Its value differs quantitatively from the boundary-sink optimum and breaks a known reciprocal-coupling duality. Strict dependence on launch distance and the inverse-square correction quantify the approach to this remote-source efficiency, rather than merely restating nonzero quantum survival. These features form a motivated complete classification of this canonical single-trap transport problem, not a parameter relabeling.

## Closest literature and limits

- S. Longhi, *Photonic random walks with traps*, 2024, https://arxiv.org/html/2405.07192v1 — same physical full-line setup; survival criterion and examples, but no assessed optimizer in accessible main text. Supplemental material was inaccessible.
- F. Riberi, *An Exactly Solvable Absorbing Quantum Walk*, 2026, https://arxiv.org/html/2605.08056v1 — half-line boundary sink and a different exact absorption kernel, reciprocal coupling symmetry and boundary optimum.
- M. Sabri, E. Segawa, M. Štefaňák, *Conditional limit measure of a one-dimensional quantum walk with an absorbing sink*, 2018, DOI: 10.1103/PhysRevA.98.012136 — different discrete-time coined evolution and conditional limit law.

The theorem has one interior loss site, infinite homogeneous full line, no dephasing, and fixed-parameter large-distance limits. It does not optimize each finite-distance absorption probability or provide finite-time first-passage distributions.

Self-review: passed. Independent audit: not yet performed.
