# Exact planar sharpness locus of the new Ball-plank basis certificate

## Finding

Let \((x_1,x_2)\) be an orthonormal basis of \(\mathbb R^2\), and let real linear functionals \(\ell_1,\ell_2\) satisfy
\[
\ell_i(x_i)=1.
\]
Put
\[
a=\ell_1(x_2),\qquad b=\ell_2(x_1).
\]
For an ordered orthonormal basis \(Y=(y_1,y_2)\), define
\[
F(Y)=\frac{1}{\ell_1(y_1)^2}+\frac{1}{\ell_2(y_2)^2},
\]
with \(F(Y)=+\infty\) if a denominator vanishes, and set
\[
R(a,b)^2=\min_{Y\in O(2)}F(Y).
\]

Then
\[
R(a,b)=\sqrt2
\]
if and only if
\[
a=b=q,\qquad |q|\le1.
\]
Equivalently, equality with the universal radius occurs exactly when the normalized coefficient matrix
\[
A=
\begin{pmatrix}
1&q\\
q&1
\end{pmatrix}
\]
is positive semidefinite.

More precisely, on the entire symmetric line one has the closed formula
\[
R(q,q)^2=\frac{2}{\max\{1,q^2\}}.
\]
Hence every symmetric indefinite matrix, characterized by \(|q|>1\), gives the strict value
\[
R(q,q)=\frac{\sqrt2}{|q|}<\sqrt2.
\]
If \(a\ne b\), then also
\[
R(a,b)<\sqrt2.
\]

Akopyan and Polyanskii use a minimizing orthonormal basis \(Y\) and points
\[
z_\varepsilon=\sum_{i=1}^2\varepsilon_i p_i y_i,
\qquad
p_i=\frac{1}{\ell_i(y_i)},
\]
whose common squared norm is \(F(Y)\). Therefore the same proof gives witness radius \(R(a,b)\) in dimension two. The theorem above says that the proof's universal radius \(\sqrt2\) is attained at this variational step exactly on the correlation-matrix locus.

## Assumptions and scope

The assertion concerns the basis-minimization invariant introduced in the 2026 proof of Ball's plank theorem. It does not claim that \(R(a,b)\) is the smallest possible radius for which the core avoidance statement is true for all shifts \((c_1,c_2)\). It classifies sharpness of the proof's variational certificate.

The ordered coefficient matrix is normalized by the hypotheses \(\ell_i(x_i)=1\). Reversing the orientation of the moving orthonormal basis does not change the minimization because the relevant denominators are squared.

## Proof

Choose an oriented orthonormal basis
\[
y_1=(\cos\theta)x_1+(\sin\theta)x_2,\qquad
y_2=-(\sin\theta)x_1+(\cos\theta)x_2.
\]
The other component of \(O(2)\) gives the same squared-denominator family after changing a column sign. Thus
\[
F(\theta)=
\frac{1}{(\cos\theta+a\sin\theta)^2}
+
\frac{1}{(\cos\theta-b\sin\theta)^2}.
\]
At \(\theta=0\),
\[
F(0)=2,
\]
so \(R(a,b)^2\le2\). Differentiation gives
\[
F'(0)=2(b-a).
\]
If \(a\ne b\), then \(F'(0)\ne0\). Moving from \(0\) in the sign opposite to \(F'(0)\) decreases \(F\), proving
\[
R(a,b)^2<2.
\]

It remains to analyze \(a=b=q\). The function is then even. For \(\cos\theta\ne0\), put
\[
u=\tan^2\theta\ge0.
\]
A direct simplification gives
\[
F=
\frac{2(1+u)(1+q^2u)}{(1-q^2u)^2}.
\]
Differentiating with respect to \(u\) yields
\[
\frac{dF}{du}
=
-\frac{
2\bigl(q^4u+3q^2u+3q^2+1\bigr)
}{
(q^2u-1)^3
}.
\]
The numerator is strictly positive for \(u\ge0\). Hence, when \(q\ne0\), \(F\) increases from \(2\) on
\[
0\le u<q^{-2},
\]
blows up at \(u=q^{-2}\), and then decreases on
\[
u>q^{-2}
\]
toward the value attained at \(\cos\theta=0\),
\[
\frac{2}{q^2}.
\]
For \(q=0\), one simply has \(F=2(1+u)\).

Therefore
\[
R(q,q)^2=\min\left\{2,\frac{2}{q^2}\right\}
=\frac{2}{\max\{1,q^2\}}.
\]
This equals \(2\) exactly when \(|q|\le1\). Finally,
\[
\begin{pmatrix}
1&q\\
q&1
\end{pmatrix}\succeq0
\]
holds exactly when \(|q|\le1\), proving the stated characterization.

## Verification

The proof is exact and one-dimensional. The accompanying checker symbolically differentiates both the general angular objective at the original basis and the symmetric rationalized objective. It also samples representative symmetric and nonsymmetric matrices as a stress test.

The finite numerical samples are not used to prove the theorem. The strict nonsymmetric case follows from the exact derivative \(F'(0)=2(b-a)\), and the symmetric classification follows from the exact sign of the displayed rational derivative.

## Relationship to prior work

Akopyan and Polyanskii's 2026 note introduces the minimization of
\[
\sum_i\ell_i(y_i)^{-2}
\]
over orthonormal bases as the central variational step in their short proof of Ball's plank theorem. They use only the universal estimate
\[
\min_Y F(Y)\le F(X)=n.
\]
Their note does not classify equality in this minimization, even in dimension two.

Verreault's open-access plank survey explains Ball's earlier matrix proof. In that proof the normalized coefficient matrix is generally nonsymmetric, while a positive-semidefinite symmetric correlation matrix appears after a polar-decomposition step. The planar theorem above identifies exactly that positive-semidefinite symmetric locus as the locus where the new basis-minimization certificate cannot improve the universal radius. This is a statement about the new variational invariant, not a reproof of Ball's theorem.

Targeted searches for equality in the new basis minimization, reciprocal-diagonal-square minimization under planar orthogonal changes of basis, and a correlation-matrix characterization found no equivalent statement.

## Limitations

No closed formula is claimed here for \(R(a,b)\) when \(a\ne b\); only the strict inequality \(R(a,b)<\sqrt2\) is proved. The result does not identify the globally optimal avoidance radius of the core theorem for prescribed functionals and arbitrary shifts. It also does not extend the equality classification to dimensions greater than two.

The originality assessment is based on the inspected 2026 proof, the detailed plank survey, and targeted searches; an equivalent observation under unrelated matrix-optimization terminology could remain unindexed.

## References

1. A. Akopyan and A. Polyanskii, *A short proof of Ball's plank theorem*, arXiv:2609.36163v1, 28 September 2026.
2. W. Verreault, *Plank theorems and their applications: A survey*, Bulletin of the London Mathematical Society 58 (2026), e70230, DOI: 10.1112/blms.70230. Primary MSC 2020: 52-02.
