# Coherence activates mean-square acceleration in two-row randomized Kaczmarz momentum

## Finding

For the geometrically smoothed momentum randomized Kaczmarz update of Alderman, Luikart, and Marshall, specialize to no geometric smoothing and independent uniform sampling of two linearly independent unit rows in \(\mathbb R^2\). If the row overlap is \(c=|\langle u_1,u_2\rangle|\in[0,1)\), the zero-momentum squared-error asymptotic factor is \(L(c)=(1+c^2)/2\). Let \(\rho(c,M)\) be the spectral radius of the exact second-moment update operator at momentum \(M\in[0,1]\).

For every fixed \(0<c<1\), the right derivative exists and is strictly negative:
\[
\left.\frac{\partial\rho(c,M)}{\partial M}\right|_{M=0+}
=-\frac{2c^2(1-c^2)}{(1+c^2)^2}<0.
\]
For sufficiently small \(M\ge0\), the factor \(\rho(c,M)\) is exactly the limiting root rate of \(\mathbb E\|x_k-x_\star\|_2^2\) for **every deterministic non-solution initial iterate** and zero initial velocity. Hence every nonorthogonal two-row system has a nonempty interval of momenta that genuinely accelerate mean-square convergence.

This is contrasted with exactly orthogonal rows: \(\rho(0,M)>1/2\) for every \(M>0\), so unsmoothed momentum strictly worsens, rather than improves, the mean-square factor in the orthonormal case. This boundary is consistent with the previously established orthonormal stability classification.

The onset of acceleration admits a sharp optimality law. For some \(c_0>0\) and every \(0<c<c_0\), there is a **unique global minimizer** of \(M\mapsto\rho(c,M)\) on \([0,1]\), and
\[
M_{\mathrm{opt}}(c)=c^2+O(c^4),\qquad
\min_{0\le M\le1}\rho(c,M)=\frac{1+c^2}{2}-c^4+O(c^6)
\quad(c\downarrow0).
\]
Thus the best weak-coherence momentum is quadratic in row overlap, while the improvement in squared-error contraction is fourth order.

## Assumptions and scope

Let \(u_1,u_2\in\mathbb R^2\) be linearly independent unit row vectors with \(c=|u_1^{\mathsf T}u_2|<1\), and let \(u_i^{\mathsf T}x=b_i\) be a consistent pair of equations with unique solution \(x_\star\). At each step select \(i_k\in\{1,2\}\) independently and uniformly. Let \(e_k=x_k-x_\star\), \(y_0=0\), and apply the unsmoothed instance \(\beta=0\) of the source update:
\[
e_{k+1}=Q_{i_k}e_k+My_k,\quad
y_{k+1}=e_{k+1}-e_k,\quad
Q_i=I_2-u_i u_i^{\mathsf T},\quad0\le M\le1.
\]
All expectations are over the independent row choices, in exact arithmetic. A squared-error root rate refers to \(\lim_{k\to\infty}(\mathbb E\|e_k\|_2^2)^{1/k}\), not to the root rate of the expected signed error, nor to a finite-horizon bound. The derivative formula holds for every fixed nonorthogonal overlap; the uniqueness and asymptotic optimality assertion is only for sufficiently small positive overlap.

## Proof

**1. Exact covariance decomposition.** Apply a signed orthogonal change of coordinates so that the two row projections are
\[
Q_\pm=\begin{pmatrix}q&\pm\sqrt{qr}\\\pm\sqrt{qr}&r\end{pmatrix},\quad
q=\frac{1-c}{2},\quad r=\frac{1+c}{2}.
\]
For the state \(z_k=(e_k,y_k)\), the random linear transition is \(z_{k+1}=T_\pm z_k\), with
\[
T_\pm=\begin{pmatrix}Q_\pm&MI_2\\Q_\pm-I_2&MI_2\end{pmatrix}.
\]
The covariance propagates exactly by \(\mathcal L_{c,M}(S)=(T_+ST_+^{\mathsf T}+T_-ST_-^{\mathsf T})/2\). Reflection through the first coordinate splits its real symmetric \(4\times4\) covariance space into six even and four odd coordinates. With even coordinates
\((S_{11},S_{22},S_{13},S_{24},S_{33},S_{44})\), and odd coordinates \((S_{12},S_{14},S_{23},S_{34})\), the two matrices are, respectively,
\[
E_{c,M}=\begin{pmatrix}
q^2&qr&2Mq&0&M^2&0\\
qr&r^2&0&2Mr&0&M^2\\
q^2-q&qr&-Mc&0&M^2&0\\
qr&r^2-r&0&Mc&0&M^2\\
r^2&qr&-2Mr&0&M^2&0\\
qr&q^2&0&-2Mq&0&M^2
\end{pmatrix},
\]
\[
O_{c,M}=\begin{pmatrix}
2qr&Mq&Mr&M^2\\
2qr-q&Mq&-Mq&M^2\\
2qr-r&-Mr&Mr&M^2\\
2qr&-Mr&-Mq&M^2
\end{pmatrix}.
\]
These matrices are verified by direct multiplication from \(T_\pm\), not presumed independent coordinate dynamics. The moment radius is \(\rho(c,M)=\max\{\rho(E_{c,M}),\rho(O_{c,M})\}\).

**2. Zero momentum and first variation.** At \(M=0\), direct determinants yield
\[
\det(tI-E_{c,0})=t^5\left(t-\frac{1+c^2}{2}\right),\qquad
\det(tI-O_{c,0})=t^3\left(t-\frac{1-c^2}{2}\right).
\]
Thus, for every fixed \(c>0\), the leading even eigenvalue \(L=(1+c^2)/2\) is simple and strictly dominates every other eigenvalue. It is locally real, positive, and analytic. Implicit differentiation of \(\det(tI-E_{c,M})=0\) at \((t,M)=(L,0)\) gives
\[
a(c)=\partial_M\rho(c,0+)=-\frac{2c^2(1-c^2)}{(1+c^2)^2}.
\]
Consequently, the contraction improves strictly for all sufficiently small positive \(M\). The left eigenfunctional of the unperturbed error-covariance map is \(qS_{11}+rS_{22}\), strictly positive on the nonzero deterministic initial error covariances. Its continuation remains strictly positive on those covariances for small enough \(M\). The observed squared-error functional is likewise nonzero on the leading right eigenmatrix. Therefore for every \(e_0\ne0\) with \(y_0=0\), the squared-error root rate equals this dominant eigenvalue, rather than merely being bounded above by it.

**3. Orthogonal boundary.** At \(c=0\), the two coordinate histories are symmetric, and one coordinate satisfies \(e_{k+1}=(I_k+M)e_k-Me_{k-1}\), where \(I_k\) is an independent fair Bernoulli indicator (the choice of whether the given coordinate is *not* projected). The exact second-moment recurrence on \((\mathbb E e_k^2,\mathbb E[e_ke_{k-1}],\mathbb E e_{k-1}^2)\) has matrix
\[
B_M=\begin{pmatrix}
1/2+M+M^2&-M-2M^2&M^2\\
1/2+M&-M&0\\1&0&0
\end{pmatrix},
\]
whose characteristic polynomial is
\[
p_M(t)=t^3-(1/2+M^2)t^2+M^3t-M^3.
\]
At \(t=1/2\), \(p_M(1/2)=-M^2(2M+1)/4<0\) for \(M>0\). Since \(p_M(t)\to+\infty\) as \(t\to\infty\), the covariance operator has a real eigenvalue \(>1/2\). Conversely, at \(M=0\) its spectral radius is \(1/2\). Hence the strict orthogonal slowdown is exact. In particular the eigenvalue is observable from a nonzero coordinate with zero initial velocity (the relevant left eigenvector has nonzero first component).

**4. Sharp weak-coherence optimum.** The simple even eigenvalue near \((c,M)=(0,0)\) admits a jointly analytic continuation. An exact second implicit differentiation yields
\[
\lambda_{\mathrm{ev}}(c,M)=L(c)+a(c)M+b(c)M^2+O(M^3),
\]
where
\[
b(c)=\frac{(c-1)(c+1)(3c^2-1)(c^6-c^4+7c^2+1)}{(1+c^2)^5}.
\]
In particular \(a(c)=-2c^2+O(c^4)\), \(b(c)=1+O(c^2)\). All expressions are even in \(c\); the Taylor remainder can be taken uniformly in a neighborhood of zero. The implicit-function theorem applied to \(\partial_M\lambda_{\mathrm{ev}}=0\), with its positive second derivative at \((0,0)\), gives the unique local minimizing branch
\[
M_{\mathrm{ev}}(c)=c^2+O(c^4),\qquad
\lambda_{\mathrm{ev}}(c,M_{\mathrm{ev}}(c))=L(c)-c^4+O(c^6).
\]
The odd eigenvalue originating at \((1-c^2)/2\) has first momentum derivative \(-2c^2/(1-c^2)\) at \(M=0\); in particular at \(M=O(c^2)\) its value is \(1/2-c^2/2+O(c^4)\), whereas the even value is \(1/2+c^2/2+O(c^4)\). The other eigenvalues tend to zero. Hence the even eigenvalue is the actual spectral radius along the local optimizer.

To prove **global** uniqueness for sufficiently small \(c>0\), use the strict orthogonal inequality \(\rho(0,M)>1/2\) for every fixed \(M>0\), the continuity of finite-dimensional spectral radii, and compactness of \([0,1]\). Since the trial choice \(M=c^2\) has radius \(1/2+O(c^2)\), every global minimizer must converge to \(M=0\) as \(c\downarrow0\); otherwise a subsequence with positive limiting momentum would contradict the strict orthogonal inequality. In a fixed neighborhood of \((c,M)=(0,0)\), the analytic even eigenvalue is strictly convex in \(M\) because \(\partial_{MM}\lambda_{\mathrm{ev}}(0,0)=2\); and the full spectral radius is always at least this positive even eigenvalue. The local minimizing branch attains equality because its odd sector is strictly below it. Thus no other local or remote momentum can tie its value; it is the unique global minimizer, proving the stated expansions.

## Verification

The self-contained `verify.py` reconstructs both covariance blocks from the source's two random transition matrices at exact rational parameters, checks their entries, their complete zero-momentum characteristic polynomials, the derivative identity, the exact second-order coefficient, the scalar orthogonal cubic and its sign at \(1/2\), and 15 iterations of rational covariance propagation. Further finite floating-point tests check the predicted first derivative and the weak-coherence quartic gain. It passes 285 assertions. Numerical experiments do not establish the infinite-time assertions; those follow from the algebraic recurrence, analytic perturbation theory, and the compactness argument.

## Relationship to prior work

Alderman, Luikart, and Marshall introduced this algorithm and analyzed the signed expected error, explicitly distinguishing unresolved Euclidean-norm behavior. Their algorithm and directional mean theory are not claimed as new. Bollapragada, Chen, and Ward studied minibatch heavy-ball momentum, including nonuniform acceleration phenomena, but their general sufficient estimates do not imply the exact two-row KGSM mean-square derivative or optimal weak-coherence law.

An earlier exact analysis of the **orthonormal** \(2\times2\) KGSM system characterized the mean-square stability threshold \(\beta+2(1-\beta)M<\sqrt{\beta+2}\); another diagonal-system analysis established unequal-row-sampling stability thresholds. Neither covers nonorthogonal rows or the **asymptotic mean-square acceleration derivative**. A separate two-row **cyclic Kaczmarz overrelaxation** result concerns deterministic alternation and an unrelated parameter. The present contribution is the coherent two-row rate perturbation and its sharp optimal emergence, not the known stability frontier.

## Limitations

The theorem concerns only a consistent two-equation, two-unknown, full-rank real system, independent uniform row sampling, zero initial momentum state, \(\beta=0\), and squared Euclidean iterate error in exact arithmetic. The derivative conclusion holds pointwise in \(c\), not uniformly near \(c=1\). The unique global minimizer expansion is only for sufficiently weak, nonzero coherence, with no explicit universal upper value of \(c_0\). Neither a global optimal-momentum formula for arbitrary coherence nor almost-sure convergence or noisy/inconsistent-system conclusions are established. Same-algorithm equivalents in older stochastic heavy-ball work cannot be ruled out solely by bibliographic search.

## References

1. Seth J. Alderman, Roan W. Luikart, and Nicholas F. Marshall, “Randomized Kaczmarz with Geometrically Smoothed Momentum,” arXiv:2401.09415v1, initially public January 17, 2024; SIAM Journal on Matrix Analysis and Applications 45(4), 2024, DOI 10.1137/24M1633820.
2. Raghu Bollapragada, Tyler Chen, and Rachel Ward, “On the Fast Convergence of Minibatch Heavy Ball Momentum,” arXiv:2206.07553, initially public June 2022.
3. “Exact mean-square stability frontier and a signed-mean blind spot in KGSM,” published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-mean-square-stability-frontier-and-a-signed-mean-blind-spo--e15c00248209.
