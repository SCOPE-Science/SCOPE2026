# All-coupling equidistant maximizer for repulsive point interactions on a loop
## Finding
For every integer \(N\ge 2\), every \(lpha>0\), and every set of \(N\) distinct identical repulsive delta interactions on a loop of length \(2\pi\), the ground-state eigenvalue is uniquely maximized, up to rotation and relabeling, when the interactions are equally spaced. Equivalently, Exner's Conjecture 5.1 for the periodic one-dimensional repulsive point-interaction problem holds for every coupling strength and every \(N\ge2\).

If the cyclic gaps are \(d_1,\ldots,d_N>0\), with \(\sum_j d_j=2\pi\), and \(\lambda_1(lpha,Y)=k^2\), then
\[
lpha\ge rac{2k}N\sum_{j=1}^N	an\!\left(rac{k d_j}2ight)
\ge 2k	an\!\left(rac{\pi k}Night).
\]
The second inequality is strict unless \(d_1=\cdots=d_N=2\pi/N\). For the equidistant configuration the ground-state wave number \(k_*\in(0,N/2)\) is characterized exactly by
\[
lpha=2k_*	an\!\left(rac{\pi k_*}Night).
\]
Hence \(k\le k_*\), strictly for every non-equidistant configuration.

## Assumptions and scope
The operator acts in \(L^2(0,2\pi)\) as the negative second derivative away from the interaction sites, with periodic endpoint conditions, continuity at each interaction site, and derivative jump \(u'(y_j+)-u'(y_j-)=lpha u(y_j)\). The interaction strength is common and repulsive, \(lpha>0\), and all sites are distinct. The result concerns only the lowest eigenvalue. By scaling, an equivalent statement holds for any fixed loop length after the usual simultaneous rescaling of length and coupling, but the displayed formulas use the source normalization \(2\pi\).

## Proof
The quadratic form is
\[
q[u]=\int_0^{2\pi}|u'(x)|^2\,dx+lpha\sum_{j=1}^N|u(y_j)|^2.
\]
It is strictly positive on nonzero periodic \(H^1\) functions, so the ground-state eigenvalue is \(k^2>0\). Replacing a ground state by its modulus does not increase the form. Standard one-dimensional uniqueness then gives a strictly positive ground state \(u\): if a nonnegative eigenfunction vanished at any point, the local minimum and the matching condition would force zero Cauchy data and hence the zero solution.

Let \(d_j\) be the clockwise distance from \(y_j\) to \(y_{j+1}\), indices cyclically. On that open gap, \(-u''=k^2u\). A nonzero sinusoidal solution cannot remain strictly positive on an interval of length at least \(\pi/k\), so
\[
0<k d_j<\pi\qquad(j=1,\ldots,N).
\]
Write \(v_j=u(y_j)>0\). Solving the ODE on each gap from its two endpoint values and applying the derivative-jump conditions gives
\[
(B_Y(k)v)_j=
 k\csc(kd_{j-1})v_{j-1}+k\csc(kd_j)v_{j+1}
-kigl(\cot(kd_{j-1})+\cot(kd_j)igr)v_j
=lpha v_j.
\]
For \(N=2\), the two displayed neighbor contributions are the two distinct arcs joining the same pair of sites and are added. Since every \(\sin(kd_j)\) is positive, all graph off-diagonal edge weights in \(B_Y(k)\) are positive. The matrix is real symmetric and irreducible. After adding a sufficiently large scalar multiple of the identity it is an irreducible nonnegative matrix; Perron--Frobenius therefore identifies the eigenvalue belonging to the positive vector \(v\) with the largest eigenvalue of \(B_Y(k)\). Thus \(lpha=\lambda_{\max}(B_Y(k))\).

Testing the largest eigenvalue on the constant vector gives
\[
lpha\ge rac1N\mathbf 1^TB_Y(k)\mathbf 1
=rac{2k}N\sum_{j=1}^Nigl(\csc(kd_j)-\cot(kd_j)igr)
=rac{2k}N\sum_{j=1}^N	an\!\left(rac{kd_j}2ight).
\]
Because \(0<kd_j/2<\pi/2\), the tangent is strictly convex there. Jensen's inequality and \(N^-1\sum_jd_j=2\pi/N\) yield
\[
lpha\ge 2k	an\!\left(rac{\pi k}Night),
\]
strictly when the gaps are not all equal.

For equal gaps \(d_j=2\pi/N\), the constant vector is positive and hence is itself the Perron eigenvector of the same matrix. Therefore the corresponding ground-state wave number \(k_*\) satisfies equality,
\[
lpha=F_N(k_*),\qquad F_N(s)=2s	an\!\left(rac{\pi s}Night),\qquad 0<s<N/2.
\]
Moreover \(F_N'(s)=2	an(\pi s/N)+(2\pi s/N)\sec^2(\pi s/N)>0\). Hence \(F_N\) is strictly increasing from \(0\) to \(+\infty\) on \((0,N/2)\). Comparing \(F_N(k)\lelpha=F_N(k_*)\) gives \(k\le k_*\), and the strict Jensen step gives \(k<k_*\) for every non-equidistant configuration. Squaring proves the claim.

## Verification
The bundled `verify.py` implements the exact transfer matrix for free propagation followed by repulsive delta jumps, and separately implements the finite-dimensional Dirichlet-to-Neumann matrix used in the proof. It checks unequal configurations for \(N=2,3,4,5,6,7\) at several positive couplings, verifies the periodic transfer condition at the numerically reconstructed ground-state root, verifies the Jensen/Perron inequality, and confirms strict improvement by the equidistant configuration. Running `python3 verify.py` returns `VERIFY_OK`.

These computations only test finite instances. The all-\(N\) statement is established by the analytic positivity, Perron--Frobenius, Jensen, and monotonicity argument above; it is not inferred from the numerical checks.

## Relationship to prior work
Pavel Exner, *An optimization problem for finite point interaction families*, arXiv:1906.01229 (first public version 2019-06-04), J. Phys. A: Math. Theor. 52 (2019), 405302, DOI 10.1088/1751-8121/ab3d82, treats the same periodic one-dimensional operator. Section 5 proves the equidistant maximizer for sufficiently weak repulsion and sufficiently strong repulsion, then states as Conjecture 5.1 that the strict inequality should hold for every \(lpha\in(0,\infty)\). The result here supplies the missing all-coupling argument for every \(N\ge2\).

The key change of viewpoint is to use the energy-dependent cyclic Dirichlet-to-Neumann matrix on the positive ground-state branch. Positivity forces every phase \(kd_j\) into \((0,\pi)\), exactly the interval on which the edge weights have one sign and \(	an(kd_j/2)\) is strictly convex. This avoids the global loss of convexity of the periodic resolvent kernel noted in the source.

## Limitations
The proof uses identical positive delta strengths, a one-dimensional loop, and periodic boundary conditions. It does not treat unequal couplings, magnetic/quasiperiodic boundary conditions, excited eigenvalues, higher-dimensional point interactions, or optimization of minimizers. It also does not assert any stability modulus quantifying the eigenvalue loss in terms of the distance from the equidistant configuration.

## References
1. P. Exner, *An optimization problem for finite point interaction families*, arXiv:1906.01229, v1 dated 2019-06-04; DOI 10.1088/1751-8121/ab3d82.
2. P. Exner, mp_arc 19-36, public manuscript of the same work; Section 5 contains Theorems 5.1--5.2 and Conjecture 5.1.
