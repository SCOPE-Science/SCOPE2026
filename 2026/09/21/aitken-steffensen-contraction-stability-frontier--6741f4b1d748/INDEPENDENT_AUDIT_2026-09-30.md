# Independent Audit — 2026/09/21/aitken-steffensen-contraction-stability-frontier--6741f4b1d748

- Audit date: 2026-09-30 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d26c0160eda51bb0fa37468df489e13ff9e0f17f`
- Disposition: **PASSED**

## Correctness

**PASS** — The normalized feasible-region optimization checks. With x*=0 and x=1, writing a=g(1), c=g(a), and t=(c-a)/(a-1) gives S(1)=(a-t)/(1-t), |a|<=q, |c|<=q|a|, and |t|<=q. Splitting a>0 and a<0 and optimizing the interval endpoints yields the global maximum W(q)=2q^2/((1-q)(1+2q)); the submitted piecewise-affine map attains it. Solving W(q)<=1 gives (1+sqrt(17))/8, and maximizing the same-evaluation ratio gives 16/9. Under monotonicity the feasible interval contracts and the exact maximum becomes q^2/(1-q^2), attained by the stated monotone piecewise-affine map. Independent dense feasible-pair searches at q=0.2,0.5,0.7,0.9 approached the closed forms from below, and exact witness substitution reproduces them.

## Originality

**PASS** — The closest classical sources were checked beyond abstracts. Johnson-Scholz (1968), Hofmann (1975), and Schneider (1981) were obtained through authorized institutional access after open-access searches and inspected in full; they prove local/semilocal convergence, monotone enclosure, or ordered-Banach-space results under divided-difference, convexity, and sign hypotheses, not the bare-global-Lipschitz minimax constants or thresholds here. Targeted searches found no exact 2q^2/((1-q)(1+2q)), q^2/(1-q^2), or 16/9 result. The novelty claim is therefore supported for the sharp black-box one-cycle frontier, not for Steffensen acceleration itself.

## Scientific value

**PASS** — The theorem gives a complete robustness benchmark under the weakest natural scalar contraction oracle: it quantifies when acceleration can enlarge error, shows two ordinary Picard evaluations are minimax-better under the same information, and identifies the exact improvement from monotonicity. This cleanly separates classical local acceleration from worst-case global robustness.

## Sources

- **On Steffensen's Method** — L. W. Johnson; D. R. Scholz. https://doi.org/10.1137/0705026 — Authorized full text checked, all 7 pages; gives convergence criteria for divided-difference Steffensen iterations, not the audited minimax frontier.
- **Monotonieeigenschaften des Steffensen-Verfahrens** — Wolf Hofmann. https://doi.org/10.1007/BF01834035 — Authorized full text checked, all 11 pages; studies monotone enclosure under slope-convexity/order hypotheses, not a global contraction worst-case factor.
- **Results about monotone convergence of Steffensen-like-methods** — Norbert Schneider. https://doi.org/10.1007/BF01941470 — Authorized full text checked, all 8 pages; gives ordered-Banach-space monotone enclosure and quadratic convergence conditions.
- **Acceleration methods for fixed-point iterations** — Yousef Saad. https://doi.org/10.1017/S0962492924000096 — Modern survey context for Aitken/Steffensen and acceleration methods.

## Limitations

- The theorem is scalar, real, exact-arithmetic, and one-cycle; it does not cover floating-point instability or vector acceleration.
- Crossing the nonexpansion threshold does not imply long-run divergence of restarted Steffensen.
- The result assumes only a global contraction; smoother maps may have much stronger local behavior.
- Older literature under different notation remains a residual priority risk despite full checks of the most directly relevant classical papers.

## Independent checks

```json
{
  "normalized_feasible_region_rederived": true,
  "sharp_piecewise_affine_witness_checked": true,
  "threshold_and_16_over_9_algebra_checked": true,
  "monotone_frontier_rederived": true,
  "dense_numeric_q_values": [
    0.2,
    0.5,
    0.7,
    0.9
  ],
  "open_access_first": true,
  "oxford_used": true,
  "oxford_jobs": {
    "johnson_scholz_1968": {
      "job_id": "c47a8cac0125f1c4f615e8fecc15bbcb",
      "status": "complete",
      "pages": "1-7 of 7"
    },
    "hofmann_1975": {
      "job_id": "67f2ad565a89036f761dd77a113727ce",
      "status": "complete",
      "pages": "1-11 of 11"
    },
    "schneider_1981": {
      "job_id": "2090b99d7971f2340364c63ebc69b2e8",
      "status": "complete",
      "pages": "1-8 of 8"
    }
  }
}
```

GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. Open-access/preprint sources were checked before authorized institutional retrieval. Inaccessible material is explicitly identified and is not claimed read.
