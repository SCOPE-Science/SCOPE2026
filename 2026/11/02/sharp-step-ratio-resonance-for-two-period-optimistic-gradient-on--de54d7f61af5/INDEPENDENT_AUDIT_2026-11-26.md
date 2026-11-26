# Independent mathematical audit

## correctness

PASS

In complex coordinates T(h)=[[1−2ih,ih],[1,0]]. The product T(v)T(u) has trace 1−4uv−i(u+v) and determinant −uv. For roots ξ,η of z²+Az+B, the Schur margin (1−|B|²)²−|A−BĀ|² factors as (1−|ξ|²)(1−|η|²)|1−ξ conjugate(η)|². Under |B|<1 the last factor is positive and the roots cannot both be outside. This proves the strict test and the neutral/expansive alternatives without a continuity argument. Here the margin is Δ. When Δ<0, uv<1, the expansive eigenvalue is simple and its coefficient is nonzero off a proper real subspace; the expansive eigenvector has nonzero first component since M₁₂=(1−2iv)iu≠0, so even iterates themselves grow. The constant-step factor and the negative rational witness agree. At a fixed ratio write r=ab t² and C=(a+b)²/(ab). The leading bracket is 6−C, and when C=6 the exact bracket is 3r(3−10r−5r²)>0 for sufficiently small r. Hence both endpoints are stable in the stated small-step sense. The source checker was inspected, not run; its finite ratio samples are not equality certificates. `python3 /workspace/branches/review_reproduction.py 5` independently passed exact rational transfer-matrix, margin, witness and critical-bracket tests.

## originality

PASS

The sharp constant-step cutoff and the Schur test are known and are not credited. The distinct claim is the explicit two-period stability/instability region for this current-step-scaled explicit method and its closed ratio boundary at vanishing scales. The strongest inspected period-two comparison has an extra resolvent, with a different stability region.

## value

PASS

The first nonconstant periodic schedule is a natural test of whether fixed-step safeguards carry over to the explicit historical-gradient substitution. The sharp relative-step restriction gives a concrete negative answer even for arbitrarily small step sizes, and resolving the closed endpoints is important for that criterion. The finding gives a meaningful boundary for one precise optimizer, not a claim against safeguarded variable-step methods.

The dated certificate retains the supplied scientific assessment, sources and limitations.
