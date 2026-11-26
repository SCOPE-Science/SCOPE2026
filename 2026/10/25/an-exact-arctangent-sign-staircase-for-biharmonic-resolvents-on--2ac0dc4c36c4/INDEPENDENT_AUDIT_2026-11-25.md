# Independent mathematical audit

## correctness

PASS

For the unnormalized combinatorial Laplacian, normalized Walsh characters have eigenvalues 2k and give the scaled antipodal binomial sum with factor (-1)^k. Independently, the kernel of exp(-s L_d) between antipodes is [(1-exp(-2s))/2]^d by independent coordinate flips. Laplace integration for the ordinary shifted resolvent and the change u=exp(-2s) give its beta product for Re z>0, and rational continuation to z=±i/sqrt(t) is legitimate. Taking the appropriate imaginary part gives the positive product amplitude times cos(sum arctan(a/j)), with a=1/(2 sqrt(t)); this confirms the partial-fraction signs and 2^d normalizing factor. Phase derivative is strictly positive, and the phase ends at dπ/2 only at a=∞. Thus exactly floor(d/2) half-odd multiples of π lie in its open range, including the distinction at odd d; each crossing is simple and remains so under the decreasing parameter change. At p=π/2 the smallest phase root lies between p/H_d and 2p/H_d for large d by the uniform cubic arctangent remainder. Expansion gives a_0=p/H_d+H_d^(3)p³/(3H_d⁴)+O(H_d^(-6)); inverting gives the stated negative H_d^(3)/(6H_d) correction. The independent diagnostic matched 45 exact rational solves on the Hamming-layer quotient for d=2–10 with the binomial sum (independent_recheck.py, cube); the frozen script was inspected, not run. Only the antipodal entry is classified; t=0 is excluded and the last antipodal crossing is only a lower bound for an eventual full-matrix positivity cutoff.

## originality

PASS

The exact finite sign classification and final-zero expansion of this antipodal squared resolvent remain distinct from the inspected heat, time-stepping and path-resolvent results. Ordinary resolvent partial fractions and the beta integral themselves are standard; no priority is claimed for those tools or for eventual positivity in general.

## value

PASS

A natural entry of a standard fourth-order graph resolvent exhibits an unbounded number of sign changes as the graph dimension grows. The exact count, ordered simple crossings and precise logarithmic scale resolve more than eventual positivity or a small-dimensional witness, and can be used to benchmark positivity or reentry for higher-order graph operators. The result neither assumes nor infers entrywise positivity at the antipodal cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
