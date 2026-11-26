# Independent mathematical audit

## correctness

PASS

For each literal nonempty factor of a rotation (length at most the word length), hitting its union of cyclic occurrence positions is equivalent to hitting one occurrence. I generated coverage sets from all rotation prefixes, with positions reduced modulo the length. After dropping redundant supersets, each pair is tested for unhit sets; each possible larger third position lies in the intersection of precisely those sets, giving each triple once. Finite replay: python3 /workspace/branches/independent_replay.py 4. At lengths 4,13,40,121 the distinct-factor counts are 13,124,1159,10582 and the complete pair counts are 3,3,1,0. Both letters exclude any singleton. The five published factors have exactly the stated start lists (including the wrap at 120), and no pair meets all five coverages. The full test finds 546 triples and verifies {0,16,80}. Positions are in the fixed representative, not counted modulo rotation. The frozen output's triple zeroes at stages 1–3 are placeholders for triples not tested, not part of the claim. Nothing is asserted about stages above four.

## originality

PASS

No inspected statement covers the finite circular transition and exact optimum census. The closest overlapping sources study the same morphism in a different (linear) model, or the same circular invariant on a different word family. An algorithm giving a generic check is not an already established classification or the particular five-factor obstruction.

## value

PASS

The initial iterates of a standard morphic construction supply a natural threshold question, not a choice of arbitrary words. The five-factor obstruction explains the first failure of size two in small cyclic intervals; the exact count and witness distinguish the new optimal layer from the earlier unique optimal pair. These are usable benchmarks for structural and computational work on later Chacon stages, without an all-stage conjecture being assumed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
