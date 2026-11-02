# Independent mathematical audit

## correctness

PASS

For scalar OU dX=-lambda X dt+sqrt(2)dB, K>=2 and s=lambda h, derive the published predictor-index convention A_H=1-s+(s²/K)sum_i i H_i and Gaussian-noise coefficient 1-s sum_{i>j}H_i. Indicator first and second moments give m_j=(1-s+cs²)^2+d_j s^4 with c=(K-1)/(2K), d_S=(K²-1)/(12K²), d_B=(K-1)²(2K-1)/(6K³), and n_S=2s/lambda(1-2cs+cs²), n_B=n_S+2s³(K-1)(K-2)/(3lambda K²). Then 1-m_j=sQ_j(s) for strictly decreasing cubic Q_j (Q_j'<=1/3-2c<0); unique roots yield exact finite second-moment stability intervals and s_B<s_S for K>=3. Since m_B>m_S and n_B>=n_S, 1/lambda<V_S<V_B over their shared stable interval. K=2 agrees in law. Verified exact moment algebra by independent rational enumeration of all Bernoulli patterns K=2..8.

## originality

PASS

Kandasamy–Nagaraj (arXiv:2405.17068) explicitly introduces both midpoint selectors and notes qualitative lower variance without replacement; no priority is claimed for those facts. Its reviewed Section 2.2 and later log-concave sampling follow-up concern general sampling bounds, not this scalar all-K sharp stationary mean-square stability pair and temperature ordering. Related published random-OU/ULMC covariance comparisons concern different schemes.

## value

PASS

It gives exact admissible stepsizes and a strict stationary covariance-bias ranking of two published stochastic integrators at the same expected midpoint workload; the strictly larger one-choice interval is a substantive design distinction, not simply the already-known variance-of-update comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
