# Independent mathematical audit

## correctness

PASS

The frozen proof's degree-four coefficient for mixed signs has an incorrect factor d-4; the frozen symbolic checker expands nodes epsilon*(1+a*u), not the required epsilon*(1+u)^a. For p=7, d=6 and (A,B,C,D)=(1,6,2,5), direct integer binomial expansion of the required determinant gives coefficient -4800, or 2 modulo 7, whereas the frozen formula gives 5 modulo 7. This is a proof and checker defect, not a false incidence statement. The replacement derives the true factor d-1 by formal log/exponential reparametrization with invertible denominators through degree four. For even d the cubic two-pair term forces equality of sums; for d other than p+1 the quartic term is a unit unless the unordered exponent pairs agree, while the cubic term has valuation at least p+2>4. The two pairs that do agree are precisely antipodal pairs. The repaired proof handles d=4 in the same argument. The three-plus-one cubic term is a unit, same-sign columns reduce to prime-order Fourier minors except the repeated row residues, and for odd d the Schur polynomial reduction gives exactly the two parity-pure exceptions. At d=p+1 the direct two-pair determinant is, up to sign, 2(a-b)(c-e)(ab-ce), with the expected equality of sums; the count follows since a fixed sum admits (p-1)/2 distinct unordered pairs in each parity. The first three Vandermonde rows give rank at least three for all column sets. This rechecks the unchanged finding including p=5, the counts and the uniformity equivalence. The new exact symbolic script at /workspace/repairs/5/verify_expansions.py was run successfully, and the direct binomial example independently checks the corrected coefficient. Neither check substitutes for the all-prime proof; the uploaded scripts were not executed.

## originality

PASS

The repaired proof does not change the mathematical statement. Credit the fixed d=4 incidence and the order-14 full-spark dichotomy as existing coverage. The distinct content is the uniform variable-d incidence and rank/count classification at order 2p, including the central equal-sum mechanism and count. The strongest inspected exact and general matches do not supply that content. This is a best-of-knowledge assessment, not a priority certificate.

## value

PASS

The row mask is a natural one-row extension of the ordinary three-row Vandermonde mask. An exact incidence theorem identifies the failure mechanism of each non-full-spark case (parity, antipodal pairs, or equal sums), including how the central mask differs from other even masks. It gives structure and ranks, not merely a computation of deficiencies for selected primes. The repaired proof preserves all of this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
