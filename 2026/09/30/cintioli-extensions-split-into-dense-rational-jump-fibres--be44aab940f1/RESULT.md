# Cintioli extensions split into dense rational jump fibres
## Finding
Let \(\mathcal Q\subseteq 2^{\mathbb N}\) be any special \(\Pi^0_1\) class such that \(\mathcal Q\subseteq\mathrm{GL}_1\). Cintioli's extension theorem produces a special \(\Pi^0_1\) class \(\mathcal P\) satisfying
\[
\mathcal Q\subseteq\mathcal P\subseteq\mathrm{GL}_1
\]
and such that every nonempty relatively basic open subclass \(\mathcal P\cap[\sigma]\) has the Join Property.

For every Turing degree \(\mathbf a\geq\mathbf 0'\), set
\[
J_{\mathbf a}(\mathcal P)=\{B\in\mathcal P:\deg_{\mathrm T}(B')=\mathbf a\}.
\]
Then the following stronger local statement holds: whenever \(\mathcal P\cap[\sigma]\neq\varnothing\), the intersection
\[
J_{\mathbf a}(\mathcal P)\cap[\sigma]
\]
contains representatives of countably infinitely many distinct Turing degrees.

Consequently, for every \(\mathbf a\geq\mathbf0'\), the space \(J_{\mathbf a}(\mathcal P)\), with the subspace topology inherited from Cantor space, is countable, dense in \(\mathcal P\), has no isolated points, and is therefore homeomorphic to \(\mathbb Q\). Distinct jump degrees give disjoint fibres, every degree above \(\mathbf0'\) occurs, and the fibres cover \(\mathcal P\). Thus \(\mathcal P\) is partitioned into continuum many pairwise disjoint dense copies of \(\mathbb Q\), indexed canonically by jump degree.

## Assumptions and scope
The Join Property is Cintioli's class-restricted Posner--Robinson property. For a class \(\mathcal R\), Cintioli defines the generalized-low jump-inversion fibre above a real \(A\geq_{\mathrm T}0'\) by the Turing degrees represented by those \(B\in\mathcal R\) satisfying
\[
B'\equiv_{\mathrm T}B\oplus0'\equiv_{\mathrm T}A.
\]
His Proposition A.2 proves that this degree fibre is countably infinite whenever \(\mathcal R\) has the Join Property.

Because the extension \(\mathcal P\) lies inside \(\mathrm{GL}_1\), every \(B\in\mathcal P\) already satisfies
\[
B'\equiv_{\mathrm T}B\oplus0'.
\]
Therefore, inside \(\mathcal P\) and all its subclasses, the generalized-low fibre equals the ordinary jump-inversion fibre.

The topological conclusion uses the classical theorem of Sierpiński that every countable metrizable space without isolated points is homeomorphic to the rational numbers.

## Proof
Fix \(\mathbf a\geq\mathbf0'\) and choose a real \(A\) of Turing degree \(\mathbf a\).

Let \(\sigma\) be any finite binary string such that \(\mathcal P\cap[\sigma]\neq\varnothing\). By Cintioli's extension theorem, the class
\[
\mathcal R=\mathcal P\cap[\sigma]
\]
has the Join Property. Proposition A.2 applied to \(\mathcal R\) and \(A\) says that the generalized-low jump-inversion fibre in \(\mathcal R\) contains countably infinitely many distinct Turing degrees. Since \(\mathcal R\subseteq\mathcal P\subseteq\mathrm{GL}_1\), this is exactly the set of degrees represented in
\[
J_{\mathbf a}(\mathcal P)\cap[\sigma].
\]
This proves the local infinitude statement.

Taking arbitrary nonempty relatively basic open subsets shows that \(J_{\mathbf a}(\mathcal P)\) is dense in \(\mathcal P\). It also has no isolated points. Indeed, if \(B\in J_{\mathbf a}(\mathcal P)\) and \(U\) is any neighborhood of \(B\) in the fibre, some cylinder \([\sigma]\) containing \(B\) satisfies
\[
J_{\mathbf a}(\mathcal P)\cap[\sigma]\subseteq U.
\]
The local infinitude statement supplies a member of this cylinder having a Turing degree different from that of \(B\), so \(B\) is not isolated.

The fibre is countable. If \(B\in J_{\mathbf a}(\mathcal P)\), then
\[
B\leq_{\mathrm T}B'\leq_{\mathrm T}A.
\]
Only countably many reals are computable from a fixed oracle \(A\), because there are only countably many oracle Turing programs. Hence \(J_{\mathbf a}(\mathcal P)\) is countable. As a subspace of Cantor space it is metrizable. Sierpiński's theorem therefore gives
\[
J_{\mathbf a}(\mathcal P)\cong\mathbb Q.
\]

If \(\mathbf a\neq\mathbf b\), then \(J_{\mathbf a}(\mathcal P)\cap J_{\mathbf b}(\mathcal P)=\varnothing\) by definition. Every \(B\in\mathcal P\) belongs to the fibre indexed by \(\deg_{\mathrm T}(B')\), and \(0'\leq_{\mathrm T}B'\), so these fibres cover \(\mathcal P\). Conversely, every \(\mathbf a\geq\mathbf0'\) occurs because the local argument with the empty string gives a nonempty fibre. Finally, there are continuum many Turing degrees above \(\mathbf0'\): the continuum many reals \(0'\oplus X\) are partitioned into countable Turing-degree classes. Hence the displayed partition has continuum many dense members.

## Verification
The proof uses two separate source statements with their quantifiers preserved: the extension theorem gives the Join Property for every nonempty relative cylinder, and Proposition A.2 applies to every class with that property and every jump target above \(0'\). Applying Proposition A.2 locally is therefore legitimate.

The identification of generalized-low and ordinary fibres was checked pointwise from \(\mathcal P\subseteq\mathrm{GL}_1\). Countability was checked at the level of reals, not merely degree classes, using \(B\leq_{\mathrm T}A\). The no-isolated-points argument uses the stronger local conclusion that every relative cylinder contains infinitely many distinct fibre degrees, so it cannot accidentally reuse only the degree of the chosen point.

The final homeomorphism step is exactly Sierpiński's countable-metrizable-no-isolated-points characterization. The partition claim was checked in both directions: distinct jump degrees give disjoint fibres, every member belongs to its own jump-degree fibre, and every degree above \(0'\) is realized.

## Relationship to prior work
Cintioli proves two ingredients separately. His extension theorem constructs \(\mathcal P\subseteq\mathrm{GL}_1\) with the Join Property on every nonempty relatively basic open part. His Appendix A proves that a class with the Join Property has countably infinitely many jump-inversion degrees above every target \(A\geq_{\mathrm T}0'\). The paper does not state the resulting topological structure of the fibres: a search of the source finds no occurrence of a homeomorphism-to-\(\mathbb Q\) or resolvability conclusion.

Combining the local theorem with the appendix upgrades global infinitude to local infinitude in every relative cylinder. This forces each jump fibre to be dense and dense-in-itself. Sierpiński's theorem then identifies its exact homeomorphism type, while the full range of the jump targets gives a continuum-sized dense partition.

Targeted searches for jump-inversion fibres homeomorphic to the rationals, dense local jump fibres, and resolvability by Turing-jump fibres did not locate an equivalent or stronger published statement. Earlier class-restricted jump and pseudojump inversion work supplies the background degree-theoretic setting but not this topological conclusion.

## Limitations
The homeomorphism conclusion concerns the particular extensions supplied by Cintioli's local Join Property theorem; it is not asserted for arbitrary special \(\Pi^0_1\) classes or arbitrary classes with only a global Join Property.

The result identifies the topology of each jump fibre as a set of reals. It does not classify the partial order of Turing degrees within a fibre, which remains a separate problem highlighted in the source.

No effective homeomorphism with \(\mathbb Q\) is claimed. Sierpiński's theorem is purely topological, and the construction does not here provide uniform indices for such homeomorphisms as the jump target varies.

## References
Patrizio Cintioli, “A Special \(\Pi^0_1\) Class with the Join Property but without Pseudojump Inversion,” arXiv:2609.37480v1, first public version 2026-09-27.

Wacław Sierpiński, “Sur une propriété topologique des ensembles dénombrables denses en soi,” Fundamenta Mathematicae 1 (1920), 11--16, DOI 10.4064/fm-1-1-11-16.

Hayden R. Jananthan and Stephen G. Simpson, “Pseudojump inversion in special r. b. \(\Pi^0_1\) classes,” arXiv:2102.06135v1, 2021.
