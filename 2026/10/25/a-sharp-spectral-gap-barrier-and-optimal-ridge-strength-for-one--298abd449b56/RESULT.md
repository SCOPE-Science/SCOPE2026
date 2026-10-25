# A sharp spectral-gap barrier and optimal ridge strength for one-row preconditioning

## Finding

A single *unbiased* isotropic sketch row can help or harm the spectral conditioning of regularized least squares. For the diagonal two-coordinate problem below, strict improvement over the unpreconditioned augmented system is **impossible for every sketch orientation and every positive ridge strength** when the unregularized Gram spectral ratio lies at or below \(3+2\sqrt2\). Above that sharp barrier, improvement has an exact arcsine probability law, turns on at an explicit positive ridge strength, and is most probable at a *unique finite* ridge strength.

Write \(r=a/b>1\), \(\ell=\lambda/b>0\) and \(t=\cos(2\theta)\). Define
\[
P_{r,\ell}(t)=\ell^2\bigl((r-1)^2t^2-(r^2-6r+1)\bigr)
+\ell\bigl(-(r-1)^3t-r^3+5r^2+5r-1\bigr)+4r^2.
\]
Then the exact two-norm condition-number improvement event is \(P_{r,\ell}(\cos2\theta)<0\).

Let \(r_\star=3+2\sqrt2\). If \(1<r\le r_\star\), this event has probability zero for every \(\ell>0\). If \(r>r_\star\), set
\[
\delta=\sqrt{r^2-6r+1},\qquad
L_\pm=\frac{r^2-4r-1\pm(r-1)\delta}{4},\qquad
 t_\pm=\frac{r-1}{2\ell}\pm
\frac{(2\ell+r+1)\delta}{2\ell(r-1)}.
\]
Here \(0<L_-<L_+\). Strict improvement occurs exactly for
\[
 t_-<\cos(2\theta)<t_+.
\]
For a uniform sketch orientation, the exact probability is
\[
p_r(\ell)=
\begin{cases}
0,&0<\ell\le L_-,\\
\frac12-\frac1\pi\arcsin t_-,&L_-<\ell\le L_+,\\
\frac1\pi(\arcsin t_+-\arcsin t_-),&\ell>L_+.
\end{cases}
\]
The arguments of \(\arcsin\) lie in their real domain in their respective cases. The probability increases strictly on \((L_-,L_+)\) and decreases strictly on \((L_+,\infty)\). Its **unique global maximizer** is \(\ell=L_+\), with
\[
\boxed{\;p_{\max}(r)=\frac{1}{\pi}\arccos\!\left(\frac{r-1}{L_+}-1\right).\;}
\]
For example, at \(r=6\) the probability turns on above \(\ell=3/2\), reaches its unique maximum at \(\ell=4\), and the maximal probability is \(\arccos(1/4)/\pi\).

## Assumptions and scope

Fix real \(a>b>0\) and \(\lambda>0\). Consider the invertible least-squares coefficient matrix
\[
A=\operatorname{diag}(\sqrt a,\sqrt b),\qquad
B_\lambda=\begin{pmatrix}A\\ \sqrt\lambda I_2\end{pmatrix},
\]
where the regularization term is explicitly included as two additional rows. Let \(\theta\) be uniform on \([0,2\pi)\) and let the one-row sketch be
\[
X_\theta=\sqrt2\begin{pmatrix}\cos\theta&\sin\theta\end{pmatrix}.
\]
Thus \(\mathbb E[X_\theta^{\mathsf T}X_\theta]=I_2\), although each realized sketch has rank one. Define a real invertible right preconditioner by
\[
R_\lambda^{\mathsf T}R_\lambda
 =A^{\mathsf T}X_\theta^{\mathsf T}X_\theta A+\lambda I_2.
\]
The right-hand side is positive definite, so either its symmetric positive square root or a Cholesky factor may be used. The singular values, and hence the spectral condition number, of \(B_\lambda R_\lambda^{-1}\) are independent of the particular factor. We compare this to \(\kappa_2(B_\lambda)\), not to the unregularized \(\kappa_2(A)\). All statements use exact arithmetic. The strict improvement event deliberately excludes ties.

## Proof

Rescale by \(b\), so the augmented normal matrix and sketch normal matrix become, up to a common positive factor,
\[
G=\operatorname{diag}(r+\ell,1+\ell),\qquad
H=\ell I_2+2zz^{\mathsf T},\qquad
z=\begin{pmatrix}\sqrt r\cos\theta\\ \sin\theta\end{pmatrix}.
\]
Their two-dimensional generalized eigenvalues are positive. Define
\[
d=r+1+(r-1)t,\qquad
N=2\ell^2+\ell(r+1+d)+2r,
\qquad t=\cos(2\theta).
\]
Direct inversion, or the Sherman–Morrison formula, gives
\[
\det H=\ell(\ell+d),\qquad
\operatorname{tr}(H^{-1}G)=\frac{N}{\ell(\ell+d)},\qquad
\det(H^{-1}G)=\frac{(r+\ell)(1+\ell)}{\ell(\ell+d)}.
\]
The squared spectral condition number of \(B_\lambda R_\lambda^{-1}\) is the eigenvalue ratio of \(H^{-1/2}GH^{-1/2}\), the latter sharing its two positive eigenvalues with \(H^{-1}G\). For a positive \(2\times2\) matrix of eigenvalue ratio \(k\ge1\), the identity \(\operatorname{tr}(M)^2/\det(M)=k+2+k^{-1}\) holds and its right side is strictly increasing in \(k>1\). Applying this identity to the preconditioned and unpreconditioned normal matrices, multiplying by positive denominators, and simplifying yields
\[
\kappa_2(B_\lambda R_\lambda^{-1})<\kappa_2(B_\lambda)
\quad\Longleftrightarrow\quad
N^2-\ell(\ell+d)(r+1+2\ell)^2<0
\quad\Longleftrightarrow\quad P_{r,\ell}(t)<0.
\]
This also treats boundary equality exactly.

As a quadratic in \(t\), \(P_{r,\ell}\) has positive leading coefficient \(\ell^2(r-1)^2\), and its discriminant is
\[
\operatorname{disc}_t(P_{r,\ell})
=\ell^2(r-1)^2(2\ell+r+1)^2(r^2-6r+1).
\]
For \(1<r<3+2\sqrt2\) it has no two distinct real roots, while at equality it is a nonnegative perfect square; thus strict improvement is impossible. For larger \(r\), its two roots are exactly \(t_\pm\) printed above, and strict improvement means \(t_-<t<t_+\).

The roots intersect the physically attainable interval \([-1,1]\) as follows. The endpoint evaluations factor as
\[
P_{r,\ell}(1)=2r\{2\ell^2-(r^2-4r-1)\ell+2r\},
\]
\[
P_{r,\ell}(-1)=2\{2r\ell^2+(r^2+4r-1)\ell+2r^2\}>0.
\]
For \(r>r_\star\), the two positive roots in \(\ell\) of the first endpoint expression are \(L_\pm\); their positivity follows from \((r^2-4r-1)^2-(r-1)^2(r^2-6r+1)=16r\) and \(r^2-4r-1>0\). Put \(u=\delta/(r-1)\in(0,1)\) and
\[
c_\pm=\frac{r-1}{2}\pm\frac{(r+1)\delta}{2(r-1)}.
\]
Both are positive because \(c_+>0\) and \(c_+c_-=4r^2/(r-1)^2>0\). Moreover
\[
t_+=u+\frac{c_+}{\ell},\qquad t_-=-u+\frac{c_-}{\ell}.
\]
Consequently both roots decrease strictly in \(\ell\); \(t_-\) crosses \(1\) only at \(L_-\), \(t_+\) crosses \(1\) only at \(L_+\), and \(t_->-1\) always. This proves the complete intersection description with \([-1,1]\).

Uniform \(\theta\) makes \(t=\cos(2\theta)\) arcsine-distributed, with density \(1/(\pi\sqrt{1-t^2})\) for \(-1<t<1\). Integrating over the interval between the roots intersected with \([-1,1]\) gives the three exact probability cases. On \((L_-,L_+)\), \(t_+\ge1\) while \(t_-\) decreases, so the probability increases strictly. On \((L_+,\infty)\), differentiation yields
\[
\pi\ell^2 p_r'(\ell)=
\frac{c_-}{\sqrt{1-t_-^2}}-
\frac{c_+}{\sqrt{1-t_+^2}}.
\]
Both terms are positive; their strict ordering follows from the exact algebraic identity
\[
c_+^2(1-t_-^2)-c_-^2(1-t_+^2)
=\frac{4r\delta((r+1)\ell+2r)}{\ell(r-1)^2}>0.
\]
Thus \(p_r'(\ell)<0\) and the maximizer \(L_+\) is unique. At that parameter \(t_+=1\) and \(t_-=(r-1)/L_+-1\), so the stated \(p_{\max}\) formula follows. The limiting probability for strong regularization is
\[
\lim_{\ell\to\infty}p_r(\ell)=
\frac{2}{\pi}\arcsin\frac{\delta}{r-1},
\]
which is strictly smaller than the probability at the finite maximizer by strict decrease.

## Verification

Run `python3 verify_ridge_sketch.py`, using only the Python standard library. The script tests the exact trace/determinant-versus-polynomial identity for 210 rational parameter triples, evaluates 42 independent rational reconstructions of the two-dimensional normal matrices, and compares angular quadrature against the closed probability law for representative parameter values (including both threshold regimes), totaling 276 checks. The expected terminal line is `VERIFY_OK 276`.

Separate symbolic factorization with rational polynomial arithmetic confirms the displayed discriminant and endpoint factorizations. These checks are finite consistency tests; the preceding algebra and monotonicity arguments provide the proof for all admissible real parameters.

## Relationship to prior work

Meier and Nakatsukasa (2022, arXiv:2203.07329v1) motivate the *partially sketched regularized normal matrix* \((XA)^{\mathsf T}(XA)+\lambda I\), including an undersampled regime. Their regularized subspace-embedding bounds give sufficient conditioning guarantees when a suitable embedding holds; they do not yield an exact one-row condition-number improvement event, an intrinsic Gram-gap barrier, or its optimal regularization strength.

Avron, Clarkson and Woodruff (2016/2017, arXiv:1611.03220) study sketching and preconditioning for kernel ridge regression with sufficiently informative sketches and high-probability spectral approximation, not this exact rank-one two-coordinate probability law. Meier and Nakatsukasa and coauthors (2023, arXiv:2302.07202) study numerical stability of sketch-and-precondition least squares in regimes distinct from the exact-arithmetic rank-deficient ridge-sketch comparison here.

These differences are distinctions in the hypotheses and implications, not a proof of global uniqueness. Unindexed or inaccessible equivalent literature remains possible.

## Limitations

This is an exactly solvable two-column positive diagonal model with one *unbiased isotropic row*, positive ridge penalty, and an exact regularized right preconditioner. The statement does not assert the threshold for higher-dimensional matrices, non-isotropic or multirow sketches, unregularized rank-deficient factors, general optimization performance, finite precision, or the actual number of iterations of a Krylov solver. The criterion compares only spectral condition numbers for the *same* regularized augmented problem; improving that metric is not sufficient to guarantee wall-clock benefit.

## References

1. M. Meier and Y. Nakatsukasa, *Randomized Algorithms for Tikhonov Regularization in Linear Least Squares*, arXiv:2203.07329v1 (public 2022-03-14). https://arxiv.org/abs/2203.07329 ; full text https://arxiv.org/html/2203.07329
2. H. Avron, K. L. Clarkson and D. P. Woodruff, *Faster Kernel Ridge Regression Using Sketching and Preconditioning*, arXiv:1611.03220. https://arxiv.org/abs/1611.03220
3. M. Meier and collaborators, *Are Sketch-and-Precondition Least Squares Solvers Numerically Stable?*, arXiv:2302.07202. https://arxiv.org/abs/2302.07202
