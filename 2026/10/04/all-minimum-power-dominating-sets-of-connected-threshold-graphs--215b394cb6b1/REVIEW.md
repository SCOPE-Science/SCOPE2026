# Review

## Correctness
PASS. The proof uses only the canonical threshold adjacency rules and the standard power-domination process. The one-block case is characterized by the presence or absence of a later false-twin pair; the \(A_1\) case has the analogous obstruction and an explicit forcing chain; and any \(A_i\) with \(i\ge2\) stalls immediately because every observed one-block vertex has at least two unobserved neighbors. The universal final one-block proves \(\gamma_P(G)=1\). Exhaustive replay through order \(12\) agrees with the theorem on every singleton.

## Originality
PASS with a stated residual risk. The founding literature defines power domination and the split-graph literature gives complexity results, but those statements do not imply which vertices of a threshold graph are optimal singleton PMU locations. The closest threshold-specific result located states polynomial-time solvability for minimum connected power domination on threshold graphs; the accessible abstract and preview do not state the creation-block iff criterion or the exact count. The unavailable threshold-specific full section is therefore recorded as a residual risk rather than treated as negative evidence.

## Value
PASS. Although \(\gamma_P(G)=1\) itself follows immediately from the universal final one-block, identifying every optimal location is not determined by that scalar fact. The theorem gives a sharp structural suffix rule and exact multiplicity, quantifying placement flexibility in a natural graph class used in power-domination algorithmics.

## Closest literature and limitations
The closest sources are the split-graph complexity theorem of Liao--Lee and the threshold-graph polynomial-time connected-power-domination result of Goyal--Panda. The present claim is narrower in graph class but stronger in output: it classifies every optimum singleton and counts them. It does not address nonminimum sets or propagation time, and the unavailable threshold-specific section of the closest connected-power-domination paper remains the principal literature risk.

Same-model review: passed. Independent audit: not yet performed.
