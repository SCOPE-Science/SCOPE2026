# Independent mathematical audit

## correctness

PASS

Reconstructed the dihedral automorphism averaging argument using the convex centered operator norm, valid for all noninvariant feasible matrices. For invariant weights a,b, 2a+b<=1, diagonalization along the ring yields eigenvalues 1-b-a delta ±sqrt(b²+a²delta²), delta=1-cos(2pi j/n). For r=u²=1-cos(2pi/n), the positive-mode lower envelope strictly decreases in a and has a strictly convex unique b optimizer: a=(u+2)/(2H), b=u(u+1)/H, H=u²+2u+2. Check negative modes using mu²-[b²+(1-b)²]=u(u+2)(2-u²)/H²>0 for n>=3; mu=2(u+1)/H is actually attained as SLEM. At a=b=1/3 heuristic mu=(2-u²+sqrt(1+u^4))/3, optimal/heuristic gap tends to 3/2. Independent matrix eigenvalue experiments at all n=3..50 reproduce both; proof is all-mode analytical and not extrapolated.

## originality

PASS

Boyd–Diaconis–Xiao provide convex fastest-mixing Markov-chain framework; Boyd–Diaconis–Parrilo–Xiao give automorphism averaging and examples pure cycles/wheels/bump rings, not the present ring with one degree-one pendant per cycle node. The general SDP solves finite instances but does not state this exact all-n closed form or asymptotic ratio in inspected text. Specialized sunlet chain literature remains possible.

## value

PASS

Sunlets form a natural infinite bounded-degree graph family with slow ring mixing. Exact optimum edge weights, all-eigenmode attainment, and a 50% limiting gap advantage over standard heuristics are useful analytic mixing benchmarks; the result is not merely a numerical SDP instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
