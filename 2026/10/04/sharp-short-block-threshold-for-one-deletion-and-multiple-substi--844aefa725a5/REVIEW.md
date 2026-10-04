# Review of Sharp short-block threshold for one deletion and multiple substitutions

## Correctness
**PASS.** The argument reduces every deletion/substitution output set to a contained radius-\(s\) Hamming ball by deleting one fixed coordinate. Pairwise disjoint channel balls therefore force prefix Hamming distance at least \(2s+1\). This is impossible below length \(2s+2\), and at the boundary it makes the first-coordinate map injective. The constant-word construction attains the resulting \(q\) upper bound. All quantifiers, including \(s=0\), are covered. Direct finite reconstruction of the channel corroborates the proof for \(0\le s\le2\) and \(2\le q\le3\).

## Originality
**PASS.** The closest primary source, arXiv:2005.09352 / DOI:10.1109/ISIT44484.2020.9174213, defines the same deletion/substitution channel and extremal question. The inspected conference-paper material gives its nonbinary one-substitution upper bound only for longer blocks and does not state the all-\(q\), all-\(s\) threshold above. DOI:10.1109/TIT.2022.3177169 concerns systematic multiple-deletion/multiple-substitution constructions rather than this exact short-block optimum. The 2023 journal extension was checked through public metadata/abstract but not in complete full text, leaving a residual literature risk. Exact-formula, threshold, and alias searches in a published-results database returned no statement implying the claim. A cumulative record of prior findings was also checked; the closest prior item determines binary one-deletion one-substitution optima at lengths seven and eight, which neither contains nor implies this all-parameter initial threshold.

## Value
**PASS.** The first block length supporting more than one codeword is a natural structural boundary of the channel, not an arbitrary finite parameter choice. The theorem determines that boundary and the exact optimum there simultaneously for every alphabet size and every substitution radius, giving a sharp complement to the longer-block and asymptotic emphasis of the cited coding literature.

## Closest literature and limitations
The closest literature is the 2020 foundational single-deletion single-substitution paper and its later systematic/generalized follow-ups. The result does not address longer lengths and does not claim that database searches establish novelty. An unindexed note, thesis, or differently worded elementary observation could contain the same threshold.

Same-model review: passed. Independent audit: not yet performed.
