# Full-parallel-class-free packings on 16 points: beta(4,16) in [33,37] with two non-isomorphic 33-triple witnesses

## Context
For integer rho with 1 <= rho <= v/3, beta(rho,v) is the maximum number of
blocks in a partial Steiner triple system (PSTS) on v points whose maximum
partial parallel class (PPC) has size rho (Stinson, arXiv:2007.11033).
At (rho,v) = (4,16), five pairwise disjoint triples form a full parallel
class up to one leftover point, so beta(4,16) is the natural full-class
threshold at the smallest even order where the boundary is nontrivial.
Prior literature gave only the interval [25,37]: the Stinson Theorem 2.4
Room-square construction yields beta(4,16) >= 4*(16-4)/2 + D(4) = 24+1 = 25,
and the unconstrained Schoenheim counting bound yields beta(4,16) <= 37.
Maximum-system enumerations (Demirkale-Donovan-Grannell, arXiv:1708.07646)
tabulate only automorphism/Pasch/mitre/Fano data for 37-triple MMPTS(16),
with no parallel-class column. No-parallel-class STS theory
(Bryant-Horsley, arXiv:1407.5766) treats full STS of orders 3 mod 6,
motivating but not implying this even-order packing question.

## Definitions
Work on point set {0,...,15}. A packing (PSTS) is a family of 3-subsets
(triples) with every pair of points in at most one triple. A partial
parallel class is a subfamily of pairwise disjoint triples; its size is
the number of triples. beta(4,16) is the largest number of triples in a
packing containing no 5 pairwise disjoint triples (maximum PPC size <= 4).

## Result
Theorem. beta(4,16) lies in [33,37]. More precisely:
(a) There exist packings with 33 triples and maximum PPC exactly 4; two
explicit non-isomorphic block lists are given below.
(b) No packing of any kind on 16 points has more than 37 triples, hence
beta(4,16) <= 37.
This raises the constructive floor 25 -> 33.

Witness W1 (33 triples):
(1,4,12),(8,9,10),(10,13,15),(4,7,11),(0,2,7),(0,6,15),(7,12,15),
(3,4,14),(8,11,14),(7,10,14),(2,6,11),(3,9,13),(6,9,14),(0,3,10),
(5,8,12),(4,6,13),(3,6,8),(0,11,13),(1,9,15),(5,11,15),(0,4,5),
(0,1,14),(3,11,12),(2,12,14),(3,5,7),(0,9,12),(2,4,9),(6,10,12),
(2,5,13),(4,8,15),(2,3,15),(1,6,7),(1,10,11)

Witness W2 (33 triples):
(3,11,15),(0,2,15),(3,4,6),(0,7,9),(5,8,11),(1,10,15),(1,9,12),
(5,12,14),(1,7,14),(1,6,11),(5,9,15),(2,6,9),(5,10,13),(7,10,12),
(3,13,14),(3,8,10),(2,4,14),(0,1,8),(1,2,3),(7,11,13),(4,7,8),
(4,10,11),(1,4,13),(2,8,12),(0,4,5),(8,9,13),(8,14,15),(9,10,14),
(0,3,12),(4,12,15),(3,5,7),(0,11,14),(0,6,10)

## Proof / Evidence
Lemma 1 (packing): each of W1, W2 covers exactly 99 distinct pairs
(3 per triple, no repetition). Direct enumeration; verifier asserts
|pairs| = 99.
Lemma 2 (five-free, PPC <= 4): neither witness contains 5 pairwise
disjoint triples. Exhaustive search over all C(33,5) = 237,336 five-tuples;
every five-tuple has two triples sharing a point.
Lemma 3 (PPC == 4): enumeration over C(33,4) = 40,920 four-tuples gives
269 disjoint 4-sets in W1 and 266 in W2, so maximum PPC size is exactly 4.
Lemma 4 (non-isomorphic pair): sorted point-degree multisets are
W1: [5,5,5,5,6,6,6,6,6,7,7,7,7,7,7,7],
W2: [4,5,5,6,6,6,6,6,6,7,7,7,7,7,7,7].
They differ (W2 has a degree-4 point; W1 minimum degree 5), so no
point-permutation carries one to the other.
Lemma 5 (ceiling): each point lies in at most floor(15/2) = 7 triples;
3B <= 16*7 = 112 gives B <= 37 (Schoenheim bound).
Theorem follows from Lemmas 1, 2, 5 (L=33, U=37). All claims replay in
seconds via `python3 output/artifacts/verify.py` (stdlib only) -> VERIFY_OK.
Independently re-checked by the auditor with separate pair/disjointness code.

## Limitations
Exact beta(4,16) is NOT determined; values 34-37 remain open. No
branch-and-bound UNSAT log above 33 is offered. The upper bound 37 is the
trivial unconstrained ceiling, not a PPC-specific counting bound. Witnesses
are computer-found by random-order greedy packing with incremental
five-disjointness rejection; no structural explanation of the 33 barrier is
given. Heuristic saturation near 33-35 over ~10^4 trials is conjecture only.

## Reproducibility
Run `python3 output/artifacts/verify.py` (stdlib only, seconds-scale).
Expected tail output: VERIFY_OK with per-witness lines (triples=33,
pairs=99, five-free, PPC==4 with #4-sets 269/266, degree sequences) and
recomputed Schoenheim ceiling 37.

## References
- D. R. Stinson, On partial parallel classes in partial Steiner triple
systems, arXiv:2007.11033. beta(rho,v) theory; Thm 2.4 lower bound,
Thm 3.2 counting upper bound; sequenceable-PSTS applications.
- F. Demirkale, D. Donovan, M. Grannell, Enumerations of maximum partial
triple systems on 16 and 17 points, arXiv:1708.07646. MMPTS(16/17) census
with Pasch/mitre/Fano/automorphism tables; no parallel-class column.
- D. Bryant, D. Horsley, Steiner triple systems without parallel classes,
arXiv:1407.5766. Motivation (packing-side analogue at even order).
- B. Alspach, D. L. Kreher, A. Pastine, Sequencing partial Steiner triple
systems. Downstream use of bounded-PPC packings.
