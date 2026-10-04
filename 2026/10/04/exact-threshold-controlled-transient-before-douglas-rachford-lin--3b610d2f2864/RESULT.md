# Exact threshold-controlled transient before Douglas--Rachford linear convergence in two-variable basis pursuit
## Finding
Consider the two-variable basis-pursuit problem
\[
\min_{x\in\mathbb R^2} |x_1|+|x_2|
\qquad\text{subject to}\qquad
x_1+a x_2=b,
\]
where \(0<a<1\) and \(b>0\). Apply the standard Douglas--Rachford iteration used by Demanet and Zhang, with soft-threshold \(\gamma>0\), projection \(P\) onto the affine constraint, reflection \(R=2P-I\), and initialization \(y^0=0\):
\[
y^{k+1}=S_\gamma(Ry^k)+y^k-Py^k.
\]
If
\[
\gamma\ge \frac{b}{1-a},
\]
then the unique minimizer is \(x^*=(b,0)\), one Douglas--Rachford fixed point is
\[
y^*=(b-\gamma,-a\gamma),
\]
and the first iterate whose reflected point belongs to the correct sign/support cell
\[
\mathcal Q=(\gamma,\infty)\times[-\gamma,\gamma]
\]
is exactly
\[
k_*=
\max\!\left\{0,\left\lfloor\frac{\gamma(1+a^2)}{b}\right\rfloor-1}\right\}.
\]
Moreover \(Ry^k\in\mathcal Q\) for every \(k\ge k_*\), and the subsequent error has the exact norm law
\[
\|y^{k_*+n}-y^*\|_2
=
\left(\frac{a}{\sqrt{1+a^2}}\right)^n
\|y^{k_*}-y^*\|_2,
\qquad n=0,1,2,\ldots.
\]
Thus the post-identification factor is the principal-angle rate already associated with this basis-pursuit model, but the exact onset time can be made arbitrarily large by increasing \(\gamma/b\). In this family, asymptotic rate tuning alone does not control the transient.

## Assumptions and scope
The statement concerns standard, unregularized Douglas--Rachford splitting in the ordering used by Demanet--Zhang: soft-thresholding is applied to the affine reflection. The initialization is exactly \(y^0=0\), the affine row is \((1,a)\), and \(0<a<1\). The explicit invariance proof uses the sufficient large-threshold condition \(\gamma\ge b/(1-a)\). The theorem does not claim that this condition is necessary for permanent support identification, nor that the same exact delay formula holds for arbitrary initializations or higher-dimensional sensing matrices.

## Proof
Put
\[
d=1+a^2,
\qquad
A=\begin{bmatrix}1&a\end{bmatrix}.
\]
The affine projector and reflector are
\[
P(y)=y+\frac{(1,a)^\top}{d}\bigl(b-y_1-a y_2\bigr),
\qquad
R(y)=2P(y)-y.
\]
The point \(x^*=(b,0)\) is the unique basis-pursuit minimizer. Indeed,
\[
|b-a x_2|+|x_2|
\ge |b-a x_2|+a|x_2|
\ge b,
\]
and equality in the first inequality forces \(x_2=0\).

As long as \(S_\gamma(Ry^k)=0\), induction gives
\[
y^k=-\frac{k b}{d}(1,a)^\top,
\qquad
P(y^k)=\frac{b}{d}(1,a)^\top,
\qquad
R(y^k)=\frac{(k+2)b}{d}(1,a)^\top.
\]
Let
\[
t=\frac{\gamma d}{b}.
\]
The first coordinate of \(R(y^k)\) crosses the strict soft-threshold exactly when \(k+2>t\). Therefore the first candidate index is
\[
k_*=
\max\{0,\lfloor t\rfloor-1\}.
\]
Write \(j=k_*+2\); then \(j\) is the smallest integer at least \(2\) satisfying \(j>t\). Under \(\gamma\ge b/(1-a)\), one has \(t\ge d/(1-a)>a/(1-a)\), and hence
\[
a j\le a(t+1)<t.
\]
Consequently the second reflected coordinate is still inside its threshold when the first one activates, so \(R(y^{k_*})\in\mathcal Q\).

Now define
\[
y^*=(b-\gamma,-a\gamma)^\top.
\]
Its projection is \(P(y^*)=x^*\), while
\[
R(y^*)=(b+\gamma,a\gamma)^\top
\]
and \(S_\gamma(R(y^*))=x^*\). Hence \(y^*\) is a fixed point.

Inside \(\mathcal Q\), soft-thresholding is affine with derivative \(E=\operatorname{diag}(1,0)\). If \(e^k=y^k-y^*\), the error update is exactly
\[
e^{k+1}=M e^k,
\qquad
M=\frac1d
\begin{bmatrix}
a^2&-a\
a&a^2
\end{bmatrix}.
\]
A direct calculation gives
\[
M^\top M=\frac{a^2}{d}I,
\]
so every step in this affine cell contracts the Euclidean error by the exact factor
\[
r=\frac{a}{\sqrt d}.
\]
It remains to show that the iterate cannot leave \(\mathcal Q\) after first entry. Let \(\delta=j-t\in(0,1]\). Substituting the pre-entry formula gives
\[
e^{k_*}
=\frac{b}{d}
\begin{bmatrix}
1-a^2-\delta\
a(2-\delta)
\end{bmatrix},
\]
and therefore
\[
\|e^{k_*}\|_2^2
=\frac{b^2}{d}\bigl(a^2+(1-\delta)^2\bigr)
<b^2.
\]
The linear part of the affine reflection is orthogonal, so reflected-point errors have the same Euclidean norm. The fixed reflected point \((b+\gamma,a\gamma)\) is a distance \(b\) from the first threshold boundary and a distance \(\gamma(1-a)\) from the upper second-coordinate boundary. Since \(\gamma(1-a)\ge b\), the open ball of radius \(\|e^{k_*}\|_2<b\) around the fixed reflected point lies inside \(\mathcal Q\). One linear step multiplies this radius by \(r<1\), so induction proves invariance of \(\mathcal Q\) and the exact norm formula for all \(n\ge0\).

Finally, the principal angle between \(\mathcal N(A)=\operatorname{span}\{(-a,1)\}\) and the coordinate subspace associated with the nonzero support is characterized by
\[
\cos\theta=\frac{a}{\sqrt{1+a^2}},
\]
which is exactly the factor above.

## Verification
The accompanying checker evaluates the original projector--reflector--shrinkage iteration directly, with no use of the closed-form recurrence in the update routine. It tests several rational parameter choices satisfying \(\gamma\ge b/(1-a)\), verifies the exact first-entry index, checks that the correct sign/support cell is never left afterward, reconstructs the fixed point, and confirms the exact constant ratio of successive Euclidean errors to floating-point tolerance. These computations support the algebraic proof; they do not replace the continuum argument.

## Relationship to prior work
Demanet and Zhang prove eventual linear convergence of Douglas--Rachford for basis pursuit and identify the eventual rate through a principal angle. Their paper explicitly states that it makes no attempt to characterize the transient regime before linear convergence. It also notes that the time to enter the linear regime can vary substantially. The result above gives an exact transient length on the smallest nontrivial basis-pursuit family and shows that the threshold parameter can make that transient arbitrarily long while leaving the eventual principal-angle rate unchanged.

Liang, Fadili, Peyre, and Luke subsequently prove finite activity identification for Douglas--Rachford under partial smoothness and a nondegeneracy condition, followed by local linear convergence. Their theorem is qualitative in the identification time. The present two-variable calculation is consistent with that theory but supplies a closed exact onset index, an invariant-cell proof, and an exact post-identification norm law for this family.

## Limitations
The large-threshold condition \(\gamma\ge b/(1-a)\) is sufficient for the simple invariant-ball proof and is not asserted to be sharp. Smaller thresholds can also identify the correct support permanently, but the exact parameter partition is not classified here. The zero initialization is essential to the simple pre-entry arithmetic progression. This result concerns the auxiliary Douglas--Rachford fixed-point iterate \(y^k\); shadow iterates inherit convergence but are not claimed to obey the same exact norm identity. A later or differently phrased analysis could contain this exact two-variable delay law; the targeted literature and published-finding searches described in the review did not locate one.

## References
1. L. Demanet and X. Zhang, *Eventual linear convergence of the Douglas Rachford iteration for basis pursuit*, arXiv:1301.0542, first submitted 2013-01-03; Mathematics of Computation 85 (2016), 209--238, DOI 10.1090/mcom/2965.
2. J. Liang, J. Fadili, G. Peyre, and R. Luke, *Activity Identification and Local Linear Convergence of Douglas--Rachford/ADMM under Partial Smoothness*, arXiv:1412.6858, first submitted 2014-12-22.
