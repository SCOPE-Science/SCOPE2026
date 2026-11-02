# Cubic and quintic orthogonality resonances for regular simplex edge harmonics

## Finding
For every integer \(n\ge4\), consider the positive type-\(A_{n-1}\) root directions
\[
 X_n=\{r_{ij}=(e_i-e_j)/\sqrt2:1\le i<j\le n\}\subset S^{n-2}\subset H_n,
 \qquad H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
Write \(N=\binom n2\). For exactly-degree \(\ell\) spherical harmonics in \(H_n\), define the normalized sampling Gram matrix \(G_{n,\ell}\) indexed by \(X_n\) through the normalized zonal kernel \(P_{n,\ell}(\langle r_{ij},r_{kl}\rangle)\), where \(P_{n,\ell}(1)=1\). Then in degrees \(\ell=3\) and \(\ell=5\), respectively, its only eigenvalues are
\[
\begin{array}{c|cc}
\ell&a_\ell\ (\text{multiplicity }n-1)&b_\ell\ (\text{multiplicity }(n-1)(n-2)/2)\\ \hline
3&\dfrac{n-3}{8}&\dfrac{3(n+1)}{4(n-2)}\\[3pt]
5&\dfrac{n^2+135}{32n}&\dfrac{15(n^2-9)}{16n(n-2)}
\end{array}.
\]
Both are strictly positive for every \(n\ge4\). Consequently, evaluation onto the \(N\) edge samples is surjective in each of these exact harmonic degrees. The sharp squared condition number of its nonzero singular values is \(\max(a_\ell,b_\ell)/\min(a_\ell,b_\ell)\).

Within degrees three and five, the normalized zonal kernel sections at distinct edge directions are pairwise orthogonal **if and only if**
\[
(\ell,n)=(3,11),\qquad (\ell,n)=(5,5),\qquad (\ell,n)=(5,27).
\]
At these parameter pairs the normalized Gram is the identity. At \(n=11,\ell=3\), this gives \(55\) mutually orthogonal cubic harmonic evaluation representers in the \(210\)-dimensional cubic harmonic space. At \(n=27,\ell=5\), the analogous set contains \(351\) orthogonal representers.

There is also an exact infinite ladder at the type-\(A_4\) configuration: for \(n=5\), the normalized evaluation kernels are mutually orthogonal for all degrees \(\ell\ge0\) **exactly when** \(\ell\equiv5\pmod6\). In each such degree an arbitrary collection of edge values is interpolated with no matrix inversion.

## Assumptions and scope
The ambient real Euclidean space is \(H_n\), of dimension \(d=n-1\), and its unit sphere is \(S^{n-2}\). Fix the representatives \(i<j\) of the antipodal root pairs; the full root set contains both \(r_{ij}\) and \(-r_{ij}\). For odd harmonics the values at these antipodes are negatives, so the \(N\) sample coordinates encode all parity-compatible data. Every Gram statement is about the kernel normalized to have diagonal entries one. With an orthonormal basis of harmonics for normalized surface measure, the unnormalized evaluation Gram is \(h_{n,\ell}G_{n,\ell}\), where \(h_{n,\ell}\) is the harmonic-space dimension; this scalar does not affect ranks or condition numbers. This finding classifies orthogonality for degrees three and five across all \(n\ge4\), and for all degrees at \(n=5\). It does **not** classify all orthogonality resonances in all other harmonic degrees and dimensions.

## Proof
For \(d=n-1\), the normalized zonal polynomials satisfy \(P_{n,0}(t)=1\), \(P_{n,1}(t)=t\), and
\[
P_{n,\ell+1}(t)=\frac{(2\ell+n-3)tP_{n,\ell}(t)-\ell P_{n,\ell-1}(t)}{\ell+n-3}.
\]
The Gegenbauer addition formula makes the matrix of values of \(P_{n,\ell}\) on the sphere a Gram matrix of normalized reproducing-kernel vectors in the degree-\(\ell\) harmonic space. In particular, it is positive semidefinite.

Let \(B\) be the \(n\)-by-\(N\) oriented incidence matrix of the complete graph: the column indexed by \(ij\), with \(i<j\), is \(e_i-e_j\). Since \(\langle r_{ij},r_{kl}\rangle=(B^\top B)_{ij,kl}/2\), distinct edge directions have inner products \(0\) or \(\pm1/2\). For odd \(\ell\), the normalized Gegenbauer polynomial is odd and \(P_{n,\ell}(0)=0\). Setting \(w_{n,\ell}=P_{n,\ell}(1/2)\), one obtains the exact matrix identity
\[
G_{n,\ell}=(1-2w_{n,\ell})I_N+w_{n,\ell}B^\top B.
\]
The complete-graph incidence identity \(BB^\top=nI_n-J_n\) implies that \(\Pi=B^\top B/n\) is an orthogonal projector of rank \(n-1\). Therefore
\[
G_{n,\ell}=a_{n,\ell}\Pi+b_{n,\ell}(I_N-\Pi),\quad
 a_{n,\ell}=1+(n-2)w_{n,\ell},\quad b_{n,\ell}=1-2w_{n,\ell}.
\]
For degrees three and five, the normalized Gegenbauer recurrence yields
\[
w_{n,3}=\frac{n-11}{8(n-2)},\qquad
w_{n,5}=\frac{(n-5)(n-27)}{32n(n-2)}.
\]
Substitution and simplification give the two stated spectra. All denominators are nonzero for \(n\ge4\), and the displayed numerators are strictly positive, proving surjectivity and the sharp condition-number formula. Since both spectral multiplicities are positive, the matrix is a scalar multiple of the identity exactly when \(w_{n,\ell}=0\); its diagonal is one, so the scalar must be one. Factoring the two expressions for \(w\) establishes precisely the three cubic/quintic orthogonality pairs.

For any prescribed sample vector \(y\in\mathbb C^N\), the coefficients
\[
c=\frac1{b_{n,\ell}}y+\left(\frac1{a_{n,\ell}}-\frac1{b_{n,\ell}}\right)\Pi y
\]
produce the exact harmonic interpolant \(f(x)=\sum_{i<j}c_{ij}P_{n,\ell}(\langle x,r_{ij}\rangle)\). At the resonance parameters \(a=b=1\), this reduces to \(c=y\).

For \(n=5\), the ambient sphere has dimension three and \(P_{5,\ell}(t)=U_\ell(t)/(\ell+1)\), where \(U_\ell(\cos\theta)=\sin((\ell+1)\theta)/\sin\theta\). Hence
\[
P_{5,\ell}(1/2)=\frac{\sin((\ell+1)\pi/3)}{(\ell+1)\sin(\pi/3)}.
\]
For odd \(\ell\), the above Gram identity applies; this expression vanishes exactly when \(\ell\equiv5\pmod6\). For even \(\ell\), disjoint edges exist and their inner product is zero, while \(P_{5,\ell}(0)=(-1)^{\ell/2}/(\ell+1)\neq0\), so the Gram cannot be diagonal. This proves the exact infinite periodic classification.

## Verification
The included standalone script `check_simplex_resonances.py` uses only the Python standard library and `fractions.Fraction`. Run `python3 check_simplex_resonances.py`. It independently calculates edge inner products and Gegenbauer recurrence values, checks both spectral branches and complete-graph projector identities, replays exact interpolation on deterministic data, tests the quintic resonant case \(n=27\), and checks the \(n=5\) periodic formulas through degree \(120\). It passed in the supplied package environment. Those finite tests corroborate the analytic identities; they are not proofs of the universal claims.

## Relationship to prior work
Delsarte, Goethals, and Seidel (1977) developed the classical Gegenbauer/addition-formula approach to spherical configurations; Zhu, Bannai, Bannai, Kim, and Yu (arXiv:1507.05373, first public version 2015-07-20) study spherical harmonic-index designs and Gegenbauer zeros. These foundational frameworks are acknowledged. The claim here is the particular all-size cubic/quintic two-level interpolation law for oriented regular-simplex edges, the three exact resonant parameter pairs, the explicit cardinal interpolation operator, and the infinite periodic degree ladder at \(n=5\). No claim is made to have invented Gegenbauer kernels, association schemes, or root-system geometry.

## Limitations
Independent mathematical validation has not been performed. The originality review is bounded by inspected accessible sources and search evidence; it is not proof of novelty. The complete 1977 Delsarte–Goethals–Seidel text was not accessible in the consulted channels. An equivalent earlier treatment through a Johnson-scheme harmonic embedding remains possible. No all-degree, all-dimension classification outside the stated degree restrictions is claimed.

## References
1. Y. Zhu, E. Bannai, E. Bannai, K.-T. Kim, W.-H. Yu, *More on spherical designs of harmonic index t*, arXiv:1507.05373v1 (public 2015-07-20), https://arxiv.org/abs/1507.05373 .
2. P. Delsarte, J. M. Goethals, J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388, https://doi.org/10.1007/BF03187604 .
