# Independent mathematical audit

## correctness

PASS

For full column rank A and residual r with A^Tr!=0, reflected block j has Gram H_j=C_j^TC_j, gradient g_j=C_j^Tr, exact squared-residual reduction d_j=g_j^TH_j^{-1}g_j, raw weight w_j=||g_j||². Sha–Zhang index probabilities aggregate to block weights w_j/sum w, including odd central singleton. Uniform sampling over distinct B blocks has expected decrease sum d/B. Let eigenvalues A^TA lie in [a,b], kappa=b/a; 0<=d_j, a<=w_j/d_j<=b. Set theta_j=d_j/sum d and t_j=sqrt(w_j/d_j). Cauchy–Schwarz and the bounded-moment inequality give ratio >=4sqrt(kappa)/(1+sqrt(kappa))². Four-column diagonal A=diag(s,1,1,s), r=(-1,-sqrt(s),0,0), has d=(1,s), w=(s²,s), kappa=s², and attains equality for every s>=1. Independent exact rational witness calculations corroborate all scalar ratios but all-size proof is analytic.

## originality

PASS

Sha–Zhang 2024 specifies the exact paired-column algorithm and raw-gradient sampling, but its inspected theorem concerns convergence, not the sharp ratio to uniform sampling over distinct reflected pairs. Gower–Molitor–Moorman–Needell 2019 show benefits of sampling proportional to actual sketched loss d_j, not raw w_j; their known dominance result should not be claimed as new. The scalar Kantorovich moment inequality is classical. Novelty is only the explicit sharp penalty for this specified 2024 sampling law and matching four-column witness. Related block-gradient sampling literature has different settings; possible older importance-sampling version of the bound is a material residual risk.

## value

PASS

The gap between probability proportional to ||g_j||² and actual exact block projection decrease g_j^TH_j^-1 g_j is an important algorithmic comparison. Quantifying the worst relative one-step progress with a sharp condition-number dependent coefficient and showing arbitrarily poor performance vs uniform at large kappa produces a meaningful limitation of a published method, not merely a generic inequality table. No claim of worse total iteration count or unequal per-block computation is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
