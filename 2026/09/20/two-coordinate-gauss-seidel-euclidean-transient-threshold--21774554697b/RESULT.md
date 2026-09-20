# Sharp minimax Euclidean transient bound for two-coordinate Gauss-Seidel ordering

**Same-model review: passed. Independent audit: not yet performed.**

## Result

Consider a real symmetric positive-definite matrix
\[
A=\begin{pmatrix}a&c\\c&d\end{pmatrix},\qquad a>0,\ d>0,\ ad-c^2>0,
\]
and the linear system \(Ax=b\). Equivalently, apply exact cyclic coordinate descent to the strictly convex quadratic
\[
f(x)=\tfrac12 x^T A x-b^T x.
\]
Let \(T_{12}\) and \(T_{21}\) denote the one-sweep error matrices for the two coordinate orders. Define
\[
q:=\frac{c^2}{ad}\in[0,1).
\]
Then
\[
T_{12}=\begin{pmatrix}0&-c/a\\0&q\end{pmatrix},\qquad
T_{21}=\begin{pmatrix}q&0\\-c/d&0\end{pmatrix},
\]
and hence
\[
\|T_{12}\|_2^2=q^2+\frac{c^2}{a^2},\qquad
\|T_{21}\|_2^2=q^2+\frac{c^2}{d^2}.
\]
Consequently, among the two orders, the one that updates the coordinate with the **larger diagonal entry first** minimizes the worst-case Euclidean error amplification over the first sweep. In matrix form,
\[
\min\{\|T_{12}\|_2,\|T_{21}\|_2\}
=\sqrt{q^2+\frac{c^2}{\max(a,d)^2}}.
\]

Now let the eigenvalues of \(A\) be \(0<\lambda\le \Lambda\), let \(\kappa=\Lambda/\lambda\), and set
\[
\delta:=\frac{\Lambda-\lambda}{\Lambda+\lambda}
=\frac{\kappa-1}{\kappa+1}.
\]
The exact minimax best-order amplification over all two-dimensional SPD matrices with condition number \(\kappa\) is
\[
\boxed{
\sup_{\kappa_2(A)=\kappa}\ \min_{\pi\in\{12,21\}}\|T_\pi(A)\|_2
=\delta\sqrt{1+\delta^2}.
}
\]
Equality is attained by the balanced-diagonal matrices
\[
A_*=\begin{pmatrix}
(\Lambda+\lambda)/2 & \pm(\Lambda-\lambda)/2\\
\pm(\Lambda-\lambda)/2 & (\Lambda+\lambda)/2
\end{pmatrix},
\]
for which the two orderings have the same Euclidean norm.

It follows that a suitable choice between the two coordinate orders is guaranteed to make the first sweep Euclidean-nonexpansive for **every** two-dimensional SPD matrix of condition number \(\kappa\) if and only if
\[
\boxed{
\kappa\le \kappa_*:=\frac{1+\sqrt{(\sqrt5-1)/2}}{1-\sqrt{(\sqrt5-1)/2}}
\approx 8.352410032042775.
}
\]
Equivalently, \(\kappa_*\) is the unique real root greater than one of
\[
\kappa^4-8\kappa^3-2\kappa^2-8\kappa+1=0.
\]
For every \(\kappa>\kappa_*\), the balanced matrix \(A_*\) makes **both** coordinate orders expand some Euclidean error vector during the first sweep.

The best-order worst-case factor is nevertheless uniformly bounded:
\[
\delta\sqrt{1+\delta^2}<\sqrt2,
\]
with sharp limit \(\sqrt2\) as \(\kappa\to\infty\).

## Order changes the transient, not the two-dimensional asymptotic factor

The two orderings have the same eigenvalues \(\{0,q\}\), so their spectral radii are identical:
\[
\rho(T_{12})=\rho(T_{21})=q.
\]
More strongly,
\[
T_{12}^2=qT_{12},\qquad T_{21}^2=qT_{21}.
\]
Thus, after a nonzero first-sweep error, every later sweep with that fixed order multiplies the Euclidean error norm by exactly \(q\). The ordering effect in two dimensions is therefore entirely a startup transient in the Euclidean norm even though classical asymptotic spectral convergence is unchanged.

At fixed condition number,
\[
q\le \delta^2,
\]
with equality for the same balanced-diagonal extremizer. Hence the method is asymptotically convergent for every SPD matrix while its first sweep can still have \(\|T_\pi\|_2>1\), a direct nonnormal-transient effect.

## Proof

### 1. Exact sweep matrices and the optimal order

Let \(e=x-x_*\) be the error. In order \(1\to2\), exact minimization in coordinate 1 gives
\[
e_1^+=-\frac ca e_2,
\]
and then exact minimization in coordinate 2 gives
\[
e_2^+=-\frac cd e_1^+=\frac{c^2}{ad}e_2=qe_2.
\]
This yields the displayed \(T_{12}\). Reversing the order yields \(T_{21}\).

Each matrix has only one nonzero column, so its spectral norm is the Euclidean norm of that column, giving
\[
\|T_{12}\|_2^2=q^2+c^2/a^2,\qquad
\|T_{21}\|_2^2=q^2+c^2/d^2.
\]
The common term \(q^2\) cancels in the comparison. Therefore \(1\to2\) is no worse exactly when \(a\ge d\), proving that the larger diagonal should be updated first.

### 2. Sharp condition-number envelope

For a real symmetric \(2\times2\) matrix with eigenvalues \(\lambda\le\Lambda\),
\[
a+d=\Lambda+\lambda,
\qquad
ad-c^2=\Lambda\lambda.
\]
Writing \(A=Q\operatorname{diag}(\lambda,\Lambda)Q^T\) also gives
\[
|c|\le\frac{\Lambda-\lambda}{2}.
\]
Since \(\max(a,d)\ge(a+d)/2\),
\[
\frac{|c|}{\max(a,d)}
\le\frac{\Lambda-\lambda}{\Lambda+\lambda}=\delta.
\]
Moreover,
\[
q=\frac{c^2}{ad}
=\frac{c^2}{\Lambda\lambda+c^2}.
\]
The right-hand side is increasing in \(c^2\), so using \(|c|\le(\Lambda-\lambda)/2\),
\[
q\le
\frac{(\Lambda-\lambda)^2}{4\Lambda\lambda+(\Lambda-\lambda)^2}
=\frac{(\Lambda-\lambda)^2}{(\Lambda+\lambda)^2}
=\delta^2.
\]
Therefore
\[
\min_\pi\|T_\pi\|_2^2
=q^2+\frac{c^2}{\max(a,d)^2}
\le\delta^4+\delta^2.
\]
Both inequalities become equalities simultaneously when \(a=d=(\Lambda+\lambda)/2\) and \(|c|=(\Lambda-\lambda)/2\). This proves the minimax identity and its sharpness.

### 3. Sharp nonexpansion threshold

Uniform best-order nonexpansion is equivalent to
\[
\delta^2+\delta^4\le1.
\]
With \(y=\delta^2\), this is \(y^2+y-1\le0\), hence
\[
y\le\frac{\sqrt5-1}{2}.
\]
Substitution of \(\delta=(\kappa-1)/(\kappa+1)\) gives the stated \(\kappa_*\). The quartic follows by elimination of the square roots. Since the balanced matrix attains the envelope, the threshold is necessary as well as sufficient.

### 4. Exact post-transient behavior

Direct multiplication gives \(T_\pi^2=qT_\pi\). Thus the range of either nonzero sweep matrix is its \(q\)-eigenspace. After the first sweep, every nonzero error lies on that eigenline, and each subsequent sweep scales it by \(q\). This also explains why the two orderings can have different one-sweep singular norms even though they have the same asymptotic factor.

## Examples

A condition-number-six example shows that ordering alone can reverse first-sweep expansion:
\[
A=\begin{pmatrix}2&2\\2&5\end{pmatrix},\qquad \kappa_2(A)=6.
\]
Updating the smaller diagonal first gives
\[
\|T_{12}\|_2\approx1.077032961>1,
\]
whereas updating the larger diagonal first gives
\[
\|T_{21}\|_2\approx0.565685425.
\]

A stronger separation is possible as \(\kappa\) grows. For \(\kappa\ge3\), let
\[
A_\kappa=\begin{pmatrix}
2&\sqrt{\kappa-2}\\
\sqrt{\kappa-2}&\kappa-1
\end{pmatrix}.
\]
Its eigenvalues are exactly \(1\) and \(\kappa\). If the smaller diagonal is updated first,
\[
\|T_{12}\|_2^2
=\frac{\kappa-2}{4}
+\left(\frac{\kappa-2}{2(\kappa-1)}\right)^2
\sim\frac\kappa4,
\]
so the first-sweep amplification is unbounded. Reversing the order instead gives a norm tending to \(1/2\). Thus a static diagonal-aware ordering eliminates an arbitrarily large two-coordinate Euclidean transient on this family, even though neither order changes the spectral radius.

## Computational model and scope

The result concerns exact cyclic coordinate minimization for a two-variable real SPD quadratic, equivalently exact point Gauss-Seidel on a two-by-two SPD linear system. The error is measured in the ordinary Euclidean norm and one sweep means two exact scalar updates. The only permitted ordering decision is the choice between the two coordinate permutations; the theorem is a worst-case statement over matrices with prescribed spectral condition number.

## Relation to prior literature

Ordering effects in SOR/Gauss-Seidel are classical. Varga (1959) studied how orderings affect convergence rates through spectral properties. Modern work studies random or favorable reorderings for SOR/Gauss-Seidel and cyclic coordinate descent, including Oswald--Zhou (2017), Lee--Wright (2019), and Zhou (2022). Wright (2015) surveys cyclic coordinate descent and its convergence theory. Mohlenkamp--Young--Barany (2020) studies transient block-coordinate dynamics in narrow valleys and explicitly notes that early block ordering can matter.

The statement here is different in target quantity and regime: it gives an exact two-dimensional **Euclidean one-sweep operator-norm minimax**, a closed-form best static order, a sharp condition-number threshold for avoidable versus unavoidable startup expansion, and the identity showing that ordering changes only the startup transient in two dimensions. The literature checks described in `REVIEW.md` did not locate these formulas or this threshold.

## Limitations

- The theorem is two-dimensional; no claim is made that sorting coordinates by diagonal entries is optimal in dimensions three or higher.
- The norm is the Euclidean error norm. For SPD Gauss-Seidel, energy-norm descent is a different and more classical statement.
- The nonexpansion threshold is uniform over all two-dimensional SPD matrices of a fixed condition number; individual matrices can be nonexpansive well above the threshold.
- Exact arithmetic and exact coordinate minimization are assumed. No floating-point stability or finite-precision residual claim is made.
- No implementation-speed advantage is claimed; the ordering rule only concerns one-sweep Euclidean error amplification.
- Historical monographs and some older ordering literature could contain an equivalent elementary two-dimensional calculation that was not discoverable in the inspected theorem-level material; originality is therefore stated only to the best of our knowledge.

## Reproducibility

`artifacts/verify_gs_2d_ordering.py` deterministically checks the sweep-matrix formulas, the identity \(T^2=qT\), the sharp condition-number envelope on a dense rotation grid, the exact threshold, the condition-number-six ordering example, and the unbounded bad-order family. Its recorded output is in `artifacts/verification.txt`.

## References

1. R. S. Varga, “Orderings of the Successive Overrelaxation Scheme,” *Pacific Journal of Mathematics* 9 (1959), 925–939. https://doi.org/10.2140/pjm.1959.9.925
2. S. J. Wright, “Coordinate Descent Algorithms,” *Mathematical Programming* 151 (2015), 3–34. https://doi.org/10.1007/s10107-015-0892-3
3. P. Oswald and W. Zhou, “Random reordering in SOR-type methods,” *Numerische Mathematik* 135 (2017), 1209–1220. https://doi.org/10.1007/s00211-016-0829-7
4. P. Oswald and W. Zhou, “Correction to: Random reordering in SOR-type methods,” *Numerische Mathematik* 154 (2023), 407–410. https://doi.org/10.1007/s00211-023-01365-9
5. C.-p. Lee and S. J. Wright, “Random permutations fix a worst case for cyclic coordinate descent,” *IMA Journal of Numerical Analysis* 39 (2019), 1246–1275. https://doi.org/10.1093/imanum/dry040
6. M. J. Mohlenkamp, T. R. Young, and B. Barany, “Transient Dynamics of Block Coordinate Descent in a Valley,” *International Journal of Numerical Analysis and Modeling* 17 (2020), 557–591. https://www.math.ualberta.ca/ijnam/Volume-17-2020/No-4-20/2020-04-06.pdf
7. W. Zhou, “Properties and applications of a conjugate transform on Schatten classes,” *Journal of Inequalities and Applications* 2022, 164. https://doi.org/10.1186/s13660-022-02863-4
