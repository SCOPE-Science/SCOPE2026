# Independent mathematical audit

## correctness

PASS

For one/two update images, labeled de Bruijn graphs have 4/16 vertices encoding length-3/5 input windows. A finite output word is present iff a corresponding labeled path exists, because every finite input block extends to a bilateral configuration. Subset transitions from all vertices recognize exactly both image languages. Paired-subset BFS over the finite reachable graph either returns a provably shortest accepted-at-one/rejected-at-two word or exhausts states proving equality for every finite word and hence closed subshift equality; no unbounded experiment is inferred from a cutoff. A fresh independent implementation of all 256 rules reproduced 72 stable, 184 shrinking, the entire twelve-length histogram, two extremizers and max 252 reached subset pairs. The supplied classification.csv agrees with this independently computed result.

## originality

PASS

Best-of-knowledge originality: Published process-graph methods and Rule126 graphs do not supply the complete 256-rule shortest image-language discrepancy census.

## value

PASS

This is a complete natural finite classification of the first two image subshifts for every elementary CA; a sharp 12-symbol worst-case observability threshold and equality census are useful exact invariants, not a narrow arbitrary slice. The finite family is exhaustively certified by an unbounded-language finite-state decision, not merely short-word tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
