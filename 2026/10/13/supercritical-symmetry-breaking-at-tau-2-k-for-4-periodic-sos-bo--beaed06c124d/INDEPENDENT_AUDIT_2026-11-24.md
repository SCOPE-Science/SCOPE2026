# Independent mathematical audit

## correctness

PASS

The published system and its larger shared root are the ones in the Finding. In s=(a+b)/2 and d=(a−b)/2, the two equations are equivalent to G=0 and dH=0, with G,H polynomials in s,u=d²,τ after extending the divided difference. At (x,0,τ₂), put B=k−(k−1)x² and use x^(k−1)B=1 and k(2x−τ₂)x^(k−1)=−τ₂. Direct differentiation gives G_s=2x/B, G_τ=x(1−1/B), G_u=−k/x²; H_s=2k/B−2k/x², H_τ=1−k/B, H_u=−k(k−2)/(3x³), including the vanishing k=2 term. Hence the (s,τ) determinant is 2(k−1)[k−(k+1)x²]/(xB)>0. Cramer's rule gives τ'(0)=(H_s G_u−G_s H_u)/det=C_k exactly as printed; the denominator and numerator are positive since x²<k/(k+1). Inverting this analytic local curve gives exactly two positive unequal ordered solutions above the threshold and none at or below within the neighborhood, with amplitude 2/√C_k and error O((τ−τ₂)^(3/2)). The symmetric diagonal persists by G_s>0. Swapping is a shift by two height classes; unequal a,b force minimal period four. The Henning–Külske identifiability theorem independently certifies that the resulting GGM cannot also arise from a law of smaller minimal period. Independent high-precision bisection eliminated τ using the exact divided difference at fixed d and solved the remaining original equation for k=2,3,4,8,40,120; at d=10^(−12) all six estimates (τ−τ₂)/d² matched C_k with relative discrepancy below 5×10^(−21), and the k=4 values were τ₂≈3.497359313898, A₄≈0.452949755970. The frozen checker was inspected, not executed. Its amplitude comparison builds d from the predicted amplitude and thus is not an independent estimate of it; neither computation replaces the analytic proof.

## originality

PASS

The shared root, cyclic identification and small-order explicit branches are credited to prior work. The distinct contribution is the all-order local continuation for the standard ferromagnetic equations, with a positive coefficient and the explicit onset amplitude, in particular for k≥4. The closest catalogue pitchfork is for a different interaction and pattern. No equivalent all-order result for these equations was established in the material inspected.

## value

PASS

The larger intersection is singled out by the published equations rather than chosen arbitrarily. Determining the local side and amplitude converts an algebraic crossing into actual period-four gradient-measure existence for all k≥4 in a stated regime, without claiming a global classification. The local mechanism and onset coefficient are meaningful data for subsequent branch analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
