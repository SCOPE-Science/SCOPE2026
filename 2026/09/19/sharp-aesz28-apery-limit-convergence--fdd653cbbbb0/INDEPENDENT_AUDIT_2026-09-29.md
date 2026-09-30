# Independent Audit — 2026-09-30

**Record:** `2026/09/19/sharp-aesz28-apery-limit-convergence--fdd653cbbbb0`  
**Title:** Sharp exponential constant for the AESZ 28 Apéry limit  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `0e4c166e75f3e8eba3d95269cde38ac405df9e5e`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS**: The positive double-binomial formula exactly reproduces the recurrence solution. Its entropy phase has the unique interior saddle (3/4,3/4), with the filed Hessian and amplitude, giving A_n~(2√6/(3π²))64^n/n². The exact Casoratian then gives the quotient increment and summing the asymptotically geometric positive tail yields √2π³/84·64^{-n}.
- **Originality — PASS**: Bachmann’s current v1 proves the ζ(3)/7 limit and supplies the binomial and Casoratian identities but does not state the dominant-solution asymptotic or sharp quotient-error constant. Focused searches for the exact constants and AESZ 28 did not locate an earlier public statement. The Sato–Tasaka work cited by Bachmann remains described as in preparation and was not available for inspection, so it remains an explicit residual risk.
- **Scientific value — PASS**: The result upgrades a qualitative Apéry limit to a closed sharp exponential equivalent and supplies the exact leading constant for the dominant integral solution; the binomial-saddle plus Casoratian mechanism is reusable for other recurrence quotients.

## Independent checks

- Regenerated A_n and C_n from the recurrence using exact rational arithmetic.
- Independently evaluated the binomial sum for initial n and checked agreement.
- Recomputed the saddle Hessian/amplitude algebra and the Casoratian constant.
- Searched current literature for the exact constants, AESZ 28 rate, and the cited Sato–Tasaka title.

## Findings

- Exact recurrence generation agrees with the binomial formula at small n: 1, 6, 126, 3948, 149310, 6300756.
- Independent exact-rational recurrence plus high-precision evaluation gives A_100·100²/64^100≈0.16446028 approaching 2√6/(3π²)≈0.16545680 and the scaled quotient error ≈0.51824411 approaching √2π³/84≈0.52201782.
- The Casoratian asymptotic is (2√2/π)64^n/n^4, and the tail factor 64/63 produces the filed error constant.

## Sources

- https://arxiv.org/abs/2609.18271 — Bachmann current v1; proves the underlying Apéry limit and records the exact identities used.
- https://arxiv.org/abs/math/0507430 — Calabi–Yau/AESZ operator context.
- https://arxiv.org/abs/2011.03400 — General Apéry-limit background; characteristic-root convergence without this closed connection constant.

## Limitations

- The result concerns only AESZ no. 28 and does not improve an irrationality measure for ζ(3).
- The unpublished/in-preparation Sato–Tasaka manuscript could contain overlapping sharper asymptotics; no inaccessible material is claimed as read.
- The 2008 Calabi–Yau Apéry-limit literature was not exhaustively inspected for every equivalent normalization, though no exact constant was located in targeted searches.

Repository evidence was checked against current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the assigned source-tree SHA still matches the current record tree. GitHub was used only as read-only evidence; no repository writes were made.
