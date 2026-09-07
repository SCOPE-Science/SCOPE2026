# Slow-reset census for binary one-cluster synchronizing automata on 8 states with a prime 5-cycle

## Context

The Cerny conjecture (1964) asserts every synchronizing deterministic automaton
on n states has a reset word of length at most (n-1)^2 (49 for n=8) and remains
open. Steinberg (2011) proved the bound for one-cluster automata whose unique
cycle has prime length, but gave only an upper bound with no exact small-n
maxima or extremal catalog. General surveys (Kisielewicz-Kowalski-Szykula) target
unrestricted and Cerny-cyclic classes. The (n=8, binary, one-cluster, 5-cycle)
slice was unsurveyed. Relevant benchmarks for n=8: Cerny 49, aperiodic
universal bound n(n-1)/2 = 28.

## Definitions

- Q = {0,...,7}, Sigma = {a,b}, deterministic complete DFA.
- Letter a is one-cluster of 5-cycle type: its functional digraph has exactly
  one directed cycle, of length 5. Up to relabeling the cycle is
  0->1->2->3->4->0, so a = (1,2,3,4,0,a5,a6,a7).
- rt(A) = length of the shortest reset word (merging all states to one).
- Slice maximum M = max rt(A) over synchronizing automata in this slice.
- Perm-b sub-slice: b restricted to a permutation (40320 maps).

## Result

**Theorem (machine-checked, independently reproduced).** There exists a
synchronizing binary DFA on 8 states with one-cluster letter a of 5-cycle type
whose shortest reset-word length is exactly 34:

- a = (1,2,3,4,0,0,5,6)
- b = (1,7,3,4,0,2,5,6) (a permutation; as a map it is the 8-cycle
  0->1->7->6->5->2->3->4->0)
- w = aaabaabaaaabaabaaaabaabaaaabaabaaa (|w| = 34), resetting to {0}.

No shorter reset word exists. Hence M >= 34, exceeding the aperiodic bound 28
and attaining 34/49 ~ 69% of the Cerny bound. Prime-cycle restriction therefore
still permits super-aperiodic slowness.

**Proposition (exhaustive sub-slice maximum, independently reproduced).**
Over the sub-slice where b is a permutation (14 canonical a-types x 40320 b =
564480 automata; 550796 synchronizing, 97.58%), the maximum shortest reset
length is exactly 34, attained uniquely (up to the fixed canonicalization) by
the automaton above.

**Catalog.** A certified top-10 list (all b permutation, all verified forward +
reverse) with (rt, a, b, shortest word, BFS counts): 34, 33, 32, 32, 31, 31,
31, 31, 30, 29 (full table in artifacts/catalog_top10.json, headed by the main
witness).

## Proof / evidence

1. Synchronizability: pair-automaton BFS on 64 ordered pairs; all 28 unordered
   pairs reach the diagonal.
2. Exact rt: BFS on the power automaton (2^8 = 256 bitmask subsets) forward
   from FULL={0..7} until a singleton is reached, with parent pointers to
   extract a shortest word; cross-checked by reverse BFS from the 8 singletons.
   For the main witness both give 34; 248 of 256 masks are forward-reachable
   (full distance table in artifacts/dist_main.json).
3. Replay: direct simulation of w collapses all 8 states to {0}; no proper
   prefix resets (first-reset prefix 34).
4. Enumeration: of 512 assignments of (a5,a6,a7), 320 keep the one-cluster
   5-cycle property; under 5-cycle rotation plus permutation of {5,6,7} they
   fall into 14 canonical classes (explicit list verified by orbit computation).
   Exhaustive power-automaton BFS over all 14x40320 perm-b automata gives max 34.
   Mixed random survey (484000 trials, seed 12345) plus ~318k iterated-local-
   search kicks found nothing longer; this negative evidence is not claimed as
   proof for arbitrary b.
5. Independent verification: artifacts/replay_verify.py (stdlib only, <2 s)
   replays w, checks one-cluster/permutation properties, prefix minimality,
   recomputes both BFS directions, and compares against the stored distance
   table. All 7 checks pass. The auditor additionally reproduced the full
   564480-automaton census from scratch (~32 s) with identical totals and
   maximum.

## Limitations

- The exact full-slice maximum M (arbitrary b, 8^8 maps per a-type) is not
  determined; only M >= 34 and perm-sub-slice maximum = 34 are proved.
  A non-permutation b with rt > 34 remains possible.
- Isomorphism reduction of a to 14 classes is machine-enumerated
  (rotation + S3 canonicalization), not hand-proved.
- No claim of scholarly priority is made; originality rests on cutoff
  knowledge (live literature fetches failed in-sandbox) and on explicit
  checkable artifacts.
- Wall-clock figures are machine-specific.

## Reproducibility

CPython 3.x, stdlib only. Run `python3 artifacts/replay_verify.py` (<2 s).
Artifacts: artifacts/witness_main.json (a, b, w, L),
artifacts/dist_main.json (248-entry forward distance table),
artifacts/catalog_top10.json (top-10 with words and BFS counts),
artifacts/survey_log.json (counts, seeds, timing, method record).

## References

- B. Steinberg, The Cerny conjecture for one-cluster automata with prime
  length cycle, arXiv:1107.3051 (2011). Upper bound (n-1)^2 for this regime;
  no exact n=8 k=5 census.
- Kisielewicz-Kowalski-Szykula, Experiments with synchronizing automata /
  Synchronizing automata with extremal reset length, arXiv:1309.0044.
  Heuristic/exhaustive search in unrestricted and Cerny-cyclic classes.
- M. Volkov, Synchronizing automata and the Cerny conjecture (survey).
  General bounds and slowly synchronizing series; no tight prime-5-cycle value.
- Standard bounds for n=8: Cerny (n-1)^2=49; Kari Eulerian; Trahtman/Rystsov
  aperiodic n(n-1)/2=28.
