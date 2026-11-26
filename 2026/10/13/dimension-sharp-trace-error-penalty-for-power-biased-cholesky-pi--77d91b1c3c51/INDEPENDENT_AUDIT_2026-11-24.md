# Independent mathematical audit

## correctness

PASS

For a full-column-rank Gram factor V, the residual is V(I−uuᵀ)Vᵀ for a unit u, so its rank is rank(A)−1 and every pivot trace is positive. The risk ratio is an average of T d_j^(q−1)/Q with weights proportional to d_j tr(R_j), where T=∑d_i and Q=∑d_i^q. Hölder and max d_i^q≤Q give the stated upper bound for all real q>1. The two possible residual traces m and t give the claimed singleton-block risks. Subtracting 1 gives (m−t)(t^(q−1)−1)/(2(t^q+m)), including the coincident equality cases at m=1. Substituting t=((q−1)m)^(1/q) gives the stated positive asymptotic constant, with n=m+1, and continuity at each finite m gives positive-definite examples with the same exponent. For q=2 the two-block ratio is 1/2+(r+s)t/[2(rt²+s)]; AM–GM gives equality precisely at t=√(s/r), and rs reaches its minimum n−1 at a singleton block. The n=17 risks are 32/5 and 10. These symbolic checks establish the continuous and all-dimension claims; the inspected verify.py gives optional finite rational tests and was not executed. The result makes no multistep claim and does not claim an optimal universal constant.

## originality

PASS

The sampler, the baseline expectation and the qualitative possibility of worse trace error are established, and an indexed record already uses the same block family for a different norm. The distinct supported result is the sharp dimension exponent for the one-pivot trace ratio against q=1 at every fixed finite q>1, with a restricted exact q=2 optimum. No inspected source establishes that claim; this is a bounded comparison, not priority certification.

## value

PASS

Diagonal bias is a natural variation of a practical low-rank algorithm. An exact rank-two witness turns an empirical warning into a dimension-sharp obstruction valid at every fixed finite bias q>1, even under positive-definite perturbation. The exact q=2 block extremum sharpens that obstruction without conflating it with the full PSD optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
