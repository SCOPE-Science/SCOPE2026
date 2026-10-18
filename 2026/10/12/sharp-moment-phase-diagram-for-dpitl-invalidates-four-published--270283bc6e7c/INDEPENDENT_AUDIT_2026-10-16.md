# Independent mathematical audit

## correctness

PASS

For every kappa,eta>0, S(n)=[(1+2n^eta)/(1+n^eta)^2]^kappa is a genuine decreasing survival with S(0)=1. As n tends to infinity S(n)~2^kappa n^(-kappa eta), and differentiating log S shows -S'(n)~(kappa eta/n)S(n). By a mean-value point in (n,n+1), p_n=S_n-S_(n+1)~2^kappa kappa eta n^(-kappa eta-1). Therefore E[X^r] is finite exactly when r<kappa eta (strict even at equality); for t>0 e^(tn)p_n fails to tend to 0, so ordinary MGF diverges, whereas t<=0 is finite. The six Table 1 products are .75,2.25,4.5,1.25,3.75,7.5: four rows display a finite value of a genuinely divergent mean, variance, skewness or kurtosis. Checked actual published Table1 values and source survival law. Fresh independent evaluations of S and its analytic derivative at n=10^6 for four invalid parameter pairs matched scaled constants to 0.7%; finite computations are not the proof.

## originality

PASS

The limiting exponent is elementary regular-variation reasoning, but the same DPITL distribution's published Table 1 and claimed finite dispersion across the full parameter domain are concretely contradicted; no verified published correction or stronger DPITL theorem was found.

## value

PASS

This is a material correction to a current statistical model with wrong population means, variances and higher moments in four of six highlighted parameter rows, affecting interpretation of model fit and dispersion. The whole sharp moment-existence diagram and MGF failure resolve a specific consequential published error, rather than an arbitrary p-series exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
