# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/uniform-maximizes-three-point-minmax-correlation--92f0f4188ee4`  
Assigned and audited source tree: `ab8f88bb2c622e835800e391870db0f2d98425b4`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `d0a4ac8b120d6e43c791f45fb9951719e1b77427`  
Disposition: **passed**

## Correctness

**independently_reproduced**. The sharp correlation theorem is correct. After affine normalization to {-1,0,1}, direct enumeration of the nine iid outcomes reproduces the stated G, covariance and variance identities and hence the rational squared correlation R(q,t). Independent symbolic differentiation reproduces the common factor structure and the exact resultant -2304 q(q-1)^9(2q-1)(4q^2-2q+1). Thus a nonsymmetric interior stationary point could only have q=1/2, where the sole common real derivative root t=1/4 equals q^2 and is boundary. On the symmetry line t=0, the derivative has the stated factor 3q-2 and the unique interior maximum is q=2/3, giving R=64/361 and Corr=8/19 at uniform weights. The two simplex-edge formulas are at most 1/9, while degenerating to a point mass drives the correlation to zero. Continuity along the symmetric family gives every full-support value in (0,8/19].

## Originality

**supported_first_nontrivial_open_direction_case**. The closest prior work is unusually specific. López-Blázquez-Salamanca-Miño already treat order-statistic correlations from discrete parents computationally, including the three-point/two-draw setting at fixed probabilities. Papadatos's 2022/2023 discrete Terrell paper then considers varying the probability vector on a fixed lattice and states the expectation that the uniform vector maximizes correlations, while noting that a proof was unavailable. The audited theorem proves exactly the first nontrivial N=3, n=2, min-max instance, with the sharp constant, unique equality case, boundary analysis and full attainable range. Searches for 8/19 and synonymous three-point min-max formulations found no covering theorem. Originality is therefore well supported in this deliberately narrow scope, not for the fixed-p correlation formula or general Terrell theory.

## Scientific value

**meaningful_exact_open_problem_progress**. The result resolves the first nontrivial probability-weight case of an explicitly stated extremal direction and supplies a complete sharp simplex optimization. Its algebraic reduction also provides a plausible template for testing larger finite supports.

## Independent checks

- Enumerated the nine sample outcomes independently and recovered the covariance/variance reduction.
- Recomputed the two partial derivatives and their exact resultant symbolically.
- Verified the q=1/2 boundary root, the q=2/3 symmetric maximizer, and both simplex-edge maxima.
- Checked Corr=8/19 at uniform weights and the benchmark nonuniform value 9/23 at (1/4,1/2,1/4).

## Literature and evidence checked

- https://doi.org/10.1016/0167-7152(85)90035-5
- https://doi.org/10.1007/BF02929879
- https://doi.org/10.1007/s00180-021-01103-5
- https://arxiv.org/abs/2205.14360
- https://doi.org/10.3103/S1066530723020035
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/uniform-maximizes-three-point-minmax-correlation--92f0f4188ee4

## Limitations

- Only three equally spaced support points, two iid observations, and the min-max pair are covered.
- No claim is made for larger supports, different order-statistic pairs, unequal support geometry, nonlinear maximal correlation or sampling without replacement.
- The exact elimination was independently reproduced symbolically but is not formally proof-assistant verified.
- As with any narrowly phrased finite-support extremal result, differently indexed older coverage remains a residual terminology risk.
