# Exact lower endpoint and full fixed-profile range for expected maxima

## Finding

Fix an integer \(n\ge2\). Let \(X\) be a nondegenerate discrete random
variable with distinct ordered atoms
\[
x_1<\cdots<x_m
\]
and prescribed positive masses
\[
p_1,\ldots,p_m,
\qquad
\sum_{i=1}^m p_i=1.
\]
Let
\[
P_j=\sum_{i=1}^j p_i,
\qquad P_0=0,
\]
and let \(X_1,\ldots,X_n\) be iid copies of \(X\). Define
\[
M_n=\max(X_1,\ldots,X_n)
\]
and the standardized expected-maximum gap
\[
R_n(X)=
\frac{\mathbb E M_n-\mathbb E X}
{\sqrt{\operatorname{Var}(X)}}.
\]

Set
\[
w_i=P_i^n-P_{i-1}^n
\]
and define
\[
L_n(\mathbf p)
=
\min_{1\le j<m}
\frac{P_j-P_j^n}{\sqrt{P_j(1-P_j)}},
\tag{1}
\]
\[
U_n(\mathbf p)
=
\sqrt{
\sum_{i=1}^m\frac{w_i^2}{p_i}-1
}.
\tag{2}
\]

If \(m\ge3\), then the exact attainable range over all strictly increasing
support locations carrying the fixed mass profile \(\mathbf p\) is
\[
\boxed{
R_n(X)\in
\bigl(L_n(\mathbf p),\,U_n(\mathbf p)\bigr].
}
\tag{3}
\]

The upper endpoint in (3) is attained exactly when
\[
x_i=a+b\frac{w_i}{p_i},
\qquad b>0.
\tag{4}
\]
This is the classical projection extremizer for the discrete
expected-maximum upper bound.

The lower endpoint is not attained when \(m\ge3\), but it is a sharp
infimum. If a cut \(j\) attains the minimum in (1), the infimum is approached
by collapsing
\[
x_1,\ldots,x_j
\]
toward one level and
\[
x_{j+1},\ldots,x_m
\]
toward a second level while retaining strict inequalities between all atoms.

For \(m=2\),
\[
\boxed{
L_n(\mathbf p)=U_n(\mathbf p)=R_n(X),
}
\tag{5}
\]
so every two-point support with the prescribed masses has the same
standardized expected-maximum gap.

For equal masses \(p_i=1/m\), the lower endpoint reduces to the finite cut
formula
\[
L_{n,m}
=
\min_{1\le j<m}
\sqrt{\frac{j}{m-j}}
\left[
1-\left(\frac jm\right)^{n-1}
\right].
\tag{6}
\]
Thus even after the mass profile is fixed, the standardized expected maximum
has a nontrivial sharp lower geometry as well as the familiar projection
upper geometry.

## Assumptions and scope

The sample is iid and the support has finitely many distinct atoms. The mass
profile is fixed while the ordered support locations are allowed to vary.

The theorem concerns the normalized excess of the sample maximum over the
parent mean. Location and positive scale changes of the support leave
\(R_n(X)\) unchanged.

The upper endpoint is included to give the complete attainable interval, but
its projection formula is established prior literature. The new part is the
sharp lower endpoint, its two-level-collapse extremizers in the closure, and
the proof that every intermediate value is attainable.

## Proof

The maximum has atom probabilities
\[
\Pr(M_n=x_i)=w_i=P_i^n-P_{i-1}^n.
\]
Define the score
\[
s_i=\frac{w_i}{p_i}.
\]
Since
\[
\sum_i p_i s_i=\sum_i w_i=1,
\]
we have
\[
\mathbb E M_n-\mathbb E X
=
\sum_i p_i x_i(s_i-1)
=
\operatorname{Cov}(X,S),
\tag{7}
\]
where \(S=s_i\) on the event \(X=x_i\).

The function
\[
g(u)=nu^{n-1}
\]
is strictly increasing on \((0,1)\), and
\[
s_i
=
\frac1{p_i}
\int_{P_{i-1}}^{P_i}g(u)\,du.
\]
Therefore
\[
s_1<\cdots<s_m.
\tag{8}
\]

Cauchy--Schwarz applied to (7) gives
\[
R_n(X)
\le
\sqrt{\operatorname{Var}(S)}
=
U_n(\mathbf p).
\tag{9}
\]
Equality holds exactly when \(X\) is an increasing affine function of \(S\),
which is (4).

We now prove the lower endpoint. Center the support:
\[
y_i=x_i-\mathbb E X.
\]
Write the adjacent gaps as
\[
d_j=x_{j+1}-x_j>0.
\]
For \(1\le j<m\), define the centered threshold vector
\[
v^{(j)}_i
=
\mathbf 1_{\{i>j\}}-(1-P_j).
\]
Then
\[
y=\sum_{j=1}^{m-1}d_jv^{(j)}.
\tag{10}
\]

In the weighted inner product
\[
\langle a,b\rangle_p=\sum_i p_i a_i b_i,
\]
one has
\[
\|v^{(j)}\|_p^2=P_j(1-P_j).
\tag{11}
\]
Also, using \(\sum_i p_i(s_i-1)=0\),
\[
\begin{aligned}
\langle v^{(j)},S-1\rangle_p
&=
\sum_{i>j}p_i(s_i-1)\\
&=
(1-P_j^n)-(1-P_j)\\
&=
P_j-P_j^n.
\end{aligned}
\tag{12}
\]
Hence, by the definition of \(L_n(\mathbf p)\),
\[
\langle v^{(j)},S-1\rangle_p
\ge
L_n(\mathbf p)\|v^{(j)}\|_p.
\]
Using (10), followed by the triangle inequality,
\[
\begin{aligned}
\mathbb E M_n-\mathbb E X
&=
\langle y,S-1\rangle_p\\
&\ge
L_n(\mathbf p)
\sum_j d_j\|v^{(j)}\|_p\\
&\ge
L_n(\mathbf p)\|y\|_p\\
&=
L_n(\mathbf p)\sqrt{\operatorname{Var}(X)}.
\end{aligned}
\tag{13}
\]

If \(m\ge3\), at least two coefficients \(d_j\) are positive. Distinct
centered threshold vectors \(v^{(j)}\) are not positive scalar multiples of
one another, so the triangle inequality in (13) is strict. This proves
\[
R_n(X)>L_n(\mathbf p).
\]

If a cut \(j_*\) minimizes (1), choose supports whose gap at \(j_*\) is fixed
and whose other gaps tend to zero through positive values. After centering and
rescaling, the support vector converges to
\[
v^{(j_*)}.
\]
Equation (12) then shows
\[
R_n(X)\longrightarrow L_n(\mathbf p).
\]
Thus the lower endpoint is the exact infimum.

For \(m=2\), there is only one threshold vector, so both the lower argument
and Cauchy--Schwarz are equalities. This proves (5).

Finally, modulo translation and positive scale, the strictly positive gap
vectors form a connected open simplex. The map from the gap vector to
\(R_n(X)\) is continuous. Its image is therefore an interval. It contains
the upper endpoint by (4) and has lower infimum \(L_n(\mathbf p)\), proving
the full range (3).

Formula (6) follows by substituting
\[
P_j=\frac jm
\]
into (1).

## Verification

The accompanying exact-rational checker verifies the score identity, threshold
decomposition, lower and upper inequalities, the exact upper equality
support, and two-point equality over thousands of rational probability
profiles and rational supports.

It also constructs strict supports converging to each minimizing two-level
cut and verifies convergence of the squared standardized gap to the claimed
lower constant.

The finite checks are supplementary. The universal proof is the cone
decomposition and connectedness argument above.

## Relationship to prior work

López-Blázquez studied the upper problem for discrete parents in 1998:
maximizing the expected sample maximum under mean and variance constraints
and characterizing the maximizing discrete distributions. The accessible
publisher material states the upper-bound objective and begins from arbitrary
positive masses on ordered support points. That is precisely the upper side
represented by (2)--(4). The complete article was not available for inspection
in this review, so it remains a residual source risk for the lower endpoint.

Balakrishnan, Charalambides, and Papadatos later derived best possible
expected-order-statistic bounds for sampling without replacement from an
equiprobable finite population. Their model and optimization constraints are
different from fixing an arbitrary iid atom-probability profile.

Papadatos gives a full treatment of sequences of expected maxima and expected
ranges and, in a constructive argument, records the exact maximum probabilities
for iid sampling from discrete uniform approximants. That work concerns which
sequences can arise as expected maxima, not the minimum standardized maximum
over support geometries with prescribed atom probabilities.

The classical Hartley--David--Gumbel bound controls the expected maximum using
only mean and variance. The fixed-profile lower endpoint in (1) is of a
different direction: it prevents the expected maximum from approaching the
parent mean too closely once the ordered atom masses are held fixed.

Targeted searches using lower-bound, fixed-probability-profile,
standardized-maximum, support-optimization, and discrete-order-statistic
terminology did not locate (1), the two-level-collapse characterization, or
the complete interval (3).

## Limitations

The lower endpoint is generally an infimum rather than a minimum because the
support atoms are required to remain distinct.

No positive profile-free lower bound exists when the number and probabilities
of atoms are allowed to vary freely; the result is intentionally
profile-specific.

The most directly related 1998 upper-bound paper could not be inspected in
full. Its accessible abstract and introduction describe an upper optimization,
not the lower endpoint, but an unobserved lower-side remark remains a residual
originality risk.

## References

1. F. López-Blázquez, “Discrete distributions with maximum expected value of
   the maximum,” *Journal of Statistical Planning and Inference* 70 (1998),
   201--207, DOI 10.1016/S0378-3758(97)00181-X.
2. N. Balakrishnan, C. Charalambides, and N. Papadatos, “Bounds on
   expectation of order statistics from a finite population,” *Journal of
   Statistical Planning and Inference* 113 (2003), 569--588,
   DOI 10.1016/S0378-3758(01)00321-4.
3. N. Papadatos, “On sequences of expected maxima and expected ranges,”
   arXiv:1610.06835, first submitted 2016-10-21.
4. H. O. Hartley and H. A. David, “Universal bounds for mean range and extreme
   observation,” *Annals of Mathematical Statistics* 25 (1954), 85--99.
5. E. J. Gumbel, “The maxima of the mean largest value and of the range,”
   *Annals of Mathematical Statistics* 25 (1954), 76--84.
