# A sharp reciprocal critical-point diameter bound for collinear zeros

## Result

Let \(p\) be a complex polynomial of degree \(N\ge 2\) whose zeros are collinear, and let
\[
D=\max\{|z-z'|:p(z)=p(z')=0\}>0
\]
be the diameter of its zero multiset. Fix a zero \(a\) of \(p\), and let
\(\zeta_1,\ldots,\zeta_{N-1}\) be the critical points of \(p\), counted with multiplicity.

With the convention \(0^{-\lambda}=+\infty\), for every \(\lambda\ge 1\),
\[
\boxed{\quad
\sum_{k=1}^{N-1}\frac{1}{|a-\zeta_k|^\lambda}
\ge (N-1)\left(\frac{2}{D}\right)^\lambda .
\quad}
\]

For \(\lambda=1\), equality holds if and only if \(a\) is a simple endpoint of the zero segment and every other zero is the opposite endpoint. Equivalently, after an affine isometry of the line of zeros,
\[
p(z)=c\,(z-A)(z-B)^{N-1},\qquad a=A,
\]
or the reflected configuration, with \(A\ne B\).

For every \(\lambda>1\), equality occurs if and only if \(N=2\).

This gives the full Tang--Zhang reciprocal-distance conjecture for the collinear-zero class. Indeed, the conjecture asks, in its normalized unit-disk form, for
\(\sum |w_k|^{-\lambda}\ge n\) for every \(\lambda\ge1\). Any collinear set of zeros in the closed unit disk has diameter at most \(2\), and the theorem above therefore gives exactly that lower bound. The endpoint \(\lambda=1\) is the decisive one: by the power-mean inequality it implies every \(\lambda>1\).

## A stronger two-sided estimate

The diameter theorem follows from a more informative inequality.

Translate and rotate so that the distinguished simple zero is \(a=0\) and all other zeros
\(x_1,\ldots,x_m\) are real and nonzero, where \(m=N-1\). Put
\[
r=\#\{j:x_j>0\},\qquad \ell=\#\{j:x_j<0\},
\]
and
\[
R=\sum_{x_j>0}\frac1{x_j},\qquad
L=\sum_{x_j<0}\frac1{-x_j}.
\]
If \(w_1,\ldots,w_m\) are the critical points in these translated coordinates, then
\[
\boxed{\quad
\sum_{k=1}^{m}\frac1{|w_k|}
\ge
\max\left\{
2L+\frac{2R}{\ell+1},
\;
2R+\frac{2L}{r+1}
\right\}.
\quad}
\]
When all other zeros lie on one side of the distinguished zero, this becomes an identity:
\[
\sum_{k=1}^{m}\frac1{|w_k|}=2R
\quad\text{or}\quad
\sum_{k=1}^{m}\frac1{|w_k|}=2L.
\]

## Proof

If \(a\) is a multiple zero, then \(a\) is also a critical point and the asserted reciprocal sum is \(+\infty\). Hence assume \(a\) is simple.

After translation and rotation, write
\[
P(t)=t\prod_{j=1}^{m}(t-x_j),
\qquad x_j\in\mathbb R\setminus\{0\}.
\]
Set
\[
u_j=\frac1{x_j},\qquad
D_0=\operatorname{diag}(u_1,\ldots,u_m),\qquad
C=I_m+J_m,
\]
where \(J_m\) is the all-ones matrix.

### 1. Reciprocal critical points as a real spectrum

Let \(q=1/w\). The matrix determinant lemma gives
\[
\det(qI-D_0C)
=
\prod_{j=1}^{m}(q-u_j)
\left(1-\sum_{j=1}^{m}\frac{u_j}{q-u_j}\right).
\]
A direct expansion of
\[
P'(t)=\prod_{j=1}^{m}(t-x_j)
+t\sum_{i=1}^{m}\prod_{j\ne i}(t-x_j)
\]
shows the polynomial identity
\[
\det(qI-D_0C)
=
(-1)^m q^m\!\left(\prod_{j=1}^{m}u_j\right)P'(1/q).
\]
Since \(P'(0)=\prod_j(-x_j)\ne0\), no critical point is zero. Hence the eigenvalues of
\[
M=D_0C=D_0+D_0J_m
\]
are exactly the reciprocal critical points \(q_k=1/w_k\), with multiplicity. This derivation also covers repeated nonzero zeros without dividing by \(P(w)\). It is the reciprocal \(D\)-companion representation used in the modern polynomial-geometry literature.

Because \(C\) is positive definite,
\[
M\sim H:=C^{1/2}D_0C^{1/2},
\]
and \(H\) is real symmetric. By Sylvester inertia, \(H\) has exactly \(r\) positive and \(\ell\) negative eigenvalues.

Let
\[
P_+=\sum_{q_k>0}q_k,\qquad
P_-=\sum_{q_k<0}(-q_k).
\]
Then
\[
\sum_{k=1}^{m}\frac1{|w_k|}=P_++P_-,
\]
while the trace identity gives
\[
P_+-P_-=\operatorname{tr}H
=\operatorname{tr}(D_0C)
=2(R-L).
\]

### 2. A Ky Fan compression on each sign subspace

Let \(E_+\) denote the coordinate subspace corresponding to the \(r\) positive \(u_j\)'s. Apply the Ky Fan maximum principle to the \(r\) positive eigenvalues of \(H\), using the trial subspace \(C^{-1/2}E_+\).

Since
\[
C^{-1}=I_m-\frac{1}{m+1}J_m,
\]
the Gram matrix on that trial subspace is
\[
G_+=I_r-\frac{1}{m+1}J_r.
\]
As \(m+1-r=\ell+1\),
\[
G_+^{-1}=I_r+\frac{1}{\ell+1}J_r.
\]
Therefore the trace of the compressed operator is
\[
\operatorname{tr}(G_+^{-1}D_+)
=
R+\frac{R}{\ell+1}
=
\frac{\ell+2}{\ell+1}R,
\]
where \(D_+\) is the positive diagonal block of \(D_0\). Hence
\[
P_+\ge \frac{\ell+2}{\ell+1}R.
\]
Applying the same argument to \(-H\) on the negative coordinate subspace gives
\[
P_-\ge \frac{r+2}{r+1}L.
\]

Using \(P_+-P_-=2(R-L)\), we obtain in two ways
\[
P_++P_-
=2P_+-2(R-L)
\ge 2L+\frac{2R}{\ell+1},
\]
and
\[
P_++P_-
=2P_-+2(R-L)
\ge 2R+\frac{2L}{r+1}.
\]
This proves the stronger two-sided estimate.

### 3. From the two-sided estimate to the diameter bound

Let the real zero segment be \([A,B]\), with \(D=B-A\), and let the distinguished zero be \(a\in[A,B]\). Put
\[
x=a-A,\qquad y=B-a,\qquad x+y=D.
\]
If both \(\ell,r>0\), then
\[
L\ge \frac{\ell}{x},\qquad R\ge \frac{r}{y}.
\]
At least one of
\[
x\le \frac{\ell D}{m},\qquad
y\le \frac{rD}{m}
\]
must hold, since the two right-hand sides add to \(D\). In the first case,
\[
2L\ge \frac{2m}{D};
\]
in the second,
\[
2R\ge \frac{2m}{D}.
\]
The additional term in the corresponding two-sided bound is positive, so the inequality is strict whenever zeros occur on both sides of \(a\).

If all other zeros lie to the right of \(a\), then \(\ell=0\), all reciprocal critical points are positive, and the trace identity is exact:
\[
\sum_{k=1}^{m}\frac1{|w_k|}=2R.
\]
Since every \(x_j-a\le D\),
\[
R\ge \frac{m}{D},
\]
with equality if and only if every other zero is exactly distance \(D\) from \(a\). Thus equality at exponent \(1\) occurs precisely when \(a\) is one endpoint and all remaining zeros are the other endpoint. The left-sided case is identical.

Therefore
\[
\sum_{k=1}^{m}\frac1{|w_k|}\ge\frac{2m}{D}.
\]

Finally, for \(\lambda\ge1\), apply the power-mean inequality to
\(s_k=|w_k|^{-1}>0\):
\[
\frac1m\sum_{k=1}^{m}s_k^\lambda
\ge
\left(\frac1m\sum_{k=1}^{m}s_k\right)^\lambda
\ge
\left(\frac2D\right)^\lambda.
\]
This proves the claimed bound for every \(\lambda\ge1\).

For \(\lambda>1\), equality in the power-mean step requires all \(s_k\) to be equal. In the \(\lambda=1\) extremal configuration
\[
P(t)=(t-A)(t-B)^{N-1},
\]
the critical points are \(B\) with multiplicity \(N-2\) and
\[
A+\frac{D}{N}.
\]
Their reciprocal distances from \(A\) are \(1/D\) (with multiplicity \(N-2\)) and \(N/D\). These are all equal only when \(N=2\). This completes the equality classification.

## Relation to prior literature

Tang and Zhang formulated the normalized reciprocal-distance conjecture in 2025: for
\[
P(z)=z\prod_{j=1}^{n}(z-z_j)
\]
with the other zeros in the relevant unit disk, they conjectured
\[
\sum_{k=1}^{n}|w_k|^{-\lambda}\ge n,\qquad \lambda\ge1.
\]
Their same paper proves sharp *upper* bounds for negative-order Schoenberg sums; in particular,
\[
\sum_{k=1}^{n}|w_k|^{-1}\le 2\sum_{j=1}^{n}|z_j|^{-1},
\]
with equality when the nonzero zeros lie on one ray. It also records the reciprocal \(D\)-companion matrix
\(\operatorname{diag}(u)+u\mathbf1^\top\). The present result uses that matrix geometry in the opposite direction: when the \(u_j\) are real with mixed signs, a sign-sensitive Ky Fan compression yields a lower bound.

In September 2026, Zhang proved the quadratic case globally:
\[
\sum_{j=1}^{N-1}|a-\zeta_j|^{-2}\ge N-1
\]
for arbitrary zero configurations in the closed unit disk. The exponent-one case remains the stronger unresolved endpoint in the general complex setting; once exponent one is known, all larger exponents follow by power means. The theorem here resolves that endpoint for every collinear zero configuration and gives a scale-invariant sharp diameter form.

## Limitations

The sign-sensitive compression uses the real ordering after the zeros are put on a line; it does not directly extend to non-collinear configurations. The originality assessment is necessarily to the best of our knowledge. The most relevant modern primary source, Tang--Zhang (2025), was inspected in full and does not state this lower bound. Older matrix/majorization literature provides the companion-matrix and majorization machinery used here, and obscure equivalent formulations may exist. In particular, the full text of Pereira (2003) and the full text of Zhang's 2025 Proc. AMS paper corresponding to arXiv:2411.07105 were not inspected here; their available descriptions concern majorization or one-sided/nonnegative-zero relations and do not establish the mixed-sign diameter lower bound above.

## References

1. Q. Tang and T. Zhang, *Sharp Schoenberg type inequalities and the de Bruin--Sharma problem*, arXiv:2508.10341v3 (2025), especially Conjecture 1.10 and Sections 5--9. https://arxiv.org/abs/2508.10341
2. T. Zhang, *Beyond Sendov's conjecture: the quadratic Tang--Zhang inequality*, arXiv:2609.19126 (2026). https://arxiv.org/abs/2609.19126
3. R. Pereira, *Differentiators and the geometry of polynomials*, J. Math. Anal. Appl. 285 (2003), 336--348. https://doi.org/10.1016/S0022-247X(03)00465-7
4. W.-S. Cheung and T. W. Ng, *A companion matrix approach to the study of zeros and critical points of a polynomial*, J. Math. Anal. Appl. 319 (2006), 690--707. https://doi.org/10.1016/j.jmaa.2005.06.071
5. T. Zhang, *A refinement of Pawlowski's result* / *Sendov conjecture, Borcea variance conjectures and Schoenberg inequalities*, arXiv:2411.07105 (2025). https://arxiv.org/abs/2411.07105
