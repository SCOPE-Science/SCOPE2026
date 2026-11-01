# Mathematical review

## Correctness — PASS

The two affine coefficient vectors have nonzero determinant, so they are not phase equivalent. Their squared-magnitude difference is computed exactly and reduces along the spiral to \(2e^t(\sinh t+\kappa\cos(\alpha t))\). Every zero has positive parameter no larger than \(\operatorname{arsinh}\kappa\) and lies in a negative-cosine lobe. Lobe centers below this cutoff yield two roots each. Strict convexity of \(\log(\sinh t/(-\cos(\alpha t)))\) beyond a fixed pitch-dependent threshold bounds late lobes by two roots each, and only finitely many early lobes remain. Counting lobe centers gives matching upper and lower asymptotics. Alternating signs at the explicit parameters \(j\pi/|\alpha|\) prove every finite collision budget possible. Exponential independence supplies the separately stated whole-spiral uniqueness, including the zero polynomial. Finite numerical tests support, but do not establish, these conclusions.

## Originality — PASS, provisional

The evidence check compared aliases (circle–spiral intersections, affine phaseless ambiguities, arbitrary-site polynomial phase retrieval), stronger phase-retrieval theorems, and related geometric meshes. Wellershoff [1] studies equality on lines and line families; Liehr [2] works with arithmetic progressions of lines and Gabor sampling; Chalendar–Partington [3] treat pairs of circles and intersecting curves. Their inspected statements do not directly imply the specific quantitative circle–spiral crossing law. General exponential-Vandermonde interpolation on prescribed geometric meshes is already available as a separate fact and is not claimed as new here. Searching for the exact quantitative crossing law did not locate a directly covering source; absence from a search is not a priority proof. A generic intersection-bound result or an older spiral-geometry source remains a residual priority risk.

## Mathematical value — PASS

A sampling set can provide full continuous phase uniqueness and efficient designed finite measurements while allowing arbitrarily many adversarially chosen points to be entirely uninformative. The explicit sharp logarithmic rate gives a quantitative geometric mechanism for this divergence, even for degree-one polynomials, and is a natural boundary phenomenon in uniform sampling design. The assertion is neither a generic failure of every finite set nor an unwarranted optimality claim.

## Limitations and relevant literature

The collision law belongs to a specific one-parameter family of circles, rather than a maximum over every circle or every polynomial pair. The error term is pitch-dependent and no robust-noise statement is made. The closest related full-text literature is [1] M. Wellershoff, arXiv:2202.03733; [2] L. Liehr, arXiv:2308.05722; [3] I. Chalendar and J. R. Partington, arXiv:2403.16255. No independent priority or mathematical audit is represented.

Self-review: passed. Independent audit: not yet performed.
