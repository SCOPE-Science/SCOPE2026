# Independent audit — 2026-09-29

Record: `2026/09/19/forced-colouring-polynomials-paths--6ce41e28b289`  
Assigned and audited source tree: `2507a96e17afd1f1f5115cd62fc58826cf74993d`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **repaired**

## Correctness

**independently_supported**. The path coefficient theorem is correct. Independent exhaustive enumeration for P_n, 1<=n<=6 gives exactly 3*2^(n-j-1)*C(n-1-j,j) successful partial assignments with n-j initially coloured vertices. The Fibonacci recurrence, minimum-domain size and counts, uniform-point exponential scale, and the correction FC_3(P_3;p)=6p^2(1-p) all follow. The proof using independent omitted vertices and disjoint equal-sign constraints is valid.

## Originality

**requires_provenance_repair**. The exact path coefficient formula is not a separate September 19 discovery inside SCOPE. The earlier record `2026/09/17/forced-three-colouring-max-degree-two--2226d8f07ffd`, committed at 2026-09-17 23:56:20 UTC, already contains precisely this path formula as part of the broader path-and-cycle theorem. This record was committed at 2026-09-19 08:44:58 UTC. The repair retains it as a focused path corollary/alternate proof with extra minimum-domain and growth consequences, while removing the standalone originality claim.

## Scientific value

**useful_corroborating_specialization**. The focused path derivation and its enumerative corollaries are useful and independently verified, but their role is corroborative/refinement-oriented because the core coefficient law was already present in the earlier broader SCOPE record.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/commit/2bc43a7d60092cce0c0f86cebf225b20f6b40982
- https://github.com/SCOPE-Science/SCOPE2026/commit/1e80392bea35d307f7d99fd4e85c2b5f59d3692b
- https://arxiv.org/abs/2609.17108
- https://arxiv.org/abs/2406.15746

## Limitations

- The central path formula is a specialization of an earlier SCOPE theorem.
- The result is restricted to paths and the new content is in presentation and corollaries rather than first discovery.
- No claim is made about the inaccessible 1994 paper because repository chronology already resolves the originality issue.
