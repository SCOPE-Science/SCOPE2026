# Independent audit — 2026-09-29

Record: `2026/09/12/100`  
Audited source tree: `c4bcbfb916a01d9d9211c3a0a14d3231c839fb5c`  
Disposition: **passed**

## Correctness

The thinned-subfield counterexample is mathematically sound. For P0=F_r^3 and the affine F_r-planes inside F_{r^2}^3, |P0|=r^3, |Pi0|=r^3+r^2+r, every starter plane contains r^2 starter points, and every F_r-line contains r starter points and lies in r+1 starter planes. Independent Bernoulli thinning with probability 1/r gives point/plane expectations r^2 and r^2+r+1 and incidence expectation r^3+r^2+r. The record's variance bound Var(I)<=4r^5 is conservative but valid; direct covariance counting gives an even smaller order. At r=6561 the stated failure majorant evaluates to about 0.00247349<1, including the line-cap union bound. The equalization-by-minimum-degree deletions retains at least one quarter of the pre-equalization incidences under the stated size windows, yielding I>=r^3/8 at N=floor(3r^2/4). Since N is Theta(r^2), I/N^(3/2-delta) grows like a positive power r^(2 delta) for every fixed delta>0.

## Originality

Subfield constructions are a standard obstruction in finite-field incidence geometry, and Rudnev's point-plane theorem explicitly contains a line-richness term. A focused literature check did not locate this exact random-thinning argument imposing an N^(1/4) point-and-plane line cap while retaining Omega(N^(3/2)) incidences. That non-detection is not treated as proof of priority.

## Scientific value

The result decisively falsifies the proposed power-saving statement under the stated line cap, and it identifies a concrete obstruction that any corrected incidence theorem must exclude or control more strongly.

## Limitations

- The witness is probabilistic-existential for each r=3^k rather than a deterministic closed-form point/plane list.
- The construction refutes the N^(1/4) cap formulation but does not identify an optimal replacement hypothesis.
- The originality assessment is deliberately qualified because literature non-detection does not establish priority.

## Evidence and literature

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/12/100
- https://arxiv.org/abs/1806.03534
- https://arxiv.org/abs/1612.02719
