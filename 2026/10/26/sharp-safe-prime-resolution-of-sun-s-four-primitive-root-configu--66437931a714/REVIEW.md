# Scientific review

## Correctness — PASS
The claim fixes safe primes \(p=2q+1\), requires ordinary positive representatives \(a+b<p\), and counts only fixed-first-entry witnesses in the \(3\pmod8\) branch. For \(p\ge11\), the congruence \(p\equiv11\pmod{12}\) and order-\(2q\) criterion reduce primitive roots to nonresidues other than \(-1\). The \(7\pmod8\) construction is verified by exact residues \((-1/2,-3/2,-2)\) and a product congruence. The \(3\pmod8\) count follows from the quadratic-character sum \(-1\), proved by a hyperbola bijection, the two linear character sums, and removal of exactly one forbidden residue. A nonsquare discriminant excludes the only remaining order-\(2\) obstruction in the product. Explicit smallest-prime cases are checked. The standalone order-based verifier checks all safe primes through \(50000\), but finite checking is not the proof.

## Originality — PASS, qualified
Sun's Conjecture 4.2(i) states the complete four-primitive-root requirement as a conjecture, and OEIS A260947 provides scattered minimum-sum data, not a general safe-prime theorem or fixed-first-entry count. Cohen–Oliveira e Silva–Trudgian's two-summand theorem lacks the primitive-sum/product conditions; neither its implication nor a standard additive representation supplies the new assertion. Search comparisons included safe-prime, Sophie Germain, primitive-root quadruple and quadratic-nonresidue-pair formulations, plus relevant published-result searches. A previously published equivalent statement could have escaped these searches; see the structured scientific comparison.

## Mathematical value — PASS
The answer resolves a canonical and naturally defined infinite *parameter family* of an explicitly posed four-primitive-root existence question, identifies both small exceptions, gives a uniform constructive branch, and sharpens the other branch to an exact multiplicity. It connects multiplicative order and a short-distance character correlation while retaining the integer inequality that the original conjecture demands. It is not merely the classical character-sum identity, which is acknowledged as existing background.

## Scope and residual uncertainty
No assertion for nonsafe primes, no all-pairs enumeration, no claim that infinitely many safe primes exist, and no independent mathematical review. An equivalent safe-prime specialization in unlocated literature remains possible.

Self-review: passed. Independent audit: not yet performed.
