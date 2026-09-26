# Independent Audit — 2026-09-22 campaign

**Record:** `2026/09/08/080`  
**Audit performed:** 2026-09-26 UTC  
**Audited source tree:** `fcdddc38c82161cba0d44879fa16a57c8056faf4`

## Claim audited

The record gives three explicit binary cyclic symbol-pair codes at parameters ((8,3,6)), ((12,5,8)), and ((14,3,12)) that attain the binary (b=2) Griesmer bound, with generators, spectra, Singleton gaps, and a short-length cyclic census.

## Correctness — PASS

I independently implemented binary-polynomial division and codeword generation, then recomputed Hamming and cyclic pair weights for all codewords of the three headline generators.

The results match the record:

- (n=8), (g=0x33): (k=3,d_H=4,d_2=6), pair spectrum (A_6=4,A_8=3).
- (n=12), (g=0xbd): (k=5,d_H=4,d_2=8), pair spectrum (A_8=9,A_9=16,A_{12}=6).
- (n=14), (g=0xb97): (k=3,d_H=8,d_2=12), constant nonzero pair weight 12.

Each generator divides (x^n+1). Recomputing the (b=2) Griesmer sums gives
(S(8,3,6)=21\le24<S(8,3,7)=25),
(S(12,5,8)=31\le36<S(12,5,9)=37), and
(S(14,3,12)=42\le42<S(14,3,13)=46).
The Singleton gap is 1 in each case. The three lengths are not (2^t-1), so these codes are outside the two specific Luo et al. construction families described in the record.

## Originality — PASS, with a material narrowing

Luo–Ezerman–Güneri–Ling–Özbudak (arXiv:2401.04941) proves the general b-symbol Griesmer bound and gives two distance-optimal construction families.

However, Sascha Kurz, *Linear codes for b-symbol read channels attaining the Griesmer bound* (arXiv:2507.07728, 2025), predates this SCOPE record and determines optimal binary pair-symbol parameters for small dimensions. That work already covers the parameter landscape containing these triples; in particular it discusses many non-isomorphic ([8,3,6]) codes and gives/derives optimal small-dimension points including ([12,5,8]) and the dimension-3 ([14,3,12]) point.

Therefore **the optimal parameter triples themselves are not original**. The surviving originality is narrower: the specific **cyclic realizations**, their explicit generator polynomials and pair-weight spectra, and the exhaustive short binary-cyclic census. I did not identify those cyclic generators/spectra as claims of the covering general-linear-code paper.

Open-access sources:
- https://arxiv.org/abs/2401.04941
- https://arxiv.org/abs/2507.07728
- https://epub.uni-bayreuth.de/id/eprint/8523/

## Scientific value — PASS, narrowly scoped

Explicit cyclic realizations of known-optimal parameter points remain useful because cyclic structure supports compact algebraic descriptions and implementation. The generator/spectrum data and exhaustive (3\le n\le15) cyclic census provide reproducible benchmark material. The scientific value is in that cyclic classification/construction layer, not in discovering the general optimal parameter triples.

## Final disposition

**PASS.** Correctness passes. Originality and scientific value pass only after narrowing the contribution to the specific cyclic constructions, spectra, and cyclic census; the record must not be cited as first discovery of the three optimal parameter points.
