# Independent mathematical audit

## correctness

PASS

For the exact RKL2 stability polynomial R3(z)=1+z+z^2/2+z^3/15 and Q=[[-1,1,0],[0,-1,1],[0,0,0]], direct multiplication gives R3(hQ)=[[r(h),h(1-h+h^2/5),h^2(1/2-2h/15)],[0,r(h),1-r(h)],[0,0,1]], with r(h)=1-h+h^2/2-h^3/15. Factoring the two independent offdiagonal signs proves exactly [0,(5-sqrt(5))/2] union [(5+sqrt(5))/2,15/4], with r(h) and 1-r(h) positive over the candidate interval using the Legendre bound for 0<=h<=5. For every finite Markov generator, R2(hQ) has strictly positive diagonal entries and offdiagonal entries h(q_ij+h(Q^2)_ij/2), each with a nonnegative initial interval. On at most two states Q^2=-lambda Q; for R3 the offdiagonal multiplier 1-r(lambda h) stays nonnegative and diagonal positivity cannot return after z>=5. Strict signs at h=3,3.7,4 establish robustness for a neighborhood of the two birth rates. Independent SymPy exact matrix computation confirms the three diagnostic step signs. This proves endpoint positivity only, not positivity of internal stages.

## originality

PASS

Published RKL diffusion/STSt literature analyzes scalar stability, spatial monotonicity and positivity near Dirichlet boundaries; no inspected original theorem gives this three-state directed pure-birth reentrance and simultaneous stage/state minimality. Other published mathematical maps SSP-SDIRK2(2) and [2/2] Pade concern different stability functions and do not imply it.

## value

PASS

A smallest possible state count and method stage count for loss-recovery-loss positivity is a natural structural boundary in numerical Markov integration. The two separated exact admissible step intervals and their robustness distinguish endpoint positivity from scalar absolute stability and are not a routine derivation of the RKL polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
