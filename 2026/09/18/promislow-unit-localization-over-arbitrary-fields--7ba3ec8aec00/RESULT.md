# Coefficient transport removes the characteristic-two restriction in Promislow unit localization

## Statement

Let \(\mathsf P\) be the Promislow group in its standard generators and let \(B(r)\) be the corresponding word ball. Let \(k\) be an arbitrary field.

Tabei's effective-localization theorem for \(\mathbb F_2[\mathsf P]\) associates to every total support size \(n\) an explicit radius \(D_u(n)\), with
\[
D_u(n)\le 4^n\operatorname{poly}(n),
\]
such that any nontrivial unit of total support \(n\) can be replaced by one whose support and inverse support both lie in \(B(D_u(n))\).

The same radius works over every field:

**Theorem.** If \(k[\mathsf P]\) contains a nontrivial unit
\[
\alpha=\sum_{i=1}^r a_i g_i
\]
with inverse
\[
\beta=\sum_{j=1}^s b_j h_j,
\qquad r+s=n,
\]
then \(k[\mathsf P]\) contains a nontrivial unit
\[
\alpha'=\sum_{i=1}^r a_i g_i'
\]
with inverse
\[
\beta'=\sum_{j=1}^s b_j h_j'
\]
such that
\[
\operatorname{supp}\alpha'\cup\operatorname{supp}\beta'
\subseteq B(D_u(n)).
\]
In particular, the ordered coefficient lists \((a_i)\) and \((b_j)\) can be preserved exactly; only the support elements need to be moved.

Consequently, for every finite field \(\mathbb F_q\), the existence of a nontrivial unit of total support \(n\) in \(\mathbb F_q[\mathsf P]\) is decidable by a finite search. Moreover, the least total support of a nontrivial unit in \(\mathbb F_q[\mathsf P]\) is computable in principle.

## Coefficient-sum coarsening lemma

Let \(I,J\) be finite sets and let
\[
I\times J=C_0\sqcup C_1\sqcup\cdots\sqcup C_m
\]
be a partition. Fix nonzero coefficients \(a_i,b_j\in k\), and write
\[
\sigma(C_t)=\sum_{(i,j)\in C_t}a_i b_j.
\]
Assume
\[
\sigma(C_0)=1,\qquad \sigma(C_t)=0\quad(t\ge1).
\]

Suppose group elements \(g_i'\) and \(h_j'\) are assigned injectively on each side so that:

1. all cells in each \(C_t\) have a common product \(g_i'h_j'\);
2. the common product of \(C_0\) is the identity.

Then
\[
\left(\sum_i a_i g_i'\right)\left(\sum_j b_j h_j'\right)=1.
\]

### Proof

For any group element \(w\), its new product fiber
\[
F_w=\{(i,j):g_i'h_j'=w\}
\]
is a disjoint union of whole classes \(C_t\), because every \(C_t\) is monochromatic for the new product map.

If \(w\ne1\), then \(F_w\) cannot contain \(C_0\), hence its coefficient is a sum of terms \(\sigma(C_t)=0\). If \(w=1\), the fiber contains \(C_0\) and possibly some other classes, so its coefficient is
\[
\sigma(C_0)+\sum_{C_t\subseteq F_1,\ t\ge1}\sigma(C_t)=1.
\]
Thus the product is exactly \(1\). \(\square\)

This is the coefficient-weighted analogue of Tabei's parity-coarsening lemma. It is stronger in the relevant direction: arbitrary mergers of old product fibers remain harmless whenever each old nonidentity fiber has coefficient sum \(0\).

## Proof of the theorem

Write
\[
\alpha=\sum_{i=1}^r a_i g_i,\qquad
\beta=\sum_{j=1}^s b_j h_j,\qquad
\alpha\beta=1,
\]
where all displayed coefficients are nonzero and the support elements are distinct on each side.

Partition the cell set \([r]\times[s]\) into the exact fibers of
\[
(i,j)\longmapsto g_i h_j.
\]
Call the fiber whose product is \(1\) the anchored class \(C_0\). Reading the equation \(\alpha\beta=1\) coefficientwise gives
\[
\sum_{(i,j)\in C_0}a_i b_j=1
\]
and, for every other fiber \(C_t\),
\[
\sum_{(i,j)\in C_t}a_i b_j=0.
\]

Now retain the coset labels and the product-fiber partition but forget the magnitudes of the original exponent vectors. In the standard normal form
\[
\mathsf P=\mathbb Z^3\rtimes(\mathbb Z/2)^2,
\]
the equal-product constraints inside a fiber are precisely the sparse integer linear equations used in Steps 2--3 of Tabei's proof of Theorem 7.2. The anchored class additionally imposes that its common product is \(1\). Those equations depend only on the group labels and the partition of index pairs, not on the field or on the coefficients \(a_i,b_j\).

Tabei's small-integer-solution argument therefore applies without change. It gives new pairwise-distinct support elements \(g_i',h_j'\), with the same coset labels, satisfying every old within-class product equality and the anchored identity constraint, and lying in the same ball \(B(D_u(n))\). Different old fibers may acquire the same new product; this is exactly the only point at which the characteristic-two proof used parity.

Keep the original coefficients and define
\[
\alpha'=\sum_i a_i g_i',\qquad
\beta'=\sum_j b_j h_j'.
\]
The coefficient-sum coarsening lemma gives \(\alpha'\beta'=1\).

The Promislow group is virtually abelian, hence amenable and therefore sofic. By the direct-finiteness theorem for group algebras of sofic groups over arbitrary fields, \(\alpha'\beta'=1\) implies \(\beta'\alpha'=1\). Thus \(\alpha'\) is a two-sided unit with inverse \(\beta'\). Pairwise distinctness and nonzero coefficients preserve both support cardinalities, so nontriviality and total support \(n\) are preserved.

This proves the field-independent localization statement with the same \(D_u(n)\).

## Finite-field computability

For fixed finite \(q\) and \(n\), the ball \(B(D_u(n))\) is finite. There are therefore finitely many pairs of supports of total size \(n\), and finitely many assignments of nonzero coefficients in \(\mathbb F_q\). Multiplication in the group ring is exact and finite, so all candidates can be checked.

Hence the predicate

> "\(\mathbb F_q[\mathsf P]\) has a nontrivial unit of total support \(n\)"

is decidable.

Murray constructed nontrivial units in \(\mathbb F_p[\mathsf P]\) for every prime \(p\). Since \(\mathbb F_p\subseteq\mathbb F_q\) when \(\operatorname{char}\mathbb F_q=p\), every finite field \(\mathbb F_q\) has at least one such unit. Enumerating \(n\) upward and using the finite decision procedure therefore terminates and computes the least total support.

## Relation to the source theorem

Tabei's Theorem 7.2 proves the localization result over \(\mathbb F_2\), with parity as the mechanism that survives accidental merging of product fibers. Remark 7.3 explicitly notes that the proof is characteristic-two-specific as written, because coefficients enter over \(\mathbb F_p\), and says that the coefficient-sum version is not pursued.

The observation above resolves precisely that obstruction: one does not need to solve for new coefficients after geometric compression. The coefficients of the original unit can be transported unchanged. Each original product fiber already has the required coefficient sum, and any new fiber is a union of whole original fibers.

## Scope and limitations

- The new claim is the field-independent extension of the effective localization theorem and its finite-field computability consequence. Tabei's \(\mathbb F_2\) theorem, his integer-coordinate compression, and the bound \(D_u(n)\) are prior work.
- Murray's existence of units in every positive prime characteristic is prior work.
- Direct finiteness for sofic group algebras over arbitrary fields is prior work.
- Older property-(U) results for virtually abelian group rings bound inverse support in terms of a prescribed support set. They are related but have a different input/output shape from a radius bound depending only on total support size.
- Over an infinite field, the localization theorem still holds, but bounded support does not by itself make coefficient search finite. No unrestricted decidability claim is made for infinite coefficient fields.
- Originality is asserted only to the best of our knowledge. The source localization paper is recent and explicitly leaves the positive-characteristic coefficient extension untreated; a later revision or concurrent observation may supersede this result.

## References

1. M. Tabei, *Localizing the Gardam unit: the support geometry of units in \(\mathbb F_2[\mathsf P]\) and its non-unique-product relatives*, arXiv:2609.17559v1. https://arxiv.org/abs/2609.17559
2. G. Elek and E. Szabó, *Sofic groups and direct finiteness*, Journal of Algebra 280 (2004), 426--434. https://arxiv.org/abs/math/0305440
3. A. G. Murray, *More Counterexamples to the Unit Conjecture for Group Rings*, arXiv:2106.02147. https://arxiv.org/abs/2106.02147
4. D. A. Craven and P. Pappas, *On the unit conjecture for supersoluble group algebras*, Journal of Algebra 394 (2013), 310--356. https://doi.org/10.1016/j.jalgebra.2013.07.014
5. J. Claramunt and Ł. Grabowski, *On group rings of virtually abelian groups*, arXiv:2303.02823. https://arxiv.org/abs/2303.02823
