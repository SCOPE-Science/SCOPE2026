# Critical exponential boundary layer for cyclic Dirichlet Gram spectra

## Finding
Fix \(c>0\) and \(\tau>0\). In the Dirichlet-type Hilbert space with coefficient norm
\[\|f\|_\tau^2=\sum_{n=0}^\infty(n+\tau)|a_n|^2,\qquad f(z)=\sum_{n=0}^\infty a_nz^n,\]
let \(K_\tau(z,w)=\sum_{n\ge0}(z\overline w)^n/(n+\tau)\) be the reproducing kernel. For each integer \(N\ge2\), place \(N\) points \(z_{N,k}=r_Ne^{2\pi ik/N}\) at radius \(r_N=\sqrt{1-e^{-cN}}\), and define their normalized kernel Gram matrix
\[G_N=(K_\tau(z_{N,k},z_{N,l})/K_\tau(r_N,r_N))_{0\le k,l<N}.\]
Its discrete-Fourier eigenvalues \(\lambda_{N,j}\), indexed by \(0\le j<N\), are strictly decreasing, and satisfy the uniform sharp boundary-layer law
\[\boxed{\max_{0\le j<N}\left|\lambda_{N,j}-\left(1+\frac1{c(j+\tau)}\right)\right|\le C_{c,\tau}\frac{\log N}{N}\quad (N\ge N_0(c,\tau)).}\]
Thus the optimal squared upper and lower finite interpolation-frame bounds obey
\[\lambda_{\max}(G_N)\longrightarrow1+\frac1{c\tau},\qquad \lambda_{\min}(G_N)\longrightarrow1,\qquad \kappa(G_N)\longrightarrow1+\frac1{c\tau}.\]
With the matrices first conjugated by the discrete Fourier transform and then extended as identity beyond their first \(N\) coordinates, they converge in operator norm on \(\ell^2(\mathbb N_0)\) to \(I+\operatorname{diag}_{j\ge0}(1/[c(j+\tau)])\). In contrast, the maximum absolute inner product of two **distinct normalized kernel vectors** is \(O_{c,\tau}(\log N/N)\), hence tends to zero. Pairwise asymptotic orthogonality therefore does not imply asymptotic tightness for this growing point array.

## Assumptions and scope
The parameters \(c\) and \(\tau\) are fixed positive real numbers, and \(N\) tends to infinity through integers at least two. The norm specifies the precise Dirichlet normalization; in particular \(\tau=1\) gives the logarithmic kernel \(K_1(z,w)=-\log(1-z\overline w)/(z\overline w)\), with the continuous value at zero. The result concerns these finite regular-circle arrays only. Frame eigenvalues refer to the positive kernel Gram matrix, with no claims about arbitrary point sets or a single infinite interpolating sequence.

## Proof
Write \(\rho=1-e^{-cN}\), \(t=\rho^N\), and \(d_N=K_\tau(r_N,r_N)\). A discrete Fourier transform of the nonnegative power series gives the exact eigenvalue identity
\[\lambda_{N,j}=\frac{N}{d_N}\sum_{k=0}^\infty\frac{\rho^{j+kN}}{j+kN+\tau},\qquad 0\le j<N.\tag{1}\]
Every summand decreases strictly as \(j\) increases, so \(\lambda_{N,0}>\lambda_{N,1}>\cdots>\lambda_{N,N-1}>0\). This also identifies all maximizing and minimizing Fourier modes without a limiting argument.

For \(a>0\) put \(F_a(t)=\int_0^t v^{a-1}/(1-v)\,dv\). Geometric-series integration shows
\[N\sum_{k\ge0}\frac{\rho^{j+kN}}{j+kN+\tau}=\rho^{-\tau}F_{(j+\tau)/N}(t).\tag{2}\]
Uniformly for \(0<a\le2\) and \(1/2<t<1\),
\[F_a(t)=-\log(1-t)+\frac1a+O(1).\tag{3}\]
To see this without special-function assumptions, subtract \(-\log(1-t)\) from the integral. The resulting integral up to one is
\[\int_0^1\frac{v^{a-1}-1}{1-v}\,dv=\frac1a+\int_0^1\frac{v^a-1}{1-v}\,dv.\]
The last integral is bounded uniformly on \(0<a\le2\): for \(v\) away from one this is immediate, while near one its integrand tends to \(-a\). Omitting \([t,1]\) changes the difference integral by at most a constant times \(1-t\). This proves (3), including the small-\(a\) boundary relevant to the lowest Fourier modes.

Since \(1-t=Ne^{-cN}(1+O(Ne^{-cN}))\),
\[-\log(1-t)=cN-\log N+O(Ne^{-cN}).\tag{4}\]
Also \(\rho^{-\tau}=1+O_\tau(e^{-cN})\). Combining (2)--(4), uniformly over all \(0\le j<N\), yields
\[d_N\lambda_{N,j}=cN-\log N+\frac{N}{j+\tau}+O_{c,\tau}(1).\tag{5}\]
The diagonal normalization satisfies \(d_N=cN+O_\tau(1)\): indeed \(K_\tau(\rho)=1/\tau-\log(1-\rho)+\sum_{n\ge1}\rho^n[(n+\tau)^{-1}-n^{-1}]\), and the correction series is uniformly bounded because its coefficients are \(O_\tau(n^{-2})\). Division in (5) proves the displayed uniform spectral estimate.

For the operator limit, Fourier-conjugate \(G_N\), extend its diagonal by ones on modes \(j\ge N\), and compare with \(I+\operatorname{diag}_{j\ge0}(1/[c(j+\tau)])\). The first \(N\) diagonal differences are \(O_{c,\tau}(\log N/N)\) by the uniform estimate; the remaining supremum is at most \(1/[c(N+\tau)]\). Hence convergence holds in operator norm.

Finally, for distinct polygon vertices the argument of \(u=z_{N,k}\overline{z_{N,l}}\) has magnitude at least \(2\pi/N\) modulo a full turn, so \(|1-u|\ge C/N\). The absolutely summable difference between coefficients \(1/(n+\tau)\) and \(1/n\) shows \(K_\tau(u)=1/\tau-\log(1-u)+O_\tau(1)\). Thus \(|K_\tau(u)|=O_\tau(\log N)\), whereas \(K_\tau(\rho)=cN+O_\tau(1)\). This proves the coherence bound and completes the proof.

## Verification
The included `verify_dirichlet.py` checks discrete-Fourier eigenvalues against independent residue-series calculations for four small polygon sizes and three integer coefficient shifts. It also diagonalizes the closed-form logarithmic kernels for shifts one and two at two boundary-layer parameters and three larger sizes, checking strict mode order and the analytic \(O(\log N/N)\) asymptotics. The program reported 60 passing assertions. These finite tests corroborate, but do not replace, the uniform analytical argument in the proof.

## Relationship to prior work
Chalmoukis, *A note on simply interpolating sequences for the Dirichlet space* (first public version 2021), formulates normalized logarithmic Gram matrices, proves implications between interpolation conditions, and constructs examples with finitely many equispaced points on arcs. Its theorem and Example 2.3 do not state the full-circle, Fourier-resolved exponential-scale spectral limit above. Chalmoukis--Hartmann--Kellay--Wick (2019) study random radii and angles, and Chalmoukis--Dayan--Hartz (2023) characterize simply interpolating sequences in complete Pick spaces; neither inspected treatment supplies this finite-array critical operator-norm limit. Related sharp results for Szegő orbit frames concern a different (geometric-coefficient) kernel rather than the present logarithmic Dirichlet family. The general concept of Fourier-diagonalizing circulant matrices is classical and is not claimed as new; the claimed contribution is the uniform critical scaling, outlier spectrum, and coherence/frame-bound separation.

## Limitations
The theorem does not establish sharp constants in the finite-\(N\) remainder, treat \(c\) or \(\tau\) varying with \(N\), identify arbitrary nonregular configurations, or infer infinite-sequence interpolation from growing finite arrays. Full priority against all unpublished and inaccessible literature has not been established. The earlier Dirichlet literature provides the underlying framework, and some general estimates may imply weaker asymptotic bounds.

## References
1. N. Chalmoukis, *A note on simply interpolating sequences for the Dirichlet space*, arXiv:2111.05050 (public 2021-11-09), especially the normalized Gram definition and Example 2.3, https://arxiv.org/abs/2111.05050.
2. N. Chalmoukis, A. Hartmann, K. Kellay, B. Wick, *Random interpolating sequences in Dirichlet spaces*, arXiv:1904.12529 (public 2019-04-29), https://arxiv.org/abs/1904.12529.
3. N. Chalmoukis, A. Dayan, M. Hartz, *Simply interpolating sequences in complete Pick spaces*, arXiv:2306.13602 (public 2023-06-23), https://arxiv.org/abs/2306.13602.
