# Kirkman resolvability dichotomy for two cyclic STS(15) representatives on Z15

## Context
A Steiner triple system STS(v) is a set of 3-subsets (blocks) of a v-point set
in which every pair of points occurs in exactly one block. Necessary and
sufficient existence: v = 1 or 3 mod 6 (Kirkman 1847). For v=15 there are
80 nonisomorphic STS(15)s, of which 7 are resolvable (Kirkman triple systems
KTS(15): blocks partition into parallel classes, each covering all points).
Order 15 is the smallest order where resolvability nontrivially distinguishes
isomorphism types. Prior sources give only general existence/counts and one
letter-labelled schoolgirl table — not replayable parallel-class decision logs
for the two named cyclic (difference-family) representatives below.

## Definitions
- Point set: Z15 = {0,...,14}.
- System B: cyclic development of base triples {0,1,4}, {0,2,8} plus short
  orbit {0,5,10} (each full-orbit base yields 15 blocks; short orbit yields 5;
  total 35).
- System A: cyclic development of {0,1,4}, {0,2,9} plus short orbit {0,5,10}
  (35 blocks).
- Parallel class: 5 pairwise-disjoint blocks covering Z15.
- Kirkman resolution: partition of all 35 blocks into 7 parallel classes.

## Result (verified computational theorem)
On Z15:
- System B is an STS(15) and is resolvable (Kirkman): exactly 56 parallel
  classes; exactly 240 distinct 7-class resolutions. One explicit resolution:
  1. (0,1,4),(2,3,6),(5,7,13),(8,9,12),(10,11,14)
  2. (0,2,8),(1,3,9),(4,11,13),(5,12,14),(6,7,10)
  3. (0,3,14),(1,2,5),(4,6,12),(7,8,11),(9,10,13)
  4. (0,5,10),(1,6,11),(2,7,12),(3,8,13),(4,9,14)
  5. (0,6,13),(1,7,14),(2,9,11),(3,10,12),(4,5,8)
  6. (0,7,9),(1,12,13),(2,4,10),(3,5,11),(6,8,14)
  7. (0,11,12),(1,8,10),(2,13,14),(3,4,7),(5,6,9)
- System A is an STS(15) and is not resolvable: exactly 11 parallel classes;
  0 ways to partition its 35 blocks into 7 disjoint parallel classes
  (certified by exhaustive exact-cover search).
- Automorphism orders: |Aut(B)| = 20160 (point-stabilizer 1344 x 15
  translations); |Aut(A)| = 60 (stabilizer 4 x 15). Hence the systems are
  non-isomorphic, and resolvability distinguishes their types.
- Cyclic-class census: among triples containing 0 paired with the fixed short
  orbit {0,5,10}, exactly 36 unordered generator pairs yield STS(15)s; under
  x -> u*x+t (u a unit mod 15) they split 18/18 into two classes containing
  B and A respectively.

## Proof / evidence
Computation, independently re-derived from generators with stdlib Python only:
1. Rebuild each 35-block list by cyclic development; STS audit: 35 blocks,
   all C(15,2)=105 pairs covered exactly once.
2. Enumerate parallel classes by smallest-uncovered-point backtracking and
   independently by brute-force C(35,5) partition test: 56 (B) vs 11 (A).
3. Decide resolution by exact cover of the 35 blocks with the parallel-class
   family; independent MRV recount confirms 240 (B) vs 0 (A).
4. Automorphism orders by point-stabilizer backtracking with pair-third
   propagation (calibrated on Fano STS(7): stab 24); translations verified as
   automorphisms of both systems, so |Aut| = 15 x stab by orbit-stabilizer.
5. Cyclic census by enumerating all 91 choose-2 pairs with (0,5,10) and
   partitioning under multipliers+translations.
Reproduction: `python3 artifacts/verify.py` prints
`B: ... npcs=56 resolvable=True ... nsol=240 stab=1344 aut=20160`,
`A: ... npcs=11 resolvable=False ... stab=4 aut=60`, then ALL CHECKS PASSED.

## Limitations
Computational certificates for the two named cyclic representatives only.
No claims about the remaining STS(15)s or about numbered catalog entries
(#61 etc.). Automorphism numbers rest on backtracking search correctness
(Fano-calibrated, translation cross-checked), not a separate proof kernel.

## Reproducibility
stdlib-only `artifacts/verify.py` plus `blocks_A.json`, `blocks_B.json`,
`parallel_classes_A.json`, `parallel_classes_B.json`, `resolution_B.json`.
Design checks take seconds; full replay including automorphism orders takes
about a minute.

## References
- Kirkman, T. P. On a problem in combinations. Cambridge and Dublin Math. J.
  2 (1847), 191-204.
- Ray-Chaudhuri, D. K. and Wilson, R. M. Solution of Kirkman's schoolgirl
  problem. Proc. Sympos. Pure Math. 19 (1971), 187-203.
- Mulder, P. Kirkman-Systemen. PhD dissertation, Groningen, 1917; Cole, F. N.
  Kirkman parades. Bull. Amer. Math. Soc. 28 (1922), 435-437 (7 KTS(15)s).
- Tonchev, V. D. and Weishaar, R. S. Steiner triple systems of order 15 and
  their codes. J. Stat. Plan. Inference 58 (1997), 207-216.
- MathWorld: Kirkman Triple System; Steiner Triple System; Kirkman's
  Schoolgirl Problem. OEIS A030129 (80 STS(15)s).
- Costa, S. and Pavone, M. arXiv:2408.03743 (F21 for KTS #61 — backdrop only).
- Heinlein, D. and Ostergard, P. R. J. arXiv:2303.01207 (STS enumeration).
