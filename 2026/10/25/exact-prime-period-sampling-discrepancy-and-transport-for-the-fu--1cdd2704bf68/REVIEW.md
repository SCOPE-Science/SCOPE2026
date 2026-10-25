# Scientific review — Exact prime-period sampling for the full tent map

## Correctness (C): PASS
The \(p\)-fold tent iterate is explicitly affine on its dyadic branches. For prime \(p\), deletion of precisely the two fixed points leaves \(2^p-2\) least-period points. The proof uses the exact deletion index around \(2/3\) and checks all discrepancy inequalities for both branch parities on both sides. Quantile coupling and matching mass bounds prove the optimal transport identity. Covering and minimax optimality have explicit witnesses. The case \(p=2\) is separate. The included exact-rational verifier returned 41,669 successful assertions; finite tests are supplemental, not the universal proof.

## Originality (O): PASS under examined evidence
Fuhrmann–Gröger–Passeggi, arXiv:2610.07435v1 (2026), prove global rigidity from complete periodic-orbit spectra and discuss qualitative prime-period density, but no sharp finite-stage spatial discrepancy, covering-radius or bottleneck-transport identity. Gauthier–Vigny, arXiv:2505.02608v1 (2025), give a broader complex-rational-map quantitative equidistribution theorem for regular test functions, not an exact least-prime-period tent-map formula. Classical descriptions of tent-map fixed points and the general Lipschitz recovery principle are credited to prior mathematics. Relevant published mathematical-record searches did not identify a stronger source implying this exact combination. Residual risk: an older equivalent formula may exist under a different discrepancy/transport/interval dynamics terminology; this is not an independent priority certification.

## Mathematical value (V): PASS
The full exact-prime-period point set is a natural finite-resolution version of the periodic-data objects important to interval-map rigidity. The theorem provides a closed sharp error scale for **three distinct geometries** and an optimal worst-case Lipschitz observation guarantee, while identifying the exact internal gap and the primitive-period deletion effect. The composite-period-six countercontrol demonstrates a real boundary rather than a generic counting exercise. No extension to arbitrary interval maps or unlabeled map reconstruction is asserted.

## Scope and verification limits
The proof applies to the full-slope tent map and complete collections of least-prime-period points on the Euclidean unit interval. The verifier covers primes \(2,3,5,7,11,13\) and composites \(4,6,8\) only. Historical bibliographic priority and interpretation beyond the stated class remain open.

Self-review: passed. Independent audit: not yet performed.
