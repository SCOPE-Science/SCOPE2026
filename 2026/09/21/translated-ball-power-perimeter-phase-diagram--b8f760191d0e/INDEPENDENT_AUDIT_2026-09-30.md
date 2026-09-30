# Independent audit — 2026-09-30

**Record:** `2026/09/21/translated-ball-power-perimeter-phase-diagram--b8f760191d0e`  
**Audited repository:** `SCOPE-Science/SCOPE2026`  
**Audited current commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Assigned/current source tree SHA:** `56db5617564bb36bc41cfe9310be3c6f3318a39e`  
**Disposition:** passed

The assignment snapshot remains current for this record: comparison from the dispatcher's source-tree-checked commit to current `main` showed no changed file under the assigned record path. The dated independent-audit targets were separately verified absent, and the current `VERIFICATION.md` blob guard was verified before staging this change-set.

## Correctness — PASS

PASS. For 0<t<1, differentiation under the spherical average gives (t^(n-1)Phi')'=p(p+n-2)t^(n-1)Phi_{p-2}; positivity of Phi_{p-2} and the radial condition at t=0 give exactly the claimed interior sign. For t>1, t+theta_1>0 pointwise, so Phi' has the sign of p. At p=2-n the interior profile is constant and Newton's shell theorem gives the exterior value t^(2-n). At t=1, the first-coordinate density reduces the integral to a beta integral, with integrability exactly p>1-n and the displayed gamma-function value. Independent numerical quadrature for (n,p)=(3,-1/2),(4,-1),(5,1.2) matched the closed formula to numerical precision. The one-sided divergence for p<=1-n follows from the nonnegative singular kernel and Fatou's lemma. These ingredients yield all five monotonicity regimes and the unique maximum for 1-n<p<2-n.

## Originality — PASS

PASS, narrowly scoped. Csató (2018) is the directly relevant weighted-isoperimetric antecedent and studies the |x|^p perimeter, including translation variations and the sign change associated with p=2-n. The harmonic/Newton-shell identity at p=2-n and the spherical-mean differential identity are classical and are not new. The 2026 Csató--Giovagnoli--Roy preprint again studies weighted perimeters and translation-based arguments in a broader convex-optimization setting. I did not locate in either source or in targeted spherical-mean/Riesz-kernel searches the combined all-p global translated-ball monotonicity phase diagram, the touching integrability threshold p=1-n, and the stable-but-not-global interpretation as one theorem. Because the proof is an elementary synthesis of classical potential theory, an equivalent result under purely potential-theoretic terminology remains a material priority risk.

## Scientific value — PASS

PASS, moderate. The contribution is not a new potential-theory identity, but it organizes the complete one-parameter translation behavior of a weighted perimeter into a sharp global phase diagram, identifies the entire critical flat family, and separates translation instability from genuinely non-ball competitors in the delicate 1-n<p<2-n range. This is useful clarification for the weighted-isoperimetric literature.

## Independent checks

- Re-derived the radial Laplacian identity and sign table for all p regimes.
- Re-derived the exterior derivative sign directly from t+theta_1>0.
- Rechecked the Newton-shell critical profile and the beta-integral touching formula.
- Numerically compared the closed touching formula with direct quadrature at three dimensions/exponents spanning negative and positive cases.

## Literature evidence

- https://doi.org/10.3934/cpaa.2018129 — Csató (2018), weighted isoperimetric problem with perimeter density |x|^p.
- https://arxiv.org/abs/1706.09619 — Open preprint of Csató (2018).
- https://arxiv.org/abs/2608.19851 — Csató, Giovagnoli and Roy (2026), weighted perimeter/moment optimization with translation arguments.

## Access notes

- No restricted full-text claim was needed beyond the sources described above.

## Limitations

- The result classifies only translations of a fixed Euclidean ball, not arbitrary shape deformations.
- The p=2-n flat profile is a direct classical Newton-shell phenomenon; originality is only in the combined perimeter phase diagram and interpretation.
- Potential-theory literature under different spherical-mean or Riesz-kernel terminology could contain an equivalent formulation.

No GitHub write was performed by the audit chat. This file is staged only by the guarded `scope-audit-change-set-v1` publication plan.
