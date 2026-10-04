# Sharp genus-degree floor for one-dimensional Fano schemes of complete intersections
## Finding
Let
\[
X\subset\mathbb P^n_{\mathbb C}
\]
be a general complete intersection of type
\[
(d_1,\ldots,d_r),
\qquad
n\ge4,
\qquad
d_i\ge2,
\]
and let \(k\ge1\). Suppose the expected dimension of the Fano scheme of \(k\)-planes is one:
\[
\delta
=
(k+1)(n-k)
-
\sum_{i=1}^{r}\binom{d_i+k}{k}
=
1.
\]
Then \(F_k(X)\) is a connected smooth projective curve. Write \(e\) for its Plücker degree and \(g\) for its genus.

The sharp universal bound is
\[
g\ge e+1.
\]
Equality holds if and only if
\[
k=1,
\qquad
n=6,
\qquad
(d_1,d_2,d_3)=(2,2,2)
\]
up to permutation. In the equality case,
\[
e=128,
\qquad
g=129.
\]

Equivalently, define
\[
B
=
\sum_{i=1}^{r}\binom{d_i+k}{k+1}
-
n
-
1.
\]
The classical genus-degree formula gives
\[
g
=
1+\frac{B}{2}e,
\]
and the new statement is the sharp arithmetic classification
\[
B\ge2,
\]
with
\[
B=2
\]
only for the Fano curve of lines on a general intersection of three quadrics in \(\mathbb P^6\).

Thus no one-dimensional Fano scheme of positive-dimensional linear spaces on a general complete intersection can be rational or elliptic, and among all such curves the three-quadric line curve is uniquely closest to the diagonal \(g=e\).

## Assumptions and scope
The result concerns general complete intersections over \(\mathbb C\), in the range used by the standard smoothness and connectedness theorem for Fano schemes. The ambient dimension satisfies \(n\ge4\), the defining degrees satisfy \(d_i\ge2\), and the parametrized linear spaces have positive dimension \(k\ge1\).

The restriction \(k\ge1\) is essential. For \(k=0\), the Fano scheme is the complete intersection itself, so the statement becomes a different problem about complete-intersection curves.

The result concerns the Plücker degree of the Fano curve inside the Grassmannian. It does not assert that \(F_k(X)\) is a complete-intersection curve in its Plücker projective space.

## Proof
A genus-degree formula for one-dimensional Fano schemes gives
\[
g
=
1+
\frac{1}{2}
\left(
\sum_{i=1}^{r}\binom{d_i+k}{k+1}
-
n
-
1
\right)e.
\]
It therefore suffices to prove
\[
B
=
\sum_{i=1}^{r}\binom{d_i+k}{k+1}
-
n
-
1
\ge2
\]
and classify equality.

Put
\[
q=k+1\ge2
\]
and
\[
R_i=\binom{d_i+k}{k}.
\]
The expected-dimension equation is
\[
q(n-k)=1+\sum_i R_i.
\]
Using
\[
\binom{d_i+k}{k+1}
=
\frac{d_i}{q}R_i,
\]
one obtains
\[
qB
=
\sum_i(d_i-1)R_i
-
(q^2+1).
\]
Hence
\[
B\ge2
\]
is equivalent to
\[
\sum_i(d_i-1)R_i
\ge
(q+1)^2.
\]

There are three cases.

If \(r\ge3\), then every \(d_i\ge2\), so
\[
(d_i-1)R_i
\ge
\binom{q+1}{2}
=
\frac{q(q+1)}2.
\]
Therefore
\[
\sum_i(d_i-1)R_i
\ge
\frac{3q(q+1)}2
\ge
(q+1)^2.
\]
The last inequality is equality only when \(q=2\). Equality throughout then also forces \(r=3\) and every \(d_i=2\). The expected-dimension equation gives \(n=6\), so this is exactly the line curve on a three-quadric intersection.

If \(r=2\) and both degrees equal \(2\), then
\[
\sum_iR_i=q(q+1),
\]
so
\[
1+\sum_iR_i\equiv1\pmod q,
\]
contradicting the expected-dimension equation. Thus at least one defining degree is at least \(3\). The smallest possible left side is therefore
\[
\binom{q+1}{2}
+
2\binom{q+2}{3}
=
\frac{q(q+1)(2q+7)}6,
\]
which is strictly larger than
\[
(q+1)^2
\]
for every \(q\ge2\).

Finally suppose \(r=1\). A quadric cannot occur. Indeed, for \(d_1=2\),
\[
R_1=\frac{q(q+1)}2,
\]
and the divisibility
\[
q\mid R_1+1
\]
forced by the expected-dimension equation has only the formal possibility \(q=2\); that possibility gives \(n=3\), outside the stated range. Hence \(d_1\ge3\).

For \(q\ge3\),
\[
(d_1-1)R_1
\ge
2\binom{q+2}{3}
=
\frac{q(q+1)(q+2)}3
>
(q+1)^2.
\]
For \(q=2\), the expected-dimension divisibility forces \(d_1\) to be even, so \(d_1\ge4\), and then
\[
(d_1-1)R_1
=
d_1^2-1
\ge15
>
9
=
(q+1)^2.
\]

Thus \(B\ge2\) in every admissible case, and equality occurs exactly for
\[
(k,n,\mathbf d)
=
(1,6,(2,2,2)).
\]
Substitution into the known degree computation gives
\[
e=128,
\qquad
g=129.
\]

## Verification
The bundled exact checker exhausts a broad finite box of codimensions, plane dimensions, and defining degrees satisfying
\[
\delta=1.
\]
It recomputes \(B\) from the binomial formula, verifies
\[
B\ge2,
\]
and confirms that the only equality instance in the tested range is
\[
(k,n,\mathbf d)
=
(1,6,(2,2,2)).
\]

The script also checks the three classical calibration examples:
\[
(4)\subset\mathbb P^4,
\qquad
(2,3)\subset\mathbb P^5,
\qquad
(2,2,2)\subset\mathbb P^6,
\]
for which \(B\) equals \(5\), \(3\), and \(2\), respectively.

The finite search is regression evidence only. The infinite theorem is proved by the three-case inequality above.

## Relationship to prior work
Dang Tuan Hiep proves the general genus-degree identity for one-dimensional Fano schemes of linear spaces on complete intersections and records the standard quartic, \((2,3)\), and three-quadric line examples. The same paper gives
\[
e=128,
\qquad
g=129
\]
for the three-quadric line curve.

A later survey by Ciliberto and Zaidenberg recalls the genera
\[
801,\ 271,\ 129
\]
for the Fano curves of lines on the three index-one complete-intersection Fano threefolds and points readers back to the general genus formula. It does not state a universal lower bound comparing genus with Plücker degree, nor does it classify equality across arbitrary \(k\), codimension, and multidegree.

Claim-specific database and literature searches using genus-degree, lower-bound, equality, three-quadrics, and one-dimensional Fano-scheme formulations did not locate the sharp statement
\[
g\ge e+1
\]
or its unique equality classification.

## Limitations
The theorem is a consequence of the known genus-degree formula plus a new sharp arithmetic analysis of the expected-dimension constraint. It does not refine the Plücker degree itself and gives no upper bound for genus.

The result is for general complete intersections over \(\mathbb C\). Special complete intersections can have Fano schemes with singularities, excess dimension, or additional components, so the statement should not be transferred to special fibers without separate hypotheses.

The originality comparison cannot exclude an unindexed classical source in which the same inequality is stated explicitly.

## References
Dang Tuan Hiep, *Numerical invariants of Fano schemes of linear subspaces on complete intersections*, arXiv:1602.03659, first submitted 11 February 2016.

Ciro Ciliberto and Mikhail Zaidenberg, *On Fano schemes of complete intersections*, arXiv:1903.11294.
