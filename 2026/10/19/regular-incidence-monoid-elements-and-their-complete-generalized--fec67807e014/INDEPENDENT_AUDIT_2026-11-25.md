# Independent mathematical audit

## correctness

PASS

The four displayed formulas, the fixed-support double-unit orbit and the group-inverse assertion in the source are correct. The accompanying qualification about orientation dependence of the numerical inverse refinements is false for the displayed counts: all four depend on the support and on undirected internal and crossing edge counts only. The complete corrected RESULT.md also makes the weighting in the ordered-pair sums explicit. Rechecking it, the unit Peirce elimination is internal to the algebra and the zero-diagonal Schur complement cannot be both nonzero radical and regular (iterate s=sbs in the radical filtration). The free coordinates give the support count; transporting inverses to e_T fixes the TT block and then either determines the ZZ block for reflexivity or restricts its Schur complement to units for invertibility. For commutation, use rank |T| and algebraic zero multiplicity |Z| to obtain a semisimple zero part; the polynomial group inverse belongs to the algebra. These arguments include both empty corners. Independent Bernoulli selection of Z reduces the total to a product over unordered edges; single edges, incident pairs, and triangles contribute respectively -m/q^2+m/q^3, w/q^3, and -tau/q^3 through degree three in 1/q. An independent inline exact F2 replay (no persistent script) checked all 16,384 ordered pairs per example and every support in the star and fence, obtaining 91/341 and 89/337 regular elements/reflexive pairs. The frozen CHECK.py is a separate replay path, inspected but not executed. Finite tests do not prove the general claim.

## originality

PASS

Pass for the joint all-poset finite-field inverse spectrum and its numerical graph invariance and graph expansion, not the Peirce method, orbit terminology, or the isolated star/fence example. Actual available work overlaps the height-at-most-two regular totals, orbit geometry, and the triangular setting, but does not establish prior coverage of this joint counting statement. This is a best-of-knowledge decision after bounded lawful access attempts.

## value

PASS

The joint support spectrum addresses natural differences among inner, reflexive, and unit inner inverse equations inside a pattern algebra. It gives exact probabilities and pair totals without exhaustively enumerating matrices. The same graph governs all scalar refinements, and the triangle/incident-pair correction explains why size and ambient dimension alone do not determine even the regular fraction. The value is the uniform graph-sensitive enumeration, not the use of familiar elimination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
