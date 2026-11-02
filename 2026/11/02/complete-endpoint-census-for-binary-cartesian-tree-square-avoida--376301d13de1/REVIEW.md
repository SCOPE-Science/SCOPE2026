# Review: endpoint classification for binary Cartesian-tree square avoidance

## Correctness

PASS. The claim is a finite exact classification of all valid words at the known sharp endpoint. The proof explicitly defines the ordered binary alphabet and leftmost-minimum Cartesian tree. Prefix closure makes the two-way extension recurrence exhaustive: all valid length-\(n\) words are generated, and a forbidden factor added by one symbol must end at the new position. Literal recursive tree comparison gives exactly \(20\) valid words at length \(29\) and none at length \(30\); hence longer valid words are impossible. The included independent parent-distance enumeration obtains the same layer counts and sorted endpoint-word SHA-256. The exact fixed-position template and its eight disjoint variable-pattern rules account for all \(20\) enumerated words. Code and recorded outputs are included and have been executed.

## Originality

PASS, subject to literature risk. Shibata et al., arXiv:2607.00674 (2026), Table 1 and Table 2 give the previously known maximum length \(29\) and **one** example, but not the count \(20\), a positional rigidity template, or an optimizer classification. Park et al., arXiv:1905.08974, define Cartesian-tree matching and give the parent-distance equivalence; they do not investigate this endpoint enumeration. Targeted equivalence, endpoint-count, parent-distance, research-record, and exact-phrase searches found no stated coverage of the census. A previously available yet uninspected accompanying code output or other scattered literature could have counted the same witnesses; this risk cannot be eliminated by negative search results.

## Value

PASS. The primary paper reports a sharp natural finite avoidability threshold, so the complete structure and multiplicity of **all** extremal words are motivated mathematical endpoint data rather than a selected arbitrary small instance. The result shows a rigid \(21\)-fixed-position skeleton, with only eight variable sites admitting \(20\) explicitly characterized fillings. This reveals the extent of extremal nonuniqueness and supplies fully reproducible boundary cases for the generalized-square-avoidance problem. It does not purport to resolve the open higher-alphabet cases.

## Closest literature and limits

The numerical maximum length \(29\) is prior work (Shibata et al.); its independent reproduction here is a completeness boundary, not the claimed novel part. The classification uses exhaustive finite computation and does not provide a short symbolic formula for every smaller length. External priority review remains necessary, especially for unpublished enumerator outputs or implicit tabulations.

Self-review: passed. Independent audit: not yet performed.
