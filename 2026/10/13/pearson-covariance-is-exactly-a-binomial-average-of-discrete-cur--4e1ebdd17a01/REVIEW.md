# Independent mathematical audit

## correctness

PASS

For iid uniform cell labels Z_a, C=sum_{a<b}1[Z_a=Z_b] and X²=m−n+(2m/n)C. By pair exchangeability Cov(C,T_h)=choose(n,2)Cov(I12,T_h). Conditioning on pair collision versus distinct cells gives E[T_h|I=1]−E[T_h|I=0]=E[h(Y+2)−2h(Y+1)+h(Y)], Y~Bin(n−2,1/m). Cov(I,T_h)=(m−1)/m² times that, obtaining coefficient (n−1)(m−1)/m. For D_lambda, the sign of prefactor cancels convexity reversal across lambda=0, so covariance>0 all lambda>−1. For G², discrete convex f(k)=k log k, n E Δ²f(Y)→m, giving 2(m−1) limit; tail bounds justify interchange. Exhaustively independently enumerated sample label sequences and confirmed 60 covariance identities. The m,n≥2 and empty-cell conventions verified.

## originality

PASS

The power-divergence family, its large-sample common chi-square limit and algorithms for exact marginal distributions are classical. The checked Marhuenda et al complete article deals with separate exact laws and critical values and does not furnish the joint covariance for arbitrary additive score. The general finite-sample binomial-curvature mixed-moment identity and positive covariance at every λ>−1 are distinctive. Foundational Cressie–Read 1984 original full text could not be acquired: a publisher abstract and opening page are visible, and Oxford returned no verified PDF. Best-of-knowledge PASS with priority risk rather than treating inaccessible text as failure.

## value

PASS

The joint finite-sample behavior of classical goodness-of-fit statistics determines agreement in noisy categorical tests. An exact covariance identity for every additive cell score, with immediate global sign determination across the power-divergence family and chi-square limit, is useful beyond any one numeric sample regime and not a marginal-test recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
