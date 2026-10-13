# The model \(\mathcal{DT}_3^1\) has a three-dimensional derivation algebra

## Finding

Let \(K\) be a field of characteristic zero. Consider the three-dimensional tridendriform algebra \(\mathcal{DT}_3^1\) with basis
\[
\{e_1,e_2,e_3\}
\]
and nonzero products
\[
e_1\prec e_1=e_2,
\qquad
e_1\prec e_3=e_2,
\qquad
e_3\prec e_1=e_2,
\]
\[
e_1\succ e_3=e_2,
\qquad
e_3\succ e_1=e_2,
\qquad
e_3\succ e_3=e_2,
\]
and
\[
e_1\vee e_1=e_2,
\qquad
e_1\vee e_3=e_2,
\qquad
e_3\vee e_3=e_2.
\]

Its derivation algebra is
\[
\boxed{
\operatorname{Der}(\mathcal{DT}_3^1)
=
\left\{
\begin{pmatrix}
a&0&0\\
b&2a&c\\
0&0&a
\end{pmatrix}
:
a,b,c\in K
\right\}.
}
\]
Therefore
\[
\boxed{
\dim\operatorname{Der}(\mathcal{DT}_3^1)=3.
}
\]

In particular, the published assertion that every three-dimensional tridendriform algebra has only trivial derivations fails already on the first three-dimensional model in the same classification.

If
\[
H=\operatorname{diag}(1,2,1),
\qquad
U=E_{21},
\qquad
V=E_{23},
\]
then
\[
[H,U]=U,
\qquad
[H,V]=V,
\qquad
[U,V]=0.
\]
Thus the derivation Lie algebra is the three-dimensional solvable semidirect product
\[
K^2\rtimes K,
\]
where the one-dimensional factor acts by scalar multiplication on the two-dimensional abelian ideal.

## Assumptions and scope

The calculation uses the multiplication table printed for \(\mathcal{DT}_3^1\) in Theorem 3.2 of the cited source and the source's own definition of derivation: a linear map \(D\) must satisfy
\[
D(x\circ y)=D(x)\circ y+x\circ D(y)
\]
for each operation
\[
\circ\in\{\prec,\succ,\vee\}.
\]

The result is stated in characteristic zero, matching the classification setting of the source. No claim is made here about the correctness or completeness of the other low-dimensional classes.

The source's first-listed Mathematics Subject Classification code is \(16Z05\), within the algebra scope used here.

## Proof

Write
\[
D(e_1)=a e_1+b e_2+c e_3,
\]
\[
D(e_2)=p e_1+q e_2+r e_3,
\]
and
\[
D(e_3)=s e_1+t e_2+u e_3.
\]

From
\[
e_1\prec e_1=e_2
\]
we obtain
\[
D(e_2)=D(e_1)\prec e_1+e_1\prec D(e_1)
=2(a+c)e_2.
\]
Hence
\[
p=r=0,
\qquad
q=2(a+c).
\]

The product
\[
e_1\succ e_1=0
\]
gives
\[
0=D(e_1)\succ e_1+e_1\succ D(e_1)=2c e_2.
\]
Characteristic zero therefore forces
\[
c=0.
\]
Thus
\[
D(e_2)=2a e_2.
\]

Now use
\[
e_1\prec e_3=e_2.
\]
The derivation identity gives
\[
2a e_2
=
D(e_1)\prec e_3+e_1\prec D(e_3)
=(a+s+u)e_2,
\]
so
\[
s+u=a.
\]

Finally,
\[
e_3\prec e_3=0
\]
implies
\[
0=D(e_3)\prec e_3+e_3\prec D(e_3)=2s e_2,
\]
whence
\[
s=0,
\qquad
u=a.
\]

The parameters
\[
b
\quad\text{and}\quad
t
\]
remain free. Direct substitution into every remaining listed zero and nonzero product imposes no further constraint. Hence
\[
D(e_1)=a e_1+b e_2,
\qquad
D(e_2)=2a e_2,
\qquad
D(e_3)=t e_2+a e_3,
\]
which is exactly the displayed three-parameter matrix family.

The commutator calculation on the basis \(H,U,V\) is immediate:
\[
[H,U]=U,
\qquad
[H,V]=V,
\qquad
[U,V]=0.
\]

## Verification

The included checker reconstructs all three products exactly, checks all seven tridendriform identities on all \(27\) ordered basis triples, builds the full linear system for a general \(3\times3\) derivation, and performs exact rational Gaussian elimination.

It finds rank \(6\) in the nine matrix variables, so the derivation space has dimension \(3\). It then verifies that the kernel is spanned by
\[
H,
\qquad
U,
\qquad
V,
\]
with the commutator relations above.

The checker returns `VERIFY_OK`.

No finite experiment is used in place of the symbolic proof.

## Relationship to prior work

Mosbahi, Asif, and Zahari give the multiplication table of \(\mathcal{DT}_3^1\) in Theorem 3.2. Their Definition 2.6 gives the ordinary Leibniz rule used above for each tridendriform product.

The same paper states in its abstract and introduction that only trivial derivations exist in dimensions two and three, and Corollary 4.2 explicitly states that only trivial derivations exist for the three-dimensional tridendriform algebras.

The calculation above is therefore a direct statement-level counterexample to that corollary using one of the paper's own classified models. It does not depend on a different convention for derivations.

Targeted semantic and literature searches for \(\mathcal{DT}_3^1\), its derivation algebra, the exact multiplication table, and corrections to the 2023 classification did not locate a published correction or an equivalent explicit three-dimensional derivation formula.

A nearby 2023 paper on finite-dimensional complex Hom-trialgebras studies \(\alpha\)-inner derivations for a different Hom-type structure. Its objects and operator notion do not imply the derivation algebra computed here.

## Limitations

This result corrects one specific low-dimensional derivation assertion. It does not re-audit the remaining tridendriform classification, centroid tables, quasi-centroid tables, or four-dimensional derivation tables.

The proof is given in characteristic zero, which is the field regime of the source's classification.

An unindexed author note or later correction may exist.

Failed searches do not prove novelty.

## References

1. B. Mosbahi, S. Asif, and A. Zahari, “Classification of tridendriform algebra and related structures,” arXiv:2305.08513v1, first public version 15 May 2023.
2. B. Mosbahi, A. Zahari, and I. Basdouri, “Classification, \(\alpha\)-Inner Derivations and \(\alpha\)-Centroids of Finite-Dimensional Complex Hom-Trialgebras,” *Pure and Applied Mathematics Journal* 12 (2023), 86–97, DOI 10.11648/j.pamj.20231205.12.
