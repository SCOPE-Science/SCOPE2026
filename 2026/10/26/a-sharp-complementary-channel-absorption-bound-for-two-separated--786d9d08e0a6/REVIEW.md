# Independent mathematical audit

## correctness

PASS

Distributional jump -2ikc u gives U(c)=[[1-c,-c],[c,1+c]]. M=U(b)diag(e^{iθ},e^{-iθ})U(a), det M=1 and M22 nonzero. Flux-balanced two-port scattering has det S=-M11/M22. Thus CPA iff e^{2iθ}(1-a)(1-b)=ab. Since a,b>0 and a,b≠1 on solutions, the phase is ±1; plus forces a+b=1, minus forces a+b-2ab=1 and therefore L>1. At CPA, rank-one S has nonzero singular value (|M21|+|M21|^-1)/|M22|, evaluating to 1 at L=1 and sqrt((L-1)^2+1)/L overcritical. Minimizing absorption over all input states is 1-||S||², yielding 2(L-1)/L². Its derivative -2(L-2)/L³ gives sharp maximum 1/2 at L=2; ordered strengths 1±1/sqrt(2) and incident-power asymmetry from B_R=M21 A_L. Independent symbolic matrix verification at L=2 confirms S^*S spectrum {0,1/2}; no general assertion depends on finitely sampled phases.

## originality

PASS

General CPA scattering zeros, equal illumination and phase matching are known since Chong et al. (2010), while a 2019 primary preprint constructs complex point-potential lasing/CPA examples. The assessed theorem concerns the constrained two-positive-loss delta pair with fixed sum and optimizes the *minimum over all coherent incoming fluxes*, which is different from existence of one perfect absorption input or maximum absorption. The sharp 1/2 may numerically coincide with single-sheet 50% limits but the metrics differ. The close 2019 full text was not inspected exhaustively: explicit priority risk retained.

## value

PASS

For the physically natural two-dissipator model, maximizing absorption under adversarial coherent illumination while insisting on exact CPA is a meaningful design tradeoff, distinct from identifying a single perfectly absorbing eigenchannel. The exact all-positive-loss branch classification and unique L=2 asymmetric optimal device provide sharp spectral and energy-budget information, not a generic rephrasing of CPA.

The dated certificate retains the supplied scientific assessment, sources and limitations.
