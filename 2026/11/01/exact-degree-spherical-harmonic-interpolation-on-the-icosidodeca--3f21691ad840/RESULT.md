# Exact-degree spherical-harmonic interpolation on the icosidodecahedron

## Finding

Let \(X\subset S^2\) be the thirty vertices of a regular icosidodecahedron, and let \(\mathcal H_\ell(S^2)\) denote complex spherical harmonics of *exact* nonnegative integer degree \(\ell\). For the evaluation map
\[
E_\ell:\mathcal H_\ell(S^2)\longrightarrow\mathbb C^{X},\qquad E_\ell f=(f(x))_{x\in X},
\]
its exact rank is
\[
\operatorname{rank}E_\ell=\begin{cases}
2\ell+1,&0\le\ell\le5,\\
10,&\ell=6,\\
14,&\ell\in\{8,14\},\\
15,&\ell\ge7\text{ and }\ell\notin\{8,14\}.
\end{cases}
\]
All images obey \(f(-x)=(-1)^\ell f(x)\). The map reaches **every** antipodally parity-compatible assignment on the thirty vertices for the first time at degree \(7\), again at degrees \(9\)–\(13\), and at **every** degree from \(15\) onward. In degrees \(8\) and \(14\) the unique additional restriction is \(\sum_{x\in X}f(x)=0\). In degree \(6\) the parity-compatible image has codimension five. This includes a one-step rank decrease from degree \(5\) to \(6\), and two later isolated interpolation blackouts.

## Assumptions and scope

Put \(\varphi=(1+\sqrt5)/2\). Start with the twelve icosahedron vectors given by all cyclic coordinate permutations of \((0,s,t\varphi)\), \(s,t\in\{-1,1\}\). Declare \(u,v\) adjacent when \(u\cdot v=\varphi\); there are exactly thirty unordered such pairs. Their normalized midpoints \((u+v)/(2\varphi)\) form the specified set \(X\) of unit vectors. This fixes scale, orientation, adjacency, and the thirty distinct sampling sites. No sampling weights are required for the rank statement. Equivalently, use a basis of \(\mathcal H_\ell\) orthonormal for probability surface measure on \(S^2\); then the evaluation Gram is \((2\ell+1)[P_\ell(x\cdot y)]_{x,y\in X}\), where \(P_\ell(1)=1\) is the classical Legendre polynomial.

## Proof

**1. Exact finite geometry.** The golden ratio satisfies \(\varphi^2=\varphi+1\), so the original edges have length \(2\) and each normalized midpoint lies on the unit sphere. The thirty midpoints form fifteen antipodal pairs. Select any one representative \(x_1,\ldots,x_{15}\) from each pair. Their off-diagonal inner products belong to
\[
\left\{0,\pm\tfrac12,\pm\tfrac{\sqrt5-1}{4},\pm\tfrac{\sqrt5+1}{4}\right\}.
\]
The reproducible exact field-arithmetic checker independently reconstructs all thirty midpoints, tests unit norms, identifies the fifteen antipodal pairs, and verifies this list of inner products.

**2. Gram reduction.** The spherical-harmonic addition formula makes the sampling Gram a positive multiple of \([P_\ell(x\cdot y)]\). As \(P_\ell(-t)=(-1)^\ell P_\ell(t)\), its rank equals the rank of the fifteen-by-fifteen matrix
\[
B_\ell=[P_\ell(x_i\cdot x_j)]_{1\le i,j\le15}.
\]
The other fifteen Gram eigenvalues vanish for the forced antipodal parity reason. Hence the rank can never exceed \(15\).

**3. Exact low-degree ranks.** Every entry of \(B_\ell\) lies in \(\mathbb Q(\varphi)\). Apply the exact recurrence
\[
P_0(t)=1,\quad P_1(t)=t,\qquad (n+1)P_{n+1}(t)=(2n+1)tP_n(t)-nP_{n-1}(t).
\]
Gaussian elimination over \(\mathbb Q(\varphi)\), with \(\varphi^2=\varphi+1\), gives, for \(\ell=0,1,\ldots,14\), respectively,
\[
(1,3,5,7,9,11,10,15,14,15,15,15,15,15,14).
\]
These are exact field ranks, not numerical singular-value estimates. In degrees \(8\) and \(14\), exact computation additionally gives \(B_\ell\mathbf1=0\). As the nullity is exactly one, the missing parity-compatible direction is the constant data vector, proving the stated sum condition. In degree \(6\) the nullity is exactly five.

**4. Exact finite cut-off without floating point.** For every \(15\le\ell\le262\), reduce the recurrence and the midpoint inner products in \(\mathbb F_{1009}\) by mapping \(\sqrt5\mapsto244\) and \(\varphi\mapsto627\), noting \(244^2\equiv5\pmod{1009}\) and \(627^2=627+1\) modulo \(1009\). All denominators appearing in the recurrence through degree \(262\) are invertible modulo \(1009\). Exact Gaussian elimination shows that \(B_\ell\) has rank fifteen modulo \(1009\) for each of the \(248\) degrees. A determinant nonzero after valid reduction modulo a prime is nonzero over the original characteristic-zero field, so all these matrices have full rank over \(\mathbb R\).

**5. Infinite tail.** Each off-diagonal inner product has absolute value at most \(c=(1+\sqrt5)/4\), and \(c^2=(3+\sqrt5)/8<3/4\). Thus, for every off-diagonal entry, \(\sin\theta=\sqrt{1-t^2}>1/2\) when \(t=\cos\theta\). The classical Bernstein inequality for Legendre polynomials, for integers \(\ell\ge1\), states
\[
(\sin\theta)^{1/2}\,|P_\ell(\cos\theta)|
<\sqrt{\frac{2}{\pi(\ell+1/2)}}.
\]
Consequently, using \(\pi>3\), every off-diagonal entry is bounded by \(2/\sqrt{3(\ell+1/2)}\). At \(\ell\ge263\), the sum of the absolute values of the fourteen off-diagonal entries in any row is strictly less than one, because
\[
3(263+1/2)>28^2.
\]
Every \(B_\ell\) is therefore strictly diagonally dominant with diagonal entries one, hence invertible. Together with steps 3–4, this covers *all* nonnegative degrees without extrapolation from finite tests.

## Verification

The standalone program `check_icosidodecahedron.py` uses Python's exact rational arithmetic in the quadratic field \(\mathbb Q(\varphi)\), then exact finite-field arithmetic modulo \(1009\). Running `python3 check_icosidodecahedron.py` reproduces the complete low-degree ranks, both constant null constraints, all \(248\) modular full-rank witnesses, and the strict integer inequality that closes the Bernstein tail. No external scientific software, numerical tolerance, stochastic step, or downloaded data is required.

## Relationship to prior work

Bannai–Okuda–Tagami's harmonic-index-design framework and its icosahedral Molien observation explain why invariant constant-data obstructions can occur in degrees \(8\) and \(14\). That observation by itself does not determine the rank of evaluation on the thirty *edge-midpoint* vertices, the additional five-dimensional deficiency in degree \(6\), or the first and eventual interpolation thresholds. Khalid–Kennedy–McEwen study cumulative-bandlimit sampling on latitude rings, not exact-degree interpolation on this finite polyhedral orbit. Other published discussions of icosahedral vertex orbits and hybrid spherical designs use different operators. The classification here treats the full finite evaluation map on the rectified orbit, not only the invariant sum functional. Related rank classifications on the twelve icosahedral and twenty dodecahedral vertices do not imply this result: their sampling domains are different, and, for example, at degree \(7\) a dodecahedral ten-axis evaluation can have rank at most ten whereas the present fifteen-axis evaluation has rank fifteen.

## Limitations

The theorem concerns only the vertex orbit of the regular icosidodecahedron and the ranks, not a universal interpolation theorem for arbitrary polyhedral orbits. It does not determine the nonzero singular values or optimal interpolation condition numbers at every degree. The finite rank check is an exact, finite computation with fully supplied source; the infinite tail is a separate analytic argument requiring the standard Legendre Bernstein inequality. The literature check is bounded: an equivalent prior calculation hidden in unindexed representation-theory or cubature literature cannot be excluded. No independent mathematical audit or independent validation is asserted.

## References

1. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101, first posted 2013-08-23; notably the harmonic-index definition, reproducing-kernel identity, and icosahedral examples. https://arxiv.org/abs/1308.5101
2. Z. Khalid, R. A. Kennedy, J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661, first posted 2014-03-19. https://arxiv.org/abs/1403.4661
3. P. Boyvalenkov, D. Danev, P. Kazakov, *Indexes of spherical codes*, *Codes and Association Schemes*, DIMACS Series 56 (2001), 47–57; cited as earlier context on icosahedral harmonic indices, not as an assertion about the present thirty-point ranks.
4. *Hybrid Spherical Designs*, *Discrete & Computational Geometry*, 2026, DOI:10.1007/s00454-026-00861-7; comparison to use of the same geometric orbit with a different cubature operator. https://doi.org/10.1007/s00454-026-00861-7
5. Classical Bernstein inequality for Legendre polynomials, e.g. *How sharp is Bernstein's inequality for Jacobi polynomials?*, inequality (1.1); the displayed normalization is \(P_\ell(1)=1\).
