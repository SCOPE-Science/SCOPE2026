# Scientific review

## Correctness — PASS

The object is the unit-rate reflecting path generator and the claim covers every integer path size at every nonnegative step. The exact RK4 stability polynomial yields the nonnegative uniformization interval. A four-vertex walk count proves the sharp obstruction for all larger paths, and explicit rational formulas close the small-size cases. Positive definiteness of the scalar RK4 polynomial on the negative real axis rules out diagonal obstructions. The accompanying exact arithmetic verifier passed 40,497 assertions. Root uniqueness is proved analytically, not inferred from a solver.

## Originality — PASS, subject to documented risk

The 2021 source arXiv:2102.08242 treats graph-Laplacian integrators and RK4 without the exact reflecting-path classification; the 2014 SSP literature gives universal convex-combination guarantees rather than these sharp graph-specific limits. Horváth (1998) explicitly establishes zero universal positivity radius for classical RK4 (Example 1), and Horváth (2005) gives universal problem-class restrictions and invariant subcones, including Dirichlet discretizations, without the reflecting-path entrywise threshold. The earlier directed-cycle classification does cover exactly the two-vertex root as a known component. For three or more vertices, that work concerns different nonsymmetric one-way generators, not the degree-one reflecting path endpoints. Novelty attaches to the complete reflecting-path transition, not the already known two-state special case. The specific all-size path theorem and degree-sum mechanism were not covered by the inspected primary material or by claim-level overlap searches. The 2022 heat-scheme paper was fully inspected and does not analyze this classical RK4 path problem; a 2026 heat-scheme preprint remains inaccessible in full and poses residual historical-priority risk.

## Value — PASS

The precise positivity CFL limit is a physically motivated numerical question for diffusion solvers, separate from spectral stability. The complete classification across arbitrary grid size captures finite boundary effects and the first onset of an interior four-site obstruction. The perhaps counterintuitive result that a fourth-order step shares forward Euler's positivity ceiling on every path of at least six sites is a structural design benchmark, not an arbitrary parameter slice. No claim is made about higher-order accuracy requiring nonnegative intermediate stages or about other discretizations.

## Closest literature and limitations

Blanes–Iserles–Macnamara (2021), Gottlieb–Grant–Higgs (2014), Horváth (1998, 2005), Omle–Askar–Kovács (2022), and Coquerelle (2026) were compared with attention to exact operator, boundary condition, and conclusion. The first five studies were fully inspected; the 2026 preprint was accessible only through bibliographic information and summaries. Detailed source comparisons appear in the structured review. The scientific result is limited to the classical RK4 end-step on exact unit-rate symmetric path generators.

Self-review: passed. Independent audit: not yet performed.
