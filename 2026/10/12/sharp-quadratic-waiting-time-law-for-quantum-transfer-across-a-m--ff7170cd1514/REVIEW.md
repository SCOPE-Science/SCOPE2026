# Scientific review: sharp quadratic waiting-time law

## Correctness — PASS

The invariant basis consists of the antisymmetric missing-edge state (zero eigenvalue) and the symmetric state coupled to the uniform clique core; it produces the exact two-root amplitude. The loss is sandwiched by a positive weighted sum of phase errors. Every pair of nearest odd eigenphases determines integers of opposite parity. The algebraic norm of their approximate eigenfrequency ratio is a nonzero integer, yielding the displayed uniform lower obstruction. Conversely, the quadratic irrational ratio has bounded continued-fraction coefficients, giving an inhomogeneous half-integer approximation of size \(O_n(1/T)\), and thus an upper loss \(O_n(T^{-2})\). The executable reproduces independent finite matrix-amplitude checks. No finite calculation is used to establish the all-time assertions.

## Originality — PASS, with explicit residual risk

The close prior result is Kirkland--Monterde--Plosker, arXiv:2201.02720, Theorem 14(2a) and Example 3, which already gives adjacency proper pretty good transfer and no perfect transfer on exactly \(K_n\setminus e\). The present statement does **not** claim either qualitative property as novel; it concerns the exact optimal finite-deadline exponent, including a uniform all-time obstruction. The two additional primary sources (arXiv:2208.08971, Sections 3 and 5, and arXiv:2312.06906, introduction and join analysis) concern decidability, limiting probabilities, and perfect transfer, not the matched finite-time rate. The mathematical step distinguishing the claim is the nonzero integer norm combined with a bounded-type half-rotation covering argument. A general, differently indexed theorem about quantitative returns of two-frequency quantum dynamics could cover part of this claim; the targeted sources inspected did not establish such a domination. A failed search is not treated as a proof of novelty.

## Value — PASS

This is a physically meaningful resource question: knowing that near-perfect transport occurs in an almost-complete network does not say how waiting time depends on the required fidelity. The theorem proves both a universal impossibility of improving the exponent and a constructive route matching that exponent, not just one successful sequence. It distinguishes the adjacency model from the known Laplacian perfect-transfer phenomenon. The constants are not claimed to be optimal and depend on fixed graph order.

Self-review: passed. Independent audit: not yet performed.
