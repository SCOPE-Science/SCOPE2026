# Review

## Correctness
PASS. The distance-
\(4\) condition makes every two-coordinate projection injective. A hypothetical size-
\(16\) code would therefore realize all \(16\) ordered pairs in every projection and hence contribute \(40\) equal-coordinate incidences. Symbol weight at most \(2\) permits at most two such incidences per word, giving at most \(32\), a contradiction. The displayed size-
\(15\) witness is checked directly. For size \(15\), each projection contains at least three diagonal pairs, so at least \(30\) incidences occur; the per-word upper bound gives at most \(30\), forcing the stated equality structure.

## Originality
PASS with residual search risk. The primary source arXiv:1110.0911 defines these symbol-weight codes, emphasizes finite optimal-size questions, and gives general bounds and larger examples, but no \((q,n,d,r)=(4,5,4,2)\) value was found in the inspected full text. The 2013 GBTD paper treats exact symbol-weight-code questions at different parameters. Targeted searches for the notation, expanded terminology, exact parameters, and the projection formulation returned no implication-equivalent result. The main residual risk is an unindexed small-parameter table or computation.

## Value
PASS. This is the smallest natural quaternary “one beyond the alphabet” optimal-symbol-weight setting \(n=q+1=5\) at Singleton distance \(d=n-1=4\). The result identifies an exact one-word deficit from the unrestricted Singleton ceiling and explains the obstruction by a structural incidence count. The forced equality pattern adds reusable information beyond a bare numerical search result.

## Closest literature and limitations
Chee–Kiah–Purkayastha supply the definitions, general bounds, and motivation for finite optimal symbol-weight codes. Chee–Kiah–Wang demonstrate that exact finite symbol-weight-code questions encode nontrivial design existence problems, but their exact computation is for a different ternary parameter set. No all-maxima classification is claimed here, and unindexed prior finite computations remain the main residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
