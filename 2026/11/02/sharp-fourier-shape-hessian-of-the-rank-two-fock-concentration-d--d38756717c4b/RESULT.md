# Sharp Fourier-shape Hessian of the rank-two Fock concentration deficit

## Finding

Let \(\mathcal F^2\) be the Hilbert space of entire functions with
\[\|f\|_{\mathcal F^2}^2=\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,\frac{dA(z)}{\pi},\]
and let \(T_\Omega f=P_{\mathcal F^2}(\mathbf1_\Omega f)\). Set
\(K_2(\Omega)=\lambda_0(T_\Omega)+\lambda_1(T_\Omega)\), the sum of the two largest eigenvalues (indices start at zero here).

Fix any \(t>0\) and real \(h\in C^2(\mathbb R/2\pi\mathbb Z)\) of mean zero. For sufficiently small real \(\varepsilon\), define the *exactly area-preserving* domain
\[\Omega_{\varepsilon,h}=\{\sqrt u\,e^{i\theta}:0\le u<t+\varepsilon h(\theta),\;0\le\theta<2\pi\}.\]
Its Euclidean area is always \(\pi t\), and \(D_t=\Omega_{0,h}=\{|z|^2<t\}\). Put \(\widehat h(k)=(2\pi)^{-1}\int_0^{2\pi}h(\theta)e^{-ik\theta}\,d\theta\).

Define, for every integer \(k\ge2\),
\[
\delta_k(t)=t-\frac{t^k/k!}{\sum_{j=1}^k t^j/j!}
-\frac{t^{k+2}/(k+1)!}{\sum_{j=2}^{k+1}t^j/j!}.
\]
Then the complete second-variation identity is
\[
\boxed{K_2(D_t)-K_2(\Omega_{\varepsilon,h})
=\varepsilon^2e^{-t}\sum_{k=2}^{\infty}\delta_k(t)|\widehat h(k)|^2
+O_{t,h}(\varepsilon^3).}
\]
The coefficients satisfy the strict ordering
\[
0<\delta_2(t)<\delta_3(t)<\cdots<t,
\qquad \delta_2(t)=\frac{t(2t+3)}{(t+2)(t+3)},
\qquad \lim_{k\to\infty}\delta_k(t)=t.
\]
In particular the degree-one Fourier modes are exactly the Hessian's translation null directions. Writing \(\Pi_{\ge2}\) for the orthogonal projection in normalized angular \(L^2\) onto frequencies \(|k|\ge2\), the optimal transverse quadratic constant is
\[
\boxed{\lim_{\varepsilon\to0}\frac{K_2(D_t)-K_2(\Omega_{\varepsilon,h})}{\varepsilon^2}
\ge \frac{e^{-t}t(2t+3)}{2(t+2)(t+3)}
\|\Pi_{\ge2}h\|_{L^2(d\theta/2\pi)}^2.}
\]
Equality in this quadratic inequality occurs exactly when \(\widehat h(k)=0\) for every \(|k|\ge3\). The constant is attained at quadratic order by every nonzero second harmonic, and cannot be enlarged.

## Assumptions and scope

There are no small-area or large-area restrictions: \(t\) is any positive real number. Boundary disturbances \(h\) are real, periodic, twice continuously differentiable and mean-zero; the smallness condition \(|\varepsilon|\|h\|_\infty<t\) ensures a star-shaped domain. The normalization \(e^{-|z|^2}dA/\pi\) makes the disk parameter \(t\) equal to its area divided by \(\pi\); the alternate Fock normalization \(e^{-\pi|z|^2}dA\) is related by a unitary spatial rescaling. The statement concerns the rank-two sum, not the second eigenvalue alone or higher-rank sums.

## Proof

The normalized monomials \(e_n(z)=z^n/\sqrt{n!}\), \(n=0,1,\ldots\), diagonalize \(T_{D_t}\), with simple strictly decreasing positive eigenvalues
\[
\lambda_n(t)=\frac1{n!}\int_0^t u^n e^{-u}\,du
=1-e^{-t}\sum_{j=0}^n\frac{t^j}{j!}.
\]
Consequently \(K_2(D_t)=2-(2+t)e^{-t}\), and \(\lambda_i-\lambda_j=e^{-t}\sum_{\ell=i+1}^{j}t^\ell/\ell!\) whenever \(j>i\).

Polar integration gives the exact operator matrix
\[
\langle T_{\Omega_{\varepsilon,h}}e_n,e_m\rangle
=\frac1{2\pi\sqrt{n!m!}}\int_0^{2\pi}
 e^{i(n-m)\theta}\int_0^{t+\varepsilon h(\theta)}
 e^{-u}u^{(n+m)/2}\,du\,d\theta.
\]
The first and second parameter derivatives at zero are, with \(r=(n+m)/2\),
\[
(T'_0)_{nm}=\frac{e^{-t}t^r}{\sqrt{n!m!}}\widehat h(m-n),\qquad
(T''_0)_{nm}=\frac{e^{-t}t^r}{\sqrt{n!m!}}
\left(\frac r t-1\right)\widehat{h^2}(m-n).
\]
There is no hidden first-order area term because \(\widehat h(0)=0\). For \(t>0\), the parameter-dependent Toeplitz operator is \(C^3\) in trace norm: locally near \(u=t\), the normalized coherent-state rank-one projector depends smoothly in trace norm on \(\sqrt u\,e^{i\theta}\); integrate the projector over the moving upper endpoint. The simple isolated top eigenvalues therefore admit the standard second-order perturbation formula. Since their internal couplings cancel upon summing, one obtains
\[
K_2''(0)=\sum_{i=0}^1(T''_0)_{ii}
+2\sum_{i=0}^1\sum_{j\ge2}\frac{|(T'_0)_{ji}|^2}{\lambda_i-\lambda_j}.
\]
The first sum is \(-te^{-t}\widehat{h^2}(0)\). For each positive Fourier frequency \(k\), the only external pairs are \((i,j)=(1,k+1)\), and additionally \((0,k)\) when \(k\ge2\). Their contributions are
\[
B_k(t)=\frac{t^{k+2}/(k+1)!}{\sum_{\ell=2}^{k+1}t^\ell/\ell!},\qquad
A_k(t)=\frac{t^k/k!}{\sum_{\ell=1}^{k}t^\ell/\ell!}\quad(k\ge2),
\]
with \(A_1(t)=0\). Parseval for real mean-zero \(h\) yields
\[
K_2''(0)=-2e^{-t}\sum_{k\ge1}
\bigl(t-A_k(t)-B_k(t)\bigr)|\widehat h(k)|^2.
\]
For the translation frequency \(k=1\), \(B_1(t)=t\), so its coefficient is zero. Taylor's theorem gives the stated second variation.

For strict positivity and the sharp spectral ordering, divide the last terms in each denominator by their highest-degree summand. For \(k\ge2\),
\[
A_k(t)^{-1}=1+\sum_{j=1}^{k-1}\frac{k!}{(k-j)!}\,t^{-j}.
\]
For \(k\ge1\),
\[
\frac{t}{B_k(t)}=1+\sum_{j=1}^{k-1}\frac{(k+1)!}{(k+1-j)!}\,t^{-j}.
\]
Every displayed falling-factorial coefficient increases strictly as its upper index increases, and an additional positive term appears. Thus \(A_k\) is strictly decreasing for \(k\ge2\), and \(B_k\) strictly decreases for \(k\ge1\). Direct calculation gives
\[
A_2(t)=\frac{t}{t+2},\qquad B_2(t)=\frac{t^2}{t+3},\qquad
 t-A_2(t)-B_2(t)=\frac{t(2t+3)}{(t+2)(t+3)}>0.
\]
It follows that \(0<\delta_2<\delta_3<\cdots\). Both \(A_k,B_k\to0\) at fixed \(t\) (each is bounded by its first positive denominator term, giving factorial decay), so \(\delta_k\to t\). Finally, \(\|\Pi_{\ge2}h\|_2^2=2\sum_{k\ge2}|\widehat h(k)|^2\) and the minimum \(\delta_2\) give the sharp bound and equality criterion.

## Verification

The supplementary standalone standard-library script `verify.py` checks rational identities and strict coefficient ordering for 1,060 rational-arithmetic assertions. It independently builds finite Fock Toeplitz matrices by integrating the actual noncircular indicator domains and compares symmetric second differences of their two largest eigenvalues with the analytical Hessian in 12 tests. Run `python3 verify.py`; the expected final line is `ALL_CHECKS_OK`. The all-frequency conclusion is proved by the falling-factorial comparisons above; finite checks alone do not establish it. The area of every test domain is exactly \(\pi t\) for all sufficiently small parameters.

## Relationship to prior work

Nicola, Riccardi and Tilli (arXiv:2503.07069, first posted 2025-03-10) established the disk maximization within radial Fock masks and posed the unrestricted Ky Fan maximization problem. Their later arXiv:2607.20965 (2026-07-23) proved existence of maximizing masks. Abreu (arXiv:2607.28376, 2026-07-30) subsequently proved the unrestricted global disk inequality for every rank. The new assertion here is **not** global disk optimality: it is the exact second-order Fourier spectrum and optimal *rank-two local shape-stability coefficient*. Abreu's global inequality implies a nonnegative local deficit but does not state or directly specify the quadratic coefficient, translation kernel, or degree-two rigidity. Gómez, Guerra, Ramos and Tilli (2024) treated quantitative stability for the *rank-one* concentration functional, not the rank-two Hessian considered here.

## Limitations

No global stability inequality with this coefficient is asserted; the bound is a second-order limit for fixed smooth area-preserving perturbations only. Its error constant depends on the chosen profile and area parameter, and the result does not classify all global equality sets or analyze higher Ky Fan ranks. Unindexed historical statements of the same shape Hessian cannot be categorically excluded without independent literature review.

## References

1. F. Nicola, F. Riccardi, P. Tilli, *The Faber–Krahn inequality for partial sums of eigenvalues of Toeplitz operators*, arXiv:2503.07069v1 (2025-03-10), https://arxiv.org/abs/2503.07069.
2. F. Nicola, F. Riccardi, P. Tilli, *On the existence of extremizers for the sum of eigenvalues of Toeplitz operators*, arXiv:2607.20965v1 (2026-07-23), https://arxiv.org/abs/2607.20965.
3. L. D. Abreu, *The isoperimetric inequality for the Ky Fan norm*, arXiv:2607.28376v1 (2026-07-30), https://arxiv.org/abs/2607.28376.
4. J. Gómez, A. Guerra, J. P. G. Ramos, P. Tilli, *Stability of the Faber–Krahn inequality for the short-time Fourier transform*, Inventiones mathematicae 236 (2024), 779–836, https://doi.org/10.1007/s00222-024-01248-2.
