# Same-model review

## Correctness

**PASS.** The source formula makes unit fidelity equivalent to \(\omega t=(2j+1)\pi\) for an integer \(t\). If \(\omega/\pi\) is rational, then \(e^{i\omega}\) is a root of unity, so \(2\cos\omega\) is a rational algebraic integer and therefore an integer in \(\{-2,-1,0,1,2\}\). Substituting \(2\cos\omega=2-8/N\) leaves the integer sizes \(N=2,4,8\), and each has the claimed minimal time. For every other integer \(N\), \(\omega/\pi\) is irrational, so density of irrational rotations gives arbitrarily high fidelity but equality is impossible. A direct finite-matrix replay matches the exact source fidelity formula.

## Originality

**PASS, narrowly scoped.** The source itself contains a tension between its exact integer-time implementation and its terminology: immediately after deriving the continuous phase condition it chooses the closest integer time and calls the result “(almost) perfect,” while the abstract and conclusion say perfect transfer occurs for arbitrary \(N\). The later complete-bipartite paper again reduces same-part dynamics to the star case and says perfect transfer is achieved. Neither inspected paper states the exceptional set \(N=\{2,4,8\}\) or the complementary pretty-good-transfer conclusion.

Targeted published-finding corpus and web searches for the exact exceptional sizes, rational eigenphase, root-of-unity obstruction, and pretty-good transfer did not locate this classification. Chan--Zhan's later general pretty-good-transfer theory is a substantive residual risk because it gives number-theoretic criteria for a class of discrete-time walks, but the inspected text did not explicitly identify the marked-search star model or state this classification. The accepted claim is therefore only this explicit arithmetic sharpening, not a broad theorem about coined quantum walks.

## Value

**PASS.** Perfect versus arbitrarily-good transfer is an operationally meaningful distinction in a genuinely discrete-time walk. The result resolves the source's “perfect” versus “(almost) perfect” wording using its own exact formula, gives the full finite-size exception set, and shows that every excluded size still retains asymptotically unit fidelity rather than simply failing. It also prevents nearest-integer peak estimates, such as the source's \(N=100\) example, from being mistaken for exact unit-fidelity events.

Same-model review: passed. Independent audit: not yet performed.
