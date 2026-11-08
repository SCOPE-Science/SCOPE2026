# Independent mathematical audit

## correctness

PASS

For n≥3 one-way cycle with r_i>0, t=h/2, z_i=tr_i/(1+tr_i), B=∏z_i, the exact resolvent R=(I−tQ)^(−1) has R_ii=(1−z_i)/(1−B). The Cayley identity C(2t)=2R−I and irreducible M-matrix positivity imply all off-diagonal entries positive for t>0; only diagonal crossings matter. The diagonal derivative has sign −z_i+[B/(1−B)]Σ(1−z_j); setting U=∏_(j≠i)z_j and S=Σ_(j≠i)(1−z_j)>0 makes strict negativity equivalent to U(1+S)<1, valid by U≤e^(−S)<1/(1+S). The smallest diagonal resolvent occurs exactly at maximum r_*, and its stationary limit π_i≤1/n<1/2, so it crosses 1/2 once. Clearing denominators gives F(t)=(1−tr_*)∏_(j≠i*)(1+tr_j)+t^n∏r_j with unique positive root; exact positivity 0≤h≤2t*. In the uniform case, root x_n−1=x_n^n/(1+x_n)^(n−1), x_3=φ, x_n↓1, 2^(n−1)(x_n−1)→1. Independent rational inverses verified 16 mixed-rate examples plus the exact (1,2,4) threshold; finite tests did not establish global monotonicity.

## originality

PASS

The published reversible Markov-chain result proves the general diagonal resolvent test and spectral strict monotonicity under reversibility, but expressly leaves nonreversible positivity intervals unclassified. One-way directed cycles n≥3 are nonreversible; the strict decline is established here by a different explicit product inequality, together with exact maximum-exit bottleneck and rate-dependent polynomial root. Gottlieb–Shu–Tadmor broad SSP theory and Higueras–Roldán Dirichlet heat grids do not cover the same generator family. Related Cayley/matrix-function literature remains a priority risk.

## value

PASS

Sharp timestep positivity on heterogeneous directed transport rings is a natural numerical Markov property for a genuinely nonreversible class. Identifying the governing vertex by maximum departure rate and proving a unique sharp threshold, not only a sufficient CFL-like bound, settles an interpretable parameter classification; the uniform cycle has an unexpectedly small exponential finite-size correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
