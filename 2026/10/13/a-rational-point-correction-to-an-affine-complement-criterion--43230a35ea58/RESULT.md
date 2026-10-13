# A rational-point correction to an affine-complement criterion
## Finding
Let \(k\) be a field of characteristic \(0\), let \(\pi:X=\mathbf P(\mathscr E)\to\mathbf P^1_k\) be a projective bundle of dimension \(n\ge2\), and let \(D,E\subset X\) be distinct irreducible divisors with
\[
D\sim d f+h,\qquad E\sim e f+h.
\]
Let \(W\subset\mathbf P^1_k\) be the scheme-theoretic locus where the fibre hyperplanes \(D_p\) and \(E_p\) coincide.

If
\[
X\setminus(D\cup E)\cong\mathbf A^n_k,
\]
then \(|e-d|=1\) and the support of \(W\) is a single \(k\)-rational point. Conversely, if \(|e-d|=1\) and the support of \(W\) is a single \(k\)-rational point, the reduction to a ruled surface and the subsequent affine-bundle argument in arXiv:2608.27341v2 are defined over \(k\) and yield
\[
X\setminus(D\cup E)\cong\mathbf A^n_k.
\]

Thus, over nonclosed characteristic-zero fields, “one closed collision point” is not enough: the field of definition of that point matters.

An explicit counterexample to the closed-point reading occurs over \(\mathbf Q\). Put
\[
X=\mathbf P^1_{[u:v]}\times\mathbf P^1_{[x:y]}
\]
with projection to the first factor. Let \(D\) be the graph of
\[
[u:v]\longmapsto[u:v]
\]
and let \(E\) be the graph of
\[
[u:v]\longmapsto[-v^2:u^2+v^2].
\]
Then
\[
D\sim f+h,\qquad E\sim2f+h.
\]
The two fibre points agree exactly where
\[
u(u^2+v^2)+v^3=0,
\]
so
\[
W=V(u^3+uv^2+v^3).
\]
The polynomial \(t^3+t+1\) has no rational root and is therefore irreducible over \(\mathbf Q\); its discriminant is \(-31\). Hence \(W\) is one closed point of degree \(3\) over \(\mathbf Q\), but after base change to \(\mathbf C\) it becomes three distinct points.

Consequently,
\[
\chi_c\!\left((X\setminus(D\cup E))_{\mathbf C}\right)
=4-2-2+3
=3,
\]
whereas
\[
\chi_c(\mathbf A^2_{\mathbf C})=1.
\]
Therefore \(X\setminus(D\cup E)\) is not isomorphic to \(\mathbf A^2_{\mathbf Q}\).

## Assumptions and scope
The field is assumed to have characteristic \(0\). The divisors are exactly of the hyperplane-on-each-fibre form used in Theorem 3.1 of arXiv:2608.27341v2. The new point is field-sensitive: it distinguishes a single topological closed point of the collision support from a single geometric collision point.

No claim is made here about the optimal formulation over imperfect fields of positive characteristic. The example uses only the trivial rank-two bundle over \(\mathbf P^1_{\mathbf Q}\), so it does not depend on subtle vector-bundle splitting phenomena.

## Proof
The class condition \(|e-d|=1\) is necessary because the two boundary divisors must generate \(\operatorname{Pic}(X)\cong\mathbf Z f\oplus\mathbf Z h\) when the complement is affine space.

For the field-of-definition condition, base change to an algebraic closure \(\bar k\). Let \(r\) be the number of geometric points in the support of the collision locus. The same inclusion-exclusion calculation used for the projective-bundle criterion gives
\[
[X\setminus(D\cup E)]
=
\mathbf L^n+(r-1)\mathbf L^{n-2}
\]
after passing to \(\bar k\) and then to any additive realization. Applying compactly supported Euler characteristic gives
\[
\chi_c\!\left((X\setminus(D\cup E))_{\bar k}\right)=r.
\]
If the complement is \(\mathbf A^n_k\), then after base change it is \(\mathbf A^n_{\bar k}\), whose compactly supported Euler characteristic equals \(1\). Thus \(r=1\). In characteristic \(0\), a finite closed point is separable; therefore a collision support with one geometric point must have residue degree \(1\), hence is \(k\)-rational.

For the converse, assume \(|e-d|=1\) and the collision support is one \(k\)-rational point. The proof of the sufficient direction of Theorem 3.1 in arXiv:2608.27341v2 is then defined over \(k\): the linear-projection reduction lowers the problem to a ruled surface, the unique collision point and all successive infinitely near intersection points are \(k\)-rational, and the resulting complement is an \(\mathbf A^1\)-bundle over \(\mathbf A^1\). That bundle is trivial. The higher-dimensional complement is then an affine-space torsor over \(\mathbf A^2\) under a trivial vector bundle, hence is \(\mathbf A^n\).

For the explicit example, the second graph map is a morphism of degree \(2\): the two homogeneous quadrics \(-v^2\) and \(u^2+v^2\) have no common projective zero. A graph of a degree-\(m\) morphism \(\mathbf P^1\to\mathbf P^1\) has divisor class \(m f+h\), giving the stated classes. Equality of the two graph values is the vanishing of the determinant
\[
\det
\begin{pmatrix}
u&v\\
-v^2&u^2+v^2
\end{pmatrix}
=
u^3+uv^2+v^3.
\]
The dehomogenization \(t^3+t+1\) has no root among \(\pm1\), so it is irreducible over \(\mathbf Q\). Its discriminant is \(-31\), so its three complex roots are distinct. The Euler-characteristic calculation above then proves that the complement is not an affine plane.

## Verification
The bundled script `verify_counterexample.py` rechecks the exact arithmetic used in the explicit example: irreducibility by the rational-root test, discriminant \(-31\), base-point-freeness of the quadratic graph map, the collision determinant, and the compactly supported Euler-characteristic count. Its recorded output ends in `VERIFY_OK`.

The script is only an arithmetic consistency check. The general rational-point necessity and sufficiency are deductive arguments; no finite computation is used to infer an infinite statement.

## Relationship to prior work
Theorem 3.1 of Remy van Dobben de Bruyn, arXiv:2608.27341v2, is stated for projective bundles over \(\mathbf P^1\) over an arbitrary field and characterizes affine-space complements by \(e=d\pm1\) together with a condition described as exactly one point in the collision support. The proof counts collision points after a Grothendieck-ring computation and, in the surface reduction, removes the fibre over the unique collision point.

The present finding isolates the field-of-definition distinction that is invisible over algebraically closed fields. If “point” is interpreted geometrically, the result gives an explicit field-sensitive restatement and explains why that interpretation is necessary. If it is interpreted as a topological closed point of \(\operatorname{Supp}(W)\), the \(\mathbf Q\)-example above is a counterexample to that literal reading.

Searches of the initiating source, statement-level literature queries, a published-finding index, and the available prior findings found no earlier statement of this explicit rational-point correction or this cubic graph counterexample.

## Limitations
The corrected equivalence is asserted only in characteristic \(0\), where one geometric collision point forces a rational closed point. Positive-characteristic imperfect fields may require a formulation that distinguishes rational, separable, and purely inseparable collision points.

The finding does not challenge the algebraically closed case of the criterion or the Jacobian-counterexample application in the initiating paper. Its scope is the descent from the algebraically closed setting to nonclosed base fields.

## References
1. Remy van Dobben de Bruyn, “Divisors in projective bundles over the projective line whose complement is affine space,” arXiv:2608.27341v2. First public version: 2026-08-27. Primary MSC 14R10.
