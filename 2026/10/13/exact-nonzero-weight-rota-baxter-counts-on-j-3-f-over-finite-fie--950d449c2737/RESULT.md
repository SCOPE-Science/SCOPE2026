# Exact nonzero-weight Rota–Baxter counts on \(J_3(f)\) over finite fields

## Finding

Let \(q\) be an odd prime power, let \(V\) be a two-dimensional vector space over \(\mathbf F_q\), and let \(f\) be a nondegenerate symmetric bilinear form on \(V\). Write
\[
J_3(f)=\mathbf F_q1\oplus V
\]
for the Jordan algebra of bilinear form, with multiplication
\[
(\alpha1+u)(\beta1+v)
=(\alpha\beta+f(u,v))1+\alpha v+\beta u.
\]
Fix a nonzero Rota–Baxter weight
\[
\Delta\in\mathbf F_q^\times.
\]
Then the number of weight-\(\Delta\) Rota–Baxter operators on \(J_3(f)\) is
\[
\boxed{2q(q+1)+2=2q^2+2q+2}.
\]
More precisely, the numbers in ranks \(0,1,2,3\) are
\[
\boxed{1,\quad q(q+1),\quad q(q+1),\quad1}.
\]
The answer is independent of the isometry class, discriminant, and Witt type of \(f\).

After scalar extension to \(\mathbf F_{q^m}\), the number becomes
\[
N_m=2q^{2m}+2q^m+2.
\]
Thus the point-count zeta function of the weight-\(\Delta\) operator locus is
\[
\boxed{
Z(T)=\exp\!\left(\sum_{m\ge1}N_m\frac{T^m}{m}\right)
=\frac{1}{(1-T)^2(1-qT)^2(1-q^2T)^2}.
}
\]

## Assumptions and scope

The field has characteristic different from \(2\). The finite-field statement assumes \(q\) odd and \(f\) nondegenerate. The weight \(\Delta\) is fixed and nonzero.

Benito, Gubarev, and Pozhidaev define \(J_{n+1}(f)\) and prove that every nonzero-weight Rota–Baxter operator on an odd-dimensional simple Jordan algebra of bilinear form is splitting. Their Example 13 specializes the classification to \(J_3(f)\): up to the involution
\[
\phi(R)=-R-\Delta I,
\]
a nontrivial operator has one-dimensional image, two-dimensional kernel, and is the splitting projection determined by a two-dimensional unital subalgebra and a complementary one-dimensional subalgebra.

The present result extracts the exact finite-field arithmetic of that complete classification.

## Proof

Choose an orthogonal basis \(e_1,e_2\) of \(V\), so that
\[
f(e_i,e_i)=d_i\ne0,
\qquad
f(e_1,e_2)=0.
\]
A nonzero vector
\[
z=\alpha1+x e_1+y e_2
\]
spans a one-dimensional subalgebra exactly when \(z^2\) is a scalar multiple of \(z\). For a nonscalar line this is equivalent to
\[
\alpha^2-d_1x^2-d_2y^2=0.
\]
Hence the possible one-dimensional image subalgebras are the rational points of the nonsingular projective conic
\[
C_f:\quad \alpha^2-d_1x^2-d_2y^2=0
\]
in \(\mathbf P^2\).

Every nonsingular projective conic over \(\mathbf F_q\) has exactly
\[
q+1
\]
rational points. One elementary route is that a homogeneous quadratic form in three variables over a finite field has a nonzero zero, and a nonsingular conic with a rational point is isomorphic to \(\mathbf P^1\). Thus there are exactly \(q+1\) possible image lines.

Every two-dimensional subspace containing \(1\) is of the form
\[
A_1=\mathbf F_q1\oplus\mathbf F_q w,
\qquad 0\ne w\in V,
\]
and it is automatically a subalgebra because
\[
w^2=f(w,w)1.
\]
Therefore such subalgebras are indexed by the \(q+1\) points of \(\mathbf P(V)\).

Fix an image line
\[
A_2=\mathbf F_q(\alpha1+v),
\qquad 0\ne v\in V.
\]
Among the \(q+1\) unital two-dimensional subalgebras, exactly one fails to be complementary to \(A_2\): namely
\[
\mathbf F_q1\oplus\mathbf F_q v.
\]
Consequently exactly
\[
q
\]
choices of \(A_1\) complement each fixed \(A_2\).

Benito–Gubarev–Pozhidaev's splitting classification now gives exactly one rank-one operator for each ordered complementary pair \((A_1,A_2)\), namely
\[
R(a_1+a_2)=-\Delta a_2.
\]
Therefore the number of rank-one operators is
\[
(q+1)q=q(q+1).
\]

The involution
\[
\phi(R)=-R-\Delta I
\]
sends a splitting projection with kernel \(A_1\) and image \(A_2\) to the complementary splitting projection with kernel \(A_2\) and image \(A_1\). Hence it bijects the rank-one operators with rank-two operators, giving another
\[
q(q+1).
\]
The only rank-zero and rank-three operators are the two trivial operators
\[
0
\qquad\text{and}\qquad
-\Delta I.
\]
This proves the rank distribution and the total
\[
2q(q+1)+2.
\]

The same argument works after every finite extension \(\mathbf F_{q^m}\), where the nonsingular conic has \(q^m+1\) rational points. Hence
\[
N_m=2q^{2m}+2q^m+2.
\]
Substitution into the exponential definition of the point-count zeta function gives
\[
Z(T)
=\frac{1}{(1-T)^2(1-qT)^2(1-q^2T)^2}.
\]

## Verification

The included program `artifacts/verify.py` reconstructs the Jordan product and the weight-one Rota–Baxter identity over finite prime fields. Scaling of a nonzero weight reduces the verification to weight one.

For each of
\[
q=3,5,7,11,
\]
it checks representatives of both discriminant classes of nondegenerate diagonal binary forms, enumerates the conic points, constructs every predicted splitting operator from complementary subalgebras, verifies the Rota–Baxter identity directly, and confirms the rank distribution.

For \(q=3\), for both form classes, it additionally exhausts all
\[
3^9=19683
\]
linear endomorphisms of \(J_3(f)\). In each case the complete ambient search returns exactly
\[
1,12,12,1
\]
operators in ranks \(0,1,2,3\), totaling \(26\), with no operators outside the predicted family.

The checker returns `VERIFY_OK`.

The finite checks are replay evidence. The arbitrary odd-prime-power statement follows from the splitting theorem and the projective-conic count in the proof above.

## Relationship to prior work

The primary paper proves the decisive structural classification. Theorem 4.1 says that all nonzero-weight Rota–Baxter operators on the odd-dimensional simple Jordan algebra of bilinear form are splitting. Statement 4.4 and Example 13 specialize this to \(J_3(f)\), giving a two-dimensional kernel and a one-dimensional image up to \(\phi\), together with the quadratic equation defining the image line and the direct-sum condition.

The paper does not count these operators over finite fields, separate them by rank, or state the extension-field point counts and zeta function.

The earlier zero-weight paper of Gubarev treats nilpotency indices for Rota–Baxter operators of weight zero on Jordan algebras of Clifford type. Its hypotheses and operator locus are different from the fixed nonzero-weight locus here.

Targeted searches for finite-field counts, \(J_3(f)\) operator numbers, bilinear-form Jordan algebras, and equivalent rank-distribution formulations found no source stating the displayed formulas.

## Limitations

The result is specific to the three-dimensional Jordan algebra \(J_3(f)\) and nonzero Rota–Baxter weight.

Characteristic \(2\) is excluded, as in the primary classification.

The point-count zeta function records the operator locus over finite extensions; no claim is made here about a finer scheme structure or singularity decomposition.

A differently phrased finite-field enumeration could exist under Clifford-type terminology; this remains the principal literature risk.

## References

1. P. Benito, V. Gubarev, and A. Pozhidaev, “Rota–Baxter Operators on Quadratic Algebras,” *Mediterranean Journal of Mathematics* 15 (2018), article 189, DOI `10.1007/s00009-018-1234-5`; arXiv:1801.07037.
2. V. Gubarev, “Rota–Baxter operators of zero weight on simple Jordan algebra of Clifford type,” *Siberian Electronic Mathematical Reports* 14 (2017), 1524–1532; arXiv:1710.02377.
