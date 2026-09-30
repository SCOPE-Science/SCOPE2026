# Independent Audit — Hermite–Hellmann–Feynman extrapolation for constrained eigenvalue penalties

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `a54c4012db41eab644b6f3abe329d395214d4a90`  
**Audited current source tree:** `a54c4012db41eab644b6f3abe329d395214d4a90`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree is unchanged from the assigned source tree. GitHub was used only as read-only evidence, and the dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. In a range/null-space orthogonal block basis, the large-penalty eigenvalue equation reduces by Schur complement to an analytic matrix pencil in t=1/rho. Simplicity of the constrained eigenvalue gives an analytic branch F(t) through t=0. The displayed expansion D-tG+t^2J+O(t^3) and the second-order simple-eigenvalue coefficient have the correct signs. Hellmann–Feynman gives f'(rho)=||Ax_rho||^2 and the chain rule gives F'(1/rho)=-rho^2 f'(rho). Hermite interpolation at q shrinking nodes therefore has a remainder proportional to prod_j t_j^2 and gives O(rho^(-2q)). Solving the two-node confluent system independently yields exactly 5f(rho)-4f(2rho)+rho f'(rho)+8rho f'(2rho). Recomputing the record's numerical example gives the stated c and d and a nonzero rho^4-scaled Hermite error tending near 8.1e-2, confirming genuine fourth order.

## Originality — PASS

PASS, narrowly scoped. The motivating Wang–Xia preprint publicly advertises the exact penalty representation, a first-order asymptotic error expansion with an explicit leading coefficient, and Hellmann–Feynman sensitivity. Hermite interpolation, Richardson extrapolation, analytic simple-eigenvalue perturbation, and derivative-assisted extrapolation as generic techniques are classical and receive no novelty credit. Targeted searches did not locate the source-specific combination of the analytic inverse-penalty branch with q value/derivative samples giving the 2q-order rule or the closed two-level fourth-order formula. The older structural-penalty literature visibly establishes convergence/bracketing, but no accessible statement located in this audit subsumes the submitted Hermite–HF result.

## Scientific value — PASS

PASS. The theorem turns sensitivity information already available from each penalized eigenpair into a rigorously higher-order scalar extrapolant. In the two-level case it raises the asymptotic order from the source's value-only second order to fourth order without an additional eigenpair solve, materially reducing the penalty scale needed for a target scalar error when the leading coefficients are nonzero. This is useful even though no backward-stability, multiple-eigenvalue, or eigensolver-complexity theorem is claimed.

## Independent checks

- Re-derived the Schur-complement analytic branch and the first two inverse-penalty coefficients under the simple constrained-eigenvalue hypothesis.
- Solved the two-node Hermite system independently and recovered the exact coefficients in the displayed two-level formula.
- Recomputed the supplied 5-by-5 example: c=0.5485714285714287 and d=-0.102639455782313, with rho^4-scaled fourth-order error remaining nonzero.
- Compared the claim with the current public statement of Wang–Xia arXiv:2609.18538 and with older structural penalty/constrained-Rayleigh literature.
- Searched the SCOPE repository for overlapping Hermite/Hellmann–Feynman constrained-eigenvalue records; none was found.
- Verified the assigned record was unchanged from the dispatcher source-check commit to current main and that the 2026-09-30 audit markers are absent.

## Limitations

- The theorem assumes a simple constrained eigenvalue and sufficiently large positive penalty in the non-finitely-exact regime.
- Generic Hermite/Richardson extrapolation and the Hellmann–Feynman theorem are prior art; originality is only in this constrained-eigenvalue synthesis and its exact formulas.
- The full text of every older structural-penalty paper was not exhaustively inspected, so specialized equivalent higher-order asymptotics remain a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.18538
- https://doi.org/10.1002/nme.2247
- https://doi.org/10.4208/csiam-am.2021.nla.01
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/19/hellmann-feynman-hermite-penalty-extrapolation--b0d1ece5e105

This change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
