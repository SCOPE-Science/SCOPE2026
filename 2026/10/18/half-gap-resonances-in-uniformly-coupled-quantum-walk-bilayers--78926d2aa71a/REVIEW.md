# Scientific review: half-gap resonance law for uniformly coupled bilayers

## Correctness (PASS)

The theorem covers every real symmetric finite matrix, including repeated eigenvalues and all coupling strengths \(g\ge0\). The proof establishes the exact factorization of the propagator, the two-channel time-dependent mixing matrix, and the Cesàro selection of precisely zero and opposite \(2g\)-frequencies. It then uses orthogonal layer projectors to obtain the additive rank formula. The Schur product theorem proves positive semidefiniteness of every positive-gap contribution, and orthogonality of distinct spectral projectors proves its constant-vector null direction. At \(g=0\), the formula recovers two disconnected copies. The complete-graph specialization evaluates both required matrices explicitly and checks their eigenvalues. The packaged exact rational checker independently reconstructs the bilayer spectral projectors and validates 42 finite profiles, including resonance, nonresonance and zero coupling. Finite tests are evidence, not the unrestricted proof.

## Originality (PASS; residual risk)

The closest antecedents are the spectral-commutant and rank treatment of Coutinho–Godsil–Guo–Zhan (2017), the exact spectral methods of Coutinho and collaborators (2022), and the general time-distribution and Cartesian-product formulas of Baptista–Coutinho–Marques (2023). In the latter work, Proposition 5 gives a general Fourier expansion and Section 5 gives instantaneous tensor factorization plus an averaged **trace** identity, but the inspected manuscript does not state this full block-diagonal Cesàro matrix, its finite gap-selector rank formula, the positive-semidefinite rank-jump restriction, or the tunable complete-graph three-regime classification. The known formulas substantially motivate and simplify the derivation; no claim of an entirely new Fourier technique or logical independence is made. Potential prior stronger coverage of tunable weighted bilayer ranks remains the principal originality risk. Fixed unweighted Cartesian products are acknowledged as special cases rather than credited as new; the explicit arbitrary-coupling classification is the claim under review.

## Value (PASS)

Cesàro mixing rank measures the dimension of accessible long-time vertex probability profiles. In uniformly coupled bilayers, coupling generally *reduces* rank to that of a single layer, while isolated exact energy resonances restore identifiable orthogonal directions. The formula gives an exhaustive finite set of possible resonance strengths and computable rank increments for arbitrary real-symmetric intralayer dynamics. The complete-graph case yields a sharp rank transition of size \(m-1\) at the physically distinguished coupling \(g=m/2\), showing this is not only a reformulation of a matrix identity. It provides a useful exact design and interpretation criterion in the standard two-layer coherent-transport setting. It does not address nonuniform or complex rung engineering.

## Principal sources and limits

Full primary text inspected: arXiv:1709.03591v1 (spectral formula, commutant, and rank); arXiv:2208.08971v1 (exact quantum mixing and source classification); arXiv:2308.16378v1 (general sampled averages, Cartesian tensor mixing and trace results). The theorem is an explicit consequence of Fourier decomposition under the stated physical specialization; a sufficiently general published classification may imply it. No independent external audit or validation has been performed.

Self-review: passed. Independent audit: not yet performed.
