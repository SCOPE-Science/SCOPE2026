# Finite IFS frames are downset families over minimal worlds
## Finding

Aguilera and Massas introduce an **involutive Fischer--Servi frame** (IFS frame) as a triple
\[
(X,\leq,R)
\]
where \((X,\leq)\) is a poset and \(R\) satisfies
\[
z\leq x,\ xRy
\quad\Longrightarrow\quad
\exists y'\leq y\; zRy'
\]
and
\[
xRy,\ z\leq y
\quad\Longrightarrow\quad
z=y.
\]

These two conditions admit a complete structural normal form.

Let
\[
M=\operatorname{Min}(X)
\]
be the set of minimal points. For each \(m\in M\), define the predecessor fiber
\[
D_m=\{x\in X:xRm\}.
\]

Then \((X,\leq,R)\) is an IFS frame if and only if:

1. every \(R\)-target is minimal; and
2. each \(D_m\) is a downset of \((X,\leq)\).

Equivalently, IFS relations on a fixed poset are in bijection with arbitrary families
\[
(D_m)_{m\in M},
\qquad
D_m\in\operatorname{Dn}(X).
\]

For a finite poset \(P\), this gives the exact labelled census
\[
\boxed{
N_{\mathrm{IFS}}(P)
=
|\operatorname{Dn}(P)|^{|\operatorname{Min}(P)|}.
}
\]

The modal operators from the source paper also simplify completely. For every downset \(U\subseteq X\),
\[
\boxed{
\Diamond_R U
=
\bigcup_{m\in U\cap M} D_m
}
\]
and
\[
\boxed{
\Box_R U
=
X\setminus
\bigcup_{m\in M\setminus U}
\uparrow D_m,
}
\]
where
\[
\uparrow D_m
=
\{x\in X:\exists y\in D_m\ (y\leq x)\}.
\]

Hence both modal operators depend on \(U\) only through its trace
\[
U\cap M
\]
on the minimal worlds.

Two extremal finite cases are immediate. If \(P\) is an \(n\)-element chain, then it has one minimal point and \(n+1\) downsets, so
\[
N_{\mathrm{IFS}}(P)=n+1.
\]
If \(P\) is an \(n\)-element antichain, then every point is minimal and every subset is a downset, so
\[
N_{\mathrm{IFS}}(P)
=
(2^n)^n
=
2^{n^2};
\]
in this case every binary relation is an IFS relation.

## Assumptions and scope

The definition of IFS frame and the modal operators are exactly those of Aguilera and Massas. Their condition (IFC) strengthens the usual Fischer--Servi condition and is the source of the minimal-target phenomenon.

The structural equivalence itself does not require finiteness. Finiteness is used for the exact counting statement and the finite examples.

The result concerns labelled relations on a fixed poset. Quotienting by poset automorphisms would give an isomorphism-class census and is not attempted here.

The operator formulas concern the modal action on the lattice of downsets used in the source's Lemma 5.8. They do not say that arbitrary formulas are determined only by their values at minimal points, because the underlying Heyting operations still use the full downset structure.

## Proof

Assume first that
\[
(X,\leq,R)
\]
is an IFS frame.

Suppose
\[
xRy.
\]
If
\[
z\leq y,
\]
condition (IFC) gives
\[
z=y.
\]
Thus \(y\) has no proper predecessor, so
\[
y\in\operatorname{Min}(X).
\]
Therefore \(R\) has no edges into nonminimal points.

Fix a minimal point \(m\), and let
\[
D_m=\{x:xRm\}.
\]
Suppose
\[
x\in D_m
\quad\text{and}\quad
z\leq x.
\]
By (FC2), there is \(m'\leq m\) such that
\[
zRm'.
\]
Since \(m\) is minimal,
\[
m'=m.
\]
Hence
\[
zRm,
\]
so \(z\in D_m\). Therefore \(D_m\) is a downset.

This proves that every IFS relation has the claimed form.

Conversely, let a family
\[
(D_m)_{m\in M}
\]
of downsets be given, and define
\[
xRy
\quad\Longleftrightarrow\quad
y\in M
\ \text{and}\
x\in D_y.
\]

Condition (IFC) is immediate. If \(xRy\), then \(y\) is minimal, so every \(z\leq y\) equals \(y\).

For (FC2), suppose
\[
z\leq x
\quad\text{and}\quad
xRy.
\]
Then \(y\in M\) and \(x\in D_y\). Since \(D_y\) is a downset,
\[
z\in D_y.
\]
Therefore
\[
zRy.
\]
Taking
\[
y'=y
\]
witnesses (FC2).

Thus arbitrary downset families indexed by minimal points are exactly the IFS relations.

If \(P\) is finite, the choices of \(D_m\) are independent. Each minimal point admits
\[
|\operatorname{Dn}(P)|
\]
possible predecessor fibers, so the number of relations is
\[
|\operatorname{Dn}(P)|^{|\operatorname{Min}(P)|}.
\]

It remains to derive the modal formulas.

The source defines
\[
\Diamond_R U
=
\{x:\exists y\ (xRy\ \text{and}\ y\in U)\}.
\]
Every target \(y\) is minimal, and
\[
xRm
\quad\Longleftrightarrow\quad
x\in D_m.
\]
Therefore
\[
x\in\Diamond_R U
\quad\Longleftrightarrow\quad
\exists m\in U\cap M\; x\in D_m,
\]
which is exactly
\[
\Diamond_R U
=
\bigcup_{m\in U\cap M}D_m.
\]

For the box, the source defines
\[
\Box_R U
=
\{x:\forall y,z\ (y\leq x\ \text{and}\ yRz\Rightarrow z\in U)\}.
\]
The only possible \(z\) are minimal points. Hence \(x\notin\Box_R U\) exactly when there are
\[
m\in M\setminus U
\quad\text{and}\quad
y\in D_m
\]
with
\[
y\leq x.
\]
This says exactly
\[
x\in\uparrow D_m
\]
for some \(m\in M\setminus U\). Therefore
\[
\Box_R U
=
X\setminus
\bigcup_{m\in M\setminus U}
\uparrow D_m.
\]

Both operators therefore factor through the restriction map
\[
U\longmapsto U\cap M.
\]

## Verification

The bundled checker independently enumerates every labelled poset on at most four points.

For posets on at most three points, it exhaustively enumerates every binary relation and verifies that the two source frame conditions hold if and only if the relation has only minimal targets and every minimal-target predecessor fiber is a downset. It also confirms that the exact number of admissible relations is
\[
|\operatorname{Dn}(P)|^{|\operatorname{Min}(P)|}.
\]

For every admissible relation on those posets, the checker enumerates every downset \(U\) and compares the source definitions of \(\Box_R U\) and \(\Diamond_R U\) against the two closed formulas above.

For posets on four points, it checks the structural ingredients and the counting formula from the family parametrization. The computation is corroborative; the theorem follows from the direct proof for arbitrary posets.

## Relationship to prior work

Aguilera and Massas introduce IFS frames specifically for the modal extension of their constructive quantum logic program. Their Definition 5.7 gives (FC2) and (IFC), and the proof of Lemma 5.8 explicitly observes that an \(R\)-target is minimal. The paper then uses IFS frames to build the intuitionistic factor in its modal embedding theorem.

The source does not state the converse structural classification: it does not identify an IFS relation with an arbitrary family of downsets indexed by minimal points, give the exact finite census, or rewrite both modal operators solely in terms of those fibers.

The classification makes the strength of (IFC) explicit. Instead of searching over arbitrary binary relations, finite IFS-frame construction on a fixed poset reduces exactly to choosing one downset for each minimal world.

Targeted searches for IFS-frame classifications, minimal-target predecessor fibers, and finite IFS-frame counts did not locate an equivalent statement. The terminology is very recent and generic searches for “IFS frame” are heavily polluted by unrelated uses of that acronym, so older equivalent formulations under different terminology remain a residual risk.

## Limitations

The exact count is for labelled relations on a fixed finite poset; it is not an isomorphism-class count.

The result does not classify which of the resulting modal algebras are pairwise nonisomorphic, nor which arise from the prime-filter construction used in the source's modal embedding theorem.

The modal factorization concerns only the primitive \(\Box\) and \(\Diamond\) operators on downsets. It does not collapse the full Heyting algebra to its minimal points.

An equivalent frame normal form may exist in older Fischer--Servi literature under terminology that does not use “IFS,” although no such statement was located in the checked searches.

## References

[1] Juan P. Aguilera and Guillaume Massas, “Conditionals and Modalities in Constructive Quantum Logics,” *Electronic Proceedings in Theoretical Computer Science* 447 (2026), 16–34. arXiv:2606.31853. DOI:10.4204/EPTCS.447.2.

[2] G. Fischer Servi, “Semantics for a Class of Intuitionistic Modal Calculi,” in *Italian Studies in the Philosophy of Science*, 1980, 59–72.

[3] A. Christensen, “Completeness for an Intuitionistic Modal Logic of Vagueness,” in *Advances in Modal Logic 14*, 2022.
