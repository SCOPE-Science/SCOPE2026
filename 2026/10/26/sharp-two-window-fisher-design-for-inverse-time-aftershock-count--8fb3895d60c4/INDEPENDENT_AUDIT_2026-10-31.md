# Independent mathematical audit

## correctness

PASS

Direct Poisson mean differentiation for mu1=Ku and mu2=K(L-u) gives I_KK=L/K, I_Kc=-(1-e^-L)/c and the exact nuisance-adjusted J_L(u)=L/[u(L-u)](1-e^-u-u(1-e^-L)/L)^2. Under log-time transform y=log(1+t/c), the continuous score is e^-y and the between-bin variance equals J_L. Differentiating the within-bin quadratic loss yields W'=(a-b)(a+b-2e^-u); A(u)=(e^u-1-u)/u is strictly increasing, B(L-u)=1-(1-e^-(L-u))/(L-u) is strictly decreasing with u, proving a unique global crossing, not merely Lloyd-Max stationarity. Monotone convergence gives e^uinf=1+2uinf and the two efficiency limits from full Poisson information. Independent direct roots, Schur/full-information inequalities and 1000-point cutoff scans for 8 horizons pass; small L expansion analytic, not a numerical extrapolation.

## originality

PASS

Best-of-knowledge: compared mathematical implication, equivalent aliases, broader frameworks and exact tables; not directly covered by sources actually inspected. Residual literature risks and incomplete full-text access are explicitly recorded.

## value

PASS

A fully specified statistically interpretable experiment-design decision: optimal time boundary for retaining exactly two counts with unknown amplitude, and exact information loss relative to retaining individual event times. Sharp uniqueness and efficiency constants make a natural design fact rather than a routine first-order condition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
