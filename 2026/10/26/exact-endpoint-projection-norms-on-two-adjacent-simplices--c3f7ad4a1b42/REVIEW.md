# Independent mathematical audit

## correctness

PASS

For positive volume fractions q and 1−q, multiply the nodal mass matrix by (d+1)(d+2). The shared-facet block is I+J, its columns to the tips are q·1 and (1−q)·1, and the tip block is diag(2q,2(1−q)). Eliminating the tips leaves I+J/2, whose inverse is I−J/(d+2); block substitution recovers the recorded facet and both tip representers. The row norm is maximal at some node because each evaluation row on a simplex is a convex combination of its nodal rows. The sign of a maximizing row attains the bound on real or complex L∞, and continuous functions K_v/(|K_v|+ε) approach it; the nodal value is also an essential-supremum lower bound by continuity and the nondegenerate incident simplex. Each affine row depends on one barycentric coordinate per element. Integrating against d(1−u)^(d−1) gives S_d=N_d(1) at shared nodes and N_d(q), N_d(1−q) at the tips. With m=d+1 and b=d/(d+2), the derivative equals (m+1)b[(q−1)(1+bq)^(m−1)/(1+q)^m−b^(m−1)]<0. This gives exactly the claimed nodal maximizers, balanced minimum, and unattained limit at q=0; varying heights over a common facet realizes all positive ratios. The calculation depends only on volumes, and exact substitution gives 49/18 and 7/2 in dimension two.

## originality

PASS

The known one-simplex projector gives exactly the shared-facet row and is credited, but not the two coupled tip rows. The closest exact spline result concerns a periodic one-dimensional mesh, while the same-endpoint finite-element literature inspected establishes stability under grading, not this exact volume-ratio profile and equality characterization. No equivalent exact pair profile was located in these bounded comparisons.

## value

PASS

This is the smallest conforming multidimensional mesh that couples elements across a facet. The exact profile distinguishes balanced and collapsing-volume shapes and identifies precisely which nodal tests control the sharp endpoint constant, even without bounded aspect ratios. The mixed tip kernel and its strict extremal ordering are not a local projection calculation alone and are useful as sharp stability benchmarks for conforming P1 elements.

The dated certificate retains the supplied scientific assessment, sources and limitations.
