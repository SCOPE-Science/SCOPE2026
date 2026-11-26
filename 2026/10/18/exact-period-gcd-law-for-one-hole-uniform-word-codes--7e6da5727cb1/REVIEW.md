# Independent mathematical audit

## correctness

PASS

For each boundary alignment, wholly observed blocks must avoid u and the two partial end blocks can always be extended to allowed blocks using the free symbol and |Σ|≥2. This includes the case of a word contained in one partial block. Thus a missing factor has an occurrence in every residue. Selecting one per residue gives a spanning path with gaps either proper periods or at least k+1; Kruskal's component numbers are the successive gcds, yielding the lower bound. Conversely, join translated copies of a subgroup path by positive steps p_i. Its endpoint shift within the smaller subgroup has no effect on the sequence of quotient cosets, and the last k+1-step stage generates the remaining quotient. Each stage yields exactly the recorded difference in copy-count-weighted component numbers. For any nonconsecutive overlapping copies the intervening gaps are all periods, and the sum below k is a period by chaining the defining symbol equalities. Hence all prescribed occurrences can coexist and attain the bound. The empty list and period-one cases, strict drop for a bordered word, and length-25 example check. Independent subset BFS on an explicit per-codeword path automaton confirmed all 241 binary holes at k=2–6 and ternary holes at k=2–4 combined; source scripts were inspected, not run. Replay: python3 /workspace/branches/independent_replay.py 3; output /workspace/branches/independent_replay.out.

## originality

PASS

The supported distinct claim is the exact formula for all one-hole fixed-length codes, in particular the interaction of multiple proper periods. The unbordered answer was already known, and the reduction to alignment obstructions is not itself novel. The frozen wording suggesting an independent second presentation is imprecise: Fici–Pribavkina–Sakarovitch explicitly attribute their proposition to Pribavkina (2009). No examined source covers the general bordered formula.

## value

PASS

This resolves the naturally parameterized shortest obstruction problem beyond the benchmark unbordered case. It gives a cheap computation from periods without materializing the allowed code and explains how successive periods affect attainable length. The matching constructive path proves the arithmetic is not just a lower bound or fit to small cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
