# Exact covariance spectrum and a sharp extremal-mode transition for wheel spanning-tree sampling

## Finding
For each integer \(n\ge3\), let \(W_{n+1}\) have hub \(h\), rim vertices \(j\in\mathbb Z/n\mathbb Z\), spokes \(s_j=\{h,j\}\), and rim edges \(r_j=\{j,j+1\}\). Draw a spanning tree \(T\) uniformly, set \(X_e(T)=\mathbf 1_{\{e\in T\}}\), and let \(\Sigma_n\) be the \(2n\)-by-\(2n\) covariance/Gram matrix of the centered functions \(X_e-\mathbb EX_e\), ordered by all spokes followed by all rim edges.

Put
\[
\rho=\frac{3-\sqrt5}{2},\quad r=\rho^2,\quad t=\rho^n,\quad
 g_n=\frac{1+t}{\sqrt5(1-t)},\quad c_n=\frac{(1+t)(1-r^2)}{5(1-t)},
\]
\[
 a_n=g_n-\frac{c_n}{(1-r)^2}-\frac{2nt}{5(1-t)^2},\quad
 y_k=\left|\cos\frac{\pi k}{n}\right|,\quad d_k=(1+r)^2-4r y_k^2.
\]
Then the **complete spectrum**, with repetitions indexed by \(k\), is
\[
\boxed{\operatorname{Spec}(\Sigma_n)=\{0,\ 2a_n\}\ \cup\
\bigcup_{k=1}^{n-1}\left\{
 g_n-\frac{c_n(1+2y_k/3)}{d_k},\quad
 g_n-\frac{c_n(1-2y_k/3)}{d_k}
\right\}.}
\]
The only null direction is the all-edges constant vector. Write the two displayed nonzero-frequency eigenvalues as \(\lambda_{k,-}<\lambda_{k,+}\), and set \(\lambda_{1,-}=g_n-c_n(1+2\cos(\pi/n)/3)/d_1\) and \(\lambda_{1,+}=g_n-c_n(1-2\cos(\pi/n)/3)/d_1\).

The smallest positive eigenvalue is **always** \(\lambda_{1,-}\), with a tie with \(2a_n\) only when \(n=3\). The largest eigenvalue changes extremizing Fourier sector **exactly between \(n=8\) and \(n=9\)**:
\[
\boxed{\lambda_{\max}(\Sigma_n)=
\begin{cases}\lambda_{1,+},&3\le n\le8,\\2a_n,&n\ge9.\end{cases}}
\]
Consequently, its sharp squared nonzero-singular-value condition number is the ratio of this largest eigenvalue to \(\lambda_{1,-}\). Moreover,
\[
 \lambda_{1,-}=\frac{\pi^2}{\sqrt5\,n^2}+O(n^{-4}),\qquad
 \lambda_{\max}=\frac4{5\sqrt5}+O(n\rho^n),\qquad
 \boxed{\kappa_n^2=\frac4{5\pi^2}n^2+O(1)}.
\]
The centered spoke and rim indicator families, despite having different individual means, have **exactly identical within-family covariance blocks**. This symmetry holds at every finite \(n\), not only asymptotically.

## Assumptions and scope
All edges have unit weight; the probability measure is uniform over every spanning tree of the simple wheel. Covariance uses the **probability** normalization (not a sum over trees). The results concern centered one-edge indicator functions and their full \(2n\)-coordinate Gram matrix. There is one deterministic linear relation \(\sum_eX_e=n\). The graph convention is a rim of size \(n\) plus a hub; all stated indices begin at \(n=3\). Eigenvalue multiplicities are those of the indicated indexed multiset; coincident values are counted with their repetitions. No claim is made about higher-order edge products, weighted wheels, or arbitrary planar graphs.

## Proof
**1. Transfer-current reduction.** Ground the hub. The reduced Laplacian on rim vertices is \(L=3I-S-S^{-1}\), where \(S\) is cyclic shift. Its inverse \(H\), computed by the recurrence \(3H_m-H_{m-1}-H_{m+1}=\mathbf1_{\{m=0\}}\), has entries
\[
 H_{ij}=g_{i-j},\qquad g_m=\frac{\rho^{\bar m}+\rho^{n-\bar m}}{\sqrt5(1-\rho^n)},\quad 0\le\bar m<n.
\]
Here \(\rho+\rho^{-1}=3\), \(\rho^{-1}-\rho=\sqrt5\), and the indices are cyclic. Orient spoke \(s_j\) from the grounded hub to \(j\), and orient rim edge \(r_j\) from \(j\) to \(j+1\). The transfer-current matrix is \(K=B^{\mathsf T}HB\), where the columns of \(B\) are \(e_j\) for spokes and \(e_j-e_{j+1}\) for rim edges; changing orientations never affects the squared entries used below. Burton--Pemantle's two-edge determinant identity gives
\[
 \Sigma_{ef}=\mathbf1_{\{e=f\}}K_{ee}-K_{ef}^2.
\]
In particular \(K_{s_0s_m}=g_m\), \(K_{s_0r_m}=g_m-g_{m+1}\), and
\[
 K_{r_0r_m}=2g_m-g_{m-1}-g_{m+1}=\mathbf1_{\{m=0\}}-g_m.
\]
Thus \(\Sigma_{s_0s_m}=\Sigma_{r_0r_m}\) for every \(m\). The common cyclic block has first row \(\mathbf1_{\{m=0\}}g_0-g_m^2\); the spoke--rim block has first row \(-(g_m-g_{m+1})^2\). This proves the asserted finite spoke--rim covariance symmetry.

**2. Exact finite Fourier transform.** Fourier-diagonalize both circulant blocks at \(z=e^{-2\pi i k/n}\). Put \(r=\rho^2\), \(t=\rho^n\). For \(k\ne0\), expanding \(g_m^2\) into the three geometric terms and using \(z^n=1\) gives
\[
 \sum_{m=0}^{n-1}g_m^2z^m=\frac{c_n}{1-2r\cos(2\pi k/n)+r^2}.
\]
Similarly,
\[
 \sum_{m=0}^{n-1}(g_m-g_{m+1})^2z^m
 =\frac{2c_n}{3}\frac{1+z^{-1}}{2[1-2r\cos(2\pi k/n)+r^2]}.
\]
The factor \(2/3\) follows from the exact identity \(2(1-\rho)^2/(1+\rho^2)=2/3\). Since \(|1+z^{-1}|=2y_k\), the associated Hermitian two-by-two block has equal diagonal entries \(g_n-c_n/d_k\) and off-diagonal absolute value \(2c_ny_k/(3d_k)\). Its two eigenvalues are exactly \(\lambda_{k,\pm}\).

For \(k=0\), the constant term \(2t\) in \(g_m^2\) survives the Fourier sum, yielding common diagonal entry \(a_n\). Every spanning tree has \(n\) edges, so the global all-edges vector is a covariance null vector; the zero-mode block must therefore have eigenvalues \(0\) and \(2a_n\). This proves the complete list.

**3. Positivity and the extremizing sectors.** For \(0\le y<1\), the quantity \((1+2y/3)/((1+r)^2-4ry^2)\) is strictly increasing in \(y\). Its limit at \(y=1\) gives \(\lambda_-(1)=0\); consequently \(\lambda_{k,-}>0\) for all nonzero \(k\), and \(\lambda_{1,-}\) is the smallest among them. The quantity \((1-2y/3)/((1+r)^2-4ry^2)\) is strictly decreasing in \(y\): its derivative has numerator proportional to \(-(1+r)^2+12ry-4ry^2\), which is negative for \(0\le y\le1\), using \(1-6r+r^2=r>0\). Thus the largest eigenvalue among all nonzero-frequency blocks is \(\lambda_{1,+}\). Finally \(a_n>0\), because hub degree is not constant across wheel spanning trees.

For completeness, the comparison with the zero-frequency positive level is reduced to a one-variable inequality. Let \(y=\cos(\pi/n)\), \(D(y)=(1+r)^2-4ry^2\), and \(c_\infty=(1-r^2)/5\). The limiting positive zero-mode level equals \(L_\infty=4/(5\sqrt5)\). Algebra gives
\[
 2a_n-\lambda_{1,+}
 =\frac{1+t}{1-t}\left[
 \frac{2c_\infty(1-y)(1-4r+r^2-2ry)}{3D(y)(1-r)^2}
 -\frac{4nt}{5(1-t^2)}\right].
\]
The first term in brackets is positive. Its comparison with the second term is **negative for \(3\le n\le8\) and positive for \(n=9,10\)**, as witnessed by the rational-interval evaluations in `verify_wheel.py`: those evaluations use the Machin arctangent identity, alternating-series enclosures for \(\pi\) and cosine, and exact rational bounds for \(\sqrt5\). For every \(n\ge11\), use \(1-\cos(\pi/n)\ge2/n^2\), \(1-4r+r^2-2ry\ge r\), and \(D(y)\le(1+r)^2\). The first term is then at least
\[
 \frac{4c_\infty r}{3(1+r)^2(1-r)^2n^2}.
\]
This exceeds \(4n\rho^n/[5(1-\rho^{2n})]\) at \(n=11\), as confirmed by exact rational inequalities in the checker, and the inequality persists thereafter because \(1-\rho^{2n}\) increases and \(n^3\rho^n\) decreases for \(n\ge4\). This proves the sharp switch. The analogous comparison \(2a_n\ge\lambda_{1,-}\) holds with equality only at \(n=3\): check \(3\le n\le10\) by the same rational enclosures; for \(n\ge11\), the explicit bounds \(2a_n>0.35\) and \(\lambda_{1,-}<0.08\) follow from \(y\ge9/10\) and the exponentially small correction.

**4. Conditioning asymptotics.** For nonzero Fourier frequencies, \(\lambda_{k,\pm}\) is \((1+t)/(1-t)\) times the corresponding infinite-cycle symbol. At \(y=\cos(\pi/n)\), expansion of the lower symbol about \(y=1\) gives \(\lambda_{1,-}=(\sqrt5/20)(2\pi/n)^2+O(n^{-4})+O(\rho^n)\). For \(n\ge9\), \(2a_n=4/(5\sqrt5)+O(n\rho^n)\). Division proves the asserted condition-number law, including its exact leading constant.

## Verification
The included Python-standard-library script `verify_wheel.py` has been executed from this package. It (i) exhaustively enumerates all wheel spanning trees for rim sizes \(3\le n\le8\), (ii) compares their **exact rational** covariances with an independently inverted grounded Laplacian and the transfer-current formula, (iii) numerically checks the complete analytic spectrum through size 60, and (iv) supplies rational-interval certificates for the finite extremal inequalities and the large-size cutoff bound. It prints `RATIONAL_INTERVAL_CERTIFICATES_OK` and `CHECK_OK`. Finite tests alone do not prove the all-size theorem; the recurrence, Fourier formulas, monotonicity, and analytic comparison above do.

## Relationship to prior work
Burton and Pemantle's transfer-current theorem (original 1993 article, day-verified open arXiv posting 2004-04-02) supplies general spanning-tree inclusion determinants, hence the starting covariance formula. The standard wheel Laplacian and its Fourier diagonalization are classical. These ingredients alone do **not** state the equal spoke/rim covariance-block identity, the explicit all-size two-band eigenvalue list, the exact change of extremizing mode at nine rim sites, or the quadratic sharp conditioning constant. An earlier paper deriving these quantities using another normalization or the cycle Green kernel would cover the contribution; no such statement was found in the bounded comparisons.

## Limitations
Only uniform spanning trees on simple wheels are covered. The spectral result is exact for every \(n\ge3\), but it is not an independent audit or a statement about weighted wheels. The wheel-specific diagonalization uses the general transfer-current theorem as an acknowledged premise. No claim is made that the classical Green kernel, general covariance determinant formula, or wheel spanning-tree counts are new. Equivalent prior calculations in specialized electrical-network or spectral sampling literature may exist.

## References
1. R. Burton and R. Pemantle, *Local Characteristics, Entropy and Limit Theorems for Spanning Trees and Domino Tilings via Transfer-Impedances*, Annals of Probability 21 (1993), 1329–1371; publicly accessible preprint arXiv:math/0404048v1 (2004-04-02), especially Theorem 1.1, Theorem 4.2, and Section 4.
2. Y. Zhang, X. Liu, and X. Yong, *Which wheel graphs are determined by their Laplacian spectra?*, Computers & Mathematics with Applications 58 (2009), 1887–1890, DOI:10.1016/j.camwa.2009.07.028 (wheel Laplacian context, not an assertion about spanning-tree covariance).
3. F. Chung, *Spectral Graph Theory*, CBMS Regional Conference Series 92, AMS (1997) (standard finite Fourier/Laplacian background).
