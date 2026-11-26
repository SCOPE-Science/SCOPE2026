# Two-defect bound-state threshold and separation scaling on a finite cycle

## Finding

Let \(C_N\) be the cycle with \(N\ge3\) vertices, let \(H_0\) be its unit-hopping nearest-neighbour adjacency operator, and set
\[
 H_N=H_0+V\bigl(|0\rangle\langle0|+|d\rangle\langle d|\bigr),
 \qquad V>0,\quad 1\le d<N.
\]
Use \([-2,2]\), the infinite-chain band, as the reference interval. A simple symmetric eigenvalue always lies strictly above \(2\). An additional, simple antisymmetric eigenvalue lies strictly above \(2\) if and only if
\[
 V>V_c(N,d):=\frac{2N}{d(N-d)}.
\]
At equality the antisymmetric eigenvalue is \(2\). There are no eigenvalues below \(-2\).

For a sequence of separations, put \(r_N=\min(d_N,N-d_N)/N\) and assume \(r_N\to\rho\in(0,1/2]\). If \(V_N=\lambda/N\) with \(\lambda>0\) fixed, then for all sufficiently large \(N\) there are two eigenvalues above \(2\) when \(\lambda>\lambda_c(\rho):=2/[\rho(1-\rho)]\), and one when \(\lambda<\lambda_c(\rho)\). At \(\lambda=\lambda_c(\rho)\) the exact criterion for a second eigenvalue strictly above \(2\) is \(r_N>\rho\), and it is at \(2\) if \(r_N=\rho\). In particular, for \(\rho=1/2\) and \(\lambda=8\) there is never a second eigenvalue strictly above \(2\), and the edge eigenvalue occurs precisely for exactly antipodal defects. For \(\rho<1/2\), the limiting fraction alone does not determine on which side of the critical separation a finite cycle lies.

The symmetric energy satisfies \(N^2(E_{+,N}-2)\to y_+^2\), for the unique \(y_+>0\) with \(\lambda=\Psi_+(y_+;\rho)\). When \(\lambda>\lambda_c(\rho)\), the antisymmetric energy satisfies the same limit with \(y_->0\) the unique solution of \(\lambda=\Psi_-(y_-;\rho)\), where
\[
 \Psi_\pm(y;\rho)=\frac{2y\sinh(y/2)}{\cosh(y/2)\pm\cosh((1/2-\rho)y)}.
\]
At \(\lambda=\lambda_c(\rho)\), along any subsequence with \(E_{-,N}>2\), one instead has \(N^2(E_{-,N}-2)\to0\). The limiting antipodal equations reduce to \(\lambda=2y_+\tanh(y_+/4)\) and \(\lambda=2y_-\coth(y_-/4)\).

## Assumptions and scope

The operator acts on \(\mathbb C^N\), with \((H_0\psi)_j=\psi_{j-1}+\psi_{j+1}\) and indices modulo \(N\). The two defects are distinct and have the same positive on-site potential. Reflection \(j\mapsto d-j\) exchanges them. This result is about eigenvalues at or above the upper edge \(2\), not about in-band resonances, unequal or negative strengths, disorder, or interacting particles.

## Proof

For \(E=2\cosh\kappa>2\), the cycle resolvent is obtained by summing the infinite-line kernel \(e^{-\kappa|j|}/(2\sinh\kappa)\) over period translates:
\[
 G_{0j}(E)=\frac{\cosh((N/2-j)\kappa)}{2\sinh\kappa\,\sinh(N\kappa/2)},\qquad 0\le j\le N.
\]
Put \(g_0=G_{00}(E)\), \(g_d=G_{0d}(E)\). The finite-rank determinant reduces to the two equations \(1=V(g_0+g_d)\) and \(1=V(g_0-g_d)\). The sums and differences are the resolvent quadratic forms for the normalized symmetric and antisymmetric defect vectors. They are strictly decreasing in \(E\), since the derivative of \((E-H_0)^{-1}\) is \(-(E-H_0)^{-2}\), and both tend to zero at infinity. The symmetric form diverges at \(2\). The antisymmetric form has the finite edge limit
\[
 \lim_{\kappa\downarrow0}\frac{\sinh(d\kappa/2)\sinh((N-d)\kappa/2)}{\sinh\kappa\sinh(N\kappa/2)}=\frac{d(N-d)}{2N}.
\]
Thus there is one root of each secular equation exactly under the conditions in the Finding. Since \(g_d>0\), the two roots cannot coincide, and each root has one-dimensional eigenspace. Positivity of the diagonal perturbation excludes eigenvalues below \(-2\).

For an eigenfunction at \(2\), summing the equation over the cycle yields \(\psi_0+\psi_d=0\). The equation off the defects gives a linear interpolation between the endpoint values along each arc. If both values are zero, the entire function is zero. Otherwise scale to \(\psi_0=1,\psi_d=-1\). The equation at \(0\) is then \(V=2/d+2/(N-d)=V_c\); the equation at the other defect follows by antisymmetry. This proves existence at equality, and excludes an edge eigenvalue at any other positive \(V\).

Write \(\kappa=y/N\). The finite-size functions are
\[
 \Psi_{\pm,N}(y)=\frac{2N\sinh(y/N)\sinh(y/2)}{\cosh(y/2)\pm\cosh((1/2-r_N)y)}.
\]
They are strictly increasing on \((0,\infty)\) by the preceding quadratic-form argument. They converge uniformly on compact positive intervals to \(\Psi_\pm(\cdot;\rho)\), which are therefore nondecreasing. The limiting functions are analytic there and unbounded as \(y\to\infty\) (both are asymptotic to \(2y\)), so neither can be constant on a positive interval; each is strictly increasing. Their limits at zero are \(0\) and \(\lambda_c(\rho)\), respectively, by the Taylor expansions of hyperbolic functions. For every claimed positive limiting root, bracket it on a compact positive interval. Convergence of both function values at the endpoints and monotonicity trap the finite-size root inside that bracket for all sufficiently large \(N\). Arbitrarily small brackets give convergence to that root.

The exact finite-size threshold in the scaled coupling is \(NV_c=2/[r_N(1-r_N)]\), tending to \(\lambda_c(\rho)\). On \((0,1/2]\) the threshold function is strictly decreasing. Thus at limiting equality the second root exists exactly for \(r_N>\rho\), and the edge state exactly for \(r_N=\rho\). For each \(\delta>0\), \(\Psi_-(\delta;\rho)>\lambda_c(\rho)\); eventually \(\Psi_{-,N}(\delta)>\lambda_c(\rho)\), so any above-edge antisymmetric root at this coupling lies in \((0,\delta)\). Its \(y\) tends to zero along every such subsequence. Finally \(N^2(2\cosh(y_N/N)-2)\to y^2\) when \(y_N\to y\), including \(y=0\). The antipodal equations follow from the hyperbolic half-angle identities.

## Verification

The analytic proof establishes the count, equality classification, and scaling for all stated sizes and sequences. The standalone `CHECKER.py` checks the resolvent against its Fourier sum for tested cycles, the antisymmetric edge limit, and numerical convergence for selected supercritical couplings. The recorded 40 numerical checks do not constitute a proof of the threshold or the limit and do not test the critical-sequence classification.

## Relationship to prior work

Exner [1, §2, equations (2.4)–(2.5)] gives the continuum circle Green kernel and the finite-point determinant for attractive point interactions. On a unit-length circle its two-equal-defect specialization at energy \(-y^2\) gives exactly \(\lambda=\Psi_\pm(y;\rho)\). These functions and their continuum threshold are thus not a separate new continuum spectral claim. The finite lattice uses \(2N\sinh(y/N)\) in place of \(2y\); its exact count, edge state and the rigorous discrete-to-continuum limit (including the critical finite-size distinction) are the focus. Joglekar et al. [2] treat imaginary parity-time-symmetric defects on an open chain and the onset of complex eigenvalues, a different transition. The accessible abstract of Bierman [3] treats impurity-band formation in a dilute many-impurity crystal, not the equal positive pair on a finite cycle. These comparisons do not settle historical priority across all tight-binding defect literature.

## Limitations

The separation limit requires a positive limiting fraction; the finite-cycle threshold still applies at bounded separations, but the stated scaling law does not. The result neither asserts a new general finite-rank method nor gives an energy expansion to higher orders at criticality.

## References

1. P. Exner, “An optimization problem for finite point interaction families,” arXiv:1906.01229 (2019), §2.
2. Y. N. Joglekar, D. Scott, M. Babbey, and A. Saxena, “Robust and fragile PT-symmetric phases in a tight-binding chain,” *Physical Review A* **82** (2010), 030103; arXiv:1008.2968.
3. A. Bierman, “Statistical Theory of Localized States of a Many-Impurity Crystal,” *Physical Review B* **1** (1970), 3402–3408, DOI: 10.1103/PhysRevB.1.3402 (abstract only).
