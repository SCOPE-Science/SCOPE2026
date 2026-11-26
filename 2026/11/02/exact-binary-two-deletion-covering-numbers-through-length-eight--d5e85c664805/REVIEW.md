# Independent mathematical audit

## correctness

PASS

At length n the targets are precisely the 2^(n-2) binary words of length n-2, including the empty word at n=2. Incidence is ordinary subsequence containment: any length-n embedding of a target leaves exactly two positions unselected. I reconstructed this entire incidence relation independently via leftmost symbol matching, checked each cover printed in RESULT.md, expanded the weight prescriptions by canonical reversal/complement representative, and computed the exact total and per-source maximum. The pairs at lengths 6,7,8 are (8,3),(10,3),(74,12). For nonnegative weights, a cover must account for every target's weight at least once, so k members account for at most k times the cap, even if there are overlaps. The three ceilings are 3,4,7, matching the witnesses. At n=5 one word cannot contain both 000 and 111; at n=2..4 the nonempty-cover lower bound is sharp. The finite profile is (1,1,1,2,3,4,7). Replay: /workspace/review-work/small_checks.py deletion; output deletion_results.txt. No optimization tolerance, inference beyond the seven specified lengths, or classification of optimal covers is needed.

## originality

PASS

The complete initial binary arbitrary-two-deletion covering profile, particularly exact length-eight optimality, is distinct on inspected evidence. Existing deletion-covering definitions, general bounds, packing results, and a ternary two-deletion profile do not certify this result. The problem, set-cover bound and similar certificate methods are prior art.

## value

PASS

Minimum deletion covers are a standard directed covering invariant. The complete initial binary radius-two table includes a nontrivial 64-target optimum with a lower certificate stronger than generic volume bounds. The seven-word matching cover and small verifiable dual weights give an exact benchmark for finite deletion-cover constructions and bounds; the value does not rest on the trivial small lengths or on a claim to have invented the dual method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
