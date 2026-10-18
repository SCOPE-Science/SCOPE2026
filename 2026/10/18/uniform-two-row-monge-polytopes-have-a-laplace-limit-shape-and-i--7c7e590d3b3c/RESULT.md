# Uniform two-row Monge polytopes have a Laplace limit shape and independent Gumbel edges

## Finding
For every integer \(n\ge2\), let \(\mathcal M_{2,n}\) be the convex polytope of nonnegative real matrices \(C=(c_{ij})\) with two rows and \(n\) columns satisfying
\[
\sum_{i=1}^{2}\sum_{j=1}^{n}c_{ij}=1,
\qquad c_{1j}+c_{2,j+1}\le c_{1,j+1}+c_{2j}
\quad (1\le j<n).
\]
Give this \((2n-1)\)-dimensional polytope its normalized intrinsic Lebesgue measure. The following results hold for a uniformly sampled \(C\).

**Exact uniform sampler.** Independently sample \(n\) standard Laplace variables \(D_i\), with density \(\tfrac12e^{-|d|}\), and \(n\) exponential variables \(W_i\), with rate \(2\). Let \(\sigma\) order the \(D_i\) increasingly and set \(S=\sum_i(|D_i|+2W_i)\). Then the following matrix is exactly uniform in \(\mathcal M_{2,n}\):
\[
c_{1j}=\frac{W_{\sigma(j)}+(D_{\sigma(j)})_+}{S},
\qquad
c_{2j}=\frac{W_{\sigma(j)}+(-D_{\sigma(j)})_+}{S},
\quad 1\le j\le n,
\]
where \(x_+=\max\{x,0\}\). In particular, the total mass in the first row is **exactly** \(\operatorname{Beta}(n,n)\), with variance \(1/[4(2n+1)]\).

**Two complete cumulative limit shapes.** Couple all dimensions using the first \(n\) pairs of one infinite independent sequence \((D_i,W_i)\) in the preceding construction. Set
\[
A_n(t)=\sum_{j\le\lfloor nt\rfloor}c_{1j},\qquad
B_n(t)=\sum_{j\le\lfloor nt\rfloor}c_{2j},\qquad 0\le t\le1.
\]
Then almost surely, *uniformly for all* \(t\in[0,1]\), \(A_n(t)\to A(t)\) and \(B_n(t)\to B(t)\), where (with \(0\log0:=0\))
\[
A(t)=\begin{cases}
 t/4,&0\le t\le1/2,\\
 (3t-1)/4+(1-t)\log(2(1-t))/2,&1/2\le t\le1,
\end{cases}
\]
\[
B(t)=\begin{cases}
3t/4-t\log(2t)/2,&0\le t\le1/2,\\
(t+1)/4,&1/2\le t\le1.
\end{cases}
\]
Thus \(A(1/2)=1/8\), \(B(1/2)=3/8\): the first half of the columns asymptotically carries **one quarter more of the total matrix mass in row two than in row one**, while both full-row totals tend to \(1/2\). In an arbitrary uncoupled sequence of uniform samples, the asserted convergence is in probability.

**Two independent extreme laws.** As \(n\to\infty\),
\[
\left(2n(c_{1n}-c_{2n})-\log(n/2),
-2n(c_{11}-c_{21})-\log(n/2)\right)
\ \Longrightarrow\ (G_+,G_-),
\]
where \(G_+\) and \(G_-\) are independent random variables with standard Gumbel distribution \(\Pr(G\le x)=\exp(-e^{-x})\).

An optional exact finite-dimensional centroid formula is also available: if \(Q\) is the standard Laplace quantile function and \(\mathrm B\) is Euler's beta function, then for every \(1\le j\le n\),
\[
\mathbb E(c_{1j}-c_{2j})
=\frac1{2n}\int_0^1Q(u)\frac{u^{j-1}(1-u)^{n-j}}{\mathrm B(j,n+1-j)}\,du.
\]

## Assumptions and scope
The uniform measure is the intrinsic Euclidean volume measure on the affine hyperplane of total mass one, restricted to the closed Monge polytope and normalized to probability one. All inequalities hold weakly, but equalities of adjacent row contrasts have probability zero under this measure. In the almost-sure limit assertion, the samples for different \(n\) are coupled by truncating a common infinite sequence; the marginal at each \(n\) is the specified uniform volume law. No claim of independence between the Beta row mass and the Gumbel variables is made.

For \(0<u<1\), the standard Laplace quantile function is
\[
Q(u)=\begin{cases}\log(2u),&0<u\le1/2,\\-\log(2(1-u)),&1/2\le u<1.\end{cases}
\]

## Proof
**1. Uniform measure and ordering.** Let \(U_j,V_j\), \(1\le j\le n\), be \(2n\) independent rate-one exponential random variables and set \(S_n=\sum_j(U_j+V_j)\). By the change of variables from positive coordinates to their sum and normalized proportions, \((U_1,V_1,\ldots,U_n,V_n)/S_n\) is uniform on the \((2n-1)\)-simplex, and is independent of \(S_n\sim\operatorname{Gamma}(2n,1)\). The Monge inequalities reduce exactly to
\[
U_1-V_1\le U_2-V_2\le\cdots\le U_n-V_n.
\]
All \(n!\) strict orderings of the independent identically distributed continuous differences have equal probability. Permuting *entire* column pairs preserves the unconditioned simplex distribution. Accordingly, sorting these pairs by \(U_j-V_j\) gives exactly the uniform simplex law conditioned on the Monge inequalities, which is intrinsic-uniform volume on \(\mathcal M_{2,n}\). This also recovers the previously known relative volume \(1/n!\); that volume formula is not asserted to be new.

**2. The Laplace–exponential decomposition.** For an independent rate-one exponential pair define \(D=U-V\) and \(W=\min(U,V)\). The inverse map is \(U=W+D_+\), \(V=W+(-D)_+\). On either half-plane of \(D\), the Jacobian has absolute value one and the density becomes \(e^{-|d|-2w}\) for \(w>0\). It factors as \((e^{-|d|}/2)(2e^{-2w})\). Thus \(D\) is standard Laplace, \(W\) is exponential of rate two, and they are independent. Sorting the pairs as in step 1 proves the exact sampler. Sorting never changes the sums of either row's unnormalized exponentials; hence the first-row share equals the ratio of an independent \(\operatorname{Gamma}(n,1)\) numerator to the sum of two such variables. It has exactly the \(\operatorname{Beta}(n,n)\) distribution, proving the finite-\(n\) assertion.

**3. Uniform cumulative limit.** Let \(D_{(j)}\) denote the \(j\)-th order statistic of \(D_1,\ldots,D_n\), and sort the corresponding \(W_i\) with the same permutation. The strong law gives
\[
S_n/n\longrightarrow\mathbb E(|D|+2W)=2\quad\text{almost surely}.
\]
Since the standard Laplace law has finite first absolute moment, the empirical quantile \(Q_n(u)=D_{(\lceil nu\rceil)}\) converges to \(Q(u)\) in \(L^1(0,1)\), almost surely. One elementary proof truncates the sample at a fixed absolute threshold, applies uniform convergence of empirical distribution functions on the bounded interval, and then lets the threshold increase, controlling the empirical tails by the strong law. Consequently, uniformly in \(t\),
\[
\frac1n\sum_{j\le\lfloor nt\rfloor}(D_{(j)})_+
\longrightarrow\int_0^t(Q(u))_+\,du,
\quad
\frac1n\sum_{j\le\lfloor nt\rfloor}(-D_{(j)})_+
\longrightarrow\int_0^t(-Q(u))_+\,du.
\]
The interval discrepancy of length at most \(1/n\) vanishes uniformly because the quantile is integrable.

It remains to account for the \(W\)-marks, rather than incorrectly treating their sorted locations as deterministic. For each fixed real threshold \(x\), the strong law yields
\[
\frac1n\sum_{i=1}^n W_i\mathbf1_{\{D_i\le x\}}
\longrightarrow\frac12F_D(x).
\]
The functions of \(x\) on both sides are nondecreasing, and the limit is continuous. Apply the strong law on a countable dense grid and use monotonicity and tail control to obtain uniform convergence in \(x\). Combining this with uniform empirical-CDF convergence and the absence of ties gives
\[
\sup_{0\le k\le n}\left|
\frac1n\sum_{j=1}^kW_{\sigma(j)}-\frac{k}{2n}\right|\longrightarrow0
\quad\text{almost surely}.
\]
Division by \(S_n/n\to2\) proves the uniform limits
\[
A(t)=\frac t4+\frac12\int_0^t(Q(u))_+\,du,
\qquad
B(t)=\frac t4+\frac12\int_0^t(-Q(u))_+\,du.
\]
Evaluating the integrals on either side of \(1/2\) gives the two stated explicit formulas. Their difference has unique minimum \(-1/4\) at \(t=1/2\), and each total tends to \(1/2\).

**4. Joint extremes.** Put \(a_n(x)=\log(n/2)+x\). For all sufficiently large \(n\), the Laplace CDF \(F_D\) satisfies
\[
\Pr\{D_{(n)}\le a_n(x),\ -D_{(1)}\le a_n(y)\}
=\left[1-\frac{e^{-x}+e^{-y}}n\right]^n
\longrightarrow\exp(-e^{-x}-e^{-y}).
\]
This is precisely the product CDF of two independent standard Gumbel variables. Moreover \(S_n/(2n)-1=O_{\mathsf P}(n^{-1/2})\), while both extremes are \(O_{\mathsf P}(\log n)\), so replacing the extremes \(D_{(n)},-D_{(1)}\) by their normalized contrasts \((2n/S_n)D_{(n)},-(2n/S_n)D_{(1)}\) changes each centered quantity by \(o_{\mathsf P}(1)\). Joint Slutsky convergence proves the stated limit.

**5. Finite centroid.** The gamma sum \(S_n\) is independent of the entire normalized vector and its column-sorted version. Thus \(\mathbb E[D_{(j)}]=\mathbb E[S_n]\mathbb E[c_{1j}-c_{2j}]=2n\mathbb E[c_{1j}-c_{2j}]\). The probability integral transform represents \(D_{(j)}=Q(Z_j)\) with \(Z_j\sim\operatorname{Beta}(j,n+1-j)\). Integrating its density proves the exact centroid formula.

## Verification
The standalone standard-library script `verify_monge.py` checks the unique ordering-region partition for \(n=2,\ldots,7\), normalization and Monge inequalities of simulated uniform points, finite beta moments and exact last-contrast means, the entire two-row limiting profile in a sample of 40,000 columns, and the joint extreme CDF at zero. Execute `python3 verify_monge.py` in the file's directory. Its numerical checks are corroborative only: the preceding proof supplies the universal and asymptotic assertions. In particular, a finite sample cannot establish almost-sure convergence or independence in a limit.

## Relationship to prior work
Erickson and Kretschmann introduced and studied the normalized Monge polytope, including its vertices, facets, and the relative \(1/n!\) volume of the two-row case (arXiv:2311.07522, Sections 1, 2, and 5). Their normalization and volume theorem are prerequisites, not new findings here. The present result concerns the **complete uniform probability model**, its almost-sure **two-row cumulative limit shapes**, and the **joint independent Gumbel edge laws**; these are not determined by the volume fraction alone. Hütter, Mao, Rigollet, and Robeva (arXiv:1904.03136) study statistical estimation under noise, not the intrinsic uniform-volume law on these normalized polytopes. Standard Dirichlet, order-statistic, and exponential identities are used and not presented as new in isolation.

## Limitations
Only two-row normalized Monge polytopes are classified; no general \(p\)-row limit shape is asserted. The limit profiles require uniform intrinsic-volume sampling, not arbitrary Monge matrices or a uniform measure on vertices. The almost-sure statement uses the specified common-sequence coupling; for separately sampled dimensions, convergence in probability follows. Numerical tests neither prove the infinite statements nor eliminate the possibility of earlier equivalent work under different terminology. Independent mathematical validation has not been performed.

## References
1. W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522v2, first public version 2023-11-13, especially Sections 1, 2, and 5; https://arxiv.org/abs/2311.07522.
2. J.-C. Hütter, C. Mao, P. Rigollet, and E. Robeva, *Estimation of Monge Matrices*, arXiv:1904.03136v1, 2019; https://arxiv.org/abs/1904.03136.
