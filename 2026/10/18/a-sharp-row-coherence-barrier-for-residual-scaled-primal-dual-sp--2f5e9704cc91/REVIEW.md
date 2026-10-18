# Review of the exact row-Gram spectral claim

## Correctness
PASS. The error matrix follows from the specified PDHG map by direct substitution. A diagonal similarity and singular-value decomposition reduce the full problem to explicit two-by-two matrices; the characteristic polynomial, strict threshold, critical eigenvalue, divergence direction, nilpotency, and uniqueness of the positive diagonal two-step scaling are algebraically derived. The projected variant uses an explicit sufficient inactive-projection condition. The finite checker independently compares original updates, eigenvalues, and the claimed local two-step basin; these checks are not used as proofs.

## Originality
PASS under the available comparison. Zhang–Gao–Udell introduce the general poststep residual-scaling idea, and Zhang's related scientific exposition specifies PDHG and safeguarded block scaling. The complete presented spectral threshold for a fixed, unguarded, row-Gram-normalized *dual-only* scaling, its exact two-row correlation frontier, and the uniqueness of a two-step positive diagonal residual correction are distinct mathematical statements. Pock–Chambolle preconditioning changes proximal metrics, not this residual map. Relevant published mathematical records contained nearby results on PDHG parameter ratios and row coherence but not the same map and implication. An older general treatment of stationary primal-dual iterations might subsume the polynomial calculation; absolute bibliographic novelty is not certified.

## Mathematical value
PASS. The construction isolates a genuine algorithm-design tradeoff: a simple diagonal correction exactly solves the orthogonal-row benchmark in two iterations, but a sharply quantified small cross-row correlation suffices to destroy convergence even while the base method converges. The universal Gram-eigenvalue criterion permits pretesting a proposed unguarded trial on arbitrary dimensions, and the projected half-space basin links it to the motivating linear-program regime. This is a motivated structural boundary rather than an arbitrary parameter example.

## Closest literature and limitations
Zhang, Gao and Udell (2026), arXiv:2609.10732, discuss online scaling and its safeguards. Zhang (September 10, 2026) spells out the PDHG LP map and block residual safeguard. Pock and Chambolle (2011), doi:10.1109/ICCV.2011.6126441, treat diagonal primal-dual *metric* preconditioning. The present result does not apply to dynamically accepted safeguarded iterates, noninvertible matrices, or every starting state of the projected LP. The older 2011 source was located and compared by its abstract and described algorithmic class, not certified from its full text.

Self-review: passed. Independent audit: not yet performed.
