# Eliminating the dimension-24 Type-II exception in the Knutson classification

## Result

Let \(H\) be a finite-dimensional semisimple Hopf algebra over an algebraically closed field of characteristic \(0\).

In the dimension-\(24\) module structure
\[
(1^2,2,3^2),
\]
the **Type II** action considered in D. Martín Duro, *The Knutson Index of the Representation Ring* (J. Algebra 659 (2024), Corollary 2.32) cannot occur. Consequently, the exception in that corollary is empty, and therefore:

> **Theorem.** Every finite-dimensional semisimple Hopf algebra over an algebraically closed field of characteristic \(0\) and of dimension at most \(31\) is of Knutson type.

Here “of Knutson type” has the meaning used by Martín Duro: every simple \(H\)-module has Knutson index \(1\).

## Proof

For the module structure \((1^2,2,3^2)\), the group \(G(H^*)\) of grouplike elements of \(H^*\), equivalently the group of one-dimensional \(H\)-modules, has order \(2\).

Let \(U\) be either of the three-dimensional simple modules. In Type II, both one-dimensional modules act trivially on \(U\). Thus the stabilizer of \(U\) under tensoring by one-dimensional modules has order \(2\).

For an irreducible character \(\chi\) of a semisimple Hopf algebra, Natale and Plavnik recall the standard consequence of the Nichols--Zoeller freeness theorem
\[
|G[\chi]|\mid (\deg\chi)^2,
\]
where \(G[\chi]\subseteq G(H^*)\) is the stabilizer under left multiplication by grouplikes.

If the Type-II convention is expressed by left tensoring, apply this directly to \(\chi_U\). If it is expressed by right tensoring, then
\[
U\otimes g\simeq U
\quad\text{for all }g\in G(H^*)
\]
implies after dualizing that
\[
g^{-1}\otimes U^*\simeq U^*,
\]
so the left stabilizer of the three-dimensional simple \(U^*\) also has order \(2\).

In either convention, the stabilizer divisibility gives
\[
2\mid 3^2=9,
\]
a contradiction. Hence Type II is non-realizable.

Martín Duro's Corollary 2.32 proves that every other semisimple Hopf algebra of dimension at most \(31\) is of Knutson type; in the same \((1^2,2,3^2)\) module structure, the remaining Type I case is explicitly shown there to be of Knutson type. Removing the impossible Type-II case therefore yields the stated theorem. \(\square\)

## Context and significance

Martín Duro's published classification leaves exactly one possible exception below dimension \(32\): dimension \(24\), module structure \((1^2,2,3^2)\), Type II. In that case the paper states that both one-dimensional modules fix each three-dimensional simple and concludes that the Hopf algebra would not be of Knutson type.

The stabilizer divisibility above rules out precisely that action. The conclusion is therefore not a new general stabilizer theorem; it is a short correction/application that closes the sole exceptional case in the low-dimensional Knutson classification.

## Limitations

The strengthened dimension-\(\le 31\) conclusion depends on the remaining case analysis in Martín Duro's Corollary 2.32. The originality claim is to the best of our knowledge: targeted searches and the current journal/arXiv versions located no published correction eliminating the Type-II case, but an unindexed erratum, note, or equivalent observation may exist.

## References

1. D. Martín Duro, “The Knutson Index of the Representation Ring,” *Journal of Algebra* **659** (2024), 516–541. DOI: https://doi.org/10.1016/j.jalgebra.2024.06.021. arXiv: https://arxiv.org/abs/2211.08123.
2. S. Natale and J. Y. Plavnik, “On fusion categories with few irreducible degrees,” *Algebra & Number Theory* **6** (2012), 1171–1197. arXiv: https://arxiv.org/abs/1103.2340. See §2.3 for the divisibility \(|G[\chi]|\mid(\deg\chi)^2\).
3. W. D. Nichols and M. B. Zoeller, “A Hopf Algebra Freeness Theorem,” *American Journal of Mathematics* **111** (1989), 381–385. DOI: https://doi.org/10.2307/2374514.
