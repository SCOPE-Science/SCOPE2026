# Scientific review: two-view Fourier tomography of finite-field conics

## Correctness — PASS

For every odd prime power, the argument defines a split or nonsplit quadratic étale algebra and the cyclic norm-one group, thereby treating \(q\equiv1\) and \(q\equiv3\pmod4\) uniformly. Directional Fourier inversion is equivalent to vanishing fibre sums. Nonisotropic projection fibres are the orbits of the explicit involutions \(z\mapsto a_u z^{-1}\), and two such involutions generate a rotation subgroup. The quotient involution has exactly zero, one or two fixed cosets according to the stated parity/quadratic-character conditions; counting its two-cycles proves the complete kernel basis and exact nullity. The bijection of nonisotropic projective directions with the norm-one torus and multiplicative orders then gives the totient pair count. Isotropic directions are individually injective by the split-torus parametrization. Exact modular incidence ranks independently match all 1,914 tested two-view pairs over ten fields, including three nonprime examples. The proof is uniform; the tests are finite corroboration only.

## Originality — PASS, qualified by literature coverage

Koh's arXiv:1209.1215v1 states sharp endpoint norm bounds for the full finite-field X-ray/Radon operators, not the nullspace or arithmetic rank of two *fixed* frequency-line measurements on a conic. Chandra and Svalbe's 2014 full article develops number-theoretic projection slices and full-image reconstruction using enough directions, not a two-direction finite-field conic classification. Iosevich, Mayeli and Pakianathan's arXiv:1505.00883v1 characterizes exponential orthogonality and translational tiling of finite-plane subsets, a different requirement from arbitrary weighted conic reconstruction. A previously established general two-projection bipartite-cycle criterion is compatible with the proof, but does not by itself evaluate the rotation order, quadratic-character fixed-point obstruction, and exact totient enumeration for this geometric family. An equivalent historical treatment in finite-field norm-one torus or discrete tomography literature is a residual priority risk. Independent historical certification is not claimed.

## Mathematical value — PASS

The unit conic is a canonical finite-field homogeneous curve whose split/nonsplit arithmetic is nontrivial. Fourier sampling along projective lines is a natural sparse-view acquisition model. The result gives the exact kernel and all ambiguity spaces for **every** pair, a closed arithmetic count of the identifiable pairs, and a sharp one-versus-two-direction threshold, rather than an isolated rank computation or a routine Fourier-inversion restatement. The restrictions (all frequencies per line, unrestricted complex weights, no numerical stability assertion) are explicit.

## Limitations

The proof does not quantify noisy recovery or extend to arbitrary curves. Reproduction covers finite fields of sizes \(3,5,7,9,11,13,17,19,25,49\) only; no finite census proves the infinite theorem. An independently conducted novelty search and an external proof audit remain outstanding.

Same-model review: passed. Independent audit: not yet performed.
