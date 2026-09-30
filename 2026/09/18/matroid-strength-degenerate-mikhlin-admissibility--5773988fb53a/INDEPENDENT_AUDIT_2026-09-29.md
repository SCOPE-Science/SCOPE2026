# Independent audit — 2026-09-29

Record: `2026/09/18/matroid-strength-degenerate-mikhlin-admissibility--5773988fb53a`  
Assigned and audited source tree: `fa5a3e29ffef64f93809690a10051e1b58884b9a`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The polyhedral reduction is correct. Vandanjon's good k-directions are precisely the bases of the row matroid of the coordinate restrictions, so the possible marginal load vectors are the matroid base polytope; intersecting with 0<alpha_e<1/2 gives Xi exactly. The fractional base-packing theorem identifies the reciprocal of the minimum possible maximum marginal with min_D |D|/(k-r(E\D)), proving Xi nonempty iff the stated strength exceeds 2; a small mixture with a full-support base distribution supplies strict positivity. The capacity criterion is also correct: a base x with x_e<c_e exists exactly when c(E\S)>k-r(S) for every rank-deficient S. The strict inequalities permit a common shrink factor, Edmonds' box-intersection criterion supplies a base under the shrunken capacities, and a sufficiently small full-support mixture preserves all strict upper bounds. Closure of S shows that proper flats suffice.

## Originality

**qualified_supported**. Vandanjon's September 2026 preprint provides the degenerate multiplier theorem and its geometric admissibility set, while Edmonds' base-polytope/box-intersection theory and fractional base packing are classical prior work. Searches did not locate the exact identification of Xi with a clipped base polytope, the strength >2 characterization, or the complete rank-inequality elimination of the exponent parameter for this multiplier problem. The contribution is therefore a new synthesis/application of standard matroid optimization machinery, not a new matroid theorem.

## Scientific value

**meaningful_exact_characterization**. The result replaces several sufficient geometric tests and case analyses by an exact all-dimensional criterion and makes exponent feasibility algorithmically checkable from a rank oracle. It materially clarifies the scope of the source theorem while correctly stopping short of claiming multiplier unboundedness when the criterion fails.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/matroid-strength-degenerate-mikhlin-admissibility--5773988fb53a
- https://arxiv.org/abs/2609.18818
- https://doi.org/10.1007/s10107-024-02116-w
- https://doi.org/10.4230/LIPIcs.ESA.2026.57

## Limitations

- The result characterizes only the Xi-based geometric/exponent hypothesis of Vandanjon's theorem; it does not replace the analytic time-frequency argument.
- Failure of the matroid inequalities does not imply that the corresponding multiplier is unbounded.
- The source preprint is extremely recent, so contemporaneous unindexed reformulations remain an originality risk.
