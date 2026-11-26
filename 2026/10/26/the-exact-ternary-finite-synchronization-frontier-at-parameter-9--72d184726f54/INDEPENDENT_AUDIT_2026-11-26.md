# Independent mathematical audit

## correctness

PASS

Insertion/deletion distance on adjacent nonempty factors with total length L is L−2 LCS, giving the strict integer test 20 LCS < 9L. All earlier endpoints survive extension, so the new right endpoint suffices, and a missing length 33 also excludes every greater length. The canonical first-occurrence renaming is unique; no reversal quotient is used. I independently enumerated all labeled extensions with a bit-parallel LCS implementation cross-checked against explicit intersections of short subsequence sets. A split was skipped only when even its shorter side had length strictly below the forbidden threshold. The labeled counts at lengths 8, 31, 32, 33 were 78, 66, 60, 0. Normalizing the 60 length-32 words by all six letter permutations gave exactly the ten strings in RESULT.md, all using three letters. Replay: python3 /workspace/review-replay.py 2. This is an exhaustive finite computation and not a theorem about the optimal infinite-word parameter.

## originality

PASS

No earlier source checked covers the exact strict 9/10 frontier and its ten strict maximizing classes. The older literature gives the method and eventual impossibility, or studies a different set of splits. An earlier Resultary census is for the stricter 7/8 condition. The later-listed 059137292ffd covers the strict 32/33 cutoff via a weak-threshold upper bound and gives the very same list as weak survivors; the independently checked strict classification confirms that none of those ten are lost under strictness. This overlap is substantive, not a merely similar title; the catalogue dates alone do not settle priority or dependence.

## value

PASS

A fixed one-tenth normalized edit-distance gap on the smallest relevant alphabet gives a finite design obstruction not measured by the infinite threshold. The exact cutoff and complete list answer feasibility and identify every optimal short-block design at this gap, rather than giving a sample witness or repeating the asymptotic obstruction. The value is specific to this parameter, not a claim that it improves the published infinite-word threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
