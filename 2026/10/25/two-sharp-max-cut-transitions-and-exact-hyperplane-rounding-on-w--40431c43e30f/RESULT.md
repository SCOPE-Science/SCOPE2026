# Two sharp Max-Cut transitions and exact hyperplane rounding on weighted Möbius ladders

## Finding
For every integer \(n\ge3\) and every \(t\ge0\), let \(M_{2n}(t)\) be the graph on the cyclic vertex set \(\mathbb Z/(2n)\mathbb Z\), with weight one on the \(2n\) cycle edges and weight \(t\) on its \(n\) distinct antipodal edges \(\{i,i+n\}\). Define \(\operatorname{CUT}_n(t)\) as the largest weighted cut and \(\operatorname{SDP}_n(t)\) as the standard unit-vector/elliptope Max-Cut relaxation, with each edge of weight \(w\) contributing \(w(1-\langle v_i,v_j\rangle)/2\).

For odd \(n\), both optima equal \(n(2+t)\). For even \(n\ge4\), put \(c=\cos(\pi/n)\), \(t_{\mathrm{sdp}}=1-c\), and \(t_{\mathrm{cut}}=2/n\). Then \(0<t_{\mathrm{sdp}}<t_{\mathrm{cut}}\), and
\[
\operatorname{SDP}_n(t)=
\begin{cases}
2n,&0\le t\le 1-c,\\
n(1+c+t),&t\ge1-c,
\end{cases}
\qquad
\operatorname{CUT}_n(t)=
\begin{cases}
2n,&0\le t\le2/n,\\
2n-2+nt,&t\ge2/n.
\end{cases}
\]
The two formulas agree on \(0\le t\le1-c\), and the relaxation is strictly above the integer optimum for every finite \(t>1-c\). The additive gap is constant, equal to \(2-n(1-c)>0\), once \(t\ge2/n\). The multiplicative gap \(\operatorname{SDP}_n(t)/\operatorname{CUT}_n(t)\) has a unique global maximum over \(t\ge0\), precisely at \(t=2/n\), with value
\[
\frac{1+\cos(\pi/n)}2+\frac1n
=1+\frac1n-\frac{\pi^2}{4n^2}+O(n^{-4}).
\]

For every even \(n\ge4\) and \(t>1-c\), the optimal SDP *Gram matrix is unique*: writing \(\theta=\pi(n-1)/n\), it is \(X_{ij}=\cos(\theta(i-j))\). Every hyperplane-rounding normal not orthogonal to one of its representing unit vectors yields exactly \(2n-2\) cut cycle edges and all \(n\) antipodal edges. Consequently this rounding is suboptimal for every such normal when \(1-c<t<2/n\), but yields an *integer-optimal cut for every such normal* when \(t\ge2/n\), even though the SDP integrality gap remains strictly positive. At \(t=1-c\), uniqueness of the optimal Gram matrix is not asserted.

## Assumptions and scope
Weights are nonnegative, the cycle is undirected and simple, and every antipodal edge appears once. The parameter \(t\) denotes an edge weight, not a computational time step. The integer Max-Cut optimum optimizes over all bipartitions, and the SDP optimizes over arbitrary-dimensional real unit vectors or, equivalently, correlation matrices \(X\succeq0\) with \(X_{ii}=1\). The rounding statement concerns the basic Goemans–Williamson random hyperplane rule applied to an *optimal* Gram factor and excludes its finitely many degenerate normals. It does not claim that every SDP-optimal Gram at the transition parameter produces the same rounded cuts, nor that independently sampled or approximately optimal Gram factors have the stated behavior.

The cases \(n\ge3\) exclude the degenerate antipodal-edge identification at \(n=2\). When \(t=0\), zero-weight antipodal edges are harmless and the cycle remains connected.

## Proof
**1. Spectral upper bound.** Let \(N=2n\), \(A\) be the symmetric weighted adjacency matrix, and \(W=2n+nt\) the total edge weight. For a positive semidefinite \(N\)-by-\(N\) Gram matrix \(X\) with unit diagonal, \(\operatorname{tr}X=N\) and the SDP objective is \(W/2-\operatorname{tr}(AX)/4\). Since \(A-\lambda_{\min}(A)I\succeq0\), the trace of its product with \(X\) is nonnegative. Therefore
\[
\operatorname{SDP}_n(t)\le\frac W2-\frac N4\lambda_{\min}(A).
\]
Equality forces the range of \(X\) to lie in the minimum-eigenvalue eigenspace of \(A\).

**2. Exact Fourier eigenvalues and attainment.** On the Fourier mode indexed by \(k\in\{0,\ldots,2n-1\}\), the adjacency eigenvalue is
\[
\lambda_k=2\cos(\pi k/n)+t(-1)^k.
\]
For odd \(n\), the minimum is \(-2-t\), uniquely at \(k=n\). For even \(n\), the smallest even-mode eigenvalue is \(-2+t\), uniquely at \(k=n\); the smallest odd-mode eigenvalue is \(-2\cos(\pi/n)-t\), attained exactly at \(k=n\pm1\). These cross at \(t=1-\cos(\pi/n)\). The trace upper bound consequently gives the two claimed SDP branches. It is attained by real unit vectors \(v_i=(-1)^i\) in the \(k=n\) mode, or by the planar unit vectors \(v_i=(\cos(\theta i),\sin(\theta i))\), with \(\theta=\pi(n-1)/n\), in the \(k=n-1\) mode. Hence the bound is exact.

**3. Uniqueness of the Gram matrix off the crossing.** For even \(n\) and \(t<1-c\), the minimum eigenspace is the one-dimensional alternating vector, so the trace equality condition fixes \(X_{ij}=(-1)^{i-j}\). For even \(n\) and \(t>1-c\), that eigenspace is exactly the real span of the two trigonometric columns \(u_i=\cos(\theta i)\), \(z_i=\sin(\theta i)\). Thus any optimal \(X\) has the form \(X=[u\ z]Q[u\ z]^{\mathsf T}\) for a symmetric positive semidefinite \(2\)-by-\(2\) matrix \(Q\). Unit diagonal imposes
\[
1=\frac{Q_{11}+Q_{22}}2+\frac{Q_{11}-Q_{22}}2\cos(2\theta i)+Q_{12}\sin(2\theta i),
\]
for all \(i\). The three displayed discrete Fourier modes are linearly independent for even \(n\ge4\), forcing \(Q_{11}=Q_{22}=1\) and \(Q_{12}=0\). This proves uniqueness of \(X_{ij}=\cos(\theta(i-j))\). For odd \(n\), the unique alternating mode likewise gives the unique optimum.

**4. Exact integer optimum.** When \(n\) is odd, the parity assignment \(s_i=(-1)^i\) cuts every cycle edge and every antipodal edge, attaining the sum of all edge weights \(n(2+t)\). Suppose \(n\) is even. A cut of the even cycle with all \(2n\) edges crossing has the alternating signs \(s_i=(-1)^i\), so no antipodal edge crosses. Otherwise the number of cycle edges *not* crossing is a positive even integer and hence at least two. Such a cut weighs at most \(2n-2+nt\). The first bound \(2n\) is attained by alternating signs. The second is attained by setting \(s_i=(-1)^i\) for \(0\le i<n\) and \(s_{i+n}=-s_i\); this cuts every antipodal edge and all but the two joining edges of the cycle. The upper and lower bounds coincide, proving the claimed maximum.

**5. Universal rounding of the unique rank-two optimum.** For even \(n\ge4\) and \(t>1-c\), an optimal Gram factor consists (up to orthogonal isometry) of the planar vectors from Step 2. Because \(\gcd(n-1,2n)=1\), their angular labels \(j=(n-1)i\pmod {2n}\) form the full regular \(2n\)-gon. A generic hyperplane partitions those angular labels into two consecutive arcs, each containing precisely \(n\) points. Rotate the labels so that one arc is \(\{0,1,\ldots,n-1\}\). A cycle edge maps to angular displacement \(n-1\); exactly one directed edge stays inside each arc, while the other \(2n-2\) cross. Moreover \(v_{i+n}=-v_i\), so every antipodal edge crosses. Thus every generic rounded cut has value \(2n-2+nt\). Comparing with Step 4 gives its exact optimality interval.

**6. Gap boundaries and extremizer.** The strict inequality \(1-\cos(\pi/n)<2/n\) follows from \(1-\cos u\le u^2/2\) and \(\pi^2/(2n)<2\) for all even \(n\ge4\). The additive difference above \(2/n\) is \(n(1+c+t)-(2n-2+nt)=2-n(1-c)>0\). On \((1-c,2/n)\) the SDP-to-cut ratio is \((1+c+t)/2\), strictly increasing; on \((2/n,\infty)\) it is \(1+[2-n(1-c)]/(2n-2+nt)\), strictly decreasing. It is one on \([0,1-c]\). Thus the unique worst case is \(t=2/n\), with the stated ratio. Expanding \(\cos(\pi/n)\) gives the asymptotic formula.

## Verification
The included standalone `verify.py` (Python standard library only) and its recorded output `verification_output.txt` check 42 exact-rational brute-force maximum cuts (\(3\le n\le9\)), 156 Fourier minimum-eigenvalue formulas, 156 explicit planar Gram objectives, and 2,240 generic hyperplane-rounding outcomes. The script uses exhaustive cuts only for finite \(n\le9\) and floating-point evaluations for the spectral and hyperplane checks. It does not establish the quantified infinite-family theorem; that follows from the six analytic steps above.

## Relationship to prior work
Goemans and Williamson introduced and studied the unit-vector relaxation and random-hyperplane rounding [1]. Van Dam and Sotirov prove that for walk-regular (including vertex-transitive) graphs the Max-Cut SDP equals the sharp Laplacian spectral bound [2, Theorem 6, Section 4.1]. **That general SDP–spectral equivalence is prior work and is not claimed as a new principle here.** The Möbius ladder is vertex-transitive, so the spectral *value* is a consequence of that framework once its weighted Fourier eigenvalues are inserted.

The current joint classification adds the *integer* value as a function of antipodal weight, the strict separation of spectral and integer transition weights, the unique maximizing weight of the SDP-to-integer ratio, uniqueness of the rank-two optimal Gram matrix, and an exact all-hyperplanes rounding dichotomy. These are not statements supplied by the general spectral equivalence alone. The earlier literature on Möbius ladders and optimization includes unweighted Max-Cut experiments and analyses of polynomial-time solvability for arbitrarily weighted ladders [3, 4]; neither inspected material states the joint parametric phase and rounding classification. An explicit earlier theorem covering the same weighted Möbius-ladder phase boundaries or the same deterministic hyperplane-rounding dichotomy would supersede the corresponding originality assessment.

## Limitations
No claim is made for arbitrary, nonuniform edge weights or general circulant graphs. The basic SDP here does not include added triangle or higher cut inequalities. At the crossing \(t=1-\cos(\pi/n)\), optimal Gram matrices need not be unique. The rounding statement is almost sure with respect to any continuously distributed isotropic hyperplane normal and is exact for all nondegenerate normals of the specified optimal embedding; arbitrary numerical perturbations are not covered. The existing spectral-equivalence theory makes the SDP value a known consequence of prior results, rather than an independent new general principle. Specialized prior work could still imply the combined weighted phase and rounding statements; the source comparison is not a mathematical proof of novelty. Independent mathematical validation has not been performed.

## References
[1] M. X. Goemans and D. P. Williamson, *Improved approximation algorithms for maximum cut and satisfiability problems using semidefinite programming*, J. ACM 42 (1995), 1115–1145. DOI: 10.1145/227683.227684. Author-hosted full text: https://math.mit.edu/~goemans/PAPERS/maxcut-jacm.pdf.

[2] E. R. van Dam and R. Sotirov, *New bounds for the max-k-cut and chromatic number of a graph*, arXiv:1503.06595, first posted 2015-03-23. https://arxiv.org/abs/1503.06595. Especially Section 4.1, Theorem 6.

[3] *Computational complexity continuum within Ising formulation of NP problems*, Communications Physics (2022), DOI: 10.1038/s42005-021-00792-0. https://www.nature.com/articles/s42005-021-00792-0. Möbius-ladder benchmark and polynomial-time solvability discussion.

[4] S. Shirasaka, *Investigation on Oscillator-Based Ising Machines*, in *Photonic Neural Networks with Spatiotemporal Dynamics* (2023), DOI: 10.1007/978-981-99-5072-0_9. https://link.springer.com/chapter/10.1007/978-981-99-5072-0_9. Section 4.1 reports unweighted Möbius-ladder cut examples and mentions rank-two relaxations.

