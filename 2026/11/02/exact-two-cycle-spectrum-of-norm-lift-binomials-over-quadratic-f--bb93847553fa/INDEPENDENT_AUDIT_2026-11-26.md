# Independent mathematical audit

## correctness

PASS

For x nonzero let t=N(x), u=N(F_a(x)), c=Tr(a), d=N(a). Independence of 1,a and a²=ca−d make F_a²(x)=x equivalent to t+u+c=0 and tu=d+1. These force t²+ct+d=−1, so the norm recursion gives u=−t and hence c=0. Conversely c=0 and t²=−d−1 imply the two equations. Trace zero is impossible for outsiders in characteristic two; otherwise a²=−d is a nonsquare, so a²−1 is nonzero and has two distinct nonzero square roots exactly in the stated case. The corresponding fibers have q+1 points each and are exchanged; 0 is the unique fixed point because a=1−N(x) would put a in K. Independently, the conic s²−t²=1 has q−1 points by factoring, so sum_t χ(t²+1)=−1. There are 1+χ(−1) zeros of t²+1, and therefore (q−χ(−1))/2 values of t where it is a nonsquare, all t≠0. Pairing ±t and taking the two outsider square roots of each t²+1 gives the same number of active coefficients. Zieve's exact permutation parameters have trace 3μ≠0 for q≡2 mod 3 and trace zero in characteristic three; any nonzero base-field coefficient would kill the norm fiber N(x)=−a, so no permutation cases were dropped. The packaged verification/verify_cycles.py was inspected, not executed: its main loops test fixed and exact two-period counts on explicit finite fields and compare exponentiation on a subset, not permutation necessity or all prime powers. Its header mentions a stale filename; RESULT.md gives the actual replay path.

## originality

PASS

Pass for the exact period-two point and coefficient census, not for the permutation classification. The two strongest available sources on the same binomial and on its broader family settle bijectivity, not whether the lifted second iterate fixes a point. No equivalent census was identified in the inspected evidence.

## value

PASS

This classifies the first nontrivial periodic orbits of a known norm-lift family even outside the bijective cases. It identifies the exact fibers and their exchange, and quantifies how many parameters exhibit it, splitting a family whose prior bijectivity classification does not distinguish these dynamics. The result is uniform in the field and goes beyond a small-field cycle check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
