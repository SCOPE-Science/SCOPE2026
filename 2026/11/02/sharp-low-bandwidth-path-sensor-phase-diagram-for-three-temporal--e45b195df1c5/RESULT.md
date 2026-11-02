# Sharp low-bandwidth path-sensor phase diagram for three temporal frames

## Finding
For a normalized path of \(N\ge K\) vertices, \(K\in\{2,3,4\}\), take the first \(K\) low-frequency graph eigenvectors. Observe one vertex over \(K\) consecutive time steps of any spectral evolution whose first \(K\) eigenvalues are distinct. The determinant of the resulting \(K\)-by-\(K\) sampling Gramian has a completely classified optimal sensor location.

Write \(M=N-1\) and number vertices \(x=0,1,\ldots,M\). The complete lists of maximizing vertices are:

* \(K=2\): endpoints \(\{0,M\}\) for \(M=1,2\); every vertex for \(M=3\); exactly \(\{1,M-1\}\) for \(M\ge4\).
* \(K=3\): exactly \(\{0,M\}\) for \(2\le M\le5\); exactly \(\{1,M-1\}\) for \(M\ge6\).
* \(K=4\): every vertex for \(M=3\); endpoints only for \(M\in\{4,5,7\}\); \(\{0,2,4,6\}\) for \(M=6\); \(\{0,1,3,5,7,8\}\) for \(M=8\); exactly \(\{1,M-1\}\) for \(M\ge9\).

The determinant relative to an endpoint has the exact formula
\[
\frac{\det G_x}{\det G_0}=d_x^K\prod_{k=1}^{K-1}\cos^2\!\left(\frac{\pi kx}{M}\right),\qquad d_0=d_M=1,\quad d_x=2\ (0<x<M).
\]
The location classification and every equality case are independent of the particular injective spectral evolution. In particular, the optimal sensor can move from the endpoints to their immediate neighbors as the path grows, unlike the full-spectrum endpoint-optimal regime.

## Assumptions and scope
Let \(P_N\) be the unweighted path of \(N=M+1\) vertices with adjacency matrix \(A\) and degree matrix \(D\). Set \(S=D^{-1/2}AD^{-1/2}\) on ordinary Euclidean \(\mathbb C^N\). Let \(\lambda_k=\cos(\pi k/M)\), \(k=0,\ldots,M\), be the decreasing eigenvalues, and \(v_k\) corresponding orthonormal eigenvectors. Define \(E_K=\operatorname{span}\{v_0,\ldots,v_{K-1}\}\), with \(K\in\{2,3,4\}\) and \(K\le N\).

For any function \(h\) on the spectrum with pairwise distinct \(h(\lambda_0),\ldots,h(\lambda_{K-1})\), let \(T=h(S)\). At vertex \(x\), observe \(L_x:E_K\to\mathbb C^K\), \((L_x f)_t=\langle T^t f,e_x\rangle\) for \(0\le t<K\), and let \(G_x=L_x^*L_x\). The \(K\) samples are consecutive and the sensor is fixed. This is a \(D\)-optimal determinant criterion, not a claim of optimal smallest eigenvalue or condition number.

## Proof
**Spectral factorization.** The normalized path eigenvectors have, for \(0\le x\le M\), squared magnitudes
\[
|v_k(x)|^2=c_kd_x\cos^2(\pi kx/M),\quad
c_k=\begin{cases}1/(2M),&k=0\text{ or }M,\\1/M,&0<k<M.\end{cases}
\]
This follows from the cosine addition law at interior vertices and the degree-weighted endpoint equations; the discrete-cosine orthogonality gives the constants. In the eigenbasis, the sampling matrix factors as \(V_h\operatorname{diag}(\overline{v_k(x)})\), where \((V_h)_{t,k}=h(\lambda_k)^t\). Its Vandermonde determinant is nonzero under the stated distinctness assumption. Therefore
\[
\det G_x=\left|\prod_{0\le k<\ell<K}(h(\lambda_\ell)-h(\lambda_k))\right|^2\left(\prod_{k=0}^{K-1}c_k\right)d_x^K\prod_{k=1}^{K-1}\cos^2(\pi kx/M).
\]
At \(x=0\) the cosine factors and \(d_0\) equal one, proving the ratio formula. Reflection gives equality between \(x\) and \(M-x\).

**Two modes.** For an interior vertex, the determinant ratio is \(4\cos^2(\pi x/M)\). The largest interior value occurs precisely at \(x=1,M-1\); it is less than, equal to, or greater than one according as \(M\le2\), \(M=3\), or \(M\ge4\).

**Three modes.** For \(0\le\theta\le\pi/2\), put \(F_3(\theta)=|\cos\theta\cos2\theta|\). It decreases strictly on \([0,\pi/4]\). On \([\pi/4,\pi/2]\), writing \(u=\cos\theta\) gives \(F_3=u-2u^3\), whose maximum is \(2/(3\sqrt6)\). For \(M\ge6\), the nearest-interior angle is \(\theta=\pi/M\le\pi/6\), so \(F_3(\pi/M)\ge\sqrt3/4>2/(3\sqrt6)\), and its determinant ratio is at least \(8(\sqrt3/4)^2=3/2>1\). Thus exactly the two vertices adjacent to the endpoints maximize. At \(M=2,3,4,5\), the interior maxima are respectively \(0,1/4,0,1/4\), each below \(1/\sqrt8\), leaving only endpoints.

**Four modes.** With \(u=\cos^2\theta\), the signed cosine product is
\[
\cos\theta\cos2\theta\cos3\theta=P(u):=u(2u-1)(4u-3)=8u^3-10u^2+3u.
\]
The polynomial is strictly increasing for \(u\ge3/4\), corresponding to \(0\le\theta\le\pi/6\). On \(0\le u\le3/4\), its absolute value is at most \((10+7\sqrt7)/108<1/3\), by the derivative \(P'(u)=24u^2-20u+3\) and evaluation at its two critical points. For \(M\ge9\), \(\cos(\pi/M)>15/16\) (from \(\cos t\ge1-t^2/2\) and \(\pi^2<10\)); hence
\[
P(\cos^2(\pi/M))>P(225/256)=720225/2097152>1/3.
\]
Consequently no interior vertex farther from an endpoint can match the adjacent vertex, and the latter strictly beats endpoints since its ratio is \(16P^2>16/9>1\).

For the remaining \(M=3,4,5,6,7,8\), exact evaluations settle all ties. At \(M=3,6\), the angles \(\pi/3\) (as applicable) give \(P=1/4\), the endpoint-equality threshold; \(M=6\) has this only at \(x=2,4\). For \(M=8\), both \(\theta=\pi/8\) and \(3\pi/8\) give \(P=1/4\), yielding all four odd interior positions as ties. For \(M=4\), all interior values vanish. For \(M=5\), the two nonreflected interior values are \((1-\sqrt5)/16\) and \((1+\sqrt5)/16\), both of modulus below \(1/4\). For \(M=7\), examine \(x=1,2,3\): the first angle lies strictly between \(\pi/8\) and \(\pi/6\), so its \(P\) is between zero and \(1/4\); the second yields \(u\in(1/4,1/2)\), where \(P\) decreases from \(1/4\) to zero; the third has \(\cos(3\pi/7)=\sin(\pi/14)<1/4\), whence \(0<P(u)\le3u<3/16\). Thus endpoints alone win at \(M=7\). This exhausts all integers.

## Verification
The standalone `CHECK.py` reproduces the factored polynomial and small-path exact identities symbolically, checks every claimed maximizing location for \(1\le M<80\) and every admissible \(K\), and independently constructs the normalized adjacency and its spectral sampling matrices for \(1\le M\le20\). The script reports 917 finite comparisons and the symbolic identities. The proof above, not finite computation, covers all paths and every injective spectral evolution.

## Relationship to prior work
Bulai, Cabrelli, Cordero, Molter and Saliani (2026) introduce graph Paley–Wiener dynamical reconstruction and investigate finite path sensor placement numerically; the exact low-bandwidth determinant phase diagram here addresses that motivated setting. General graph dynamical sampling papers offer reconstruction and sample-selection machinery but do not, in their accessible descriptions, establish these sharp normalized-path formulas. A separately published full-spectrum result shows endpoint-optimality for all \(N\) eigenmodes; that conclusion does not imply the present classification because here the endpoint is strictly suboptimal at sufficiently large \(M\) for each of the three fixed bandwidths. The relevant 2026 preprint's complete text was inaccessible at review time, so overlap with material beyond its accessible abstract remains a concrete risk, not a proved absence.

## Limitations
The classification is complete only for the first two, three, or four normalized-path spectral modes and exactly the minimum matching number of consecutive temporal samples. It concerns one static sensor and determinant maximization, not smallest frame bounds, arbitrary graph geometries, larger bandwidths, irregular sample times, or evolving sensor locations. The full text of the 2026 motivating preprint was inaccessible, so a literature-overlap risk remains. No independent mathematical validation is claimed.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472, first posted 2026-09-21, https://arxiv.org/abs/2609.25472.
2. G. Parlangeli and G. Notarstefano, *On the observability of path and cycle graphs*, IEEE Conference on Decision and Control (2010), DOI:10.1109/CDC.2010.5717507. This addresses a different Laplacian-based observability problem.
3. *Universal endpoint optimality for dynamical sampling on normalized paths*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f (full-spectrum setting).
4. F. Wang, Y. Wang and G. Cheung, *A-Optimal Sampling and Robust Reconstruction for Graph Signals via Truncated Neumann Series*, arXiv:1803.03353 (2018), https://arxiv.org/abs/1803.03353.
