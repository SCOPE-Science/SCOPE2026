# Independent mathematical audit

## correctness

PASS

Iteration is an affine map of 2t independent fair bits, and all fibers of its linear part have equal size. The one-site Krylov basis consists of the center singleton and successive reflection-pair sums: the operator sends each interior pair to its neighboring pair sums (the center contribution cancels), and at the far end the even antipode cancels while the odd last pair contributes to itself. This also covers the n=3 and n=4 boundary cases. Dual vectors are constant on the inversion orbits of residues modulo h=gcd(n,2d) and must vanish on the residues 0 and d. For odd n there is just one fixed inversion residue and d=0 mod h; for even n the second fixed residue h/2 is removed exactly when d is not 0 mod h. This gives the stated deficiency and the coprime iff. In the coprime odd case the two truncated spaces intersect only in constants, which do not appear before the final step. In the coprime even case a common vector is separately constant on the two parity classes and vanishes at the two opposite-parity antipodes, hence is zero. These dimension calculations give min(2t,n), and the single-site basis is always too short. Independent coordinate updates and incremental binary elimination replay via `python3 /workspace/review_evidence/reproduce.py 4`: 21,318 rank-time steps over n=3..40 and 166 exact output-mass checks including noncoprime separations over n=3..8.

## originality

PASS

The exact deficiency, sharp coprime horizon and complete coprime rank profile survive comparison to verified earlier statements. The striking exact sensor-dual match is from a later dated record, not earlier priority evidence; the earlier stochastic model inspected has a different transition operator. This is a bounded best-of-knowledge decision, not a global priority claim.

## value

PASS

The natural two-site randomization question asks for both the obstruction and the first full-support time, not just eventual existence. The orbit formula quantifies every obstructed separation, including parity-dependent defects, and the rank profile shows exact saturation of the information-theoretic bound in the unobstructed cases. These results are directly useful for choosing two sites and a finite update budget.

The dated certificate retains the supplied scientific assessment, sources and limitations.
