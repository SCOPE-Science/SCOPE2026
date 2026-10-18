# Independent mathematical audit

## correctness

PASS

The source rate eta_i=(sqrt(v_i)+eps)^{-1} ranges in [1/(G+eps),1/eps]. RMS normalization p_i=sqrt(d)eta_i/||eta|| increases with eta_i and decreases with each other eta_j, so the two opposite-corner states realize sharp p_min,p_max. For isotropic F, x_i^+=(1−a p_i)x_i, hence F(x+)/F(x) is a convex combination of squared coordinate multipliers. Convexity of (1−ap)^2 places its worst case at the two sharp endpoints. As p_min>0, strict contraction is equivalent to a p_max<2 for a>0. Independent numerical tests covered d=1,2,3,100 and reconstructed both corner rates exactly; at a=2/p_max extremal sign reflection retains objective. This is one step only; does not prove global training convergence.

## originality

PASS

Best-of-knowledge non-coverage after primary statement and implication comparisons. The claim is not made new merely because a text query lacked an identical title.

## value

PASS

The sharp stability boundary quantifies exactly how AvaGrad RMS normalization retains coordinate concentration despite eliminating global scale. It gives a motivated optimizer-specific learning-rate/adaptability tradeoff, including actual sign-reflection instability, not a generic textbook SGD threshold alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
