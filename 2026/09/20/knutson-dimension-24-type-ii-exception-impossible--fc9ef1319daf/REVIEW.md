# Review: Eliminating the dimension-24 Type-II exception in the Knutson classification

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

For a semisimple Hopf algebra with module structure \((1^2,2,3^2)\), there are exactly two one-dimensional modules, hence \(|G(H^*)|=2\). The Type-II case in Martín Duro's dimension-\(24\) analysis is the case in which both one-dimensional modules fix each three-dimensional simple module.

Natale--Plavnik state the standard Nichols--Zoeller consequence that for every irreducible character \(\chi\),
\[
|G[\chi]|\mid(\deg\chi)^2,
\]
where \(G[\chi]\) is the stabilizer under left multiplication by grouplikes. Thus a three-dimensional simple cannot have a stabilizer of order \(2\), since \(2\nmid9\).

The only possible convention issue is whether the action in the Type-II description is written on the right. This does not affect the argument: from \(U\otimes g\simeq U\), duality gives \(g^{-1}\otimes U^*\simeq U^*\), so the left stabilizer of the three-dimensional simple \(U^*\) again has order \(2\). Hence Type II is impossible in either convention.

The global conclusion follows by combining this obstruction with Martín Duro's Corollary 2.32, which already treats every other case up to dimension \(31\) and proves the alternative Type-I action in module structure \((1^2,2,3^2)\) is of Knutson type.

## Originality

**PASS, to the best of our knowledge.**

The relevant published statement is Martín Duro's 2024 Corollary 2.32, which still lists the dimension-\(24\), \((1^2,2,3^2)\), Type-II case as the sole exception and describes it as non-Knutson. The current arXiv version (v5, revised 20 September 2024) and the current journal text retain that exception.

Targeted searches for the paper title and arXiv identifier together with “Type II”, “dimension 24”, “Knutson type”, “correction”, the module structure \((1^2,2,3^2)\), and the stabilizer obstruction did not locate a later correction or equivalent published observation.

The divisibility theorem itself is not new: Natale--Plavnik explicitly record \(|G[\chi]|\mid(\deg\chi)^2\), as a consequence of Nichols--Zoeller. The contribution claimed here is only the application of that standard theorem to eliminate the published Type-II exception and thereby sharpen the low-dimensional Knutson conclusion. Because the proof is short and uses an old general theorem, an unindexed correction, private author correction, or differently worded observation remains the principal originality risk.

## Value

**PASS.**

Although the obstruction is elementary once the stabilizer theorem is recalled, it removes the unique exception in a published low-dimensional classification. It converts the statement “all semisimple Hopf algebras of dimension at most \(31\), except one possible dimension-\(24\) Type-II case” into an unconditional dimension-\(\le31\) theorem and identifies the reason the excluded action cannot be realized by a semisimple Hopf algebra.

## Checked evidence and limitations

The current journal text of Martín Duro's paper was checked at the dimension-\(24\) case and Corollary 2.32. The current arXiv record reports v5 as the latest version, revised 20 September 2024. Natale--Plavnik's open arXiv text was checked at §2.3, where the stabilizer divisibility is stated explicitly. The original Nichols--Zoeller freeness theorem was also bibliographically verified.

The strengthened corollary inherits all hypotheses and all non-exceptional case analysis from Martín Duro's result. No claim is made about dimensions above \(31\). Originality is qualified to the best of our knowledge.
