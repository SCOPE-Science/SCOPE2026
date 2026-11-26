# Independent mathematical audit

## correctness

PASS

Away from 2, an odd prime maps to an even composite and a composite to a prime, so an odd cycle must contain 2. If k+2 is composite, the next steps from 2 go through an odd prime and an even composite to a prime at step four; that either returns too early or has an even composite at step five. Otherwise the first three steps end at P+(2(k+1))=q; q=2 returns too early and q>2 gives the last composite k+q. It returns to 2 exactly for a power of two. Conversely q<=k+1<k+2 separates the three primes and also precludes equality of the two even composites. Determinism yields uniqueness. In the divisor parametrization 2^m+1=q+(k+1)=qh, so h>=3 is odd, and P+(q(h-1))=q iff P+(h-1)<=q; reversing gives all hypotheses and positive odd k. The separate direct return-time test from 2 using trial division reproduced exactly (5,3,3), (21,11,5), (51,13,6), (59,5,6), (1365,683,11) for the stated finite range.

## originality

PASS

The supported distinct claim is the exact characterization and uniqueness for every positive odd shift, with its divisor reformulation. Das defines the same map and discusses attainable periods but does not supply this classification in the inspected text. A very close later record is credited explicitly; it does not establish prior coverage of the assigned result. This is a best-of-knowledge finding, not proof of priority.

## value

PASS

This classifies the next odd period after three in a natural published dynamical system, for all positive odd shifts, and explains why there is at most one such cycle. The exact tests reduce the search to prime divisors of 2^m+1 and a cofactor check. Value lies in the exhaustive parameter characterization, not the isolated examples or the algebraic recoding alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
