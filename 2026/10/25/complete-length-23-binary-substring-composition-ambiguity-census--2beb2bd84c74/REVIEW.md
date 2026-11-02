# Independent mathematical audit

## correctness

PASS

The defining observation is H_w(k,j)=#{i: sum_{h=i}^{i+k-1}w_h=j}. Inspected C++17 source enumerates exactly all integers 0≤w<2²³ as words, computes an additive deterministic 64-bit key K from complete H; H_w=H_v implies K_w=K_v with certainty. It sorts all keys and independently recomputes the complete prefix-sum H for EVERY member of any nonsingleton key bucket, rejecting a bucket containing different histograms. Therefore hash collisions cannot yield false equivalences, and singleton buckets cannot hide any equal observations in other keys. Independent complete C++ exhaustive enumeration processed all 8,388,608 words and reproduced 4096 singleton, 4,191,936 doubleton, and 160 four-word classes (4,196,192 observations), with 152 classical reversible interleaving families and eight noninterleaved. Independent interleaving construction enumerated all factor length pairs satisfying (m+1)(k+1)=24 and all nonpalindromic factors, confirming exactly 152 matched quadruples. The original source additionally checks all 160 CSV witnesses against computed classes; source table Git blob was verified in tree. This is an exhaustive *finite* certificate only for length 23. The sum 4096+2·4191936+4·160=8388608 is a consistency check, not the sole proof.

## originality

PASS

Acharya–Das–Milenkovic–Orlitsky–Pan 2010 and arXiv:1403.2439 already prove the observation/polynomial and classical interleaving mechanism and specifically identify length 23 as the first noninterleaved ambiguity example. This known phenomenon is NOT original. Their materially read primary papers do not list the entire n=23 class-size histogram, the exact observation count or all eight exceptional quadruple fibers. Indexed related records treat restricted read length 2 or distinct multispectra, not the full multiset of all substring compositions. An obscure earlier full census or appendix not identified remains a residual priority risk.

## value

PASS

Length 23 is the natural first exceptional length for the canonical full-substring-composition reconstruction channel, not an arbitrary cut. An exhaustive ambiguity class spectrum, exact zero-error code cardinality and explicit complete division of nonclassical exceptions are concrete reusable finite classification facts. The finite result does not claim an all-length theory or improved reconstruction algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
