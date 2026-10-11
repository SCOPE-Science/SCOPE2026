# Scientific review of the complete multipartite parity cycle classification

## Correctness: PASS

The statement covers all complete multipartite graphs with at least two nonempty parts and exactly the two unshifted synchronous XOR neighborhood updates. The proof factors the adjacency operator through the surjective part-parity map and the injective part-duplication map. The explicitly multiplied middle matrix gives the ranks of the first two powers; the recurrence on odd-sized part coordinates gives the stabilized rank and exact polynomial identities. These imply all enumerated periodic lengths, fixed-point dimensions, primitive cycle counts, and the rational zeta function. The sharp four-cycle is witnessed by \(K_{1,2}\). The locally packaged checker `verify.py` passed 481,628 exact finite assertions; it supports rather than replaces the infinite proof.

## Originality: PASS, with residual risk

Rollier--Baetens, arXiv:2606.14521v1, Sections 2.3 and 4, supplies the real-Jacobian spectral setting and identifies modulo-two walk cancellation, not this complete multipartite cycle census. Kantic--Qureshi--Panario--Legl, arXiv:2604.01548v1, provides general polynomial-module decomposition and algorithms for lengths and heights; it does not give the parity-of-part-sizes rank law or the exact network-specific zeta expression. Standard finite-field matrix theory supplies the general method but not the stated explicit classification without the part-parity calculation. Searches for complete multipartite Boolean parity networks, equivalent adjacency-matrix powers, primitive periods two and four, and broader dynamical counts did not reveal an identical published theorem. Priority risk remains: an earlier graph-specific calculation or an unindexed equivalent matrix formula could establish the same statement.

## Mathematical value: PASS

This is a natural complete classification of the periodic-point dynamical invariant for all graph sizes in a widely used network family and for both the self-inclusive and self-exclusive versions of the parity rule. The result gives exact counts, sharp period-four onset, explicit zeta functions, and a uniform global settling bound, rather than a sample of trajectories. In particular, on \(K_{2m,2m}\) the real adjacency radius diverges while the finite Boolean state dynamics are nilpotent or involutive, precisely delineating how two different diagnostic quantities behave. Its arithmetic phase diagram by parity of component sizes is absent from the motivating spectral calculation. The result should not be extrapolated to arbitrary network topologies or interpreted as invalidating the real tangent-space Lyapunov spectrum.

Same-model review: passed. Independent audit: not yet performed.
