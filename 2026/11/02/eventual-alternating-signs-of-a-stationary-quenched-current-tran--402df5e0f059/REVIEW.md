# Scientific review of the stationary current transform

## Correctness — PASS

The source's Brownian crossing kernel and run-and-tumble resolvent give the same stationary exponential profile after their respective length-scale changes. Integrating the exact per-particle Bernoulli logarithm yields the stated dilogarithmic function. The only unit-circle singularity of the latter is at \(z=-1\); the explicitly derived \((1+z)\log(1+z)\) term produces the signed \(n^{-2}\) coefficient with a controlled \(O_\lambda(n^{-3}\log n)\) remainder. Pringsheim's theorem independently rules out a genuine PGF, and periodicity excludes nonlattice nonnegative Laplace laws. The packaged checker executed and agreed with the exact recurrence and 240-degree numerical tests. Risk: transfer bounds require the fixed-parameter limit; no assertion is made uniformly for diverging \(\lambda\).

## Originality — PASS, with priority qualification

The primary 2023 paper *already derives* the exact logarithmically averaged dilogarithm; neither this transform nor the quenched-cumulant prescription is presented as original. The assessed statement is instead the universal eventual alternating-sign theorem and its implication that exponentiating averaged log-generators does not define an honest current distribution. The source's full relevant sections III.2, IV.2, V.2 and conclusions were compared; no tail-coefficient nonrealizability theorem was found. Derrida and Gerschenfeld cover a different unreset setting; classical singularity analysis provides a proof tool, not the physical comparison. Searches of the accessible mathematical findings and primary literature revealed no identical claim. Residual risk: the sign obstruction may be recognized implicitly by specialists as a general fact about geometric averages of Bernoulli PGFs, and an unlocated broader statement could subsume the physical application.

## Mathematical value — PASS

This is a structural limitation on a natural current-fluctuation prescription, not a one-off negative coefficient: it holds for *every* finite positive parameter, quantifies the full signed tail, supplies a computable low-order witness, and applies to two distinct physical dynamics. The exact distinction between conditional/annealed measures and the geometric logarithmic average matters because the source explicitly discusses reconstructing a stationary distribution from that transform. It does not imply physical negative probabilities, invalidate all scaled cumulants, or substitute for analysis of true quenched probability measures.

## Principal sources and limitations

- Di Bello et al., arXiv:2302.06696v1: complete relevant derivation and discussion of the stationary logarithmic average, especially equations (35)–(39), (47), (56), and the run-and-tumble crossing kernel.
- Derrida and Gerschenfeld, arXiv:0907.3294: quenched/annealed current methodology in nonreset diffusive systems; only the accessible abstract and bibliographic information were inspected, not the full paper.
- Flajolet and Sedgewick, *Analytic Combinatorics*, Chapter VI: standard logarithmic singularity transfer, not a statement about the resetting current functional.

Self-review: passed. Independent audit: not yet performed.
