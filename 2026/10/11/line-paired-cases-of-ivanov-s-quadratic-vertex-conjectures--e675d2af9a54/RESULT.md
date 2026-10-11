# Line-paired cases of Ivanov's quadratic vertex conjectures

## Finding

Let \(d\ge2\). Choose linearly independent unit vectors
\[
u_1,\ldots,u_d\in S^{d-1}
\]
and positive numbers \(\alpha_i,\beta_i\). Define
\[
b_i^+=\alpha_i u_i,
\qquad
b_i^-=-\beta_i u_i,
\qquad
K=\operatorname{conv}\{b_i^+,b_i^-:1\le i\le d\}.
\]
If
\[
B^d\subseteq K,
\]
then
\[
\boxed{
\sum_{i=1}^d(\alpha_i^2+\beta_i^2)\ge2d^2
}
\]
and, more strongly in the linear vertex-index scale,
\[
\boxed{
\sum_{i=1}^d(\alpha_i+\beta_i)\ge2d^{3/2}.
}
\]
Equality in either inequality holds if and only if, after an orthogonal change of coordinates,
\[
u_i=e_i,
\qquad
\alpha_i=\beta_i=\sqrt d
\]
for every \(i\). Thus the unique equality configuration is the regular cross-polytope
\[
\operatorname{conv}\{\pm\sqrt d\,e_i:1\le i\le d\}.
\]

Consequently, Ivanov's quadratic Conjecture 5.1 and the Bezdek--Litvak conjectured linear lower bound both hold for every line-paired \(2d\)-vertex configuration, even when the two vertices on a line have unequal distances from the origin.

There is a matching tight-frame statement. Suppose
\[
v_i^+=a_i u_i,
\qquad
v_i^-=-b_i u_i,
\qquad
a_i,b_i>0,
\]
form a tight frame:
\[
\sum_{i=1}^d\left(v_i^+\otimes v_i^++v_i^-\otimes v_i^-\right)=I_d.
\]
Put
\[
C=\operatorname{conv}\{v_i^+,v_i^-:1\le i\le d\}^{\circ}.
\]
Then
\[
\boxed{
\operatorname{tr}\sqrt{A_\gamma(C)}\ge\sqrt2\,d.
}
\]
Equality holds exactly when
\[
a_i=b_i=\frac1{\sqrt2}
\]
and the \(u_i\) form an orthonormal basis. Hence Ivanov's Conjecture 5.2 holds on the full line-paired tight-frame class.

## Assumptions and scope

A line-paired configuration has exactly two vertices on each of \(d\) independent lines through the origin, one on each ray. The two radii on a line need not agree, so the convex hull need not be centrally symmetric.

The first two inequalities concern configurations whose convex hull contains the Euclidean unit ball. The tight-frame statement uses Ivanov's Gaussian vertex second-moment operator \(A_\gamma(C)\).

The result is a structural special case of two open all-configuration conjectures. It does not settle either conjecture for arbitrary \(2d\) points, and it does not determine the full vertex index of the Euclidean ball.

## Proof

For the containment statement, let \(w_1,\ldots,w_d\) be the basis dual to \(u_1,\ldots,u_d\):
\[
\langle u_j,w_i\rangle=\delta_{ij}.
\]
Because each \(u_i\) is a unit vector,
\[
\|w_i\|\ge1.
\]
Polarity converts
\[
B^d\subseteq K
\]
into
\[
K^{\circ}\subseteq B^d.
\]
The polar is the parallelotope
\[
K^{\circ}
=
\left\{
\sum_{i=1}^d t_iw_i:
-\frac1{\beta_i}\le t_i\le\frac1{\alpha_i}
\right\}.
\]

For each \(i\), choose an independent random variable \(T_i\) with
\[
T_i=\frac1{\alpha_i}
\quad\text{with probability}\quad
\frac{\alpha_i}{\alpha_i+\beta_i},
\]
and
\[
T_i=-\frac1{\beta_i}
\quad\text{with probability}\quad
\frac{\beta_i}{\alpha_i+\beta_i}.
\]
Then
\[
\mathbb E T_i=0,
\qquad
\mathbb E T_i^2=\frac1{\alpha_i\beta_i}.
\]
The vector
\[
Z=\sum_{i=1}^dT_iw_i
\]
is always a vertex of \(K^{\circ}\), hence \(\|Z\|\le1\). Independence and the zero means give
\[
1
\ge
\mathbb E\|Z\|^2
=
\sum_{i=1}^d\frac{\|w_i\|^2}{\alpha_i\beta_i}
\ge
\sum_{i=1}^d\frac1{\alpha_i\beta_i}.
\]
Set
\[
p_i=\alpha_i\beta_i.
\]
Thus
\[
\sum_{i=1}^d\frac1{p_i}\le1.
\]

For the quadratic inequality,
\[
\sum_{i=1}^d(\alpha_i^2+\beta_i^2)
\ge
2\sum_{i=1}^dp_i.
\]
Cauchy--Schwarz yields
\[
\left(\sum_i p_i\right)
\left(\sum_i\frac1{p_i}\right)
\ge d^2,
\]
so
\[
\sum_i p_i\ge d^2.
\]
This proves the quadratic bound.

For the linear inequality, put
\[
x_i=p_i^{-1/2}.
\]
Then
\[
\sum_i x_i^2\le1
\quad\text{and therefore}\quad
\sum_i x_i\le\sqrt d.
\]
Another Cauchy--Schwarz inequality gives
\[
\left(\sum_i x_i\right)
\left(\sum_i\frac1{x_i}\right)
\ge d^2.
\]
Hence
\[
\sum_i\sqrt{p_i}
=
\sum_i\frac1{x_i}
\ge d^{3/2}.
\]
Using \(\alpha_i+\beta_i\ge2\sqrt{p_i}\) proves
\[
\sum_i(\alpha_i+\beta_i)\ge2d^{3/2}.
\]

If equality holds in either final bound, all inequalities in the relevant chain are equalities. This forces
\[
\alpha_i=\beta_i,
\qquad
p_i=d,
\qquad
\sum_i\frac1{p_i}=1,
\qquad
\|w_i\|=1.
\]
Since
\[
\langle u_i,w_i\rangle=1
\]
and both vectors are unit, \(w_i=u_i\). Biorthogonality then makes the \(u_i\) an orthonormal basis, and
\[
\alpha_i=\beta_i=\sqrt d.
\]
The converse equality is immediate because
\[
B^d\subseteq\sqrt d\,B_1^d.
\]

Now assume the line-paired vectors \(v_i^{\pm}\) form a tight frame. Put
\[
c_i=\sqrt{a_i^2+b_i^2}.
\]
The square matrix with columns \(c_iu_i\) satisfies
\[
QQ^{\mathsf T}=I_d,
\]
so it is orthogonal. Therefore the \(u_i\) are orthonormal and
\[
a_i^2+b_i^2=1
\]
for every \(i\).

In this orthonormal basis,
\[
C
=
\prod_{i=1}^d
\left[-\frac1{b_i},\frac1{a_i}\right].
\]
Every vertex normal cone is an orthant, so its Gaussian weight is \(2^{-d}\). A random vertex with these weights has independent coordinates taking \(1/a_i\) and \(-1/b_i\) with probability \(1/2\). Define
\[
m_i=\frac12\left(\frac1{a_i}-\frac1{b_i}\right),
\qquad
\sigma_i=\frac12\left(\frac1{a_i}+\frac1{b_i}\right).
\]
Then
\[
A_\gamma(C)
=
D+m\otimes m,
\qquad
D=\sum_{i=1}^d\sigma_i^2u_i\otimes u_i.
\]
Since \(A_\gamma(C)\succeq D\), operator monotonicity of the positive square root gives
\[
\operatorname{tr}\sqrt{A_\gamma(C)}
\ge
\operatorname{tr}\sqrt D
=
\sum_i\sigma_i.
\]
Because \(a_i^2+b_i^2=1\), one has \(a_ib_i\le1/2\), and hence
\[
\frac1{a_i}+\frac1{b_i}
\ge
\frac2{\sqrt{a_ib_i}}
\ge2\sqrt2.
\]
Thus \(\sigma_i\ge\sqrt2\) and
\[
\operatorname{tr}\sqrt{A_\gamma(C)}\ge\sqrt2\,d.
\]
Equality forces \(a_i=b_i=1/\sqrt2\) for every \(i\), and then \(m=0\); conversely this regular frame gives equality.

## Verification

The proof is all-dimensional and analytic. The bundled checker replays the exact scalar inequalities behind the polar argument on a large rational test family, verifies the regular equality configuration, and checks the line-paired tight-frame scalar bound on rational Pythagorean pairs. It also verifies the random-vertex second-moment decomposition coordinate by coordinate using exact rational arithmetic.

These computations are supplementary. No finite enumeration is used to infer an infinite statement.

The primary full text was inspected at Theorems 1.1--1.2, Conjectures 5.1--5.3, Proposition 5.1, and the discussion identifying the equal-norm and low-dimensional cases already known.

## Relationship to prior work

Ivanov proves Zong's \(2d\)-halfspace theorem and then formulates Conjecture 5.1:
\[
\sum_{i=1}^{2d}\|b_i\|^2\ge2d^2
\]
whenever the convex hull of the \(2d\) vectors contains the unit ball. The paper notes that the theorem settles this only when all \(2d\) norms are equal, and that the older Bezdek--Litvak result settles dimensions two and three. The line-paired theorem above removes the equal-norm assumption in every dimension on the natural cross-polytope combinatorial class.

Ivanov's Conjecture 5.2 asks for
\[
\operatorname{tr}\sqrt{A_\gamma(C)}\ge\sqrt2\,d
\]
for every tight frame of \(2d\) vectors with the origin in the interior of its convex hull. The line-paired tight-frame proof above supplies the full conjectured constant and equality case on the corresponding asymmetric box class.

Bezdek and Litvak conjectured
\[
\operatorname{vein}(B^d)=2d^{3/2}
\]
for arbitrary finite outer vertex sets. Their paper proves the exact Euclidean-ball value only in dimensions two and three and gives high-dimensional estimates. The present linear inequality proves their conjectured lower bound for every line-paired \(2d\)-vertex outer polytope, but does not address arbitrary outer vertex sets.

Targeted searches for asymmetric cross-polytopes, paired lines, dual parallelotopes, the quadratic sum, and the vertex-index sum found no prior all-dimensional statement with these hypotheses and equality classification. A dimension-four parallelotope edge-length estimate appears in unrelated classical geometric literature, reflecting that the sign-averaging mechanism itself is elementary; no inspected source connected it to these line-paired conjectures or supplied the all-dimensional asymmetric conclusion.

## Limitations

The vertices must lie on exactly \(d\) independent lines through the origin, with one vertex on each ray. Arbitrary \(2d\)-point configurations remain open.

For the tight-frame statement, the same line-pairing restriction is essential to the proof because it forces the frame directions to be orthogonal. No claim is made for a general tight frame of \(2d\) vectors.

The main residual originality risk is an older formulation of the polar-parallelotope argument under different terminology. The targeted vertex-index, cross-polytope, parallelotope, and tight-frame searches did not reveal such a formulation with the conjecture-level consequences stated here.

## References

1. Grigory Ivanov, *Zong's problem on \(2d\) half-spaces containing the unit ball*, arXiv:2609.38394v1, 29 September 2026.
2. Károly Bezdek and Alexander E. Litvak, *On the vertex index of convex bodies*, Advances in Mathematics 215 (2007), 626--641; arXiv:1110.4334.
3. Efim D. Gluskin and Alexander E. Litvak, *A remark on vertex index of the convex bodies*, in *Geometric Aspects of Functional Analysis*, Lecture Notes in Mathematics 2050 (2012), 255--265.
