# Independent mathematical audit

## correctness

PASS

An independent checker confirmed seven displayed blocks of 64 symbols, exact agreement with witness.txt, length 448, and the specified alphabet. Starting with the final four digits followed by all digits, a rolling 10-bit base-four register enumerates exactly one circular length-five factor per ending position, including wraparound. Each code was distinct from its reversal, and neither it nor its reversal was in the set of earlier codes. All 448 checks passed; each symbol occurs 112 times. The ASCII word without separators or newline has SHA-256 65a91ebd11f35aedfe544863a9aa615fa0a98274260626ee9259fdf40ae71117, matching the recorded digest. A smaller period would repeat a five-factor, so 448 is the least period. Replay with python3 /workspace/checks/5_witness_check.py; this uses only the standard library and the frozen witness and displayed blocks, not the uploaded checker. The published upper bound is independently sourced: Mitchell–Wild arXiv:2507.02526 Table 1 tabulates Theorem 2.22 and gives 452 at n=5,k=4; arXiv:2603.18646 Table 4 confirms the same bound. The combination gives 448<=lambda(5,4)<=452, not an exact maximum.

## originality

PASS

The strongest inspected publication for the same alphabet size and order constructs 404 and gives an upper bound of 452. Earlier constructions at these parameters give 372 and 360. Neither those lower bounds nor the upper bound imply a period-448 witness or a dominating lower bound. The strongest indexed nearby results change the alphabet or factor order. The verified improvement is 44 over the documented 404, with priority qualified by the search scope.

## value

PASS

This is a named extremal parameter already singled out by the benchmark literature, not an arbitrary search slice. The explicit, easily replayable word raises the documented lower bound by 44 and reduces the 48-position gap to four. The exact period is useful in its own right as a length guarantee for an orientable position-sensing word, without claiming a new general construction or maximum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
