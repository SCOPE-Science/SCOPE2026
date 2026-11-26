# Independent mathematical audit

## correctness

PASS

At N=174592 the displayed factorization gives sigma(N)=1023*12*32=392832; the excess over 2N is 43648=N/4. The nine pairs consist of 18 distinct divisors, their products are N and their sum is 349184=2N, so their union is complement-closed. For leastness, 1 cannot satisfy the proper-divisor condition. For every 2<=n<=N the divisor-sum sieve counts each divisor once and near-perfectness is exactly 0<e=sigma(n)-2n<n and n mod e=0. Complement is an involution; any closed subset is precisely a union of whole orbits, counting a square-root singleton once. The reachable-sum update from B=1 is B=(B|(B<<w)) & ((1<<(2*n+1))-1) for each orbit weight w; the 2n bit tests the condition. Positive weights make the truncation exact. A separately written Python reproduction (independent_sieve.py, default limit 174592) returned all 37 listed candidates and sole intersection [174592], independently checking the factorization, excess and witness. The frozen code was inspected, not executed.

## originality

PASS

The contribution is the conjunction and its least element, not the appearance of N in the near-perfect sequence, or the separate definition or theory of strong pseudoperfectness. The explicit witness answers Question 42. No covering prior intersection statement or sufficient theorem furnishing this example was identified in the compared passages.

## value

PASS

An explicit nonsquare example answers a precise published existence question without assuming the conjectural square-root omission route. Leastness is a natural, fully checked numerical invariant of that intersection rather than an arbitrary bounded slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
