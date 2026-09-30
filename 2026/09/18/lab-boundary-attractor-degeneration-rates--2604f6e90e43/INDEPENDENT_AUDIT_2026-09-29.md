# Independent audit — 2026-09-29

**Record:** `2026/09/18/lab-boundary-attractor-degeneration-rates--2604f6e90e43`  
**Title:** Boundary attractors and exact degeneration rates for largest-dihedral-angle bisection  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `5820ab12919824bcb28a7167b6a02094e4921e34`  
**Disposition:** **PASSED**

## Correctness

**PASS** — The dynamical refinement checks. Setting b=0 in the exact recurrence gives the cubic 2cτ^3−3τ^2+1=0; for c>1/√2 it has a unique root τ∈(1/√2,c). Differentiation at that root gives the universal transverse multiplier −1/2. The b-dependence enters at order b^2, so the stable forced recurrence yields b_n=Cτ^n and (t_n−τ)/b_n^2→g/(τ^2+1/2), which is the filed K(c). The volume, diameter, inradius, and angle asymptotics follow from the coordinates; symbolic substitution verifies the limiting angle-doubling identity.

## Originality

**PASS** — Korotov–Michaud supply the c=7/8 recurrence, invariant rectangle, and coarse geometric bounds. The located source metadata and searches do not state the boundary fixed point, exact cubic rate, universal −1/2 multiplier, second-order law, general c-family, continuum of rates, or angle-doubling equilibrium. The contribution is therefore a genuine asymptotic analysis of their new recurrence, with the usual near-simultaneous-work caveat.

## Scientific value

**PASS** — The record converts a qualitative/coarse degeneration counterexample into an explicit attracting boundary dynamics with exact exponential rate and limiting geometry, and shows a continuum of realizable degeneration factors. That substantially sharpens the numerical-analysis interpretation of the LAB failure mode.

## Findings

- The map c(τ)=(3τ^2−1)/(2τ^3) is strictly increasing on (1/√2,1), giving exact multipliers 1/τ throughout (1,√2).
- The second-order coefficient follows from δ_{n+1}=−δ_n/2+g b_n^2+o(|δ_n|+b_n^2) and b_{n+1}^2/b_n^2→τ^2.
- For c=7/8, independent high-precision iteration reproduces τ≈0.7835533375134631 and 1/τ≈1.276237305265537.
- The asymptotic inradius and diameter-to-inradius growth formulas are consistent with the exact tetrahedral coordinate formulas.

## Independent checks

- Independently differentiated the recurrence and re-derived the fixed-point polynomial and second-order balance.
- Recomputed the coordinate volume and diameter asymptotics.
- Ran symbolic/high-precision checks against the public verification artifact formulas.
- Compared current searches with Korotov–Michaud and longest-edge-bisection dynamical literature.

## Sources

- https://arxiv.org/abs/2609.18788 — Korotov–Michaud source of the LAB counterexample and exact recurrence.
- https://arxiv.org/abs/2609.08846 — Related longest-edge-bisection dynamical work using a different refinement rule.
- https://doi.org/10.21136/AM.2026.0277-25 — Earlier tetrahedral longest-edge-bisection orbit context.

## Limitations

- The theorem is local to the structured invariant family and does not establish an open basin in the full tetrahedral shape space.
- The c=1/√2 threshold is for this boundary-fixed-point mechanism, not a global classification of LAB dynamics.
- The motivating source is extremely recent, leaving a near-simultaneous-work risk.

This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
