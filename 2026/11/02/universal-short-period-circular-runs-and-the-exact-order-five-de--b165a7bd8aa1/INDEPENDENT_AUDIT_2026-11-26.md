# Independent mathematical audit

## correctness

PASS

The repaired RESULT.md retains the q-ary run theorem and removes the misleading first-variation framing. The global period q^n cannot be a maximal finite run period, and a smaller period p cannot persist to length n+p without duplicating an n-window. Fine–Wilf shows the square of a primitive p-word has least period p; a nonprimitive p-block would make its entire repeated interval have a smaller period. Exactly one run grows from each positioned primitive square with a preceding mismatch, because right extension is deterministic and terminates. Every length-t detector with t≤n has q^(n−t) occurrences; counting one outside mismatch proves the total, and counting both proves the exact lengths and, by subtracting a geometric sum, the long tail. The binary order-four examples have sixteen distinct windows; the two primitive alternating squares are adjacent in the first and separated in the second, yielding respectively one and two period-two runs. As a check on the frozen but now credited n=5 census, an independent Euler-edge DFS fixing 00000 for rotation explored 92,636 nodes and returned 2,048 distinct cycles, each directly scanned at every start and every possible run length 2–8 for least period and both maximality conditions. It reproduced all six multiplicities, the total frequencies (1008,736,304), and 25,920 positioned runs. Replay from /workspace/branches/1e63b5f9-acc3-4c49-9710-3ecdb9b5010b: python3 order5_dfs_scan.py --order 5; recorded census.json. This verifies a finite census, not the unbounded theorem; the uploaded checker was inspected rather than executed.

## originality

PASS

The frozen record's featured order-five census is covered exactly by distinct indexed result 0ff31e943bf5 and is explicitly removed from the repaired Finding's novelty claim. The surviving arbitrary-q exact period-and-length law was compared to that source and to general runs theory; the finite result does not imply it and the general results supply component lemmas, not the family-specific counting bijection. The repaired theorem makes no claim of priority for Fine–Wilf, Möbius inversion, or de Bruijn short-factor uniformity.

## value

PASS

After dropping the already known finite distribution, the structural result remains a complete universal short-period baseline for a canonical maximally diverse word family. The start criterion separates runs whose frequencies are fixed by local word balance from longer periodic features that genuinely vary; two-sided blocking also yields a full short-length histogram and exact remaining tail rather than just a total or a primitive-word count. These exact values are natural checks for circular repetition algorithms and higher-order studies. No value is attributed to recomputing the previously known order-five table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
