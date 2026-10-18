# Independent mathematical audit

## correctness

PASS

The recurrence with characteristic polynomial (T-a)^2 has x_n=(Cn+D)a^(n-1), C=x_1-a x_0 and D=a x_0. Cancellation gives [n,k]_x=a^[k(n-k)] product_{j=n-k+1}^n(Cj+D)/product_{j=1}^k(Cj+D). If C=0 the coefficients are powers of integer a; if D=0 they are ordinary binomials times such powers; both are divisible. Otherwise normalize affine factors to Aj+B with A>=1, B!=0, gcd(A,B)=1 and no zero positive-index terms. Dirichlet supplies arbitrarily large primes p congruent B mod A and not dividing a, set k=(p-B)/A. Denominator j=1..k has exactly one p factor (at j=k) and none at j<k; numerator j=k+1..2k has no multiples of p (when A=1 all lie in (p,2p), otherwise their mod-A congruence forbids hp for 2<=h<=A). Thus nu_p([2k,k]_x)=-1 for infinitely many distinct p; x_k does not divide x_2k. Independently reconstructed sample witnesses (a,x0,x1,p,k)=(2,3,1,59,13),(-3,2,5,137,13),(1,2,5,29,9). Infinite conclusion uses Dirichlet, not the finite samples. All hypotheses including a negative, D=0, C=0 and no positive zeros checked.

## originality

PASS

Best-of-knowledge novelty is the if-and-only-if binomid/divisibility classification and infinite distinct prime denominator obstruction for nonzero integer repeated roots. Shapiro explicitly leaves general order-two binomid classification and its implication to divisibility as an open question. His zero-initial-value Lucas result and polynomial divisible classification cover only the easy directions; Granville classifies division sequences but does not imply every binomid sequence is divisible.

## value

PASS

This treats a natural discriminant-zero family in a published explicit open problem on second-order recurrences, produces a full dichotomy (not an arbitrary numerical slice) and infinitely many certified central coefficient denominator primes in the complementary case. It is a nontrivial infinitary arithmetic classification, not just a finite congruence check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
