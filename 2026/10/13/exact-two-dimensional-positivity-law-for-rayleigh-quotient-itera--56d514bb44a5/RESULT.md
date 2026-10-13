# Exact two-dimensional positivity law for Rayleigh quotient iteration on Stieltjes matrices
## Finding
Let \(A=\begin{pmatrix}a&-c\\-c&d\end{pmatrix}\) be an irreducible real symmetric positive-definite Stieltjes matrix, so \(c>0\) and \(ad>c^2\). Let \(v_1=(\cos\theta,\sin\theta)^{\mathsf T}>0\) be a unit eigenvector for the smallest eigenvalue, choose \(v_2=(-\sin\theta,\cos\theta)^{\mathsf T}\), and write each positive starting ray uniquely as \(x\sim v_1+t v_2\), where \(-\tan\theta<t<\cot\theta\). For exact Rayleigh quotient iteration, whenever the start is not already an eigenvector, the projective coordinate after one step is exactly \(t_+=-t^3\). Hence the first RQI direction can be globally oriented componentwise positive exactly for
\[
 t\in(-\tan\theta,\cot\theta)\cap\bigl(-\sqrt[3]{\cot\theta},\sqrt[3]{\tan\theta}\bigr).
\]
Consequently every positive starting vector has a positive first RQI direction if and only if \(a=d\). In that equal-diagonal case \(\theta=\pi/4\), the whole positive cone corresponds to \(|t|<1\), is invariant under \(t\mapsto -t^3\), and every positive start converges cubically to the positive smallest-eigenvalue eigenvector while remaining positive up to the unavoidable global sign choice of eigenvectors. If \(a\ne d\), there are positive starts already in the attraction basin \(|t|<1\) of the positive smallest eigenvector whose first RQI direction has mixed signs. A rational witness is \(A=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}\), \(x=(1,4)^{\mathsf T}\). Its Rayleigh quotient is \(25/17<\operatorname{tr}(A)/2=3/2\), so the start lies in the smallest-eigenvector basin, but solving \((A-(25/17)I)y=x\) gives \(y=(-1309/361,255/361)^{\mathsf T}\), which has mixed signs and cannot be made positive by a global sign change.

## Assumptions and scope
The matrix is restricted to the irreducible \(2\times2\) symmetric positive-definite Stieltjes class
\[
A=\begin{pmatrix}a&-c\\-c&d\end{pmatrix},\qquad c>0,\qquad ad>c^2.
\]
RQI is taken in exact arithmetic. From a nonzero vector \(x_k\), form \(\mu_k=x_k^{\mathsf T}Ax_k/(x_k^{\mathsf T}x_k)\), solve \((A-\mu_k I)y_{k+1}=x_k\) when nonsingular, and normalize. Since eigenvectors are defined up to sign, a computed ray is called positive when one of its two representatives is componentwise positive. If the current vector is already an eigenvector, RQI terminates there.

## Proof
Let \(\lambda_1<\lambda_2\), take
\[
v_1=(\cos\theta,\sin\theta)^{\mathsf T}>0,\qquad v_2=(-\sin\theta,\cos\theta)^{\mathsf T},\qquad 0<\theta<\pi/2.
\]
Every positive ray has a unique form \(x\sim v_1+t v_2\) with
\[
-\tan\theta<t<\cot\theta.
\]
For \(t\ne0\),
\[
\mu(t)=\frac{\lambda_1+\lambda_2t^2}{1+t^2},
\qquad
y\sim \frac{1}{\lambda_1-\mu(t)}v_1+\frac{t}{\lambda_2-\mu(t)}v_2.
\]
Thus the new projective coordinate is
\[
t_+=t\frac{\lambda_1-\mu(t)}{\lambda_2-\mu(t)}=-t^3.
\]
The next ray is positive exactly when \(-\tan\theta<-t^3<\cot\theta\), namely when
\[
-\sqrt[3]{\cot\theta}<t<\sqrt[3]{\tan\theta}.
\]
Intersecting with the starting positive interval gives the exact safe-start set.

For every positive start to be safe, the endpoint images must satisfy
\[
\cot^3\theta\le\tan\theta,\qquad \tan^3\theta\le\cot\theta.
\]
These are equivalent to \(\theta=\pi/4\). For \(A=\begin{pmatrix}a&-c\\-c&d\end{pmatrix}\) with \(c>0\), the vector \((1,1)^{\mathsf T}\) is an eigenvector exactly when \(a=d\), proving the iff statement. In the equal-diagonal case the positive cone is \(|t|<1\), so \(|t_{k+1}|=|t_k|^3<1\) and \(|t_k|=|t_0|^{3^k}\to0\).

If \(a\ne d\), then \(\theta\ne\pi/4\). If \(\theta<\pi/4\), every \(t\) with \(\sqrt[3]{\tan\theta}<t<1\) starts positive and lies in the smallest-eigenvector basin \(|t|<1\), but maps outside the positive interval in one step. The case \(\theta>\pi/4\) is symmetric, using \(-1<t<-\sqrt[3]{\cot\theta}\). Hence unequal diagonals admit transient sign loss even from the correct attraction basin.

## Verification
For \(A=\begin{pmatrix}1&-1\\-1&2\end{pmatrix}\), \(x=(1,4)^{\mathsf T}\), the leading principal minors are \(1\) and \(1\). Exact arithmetic gives
\[
\mu=\frac{25}{17}<\frac32=\frac{\lambda_1+\lambda_2}{2},
\]
so \(|t|<1\) and the start belongs to the smallest-eigenvector basin. The shifted determinant is \(-361/289\), and exact elimination gives
\[
y=\begin{pmatrix}-1309/361\\255/361\end{pmatrix},
\]
which has mixed signs. The bundled `verify.py` reproduces these rational identities and returns `VERIFY_OK`.

## Relationship to prior work
Parlett's classical RQI paper gives the symmetric iteration and its cubic local behavior and records primary classification 65F15. The two-eigenvalue cubic map is standard RQI dynamics. Jia, Lin, and Liu emphasize that positivity of Perron or smallest-\(M\)-matrix eigenvector approximations can be essential and that ordinary RQI does not guarantee it, motivating positivity-preserving Noda-type methods. The present claim is narrower and sharper: the exact \(2\times2\) Stieltjes safe-start interval, the equal-diagonal iff criterion for universal cone invariance, and sign loss from inside the positive target basin.

## Limitations
The theorem is exact only for irreducible \(2\times2\) symmetric positive-definite Stieltjes matrices in exact arithmetic. It does not classify higher dimensions, nonsymmetric \(M\)-matrices, inexact inner solves, or floating-point sign perturbations. The projective map \(t_+=-t^3\) is prior structure; the literature search supports, but cannot prove, absence of the cone classification under other terminology.

## References
1. B. N. Parlett, “The Rayleigh Quotient Iteration and Some Generalizations for Nonnormal Matrices,” *Mathematics of Computation* 28 (127), 679–693 (1974). DOI: 10.1090/S0025-5718-1974-0405823-3. Bibliographic issue date: 1974-07-01. Primary classification: 65F15.
2. Z. Jia, W.-W. Lin, and C.-S. Liu, “A positivity preserving inexact Noda iteration for computing the smallest eigenpair of a large irreducible M-matrix,” arXiv:1309.3926, first submitted 2013-09-16; later *Numerische Mathematik* 130 (2015), 645–679. DOI: 10.1007/s00211-014-0677-2.
