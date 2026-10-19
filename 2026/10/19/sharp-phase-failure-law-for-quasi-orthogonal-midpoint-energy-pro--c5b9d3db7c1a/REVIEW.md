# Scientific assessment

## Correctness — PASS

For the strictly convex energy \(E(q)=q^\mathsf{T}\operatorname{diag}(1,\kappa^2)q\), the vector field \(A=\bigl(\begin{smallmatrix}0&\kappa^2\\-1&0\end{smallmatrix}\bigr)\) is exactly energy preserving. The two explicit-midpoint stage derivatives span the full plane for every nonzero start and every positive step; therefore the correction direction is precisely the full energy gradient. Completing a one-variable positive quadratic gives the exact minimum on the correction line and is sufficient to decide real-root existence, with no hidden small-step approximation.

The sharp phase threshold comes from an attained, unique maximum of a rational function on the full unit interval. The probability calculation is an exact arcsine-density integral because the predictor acts as a scaled rotation on energy coordinates; the square-root onset and inverse-square survival tail follow from explicit polynomial-root asymptotics. The standalone standard-library verifier passed 6,563 exact or numerical assertions. In particular the explicit rational witness has minimum energy \(9801/1945>2\), so there is no real correction root. No finite computation is used as a substitute for a universal proof.

## Originality — PASS, with priority uncertainty

The primary 2024 article by Najafian and Vermeire defines the prescribed stage-projected-gradient method and proves local small-step solvability for convex invariants (Theorem 3); Remark 4 identifies the full-stage-span case with orthogonal projection. The inspected mathematical portions do not state the present finite-step phase-failure law. The 2006 Calvo et al. work addresses projection methods with different chosen directions; its accessible journal abstract does not itself resolve the probability law.

The universal worst-angle factor \(((r-1)/(r+1))^2\) is a classical steepest-descent/Kantorovich fact, **not** claimed as a separately novel inequality. The item of interest is the exact fraction of energy phases for which the designated Runge--Kutta correction has *no real root*, together with the sharp onset and large-step asymptotics. The literature comparison included the general exact-line-search worst-case work of de Klerk, Glineur and Taylor (2017), whose public abstract concerns worst-case contraction rather than a phase law for an energy-projection equation. Relevant mathematical-record searches found no direct covering statement, but absence from search is not a novelty certificate. A historical exact distribution of two-eigenvalue steepest-descent contraction, or material in uninspected sections of a later journal version, could diminish priority; this is explicitly an unresolved risk rather than a claim of exhaustive coverage.

## Value — PASS

The result answers a natural operational question about an invariant-preserving numerical scheme: when can its nonlinear correction subsolve be guaranteed to admit a real solution at a **fixed step**? It proves a sharp parameter boundary for every starting phase and computes the fraction of phases that fail when this guarantee is lost. The square-root onset gives a quantitative boundary singularity, while the inverse-square large-step success law shows that inability to correct becomes typical, not an isolated contrived state. It distinguishes failure of a selected projection line from failure of the convex invariant manifold itself and respects the original small-step convergence theorem.

## Closest literature and limitations

- Najafian--Vermeire, arXiv:2409.18328v1, equations (2.5), Theorem 3, Remark 4: local solvability; no verified global phase-failure law in the inspected sections.
- Calvo--Hernández-Abreu--Montijano--Rández, SIAM J. Sci. Comput. 28 (2006), 868–885, DOI 10.1137/04061979X: invariant-projection setting; different directional construction and abstract-only access for that source.
- de Klerk--Glineur--Taylor, Optimization Letters 11 (2017), 1185–1199, DOI 10.1007/s11590-016-1087-4: general sharp worst-case gradient-line-search contraction; not evidence that the full phase measure was previously derived.

Only one midpoint step, exact arithmetic, a planar oscillator and a uniform energy-angle law are covered. Large-step feasibility for other invariant projectors, joint invariants, numerical root finders and full trajectories remains unproved. The sharp worst-case inequality is classical, and the status of any analogous probabilistic formulas outside the searched sources remains a priority risk.

Self-review: passed. Independent audit: not yet performed.
