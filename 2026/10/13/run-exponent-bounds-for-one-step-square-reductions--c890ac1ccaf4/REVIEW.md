# Independent mathematical audit

## correctness

PASS

This PASS is for repairs/4, not the frozen near-conjecture framing. The frozen numerical bounds are valid, but its assertion that the coefficient-one conjecture remains open and its alleged loss when counting period slots miss a stronger implication and a converse. For each root length p, shortened outputs at two square starts agree exactly when their intervening p-shift comparisons are all matches. This identifies the outputs with maximal p-match intervals of length at least p. Fine–Wilf forces the least period d of their factors to divide p, and a d-extension would be a p-extension, so these factors are runs. Conversely, on a d-run any p multiple of d with 2p<=|R| preserves the same boundary mismatches: each p-extension compares the same letter as the d-extension by periodicity inside the run. Thus every slot contributes exactly one output, with no cross-p collisions because output lengths differ. The prior disjoint-start inequality sum_R floor(e(R)-1)<=n-1 and floor(e(R)/2)<=floor(e(R)-1) for e(R)>=2 prove the repaired universal bound, also for n=1. The uploaded verifier was inspected and not run. The independent limited replay of the original proof checked 510 binary and 1,092 ternary words; the independently written repaired verifier checks exact equality and both bound steps on 4,094 binary and 3,279 ternary words (`python3 /workspace/repairs/4/verify.py`, verified CHECK_OK). The proof, not enumeration, supplies the unrestricted result. The corrected RESULT.md, VERIFICATION.md and verify.py are present; the original and its verification status front matter are preserved.

## originality

PASS

The supported distinct claim in the repair is the exact correspondence for distinct one-step shortened words, together with its implication of Conjecture 3 (in fact the n-1 bound). The proof credits the entire Lyndon charge bound to Bannai et al. and does not claim the run theory or the distinct-squares bound as new. No equivalent result for the repaired out-degree claim was established in the inspected literature or matching catalogue records. The most plausible alternate tandem-repeat formulation remains a named, material literature risk, not proof for or against originality.

## value

PASS

The repaired finding resolves the stated out-degree inequality on every alphabet and gives an exact per-word enumeration in terms of runs. In contrast to the frozen constants, the improvement removes a qualitative gap, and the equality explains precisely why two square occurrences can or cannot lead to the same shortened word. It is a structural reduction of a natural output-count problem, not a new name for the ordinary square vocabulary. No assertion that n-1 is the sharp extremal function is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
