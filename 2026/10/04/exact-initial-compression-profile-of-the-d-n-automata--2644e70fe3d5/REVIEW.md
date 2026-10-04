# Same-model review

## Correctness
PASS. The proof isolates the only collision pair \(\{1,n\}\), proves the three-symbol spacing lower bound for effective rank drops, proves equality uniquely forces \(a(b^2a)^{s-1}\), and then derives an exact recurrence for the missing states. The residue-class orbit of that recurrence gives \(h_n\) and proves that the next forced equality word fails. Exhaustive power-automaton verification for \(4\le n\le18\) and direct replay through \(n=300\) agree with every asserted case.

## Originality
PASS. The 2010 source introducing \(D'_n\) and the 2013 extended treatment were inspected in full around the relevant family. They prove the total reset threshold \(n^2-3n+4\) and provide an endpoint reset word but do not state the intermediate rank-compression function, the unique words \(a(b^2a)^{s-1}\), or the mod-three stopping index. Searches using rank, deficiency, image cardinality, compression, and subset-synchronization aliases found no equivalent statement. Residual risk remains because search coverage cannot exclude older work under different terminology.

## Value
PASS. The result concerns a classical extremal family rather than an arbitrary slice. It identifies a rigid initial geodesic in the subset automaton and a sharp mod-three saturation boundary, clarifying how early rank compression differs from total synchronization in \(D'_n\).

## Closest literature and limitations
The closest literature is Ananichev–Gusev–Volkov, arXiv:1005.0129v1 and arXiv:1302.5793v2, which establish the reset threshold of \(D'_n\). The present result stops after the first failure of the linear profile and does not claim a formula for later deficiencies.

Same-model review: passed. Independent audit: not yet performed.
