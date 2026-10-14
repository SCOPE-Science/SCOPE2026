# Independent mathematical audit

## correctness

PASS

Build the 11x11 Toeplitz T from the explicitly listed ternary source triple, G=[I_11|T]. The identity ker(GG^T) maps injectively to hull because rank G=11; independent GF(3) row reduction gave rank GG^T=1, so hull dimension 10, and rank Gram H=0. I independently enumerated all 3^11=177147 codewords and 3^10=59049 hull words using the source triple, reproducing ambient weights {0:1,8:990,9:1540,11:16128,12:14784,14:59400,15:31680,17:38808,18:10780,20:2772,21:264} and hull weights {0:1,9:1540,12:14784,15:31680,18:10780,21:264}. The two nonzero cosets have identical distributions by additive negation; their half-difference from ambient enumerator gives {8:495,11:8064,14:29700,17:19404,20:1386}. Griesmer sum ceil(10/3^i), i=0..9, equals23, so d=10 impossible for ternary [22,10] and the found hull d=9 is optimal. The source unique exceptional class assumption comes from the cited full classification, not from the enumeration itself; no global classification of all optimal [22,10,9] hulls is claimed.

## originality

PASS

The exceptional source code and its class uniqueness are prior-published, but the computed maximal proper Euclidean hull, optimal hull distance, full hull and two quotient-coset enumerators do not follow from isoduality or the existing optimum classification. Full primary comparisons support best-knowledge new invariant.

## value

PASS

The object is the unique exceptional ternary DT optimum at its natural length, and Euclidean hull is a standard invariant relevant to duality, orthogonality and code construction. Maximal proper hull gives a new optimal ternary self-orthogonal [22,10,9] subcode with exact distribution, and quotient-coset spectra classify its immediate extension; a coherent useful invariant not an arbitrary isolated slice. Exhaustive finite computation is complete for the natural 3^11 state space, with separate Griesmer optimality proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
