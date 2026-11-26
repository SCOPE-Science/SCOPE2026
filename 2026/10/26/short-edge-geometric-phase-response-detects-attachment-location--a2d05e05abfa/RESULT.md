# A short-edge spectral response distinguishes endpoint and hub attachment

## Finding

Fix \(a,b>0\), \(a\ne b\), and write \(S=a+b\). Compare a metric path whose endpoint edge has length \(\varepsilon\) and whose two other edges have lengths \(a,b\), with a three-arm metric star of arm lengths \(\varepsilon,a,b\). For the normalized first positive eigenstate, write
\[
 E_1(\varepsilon)=\int_{-1/2}^{1/2}(\xi^2-1/4)|g_1(\xi;\varepsilon)|^2\,d\xi,
 \qquad A_{11}(\varepsilon)=\varepsilon E_1'(\varepsilon),
\]
where \(g_1(\xi;\varepsilon)=\sqrt{\varepsilon}\,\psi_\varepsilon(\varepsilon(\xi+1/2))\) is the unitary rescaling of the eigenfunction on the short edge. Then as \(\varepsilon\downarrow0\),
\[
 A_{11}^{\rm path}=-\frac{\varepsilon}{3S}+O(\varepsilon^2),\qquad
 A_{11}^{\rm star}=-\frac{\varepsilon}{3S}\cos^2(\pi a/S)+O(\varepsilon^2).
\]
The star-to-path ratio tends to \(\cos^2(\pi a/S)\in(0,1)\). Thus this local eigenfunction observable distinguishes the two attachment locations despite the common edge-length multiset.

The same ratio applies to the diagonal quadratic term of a specific *length-cycle functional* from the first preprint [1], as defined below. This is not a ratio of Berry phases in the published convention [2].

## Assumptions and scope

Use the edge Laplacians \(-d^2/dx^2\), Neumann conditions at leaves, and continuity and the Kirchhoff derivative condition at internal vertices. Normalize in the original metric-graph \(L^2\) space. The lengths \(a,b\) are held fixed, and no uniform estimate as \(a\) approaches \(b\) is assumed. The length-cycle functional uses a Taylor expansion in modulation amplitude at fixed positive short length before sending the short length to zero.

## Proof

On the path, degree-two Kirchhoff conditions give a single Neumann interval of length \(S+\varepsilon\). The short-edge expression is the restriction of the normalized first cosine eigenfunction. On rescaling its squared modulus is \(\varepsilon\) times an analytic function of \(\varepsilon\) with value \(2/S\) at zero, uniformly for \(|\xi|\le 1/2\).

For the star, on an arm of length \(\ell_j\), the Neumann condition at its leaf gives the form \(C_j\cos(k(\ell_j-x))\) with \(x\) measured outwards from the hub. For \(k>0\), continuity and the Kirchhoff condition have a nonzero solution exactly when the pole-free secular determinant vanishes:
\[
 D(k,\varepsilon)=\sin(k\varepsilon)\cos(ka)\cos(kb)+\cos(k\varepsilon)\sin(kS)=0.
\]
Indeed, before specializing the lengths, the determinant is the sum of \(\sin(k\ell_j)\) times the product of the two other cosines; this follows by eliminating the common value at the hub in the homogeneous linear equations. The determinant does not divide by any cosine. In the limit it is \(\sin(kS)\), with simple roots at 0 and \(k_0=\pi/S\). The implicit-function theorem gives a unique real root near each, with the near-zero root remaining exactly zero. Uniform convergence and a positive lower bound for \(|\sin(kS)|\) on the intervening closed subinterval exclude smaller positive roots for small \(\varepsilon\). The root near \(k_0\) is therefore the first positive wavenumber. All three arm cosines there are nonzero, since \(a,b>0\), \(a\ne b\), and \(\varepsilon\) is small. Setting the hub value to 1 fixes all three amplitudes analytically; division by the positive analytic square root of the squared norm normalizes them. The norm is analytic because each edge integral can be put on a fixed interval with its length as prefactor. The first positive eigenvalue is simple along this branch.

The two long arms in the limit form a Neumann interval with the hub at distance \(a\) from one end. The limiting squared hub value is \(2\cos^2(\pi a/S)/S\). Hence on the short arm \(|g_1|^2\) is again \(\varepsilon\) times an analytic function of \(\varepsilon\), with value at zero given by that intensity. In each graph we can differentiate the Taylor expansion
\[
 E_1(\varepsilon)=-\frac{\varepsilon}{6}|\psi_0(v)|^2+O(\varepsilon^2),
 \qquad \int_{-1/2}^{1/2}(\xi^2-1/4)\,d\xi=-\frac16,
\]
where \(v\) is the limiting attachment, endpoint or hub. This gives the two formulas and their ratio. Reversing the choice of endpoint of the long interval does not change the squared intensity.

## The length-cycle functional and the Berry phase

For a unit-period modulation of only the short length, \(L(\tau)=\varepsilon+\rho\cos(2\pi\nu\tau)\), with \(\nu\) a positive integer and \(|\rho|<\varepsilon\) sufficiently small, consider the explicit functional from [1, Eq. (47)]:
\[
 \mathcal F[L]=\frac18\int_0^1 (L^2)''(\tau) E_1(L(\tau))\,d\tau
  =-\frac14\int_0^1 L(\tau) (L'(\tau))^2 E_1'(L(\tau))\,d\tau .
\]
The second equality is periodic integration by parts. The quadratic coefficient of \(\rho^2\nu^2\) is \(-\pi^2 A_{11}(\varepsilon)/2\), since the period average of \(\sin^2(2\pi\nu\tau)\) is \(1/2\). This is the diagonal term in [1, Eqs. (49)–(50)], where the functional was introduced via a period-rescaled contribution. No claim about the full finite-rate phase of the evolving wavefunction is needed here.

By contrast, [2, Eqs. (3.23)–(3.25)] defines the adiabatic Berry phase by the Berry connection. For these small single-edge cycles one can choose a continuous real normalized eigenstate with the same sign at the beginning and end. Its connection vanishes, since a real normalized vector is orthogonal to its derivative. The Berry phase is therefore zero modulo \(2\pi\) in each graph, rather than having the nonzero quadratic coefficients of \(\mathcal F\). The Berry winding phase of a star around the degeneracy line in [2, Corollary 3.7] concerns different cycles.

## Verification and limitations

The proof is analytic, not a numerical root search. The determinant argument excludes poles and competing lower branches; analyticity after separating the short-length prefactor justifies differentiation. The result is not an exact identity at finite \(\varepsilon\), a statement uniform in nearly equal long-arm lengths, or a classification of graph topologies. At \(a=b\) the limiting hub intensity is zero and the stated positive ratio is outside scope.

## Relationship to prior work

The first preprint [1, §3.2 and §4] gives the general functional and star expressions but not the normalized first-positive-mode response at a shrinking endpoint versus a shrinking hub attachment. Its higher-order analytic star examples concern the ground state. The final article [2] instead treats the Berry phase. The shrinking-edge work [3,4] addresses operator convergence, resolvent or spectral asymptotics rather than this derivative of a rescaled short-edge moment and its path-versus-star ratio.

## References

1. U. Smilansky and G. Sofer, *Time dependent quantum graphs, the geometric phase and knots on closed Lissajous figures*, [arXiv:2210.14652v1](https://arxiv.org/abs/2210.14652v1), especially Eqs. (47)–(50).
2. U. Smilansky and G. Sofer, *Time evolution and the Schrödinger equation on time dependent quantum graphs*, J. Phys. A **57** (2024), 065204, [DOI:10.1088/1751-8121/ad1fb6](https://doi.org/10.1088/1751-8121/ad1fb6); [arXiv:2210.14652v2](https://arxiv.org/abs/2210.14652v2), §3.2.
3. G. Berkolaiko, Y. Latushkin, and S. Sukhtaiev, *Limits of Quantum Graph Operators With Shrinking Edges*, [arXiv:1806.00561](https://arxiv.org/abs/1806.00561), Adv. Math. **352** (2019), 632–669.
4. G. Berkolaiko, D. I. Borisov, and M. King, *Exotic eigenvalues and analytic resolvent for a graph with a shrinking edge*, [arXiv:2308.06362](https://arxiv.org/abs/2308.06362), Anal. Math. Phys. **13** (2023), 90.
