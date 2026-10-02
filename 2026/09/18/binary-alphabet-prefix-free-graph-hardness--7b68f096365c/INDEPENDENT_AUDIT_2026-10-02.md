# Independent mathematical audit

## correctness

PASS

Read Baláž--Popa arXiv:2609.17353v1 Section 2 and full Section 3.2 Lemma 1/proof: the lemma requires an injective equal-length synchronized code, a guard g forbidding codeword occurrences in g t g for every unaligned non-codeword k-mer t, and absence of such gadgets in encoded input strings, then yields OPT(S')=k OPT(S)+C. The proposed binary code phi(a)=001 h(e(a)) 10, h(0)=10,h(1)=11, length 2 beta+5, is injective. Marker 001 occurs only at aligned starts: no interior 00 in h(e(a))10 and boundary 10|001 has crossing 100,000. A codeword begins/ends in zero; g=1^k means an occurrence beginning in guard cannot start with zero, an occurrence strictly within t must end in the right guard with one, and occurrence at t's first bit would equal non-codeword t. Maximum ones run in encoded strings is 2 beta+2<k, including boundaries. Thus every actual Lemma 1 hypothesis holds, and the source proof's penalty M=(k+1)L+1 excludes non-codeword triggers with the affine objective. Membership in NP follows from listing at most N occurring trigger windows and evaluating all segments and paths in polynomial time. k=2 ceil(log2 |Sigma|)+5=O(log N) after discarding unused symbols. The finite beta<=6 artifact is only a sanity check; the symbolic proof is decisive.

## originality

PASS

The motivating complete primary text proves fixed-k with growing alphabets (Theorem 2) and size-three variable-k hardness (Theorem 3), not binary hardness; its Lemma 1 is a reusable reduction rather than an explicit binary instance. A same-problem literature search found no prior binary MPFG result. Best-of-knowledge, with the recent-paper/simultaneous-work caveat.

## value

PASS

Moving the proven hardness boundary from a three-symbol alphabet to binary is a natural minimum-alphabet classification for a biologically motivated parsing optimization problem. The fixed-k versus logarithmic-k contrast accurately delineates the parameter dependence of the source's O(2^q N) algorithm. This is not just a relabeled instance: an explicit self-synchronizing/guarded binary encoding is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
