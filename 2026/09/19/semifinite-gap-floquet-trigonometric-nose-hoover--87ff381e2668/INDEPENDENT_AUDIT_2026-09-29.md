# Independent Audit — 2026-09-30

**Record:** `2026/09/19/semifinite-gap-floquet-trigonometric-nose-hoover--87ff381e2668`  
**Title:** Semifinite-gap Floquet selection in the trigonometric Nosé–Hoover orbit  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `c103cff82117252da29a96a30a65aa9775fa0766`  
**Disposition:** **REPAIRED**

## Three-axis assessment

- **Correctness — PASS**: The periodic gauge maps the normal variational equation to the s=1 Whittaker–Hill operator. Hemery–Veselov’s stated classical theorem closes every even gap for s=1, so only anti-periodic weak-coupling resonances can open. Independent monodromy calculations for small a agree with b_±(a)=2±a/2−a^2/32+O(a^3), and reproduce the b=1/2 trace crossing.
- **Originality — PASS**: After repair, novelty is restricted to the source-specific use of the semifinite-gap theorem to obtain the exact weak-coupling parity selection rule and to the principal anti-periodic tongue asymptotics. The exact Whittaker–Hill reduction, reciprocal multipliers, and b=1/2 edge are explicitly credited to the earlier accepted SCOPE record `cohomological-contraction-floquet-threshold-trigonometric-nose-hoover--0debb0e2ee19` and are no longer claimed here.
- **Scientific value — PASS**: The repaired result supplies a clean spectral selection rule that suppresses an infinite family of periodic resonances and gives quantitative opening data for the first allowed anti-periodic tongue. This is a useful non-generic stability consequence beyond the earlier reduction itself.

## Repair boundary

The original package materially overstated its originality by claiming the Whittaker–Hill reduction, multiplier reciprocity and b=1/2 Floquet threshold as new despite an earlier accepted SCOPE record already containing them. The corrected research files narrow the claim to the semifinite-gap parity selection rule and the principal-tongue expansion.

## Independent checks

- Re-derived the periodic gauge and determinant-one condition.
- Read the classical semifinite-gap theorem in Hemery–Veselov rather than relying on the filed citation summary.
- Numerically solved the original normal variational equation near b=2 and at b=1/2 to check the asymptotic and finite-coupling statements.
- Compared against the earlier accepted SCOPE Floquet record to isolate genuinely new content.

## Findings

- Hemery–Veselov state that for odd s=2m+1 all even gaps except the first m are closed; s=1 therefore closes every even gap.
- For the physical a=0 resonances, periodic levels give |b|=1/j and anti-periodic levels give |b|=2/(2j+1), so the parity-selection statement follows directly.
- DOP853 monodromy checks at a=0.02,0.05,0.1 place the principal trace −2 boundaries within O(a^3) of 2±a/2−a^2/32.
- The exact WH reduction and the b=1/2 numerical edge were already present in an earlier accepted SCOPE record and required explicit de-duplication.

## Sources

- https://arxiv.org/abs/0906.1697 — Hemery–Veselov; Theorem 1 states the even-gap closure used for s=1.
- https://arxiv.org/abs/2609.19958 — Current source preprint introducing the model and normal variational equation.
- https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/09/19/cohomological-contraction-floquet-threshold-trigonometric-nose-hoover--0debb0e2ee19/RESULT.md — Earlier accepted SCOPE record containing the WH reduction, reciprocal multiplier structure and b=1/2 Floquet edge.

## Limitations

- The surviving theorem is only linear transverse stability of the exact central orbit.
- The small-a tongue expansion is local near |b|=2 and does not establish nonlinear bifurcation or global chaos.
- The repair removes duplicated claims rather than changing the underlying equations.

Repository evidence was checked against current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the assigned source-tree SHA still matches the current record tree. GitHub was used only as read-only evidence; no repository writes were made.
