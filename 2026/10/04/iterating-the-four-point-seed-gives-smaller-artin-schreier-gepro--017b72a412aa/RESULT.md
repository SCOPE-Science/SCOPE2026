# Iterating the four-point seed gives smaller Artin--Schreier geproci families
## Finding
Let \(K\) be an algebraically closed field of characteristic \(p>0\). For every integer
\[
n\ge4,
\]
the Artin--Schreier lifting construction of Chiantini--Farnik--Favacchio--Harbourne--Migliore--Szemberg--Szpond can be iterated from four general points in \(\mathbf P^3\) to give geproci sets in \(\mathbf P^n\) with complete-intersection degrees strictly smaller, term by term, than those in their Propositions 4.5 and 4.6.

If
\[
p\ge3,
\]
there is a geproci set
\[
Z_n\subset\mathbf P^n
\]
whose general projection is a complete intersection of type
\[
(2,2,p,p^2,\ldots,p^{n-3}).
\]
Its cardinality is
\[
|Z_n|
=
4p^{1+2+\cdots+(n-3)}
=
4p^{(n-3)(n-2)/2}.
\]

If
\[
p=2,
\]
there is a geproci set
\[
Z_n\subset\mathbf P^n
\]
whose general projection is a complete intersection of type
\[
(2,2,4,8,\ldots,2^{n-2}).
\]
Its cardinality is
\[
|Z_n|
=
4\prod_{i=2}^{n-2}2^i
=
2^{(n-2)(n-1)/2+1}.
\]

The paper's Proposition 4.5 gives, for \(p\ge3\), type
\[
(3,p,p^2,\ldots,p^{n-2})
\]
with
\[
3p^{(n-1)(n-2)/2}
\]
points. Proposition 4.6 gives, for \(p=2\), type
\[
(3,4,8,\ldots,2^{n-1})
\]
with
\[
3\cdot2^{n(n-1)/2-1}
\]
points. Every degree in the new type is strictly smaller than the corresponding degree in the published type.

Consequently the new families answer affirmatively the "in particular" clause of Question 5.2 in the initiating paper: the Artin--Schreier lifting procedure does produce geproci sets in higher projective spaces with complete-intersection degrees smaller than those of Propositions 4.5 and 4.6.

## Assumptions and scope
A finite nondegenerate set \(X\subset\mathbf P^m\) is geproci of type
\[
(d_1,\ldots,d_{m-1})
\]
if its projection from a general point to \(\mathbf P^{m-1}\) is a reduced complete intersection of those degrees.

The construction uses Theorem 4.2 of the initiating paper. That theorem starts with a geproci set \(X\subset\mathbf P^m\), forms a cone over \(X\) in \(\mathbf P^{m+1}\), and places an \(\mathbf F_N\)-Artin--Schreier orbit on each generator, where
\[
N=p^e.
\]
If the evaluation map on a general projected complete intersection is surjective in degree
\[
N-1,
\]
the lifted set is geproci and its complete-intersection type is obtained by appending \(N\).

The argument below uses only this theorem, the standard regularity formula for a zero-dimensional complete intersection, and Example 4.3 of the same paper, which starts from four general points.

No optimality claim is made among all conceivable geproci constructions or among special Artin--Schreier choices for which surjectivity might fail but the required interpolation vectors happen to lie in the evaluation image.

## Proof
Let \(X_3\subset\mathbf P^3\) be four general points. Their general projection to \(\mathbf P^2\) is a complete intersection of type
\[
(2,2).
\]
Thus \(X_3\) is a \((2,2)\)-geproci set. This is precisely the seed used in Example 4.3 of the initiating paper.

For a zero-dimensional complete intersection
\[
\Gamma\subset\mathbf P^r
\]
of type
\[
(d_1,\ldots,d_r),
\]
the coordinate ring has regularity
\[
\operatorname{reg}(S/I_\Gamma)
=
\sum_{i=1}^{r}(d_i-1).
\]
Therefore the evaluation map on \(\Gamma\) is surjective in every degree at least that integer.

Assume first that \(p\ge3\). Since the \((2,2)\) complete intersection has regularity
\[
(2-1)+(2-1)=2,
\]
the degree-\((p-1)\) evaluation map is surjective. Theorem 4.2 with \(N=p\) therefore lifts \(X_3\) to a set
\[
Z_4\subset\mathbf P^4
\]
of type
\[
(2,2,p).
\]

Now suppose inductively that, for some \(m\ge4\), a geproci set
\[
Z_m\subset\mathbf P^m
\]
has general projected complete-intersection type
\[
(2,2,p,p^2,\ldots,p^{m-3}).
\]
Its coordinate-ring regularity is
\[
r_m
=
2+\sum_{i=1}^{m-3}(p^i-1).
\]
For \(p\ge3\),
\[
r_m
\le
p^{m-2}-1.
\]
Indeed,
\[
p^{m-2}-1-r_m
=
p^{m-2}-3-\sum_{i=1}^{m-3}(p^i-1),
\]
which is positive for \(m\ge4\) and \(p\ge3\). Hence the evaluation map is surjective in degree
\[
p^{m-2}-1.
\]
Applying Theorem 4.2 with
\[
N=p^{m-2}
\]
produces
\[
Z_{m+1}\subset\mathbf P^{m+1}
\]
of type
\[
(2,2,p,p^2,\ldots,p^{m-2}).
\]
This proves the odd-characteristic family by induction.

Its number of points is the product of the complete-intersection degrees:
\[
|Z_n|
=
4\prod_{i=1}^{n-3}p^i
=
4p^{(n-3)(n-2)/2}.
\]

Now let \(p=2\). The \((2,2)\) seed has regularity \(2\), so the first available Artin--Schreier orbit size whose degree-minus-one is at least \(2\) is
\[
N=4.
\]
Theorem 4.2 gives a set in \(\mathbf P^4\) of type
\[
(2,2,4).
\]

Inductively, suppose
\[
Z_m\subset\mathbf P^m
\]
has type
\[
(2,2,4,8,\ldots,2^{m-2}).
\]
Its coordinate-ring regularity is
\[
r_m
=
2+\sum_{i=2}^{m-2}(2^i-1)
=
2^{m-1}-m+1.
\]
Since
\[
2^{m-1}-m+1
\le
2^{m-1}-1,
\]
the degree-\((2^{m-1}-1)\) evaluation map is surjective. Theorem 4.2 with
\[
N=2^{m-1}
\]
therefore gives a lift in \(\mathbf P^{m+1}\) of type
\[
(2,2,4,8,\ldots,2^{m-1}).
\]
Thus
\[
|Z_n|
=
4\prod_{i=2}^{n-2}2^i
=
2^{(n-2)(n-1)/2+1}.
\]

Finally, compare with the published types. For \(p\ge3\),
\[
(2,2,p,p^2,\ldots,p^{n-3})
<
(3,p,p^2,\ldots,p^{n-2})
\]
coordinatewise. For \(p=2\),
\[
(2,2,4,8,\ldots,2^{n-2})
<
(3,4,8,\ldots,2^{n-1})
\]
coordinatewise. This is exactly the requested strict reduction in complete-intersection degrees.

## Verification
The accompanying `verify.py` checks the induction inequalities, degree lists, cardinality formulas, and coordinatewise comparisons for all primes
\[
p\le97
\]
and all dimensions
\[
4\le n\le30.
\]
It also checks the symbolic closed forms used in the proof against their finite sums.

The finite computation is only a consistency check. The all-\(p\), all-\(n\) proof is the induction above, based on Theorem 4.2 and the complete-intersection regularity formula.

The stored replay output ends in `VERIFY_OK`.

## Relationship to prior work
The initiating paper introduces Artin--Schreier geproci configurations, proves the lifting theorem, and gives explicit dimension-uniform families in Propositions 4.5 and 4.6. It also gives Example 4.3: four general points in \(\mathbf P^3\) can be lifted to a geproci set in \(\mathbf P^4\) of type
\[
(2,2,N)
\]
whenever the degree-\((N-1)\) evaluation map is surjective.

Immediately afterward, Question 5.2 asks how sharp the regularity bound is and, in particular, whether the lifting procedure can produce complete-intersection degrees smaller than those in Propositions 4.5 and 4.6. The paper does not iterate Example 4.3 or state the two dimension-uniform sequences proved here.

An earlier paper by the same authors emphasizes that four general points are the basic known geproci set in linear general position in \(\mathbf P^3\), but it predates the positive-characteristic Artin--Schreier lifting construction and therefore does not contain these higher-dimensional families.

Targeted searches for the exact degree sequences, their cardinalities, the four-point Artin--Schreier iteration, and an answer to Question 5.2 located no covering statement.

## Limitations
The result answers the "in particular" clause of Question 5.2, not the entire sharpness problem. It does not prove that the displayed degree sequences are optimal among all possible Artin--Schreier configurations, nor among all geproci sets.

The construction uses the surjectivity criterion in Theorem 4.2. Special orbit data might permit a successful interpolation even when the full evaluation map is not surjective, so the present argument does not exclude still smaller degrees.

The originality comparison is strongest against the full initiating paper and the earlier same-author geproci literature inspected for the four-point seed. An unindexed note could have observed the same iteration independently.

## References
1. L. Chiantini, Ł. Farnik, G. Favacchio, B. Harbourne, J. Migliore, T. Szemberg, J. Szpond, *Artin--Schreier geproci configurations in projective spaces of arbitrary dimension*, arXiv:2609.03024v1, 2026.
2. L. Chiantini, Ł. Farnik, G. Favacchio, B. Harbourne, J. Migliore, T. Szemberg, J. Szpond, *Configurations of points in projective space and their projections*, arXiv:2209.04820.
3. L. Chiantini, Ł. Farnik, G. Favacchio, B. Harbourne, J. Migliore, T. Szemberg, J. Szpond, *Finite sets of points in \(\mathbf P^4\) with special projection properties*, arXiv:2407.01744v1.
