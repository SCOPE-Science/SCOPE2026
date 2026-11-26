# Independent mathematical audit

## correctness

PASS

The complete corrected result is repairs/5/RESULT.md. It retains the all-start sharp bound and marks the already covered aligned calculations as background. For the binary alphabet, one symbol can be selected from each greedy arch; taking instead the closing symbols of all arches and then a bit absent from the rest produces a missing subsequence. The odd-part rule gives the four block shapes. Pending zero and empty input give the same state after the initial zero in a complete block; this supplies the third incoming state. Telescoping then leaves 3K minus the final bit plus the incoming pending-one flag, and the final state is determined solely by the last bit. Thus replacing any K≥1 complete middle blocks by one with the same last bit leaves 8ι−3N invariant. Every nonempty window either lies within one block, touches two consecutive blocks, or has such a middle. The independent run-boundary reconstruction, replayable with python3 /workspace/audit-evidence/paperfolding.py, checked all 12 block transfers and the 144, 1024 and 2048 endpoint cases, respectively giving extrema (−10,6), (−11,7), (−11,7). The endpoint cases are an exact covering superset, not a finite-prefix test. The same script generated both literal factors from the odd-part definition, found all length-five subsequences, and found the missing length-six words 100110 and 000100, respectively. Both constants are attained. The frozen verifier and notes were inspected but the uploaded script was not executed.

## originality

PASS

For the original, the exact length-8J prefix law is explicitly covered and the aligned dyadic formula is directly implied by the earlier block transfer. That original scope is not passed. The corrected result confines the contribution to the sharp discrepancy for arbitrary starting positions and lengths; neither the earlier exact prefix record nor the inspected primary results determine the needed factor boundary behavior or the optimal endpoints.

## value

PASS

The surviving result answers a natural uniform-in-start quantitative question for a canonical infinite word. It identifies both optimal integer endpoints of the deviation and witnesses on actual factors, not merely a bounded prefix error or an estimate derived by subtracting prefix sizes. The aligned formulas are background, not offered as value added.

The dated certificate retains the supplied scientific assessment, sources and limitations.
