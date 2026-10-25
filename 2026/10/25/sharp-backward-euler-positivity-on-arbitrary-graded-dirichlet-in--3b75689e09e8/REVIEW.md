# Scientific review

**Correctness — PASS.** The result is reconstructed with the exact nonuniform Dirichlet consistent-mass and stiffness entries. The positive-offdiagonal necessity uses an independently proved strictly positive nearest-neighbor entry and a signed tridiagonal-inverse ratio, rather than inferring necessity from the Stieltjes sufficiency theorem. Exact-rational experiments (618 configurations) verify sampled cases, while the proof covers all meshes and steps. The low-dimensional exceptions and equality boundary are stated explicitly.

**Originality — PASS, with literature residual risk.** Li--Huang (arXiv:1209.5657) Theorem 3.1 and Schatz--Thomée--Wahlbin (2010) Theorem 5.7 supply the corresponding sufficient condition, but neither inspected theorem states that any positive step below it necessarily produces a negative distance-two coefficient on *every* arbitrary nonuniform Dirichlet interval mesh. The 2010 paper's Theorem 5.5 concerns sufficiently small steps rather than an exact fixed-mesh boundary. Thomée--Wahlbin (2008) was accessible only in abstract, so specialized older coverage cannot be fully ruled out. Previous periodic special-mesh classifications do not imply the arbitrary graded Dirichlet statement.

**Value — PASS.** The classification is exact across all interior dimensions at least three and all positive graded intervals, isolates the exceptional one- and two-degree cases, and identifies the precise (and easily computed) forbidden range for positivity preservation. The boundary-cell independence and positive adjacent-entry principle are structural, with a plausible direct role in designing positive time steps.

**Scope and limits.** This is a homogeneous one-step matrix positivity theorem, not a complete discrete maximum principle for nonhomogeneous boundary/forcing data, variable diffusivity, or higher dimensions. Finite rational tests are supplementary; residual publication-priority risk remains.

Self-review: passed. Independent audit: not yet performed.
