# Independent mathematical audit

## correctness

PASS

For every positive m, parity forces odd m, and m=1 fails. For an odd prime power the finite reciprocal geometric sum is strictly below 3/2. With two distinct primes p<q and p>=5 the abundancy is strictly below (5/4)(7/6)=35/24, so p=3. Writing T=3^(a+1), exact multiplication by q-1 gives (T-q)(q^b-1)=4(q-1); thus T-q is a positive integer equal to 4/(1+q+...+q^(b-1)). For b>=2 this is less than 1; b=1 gives q=T-4. Conversely (T-1)(q+1)=Tq+3 when q=T-4, and the prime cofactor is >=5. This proves the unrestricted classification by distinct support, independently of the cutoff. The independently checked large q=10460353199 has no trial divisor through 102275; the corresponding m=36472996363223648799 satisfies the exact identity and 102461 divides (m-1)/2. The frozen VERIFICATION.md lines 23–29 report the 1,000,000 sieve, three hits and 367461 eligible integers; verify.py lines 23–66 implement it. That recorded sieve was inspected, not run or taken as the universal proof. The original expert, independent-audit, and Lean fields were not_performed.

## originality

PASS

The equation and included parametric family are prior art, not discoveries here. The supported distinction is the unbounded necessity of that family under distinct prime support at most two for the standalone equation. The strongest available comparisons do not already establish that necessity.

## value

PASS

An exact natural low-support boundary for an established Diophantine equation replaces a list of examples and a sufficient family with a full characterization at arbitrary exponents. The composite-neighbor witness concretely separates the standalone question from the older adjacent-pair construction. The contribution does not purport to classify higher support or predict infinitely many prime cofactors.

The dated certificate retains the supplied scientific assessment, sources and limitations.
