# Independent mathematical audit

## correctness

PASS

Changing the rook index to j=n-k gives integer factorial-binomial expansions: at r=0 a sum of (-1)^(n+j) j! [C(n+j,2j)+C(n+j-1,2j)]; for 1<=r<p the extracted coefficient is (-1)^(n-r)(2n/r!) sum_j (-1)^j j!(n-j-1)_(r-1) C(n+j-1,2j). The integer binomial/falling-factorial support justifies extension to all j>=0. Mod p, all terms j>=p vanish, while Frobenius (1+X)^(N+kp)=(1+X)^N(1+X^p)^k mod p and 2j<=2p-2 leave only zeroth/first carry C(N,2j)+k C(N,2j-p). As other factors are p-periodic, A and B are exactly the displayed formulas, for all k>=0 and every n>=1. The alternating sign yields the 1,2,1 second difference for odd p; p=2 gives a two-step equality, and its r=2 nonincluded diagonal follows separately. The original integer sum verifies h3(1)=0,h3(4)=8,h3(7)=994, with weighted sum 1010=2 mod3. Independent direct construction tested 5 shifts of every r<p for p=2,3,5,7,11, n<=14, plus boundary. This is a proof of infinite prime progression, not extrapolated from 2485 tests.

## originality

PASS

The original claim survives only as the simultaneous, explicit affine progression theorem for all low-degree coefficients and its sharp cutoff; existing specific degree-two and original rook formulas are credited as prior work.

## value

PASS

The classical ménage hit polynomial is an intrinsic permutation/rook enumerator; classifying all coefficients below the prime in one uniform law, rather than an isolated digit congruence, is a natural p-adic arithmetic statement. The sharp failure exactly at the first excluded degree identifies the mechanism boundary of the single carry. These explicit residue forms are useful independent of an unproved downstream conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
