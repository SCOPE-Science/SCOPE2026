# Independent mathematical audit

## correctness

PASS

A common length-3 deletion output exists iff the intersection sum_i min(x_i,y_i) is >=3. Distinct valid codewords cannot share a coordinate of multiplicity >=3, hence at most four heavy codewords. Light multiplicities <=2 total at most 8: none for n>=9. Two light vectors of length n>=6 have intersection >=2n-8>=4, so at most one joins the heavy words. At n=5, the only light profiles are permutations of (0,1,2,2) and (2,1,1,1); the latter has no light neighbors, while any light A word has precisely two mutually incompatible light neighbors. Thus <=2 light words. Explicit four constant-vector codes plus the designated two or one light vectors reach all upper bounds. Independent enumeration finds light counts 16,10,4,1,0 and compatible-light pairs 12,0,0,0,0 for n=5..9; the all-length proof is symbolic, not an inference from those enumerations.

## originality

PASS

Best-of-knowledge PASS for the exact four-symbol, three-survivor staircase. The relevant January 2026 preprint treats the same multiset channel and high-deletion parameter but supplies an upper bound, not this tight staircase; its q=4 exact example concerns a different one-deletion setting. A March 2026 companion addresses deletion balls and asymptotic bounds. The closest materially read exact 3-survivor Resultary record solves q=3, with a distinct light-vector compatibility graph; q=3 does not imply the q=4 result. Residual priority risk of an older short-distance discrete-simplex packing table remains.

## value

PASS

The natural next alphabet after the exact ternary three-survivor problem has a genuinely different exceptional compatibility graph, allowing exactly two light words at n=5; the theorem gives a sharp all-length classification of maximum code size including two finite thresholds. The intrinsic deletion-correction capacity and its nontrivial small-alphabet transition are independently useful, not a renamed bound or a mere finite table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
