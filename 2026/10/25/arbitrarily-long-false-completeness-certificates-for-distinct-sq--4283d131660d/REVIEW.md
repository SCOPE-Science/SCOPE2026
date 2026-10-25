# Scientific review: false completeness certificates for distinct squares

## Correctness — PASS
The printed hypotheses were read in Fuller--Nichols (2015), Theorem 6, pp. 5--6. All four conditions reduce to explicit quadratics with correct inequalities for every integer \(m\ge B\ge18\). Two independent exhaustive, exact subset-sum algorithms establish the only finite starting interval \([129,324]\) and the nonrepresentability of \(128\). The induction using \((m-4)^2\) proves coverage of \([129,B^2]\) by prefix squares for every \(B\ge18\); it does not appeal to the contested theorem. Every later square is divisible by \(Q_B\), while prefix square sums range from \(0\) to \(Q_B-2\), proving the infinite missing residue class \(-1\pmod{Q_B}\). There is no inference from a finite sample to an infinite property.

## Originality — PASS, subject to residual search risk
The 2014 Fuller--Prier--Vasconi predecessor assumes unrestricted natural-number square bases and therefore does not imply any arbitrary-sequence conclusion. The 2015 Fuller--Nichols theorem explicitly generalizes to arbitrary nondecreasing sequences, and its proof assumes without a stated hypothesis that the shift base is available. The 2017 LeVan--Prier treatment concerns ordinary anti-Waring numbers. No located primary text, exact table or indexed research summary states the family \(A_B\), the modular obstruction, or the arbitrary-length failure of the 2015 sufficiency criterion. An unpublished or unindexed correction might exist; the search cannot establish absolute historical uniqueness.

## Mathematical value — PASS
The result disproves a published general completeness certification rule, with the **same** numerical square-power certificate as its classical test and arbitrary growth in the length of locally verified coverage. The positive-density eventually arithmetic-progression sequence additionally has gcd one, eliminating the ordinary global-gcd explanation for noncompleteness. The precise missing availability assumption explains why certificates requiring only local goodness cannot be applied blindly to arbitrary tails. The result neither challenges the classical threshold \(129\) nor alleges that any numerical table value is false.

## Sources and limitations
Fuller--Nichols (2015), Theorem 6 (pp. 5--6), Tables 1--6 (pp. 8--12), and publication information (p. 14); Fuller--Prier--Vasconi (2014), Theorem 2.2 (pp. 241--242); LeVan--Prier (2017), definitions and bounds (pp. 1--5); OEIS A001661. Computational checks are finite certificates for their explicitly finite assertions, while mathematical induction and congruences handle universal claims. Possible unlocated errata, alternative formulations and the lack of independent review remain risks.

Self-review: passed. Independent audit: not yet performed.
