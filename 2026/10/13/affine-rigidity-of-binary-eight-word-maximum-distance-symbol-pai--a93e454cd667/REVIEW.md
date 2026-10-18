# Independent mathematical audit

## correctness

PASS

For 8 codewords, projection onto any 3 consecutive coordinates must be injective: matching those bits gives two equal adjacent pair symbols and distance at most n-2; this also realizes symbol-pair Singleton bound |C|<=8. Summing pair-distances over all 28 pairs yields <=24n by minimum collisions of four 2-bit patterns per position, hence 28(n-1)<=24n and n<=7. For each n=3,..,7, translating to contain zero converts an arbitrary code to a seven-clique of a finite forward-adjacency graph on the eligible nonzero vectors. The complete increasing-order clique recursion (no heuristic pruning) finds through-zero counts 1,1,5,4,2; every set is XOR-closed and thus a 3-plane. Coset translation gives exact labeled numbers 1,2,20,32,32. Independent C++ code reconstructed the compatibility graphs from the metric, every clique and closure without assuming linearity, producing all five counts. n=7 sharpness checks the distinct 00-position profile; the general result uses the exhaustive bounded reduction, not a finite sample extrapolation.

## originality

PASS

Chee et al. already give the Singleton-type ceiling. Sascha Kurz Section 4/Theorem 4.2 establishes a unique isomorphism class within **linear** binary [n,3,n-1] pair codes for 3<=n<=7; this does not force arbitrary nonlinear 8-word codes to be affine. A previously published Resultary record completely covers the n=5 count 20 and affine structure, and the separate length-six result is expressly credited by this source. The surviving contribution is the universal no-nonlinear theorem over the entire feasible n=3..7 range together with the other unrestricted counts and n=7 endpoint. Source RESULT mistakenly credits the Kurz paper to Luo–Ezerman–Güneri–Özbudak; that bibliographic attribution needs correction before any public use, without changing the mathematical conclusion.

## value

PASS

The complete feasible-length, all-codeword, no-nonlinear classification is a natural equality-case theorem for a central Singleton information-theoretic bound. It unifies the entire finite n range and proves the positive endpoint n=7 by exhaustive justified finite reduction; not solely recomputing prior n=5/n=6 table entries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
