# Quadratic radial annular stability for the p-adic sharp Hardy deficit
## Finding
Fix a prime \(p\), an integer \(n\ge1\), and \(0<\alpha<n\). Let
\[
h(x)=\|x\|_p^{-(n-\alpha)/2},\qquad C_{n,\alpha}=\frac{p^\alpha-1}{1-p^{-n-\alpha}},
\]
and let \(C^{\sharp}_{p,n,\alpha}\) be the sharp quadratic Hardy constant of Sun. Write
\[
S_k=\{x\in\mathbb Q_p^n:\|x\|_p=p^{-k}\},\qquad A_N=\bigcup_{k=-N}^{N}S_k,
\]
and define the Hardy mass and deficit by
\[
W_\alpha[u]=\int_{\mathbb Q_p^n}\|x\|_p^{-\alpha}|u(x)|^2\,dx,
\]
\[
\Delta_\alpha[u]=E_\alpha[u]-C^{\sharp}_{p,n,\alpha}W_\alpha[u].
\]
For every nonzero radial Bruhat--Schwartz function \(u\) supported in \(A_N\), write \(u=h v\). Then \(v\) is constant on each shell, say \(v=a_k\) on \(S_k\), with \(a_k=0\) when \(|k|>N\). Put
\[
r=p^{-(n+\alpha)/2}.
\]
The deficit has the exact one-dimensional representation
\[
\Delta_\alpha[u]
=C_{n,\alpha}(1-p^{-n})^2
\sum_{m\ge1}r^m\sum_{k\in\mathbb Z}|a_{k+m}-a_k|^2,
\]
and
\[
W_\alpha[u]=(1-p^{-n})\sum_{k\in\mathbb Z}|a_k|^2.
\]
Thus the radial annular stability constant
\[
\mu_N^{\mathrm{rad}}=
\inf_{0\ne u\ \mathrm{radial},\ \operatorname{supp}u\subset A_N}
\frac{\Delta_\alpha[u]}{W_\alpha[u]}
\]
satisfies, for every \(N\ge1\),
\[
C_{n,\alpha}(1-p^{-n})r\lambda_N
\le \mu_N^{\mathrm{rad}}
\le C_{n,\alpha}(1-p^{-n})
\frac{r(1+r)}{(1-r)^3}\lambda_N,
\]
where
\[
\lambda_N=4\sin^2\!\left(\frac{\pi}{4N+4}\right).
\]
In particular,
\[
\mu_N^{\mathrm{rad}}\asymp (N+1)^{-2}.
\]
The upper bound is witnessed by the sine shell profile
\[
a_k=\sin\!\left(\frac{\pi(k+N+1)}{2N+2}\right),\qquad -N\le k\le N,
\]
with \(a_k=0\) outside that interval.

## Assumptions and scope
The field is \(\mathbb Q_p^n\) with Haar measure normalized by \(|\mathbb Z_p^n|=1\). The shells and the self-dual Fourier normalization are those of arXiv:2610.04463v1. The result concerns the quadratic-form Hardy inequality, radial test functions, and the finite annulus \(A_N\). It does not assert the optimal constant for nonradial functions, nor does it identify an exact closed form for \(\mu_N^{\mathrm{rad}}\); it gives explicit two-sided bounds with the sharp decay order in \(N\).

The restriction to \(A_N\) is mathematically natural: the focal source itself uses the same annuli to construct minimizing sequences and explicitly identifies quantitative lower bounds for the subcritical remainder as a further question. The present statement answers that question on the radial annular sector and shows that smoothing the shell cutoff changes the available approximation scale from the hard-cutoff estimate to a quadratic-in-width spectral scale.

## Proof
Sun's ground-state representation gives
\[
\Delta_\alpha[u]
=\frac{C_{n,\alpha}}{2}\iint
\frac{h(x)h(y)|v(x)-v(y)|^2}{\|x-y\|_p^{n+\alpha}}\,dx\,dy.
\]
For \(x\in S_k\) and \(y\in S_\ell\) with \(k\ne\ell\), the ultrametric shell identity gives
\[
\|x-y\|_p=p^{-\min\{k,\ell\}},
\]
while
\[
|S_k|=(1-p^{-n})p^{-nk},\qquad h|_{S_k}=p^{k(n-\alpha)/2}.
\]
Therefore the integral of the kernel over \(S_k\times S_\ell\) is
\[
(1-p^{-n})^2p^{-(n+\alpha)|k-\ell|/2}
=(1-p^{-n})^2r^{|k-\ell|}.
\]
Because \(v\) is shell-constant, same-shell pairs contribute zero. Combining the two orientations of each unordered pair yields
\[
\Delta_\alpha[u]
=C_{n,\alpha}(1-p^{-n})^2
\sum_{k<\ell}r^{\ell-k}|a_\ell-a_k|^2.
\]
Grouping by \(m=\ell-k\) proves the exact shell identity.

For the Hardy mass, on \(S_k\) one has
\[
\|x\|_p^{-\alpha}h(x)^2=\|x\|_p^{-n},
\]
so every shell contributes the same factor \(1-p^{-n}\). Hence
\[
W_\alpha[u]=(1-p^{-n})\sum_k|a_k|^2.
\]

Set
\[
D_m(a)=\sum_{k\in\mathbb Z}|a_{k+m}-a_k|^2.
\]
The exact identity becomes
\[
\frac{\Delta_\alpha[u]}{W_\alpha[u]}
=C_{n,\alpha}(1-p^{-n})
\frac{\sum_{m\ge1}r^mD_m(a)}{\sum_k|a_k|^2}.
\]
Since all terms are nonnegative,
\[
\sum_{m\ge1}r^mD_m(a)\ge rD_1(a).
\]
For sequences supported on \(-N,\ldots,N\) and extended by zero, the sharp Dirichlet path Poincare inequality is
\[
D_1(a)\ge\lambda_N\sum_k|a_k|^2,
\qquad
\lambda_N=4\sin^2\!\left(\frac{\pi}{4N+4}\right).
\]
This proves the lower bound.

For the upper bound choose
\[
a_k=\sin\!\left(\frac{\pi(k+N+1)}{2N+2}\right)
\]
on \(-N,\ldots,N\), zero elsewhere. This is the first Dirichlet eigenvector, so
\[
D_1(a)=\lambda_N\sum_k|a_k|^2.
\]
For every \(m\ge1\), telescoping and Cauchy--Schwarz give
\[
|a_{k+m}-a_k|^2
\le m\sum_{j=0}^{m-1}|a_{k+j+1}-a_{k+j}|^2.
\]
Summing over \(k\) gives
\[
D_m(a)\le m^2D_1(a).
\]
Therefore
\[
\sum_{m\ge1}r^mD_m(a)
\le D_1(a)\sum_{m\ge1}m^2r^m
=D_1(a)\frac{r(1+r)}{(1-r)^3},
\]
which proves the upper bound. Finally,
\[
\lambda_N\sim\frac{\pi^2}{4(N+1)^2},
\]
so the best radial annular remainder constant has exact decay order \((N+1)^{-2}\).

## Verification
The critical normalization was checked directly against Proposition 3.2 and the shell-pair computation in Proposition 3.5 of arXiv:2610.04463v1. The factor \(1/2\) in the ground-state double integral is cancelled by the two orientations of every pair of distinct shells. The Hardy mass identity follows from the exact cancellation of the shell measure with \(\|x\|_p^{-n}\).

The discrete lower bound uses the standard first Dirichlet eigenvalue of a path with \(2N+1\) interior vertices and zero boundary values, namely \(4\sin^2(\pi/(4N+4))\). The upper bound uses only the finite telescoping inequality and the exact series
\[
\sum_{m\ge1}m^2r^m=\frac{r(1+r)}{(1-r)^3},\qquad 0<r<1.
\]
Finite numerical evaluations were used only to check normalization and inequality directions; they are not part of the proof.

## Relationship to prior work
Sun proves the sharp quadratic Hardy constant, the exact ground-state representation, and an explicit hard annular truncation with an \(O((2N+1)^{-1})\) convergence estimate. The same paper states that quantitative lower bounds for the subcritical remainder are a further question. The present result uses Sun's exact shell kernel to identify a discrete weighted translation energy for arbitrary radial shell profiles and then derives an explicit annular spectral gap together with a matching \((N+1)^{-2}\) upper scale.

Bendikov, Grigor'yan, and Molchanov study the Taibleson--Vladimirov operator with the critical inverse-power potential and establish the underlying Hardy-type nonnegativity and critical coupling in the one-dimensional p-adic setting. Their inspected treatment does not provide the radial finite-annulus shell spectral estimate above. Kassymov and Velasquez-Rodriguez prove broader Hardy, Hardy--Littlewood--Sobolev, and Stein--Weiss estimates on constant-order Vilenkin groups; those estimates do not imply this deficit identity or its finite-annulus spectral scale.

## Limitations
The theorem is a radial finite-annulus stability statement. The constants displayed in the two-sided estimate are explicit but are not asserted to be the exact value of \(\mu_N^{\mathrm{rad}}\). The upper constant comes from the elementary bound \(D_m\le m^2D_1\), so a sharper analysis of the full Toeplitz-type shell energy could improve the multiplicative constant while leaving the proved \((N+1)^{-2}\) order unchanged. No claim is made about the corresponding optimal nonradial annular stability constant or about the nonlinear \(L^q\) Hardy deficit.

## References
1. Y. Sun, *Sharp Hardy inequalities for the Vladimirov--Taibleson operator on \(\mathbb Q_p^n\)*, arXiv:2610.04463v1, 2026. In particular: Lemma 2.1, Proposition 3.2, Proposition 3.5, and the discussion after the introduction.
2. A. Bendikov, A. Grigor'yan, and S. Molchanov, *Hierarchical Schrodinger operators with singular potentials*, 2022.
3. A. Kassymov and J. P. Velasquez-Rodriguez, *Hardy inequalities on constant-order noncommutative Vilenkin groups*, arXiv:2208.03495, 2022.
