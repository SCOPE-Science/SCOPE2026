# A universal squared-distance Gaussian cutoff on four-subset Johnson slices

## Finding

Let \(n\ge 8\) be an integer, let \(\mathcal X_n=\binom{[n]}4\), and give it the Johnson graph distance \(d(A,B)=4-|A\cap B|\). For \(0<q\le1\), define the \(\binom n4\)-square kernel matrix
\[
K_{n,q}(A,B)=q^{d(A,B)^2}.
\]
Let \(\rho\) be the unique zero in \((1/4,1/3)\) of
\[
F(q)=1-4q+6q^4-4q^9+q^{16};\qquad \rho\approx0.2564867889554649.
\]
Then for every \(n\ge8\):

1. \(K_{n,q}\) is strictly positive definite for \(0<q<\rho\).
2. At \(q=\rho\) it is positive semidefinite, with rank exactly \(\binom n3\) and nullity \(\binom n4-\binom n3\).
3. It is indefinite for every \(\rho<q<1\).
4. At \(q=1\) it is the all-ones matrix, of rank one.

Thus the admissible parameter set is \((0,\rho]\cup\{1\}\). In damping coordinates \(q=e^{-t}\), with \(t\ge0\), this is \(t=0\) or \(t\ge-\log\rho\approx1.360678120744664\). The sharp threshold is **independent of the ground-set size** \(n\), although the covariance matrix size grows as \(\binom n4\).

There is a spectral reentry that does **not** restore positivity: the top Johnson harmonic coefficient is positive at \(q=19/20\), but another harmonic coefficient is negative there. Hence following the top coefficient alone beyond its first zero gives an incorrect positivity test.

## Assumptions and scope

The ground set has \(n\ge8\) elements, every observation is a 4-element subset, and \(d\) is the shortest-path metric of \(J(n,4)\). This is **not** the Euclidean distance of the binary indicator vectors: their squared Euclidean distance equals \(2d\), not \(d^2\). All matrix positivity assertions concern real (equivalently complex Hermitian) quadratic forms. The endpoint \(q=1\) is included; \(q=0\) is excluded by the parameter definition.

## Proof

**1. A positive-incidence decomposition.** For each integer \(0\le j\le4\), let \(M_j\) be the 0--1 incidence matrix with rows indexed by \(A\in\mathcal X_n\), columns indexed by \(j\)-subsets \(T\) of \([n]\), and entries \(M_j(A,T)=1_{T\subseteq A}\). Then
\[
(M_jM_j^{\mathsf T})(A,B)=\binom{|A\cap B|}{j}.
\]
Newton's finite binomial expansion of \(f(s)=q^{(4-s)^2}\) at integer points \(0\le s\le4\) gives the **exact identity**
\[
K_{n,q}=\sum_{j=0}^4\gamma_j(q)M_jM_j^{\mathsf T},
\]
with
\[
\begin{aligned}
\gamma_0&=q^{16},\\
\gamma_1&=q^9-q^{16},\\
\gamma_2&=q^4-2q^9+q^{16},\\
\gamma_3&=q-3q^4+3q^9-q^{16},\\
\gamma_4&=1-4q+6q^4-4q^9+q^{16}=F(q).
\end{aligned}
\]
For \(0<q\le1/3\), the first four coefficients are strictly positive. Indeed, \(\gamma_2\ge q^4(1-2q^5)>0\) and \(\gamma_3\ge q(1-3q^3-q^{15})>0\), while the first two are immediate. Also
\[
F'(q)=-4+24q^3-36q^8+16q^{15}<-4+24(13/25)^3<0
\]
for \(0<q\le13/25\), since \(-36q^8+16q^{15}<0\). Direct substitution gives \(F(1/4)>0\) and \(F(1/3)<0\). Therefore \(F\) has exactly one root \(\rho\in(1/4,1/3)\), and \(\gamma_4>0\) before it. Since \(M_4\) is the identity, \(K_{n,q}\) is strictly positive definite for \(0<q<\rho\), and positive semidefinite at \(q=\rho\).

**2. Exact rank at the boundary.** At \(q=\rho\), the first four coefficients \(\gamma_0,\ldots,\gamma_3\) remain strictly positive and \(\gamma_4=0\). Every column of \(M_j\) for \(j\le3\) lies in the column space of \(M_3\), since
\[
M_3B_{3j}=\binom{4-j}{3-j}M_j,
\]
where \(B_{3j}(T,U)=1_{U\subseteq T}\). Thus \(\ker K_{n,\rho}=\ker(M_3^{\mathsf T})\) and \(\operatorname{rank}K_{n,\rho}=\operatorname{rank}M_3\).

For completeness, the subset incidence matrix from \(t\)-subsets to \(k\)-subsets has independent columns whenever \(t\le k\le n-t\) (over characteristic zero). Prove this by induction on \(t\). If its columns have coefficients \(c_T\) whose sum over each \(k\)-set vanishes, compare the equations for \(S\cup\{x\}\) and \(S\cup\{y\}\), with \(|S|=k-1\) disjoint from \(x,y\). By the induction hypothesis applied to \((t-1,k-1,n-2)\), one has \(c_{R\cup\{x\}}=c_{R\cup\{y\}}\) for every \((t-1)\)-subset \(R\) disjoint from \(x,y\). Since the graph of \(t\)-subsets connected by a one-element exchange is connected, all \(c_T\) are equal. Their sum over each \(k\)-set is zero, so every coefficient is zero. The base case \(t=0\) is immediate. Apply this with \(t=3,k=4,n\ge8\): \(M_3\) has column rank \(\binom n3\), proving the stated rank and nullity.

**3. Sharp obstruction on eight points.** It suffices to exhibit a negative quadratic form on the principal submatrix indexed by the 4-subsets of any fixed 8-element subset; this principal submatrix is present for every \(n\ge8\). Partition those eight points into the four pairs \(\{1,2\},\{3,4\},\{5,6\},\{7,8\}\). For \(j=3,4\) define
\[
v_j(A)=\prod_{s=1}^j\left(1_{2s-1\in A}-1_{2s\in A}\right).
\]
These are nonzero eigenvectors of \(K_{8,q}\). To see this directly, if \(A\) contains both or neither members of any of the first \(j\) pairs, swapping that pair fixes \(A\) and negates \(v_j\), so the kernel convolution vanishes at \(A\). If \(A\) contains exactly one from each such pair, pair flips and permutations of the unpaired coordinates show the ratio \((K_{8,q}v_j)(A)/v_j(A)\) is constant. Evaluate it on \(A=\{1,3,5,7\}\) by counting how many of the selected pair representatives are reversed. The resulting eigenvalues are
\[
\lambda_4(q)=\sum_{i=0}^4(-1)^i\binom4i q^{i^2}=F(q),
\]
\[
\lambda_3(q)=\sum_{i=0}^3(-1)^i\binom3i\big(q^{i^2}+q^{(i+1)^2}\big)
=1-2q+2q^9-q^{16}.
\]
The latter factors exactly as
\[
\lambda_3(q)=-(1-q)^2(1+q)(1+q^2)(1+q^4)
\left(\sum_{i=1}^7 q^i-1\right).
\]
For \(\rho<q\le13/25\), strict decrease of \(F\) gives \(\lambda_4(q)<0\). For \(13/25\le q<1\), the final parenthesis in \(\lambda_3\) is positive, because it increases with \(q\) and
\[
13/25+(13/25)^2+(13/25)^3+(13/25)^4>1.
\]
Hence \(\lambda_3(q)<0\) there. This proves indefiniteness for every \(\rho<q<1\) simultaneously for all \(n\ge8\). Finally \(q=1\) yields the all-ones matrix. At \(q=19/20\), exact rational substitution gives \(\lambda_4>0\) and \(\lambda_3<0\), confirming the claimed non-restorative top-sector reentry.

## Verification

Run `python3 check.py` from this package directory. It uses only the Python standard library. It checks exact rational Gram-matrix eigenvector identities for the degree-three and degree-four pair-difference vectors on \(J(8,4)\) and \(J(9,4)\), four rational parameter values, the full Johnson trace and squared-trace identities, sign witnesses, and a 135-step rational bracketing of \(\rho\). These finite tests supplement, rather than replace, the all-\(n\) incidence proof and the analytic negativity bounds. Independently check the displayed Newton coefficients, the factorization of \(\lambda_3\), and the inductive full-column-rank lemma for the infinite-dimensional quantifier.

## Relationship to prior work

Yuval Filmus (arXiv:1406.0142, first posted 2014-06-01), especially Section 4 and Lemma 4.3, gives an orthogonal harmonic basis for the Johnson association scheme and explains why all intersection-radial matrices share harmonic eigenspaces. That supplies a general spectral framework, but no universal squared-Johnson-distance Gaussian cutoff or its explicit boundary rank. Feragen--Lauze--Hauberg (arXiv:1411.0296, first posted 2014-11-02) study geodesic exponential kernels on path-geodesic spaces and uniform-in-bandwidth positivity; their flatness criterion does not classify a single finite Johnson scheme as damping changes. Damase--Pascoe (arXiv:2602.09010, first posted 2026-02-09), Sections 4 and 6--7, develop general positive-definite extension/preservation theory on homogeneous spaces; the inspected analysis does not compute this specific scalar polynomial cutoff.

The novelty here, subject to the limitations below, is the closed all-ground-set-size parameter classification, the proof by incidence positivity versus a fixed eight-point obstruction, and the exact rank at the transition. General Eberlein/Johnson eigenvalue formulas alone give a test, not the present sign and monotonicity conclusions. The result should not be conflated with the ordinary Euclidean Gaussian on 4-subset indicator vectors, which is positive definite for every positive bandwidth.

## Limitations

This theorem concerns *only* 4-element subsets and squared shortest-path distance, not all Johnson slice sizes, all distance exponents, or arbitrary radial profiles. The root \(\rho\) is algebraically defined rather than expressible in elementary radicals. The proof is complete within its stated mathematical assumptions but has not received independent validation; literature searches cannot establish absolute uniqueness, and equivalent unindexed calculations are a residual originality risk. The theorem does not imply positivity for the full Boolean cube with its squared Hamming metric.

## References

1. Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142, originally posted 2014-06-01, https://arxiv.org/abs/1406.0142.
2. A. Feragen, F. Lauze, S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296, originally posted 2014-11-02, https://arxiv.org/abs/1411.0296.
3. S. S. Damase, J. E. Pascoe, *Complete discrete Schoenberg-Delsarte theory for homogeneous spaces*, arXiv:2602.09010, originally posted 2026-02-09, https://arxiv.org/abs/2602.09010.
