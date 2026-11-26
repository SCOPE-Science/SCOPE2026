# Independent mathematical audit

## correctness

PASS

The affine substitution u=2a+1, v=2b+1 preserves Haar measure, and the factor 64 is a square unit. The only possible singular zero classes of F=(u²−1)(v²−1)+64n would require n=0 or 1+64n=0 modulo p. On a smooth zero ball, varying the coordinate with unit derivative gives an affine bijection for each next residue digit of F/p; this establishes uniformity and square probability 1/(2(p+1)) by summing the even positive valuations and square units. The measure of F=0 is zero. Summing the quadratic character in v gives 1+p χ(n)(3+χ(m)), with the exceptions u=±1 and u²=m accounted for separately. At F=0 the substitution w=(u²−1)v gives w²=(u²−1)(u²−m); the quartic has simple roots and two rational points at infinity, and its affine points with u=±1 are exactly the two points to remove. Thus Z=p−3−a_p. Substitution yields the claimed formula; Hasse gives the stated uniform remainder. Independently checked both examples and 420 generic prime-power cases using weighted triangular residues in the original coordinates and the exact residual smooth-ball mass. Replay: python3 -B /workspace/branches/independent-checks/record5.py. The finite tests do not prove the all-prime identity; the preceding argument does. No claim is verified at the excluded shifts or primes.

## originality

PASS

Best of current knowledge: the specific Haar-density formula and its uniform first-order bias are not covered by the inspected triangular-pair solvability or finite-field tuple-counting results. No priority is claimed for the underlying equation, quadratic-character sums, smooth lifting, or the Hasse estimate.

## value

PASS

This quantifies a natural local restriction from triangular Diophantine pairs rather than merely testing solvability of the equation: a uniform local input model has an explicit shift-dependent bias and a separately identifiable elliptic fluctuation. One finite-field curve count suffices to compute the exact infinite-level Haar measure on the full smooth shift locus. The value lies in that quantitative relation, not in the sample computations or in the classical local machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
