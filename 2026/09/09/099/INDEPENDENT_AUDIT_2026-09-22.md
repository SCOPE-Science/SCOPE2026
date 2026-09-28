# Independent audit — SCOPE-20260909-099

## Scope
Independent review of `2026/09/09/099` at tree `e7f6547a63c8ffd7db59cf5ca37f6401316bc4c5`.

## Correctness
**PASS.** An independent free-group implementation reproduces the core finite claims. For
`S={a,A,b,B,abAB,baBA}` there are no non-backtracking closed walks of length 3 or 4, while
`e -> a -> ab -> abA -> abAB -> e` has steps `a,b,A,B,baBA`, giving girth 5. The ordinary tree-metric ball `B_4(e)` has 161 vertices and 177 internal `S`-edges. An independent DSATUR search finds a proper root-0 3-coloring with class sizes 93/54/14 and no conflicts; the 5-cycle supplies the lower bound, so `chi(B_4)=3`.

Given the record's explicitly stated finite four-query game, the no-go argument is then immediate and correct: Player II can answer every queried vertex with the fixed global root-0 coloring, so no adaptive four-query Player-I strategy can force an improper partial coloring.

## Originality
**PASS, narrowly.** Targeted searches of Marks' determinacy paper and related Borel-combinatorics literature did not locate this exact commutator-augmented Cayley graph, its `B_4` chromatic certificate, or this finite query-game calculation. No priority is claimed for the general methods (free-group reduction, finite coloring, or determinacy games).

## Scientific value
**PASS, modest.** The finite computation is useful primarily as a falsification of a proposed depth-4 local spoiler route on a preselected generator set; it does not settle the infinite Borel/measurable chromatic problem. The exact 161-vertex certificate prevents repeating that finite search and records the first obstruction scale (`C_5`) for this literal local game.

## Terminology caveat
Marks' published method uses infinite games and Borel determinacy. The finite game in this record is a custom truncation. The record is acceptable because it explicitly defines the finite rules and limits the no-go to those rules; readers should not interpret the conclusion as a theorem about the full Marks game.

## Literature checked
- Andrew S. Marks, *A determinacy approach to Borel combinatorics*, JAMS 29 (2016), DOI 10.1090/jams/836; arXiv:1304.3830.
- Conley–Jackson–Marks–Seward–Tucker-Drob, *Hyperfiniteness and Borel combinatorics*, JEMS.
- Bernshteyn, work on distributed algorithms and descriptive combinatorics cited by the record.

## Limitations
No claim is made about `chi_B`, measurable chromatic number, or any infinite-game winning strategy. The scientific value is that of an exact finite obstruction/certificate.
