# Independent audit — 2026-09-29

Record: `2026/09/19/fixed-order-2-regular-coverage--f9fffbb78fec`  
Assigned and audited source tree: `6961a70e7c88884d8e87b70d61d3611e73e8546c`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The every-order construction and floor law check. Sivashankar's finite-order consequence supplies the upper deficiency floor. For sharpness, the Walecki block is valid because odd N>=r+2 leaves at least one Hamilton cycle beyond the (r-1)/2 cycles used for the base; deleting the distinguished vertex from that extra cycle gives a perfect matching on the other N-1 vertices. Attaching r-q such one-deficient blocks to each degree-q core-path vertex produces a connected simple r-regular graph. Every core incident edge is a bridge, so no core vertex lies in a 2-regular subgraph, while one Hamilton cycle from every block covers every non-core vertex. The excess e is even and keeps the enlarged block odd. The r=3 specialization algebraically agrees with the known exact cubic formula.

## Originality

**qualified_supported**. Sivashankar proves the sharp asymptotic constant 1/(r^2-3), the finite upper mechanism, and sharp endpoint constructions on n=(r^2-3)t+2(r+2). Choi--Kim--Kostochka--Park--West already settle every order for r=3. Searches did not locate the variable-order Walecki interpolation or the resulting exact fixed-order function for all odd r>=5. The contribution is therefore the all-admissible-order sharpness construction, not the upper inequality or endpoint examples.

## Scientific value

**meaningful_exact_completion**. The theorem converts a sharp asymptotic result into an exact finite-order extremal function for every admissible n and gives connected extremizers. The construction is elementary once identified but closes the discrete interpolation left by the source theorem.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/fixed-order-2-regular-coverage--f9fffbb78fec
- https://arxiv.org/abs/2609.19777
- https://arxiv.org/abs/1903.08795
- https://doi.org/10.1002/jgt.20443
- https://doi.org/10.37236/14739

## Limitations

- The theorem is only for k=2 and simple regular graphs.
- The upper inequality, asymptotic constant, endpoint constructions, and cubic specialization are prior work.
- Older factor literature under different terminology and very recent parallel work remain residual originality risks.
