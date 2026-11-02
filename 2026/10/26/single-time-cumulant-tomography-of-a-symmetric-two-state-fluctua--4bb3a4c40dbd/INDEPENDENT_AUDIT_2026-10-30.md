# Independent mathematical audit

## correctness

PASS

Conditioning on the stationary telegraph trajectory makes X_t a centered Gaussian with random variance 2(mu t+a integral S), yielding kappa_{2m}(X_t)=(2m)!/m! kappa_m(A_t) and odd integrated-spin cumulants zero. Integrated pair correlation e^{-2k|s-u|} yields kappa4=24a^2 f(x)/(2k)^2. The time-ordered connected 4-spin correlation is -2 exp[-2k(gap1+2gap2+gap3)], so kappa8=-80640a^4 I(x)/(2k)^4; coefficient normalization checked independently using a 2x2 tilted generator. Differentiation gives P(x)=2e^{2x}(I'f-2If')=(4-x)e^{2x}-(2x^2+8)e^x+(x+4); its first six series coefficients vanish and for all n>=6 the coefficient [2^{n-1}(8-n)-2n(n-1)-8]/n!<0 (verify n=6,7 then n>=8). Thus Q decreases strictly, with endpoints from f~x^2/2, I~x^4/24 and large x. Algebraic inverse x, k=x/(2t), mu=V/(2t), a=x sqrt(C/(24f))/t proves necessity/sufficiency including strict a<mu. Independent symbolic Laplace identity and three tilted-generator checks passed. Population cumulants only; no statistical estimation claim.

## originality

PASS

Guéneau–Majumdar–Schehr 2025, Supplement Section IV (Eq. 53), already gives exact finite-time two-state characteristic/moment generating function, which implies all forward cumulants here. Those are credited. The surviving theorem is the monotone one-time inverse mapping from only three prescribed cumulants with exact image and strict-positive diffusivity admissibility boundary. Inspected original Section IV/A and Eq.53–68 describe forward fluctuations and asymptotics, not the analytic Q-bijection or inverse parameter test. Residual risk of earlier inverse telegraph identifiability formulation retained.

## value

PASS

Provides a complete, sharp population identifiability and feasibility test for a natural stochastic-diffusivity model using measurements at one fixed time, resolving intrinsic parameter ambiguity without multi-time trajectories. The positivity inequality and sharp ratio image matter physically. It is a mathematically motivated inverse theorem, not merely recomputation of known forward cumulants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
