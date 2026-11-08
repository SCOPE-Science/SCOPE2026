# Independent mathematical audit

## correctness

PASS

Let R∈[0,1) be independent of X,Z standard normal, with P(R>1-s)∼c s^a (a,c>0), and Y=RX+√(1-R²)Z. Plackett differentiation gives exactly C(uw1,uw2)=u²w1w2+∫_0¹P(R>r) h_r(q1,q2)dr, valid with atoms. For r=1-t/log(1/u), normal quantiles and Mills asymptotics give scaled kernel ∝(w1w2)^1/2 t^-1/2 exp[-t/2-(log(w1/w2))²/(8t)]; endpoint survival contributes c t^a. A uniform integrable bound K t^(a-1/2)e^-t/4 justifies dominated convergence for fixed positive weights. This proves L^a C(uw1,uw2)/u→c B_a(w1,w2), with B_a as displayed and B_1=min(w1,w2)(1+|log(w1/w2)|/2). Independent SciPy Plackett quadrature for endpoint laws a=.5,1,2 and unequal weights checked convergence at L=15,30,60; finite quadrature is corroboration, not the proof.

## originality

PASS

Targeted Resultary search plus comparison of the closest published primary statements and hypotheses identifies no prior implication of the complete final claim; originality is best-of-knowledge and subject to explicitly named residual risks.

## value

PASS

Endpoint-regular-variation assumption for random correlations creates a natural near-asymptotic dependence problem where classical first-order tail copula is identically zero. The result supplies a genuinely informative second-scale logarithmic normalization and full non-product angular profile, plus exact uniform-mixing formula, a precise probabilistic invariant useful beyond the diagonal Ledford–Tawn index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
