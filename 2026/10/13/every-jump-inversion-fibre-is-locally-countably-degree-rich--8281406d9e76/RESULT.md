# Every jump-inversion fibre is locally countably degree-rich
## Finding

There is a special \(\Pi^0_1\) class
\[
\mathcal P\subseteq\mathrm{GL}_1
\]
with the following simultaneous saturation property.

For every real
\[
A\geq_T0'
\]
and every finite binary string \(\sigma\) such that
\[
\mathcal P\cap[\sigma]\neq\varnothing,
\]
the degree set
\[
\left\{
\deg_T(B):
B\in\mathcal P\cap[\sigma]
\ \text{and}\
B'\equiv_TA
\right\}
\]
is countably infinite.

In particular, for each \(A\geq_T0'\), the jump-inversion fibre
\[
\mathcal J_A
=
\{B\in\mathcal P:B'\equiv_TA\}
\]
is a countable dense subset of \(\mathcal P\), and every nonempty relatively basic open subset of \(\mathcal P\) contains members of \(\mathcal J_A\) from infinitely many distinct Turing degrees.

Thus the class constructed by Cintioli is not merely locally rich enough to realize the Join Property: every ordinary jump degree above \(0'\) is represented degree-infinitely often in every nonempty basic piece of the same class.

## Assumptions and scope

Cantor space is \(2^{\mathbb N}\), and for a finite binary string \(\sigma\),
\[
[\sigma]
=
\{X\in2^{\mathbb N}:\sigma\prec X\}.
\]

A \(\Pi^0_1\) class is special when it is nonempty and has no computable member.

The generalized-low class is
\[
\mathrm{GL}_1
=
\{B:B'\equiv_TB\oplus0'\}.
\]

For a class \(\mathcal R\subseteq2^{\mathbb N}\) and \(A\geq_T0'\), Cintioli defines the generalized-low jump-inversion degree fibre
\[
\mathcal F_{\mathcal R}(A)
=
\left\{
\deg_T(B):
B\in\mathcal R,\
B'\equiv_TB\oplus0'\equiv_TA
\right\}.
\]

The statement here concerns the particular class \(\mathcal P\) supplied by Cintioli's 2026 local Join Property theorem. It does not assert that arbitrary special \(\Pi^0_1\) classes have dense jump fibres.

## Proof

Cintioli proves that there is a special \(\Pi^0_1\) class
\[
\mathcal P\subseteq\mathrm{GL}_1
\]
such that the Join Property holds locally: whenever
\[
\mathcal P\cap[\sigma]\neq\varnothing,
\]
the class
\[
\mathcal R_\sigma=\mathcal P\cap[\sigma]
\]
has the Join Property.

Independently, Proposition A.2 of the same paper proves that if an arbitrary class \(\mathcal R\) has the Join Property, then for every
\[
A\geq_T0'
\]
the degree fibre
\[
\mathcal F_{\mathcal R}(A)
\]
is countably infinite.

Fix \(A\geq_T0'\) and a finite binary string \(\sigma\) with
\[
\mathcal P\cap[\sigma]\neq\varnothing.
\]
Apply Proposition A.2 to
\[
\mathcal R=\mathcal R_\sigma.
\]
It follows that
\[
\mathcal F_{\mathcal R_\sigma}(A)
\]
is countably infinite.

Since
\[
\mathcal R_\sigma\subseteq\mathcal P\subseteq\mathrm{GL}_1,
\]
every \(B\in\mathcal R_\sigma\) satisfies
\[
B'\equiv_TB\oplus0'.
\]
Therefore, inside this slice, the defining condition for \(\mathcal F_{\mathcal R_\sigma}(A)\) reduces to
\[
B'\equiv_TA.
\]
Hence
\[
\left\{
\deg_T(B):
B\in\mathcal P\cap[\sigma],\
B'\equiv_TA
\right\}
\]
is countably infinite.

The cylinders form a basis for Cantor space. Thus every nonempty relatively open subset of \(\mathcal P\) contains a nonempty relatively basic open set of the form
\[
\mathcal P\cap[\sigma].
\]
The preceding paragraph shows that every such basic set meets
\[
\mathcal J_A
=
\{B\in\mathcal P:B'\equiv_TA\}
\]
in infinitely many distinct Turing degrees. Consequently \(\mathcal J_A\) is dense in \(\mathcal P\).

Finally, if \(B'\equiv_TA\), then
\[
B\leq_TB'\leq_TA.
\]
Only countably many reals are computable from one fixed oracle \(A\). Hence \(\mathcal J_A\) itself is countable. Since it contains infinitely many degrees, it is countably infinite.

## Verification

The two load-bearing source statements were checked directly in the full arXiv HTML.

Cintioli's Theorem 1.2 states that the constructed special class \(\mathcal P\) lies inside \(\mathrm{GL}_1\) and that every nonempty relatively basic open subclass
\[
\mathcal P\cap[\sigma]
\]
has the Join Property.

The paper's Appendix A defines
\[
\mathcal F_{\mathcal R}(A)
\]
as the generalized-low part of the jump-inversion fibre and proves in Proposition A.2 that, for every class \(\mathcal R\) with the Join Property and every \(A\geq_T0'\),
\[
\mathcal F_{\mathcal R}(A)
\]
is countably infinite.

Applying Proposition A.2 to each basic slice is legitimate because Theorem 1.2 gives the Join Property to that slice itself, not merely to the ambient class.

The conversion from generalized-low fibres to ordinary jump fibres is exact because every member of every slice lies in \(\mathrm{GL}_1\).

No finite experiment or computational search is used in the proof.

## Relationship to prior work

Jananthan and Simpson studied class-restricted versions of the Join Theorem and Pseudojump Inversion Theorem for special \(\Pi^0_1\) classes, establishing that these properties hold in some such classes and fail in others.

Cintioli's 2026 paper closes their remaining existence case and strengthens the Join Property to hold on every nonempty relatively basic open part of one special generalized-low class. The same paper separately proves that every Join-Property class has countably infinitely many degrees in every generalized-low jump-inversion fibre above \(0'\).

The present finding combines those two results at the level of each basic slice. The source states the local Join Property and the global fibre theorem separately, but does not formulate the resulting density statement that every jump-inversion fibre is degree-infinite in every nonempty basic slice of the constructed class.

Targeted searches for dense jump-inversion fibres, local Join Property fibres, and basic-open jump-fibre saturation did not locate an equivalent published formulation.

## Limitations

The result is a structural corollary of two theorems in the same recent paper; it introduces no new priority construction.

It concerns the class \(\mathcal P\) produced by the local Join Property theorem, not all special \(\Pi^0_1\) classes.

It determines local cardinal richness and density of each jump fibre but not the order-theoretic structure among the degrees in that fibre.

No uniform procedure selecting a representative from a prescribed basic slice is asserted.

## References

[1] Patrizio Cintioli, “A Special \(\Pi^0_1\) Class with the Join Property but without Pseudojump Inversion,” arXiv:2609.37480v1, first posted 27 September 2026.

[2] Hayden R. Jananthan and Stephen G. Simpson, “Pseudojump inversion in special r. b. \(\Pi^0_1\) classes,” arXiv:2102.06135, first posted 11 February 2021.
