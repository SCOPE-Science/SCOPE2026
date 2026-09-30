# Independent Audit — 2026/09/17/degenerate-porous-neumann-steady-patterns--5a1b4944a368

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `58853cd5901ce2a4fe574c753720dd0299b37cb0`
- Disposition: **PASSED**

## Correctness

**PASS** — The proportional reduction and spatial-dynamics proof check exactly. Under the two balance identities, substituting V=alpha U makes the second stationary residual alpha^2 times the first. With p=U U_x, the scalar equation has first integral H=p^2/2-F(U), U_- is a center and U_+ a saddle, and the small-amplitude half-period tends to L_c=pi sqrt(U_/[b(U_+-U_-)]). When r=U_-/U_+>1/2, F(U_+)=b U_+^4(2r-1)/12>0 and the saddle-energy factorization has a second positive turning point below U_-, so the entire period annulus remains in U>0. Its half-period varies continuously from L_c to infinity, giving a Neumann profile for every L>L_c and m-fold profiles when L/m>L_c. For the concrete alpha=3 example, the roots 1/2 and 2/3, L_c=pi, both dispersion factorizations, the positive homoclinic turning point, and the Poincare-Lindstedt coefficient 182/3 all check algebraically.

## Originality

**PASS** — Cherniha-Kriukova explicitly state that their stability analysis is spatially homogeneous and that searching for nonconstant steady states satisfying zero Neumann conditions lies beyond the scope of their study. Their paper does use the proportional equilibrium relation to construct two homogeneous nodes, but it does not derive the stationary proportional ODE, the all-L>L_c period-annulus theorem, the perfect-square dispersion law, or the branch-direction calculation in this record. Searches of the nearby degenerate-diffusion predator-prey literature found related pattern/bifurcation theory for different systems, not this exact reduction.

## Scientific value

**PASS** — The result fills a gap explicitly identified by the source paper and exhibits a nonlinear steady-pattern mechanism that is invisible to ordinary Turing-band reasoning: the lower homogeneous state is stable except at an isolated double neutral wavenumber, yet positive stationary patterns exist for every sufficiently long Neumann interval. The sharp length threshold, multiplicity-by-half-wave count and exact branch direction provide concrete structure for subsequent temporal-stability and bifurcation analysis.

## Sources

- A Reaction-Diffusion System with Nonconstant Diffusion Coefficients: Exact and Numerical Solutions (Roman Cherniha; Galyna Kriukova): https://doi.org/10.3390/axioms14090655 — Open-access primary source; it explicitly says the search and analysis of nonconstant zero-Neumann steady states are beyond its scope.
- A reaction-diffusion system with nonconstant diffusion coefficients: exact and numerical solutions (Roman Cherniha; Galyna Kriukova): https://arxiv.org/abs/2608.11172 — ArXiv version of the same source and model.

## Limitations

- The theorem is one-dimensional and concerns stationary pure-Neumann profiles only.
- Temporal stability of the new profiles is not proved.
- The proportional family is not claimed to classify all nonconstant steady states.
- The all-length theorem uses U_->U_+/2 to keep the outer periodic/homoclinic geometry strictly positive.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first. Oxford Download was used only where version-specific or full-text source verification remained unavailable through the open-access retrieval path.
