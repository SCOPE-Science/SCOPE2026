# Short-edge geometric-phase response detects attachment location in quantum graphs

## Finding

Let \(a,b>0\), \(a\ne b\), and \(S=a+b\). Compare two compact metric graphs with standard Neumann conditions at leaves and Kirchhoff conditions at internal vertices:

1. a path with edge lengths \((\varepsilon,a,b)\), where the edge of length \(\varepsilon\) is at an endpoint;
2. a three-arm star with arm lengths \((\varepsilon,a,b)\), where the short arm of length \(\varepsilon\) is attached at the hub.

For the normalized first positive eigenstate, let
\[
E_1(\varepsilon)=\int_{-1/2}^{1/2}\left(\xi^2-\frac14\right)|g_1(\xi;\varepsilon)|^2\,d\xi,
\qquad A_{11}(\varepsilon)=\varepsilon\,\frac{\partial E_1}{\partial\varepsilon},
\]
where \(g_1\) is the scaled eigenfunction on the short edge. Then, as \(\varepsilon\downarrow0\) with \(a,b\) fixed,
\[
A_{11}^{\mathrm{path}}(\varepsilon)=-\frac{\varepsilon}{3S}+O(\varepsilon^2),\qquad
A_{11}^{\mathrm{star}}(\varepsilon)=-\frac{\varepsilon}{3S}\cos^2\!\left(\frac{\pi a}{S}\right)+O(\varepsilon^2).
\]
Thus the ratio of the two coefficients tends to \(\cos^2(\pi a/S)\), strictly between zero and one. In the geometric-phase convention of Smilansky and Sofer, the coefficient multiplying the short-edge term \(\rho_1^2\nu_1^2\) is \(-\pi^2 A_{11}/2\), so these coefficients have the same limiting ratio. The two graphs have the same edge-length multiset; the difference records where the short edge is attached.

## Assumptions and scope

The graph Laplacian acts as \(-d^2/dx^2\) on every edge. Leaves have Neumann conditions and internal vertices satisfy continuity and the Kirchhoff sum-of-outward-derivatives condition. The long-edge lengths \(a,b\) are fixed and positive, with \(a\ne b\). The short-edge limit is \(\varepsilon\downarrow0\). The first positive eigenvalue is simple for sufficiently small positive \(\varepsilon\); the condition \(a\ne b\) ensures that the limiting first excited eigenfunction does not vanish at the hub. For interpreting \(A_{11}\) as a quadratic phase coefficient, the edge-length modulation amplitude must be small compared with \(\varepsilon\), and the adiabatic limit assumed in the cited quantum-graph phase formula is in force.

## Proof

For any simple normalized eigenbranch whose eigenfunction remains bounded and varies smoothly along a short edge, the scaled eigenfunction satisfies
\[
g_1(\xi;\varepsilon)=\sqrt{\varepsilon}\,\psi_\varepsilon\!\left(\varepsilon(\xi+1/2)\right).
\]
As \(\varepsilon\to0\), its value along that edge tends to the limiting eigenfunction value \(\psi_0(v)\) at the attachment vertex \(v\). Therefore
\[
E_1(\varepsilon)=\varepsilon|\psi_0(v)|^2\int_{-1/2}^{1/2}\left(\xi^2-\frac14\right)d\xi+O(\varepsilon^2)
=-\frac{\varepsilon}{6}|\psi_0(v)|^2+O(\varepsilon^2).
\]
The simple eigenbranch depends analytically on \(\varepsilon\) near zero in these two models, so differentiating the expansion gives
\[
A_{11}(\varepsilon)=-\frac{\varepsilon}{6}|\psi_0(v)|^2+O(\varepsilon^2).
\]

For the path, deleting the short endpoint edge leaves a Neumann interval of length \(S\). Its normalized first positive eigenfunction is \(\psi_0(x)=\sqrt{2/S}\cos(\pi x/S)\), with \(x=0\) at the endpoint. Hence \(|\psi_0(0)|^2=2/S\), giving \(A_{11}^{\mathrm{path}}=-\varepsilon/(3S)+O(\varepsilon^2)\).

For the star, the positive eigenvalues obey the secular equation
\[
\tan(k\varepsilon)+\tan(ka)+\tan(kb)=0.
\]
At \(\varepsilon=0\), the identity
\[
\tan(ka)+\tan(kb)=\frac{\sin(kS)}{\cos(ka)\cos(kb)}
\]
shows that the first positive root is \(k_0=\pi/S\). Since \(a\ne b\), both denominators are nonzero there, and the root is simple; the implicit-function theorem gives a smooth eigenbranch for small \(\varepsilon\). The limiting graph is the same Neumann interval of length \(S\), but the star hub lies at position \(x=a\). Its limiting first positive eigenfunction therefore has hub amplitude squared
\[
|\psi_0(a)|^2=\frac{2}{S}\cos^2\!\left(\frac{\pi a}{S}\right).
\]
Substitution into the short-edge formula yields \(A_{11}^{\mathrm{star}}=-\varepsilon\cos^2(\pi a/S)/(3S)+O(\varepsilon^2)\). Dividing the two asymptotic expressions proves the ratio. Because \(a,b>0\) and \(a\ne b\), \(0<\cos^2(\pi a/S)<1\).

Smilansky and Sofer's leading adiabatic formula writes the quadratic contribution from edge \(1\) as \(-\pi^2\rho_1^2\nu_1^2 A_{11}/2\). The common factors \(\rho_1^2\nu_1^2\) cancel in the ratio, proving the phase-response statement.

## Verification

The proof uses the exact integral \(\int_{-1/2}^{1/2}(\xi^2-1/4)\,d\xi=-1/6\), the Neumann-interval eigenfunction, and the star secular equation. The first positive path eigenvalue is \(\pi^2/(S+\varepsilon)^2\). For the star, the simple root near \(\pi/S\) follows from the displayed tangent identity and the implicit-function theorem; no finite numerical scan is used as proof. The asymptotic error terms are for fixed \(a,b\) with \(a\ne b\). The result is an asymptotic statement, not an exact formula at finite \(\varepsilon\).

## Relationship to prior work

Smilansky and Sofer derive the adiabatic geometric-phase formula for moving metric graphs and work out a three-arm-star example. Their discussion asks whether geometric phases can reveal graph features and includes higher-order ground-state calculations for a three-star. The present claim instead concerns the first positive eigenstate and a singular short-edge limit, comparing an endpoint attachment with an interior hub attachment at the same edge lengths. Berkolaiko, Latushkin, and Sukhtaiev study operator convergence when edges shrink, while Berkolaiko, Borisov, and King classify spectral and resolvent asymptotics for a short edge under general vertex conditions. Those works provide context for the limiting graph but do not state this geometric-phase response ratio.

## Limitations

The result does not classify all graph topologies from geometric-phase data. It concerns one simple excited eigenbranch, a single short edge, standard Neumann–Kirchhoff conditions, and the limit \(\varepsilon\downarrow0\). It does not apply at \(a=b\), where the limiting first excited mode has a node at the hub and the leading star coefficient vanishes.

## References

1. U. Smilansky and G. Sofer, “Time evolution and the Schrödinger equation on time dependent quantum graphs,” *Journal of Physics A: Mathematical and Theoretical* 57 (2024), 065204. First public preprint: arXiv:2210.14652 (26 October 2022). DOI: 10.1088/1751-8121/ad1fb6.
2. G. Berkolaiko, Y. Latushkin, and S. Sukhtaiev, “Limits of Quantum Graph Operators With Shrinking Edges,” arXiv:1806.00561 (first posted 2 June 2018); *Advances in Mathematics* 352 (2019), 632–669.
3. G. Berkolaiko, D. I. Borisov, and M. King, “Exotic eigenvalues and analytic resolvent for a graph with a shrinking edge,” arXiv:2308.06362 (first posted 11 August 2023); *Analysis and Mathematical Physics* 13 (2023), article 90. DOI: 10.1007/s13324-023-00853-3.
