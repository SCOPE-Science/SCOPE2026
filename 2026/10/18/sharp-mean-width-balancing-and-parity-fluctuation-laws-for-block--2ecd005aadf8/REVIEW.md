# Scientific review

## Correctness — PASS

The vertex covariance is exactly the identity for every disjoint parity-check block of length at least three; the resulting trace-determinant inequality gives the unique enclosing ball. In each block the unconstrained maximizing sign vector either satisfies the parity check or must flip one sign, optimally at the least absolute Gaussian coordinate. The exact Gaussian support deficit and the spherical radial normalization produce the width formula. The half-normal tail integral has a strictly positive second discrete difference, proving both finite-size extremizers. Flipping the Gaussian direction proves the odd/even width-loss law. Exponential minimum limits, second-moment convergence, Lyapunov's triangular-array theorem, and a controlled spherical normalization give both asymptotic variance branches and the critical width scale. Numerical enumeration corroborates but does not replace these arguments.

## Originality — PASS, qualified

Ermel--Walter's *Parity Polytopes and Binarization* (arXiv:1803.10561) defines the classical even-parity polytope, cites Jeroslow's facet system, and studies extended formulations, outer descriptions and separation. Del Pia--Khajavirad's *The pseudo-Boolean polytope and polynomial-size extended formulations for binary polynomial optimization* (arXiv:2309.08693) studies polynomial-size descriptions of signed-hypergraph models. The publicly indexed record *Exact John–Löwner ellipsoids of type-D spin weight polytopes* (identifier `15c85fee505a`) gives John/Löwner radii of an individual rescaled parity polytope and was inspected in its full RESULT.md; it does not prove the disjoint-block width-balancing or parity-fluctuation claims. Other directly compared records concern Hanner bodies, rank-selected Boolean polytopes, logarithmic widths of crosspolytopes, or unrelated product-profile balancing. Neither the inspected primary sources nor the indexed comparisons implies the quantitative theorem here. The risk of equivalent prior statements using codeword-polytope, independent parity-check, or Gaussian complexity terminology remains; searching alone cannot certify global novelty.

## Mathematical value — PASS

This is an exact geometric optimization for an infinite family of polytopes with identical vertex counts, identical vertex radii, identical covariance matrices and identical Löwner ellipsoids. It shows that the arrangement of independent parity checks remains geometrically visible through intrinsic mean width, identifies both unique extremal block partitions, and quantifies a natural scale of visibility as block counts grow. The directional law separates odd and even block lengths not only by an atom at zero but by distinct limiting variances. Such invariants can distinguish polytope families not separated by their elementary combinatorial counts and enclosing ellipsoids.

## Limits and closest literature

All assertions require disjoint parity checks of lengths at least three. Existing single-parity-check facet and type-D ellipsoid results are prior information, not the new finding. The source search is bounded, particularly for possible alternative coding-theoretic formulations, and independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
