# Additive squared-multiplicity law and Legendre boundary profiles for optimal Hardy approximants

## Finding

Boundary zeros with different multiplicities contribute **independently, but quadratically in their multiplicities**, to the leading squared error of optimal polynomial inversion in the Hardy space. More precisely, with the definitions below,

\[
\|1-fq_n\|_{H^2}^2=\frac{\sum_{j=1}^{s}m_j^2}{n+d+1}+O_f((n+d+1)^{-2}).
\]

The full residual coefficient array also has an explicit **uniform** oscillatory profile:

\[
(n+d+1)\,[z^k](1-fq_n)=
\sum_{j=1}^{s}\overline{\zeta_j}^{\,k}\,
Q_{m_j}\!\left(\frac{k}{n+d+1}\right)
+O_f((n+d+1)^{-1}),
\qquad 0\le k\le n+d,
\]

where

\[
Q_m(t)=\sum_{\nu=0}^{m-1}(2\nu+1)(-1)^\nu P_\nu(2t-1),
\]

and \(P_\nu\) denotes the classical Legendre polynomial with \(P_\nu(1)=1\). For example, \(Q_1(t)=1\), \(Q_2(t)=4-6t\), and \(Q_3(t)=9-36t+30t^2\). The result addresses multiple **distinct** boundary nodes including at least one repeated zero; earlier simple-zero and one-node formulas alone do not state this mixed-jet law.

## Assumptions and scope

Let \(H^2\) be the classical Hardy space on the open unit disk, with \(\|\sum_{k\ge0}a_kz^k\|_{H^2}^2=\sum_{k\ge0}|a_k|^2\). Fix \(s\ge2\) pairwise distinct points \(\zeta_1,\ldots,\zeta_s\) on the complex unit circle. Fix positive integers \(m_1,\ldots,m_s\), at least one greater than one. Take

\[
f(z)=c\prod_{j=1}^{s}(z-\zeta_j)^{m_j},\quad c\in\mathbb C\setminus\{0\},\quad d=\sum_{j=1}^s m_j.
\]

For every integer \(n\ge0\), the polynomial \(q_n\) of degree at most \(n\) is the unique minimizer of \(\|1-fq\|_{H^2}\) over all such complex polynomials. Put \(N=n+d\), \(K=N+1\), and \(R_n(z)=1-f(z)q_n(z)=\sum_{k=0}^{K-1}a_{n,k}z^k\). The asymptotic limits keep \(s\), all \(\zeta_j\), and all \(m_j\) fixed. The implicit constants may depend on them.

## Proof

**1. Exact interpolation formulation.** Denote by \(\mathcal P_N\) the polynomials of degree at most \(N\). Since \(\deg f=d\), a polynomial \(R\in\mathcal P_N\) is equal to \(1-fq\) for some \(q\in\mathcal P_n\) if and only if \(R-1\) is divisible by \(f\). Equivalently, at each node \(\zeta_j\),

\[
R(\zeta_j)=1,\qquad R^{(\ell)}(\zeta_j)=0\quad(1\le\ell<m_j).
\]

The Euler derivative \(E=z\frac{d}{dz}\) is upper triangular in the ordinary-derivative jet with nonzero diagonal \(\zeta_j^\ell\) at each nonzero node. Thus these conditions are equivalent to

\[
(E^\ell R)(\zeta_j)=\delta_{\ell0},\qquad 0\le\ell<m_j.
\]

This reformulation exactly preserves all polynomial divisibility conditions, not merely their values at the nodes.

**2. Hermite Gramian.** Let \(I=\{(j,\ell):1\le j\le s,\ 0\le\ell<m_j\}\), so \(|I|=d\). Define the \(d\)-by-\(K\) matrix

\[
A_{(j,\ell),k}=k^\ell\zeta_j^k,\qquad 0\le k<K,
\]

where the standard convention \(0^0=1\) is used. Let \(b_{(j,\ell)}=\delta_{\ell0}\). Then the coefficients \(a=(a_{n,k})\) of an admissible residual satisfy exactly \(Aa=b\). The map of polynomials of degree less than \(d\) to their full jets at the distinct nodes is invertible by Hermite interpolation. Hence \(A\) has row rank \(d\). The unique minimum Euclidean-norm solution is

\[
a=A^*(AA^*)^{-1}b,\qquad
\|R_n\|_{H^2}^2=b^*(AA^*)^{-1}b.
\]

In particular this argument verifies existence and uniqueness of \(q_n\) for every \(n\ge0\).

**3. Diagonal scaling and node separation.** Write \(G=AA^*\) and define the positive diagonal matrix \(D_K\) on \(I\) by \((D_K)_{(j,\ell),(j,\ell)}=K^{\ell+1/2}\). The scaled Hermitian Gramian \(B_K=D_K^{-1}GD_K^{-1}\) has entries

\[
(B_K)_{(j,\ell),(h,v)}=
K^{-\ell-v-1}\sum_{k=0}^{K-1} k^{\ell+v}
(\zeta_j\overline{\zeta_h})^k.
\]

For \(j=h\), fixed-power Riemann sums yield \((B_K)_{(j,\ell),(j,v)}=1/(\ell+v+1)+O_f(K^{-1})\). For \(j\ne h\), the phase \(\lambda=\zeta_j\overline{\zeta_h}\) is not one, and summation by parts with the bounded geometric partial sums gives

\[
\sum_{k=0}^{K-1} k^{\ell+v}\lambda^k=O_{\lambda,\ell,v}(K^{\ell+v}),
\]

including the constant-power case. Consequently, in operator norm for the fixed-size matrices,

\[
B_K=\operatorname{diag}(H_{m_1},\ldots,H_{m_s})+O_f(K^{-1}),
\quad (H_m)_{ab}=\frac1{a+b+1}\quad(0\le a,b<m).
\]

Each \(H_m\) is strictly positive definite: it is the Gram matrix of \(1,t,\ldots,t^{m-1}\) in \(L^2[0,1]\). Fixed-dimensional inverse perturbation therefore proves

\[
B_K^{-1}=\operatorname{diag}(H_{m_1}^{-1},\ldots,H_{m_s}^{-1})+O_f(K^{-1}).
\]

The uniform constants exist because all nodes are fixed and distinct. This is the step at which geometry drops out of the leading term.

**4. Exact squared-error constant.** Let \(e\in\mathbb C^d\) have entry one at every zeroth-order jet and zero at every higher jet. Since \(D_K^{-1}b=K^{-1/2}e\),

\[
\|R_n\|_{H^2}^2=\frac1K e^*B_K^{-1}e
=\frac1K\sum_{j=1}^s(H_{m_j}^{-1})_{00}+O_f(K^{-2}).
\]

The inverse entry is determined without a tabulated inverse formula. The polynomial \(Q_m(t)=\sum_{a=0}^{m-1}(H_m^{-1})_{a0}t^a\) satisfies \(\int_0^1Q_m(t)t^b\,dt=\delta_{b0}\) for \(0\le b<m\), so it reproduces evaluation at zero on polynomials of degree less than \(m\). The orthonormal basis \(\sqrt{2\nu+1}P_\nu(2t-1)\) therefore gives

\[
Q_m(t)=\sum_{\nu=0}^{m-1}(2\nu+1)(-1)^\nu P_\nu(2t-1).
\]

At zero, \((H_m^{-1})_{00}=Q_m(0)=\sum_{\nu=0}^{m-1}(2\nu+1)=m^2\). Substitution yields the asserted sharp asymptotic with an absolute \(O_f(K^{-2})\) error.

**5. Every coefficient, uniformly.** By the minimum-norm formula, for each \(0\le k<K\),

\[
a_{n,k}=\sum_{j=1}^s\overline{\zeta_j}^{\,k}\sum_{\ell=0}^{m_j-1}
k^\ell (G^{-1}b)_{(j,\ell)}.
\]

The scaling and inverse estimate show, uniformly in the finite jet index,

\[
(G^{-1}b)_{(j,\ell)}=K^{-\ell-1}
\bigl((H_{m_j}^{-1})_{\ell0}+O_f(K^{-1})\bigr).
\]

Because \(0\le k/K<1\) and each \(m_j\) is fixed, multiplying by \(K\) and summing a fixed number of terms yields

\[
K a_{n,k}=\sum_{j=1}^s\overline{\zeta_j}^{\,k}Q_{m_j}(k/K)+O_f(K^{-1})
\]

**simultaneously for every index** \(0\le k<K\), as claimed.

## Verification

The accompanying standalone script `verify.py` computes the inverse finite Hermite Gramian directly for two genuinely mixed-multiplicity root configurations and compares its exact coefficient constraints, squared-error constant, and whole coefficient profile against the asymptotic formulas. It also constructs the first four reproducing polynomials by exact rational Hilbert-matrix inversion. The recorded output in `checks.txt` shows convergence of the normalized squared-error constants toward \(13\) for multiplicities \((2,3)\) at nodes \((1,-1)\), and toward \(5\) for multiplicities \((2,1)\) at nodes \((1,e^{2\pi i/3})\). These finite numerical computations provide checks, not a substitute for the all-degree proof above. Run with `python verify.py` from the folder containing that file; NumPy and SymPy are required.

## Relationship to prior work

Bénéteau, Manolaki, and Seco (arXiv:1901.00694, first public version January 2019) give a kernel-Gram method for optimal polynomial approximants with **simple** zeros and develop a one-node higher-multiplicity Hilbert-matrix calculation (Theorem 7.3). Their concluding remark 8(G) explicitly identifies different zeros with different multiplicities as a case they did not pursue. The present statement is not a claim to have invented the underlying Gramian method. Its contributions are the decoupled **mixed-node** leading constant, the second-order error, and the complete simultaneous coefficient profile in shifted Legendre polynomials. The leading constant \(\sum m_j^2\) is not obtained by treating repeated roots as independently distinct simple nodes (which would yield an incorrect linear multiplicity count).

The broader survey by Bénéteau and Centner discusses the use of polynomial approximants in least-squares digital inverse filtering. General derivative-kernel constructions and the one-node examples were also examined; they do not directly state this coupled asymptotic law. The relationship to older general confluent Christoffel-kernel asymptotics remains an originality risk: similar machinery could express this result without the same wording.

## Limitations

This result is restricted to classical unweighted \(H^2\), finitely many **fixed, pairwise distinct** unit-circle zeros, and fixed finite multiplicities. It does not assert constants uniform under merging nodes, moving nodes with degree, or multiplicities increasing with \(n\). It does not cover interior or exterior zeros, general analytic factors, weighted Dirichlet spaces, or the zeros of the optimal approximants themselves. The squared-error constant and the coefficient profile are asymptotic, not identities for finite degree. The finite checks use numerical linear algebra, whereas the general claim rests on the exact interpolation and block-moment proof.

## References

1. C. Bénéteau, M. Manolaki, D. Seco, *Boundary behavior of optimal polynomial approximants*, arXiv:1901.00694 (first made public 2019-01-03), Theorem 1.1, Section 7, and concluding remark 8(G). https://arxiv.org/abs/1901.00694
2. C. Bénéteau, J. Centner, *A survey of optimal polynomial approximants, applications to digital filter design, and related open problems*, arXiv:2102.01725. https://arxiv.org/abs/2102.01725
3. C. Bénéteau, D. Khavinson, C. Liaw, D. Seco, B. Simanek, *Zeros of optimal polynomial approximants: Jacobi matrices and Jentzsch-type theorems*, arXiv:1606.08615; earlier single-boundary-root computations. https://arxiv.org/abs/1606.08615
4. C. Felder, T. Le, *Analogues of finite Blaschke products as inner functions*, arXiv:2105.01766; derivative-kernel background. https://arxiv.org/abs/2105.01766
