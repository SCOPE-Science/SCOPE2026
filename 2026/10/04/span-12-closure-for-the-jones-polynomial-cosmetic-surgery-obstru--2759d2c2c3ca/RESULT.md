# Span-12 closure for the Jones-polynomial cosmetic-surgery obstruction
## Finding
Let \(K\subset S^3\) be a knot. If its Jones polynomial \(V_K(t)\) is nontrivial and
\[
\operatorname{span} V_K\le 12,
\]
then \(K\) does not admit purely cosmetic surgery.

Equivalently, among Laurent polynomials of span at most \(12\), the simultaneous conditions used by Ichihara for cosmetic-surgery candidates, together with
\[
|f(-1)|=1,
\]
have only the trivial solution \(f(t)=1\).

## Assumptions and scope
Write
\[
f(t)=t^rP(t),\qquad P(t)=\sum_{j=0}^{12}c_jt^j.
\]
For a purely cosmetic surgery candidate, the recent source imposes
\[
f(1)=1,\quad f'(1)=f''(1)=f'''(1)=f''''(1)=0
\]
and
\[
f(i)=f(\omega)=f(\zeta)=1,
\]
for primitive roots of orders \(4\), \(3\), and \(5\). Daemi--Lidman--Miller Eismeier also force the Alexander polynomial to be trivial, hence
\[
|V_K(-1)|=\det K=1.
\]
No claim is made about a hypothetical nontrivial knot with Jones polynomial exactly \(1\).

## Proof
Put
\[
r=60n+R,\qquad n\in\mathbb Z,\qquad 0\le R<60.
\]
For fixed \(R\), the five value/derivative conditions and eight independent root-of-unity coefficient conditions form a \(13\times13\) linear system
\[
M_R(n)c=b
\]
for \(c=(c_0,\ldots,c_{12})^T\). Exact elimination gives
\[
\det M_R(n)=6\,998\,400\,000
\]
for every \(R\) and \(n\). Thus there is a unique coefficient vector for each \((R,n)\); each \(c_j\) is an integer polynomial in \(n\) of degree at most \(4\).

The bundled table records all sixty coefficient families. It reproduces the source's displayed span-\(12\) formal solution at \(R=1,n=0\):
\[
(c_0,\ldots,c_{12})=(3,-4,5,-6,6,-7,7,-6,6,-5,4,-3,1).
\]

Since \(f(-1)=(-1)^rP(-1)\), the determinant condition is exactly
\[
P(-1)=\pm1.
\]
For every residue \(R\), substitution of the unique coefficient family makes \(P(-1)\) an integer polynomial in \(n\) of degree at most \(4\). The rational-root theorem applied exactly to \(P(-1)-1\) and \(P(-1)+1\) over all sixty residues leaves exactly thirteen integer parameter triples.

All thirteen are padded representations of the same Laurent polynomial \(1\): their shifts are
\[
r=-12,-11,\ldots,-1,0,
\]
and in each case the only nonzero Laurent coefficient is the coefficient \(1\) of \(t^0\). Hence no nontrivial Laurent polynomial of span at most \(12\) satisfies all necessary cosmetic-surgery conditions.

Therefore a knot with nontrivial Jones polynomial of span at most \(12\) cannot admit purely cosmetic surgery.

## Verification
The package contains `artifacts/span12_solution_table.json` and the standard-library checker `artifacts/verify_span12.py`.

For each residue, the checker substitutes the recorded coefficient polynomials into all thirteen defining equations. Each residual has degree at most \(8\), so nine exact substitutions prove each polynomial identity. The determinant has degree at most \(10\); exact Bareiss determinants at eleven distinct integers are all \(6\,998\,400\,000\), proving the determinant polynomial is that nonzero constant.

The checker reconstructs every quartic \(P(-1)\), exhausts all integer roots of \(P(-1)=\pm1\) by the rational-root theorem, verifies that exactly thirteen parameter choices survive, and checks that each produces \(f(t)=1\). It also reproduces the source's displayed span-\(12\) coefficient vector.

Replay output:

`VERIFY_OK residues=60 determinant=6998400000 determinant_compatible=13 all_trivial=true`

## Relationship to prior work
Ichihara proves the corresponding theorem for nontrivial Jones polynomial of span at most \(11\). The same paper shows that its reduced algebraic conditions first acquire nontrivial formal solutions at span \(12\). Remark 6.1 observes that the displayed example has \(f(-1)=-63\), notes that \(|f(-1)|=1\) is a necessary extra condition, and leaves extension of the method to future work.

The present result completes that missing boundary case for the full infinite one-parameter families, not merely for the displayed example or for a finite window of \(n\). Targeted searches for a span-\(12\) extension, determinant-completed classification, and equivalent formulations did not locate an earlier statement.

## Limitations
The argument closes only the span-\(12\) boundary. It gives no automatic extension to span \(13\) or higher.

It also does not address a hypothetical nontrivial knot with Jones polynomial \(1\). Because the source is a very recent preprint, a later revision could incorporate the same computation.

## References
1. K. Ichihara, *Purely cosmetic surgeries on knots with low-span Jones polynomials*, arXiv:2609.32507v1, first posted 2026-09-26.
2. A. Daemi, T. Lidman, and M. Miller Eismeier, *Filtered instanton homology and cosmetic surgery*, arXiv:2410.21248.
