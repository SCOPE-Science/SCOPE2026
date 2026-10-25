# Scientific review: centroid coincidence of a boundary Fermat–Weber center

## Correctness — PASS
The claim fixes one nondegenerate isosceles triangle at a time and defines the unnormalized perimeter-distance functional. Strict convexity yields its unique symmetry-axis minimizer. Direct differentiation and an elementary substitution give the closed scalar derivative (equation (1) in RESULT.md); independently evaluated quadratures agree to high precision. Four strictly separated signs of that derivative at the centroid were independently enclosed by outward-rounded interval arithmetic. The intermediate value theorem proves the non-equilateral coincidence, threefold symmetry proves the equilateral coincidence, and the exact negative transverse derivative proves the latter is a sign reversal. Uniform expansions on compact sets around the limiting unique zero justify both asymptotic statements. Numerical root solving alone does not establish any unclaimed uniqueness or classification.

## Originality — PASS, with stated risk
The closest primary paper, Zhang–Carlsson (2014), develops a general analytic segment-integral expression and an optimization algorithm for arclength-uniform polygon boundaries, but does not state the non-equilateral centroid coincidence, the two order reversals, or the opposite-shape limiting expansions. These specific results require additional sign and asymptotic analysis and are not direct assertions of its general algorithmic existence theorem. Panov–Savvateev (2018) concern uniform *area* demand in a filled triangle and thus do not cover the boundary-demand statement. The checked published comparisons concerned different centroid, median, or triangle inequalities; none gave this exact counterexample. Full bibliographic exhaustiveness is not proved, and earlier special-purpose studies of continuous facility location remain a residual risk.

## Mathematical value — PASS
Equality of a distance-minimizing center and the familiar area centroid is a natural geometric rigidity question. The explicit non-equilateral coincidence disproves a tempting equilateral-only characterization. Distinct thin and tall regimes approach the same relative height, yet intermediate shapes place the optimal boundary-service location below the centroid. The sign-certified second coincidence and asymptotic mechanism explain this unexpected nonmonotonicity; this is more than a routine numeric optimizer evaluation.

## Scope and limitations
Only at least two coincidence heights are proved, not a total enumeration. The thin non-equilateral height is isolated by strict interval endpoint signs, but unique isolation on that interval is not claimed. The shape parameter is real and positive; degeneracies are limiting cases only. Numerical checks supplement rather than replace the analytic proof. An independent scientific assessment remains outstanding.

Self-review: passed. Independent audit: not yet performed.
