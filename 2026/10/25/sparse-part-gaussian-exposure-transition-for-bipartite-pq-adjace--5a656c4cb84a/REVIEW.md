# Scientific review: sparse-part Gaussian exposure transition

## Correctness — PASS

The proof begins with an exact maximization over the declared vertices of the PQ-type adjacency polytope. Ordinary Gaussian extreme-value normalization yields all candidate extrema. The critical exponent \(3-2\sqrt2\) equates the leading diagonal and cross-family maxima, while the explicitly derived logarithmic factor \((\log n)^{\sqrt2-1}\) cancels their second-order mismatch. Joint extreme-value independence uses the Gaussian two-coordinate bound for every distinct pair of standardized linear forms, with correlation at most \(1/\sqrt2\) among nonopposite forms. The radial normalization accounts for the correct intrinsic dimension \(2n-2\). Bounds from the diagonal term and the two cross terms give uniform integrability for the mean correction. Finite support, centering, and CDF checks are reproducible with `verify.py`; they are not substituted for the proof.

## Originality — PASS, with bibliographic qualification

Davis and Chen (arXiv:2007.11051, first public 2020-07-21) formulate PQ adjacency polytopes and analyze draconian sequences and normalized volumes. Ohsugi and Tsuchiya (arXiv:2103.15045) extend Ehrhart/volume calculations to complete multipartite graphs. Those known results do not imply a solid-angle phase transition or Gaussian second-order directional-width law. The closest accessible same-family PQ-polytope theorem was also inspected in full: it determines the Löwner ellipsoid for balanced complete bipartite graphs, rather than sparse-part random normal cones or directional widths. The probabilistic tools themselves are classical and no claim of novelty is made for Gaussian maxima. A possible equivalent masked-array extremal formulation outside the checked polytope literature remains a real residual risk; the checked material supplies no covering implication.

## Value — PASS

The full distribution of random Euclidean widths and the fraction of the sphere exposing diagonal versus cross vertices are natural geometric measurements of a fixed standard graph polytope, independent of Ehrhart or volume data. The result identifies a nontrivial critical exponent and a logarithmic critical window with a continuously varying angular exposure probability, plus an explicit five-Gumbel stochastic law. It distinguishes two competing families of vertices on an infinite, naturally parametrized sequence of graph polytopes.

## Scope and limitations

The theorem treats the intrinsic Euclidean realization, part-size power regimes, and the specified critical window. It gives no uniform finite-size convergence rate or independent external validation. Closest literature was evaluated by scientific implication, not by name similarity alone. Self-review correctness and originality assessments do not amount to independent mathematical certification.

Self-review: passed. Independent audit: not yet performed.
