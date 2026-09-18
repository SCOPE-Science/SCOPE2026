# Same-model review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The central invariant is the singular support
\[
\sigma(a)=\{x:a_x\notin S^\times\}.
\]
For unit top components \(g\in R^\times\), wreath multiplication gives
\[
\sigma(a b^g)=\sigma(a)\cup g^{-1}\sigma(b).
\]
This uses only the finite-monoid fact that a product is a unit iff every factor is a unit. It yields a monotonic support obstruction: a word ending in a base element with one singular coordinate can use only relative generators carrying a single singular coordinate in the same unit-group orbit.

This gives the lower bound of one full relative generating set of \(S\) per \(R^\times\)-orbit, while projection to \(R\) independently forces \(\operatorname{rank}(R:R^\times)\) top generators. The construction with one local copy of each relative generator per unit orbit gives the matching upper bound.

The iterated formula follows recursively because the unit wreath product has orbit count equal to the product of the orbit counts of the factor unit groups.

Two adversarial boundary checks were made:

- if \(S\) is a group, \(c=0\), and the formula reduces to the top relative rank;
- if \(R^\times\) is transitive, \(q=1\), and the formula reduces to \(b+c\), exactly the form required by Lu's main full-transformation/symmetric-group application.

The 12-element counterexample to Lu's Lemma 3.2 was also exhaustively enumerated by the published script, which finds exact relative rank \(4\), not the asserted upper bound \(3\).

## Originality

**PASS, to the best of our knowledge.**

The relevant full text of arXiv:2609.20521v1 was inspected, especially Section 3. Lemma 3.2 assumes transitivity of the entire top monoid \(R\), and its proof uses arbitrary elements of \(R\) to move a local base generator. Lemmas 3.4 and 3.8 inherit that step. No orbit correction appears in the paper.

Targeted external searches used combinations of:

- `relative rank wreath product monoids group of units orbits`;
- `wreath product relative rank group of units semigroup`;
- `rank wreath product transformation monoids orbits generators`;
- `semigroup wreath product generation rank unit group orbit`.

The closest located prior work was Araújo--Schneider (2009) on uniform partitions and Araújo--Bentz--Mitchell--Schneider (2015) on arbitrary partitions. Their indexed statements concern specific partition-preserving transformation monoids and special wreath products; no general formula in terms of unit-group orbits was located.

The 2009 paper's arXiv abstract and Lu's description/reference to it were inspected, but its full text was not text-searchable through the sources used. That paper, older semigroup-generation monographs, or literature using different notation for semidirect/wreath products remain the main residual originality risk.

The originality claim does not include the standard finite-monoid unit fact, the definition of relative rank, the wreath-product construction, or Lu's main theorem for full transformation monoids and symmetric groups.

## Value

**PASS.**

The correction identifies the precise hypothesis missing from a new general lemma and replaces it with a sharp equality valid for arbitrary finite transformation monoids. The orbit-weighted iterated formula simultaneously removes transitivity and the relative-rank-\(\le1\) restriction from the relative-rank calculation. It also explains why Lu's advertised main theorem remains valid even though the broader intermediate lemmas are false as stated.

The result is directly reusable in semigroup generation problems where the top monoid is transitive but its unit group is not, a situation in which the difference between monoid transitivity and unit-group transitivity is essential.

## Limitations

Originality is qualified to the best of our knowledge. No independent or cross-model review has been performed. The source paper is a recent v1 and may be revised independently. The older 2009 partition paper was not fully text-searched, so differently phrased prior coverage cannot be excluded.
