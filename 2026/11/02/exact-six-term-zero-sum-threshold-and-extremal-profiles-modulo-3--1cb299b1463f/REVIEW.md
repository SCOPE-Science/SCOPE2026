# Independent mathematical audit

## correctness

PASS

For admissible entries x mod 36 with 6∤x, a qualifying six-position sum lies in T={6,12,18,24,30}. A bad 12-list exists with six entries congruent to 1 and six to 2 modulo 6, whose only 6-divisible six-sums equal 36. The exact dynamic program propagates S_j(B+x)=S_j(B)∪(x+S_{j−1}(B)) with j decreasing, prunes only persistent forbidden six-sums, and nondecreasing residue recursion exhausts all multisets. An independent separate C++ recurrence, compiled and executed, reproduced the entire 13-level prefix count vector (1,30,465,4960,40920,278256,1397210,3565140,3172686,1271740,500586,156528,23970); found exactly 23970 bad 12-multisets and none extendible by any of 30 residues; reproduced the 11 residue-profile counts and 361 affine orbits (314×72,33×36,13×12,1×18). Thus s_1(6)=13 and stated complete census, not an extrapolation to other moduli.

## originality

PASS

Sun defines s_1(n) and conjectures s_1(n)=2n+1, but his inspected Theorem 1.3 does not prove the n=6 case. Li–Ling–Sun–Zhu prove distinct w_r and rank-2 statements, not this fixed-length rank-1 count; Gao et al treat prime moduli; the published s_1(4)=9 classification is for a different modulus. The exact n=6 threshold and 23970-object orbit census survive comparison, with possible unindexed older machine calculations acknowledged.

## value

PASS

The n=6 instance is the first squarefree composite modulus in a named conjecture and its sharp finite cutoff is mathematically motivated. A complete extremal multiset census, 11 profiles and affine orbit classification describe all maximal obstructions and could support later structural work; finite exhaustiveness is valid because the domain is explicitly finite and fully traversed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
