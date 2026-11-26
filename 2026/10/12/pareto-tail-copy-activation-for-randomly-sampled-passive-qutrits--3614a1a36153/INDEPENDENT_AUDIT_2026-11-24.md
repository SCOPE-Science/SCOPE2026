# Independent mathematical audit

## correctness

PASS

PASS for repairs/4/RESULT.md. The frozen exact constant integral is correct, but its equality to 0.5226368151659937... overstates the accuracy of the archived quadrature by about 1.25e-13. Independent SciPy evaluations in two coordinates, and 50-digit mpmath, give 0.5226368151661182760231851559693..., supporting the rounded repair; replay evidence is in branches/65794f39-2759-43f0-b191-6d0a54510829/independent_quadrature.py and independent_quadrature.txt. I reconstructed the proof: adjacent shells are sufficient to test monotone population order and the two endpoint-difference maxima are floor((N-1)/2) and floor((N+1)/2), unchanged from odd N to the following even N; equality remains passive. Activation persists at higher N. The ordered simplex is one of six congruent-in-area permutation sectors, so the uniform density is 12 in (p1,p2). The change to (u,v) has Jacobian u/(1+u+uv)^3; its integral in v over the correctly ordered bounds is the stated difference with factor 6. In log coordinates the scaled interval width tends to 2a and is bounded by 2a, while b>=a/2 gives the integrable envelope proportional to a exp(-5a/2). The trace of the bounded continuous density on the diagonal yields C_f, positive at the required interior positivity; a null Gibbs curve and monotone squeezing yield almost-sure finiteness and the real-t asymptotic. Layer cake gives the positive-moment cutoff. The corrected complete file was inspected; the old finite output is retained only as an archived consistency check. No frozen script was executed.

## originality

PASS

The repaired finding claims the ensemble survival law and sharp tail, not the exact single-state activation criterion. The strongest distinct Resultary overlap gives that deterministic criterion exactly, including odd activation and the Gibbs exception. The inspected source statements do not address the pushforward of the sampling law, the sharp tail constant, or divergence of the mean. This is supported distinct ensemble content, not a claim of general priority.

## value

PASS

Even with almost-sure finite activation, the ensemble mean diverges. The exact law provides a quantitative baseline for copy budgets, and the general density result identifies the thermal-curve trace as controlling the leading tail and fixes all positive moment thresholds. This is useful statistical structure beyond the known deterministic passivity test or numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
