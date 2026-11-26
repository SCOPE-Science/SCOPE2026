# Independent mathematical audit

## correctness

PASS

An independent derivation uses successive first passages i→i−1 for the dimensionless process (time scaled by μ). By the strong Markov property the passage times that sum to extinction from j are independent. For rates d_i=i and b_i=i(3−i)x the transform satisfies φ_i(s)=d_i/[d_i+b_i+s−b_i φ_{i+1}(s)], with φ_3=3/(3+s). Its mean and variance satisfy M_i=(1+b_i M_{i+1})/d_i and W_i=M_i²+(b_i/d_i)(W_{i+1}+M_{i+1}²), with (M_3,W_3)=(1/3,1/9). In particular M_2=1/2+x/3, M_1=1+x+2x²/3. Summing mean and variance increments gives all three stated means and, after dividing variance by squared mean, the stated F_j. Subtracting one leaves numerators x(4x²+16x+9), 4(4x²−4x−9) and −24(2x+3) over their respective squared denominators. The signs and threshold follow. The quartic governing −F_1' has one sign change, is negative at zero, and tends to +∞; F_2' changes sign only at the positive zero of 4x²−8x−27, and F_3' has positive factors 2x+1 and 6x+13. These give strict monotonicity on the stated intervals. At x=0 the three values are 1, 5/9 and 49/121, and all tend to 1 at infinity. The dimensionless means have strictly positive derivatives. The supplied verify.py was inspected, not executed: it compares mean and relative-variance formulas and F_j−1 identities at eleven rational x, but does not itself test the derivative identities despite the description at RESULT.md line 53. The latter were checked algebraically; separate bisection of the quartic on [0,2] gives 1.1009654228408214.

## originality

PASS

The count process, general phase-type moments and mean-persistence framing are prior material. The supported distinct claim is the exact, initial-occupancy-specific relative-variance regime: two different maxima, an intermediate-start crossing of one, and monotonic convergence from below only from full occupancy. The closest same-generator statement inspected analyzes the hazard of a particular initial mixture, not this trichotomy. This is a bounded assessment, not a priority claim.

## value

PASS

Three patches are the smallest system with an intermediate occupied count distinct from both the singleton and full starts. That start changes from underdispersion to overdispersion and then reaches a different maximum from the singleton start, while the full start remains underdispersed. The comparison with strictly increasing means isolates a qualitative effect that mean persistence obscures. The exact thresholds and curves give a benchmark in this natural finite occupancy model; they do not justify broad ecological or intervention claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
