# Review

## Correctness
PASS. For each choice of length-two and length-three layers, the available length-four layer is determined exactly by prefix/suffix exclusion. Because distinct equal-length words cannot be proper prefixes or suffixes of one another, every subset of the available length-four words is admissible, so maximizing the available count gives an exact necessary-and-sufficient profile test. The packaged verifier exhausts all \(4096\) shorter-layer selections and then the full profile grid, reproducing the stated table and the unique first obstruction \((2,0,5)\) at Kraft sum \(13/16\).

## Originality
PASS to the best of the performed literature and database checks. The 1999 two-length result and the 2023 three-distinct-length theorem guarantee existence through Kraft sum \(3/4\); the inspected statements do not classify the region above that threshold or state the exact table for lengths \(2,3,4\). Searches under fix-free, bifix, biprefix, and reversible variable-length aliases, plus exact multiplicity and \(13/16\) wording, found no covering table. The nearest computational record concerns the algorithmic implementation of the general \(3/4\) construction rather than this above-threshold profile frontier. Residual risk remains for an obscure historical enumeration.

## Value
PASS. The \(3/4\) guarantee is the central existence threshold in fix-free coding. The result gives the complete local geometry immediately around that threshold in the shortest genuinely three-level consecutive window: it identifies exactly how far individual profiles can exceed \(3/4\), and isolates the first discrete obstruction. This is a natural boundary classification rather than a recomputation of the known guarantee.

## Closest literature and limitations
Harada–Kobayashi gives the two-distinct-length \(3/4\) guarantee, and Congero–Zeger proves the full binary three-distinct-length \(3/4\) theorem. The latter was inspected at the definition, historical review, Theorems II.1 and III.1, construction sections, and references. The present claim is only for lengths \(2,3,4\) and makes no assertion about shifted windows or arbitrary profiles.

Self-review: passed. Independent audit: not yet performed.
