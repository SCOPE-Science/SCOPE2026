# Review

## Correctness
PASS. The proof identifies the two kernel pairs of \(a\), proves by an exhaustive four-letter symbolic case split on \(R=\{1,\ldots,n-2\}\) that no post-\(a\) compression occurs in at most three letters and that four letters can lose at most one state, optimizes the resulting 1/2-state loss costs, and gives explicit hole-set inductions attaining both parity bounds. Exact BFS through odd \(n=17\) and witness replay through odd \(n=101\) agree with the formulas; those computations are checks, not the infinite proof.

## Originality
PASS. Targeted repository and literature searches under rank, image-size, deficiency, k-compressible, compressing-word, and subset-compression terminology found the \(B_n\) reset endpoint and general compression literature but not this exact half-range profile. The endpoint theorem does not imply the intermediate thresholds; the local spacing lemma plus periodic hole witnesses supply a distinct statement. Residual bibliographic risk is recorded.

Closest literature: the original Ananichev–Volkov–Zaks paper proves the complete reset threshold of \(B_n\), while the later Ananichev–Gusev–Volkov paper restates the same family and endpoint in the labeling used here. General collapsing/compressing-word literature asks universal or complexity questions. None of the inspected statements covers the exact early threshold profile proved here.

Residual risk: literature search cannot exclude an older equivalent formulation under different terminology, and two broader compression sources were available only at abstract/metadata level.

## Value
PASS. \(B_n\) is a classical slowly synchronizing extremal family built around a deficiency-two letter. Determining how quickly it can reach intermediate ranks is a natural refinement of its reset threshold, and the alternating exact marginal costs expose structure invisible in the endpoint value. The result is a parameter-uniform theorem rather than an isolated finite census.

Same-model review: passed. Independent audit: not yet performed.
