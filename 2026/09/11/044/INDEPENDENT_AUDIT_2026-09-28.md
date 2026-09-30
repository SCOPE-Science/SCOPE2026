# Independent Audit — 2026/09/11/044

**Audit date:** 2026-09-28 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `42c4a6c81a0614ac4fb99af6752d1e474b36ae78`  
**Audited current source tree:** `42c4a6c81a0614ac4fb99af6752d1e474b36ae78`  
**Audited main commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

## Correctness

PASS FOR THE LITERAL CLAIM ACTUALLY STATED. The 90-degree rotation preserves the disk, both nested squares, and the conductivity, and it sends the adapted probe at v=(1/2,1/2) to the adapted probe at (-1/2,1/2). DtN covariance therefore gives exact equality of the two quadratic-form observables. Their distance is 1, so any universal distant-smallness cap of 0.05 is incompatible with largeness at v. I independently recomputed the monotonicity lower bound on P'=[1/4,1/2]^2: with a=5sqrt(2), E=((1-exp(-a/4))/a)^2≈0.013754 and (100/3)E≈0.4585, comfortably above 0.25. Thus the distant rotated true corner also exceeds 0.05. The record carefully limits the conclusion to the literal universal-distant-smallness formulation.

## Originality

SUPPORTED, NARROW. Liu--Tsou establishes uniqueness/logarithmic stability for polygonal and nested polygonal conductivities from a single partial measurement, while related polygonal-conductivity work gives broader stability results. I did not locate the record's fixed 1/3/5, tau=5 threshold statement or this exact symmetry obstruction in those sources. The defensible originality is the explicit counterexample/certificate for the posed threshold conjunction, not a new general Calderón uniqueness theorem.

## Scientific value

MEANINGFUL ROUTE-DIAGNOSTIC VALUE. The argument exposes an exact symmetry obstruction that any proposed single-corner classifier must account for and salvages a quantitative largeness lower bound for a corrected vertices-versus-background formulation. It is a focused falsification rather than a general inverse-problem theorem, and the record says so.

## Independent checks

- rotation covariance argument independently reconstructed
- closed-form P-prime monotonicity integral independently recomputed
- current main record tree SHA equals the assigned source-tree SHA

## Sources consulted

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/044
- https://arxiv.org/abs/1902.04462
- https://doi.org/10.1088/1361-6420/ab9d6b

## Limitations

- The result refutes only a universal distant-smallness threshold that includes symmetry-related true corners; it does not prove a corrected four-corners-versus-background classifier.
- The monotonicity calculation concerns the exact full-DtN quadratic-form observable; any different CGO indicator requires an explicit identity or error analysis before inheriting the same numeric bound.
