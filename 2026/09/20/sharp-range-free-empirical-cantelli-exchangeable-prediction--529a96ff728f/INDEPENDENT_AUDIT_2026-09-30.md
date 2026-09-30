# Independent audit — 2026-09-30

**Record:** `2026/09/20/sharp-range-free-empirical-cantelli-exchangeable-prediction--529a96ff728f`  
**Audited source tree:** `eb517b462e2e4e8193cb03322a9c3c787bbd4d9a`  
**Disposition:** passed

## Correctness — PASS

PASS. For a deterministic vector of length M=n+1, I independently derived the leave-one-out identity T_i^2=M(M-2)u_i^2/((M-1)(M-1-u_i^2)) and the threshold u_i>=nt/sqrt(n^2-1+nt^2). The centered unit-second-moment vector then satisfies the sharp finite Cantelli count bound r<=M/(1+a^2), with floor/ceiling giving the inclusive/strict staircases. Exchangeability turns this deterministic count into the claimed probability bound. The two-level orbit construction saturates it: for r high coordinates, T_high^2=(M-2)(M-r)/((M-1)(r-1)), with the r=1 zero-training-variance endpoint handled by the stated extended convention. I tested multiple n and t values, including the n=20 example, and the exact integer staircase matched. The isolated nu_i/u_i notation slip in the proof is cosmetic and does not alter the mathematics.

## Originality — PASS

PASS, with one inaccessible historical comparison recorded. Troffaes and Basu (2019) explicitly formulate a one-sided empirical Cantelli bound with a range-dependent offset and state that they had not found a way to remove that offset; their deterministic one-sided counting lemma is correctly credited. The present leave-one-out transformation removes the range term and yields an exact attainable finite-sample staircase for the externally studentized prediction residual. Saw--Yang--Mo gives the earlier empirical Chebyshev line. I attempted the 1987 Konijn article after open-access routes failed; authorized institutional retrieval found no verified PDF, so I do not claim to have read that full text. Its inaccessibility is a residual originality risk but not enough to overturn the direct 2019 evidence that the no-offset Cantelli form remained unresolved there.

## Scientific value — PASS

PASS. This is an exact, distribution-free, finite-sample prediction theorem under exchangeability alone, with explicit extremizers and no population moments or range bound. The sharp integer staircase and p-box are practically interpretable and strengthen the prior bounded-range one-sided result.

## Independent checks

- Re-derived the externally studentized/full-sample-standardized algebra.
- Reproved the finite-vector Cantelli count inequality including strict versus inclusive integer rounding.
- Checked the two-level extremizer formula over multiple finite n and t values.
- Attempted lawful full-text retrieval of Konijn (1987) after open-access routes failed; no verified PDF was available.

## Literature evidence

- https://doi.org/10.1080/00031305.1984.10483182 — Saw, Yang and Mo (1984), empirical Chebyshev inequality with estimated mean and variance.
- https://proceedings.mlr.press/v103/troffaes19a.html — Troffaes and Basu (2019), open-access one-sided empirical Cantelli paper; retains a range-dependent offset and explicitly discusses inability to remove it.
- https://doi.org/10.1080/00031305.1987.10475433 — Konijn (1987), relevant distribution-free prediction article; complete text was not obtained in this audit despite authorized retrieval attempt.
- https://doi.org/10.1080/00031305.2016.1186559 — Stellato, Van Parys and Goulart (2017), multivariate empirical Chebyshev extension.

## Limitations

- Sharpness is over exchangeable laws, not specifically the iid subclass.
- The p-box is unconditional for the studentized residual rather than conditional on realized sample summaries.
- Some exact extremizers invoke the explicitly declared convention for zero leave-one-out variance.
- Konijn (1987) remained inaccessible in full text, so an older equivalent formulation cannot be absolutely excluded.

No GitHub write was performed by the audit chat. This file is staged by the guarded `scope-audit-change-set-v1` plan only.
