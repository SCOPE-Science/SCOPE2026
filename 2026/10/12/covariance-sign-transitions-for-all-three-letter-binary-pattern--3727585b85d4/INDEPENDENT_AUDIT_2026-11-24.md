# Independent mathematical audit

## correctness

PASS

The same-stream first-hit indices are finite with geometric-tail domination by disjoint blocks of three tosses, and distinct equal-length words cannot tie. The race matrix is transient. Its first-step recurrences give m=N1, s=N(1+2Qm)=(2N−I)m, w_a=Nr_a and h_a=Nw_a; the tail search starts at the longest retained proper prefix of the losing word. On the event of an a-win, T_a=τ, T_b=τ+additional time and the conditional mean of the future time depends only on the winning word, so the displayed mixed-moment equations follow. Independently derived all 28 rational covariances via a four-state last-two-letter chain after the first two tosses (branches/reproduction/covariance.py): the mixed moment obeys M=1+P_a E_a+P_b E_b+P_ab M, where each masked transition matrix drops just the designated hits. Averaging over the initial two tosses and subtracting the product of means reproduced the factored representative formulas and the supplied signs. Exact polynomial gcd and Sturm counts after excluding endpoint poles gave no nonsimple interior roots and classes 7,3,14,4. Complementation acts by p↦1−p and gives the stated 16 orbits. The highlighted cubic and approximate roots 0.307978528369904 and 0.643104132107791 reproduce. The frozen verification script was inspected, not replayed.

## originality

PASS

The distinct claim is the complete bias-dependent qualitative sign and root classification of the same-stream first-hit covariance, not the joint generating function or a new method for joint waiting times. The strongest prior joint-PGF result covers the distributions and permits exact moment extraction; its theorem and examples do not classify these root patterns. Related exact crossover analyses and indexed covariance results use different observables or sampling laws.

## value

PASS

The eight words form a complete natural family within the first short length showing these double reversals, not an arbitrarily selected list of examples. The phase diagram answers a dependence question missed by both race-odds tables and fixed-bias covariances: even the sign need not vary monotonically with bias. Simple-root certification distinguishes genuine switches from zero contacts and makes the classification usable without generating or numerically scanning a separate covariance for each pair. No value is attributed to rediscovering the general finite-state method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
