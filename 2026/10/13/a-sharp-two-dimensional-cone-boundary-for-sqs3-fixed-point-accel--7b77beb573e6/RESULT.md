# A sharp two-dimensional cone boundary for SqS3 fixed-point acceleration
## Finding
Consider the affine fixed-point problem \(F(x)=Jx\) on \(\mathbb R^2\), where \(J\) is symmetric, strictly entrywise positive, and \(\rho(J)<1\). Define \(A=I-J\). Then \(A\) is positive definite with nonpositive off-diagonal entries. For a negative squared-iteration steplength \(\alpha=-s\), \(s>0\), the raw SqS3 extrapolation stage is
\[
y=(I-sA)^2x.
\]
If
\[
A=\begin{pmatrix}a&-c\\-c&d\end{pmatrix},\qquad c>0,
\]
then this raw stage maps the whole nonnegative orthant into itself **if and only if**
\[
s\le \frac{2}{a+d}=\frac{2}{\operatorname{tr}A}.
\]

For the adaptive SqS3 magnitude
\[
s(x)=\frac{\|Ax\|_2}{\|A^2x\|_2},
\]
the positivity obstruction is generic in two dimensions. If the non-Perron eigenvalue of \(J\) is nonzero, there are strictly positive starts arbitrarily close to the positive Perron eigenvector for which the raw squared stage has mixed signs; after the standard final fixed-point update \(F\), the completed SqS3 cycle still has mixed signs.

An exact witness is
\[
J=\begin{pmatrix}1/2&1/4\\1/4&1/2\end{pmatrix},\qquad
x=\begin{pmatrix}11/10\\9/10\end{pmatrix}.
\]
Here every ordinary Picard iterate is strictly positive, because \(J\) is strictly positive, while SqS3 gives
\[
s=\frac{4\sqrt{19729}}{181}>2
\]
and, after the squared stage and the standard final application of \(F\),
\[
F(y)=\begin{pmatrix}
(4931-33\sqrt{19729})/3620\\
(3769-27\sqrt{19729})/3620
\end{pmatrix},
\]
whose second coordinate is negative.

## Assumptions and scope
The result concerns exact arithmetic and the unsafeguarded SqS3 scheme with steplength \(\alpha=-\|r\|_2/\|v\|_2\), where \(r=F(x)-x\) and \(v=F(F(x))-2F(x)+x\). For an affine map with fixed point at the origin, \(r=-Ax\) and \(v=A^2x\), so \(s=-\alpha=\|Ax\|_2/\|A^2x\|_2\). The final fixed-point update is the one used in the published SqS3 pseudocode. The theorem does not claim that globalization, projection, parameter clipping, or a problem-specific feasibility safeguard fails.

The generic statement assumes that the second eigenvalue of \(J\) is nonzero. The rank-one case, where that eigenvalue vanishes, is excluded because the final application of \(J\) annihilates the leading sign-changing mode.

## Proof
For fixed \(s>0\),
\[
I-sA=\begin{pmatrix}1-sa&sc\\sc&1-sd\end{pmatrix}.
\]
Squaring gives diagonal entries \((1-sa)^2+s^2c^2\) and \((1-sd)^2+s^2c^2\), both nonnegative, and common off-diagonal entry
\[
sc\bigl(2-s(a+d)\bigr).
\]
Since \(s>0\) and \(c>0\), every entry of \((I-sA)^2\) is nonnegative exactly when \(2-s(a+d)\ge0\), proving the sharp fixed-step criterion.

For the adaptive claim, let \(\lambda_1\) be the Perron eigenvalue of \(J\), let \(\lambda_2\ne0\) be its other eigenvalue, and choose orthonormal eigenvectors \(p,q\) with \(p>0\). Set
\[
\mu=1-\lambda_1,\qquad L=1-\lambda_2.
\]
Then \(0<\mu<L\), \(Ap=\mu p\), and \(Aq=Lq\). For sufficiently small nonzero \(\delta\), the vector \(x_\delta=p+\delta q\) is strictly positive. Its SqS3 magnitude is
\[
s_\delta=\sqrt{\frac{\mu^2+\delta^2L^2}{\mu^4+\delta^2L^4}}
\longrightarrow \frac1\mu.
\]
Therefore
\[
\frac{(I-s_\delta A)^2x_\delta}{\delta}
\longrightarrow
\left(1-\frac L\mu\right)^2q.
\]
Applying the final fixed-point map yields
\[
\frac{J(I-s_\delta A)^2x_\delta}{\delta}
\longrightarrow
\lambda_2\left(1-\frac L\mu\right)^2q.
\]
Because \(q\) has one positive and one negative coordinate and \(\lambda_2\ne0\), the completed SqS3 cycle has mixed signs for all sufficiently small \(\delta\) of either fixed sign. This proves that such starts occur arbitrarily close to the Perron ray.

For the displayed witness, direct exact arithmetic gives
\[
r=\begin{pmatrix}-13/40\\-7/40\end{pmatrix},\qquad
v=\begin{pmatrix}19/160\\1/160\end{pmatrix},
\]
so
\[
s^2=\frac{\|r\|_2^2}{\|v\|_2^2}=\frac{1744}{181},
\qquad
s=\frac{4\sqrt{19729}}{181}.
\]
The raw squared stage equals
\[
y=\begin{pmatrix}
(2031-13\sqrt{19729})/905\\
(869-7\sqrt{19729})/905
\end{pmatrix},
\]
and the final \(J\)-update is the vector stated above. The exact inequality \(27^2\cdot19729=14382441>14205361=3769^2\) proves that its second coordinate is negative.

## Verification
The accompanying `verify.py` uses only Python's standard library. It reconstructs the exact witness in the quadratic field \(\mathbb Q(\sqrt{19729})\), checks the SqS3 norm ratio, recomputes the raw and completed updates, verifies the exact radical formulas, and proves the negative signs by integer comparisons. The universal two-dimensional threshold and the Perron-ray argument are analytic and do not rely on finite sampling.

## Relationship to prior work
Varadhan and Roland introduce the SqS3 steplength \(\alpha=-\|r\|_2/\|v\|_2\), derive the squared error mechanism, and give globalization by modifying the steplength when needed. Their numerical experiments also report occasional violations of parameter constraints. The present finding does **not** claim that feasibility loss by SQUAREM was previously unknown. Its content is the exact two-dimensional cone-preservation boundary \(s\le2/\operatorname{tr}(I-J)\) and the generic proof that the published adaptive SqS3 rule can cross the positive cone on strictly positive symmetric contractions arbitrarily close to the Perron ray.

The earlier squared-polynomial paper develops the squaring device for fixed-point extrapolation and places the method in numerical nonlinear-equation solving; it does not state the SqS3 steplength or this cone theorem. Database and literature searches for SqS3 positivity, positive-cone invariance, affine contractions, and the Cauchy--Barzilai--Borwein connection did not locate an implication-equivalent statement.

## Limitations
The theorem is two-dimensional and symmetric. It does not classify nonsymmetric positive contractions or dimensions above two. It concerns unsafeguarded SqS3; a feasibility projection, clipping rule, or objective-based backtracking may prevent the displayed failure. The exact fixed-step criterion applies to the raw squared stage; the generic adaptive result separately accounts for the standard final fixed-point update. A residual originality risk is that older vector-extrapolation literature may encode an equivalent cone result under different terminology.

## References
1. R. Varadhan and C. Roland, “Simple and Globally Convergent Methods for Accelerating the Convergence of Any EM Algorithm,” *Scandinavian Journal of Statistics* 35 (2008), 335–353. DOI: 10.1111/j.1467-9469.2007.00585.x. First published 27 February 2008.
2. C. Roland, R. Varadhan, and C. E. Frangakis, “Squared polynomial extrapolation methods with cycling: an application to the positron emission tomography problem,” *Numerical Algorithms* 44 (2007), 159–172. DOI: 10.1007/s11075-007-9094-2. Published online 1 June 2007.
3. R. Varadhan and C. Roland, “Squared Extrapolation Methods (SQUAREM): A New Class of Simple and Efficient Numerical Schemes for Accelerating the Convergence of the EM Algorithm,” Johns Hopkins University Biostatistics Working Paper 63 (November 2004).
