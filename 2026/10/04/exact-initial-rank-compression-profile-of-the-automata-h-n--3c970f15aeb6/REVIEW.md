# Review of Exact initial rank-compression profile of the automata \(H_n\)

## Correctness
PASS. The proof identifies \(b\) as the only rank-decreasing letter and its sole collision pair \(\{2,n\}\). It then proves a spacing lemma for effective uses of \(b\): the first two decreases cost lengths \(1\) and \(2\), while every subsequent decrease costs at least three further letters because a nonfirst effective \(b\) leaves both \(2\) and \(n\) absent. Equality rigidly forces \((bab)^{s-1}\). The explicit hole induction proves that this forced word attains deficiency \(s\) exactly through \(s=\lfloor n/2\rfloor+1\), and the next iterate supplies the strict saturation boundary. Exact power-automaton BFS for \(4\le n\le14\) and direct replay through \(n=300\) agree with every proved statement.

Risk: a transcription error in the family definition would invalidate the argument; this was controlled by comparing the transition formulas with the defining source and reconstructing them independently in the verifier.

## Originality
PASS. The 2013 primary source defines \(H_n\) and proves the endpoint reset threshold \(n^2-4n+6\), but not the intermediate-rank profile. The 2010 precursor explicitly postpones the corresponding unnamed \(n^2-4n+6\) series to an extended version. Semantic searches of the published published-finding corpus collection and web/literature searches for `H_n`, rank compression, deficiency, shortest rank words, and equivalent wording found no statement that implies the claimed profile. The closest published-finding corpus items concern a finite slow-reset census and the Černý-family avoiding threshold, neither of which implies this result.

Residual risk: an older or unindexed source may state the same profile under different notation. No search result established such coverage.

## Value
PASS. Rank-compression time is a natural structural invariant of a synchronizing automaton, and \(H_n\) is a classical named slowly synchronizing family. The result determines an entire parameterized initial profile, its unique optimal words, and the precise first point where linear compression saturates. It therefore describes structure not contained in the known endpoint reset threshold and is not a one-off table computation or arbitrary slice.

## Closest literature and limitations
The closest primary source is Ananichev–Gusev–Volkov, arXiv:1302.5793v1, Theorem 5, which proves the full reset threshold after defining \(H_n\). The 2010 precursor arXiv:1005.0129v1 announces a series at the same endpoint threshold but leaves it for the extended version. The present result does not determine larger deficiencies after the first saturation point and does not change the known reset threshold.

Same-model review: passed. Independent audit: not yet performed.
