# Review

## Correctness
PASS. In the balanced case the first round separates degree classes and the only remaining symmetry is reflection of the spine together with permutations of pendant leaves; refinement advances one step from each branching end per round, so the final strict split is exactly at the midpoint. In the unbalanced case the two branching vertices already have distinct degree colors in round \(1\), the two leaf sets split in round \(2\), and two distinct boundary colors propagate inward along the spine; the last path split occurs in round \(\lceil L/2\rceil\). Taking the maximum with the unavoidable leaf-split round gives the stated formula. The resulting cells coincide with the explicit automorphism orbits. A full-graph checker confirms 14,440 parameter triples.

## Originality
PASS with residual priority risk. published-finding corpus searches for double-broom/bistar color refinement and orbit partitions returned no matching finding. Public searches found standard double-broom work in extremal graph theory, reconstruction, spectral graph theory, and later metric/random-walk settings, but no \(1\)-WL stabilization formula. Tiner's full text was inspected at its definition and problem statement; it concerns the Erdős--Sós conjecture, not color refinement. Krebs--Verbitsky supplies the general iteration-depth framework without a double-broom specialization. The current and prior ledgers contain exact results for other tree and unicyclic families, plus a universal tree upper bound, but no double-broom exact law.

## Value
PASS. Double brooms are a standard named extremal tree family rather than an ad hoc parameter slice. The theorem gives a complete exact iteration law on the natural nondegenerate family and exposes a sharp balanced-versus-unbalanced phase change: breaking the reflection symmetry changes both the propagation geometry and the mandatory leaf-split round. The accompanying exact orbit classification adds a structural interpretation beyond a bare depth computation.

## Closest literature and limitations
The closest object-specific source is Tiner's 2015 double-broom paper, with Ma--Shi--West's 2015 reconstruction paper as another standard-family source. Krebs--Verbitsky is the closest methodological source. None of the inspected or retrieved material states the present stabilization formula. Cases with a one-leaf broom head are excluded because the head then merges with the degree-\(2\) spine at the first round.

Self-review: passed. Independent audit: not yet performed.
