# Parity-sharp covariance conditioning of cycle fractional stable-set polytopes

## Finding
For every integer \(n\ge3\), let
\[
F_n=\{x\in\mathbb R^n:x_i\ge0,\ x_i+x_{i+1}\le1\ (i\in\mathbb Z/n\mathbb Z)\},
\]
let \(X^{(n)}\) be uniform in \(F_n\) with respect to Euclidean volume, and let \(C_n=\operatorname{Cov}(X^{(n)})\). The spectral condition number \(\kappa_n=\lambda_{\max}(C_n)/\lambda_{\min}(C_n)\) has a parity-sharp limit:
\[
\boxed{\kappa_\infty=\frac{\pi^4}{12(12-\pi^2)}}.
\]
For even \(n\), \(\kappa_n=\kappa_\infty+O(n3^{-n})\); for odd \(n\),
\[
\boxed{\lim_{\substack{n\to\infty\\n\text{ odd}}}n^2(\kappa_\infty-\kappa_n)=\frac{\pi^8}{160(12-\pi^2)}>0.}
\]
More precisely, there is an explicit strictly decreasing smooth function \(f:[-1,1]\to(0,\infty)\), defined below, such that the cyclic Fourier eigenvalues \(\widehat C_n(j)\), for \(0\le j<n\), satisfy uniformly
\[
\widehat C_n(j)=f(\cos(2\pi j/n))+O(n3^{-n}).
\]
The endpoint values and derivative are
\[
f(-1)=\frac1{12},\qquad f(1)=\frac{12-\pi^2}{\pi^4},\qquad f'(-1)=-\frac{\pi^2}{80}.
\]
Thus the distinction is not merely parity of the underlying graph: an even cycle samples the exact alternating Fourier mode, while an odd cycle necessarily misses that mode by an angular separation of order \(1/n\).

## Assumptions and scope
The body \(F_n\) is the *fractional* stable-set polytope of a cycle, not the integral stable-set polytope. Its full-dimensional interior includes points with every coordinate strictly between zero and one-half. Covariance and volume always use the standard Euclidean structure of the displayed coordinate realization. The Fourier eigenvalues are the eigenvalues of the actual uniform-volume covariance, not of an inscribed-ellipsoid shape matrix, a vertex distribution, or a graph adjacency matrix. All big-O assertions have universal constants and hold along the stated parity subsequence as \(n\to\infty\).

For \(k\ge1\) define
\[
\rho_k=\frac{(-1)^k}{2k+1},\qquad j_k=\begin{cases}k& k\text{ odd},\\ k+1&k\text{ even},\end{cases}\qquad a_k^2=\frac4{\pi^4j_k^4}.
\]
The spectral symbol is the absolutely and smoothly convergent series
\[
\boxed{f(t)=\sum_{k=1}^{\infty}a_k^2\frac{1-\rho_k^2}{1-2\rho_k t+\rho_k^2}\quad(-1\le t\le1).}
\]

## Proof
**1. Exact transfer representation.** Set \(K(x,y)={\bf1}_{\{x+y\le1\}}\) for \(x,y\in[0,1]\), and let \(T\) be the integral operator with kernel \(K\). The constraint cycle gives \(\operatorname{Vol}(F_n)=\operatorname{Tr}(T^n)\). Let \(M\) denote multiplication by the coordinate variable. For \(1\le r\le n-1\), cyclic integration gives the exact identities
\[
\mathbb E X_0=\frac{\operatorname{Tr}(MT^n)}{\operatorname{Tr}(T^n)},\quad
\mathbb E(X_0X_r)=\frac{\operatorname{Tr}(MT^rMT^{n-r})}{\operatorname{Tr}(T^n)},\quad
\mathbb E X_0^2=\frac{\operatorname{Tr}(M^2T^n)}{\operatorname{Tr}(T^n)}.
\]
The operator \(T\) is compact, self-adjoint and Hilbert–Schmidt. Solving its differentiated eigenequation with the boundary condition at \(x=1\) gives the complete orthonormal eigenbasis
\[
\phi_k(x)=\sqrt2\cos((k+\tfrac12)\pi x),\qquad
T\phi_k=\frac{2(-1)^k}{(2k+1)\pi}\phi_k\quad(k\ge0).
\]
In particular, writing \(D=\pi T/2\), we have \(D=P+R\), where \(P\) projects onto \(\phi_0\), \(PR=RP=0\), and the eigenvalues of \(R\) are \(\rho_k\) for \(k\ge1\). The operator norm of \(R\) is exactly \(1/3\), and \(R\) is Hilbert–Schmidt.

**2. The infinite-cycle correlation kernel and a uniform finite-cycle bound.** Elementary integration of the product of two cosines shows
\[
\mu=\langle\phi_0,M\phi_0\rangle=\frac12-\frac2{\pi^2},\qquad
\langle\phi_k,M\phi_0\rangle=-\frac2{\pi^2j_k^2}\quad(k\ge1).
\]
Define \(\gamma(r)=\sum_{k\ge1}a_k^2\rho_k^{|r|}\) for every integer \(r\). Then \(\gamma(0)=1/12-4/\pi^4\), and all correlations are absolutely summable. Expanding \(D^r=P+R^r\), the traces above imply, uniformly for \(1\le r\le n-1\),
\[
\operatorname{Cov}(X_0,X_r)=\gamma(r)+\gamma(n-r)+O(3^{-n+2}),
\]
and \(\operatorname{Var}(X_0)=\gamma(0)+O(3^{-n+2})\). Indeed, the remaining mixed trace is bounded by
\[
|\operatorname{Tr}(MR^rMR^{n-r})|\le\|M\|^2\|R^r\|_{\rm HS}\|R^{n-r}\|_{\rm HS}\le B3^{-n+2}
\]
for an absolute finite constant \(B\). The normalization denominator \(\operatorname{Tr}D^n=1+\operatorname{Tr}R^n\) equals \(1+O(3^{-n+2})\), and the mean differs from \(\mu\) by the same order. By cyclic symmetry the covariance matrix is circulant, so its discrete Fourier eigenvalues are sums of these entries. Summing \(n\) uniform errors, and adding the exponentially small tails from periodizing \(\gamma\), establishes
\[
\widehat C_n(j)=f(\cos(2\pi j/n))+O(n3^{-n}),
\]
where \(f(\cos\theta)=\sum_{r\in\mathbb Z}\gamma(r)e^{ir\theta}\). Summation of the geometric series in \(r\) gives precisely the claimed series for \(f\). Since \(|\rho_k|\le1/3\) and \(a_k^2=O(k^{-4})\), this series has derivatives of every order on \([-1,1]\).

**3. Strict spectral monotonicity.** Pair the term indexed by \(k=2\ell-1\) with \(k=2\ell\), for \(\ell\ge1\). Their correlation ratios have opposite signs: \(-u=-1/(4\ell-1)\) and \(v=1/(4\ell+1)\). The negative derivative term has minimum absolute magnitude at \(t=1\), and the positive derivative term attains its maximum at \(t=1\). With weights \(A=4/[\pi^4(2\ell-1)^4]\) and \(B=4/[\pi^4(2\ell+1)^4]\), their difference at that endpoint is strictly positive because
\[
\frac{Au(1-u)}{(1+u)^3}-\frac{Bv(1+v)}{(1-v)^3}
=\frac4{\pi^4}\frac{20\ell^2-1}{8\ell^2(2\ell-1)^3(2\ell+1)^3}>0.
\]
Therefore the derivative of every paired summand is strictly negative throughout \([-1,1]\), and \(f'(t)<0\) there. Moreover the first pair supplies a fixed positive lower bound for \(-f'(t)\) on the entire interval.

**4. Exact endpoint identities.** Directly setting \(t=-1\) pairs the odd-indexed denominator contributions into twice each odd reciprocal fourth power. Euler's sum \(\sum_{m\ge0}(2m+1)^{-4}=\pi^4/96\) yields \(f(-1)=1/12\). At \(t=1\), the same pairing gives
\[
f(1)=\frac4{\pi^4}\left[\frac12+2\sum_{\substack{j\ge3\\j\text{ odd}}}\frac1{j^2(j^2-1)}\right]=\frac{12-\pi^2}{\pi^4}.
\]
Here \(\sum_{j\ge3,\,j\text{ odd}}(j^2-1)^{-1}=1/4\) and \(\sum_{j\ge3,\,j\text{ odd}}j^{-2}=\pi^2/8-1\). Differentiating at \(t=-1\), the paired terms similarly reduce to the odd reciprocal sixth-power sum, giving
\[
f'(-1)=-\frac4{\pi^4}\cdot3\sum_{\substack{j\ge1\\j\text{ odd}}}\frac1{j^6}=-\frac{\pi^2}{80}.
\]
The positive endpoints show \(f\) is bounded below by \((12-\pi^2)/\pi^4>0\).

**5. Sharp parity split and the extrema.** On the Fourier mesh \(\{\cos(2\pi j/n):0\le j<n\}\), \(t=1\) occurs at \(j=0\) for every \(n\). The minimum \(t=-1\) occurs at \(j=n/2\) exactly for even \(n\), whereas odd \(n\) has the two nearest modes at \(t=-\cos(\pi/n)=-1+\pi^2/(2n^2)+O(n^{-4})\). Since \(-f'\) is bounded away from zero, the gaps between those extremal sampled levels and their competitors are bounded below by a positive constant times \(n^{-2}\). The uniform \(O(n3^{-n})\) eigenvalue error is negligible compared with those gaps, so for all sufficiently large \(n\) the actual covariance eigenvalue minimum occurs at the constant mode and its maximum occurs at the most alternating mode (two modes when \(n\) is odd). For even \(n\), the ratio is \(f(-1)/f(1)+O(n3^{-n})\). For odd \(n\), Taylor expansion at \(-1\) gives
\[
\frac{f(-\cos(\pi/n))}{f(1)}
=\frac{f(-1)}{f(1)}-\frac{\pi^2(-f'(-1))}{2f(1)n^2}+O(n^{-4}).
\]
Substituting the exact endpoint and derivative identities yields the two asserted parity rates and the positive limit constant. This completes the proof.

## Verification
The companion standard-library `verify.py` computes an independent exact rational moment check at \(n=3\) by a two-simplex decomposition, including the exact mean \(7/24\), diagonal covariance \(23/576\), off-diagonal covariance \(-29/2880\), and spectral ratio \(48/19\). It separately constructs finite transfer-matrix spectral traces and their Fourier eigenvalues for ten cycle lengths, compares the sampled symbol, and checks endpoint/derivative identities numerically from long absolutely convergent sums. Run `python3 verify.py`. These are finite checks only; the infinite-dimensional trace estimates, strict sign inequality, and asymptotic limits are proved above and are not established by the script.

## Relationship to prior work
Kafer, Pashkovich and Sanità analyze circuit diameter and half-integral vertex geometry of fractional stable-set polytopes and provide the mid-period source for this natural polytope family. Hamano, Hibi and Ohsugi analyze Ehrhart series and Gorenstein properties of the same bodies. Existing treatments of cycle fractional stable-set polytopes also give exact enclosing spheres and John ellipsoids; those **are not** uniform-volume covariance matrices and their shape spectra do not imply this theorem. The transfer-operator method and Fourier diagonalization are established techniques; originality is sought only for the complete explicit uniform-volume covariance *conditioning*, its strict symbol shape, and the sharp even/odd convergence-rate dichotomy, not for the general techniques or polytope definitions. A prior equivalent formulation in statistical mechanics of one-dimensional continuous hard-core models remains possible.

## Limitations
The spectral profile is an asymptotic approximation with an exponential error, not an exact finite-dimensional covariance formula. The location of the extreme Fourier modes is proved for all sufficiently large dimensions, not asserted for every dimension in the analytic theorem. The result applies only to these unweighted cycle constraints in the coordinate Euclidean metric, and does not determine uniform-volume covariance for arbitrary graphs or integral stable-set polytopes. The mathematical analysis and finite checks have not received independent auditing. Bibliographic completeness cannot be guaranteed, especially under alternate continuous-hard-core, transfer-integral, or excluded-volume nomenclature.

## References
1. S. Kafer, K. Pashkovich, L. Sanità, *On the Circuit Diameter of some Combinatorial Polytopes*, arXiv:1709.09642v1, publicly posted 2017-09-27, Section 5, https://arxiv.org/abs/1709.09642 .
2. G. Hamano, T. Hibi, H. Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, arXiv:1603.09613v1, publicly posted 2016-03-31, https://arxiv.org/abs/1603.09613 .
3. Au and Tunçel, *Work on the Lovász–Schrijver operator and fractional stable-set polytopes*, arXiv:2303.08971v1, publicly posted 2023-03-15, https://arxiv.org/abs/2303.08971 .
4. Previous same-object geometric results: *An exact John ellipsoid and sharp exponential law for odd-cycle fractional stable-set polytopes*, and *Cycle fractional stable-set polytopes have a parity-split minimum sphere*, public published-finding corpus findings at https://github.com/published-finding corpus/2026/tree/main/2026/10/11 .
