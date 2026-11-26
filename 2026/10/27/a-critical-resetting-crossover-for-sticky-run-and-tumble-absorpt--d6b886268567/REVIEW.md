# Independent mathematical audit

## correctness

PASS

The telegraph backward equation has decaying spatial eigenvalue −sqrt(s(s+2α))/v, and normalization in the left-moving wall state fixes the right/left amplitude ratio α/[s+α+sqrt(s(s+2α))]. Its small-s expansion gives A_wall=sqrt(2/α), A_home,−=(x₀/v)sqrt(2α), and their sum for A_home,+. Conditioning on the first independent exponential bulk reset, with any excursion start transform g and bare home transform a, gives the exact deficit 1−F_r,P(s)=s(1−g(s+r))/(s+r a(s+r)). At s=θ²z,r=Rθ² with z>0 and R≥0 fixed, this deficit is θ A_P z/sqrt(z+R)+O(θ²). Sum the independent geometric visits, including the initial home leg and the successful final wait: the numerator is θF_home φ and the denominator is 1−(1−θ)φF_P. Dividing by θ and using the square-root waiting deficit gives the claimed law, continuous at z=0, including R=0. Independent check of the Lévy measure: its tail is A_P e^(−Rt)/sqrt(πt), whose Laplace transform times z equals A_P z/sqrt(z+R). Differentiating that tail gives the stated positive density. Adding the independent stable component and sampling both at one independent mean-one exponential time gives the resolvent transform. Karamata's theorem for monotone survival yields c/sqrt(π) for R>0 and (c+A_P)/sqrt(π) for R=0 as the t^(−1/2) amplitudes. Pointwise continuity as R decreases to zero, strict Laplace-transform ordering at fixed z>0, and the orientation threshold all follow from the transform. This assumes no resetting during binding and independent waiting and absorption. The uploaded verifier was inspected, not run. A separate bounded Pareto-transform replay for both orientations and protocols at R=0 and 0.7 showed the maximum absolute error fall by about a factor of four from θ=0.04 to 0.01 in each reset regime; it is corroboration, not an asymptotic certificate.

## originality

PASS

The exact two-protocol renewal calculation and finite-parameter protocol comparison are materially prior. The contribution supported here is the fixed-R joint scaling law, the explicit bulk-excursion Lévy component, and the noncommuting zero-reset and far-tail limits. The known exact transform is a strong starting point, but the inspected prior analyses do not give the simultaneous critical scaling or the resulting reset-dependent tail behavior. Neither the general heavy-tail rule nor the protocol threshold taken in isolation supports this pass.

## value

PASS

The critical law identifies when bulk resetting alters the limiting excursion contribution without truncating the independent binding tail. The limiting distribution is continuous at zero scaled reset rate but its far-tail amplitude is not, a meaningful diagnostic for using the zero-reset approximation. The two protocol coefficients and the explicit Lévy measure make that distinction testable without assuming a finite binding mean.

The dated certificate retains the supplied scientific assessment, sources and limitations.
