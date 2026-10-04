# Review

## Correctness

PASS. The forward formulas agree with the published endpoint-derivative calculation after translating from signed midpoint coordinates to chord coordinates. The inverse is proved without assuming existence: for arbitrary \(x,y>0\), the scalar function
\[
r\longmapsto
\sqrt{r^2+\frac{2r}{x}}
+
\sqrt{r^2+\frac{2r}{y}}
\]
is continuous and strictly increasing from \(0\) to infinity, so it crosses the fixed chord length exactly once. The resulting midpoint lies more than \(r\) from both chord endpoints, yielding a valid unique segment. The exact Jacobian is strictly negative on the whole domain, which upgrades the bijection to a real-analytic diffeomorphism.

## Originality

PASS, with a clearly identified close predecessor. Lukács's 2017 article and its 2020 English follow-up prove that two endpoint derivative values determine a segment on a known chord and give explicit rational formulas for the forward map. The inspected texts do not state the image of that map, surjectivity onto all positive data pairs, a global diffeomorphism theorem, or the Jacobian factorization.

Targeted literature and record searches were run for endpoint-derivative reconstruction, positive data ranges, global coordinates, diffeomorphism formulations, and Jacobians. No stronger or equivalent range theorem was located. The logical gap is genuine: an injective reconstruction map can have a proper image, so the earlier uniqueness theorem does not itself imply that every positive pair is feasible. The new monotone inverse equation closes that range question.

Residual risk remains because the extension is elementary and could have appeared under different terminology or in material not indexed by the searched records.

## Value

PASS. This is a natural complete classification of the first-order data for the basic one-segment inverse problem: it says exactly which normalized cusp-slope pairs can occur, not only that realizable data determine the segment. The result removes any hidden feasibility constraint, gives a one-dimensional constructive inverse, and exposes the exact nondegenerate Jacobian needed for local sensitivity analysis. It is deliberately limited to the one-segment, known-chord setting and is not presented as a solution of the harder multi-segment reconstruction problem.

Same-model review: passed. Independent audit: not yet performed.
