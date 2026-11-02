# Scientific review

## Correctness — PASS

The result is an all-defect, all-semilength theorem, not a finite-sequence extrapolation. Ordinary greedy-arch factorization identifies universality index with completed arches [1,2]. Each adjacent input pair completes zero or one arch; inspecting the nine state/block possibilities yields the full transition table. A first visit to a new paired-height maximum must use a no-completion \(00\) step, forcing height at most defect; the proof handles initial state and boundaries, including the empty word and the forbidden \(10\) at paired height zero. Exactly \(d\) no-completion blocks are then counted by the stated bounded transfer matrix, proving rationality and making the four explicit series finite exact algebra. Verified direct enumeration of 82,500 paths (semilength at most 11), pair DP to 80, and symbolic matrix simplifications for defects 0–3. Residual correctness risk: implementation cross-checks are finite; the infinite assertion rests on the structural proof, as appropriate.

## Originality — PASS, qualified

The relevant primary full HTML for Adamson et al. [1] discusses subsequence-universal *regular* languages, not the nonregular Dyck class or this arch-deficit bounded-height reduction. Fleischmann et al. [2] introduce and analyze arches and the missing-subsequence-count parameter, not the semilength-minus-index distribution. Earlier published records for unrestricted binary universality, shortest absent subsequences, and primitive Dyck finite cores do not imply this classification without additional reasoning. Importantly the defect-two coefficient sequence is *not numerically new*: it agrees with OEIS A001793 [3], which lists a Dyck pyramid-weight interpretation. Its underlying pathwise statistic differs, so this coincidence leaves the general theorem and defect-three formula unaddressed. Residual risk: a broad lattice-path statistic identity or unpublished specialty formula could imply some or all of these results; this is not a proof of universal novelty.

## Value — PASS

The invariant is a natural measure of loss of scattered-read coverage under a balanced-parenthesis constraint; binary index alone is well established, while the Dyck constraint introduces an unbounded-stack obstacle. The structural height-versus-defect bound proves that every fixed loss level is a finite-state stratum, gives a constructive exact counting algorithm for any defect, and makes the near-maximal universal Dyck words exponentially rare among Catalan paths. The third-defect formula and uniform mechanism go beyond merely rediscovering a listed integer sequence.

Self-review: passed. Independent audit: not yet performed.

### Scientific limitations

No joint-bivariate rationality and no independent external validation are claimed. Algebraic simplification for the four displayed rational functions can be replayed with an optional SymPy program; all finite word/transfer checks require only Python's standard library.
