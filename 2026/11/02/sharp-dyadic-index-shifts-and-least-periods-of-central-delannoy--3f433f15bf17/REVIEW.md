# Independent mathematical audit

## correctness

PASS

Vandermonde on the binomial sum produces terms with one or two positive shift indices. v2 C(h,i)>=a-v2(i) leaves only (j,i)=(1,1),(2,2) from single-positive terms. For double-positive terms all vanish mod2^(a+3) except at a=2 the (i,l,j)=(2,2,2),(4,4,4) terms, each 16 mod32 and cancelling. The resulting phase is 2^(a+2)n(n+1)/2; its parity detects n=1,2 mod4. Powers-of-two h yield claimed periods, with half-period refuted at n=1; gcd-of-periods excludes all smaller shifts. Independent recurrence computation checked 10 moduli; finite work not substitute for cancellation proof.

## originality

PASS

Best-of-knowledge distinct mathematical claim after direct model/parameter and implication comparisons; known overlapping prerequisites and specializations credited. The identity T_n(3,2)=P_n(3)=D_n is a renaming and not original. General sum congruences or mod-2^k algorithms do not logically establish the specific uniform index-shift layer without arithmetic computation and exceptional a=2 cancellation; the proof supplies that calculation for all n,h and derives the least global periods. Lengyel Conjecture 4 explicitly anticipates part of the shifted valuation phenomenon for b=1,2 modulo four; the reviewed proof establishes those predicted special cases, but the original paper conjectures rather than proves that comparison and does not supply the full uniform h phase or period classification.

## value

PASS

The least global period modulo every 2^k is a canonical exact arithmetic invariant of the central Delannoy sequence, rather than an arbitrary finite table. The all-h dyadic phase and exceptional 32-cancellation explain why the least-period hierarchy behaves as claimed and provide usable congruences for unbounded indices. It additionally proves a natural special case of the shifted-difference valuation conjecture in Lengyel (2021) for offsets b=1 or 2 modulo four, though the other offsets remain outside the exact valuation theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
