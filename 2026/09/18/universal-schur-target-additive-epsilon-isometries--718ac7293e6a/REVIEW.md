# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The statement reduces to three standard ingredients and one explicit distance computation.

1. The Banach--Mazur theorem provides a linear isometry from every separable real Banach space \(X\) into \(C([0,1],\mathbb R)\).
2. For \(\omega(t)=\max\{t,\sqrt t\}\), Kalton's theorem gives the Schur property for the Lipschitz-free space over the metric \(\omega(\|u-v\|_\infty)\).
3. The canonical Lipschitz-free embedding converts the scaled ambient distance exactly into
   \[
   \max\{r,2\sqrt{\varepsilon r}\}.
   \]
   The excess over \(r\) is
   \[
   \max\{0,\varepsilon-(\sqrt r-\sqrt\varepsilon)^2\},
   \]
   so it lies in \([0,\varepsilon]\), and for a nonzero Banach domain equality occurs at any pair at distance \(\varepsilon\).
4. Godefroy--Kalton's isometric linearization theorem says that an isometric embedding of a separable Banach space \(X\) into a Banach space \(Y\), even nonlinear, forces \(Y\) to contain a linearly isometric copy of \(X\). Since the Schur property is inherited by closed subspaces, a non-Schur \(X\) cannot embed isometrically into the constructed \(Y\).

The separability assertion is also stable: \(C([0,1])\) is separable, the gauged metric has the same topology, and the free space over a separable metric space is separable.

The metric-space extension follows by first applying the canonical isometric embedding \(M\to\mathcal F(M)\), then Banach--Mazur to the separable Banach space \(\mathcal F(M)\).

No numerical or computer-assisted step is used.

## Originality

The originality claim is qualified as **to the best of our knowledge**.

The most relevant source is Sun--Zhang, arXiv:2609.13937v1 (12 September 2026). Its theorem constructs a particular pair of separable real Banach spaces, with \(X=\ell_2\) and target built as a gauged Lipschitz-free space over that same \(X\), and obtains exact \(\varepsilon\)-isometries for all \(\varepsilon>0\) without any exact isometric embedding. The proof explicitly combines the same Kalton and Godefroy--Kalton theorems.

The present result strengthens the quantifier structure: one target \(Y\) is fixed in advance and works for every separable Banach space \(X\). The additional step is to put every separable Banach space into the common isometric host \(C([0,1])\) before applying the gauged free-space construction. The same idea extends the additive embedding statement to all pointed separable metric spaces by passing through their separable Lipschitz-free spaces.

Searches using combinations of the terms “universal”, “epsilon-isometry”, “additive epsilon-isometry”, “Schur property”, “Lipschitz-free”, “gauge”, and “C[0,1]” did not locate the universal-target statement. Searches of the current SCOPE archive by the mathematical objects and by arXiv:2609.13937 found no overlapping record.

Relevant comparison literature on universal left-stability of \(\varepsilon\)-isometries concerns stability/recovery properties of arbitrary approximate isometries rather than existence of one fixed Schur target that admits approximate embeddings of all separable spaces. Gurarii-type almost universal disposition concerns multiplicative almost-isometries and finite-dimensional extension properties, and its universal spaces contain exact copies; it does not imply the present additive/exact separation.

The principal residual originality risk is older \(\varepsilon\)-isometry or nonlinear Banach-geometry literature phrased with different terminology. No specifically identified inaccessible paper was found whose available title or abstract closely matches the universal-target theorem.

## Value

The result turns a fixed-pair separation into an approximate-universality phenomenon. It shows that additive \(\varepsilon\)-universality can coexist with a strong hereditary obstruction to exact isometric universality. The same target handles all separable Banach spaces simultaneously, and the metric-space extension shows that the mechanism is not tied to linear structure on the source.

The conclusion also provides a clean structural boundary: exact isometric copies inside this target must have the Schur property, while arbitrary separable Banach spaces can approach exact metric behavior to any prescribed additive tolerance.

## Sources inspected

- Sun and Zhang, arXiv:2609.13937v1: theorem statement and construction.
- Kalton, *Spaces of Lipschitz and Hölder functions and their applications*, especially the gauged free-space Schur theorem.
- Godefroy and Kalton, *Lipschitz-free Banach spaces*, including the isometric linearization statement.
- Lohman's account of the Banach--Mazur embedding theorem.
- Aliaga--Petitjean--Procházka, *Lipschitz-free spaces and Schur properties*, which explicitly records Kalton's theorem for nontrivial gauges.

No source was used as evidence for a claim stronger than the portion inspected.
