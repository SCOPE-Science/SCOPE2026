# Independent mathematical audit

## correctness

PASS

Removing j leaves a path with starting coordinate i=n-1-j. Success requires visiting both ends before exit. Multiplying the two initial gambler's-ruin probabilities by the respective success probabilities of the crossing stages gives wA+wB=(1-r)r^i/(1-r^(n-1)) and conditional wB/(wA+wB)=beta. For the passage-time calculation, with the killed kernel P on [0,L], (I-P)y=-d and (I-P)(y r^y)=d r^y. The weighted time u solves (I-P)u=h_L with zero boundary data, and substitution gives u/h_L=(L C_L-y C_y)/d. Reflection inverts r and d together and yields the left-exit formula. The second stages use the same interval length and distance one from the near barrier. After reaching both path ends, the exit time from [0,n] is unconditional, with mean (n h_n(y)-y)/d by the drift martingale. At j=1 or n-1 the initial stage is zero and only the positive-probability branch is needed. The uniform remainder follows from C_m-1=O_p(r^m), beta=O_p(r^(j-1)), and the O_p(n) bound on all branch means, with C_1=1/d. The law gives a geometric tail in n-1-j and the bounded normalized conditional means there converge pointwise to 1/d, so dominated summation proves the unconditional comparison. Independent replay: python3 /workspace/reproductions/audit_cycle.py; an exact-rational forward calculation tracks successive range expansions using tridiagonal exit kernels, rather than deleting the target label. Both probability and conditional first moment agree in all 408 pairs (4≤n≤15, p=51/100, 5/8, 7/11, 9/10), including both endpoints. The finite checks corroborate the proof and do not establish the asymptotic.

## originality

PASS

Pass applies to the exact conditional elapsed-time first moment and its uniform rare-terminal expansion, not to the last-site marginal, its exponential rate, or typical unconditional timing. Earlier joint results materially overlap but do not give this exact conditional calculation or uniform coverage across rare macroscopic terminal sites.

## value

PASS

The result connects the temporal cost of coverage to a rare spatial endpoint on a natural Markov chain. The factor 2−x shows a macroscopic, endpoint-dependent slowdown not visible in the geometric terminal law or typical Gaussian scaling. Exact weights and a uniform error quantify the effect beyond an example or a numerical comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
