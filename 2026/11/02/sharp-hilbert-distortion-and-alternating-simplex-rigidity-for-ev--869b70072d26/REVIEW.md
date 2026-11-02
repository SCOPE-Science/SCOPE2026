# Scientific review

## Correctness

**PASS.** The centroid identity on either of the two distance-two alternating rim sets gives the dimension-free bound \(c_2^2\ge2-2/m\); equality forces all hub distances to saturate and both parity sets to be centered regular simplices. The proposed rational Gram matrix has diagonal blocks \(2I-2J/m\) and explicitly defined cross blocks. Fourier diagonalization gives nonzero-mode eigenvalues \(2\pm2u(1+4(1-u^2)/m)\), which are positive for \(m\ge8\) by monotonicity and for \(m=7\) by a rational cosine bound. All metric pair classes meet the sharp distortion inequalities. The exact rational checker, run on `check_wheel.py`, passed 12 orders and all corresponding pairs. The proof, not enumeration, establishes the infinite family. Unproved: smaller orders and the minimal dimension of an optimal embedding.

## Originality

**PASS, with priority risk.** Full-text sections of Balaji–Bapat–Goel's wheel distance-matrix paper (arXiv:2006.03289) concern a distance-matrix pseudoinverse and the square-root-metric Hilbert representation, not sharp Euclidean distortion of the original wheel metric. Vallentin (arXiv:math/0509716) and Cioabă–Gupta–Ihringer–Kurihara (arXiv:2109.09708) analyze distance-regular graph embeddings, whereas the wheel is nonregular. General shortest-path decomposition bounds (arXiv:1708.04073) do not imply the finite-size constant. The closest accessible research records concern wheel symmetric-edge-polytope inradii/ellipsoids, circulation projection constants, and snowflake negative type; these are different invariants. Exact aliases, graph joins, and possible implied stronger formulas were searched. An overlooked wheel-specific embedding computation remains a residual historical-priority risk; no claim of exhaustive literature coverage is made.

## Mathematical value

**PASS.** This gives an exact distortion law across an infinite, natural nonregular planar graph family, with a genuine \(1/m\) correction below the generic \(\sqrt2\) snowflake-based upper bound. The dimension-free obstruction has an **all-optimizer rigidity** conclusion, and the matching constructive Gram certificate is explicitly positive semidefinite in every dimension covered. These geometric facts are not simply a distance-matrix inverse, a finite experiment, or a substitution into a distance-regular theorem. The result may guide exact distortion analysis of other apexed graphs; no downstream theorem is asserted.

The finite checks were performed only for explicitly stated sizes. No external independent mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
