# Scientific review: linearized inertia of balanced Stuart–Landau polygons

## Correctness — PASS

The stated normalization is exact: in the frame rotating with the common frequency, the linearized map at an all-active balanced polygon is the symmetric matrix induced by \(c\|Tv\|^2-2\kappa\|Uv\|^2\). For a noncollinear polygon, tangential directions make \(T|_{\ker U}\) surjective. This produces a two-dimensional positive subspace, while arbitrary radial projections can be realized inside \(\ker T\), giving an \(M\)-dimensional negative subspace. The two rank bounds prove these are the complete positive and negative indices, and the submersion theorem identifies exactly \(M-2\) geometric zeros. At a collinear configuration, longitudinal and transverse coordinates split the Jacobian into explicit rank-one updates. Sylvester congruence produces the exact \(\tau\)-trichotomy, including the equality case. This proof covers every permitted size and parameter without numerical extrapolation. The standard-library verifier independently checked 3,504 exact-rational assertions; finite tests remain supplementary.

## Originality — PASS with stated priority risk

Zhao and Uchida, arXiv:2610.08239v1, derive the model, the gradient structure under purely real coupling, and the polygonal equilibrium family. Their Sections 3 and 5 do not state the complete inertia and singular collinear threshold; their polygon transverse-stability analysis uses numerical shape sampling with generally reactive coupling. Kemeth and collaborators, arXiv:1807.11231v2, treat homogeneous splay and cluster stability, not the all-active arbitrary-heterogeneity polygon census. Ku, Girvan and Ott, arXiv:1412.3803v1, treat related incoherent and clumped states without the result. Comparison against published research-search records identified nearby Stuart–Landau phase-reduction and cluster results but not the present all-geometry signature theorem. The gradient representation is acknowledged prior art; the claimed result is the exact geometry-independent noncollinear inertia plus the collinear phase boundary. The residual possibility of an earlier equivalent spectral argument in specialized literature remains.

## Mathematical value — PASS

The claim supplies a uniform stability-index classification for an entire family of stationary configurations singled out in recent amplitude-inclusive oscillator research. An exact count of *all* expanding, contracting and neutral modes is stronger than the easy observation that balanced configurations can be unstable. The special collinear configurations have a nontrivial, sharp parameter threshold not visible from the generic polygon dimension alone. The example of four identical oscillators locates an explicit change in unstable dimension at \(c=\beta/6\). These statements delimit the purely dissipative case and clarify why reactive coupling matters when seeking stable balanced cycles. No global-basin or nonlinear-bifurcation result is claimed.

## Scientific limitations and independent status

All oscillators must be active and the coupling must be strictly positive and real. The theorem does not cover reactive coupling, Kerr-type terms, inactive sites, nonlinear stability at the collinear zero-eigenvalue boundary, or a complete classification of all equilibria. Priority relative to inaccessible or unindexed older work cannot be ruled out. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
