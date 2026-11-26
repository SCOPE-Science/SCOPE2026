# Independent mathematical audit

## correctness

PASS

The normalized theorem is correct. Repair repairs/2/RESULT.md removes the false suggestion in frozen RESULT.md line 38 that scaling the extremizers gives bounds on the unrestricted class with a_1=c. For k=c=2, take a_1=a_2=2 and split 2a_2 as (1,3); continue with any positive splits summing to 2a_m. Then S_3=5, below the proposed scaled lower bound 6. The repaired theorem only treats a_1=1. The exact even recurrence and the one-unit odd bounds yield simultaneous comparisons by induction; the reflected digit map obeys U(2m+1)=kU(m+1)-1 and positive saturated splits realize it, while positive digit-map differences realize L. For alpha=log_2 k, the increment (2^j+t)^alpha-t^alpha is nondecreasing in t, giving n^alpha <= (k-1)L(n); superadditivity gives the reverse comparison with coefficient one. For U, recurrence yields U>=n^alpha and the reflected ratio bound is increasing in x=(2^r-n)/2^r, with the limiting value at x=1/2. Powers of two and their immediate predecessors/successors certify the four claimed limits, including k=2. Inspected frozen RESULT.md, VERIFICATION.md and verify.py without executing the package; an independent finite replay constructed the two greedy splits and compared digit formulas at every 1<=n<=333 for 2<=k<=14 (4,329 integer comparisons). The proof, not the finite replay, establishes the full ranges. Only RESULT.md needed correction.

## originality

PASS

The surviving claim is the exact normalized Galileo-family optimization and the sharp family-wide coefficients, not the digit map or the tree description. The closest inspected classification specifies the admissible splits but does not perform the coupled integer prefix optimization or derive its sharp oscillation constants. The closest quantitative bounds use a narrower class and are not sharp here.

## value

PASS

Exact simultaneous bounds across an unrestricted integer family improve on separate coarse growth estimates. The upper extremizer and sharp uniform coefficients capture how large the entire family can oscillate under the doubling constraint, rather than merely evaluating a familiar digit sequence. The result has a natural scope and a clear contrast with estimates restricted to monotone terms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
