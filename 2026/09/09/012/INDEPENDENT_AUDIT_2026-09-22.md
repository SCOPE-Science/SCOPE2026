# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/09/012`  
**Audited source tree:** `bb60c26abf911bbd181ad223c69a439efdc235d0`  
**Date:** 2026-09-26 UTC  
**Disposition:** PASSED (proof typo explicitly corrected in this audit)

## Correctness

PASS with a local algebra correction. Milnor/Koszul structure constants c1=2a/(bc), c2=2b/(ca), c3=2c/(ab) give K12=((c1−c2)^2+2c3(c1+c2)−3c3²)/4 and cyclic companions, equal to the displayed rational formulas. Coordinate curvature planes diagonalize in dimension three. On a=b=1, the extrema are s and 4−3s, yielding positivity s<4/3 and strict quarter pinching 4/7<s<16/13; both endpoints have ratio 4. Independently recalculated the rational interval certificates: positivity numerators at least 241/625 and 64009/390625; the smaller box has K in [1999/2601,7300000/5764801], ratio 18987300000/11523837199<2. The (1/4,1/4,1) example gives −704. Principal circles are closed geodesics because the diagonal connection has ∇ei ei=0, so sys≤2πmin(a,b,c). The printed identity Lmin²/Vol^(2/3)=C(min³/abc)^(1/3) is false: the exponent is 2/3. With that correction the bound follows, and the round metric attains C. The committed verifier's systolic section checks min³≤abc and the constant, but does not detect this mistaken exponent.

## Originality

PASS, narrow and qualified. Olmos–Rodríguez-Vázquez's open arXiv full text gives Berger positive curvature for its vertical metric parameter τ∈(0,4/3) and studies totally geodesic submanifolds; its geometric parameter is s here, and it does not state the exact quarter pinching window. Inoguchi–Munteanu focus on magnetic trajectories and Chen–Gaspar on widths. The window is an elementary but explicit sharp consequence of known curvature formulas. The box constants are convenient sufficient enclosures, not an optimal triaxial classification; the systolic inequality is a simple principal-circle and min≤geometric-mean observation. No independent novelty is credited to those ingredients.

## Scientific value

PASS, modest. Exact strict quarter pinching endpoints for a canonical one-parameter family are a reusable boundary check in positive-curvature examples. The triaxial boxes supply certified neighborhoods, and the sharp round equality calibrates the volume-normalized geodesic bound. The work does not classify the full triaxial parameter space or determine systoles away from the round point.

## Prior work

- https://arxiv.org/html/2302.11711v3
- https://arxiv.org/abs/2406.15886
- https://arxiv.org/abs/2505.09548

## Scope

The displayed systolic identity in RESULT.md needs the exponent correction above. The inequality and equality constant remain valid. The novelty assessment is limited to the explicit sharp Berger window, with the other pieces evaluated on their limited utility.
