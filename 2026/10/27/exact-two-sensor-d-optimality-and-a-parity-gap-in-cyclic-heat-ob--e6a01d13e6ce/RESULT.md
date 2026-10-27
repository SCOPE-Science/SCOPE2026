# Exact two-sensor D-optimality and a parity gap in cyclic heat observability

## Finding
Let \(C_n\) be the unweighted cycle on vertices \(\mathbb Z/n\mathbb Z\), where \(n\ge3\), with combinatorial Laplacian \(L\). Fix \(\tau>0\) and put \(T=\exp(-\tau L)\). Choose two distinct unit-amplitude vertex sensors at \(0\) and \(d\), with \(1\le d\le\lfloor n/2\rfloor\). At each of the \(r=\lfloor n/2\rfloor+1\) times \(t=0,1,\ldots,r-1\), observe both coordinates of \(T^t x\), where \(x\in\mathbb R^n\) is unknown. Let \(\mathcal O_d\) be the resulting \(2r\)-by-\(n\) observation matrix and \(W_d=\mathcal O_d^{\mathsf T}\mathcal O_d\) its information Gramian.

For \(0\le k<r\), define
\[
\xi_k=\exp\left(-\tau[2-2\cos(2\pi k/n)]\right),\quad
V_{tk}=\xi_k^t\ (0\le t<r),\quad
H=V^{\mathsf T}V,\quad h_{ij}=(H^{-1})_{ij}.
\]
The \(\xi_k\) are strictly positive and distinct, so \(H\) is positive definite. The following formulas are exact for every \(n,\tau,d\).

**Odd cycles:** If \(n=2m+1\),
\[
\boxed{\det W_d=\begin{cases}
\dfrac{2(\det H)^2h_{00}}{n^{n-1}},&\gcd(d,n)=1,\\[5pt]
0,&\gcd(d,n)>1.
\end{cases}}
\]
Thus **every observable pair has exactly the same information determinant**, independently of its separation and of \(\tau\). The D-optimal pairs are precisely those with \(\gcd(d,n)=1\).

**Even cycles:** If \(n=2m\),
\[
\boxed{\det W_d=\begin{cases}
\dfrac{(\det H)^2}{n^{n-2}}\left(h_{00}h_{mm}-\mathbf1_{2\mid d}h_{0m}^2\right),&\gcd(d,m)=1,\\[5pt]
0,&\gcd(d,m)>1.
\end{cases}}
\]
Here \(h_{0m}\ne0\). Consequently the D-optimal pairs are **exactly the odd separations satisfying \(\gcd(d,m)=1\)**. When an even separation is observable (possible when \(m\) is odd), it has a strictly smaller determinant, with the exact even-to-odd ratio
\[
\boxed{1-\frac{h_{0m}^2}{h_{00}h_{mm}}\in(0,1).}
\]
In particular, observability and D-optimality are different requirements: on \(C_6\), separation \(d=2\) yields a full-rank observation matrix but a smaller determinant than separation \(d=1\).

## Assumptions and scope
The cycle has unit, undirected edges; both sensors have equal independent unit-variance measurement noise at every listed time, so the Euclidean observation Gramian is the information matrix. The two sensors are used simultaneously at the same \(r\) consecutive integer times, starting at zero. The parameter \(\tau\) is positive but otherwise arbitrary. D-optimality means maximizing \(\det W_d\) among all choices of two distinct vertices; the cycle's rotational and reflection symmetries reduce these choices to the stated separations. The theorem does not assert that \(r\) is the minimum possible full-rank sampling horizon for every pair.

The determinant formulas and placement classification remain valid if the heat matrix is replaced by any real symmetric Fourier-diagonal cycle evolution having strictly **positive, distinct** eigenvalues \(\xi_0>\cdots>\xi_{r-1}>0\) on the cosine-frequency eigenspaces, with the same two-sensor and time-sampling conventions. Heat evolution is the primary application.

## Proof
**1. Fourier and temporal factorization.** Take the standard real orthonormal Fourier basis: the constant vector \(n^{-1/2}\mathbf1\), for each paired frequency \(1\le k<n/2\) the vectors \(\sqrt{2/n}\cos(2\pi kj/n)\) and \(\sqrt{2/n}\sin(2\pi kj/n)\), and, for even \(n\), the extra Nyquist vector \(n^{-1/2}(-1)^j\). Let \(U\) have these basis vectors as columns. Reorder measurement rows by time and then sensor. The Fourier-transformed observation matrix factors as
\[
\mathcal O_d U=(V\otimes I_2)S_d,
\]
where \(S_d\) is block diagonal by the distinct Fourier eigenvalues. The constant-frequency block is \(n^{-1/2}(1,1)^{\mathsf T}\), the paired-frequency blocks are
\[
S_k=\sqrt{2/n}\begin{pmatrix}1&0\\\cos(2\pi kd/n)&\sin(2\pi kd/n)\end{pmatrix},
\]
and for even \(n\) the Nyquist block is \(n^{-1/2}(1,(-1)^d)^{\mathsf T}\).

**2. Singular configurations.** Since \(V\) is square and invertible, the observation matrix has full column rank exactly when every paired block \(S_k\) is invertible. If \(n=2m+1\), the required nonvanishing conditions are \(\sin(2\pi kd/n)\ne0\) for every \(1\le k\le m\), equivalent to \(\gcd(d,n)=1\). If \(n=2m\), they are \(\sin(\pi kd/m)\ne0\) for every \(1\le k\le m-1\), equivalent to \(\gcd(d,m)=1\). These conditions follow directly from the Fourier blocks, including the separately treated one-dimensional Nyquist eigenspace.

**3. Rectangular Gram determinant identity.** If \(S\) is a full-column-rank \(q\)-by-\(p\) matrix, \(M\) is positive definite of order \(q\), and \(Z\) has orthonormal columns spanning \(\ker S^{\mathsf T}\), then
\[
\det(S^{\mathsf T}MS)=\det(S^{\mathsf T}S)\det(M)\det(Z^{\mathsf T}M^{-1}Z).
\]
To prove this, take an orthogonal completion of an orthonormal basis for the range of \(S\), apply the Schur-complement determinant identity to \(M\) in that basis, and restore the squared determinant of the change of basis from \(S\) to its orthonormalized columns. We apply the identity with \(M=H\otimes I_2\) and \(S=S_d\), noting that \(\det M=(\det H)^2\).

**4. Odd-order formula.** When \(n=2m+1\) and the observation is full rank, \(\ker S_d^{\mathsf T}\) has dimension one, supported on the constant-frequency block, with unit vector \((1,-1)/\sqrt2\). Hence \(\det(Z^{\mathsf T}M^{-1}Z)=h_{00}\). The squared block-volume product is
\[
\det(S_d^{\mathsf T}S_d)=\frac2n\left(\frac4{n^2}\right)^m
\prod_{k=1}^m\sin^2(2\pi kd/n).
\]
For \(\gcd(d,n)=1\), the residues \(dk\) permute the nonzero residues modulo \(n\) up to sign; the elementary sine product is
\[
\prod_{k=1}^m\sin^2(2\pi kd/n)=\frac n{2^{n-1}}.
\]
Substitution yields \(\det(S_d^{\mathsf T}S_d)=2/n^{n-1}\), proving the odd formula.

**5. Even-order formula.** When \(n=2m\) and the observation is full rank, \(\ker S_d^{\mathsf T}\) has an orthonormal basis supported on the constant and Nyquist blocks. In the constant block take \((1,-1)/\sqrt2\); in the Nyquist block take \((1,-(-1)^d)/\sqrt2\). Their inner product is zero for odd \(d\) and one for even \(d\), so
\[
\det(Z^{\mathsf T}M^{-1}Z)=h_{00}h_{mm}-\mathbf1_{2\mid d}h_{0m}^2.
\]
For \(\gcd(d,m)=1\), the paired block product uses
\[
\prod_{k=1}^{m-1}\sin^2(\pi kd/m)=\frac{m^2}{4^{m-1}},
\quad\text{giving}\quad\det(S_d^{\mathsf T}S_d)=\frac1{n^{n-2}}.
\]
This proves the even formula.

**6. Strict parity comparison.** Write \(V^{-1}\) by the coefficients of the Lagrange polynomials
\[
\ell_j(z)=\frac{\prod_{k\ne j}(z-\xi_k)}{\prod_{k\ne j}(\xi_j-\xi_k)}.
\]
Because all \(\xi_k\) are positive, the coefficients of the numerator of every \(\ell_j\), indexed by increasing polynomial degree, have strictly alternating signs. The denominators for the extreme nodes \(j=0\) and \(j=m\) have respectively positive sign and sign \((-1)^m\). Therefore each term in
\[
h_{0m}=\sum_{t=0}^{m}(V^{-1})_{0t}(V^{-1})_{mt}
\]
is nonzero and has the same sign \((-1)^m\); in particular \(h_{0m}\ne0\). Strict positive definiteness of \(H^{-1}\) gives \(0<h_{00}h_{mm}-h_{0m}^2<h_{00}h_{mm}\). Since separation one is always feasible, this proves all D-optimality and strict-gap assertions.

## Verification
The standalone dependency-free program `verify.py` constructs the untreated two-sensor observation matrices from exact integer powers of \(3I+A(C_n)\) and \(5I+A(C_n)\) for \(3\le n\le14\), then computes integer Gram determinants with the Bareiss algorithm. It checks all 96 ordered-distance/shift cases, including equal positive determinants at odd-order coprime distances, structural zeros, and strict even-order parity gaps. For example, it obtains determinant \(116560\) for the six-cycle with separation two and the evolution \(3I+A(C_6)\), an exact full-rank witness.

The independent high-precision test `verify_heat.py` forms the genuine heat trajectories directly from Fourier heat kernels at \(\tau=0.3\), computes their Gram determinants, and checks them against the displayed formulas for all 35 distances on cycles of order \(3\) through \(12\) at 80 decimal digits. It includes 10 zero cases and three observable even-separation cases. Their recorded outputs are supplied alongside the scripts. These finite computations do not establish the all-parameter theorem; that is supplied by the preceding proof.

## Relationship to prior work
Parlangeli and Notarstefano (arXiv:1109.3556, first public September 16, 2011) analyze qualitative controllability and observability on paths and cycles using arithmetic conditions and provide eigenvalue and eigenvector descriptions. In particular, their full text treats cycle pair locations, but not the information-Gramian determinant or D-optimal ties/strict parity gap derived here. The even-cycle Fourier rank criterion above is established directly, rather than taken from an external arithmetic criterion.

Summers, Cortesi and Lygeros (arXiv:1404.7665, first public April 30, 2014) establish general submodularity for log-determinant controllability and observability objectives, without giving this exact cyclic placement classification. Alaeddini and Morgansen (arXiv:1609.02654, first public September 9, 2016) use an observability-Gramian determinant to motivate sensor placement in a nonlinear epidemic-network application, but do not analyze these cyclic heat trajectories.

A distinct published result titled *Sharp spectral-demixed two-sensor frame bounds on finite cycles* addresses the low-pass, **spectrally demixed** Fourier output norm and explicitly distinguishes it from the untreated time-trajectory Gramian; it does not imply the displayed determinant formula or even-order parity comparison without the additional rectangular-Gram calculation. A separate result on **single-sensor normalized paths** concerns a different graph, number of sensors and sampling matrix. These general and related formulas are not claimed as new.

## Limitations
All conclusions concern finite-dimensional symmetric cycle heat diffusion, exactly two equally weighted point sensors, and the specified consecutive-time, equal-noise determinant criterion. D-optimality need not optimize the smallest eigenvalue, condition number or a different observation horizon, nor does it apply unchanged to directed or irregularly weighted cycles, colored noise or nonlinear sensing. Closed formulas use Vandermonde matrices and can be numerically ill-conditioned for long observation horizons; stable implementation may require high precision or orthogonal polynomial techniques. Novelty is assessed against inspected sources and accessible search results, not established by a complete survey or independent expert audit.

## References
1. G. Parlangeli and G. Notarstefano, *On the reachability and observability of path and cycle graphs*, arXiv:1109.3556v1, September 16, 2011, https://arxiv.org/abs/1109.3556.
2. T. H. Summers, F. L. Cortesi and J. Lygeros, *On Submodularity and Controllability in Complex Dynamical Networks*, arXiv:1404.7665v1, April 30, 2014, https://arxiv.org/abs/1404.7665.
3. A. Alaeddini and K. A. Morgansen, *Optimal Disease Outbreak Detection in a Community Using Network Observability*, arXiv:1609.02654v1, September 9, 2016, https://arxiv.org/abs/1609.02654.
4. *Sharp spectral-demixed two-sensor frame bounds on finite cycles*, publicly released scientific result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-spectral-demixed-two-sensor-frame-bounds-on-finite-cycles--b03d8e4c7818.
5. *Universal endpoint optimality for dynamical sampling on normalized paths*, publicly released scientific result, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-universal-endpoint-optimality-for-dynamical-sampling-on-normaliz--d0ca7333cb0f.
