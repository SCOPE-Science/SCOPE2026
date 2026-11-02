# Self-review

**Claim:** For odd-prime-dimensional qudit graph states on any even torus \(C_m\square C_n\), checkerboard entropy in base-\(p\) dits is exactly \(mn/2-\gcd(m,n)+\mathbf1_{\{v_p(m)=v_p(n)\}}\).

## Correctness — PASS

The proof reduces the exact flat Schmidt spectrum to the rank of the finite-field checkerboard adjacency. A Laurent symbol factors as \((x+y)(1+xy)/(xy)\), allowing direct calculation of the periodic convolution kernel at all odd primes, even when cycle lengths are divisible by \(p\). Two root branches have \(\gcd(M,N)\) points apiece and two intersections; the local crossing quotient length is \(2\min(P,Q)\) except when the two prime powers coincide, when it is \(2P-1\). The count yields the claimed entropy without finite extrapolation. The package's exact Python checker reproduces 420 independent grid ranks and 15 local-algebra quotient lengths, with no failures. The analytic calculation is the proof; the finite data are corroboration only. Boundaries: even sides at least four, odd prime local dimension, homogeneous unit edges, specified pure checkerboard cut.

## Originality — PASS on examined evidence; priority remains provisional

The strongest overlapping historical work comprises graph-state entanglement-to-cut-rank formulas (Hein, Eisert and Briegel, arXiv:quant-ph/0307130; Hein and collaborators, arXiv:quant-ph/0602096), qudit controlled-phase methods (Looi and collaborators, arXiv:0712.1979; Chen and Zhou, arXiv:1507.05386), and general finite-characteristic periodic convolution (Zaidenberg, arXiv:math-ph/0606070). Hunziker, Machiavelo and Park (2004) treat related open-boundary square-grid automata. These texts were inspected in the relevant primary sections, not inferred solely from abstracts. They establish ingredients, not the odd-prime toroidal p-adic crossing length or entropy dichotomy identified here. Multiple published-result searches under modular rank, periodic harmonic functions, graph-state Schmidt spectra, and toroidal cut geometry also found no implication-equivalent item. The characteristic-two torus calculation has different local intersection structure and cannot imply this odd-prime theorem. Residual risk: unidentified specialized finite-field torus-rank results could establish this formula under different notation. No independent priority verification has been performed.

## Mathematical value — PASS

Exact checkerboard entanglement is an intrinsic graph-state resource invariant. The proof exposes a sharp, nontrivial distinction between equal and unequal prime-adic valuations of the two period lengths, accounting for a one-dit difference throughout an infinite family of finite physical networks. Its local-crossing length also informs finite-characteristic periodic convolution beyond the immediate entanglement application. The scope and boundary are motivated by ideal square-lattice qudit cluster-state geometry, not a contrived fixed-size computation.

## Verification and limits

The independently executable proof checker is `qudit_torus_check.py`; the expected exact stdout is `qudit_torus_verification.log`. The finite tests support, but do not prove, the infinite formulas. Nonprime or characteristic-two local dimensions, other cuts, arbitrary weights, noisy states, twisted tori and edge deletion lie outside the claim.

Self-review: passed. Independent audit: not yet performed.
