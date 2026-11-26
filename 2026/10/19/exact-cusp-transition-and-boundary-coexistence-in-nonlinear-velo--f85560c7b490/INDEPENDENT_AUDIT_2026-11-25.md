# Independent mathematical audit

## correctness

PASS

The compact process has an invariant law. One can couple the orientations and then use the same resets; the first reset after orientation coupling makes both coordinates agree. Reflection gives symmetry and the fair orientation marginal makes each reset source r/2. The two nonzero interior drift coefficients give locally regular joint densities away from the source, with finite traces there (the measure transport equations also preclude interior atoms). At stationarity there is no terminal atom: neither terminal can be reached from the interior in finite time, and a reset removes any initial terminal state. Set p=p₊+p₋, q=p₊−p₋, J=Σq−gp and K=Σp−gq. On the positive interval J′=−rp and K′=−(r+2λ)q. The reset jump and odd symmetry give J(0+)=r/2. Differentiating K=[(Σ²−g²)p−gJ]/Σ yields (Σ²−g²)p′=(g′−r−2λ)J+2g(g′−r−λ)p, hence the asserted one-sided slope. At equality g″(0)=0 by oddness and only the term 2c₀λp(0) survives differentiation. The positive no-flip-from-reset age density gives p(0+)>0 and gives the endpoint lower bound after transformation by T(v)=∫₀ᵛdu/(Σ−g(u)). Since T(v)+(log(v*−v))/c* tends to a finite limit, this contribution diverges when r+λ<c*. Decay right of the central cusp and divergence at the edge force an interior minimum, with another by reflection. At r=0 the stationary total current vanishes; no boundary atom survives tumbles, and the interior scalar transport law gives the stated central curvature and strict minimum for λ<c₀. The joint weak-reset comparison uses c₀/2<λ<c₀ plus λ<c* for the divergent edges at small r. This proves sufficiency, not an exact count of extrema or a sharp full-density endpoint asymptotic. Reviewed RESULT.md equations (1)–(4), VERIFICATION.md and verify.py; no frozen code run.

## originality

PASS

The same model, stationary equations, and qualitative cusp/side-peak phenomenon are known. The slope and critical curvature are short local deductions from those equations. Credit is for the explicit quantitative classification combined with the positive-reset terminal divergence bound and weak-reset coexistence, not for the forward equations or generic cusp onset. No equivalent joint claim was identified in the primary statements inspected.

## value

PASS

The exact transition answers a natural question left by numerical density plots in the same model. It shows that higher drag terms do not affect the central slope while the terminal drag slope controls a sufficient, simultaneous boundary effect. Strict inequality plus the critical curvature distinguish the actual local behavior, and the weak-reset change of local type can be missed in plots at finite resolution. The result locates these effects without promising all stationary modes or an explicit invariant density.

The dated certificate retains the supplied scientific assessment, sources and limitations.
