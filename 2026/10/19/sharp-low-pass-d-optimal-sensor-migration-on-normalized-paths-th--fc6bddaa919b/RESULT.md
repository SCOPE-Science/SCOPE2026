# Sharp low-pass D-optimal sensor migration on normalized paths through four modes

## Finding
For the unweighted path on \(N\ge3\) vertices \(0,\ldots,N-1\), let \(\mathcal L\) be its symmetric normalized graph Laplacian. Let \(E_m\) be the subspace spanned by the \(m\) eigenvectors having the smallest eigenvalues, where \(2\le m\le\min\{4,N\}\). Choose a spectral evolution \(T=h(\mathcal L)\) whose values on these \(m\) eigenvalues are pairwise distinct. For a vertex \(j\), the observation matrix \(\mathcal O_{j,m}\) maps a signal in \(E_m\) to its values at \(j\) at times \(0,1,\ldots,m-1\) under the successive powers of \(T\). Put \(D_{j,m}=\det(\mathcal O_{j,m}^{*}\mathcal O_{j,m})\).

The **complete optimal single-vertex placement classification**, valid simultaneously for every such evolution, is as follows. Each displayed set gives **all** vertices maximizing \(D_{j,m}\).

| Number of low-frequency modes | Path sizes | All maximizing vertex indices |
| --- | --- | --- |
| \(m=2\) | \(N=3\) | \(\{0,N-1\}\) |
| \(m=2\) | \(N=4\) | all vertices |
| \(m=2\) | \(N\ge5\) | \(\{1,N-2\}\) |
| \(m=3\) | \(3\le N\le6\) | \(\{0,N-1\}\) |
| \(m=3\) | \(N\ge7\) | \(\{1,N-2\}\) |
| \(m=4\) | \(N=4\) | all vertices |
| \(m=4\) | \(N\in\{5,6,8\}\) | \(\{0,N-1\}\) |
| \(m=4\) | \(N=7\) | \(\{0,2,4,6\}\) |
| \(m=4\) | \(N=9\) | \(\{0,1,3,5,7,8\}\) |
| \(m=4\) | \(N\ge10\) | \(\{1,N-2\}\) |

In particular, the first strict four-mode movement from endpoint sensing to first-interior sensing occurs at \(N=10\). The determinant ratio for either first-interior sensor satisfies the sharp limit
\[
\lim_{N\to\infty}\frac{D_{1,4}}{D_{0,4}}=16.
\]
The exceptional ties at path sizes \(N=7,9\) are exact, not numerical approximations.

## Assumptions and scope
The path has unit edges, no loops and real symmetric normalization \(\mathcal L=I-D^{-1/2}AD^{-1/2}\); its endpoint degrees are one and every other degree is two. The graph-signal space is complex (the result holds over the real field as well). The low-pass eigenvalues are simple, so the associated spectral subspace is well-defined. The \(m\) evolution multipliers are assumed pairwise distinct. The observation uses one vertex and exactly \(m\) successive times, beginning at zero, with equally weighted observations; it is the determinant of the finite information Gramian, not a minimum singular value or condition number. The result concerns only the lowest two, three or four graph Fourier modes.

## Proof
Write \(L=N-1\) and \(d_j\) for the degree of vertex \(j\). The eigenvalues of \(\mathcal L\) are \(\nu_k=1-\cos(\pi k/L)\), for \(0\le k\le L\). For \(1\le k<L\) take the orthonormal eigenvectors
\[
\psi_k(j)=\sqrt{\frac{d_j}{L}}\cos\frac{\pi kj}{L},\qquad
\psi_0(j)=\sqrt{\frac{d_j}{2L}},\qquad
\psi_L(j)=(-1)^j\sqrt{\frac{d_j}{2L}}.
\]
These follow from the cosine addition formula and the weighted finite cosine orthogonality identity. At an endpoint, \(\psi_k(0)\ne0\) for every \(k\). Put \(\lambda_k=h(\nu_k)\). In the Fourier eigenbasis, the measurement matrix is \(\mathcal O_{j,m}=[\lambda_k^t\psi_k(j)]_{0\le t,k<m}\). Its Vandermonde factorization gives
\[
D_{j,m}=\prod_{0\le a<b<m}|\lambda_a-\lambda_b|^2\prod_{k=0}^{m-1}|\psi_k(j)|^2.
\]
Hence the ratio to either endpoint removes every dependence on \(h\). For each interior vertex, including the small cases where \(m=N\), the ratios of eigenvector magnitudes to their endpoint values all equal \(\sqrt2\,|\cos(\pi kj/L)|\) for positive modes, and equal \(\sqrt2\) for the constant mode. Consequently
\[
\boxed{\displaystyle
\sqrt{\frac{D_{j,m}}{D_{0,m}}}
=2^{m/2}\prod_{k=1}^{m-1}\left|\cos\frac{\pi kj}{L}\right|,
\quad 1\le j\le L-1.}
\]
This remains valid for \(m=N\) because the terminal alternating eigenvector has the same endpoint/interior degree-ratio law. Both endpoints have determinant ratio one.

For \(m=2\), put \(x=\pi j/L\) and use reflection symmetry \(j\mapsto L-j\). For \(0<x\le\pi/2\) the interior ratio above is \(2\cos x\), which decreases strictly with \(x\). Its largest interior value is \(2\cos(\pi/L)\), which is below, equal to or above one for \(L=2\), \(L=3\) or \(L\ge4\), respectively. This proves the first three rows.

For \(m=3\), on the same half-interval put \(u=\cos x\in[0,1]\). Up to the constant \(2\sqrt2\), the interior ratio is \(|u(2u^2-1)|\). On \(u\in[0,1/\sqrt2]\) its maximum is exactly \(2/(3\sqrt6)\); on \(u\in[1/\sqrt2,1]\) it is strictly increasing. For \(L\ge6\), the first positive grid angle satisfies \(x_1=\pi/L\le\pi/6\); its product \(\cos x_1\cos2x_1\) is at least \(\sqrt3/4>2/(3\sqrt6)\). Thus \(j=1\) (and by reflection \(j=L-1\)) uniquely maximizes among interior sites, and its ratio exceeds one, since at \(L=6\) it equals \(\sqrt{3/2}>1\). Direct exact cosine evaluation for \(L=2,3,4,5\) shows all interior values below one. This establishes the three-mode classification.

For \(m=4\), write \(z=\cos^2x\). The triple cosine product obeys the exact identity
\[
\cos x\cos2x\cos3x
=z(2z-1)(4z-3)=:p(z),\quad p(z)=8z^3-10z^2+3z.
\]
Here \(z\) ranges from zero to one and is strictly decreasing with the grid index \(j\) on the half-path. The stationary points of \(p\) are \(z_{\pm}=(5\pm\sqrt7)/12\). Direct evaluation at the critical points and at \(0,1/2,3/4\) gives the exact bound
\[
\max_{0\le z\le3/4}|p(z)|=\frac{10+7\sqrt7}{108}<\frac{21}{64}=p(7/8).
\]
On \([3/4,1]\), \(p\) is strictly increasing. For \(L\ge9\), the first grid value \(z_1=\cos^2(\pi/L)\) satisfies \(z_1\ge\cos^2(\pi/9)>7/8\): indeed \(\cos(2\pi/9)>1-(2\pi/9)^2/2>3/4\), using \(\pi^2<10\). Thus \(p(z_1)>21/64\), while all grid values below \(3/4\) are bounded by the strictly smaller extremum. For larger grid values monotonicity makes \(z_1\) uniquely best. Hence first-interior sensors uniquely maximize among interior sites, and their ratio \(4p(z_1)>4(21/64)>1\). Reflection gives exactly \(j=1,L-1\).

It remains to check the finite threshold values \(L=3,4,5,6,7,8\). Substitution into \(4|\cos x\cos2x\cos3x|\) yields the exact interior maxima \(1,0,(1+\sqrt5)/4,1,1/2,1\), respectively. Their maximizing interior sites are, respectively, both interior sites; none positive; \(j=2,3\); \(j=2,4\); all interior sites; and the odd interior sites. Comparing with endpoint ratio one proves the exceptional optimizer rows. Finally, as \(L\to\infty\) all three cosines at \(x_1=\pi/L\) tend to one; therefore the determinant ratio, which is the square of the amplitude ratio, tends to \(4^2=16\).

## Verification
The standalone checker `verify_path_sampling.py` computes all eigenvector-ratio products and maximizers over a supplementary range of path sizes, tests direct complex-heat observation matrices against the analytic Vandermonde determinant, and checks the exact stationary-polynomial identities. The proof, not finite sampling, establishes the all-size result. Run the checker with `python verify_path_sampling.py` using Python 3 and its standard library.

## Relationship to prior work
Bulai, Cabrelli, Cordero, Molter and Saliani (arXiv:2609.25472v1, first public September 21, 2026) motivate normalized-Laplacian dynamical sampling on graph Paley–Wiener spaces and describe numerical finite-path experiments on iteration counts and sensor placement; the complete manuscript could not be materially inspected through available lawful access, so overlap in its uninspected sections remains a genuine priority risk. An earlier published theorem titled *Universal endpoint optimality for dynamical sampling on normalized paths* treats **full-spectrum** recovery with \(N\) modes and \(N\) time samples, establishing endpoint optimality in that fundamentally different regime; its full result and proof were compared. Here the band is held to at most four **lowest** modes as the path grows, and the optimum moves to the first interior vertices, with exact exceptional ties. The published result *Sharp spectral-demixed two-sensor frame bounds on finite cycles* concerns cycle graphs, two sensors and a different recovery objective. Huang, Needell and Tang (2024) analyze randomized space–time graph recovery but do not provide the deterministic small-band path classifications proved here.

## Limitations
The proof optimizes the determinant for one vertex and exactly as many consecutive observations as active modes; it does not optimize conditioning, minimum frame singular value, weighted-noise criteria, arbitrary time schedules or simultaneous sensors. The low-pass threshold \(m\le4\) is essential to this classification, and no larger-band conclusion follows from it. The motivating 2026 preprint could not be read in complete full text, so bibliographic priority remains uncertain. No independent expert or formal verification is claimed.

## References
1. I. M. Bulai, C. Cabrelli, E. Cordero, U. Molter and S. Saliani, *Dynamical Sampling in Graph Paley–Wiener Spaces*, arXiv:2609.25472v1, September 21, 2026, https://arxiv.org/abs/2609.25472.
2. *Universal endpoint optimality for dynamical sampling on normalized paths*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f.
3. *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-spectral-demixed-two-sensor-frame-bounds-on-finite-cycles--b03d8e4c7818.
4. Y. Huang, D. Needell and S. Tang, *Robust estimation of smooth graph signals from randomized space–time samples*, IMA Journal of Information and Inference 13 (2024), https://academic.oup.com/imaiai/article/13/2/iaae012/7682117.
