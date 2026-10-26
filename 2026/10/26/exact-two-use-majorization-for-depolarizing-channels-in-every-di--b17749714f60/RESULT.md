# Exact two-use majorization for depolarizing channels in every dimension

## Finding

**Theorem.** For every integer \(d\ge 2\), every physical depolarizing parameter \(0\le p\le d^2/(d^2-1)\), and every density operator \(\rho\) on \(\mathbb C^d\otimes\mathbb C^d\), define
\[
\mathcal D_{p,d}(X)=(1-p)X+\frac{p}{d}\operatorname{Tr}(X)I_d,
\qquad \tau=\mathcal D_{p,d}(|0\rangle\langle0|).
\]
Then the decreasing eigenvalue vector of the two-use output is majorized by that of the pure-product output:
\[
\boxed{\lambda^\downarrow\!\left[(\mathcal D_{p,d}\otimes\mathcal D_{p,d})(\rho)\right]
\prec\lambda^\downarrow(\tau\otimes\tau).}
\]
In particular, **every** Ky Fan eigenvalue sum of the two-use output is bounded by the corresponding sum for \(\tau\otimes\tau\); the majorization defect is **exactly zero** at two uses, including the physical branch \(p>1\). This proves the \(n=2\) case of the arbitrary-copy majorization conjecture stated in [1], in every finite local dimension, without proving the conjecture for \(n\ge3\).

## Assumptions and scope

A density operator is positive semidefinite with trace one. Majorization \(x\prec y\) means that the nonincreasing coordinates have \(\sum_{j=1}^k x_j\le\sum_{j=1}^k y_j\) for every \(1\le k<d^2\), with equality at \(k=d^2\). Write
\[
a=1-p,\qquad b=p/d,\qquad \alpha=a+b,\qquad\beta=b.
\]
Complete positivity is precisely \(-1/(d^2-1)\le a\le1\) [2,3]. The pure one-use output has eigenvalues \(\alpha\) once and \(b\) with multiplicity \(d-1\). For \(a\ge0\), the decreasing eigenvalues of \(\tau^{\otimes2}\) are
\[
\alpha^2\ (1),\quad\alpha b\ (2d-2),\quad b^2\ ((d-1)^2),
\]
where parentheses denote multiplicities. For \(a<0\) the order reverses: \(b^2\) (multiplicity \((d-1)^2\)), \(\alpha b\) (multiplicity \(2d-2\)), and \(\alpha^2\) (multiplicity one). No claim is made about three or more uses, unequal local channels, or infinite dimension.

## Proof

**1. Reduction and exact block decomposition.** Ky Fan sums are convex, so it suffices to prove the inequality for a pure input; a spectral decomposition of a mixed input then gives the result by convexity. Covariance under all local unitaries reduces any pure input to Schmidt form
\[
|\psi\rangle=\sum_{i=1}^d\sqrt{\lambda_i}|ii\rangle,
\quad \lambda_i\ge0,\quad\sum_i\lambda_i=1.
\]
Put \(v=(\sqrt{\lambda_1},\ldots,\sqrt{\lambda_d})^T\) and \(\Lambda=\operatorname{diag}(\lambda_i)\). The output \(Z\) satisfies the exact identity
\[
Z=b^2 I_{d^2}+ab(\Lambda\otimes I_d+I_d\otimes\Lambda)+a^2|\psi\rangle\langle\psi|.
\tag{1}
\]
Consequently, on the \(d\)-dimensional diagonal subspace \(\operatorname{span}\{|ii\rangle\}\), it has matrix
\[
Z_{\rm diag}=b^2 I_d+2ab\Lambda+a^2 vv^*,
\tag{2}
\]
while each \(|ij\rangle\), \(i\ne j\), is an eigenvector with eigenvalue
\[
z_{ij}=b^2+ab(\lambda_i+\lambda_j).
\tag{3}
\]

**2. The rank-one Gram inequality.** For every probability vector \(\lambda\),
\[
I_d+vv^*-2\Lambda
=\sum_{1\le i<j\le d}(\sqrt{\lambda_j}e_i+\sqrt{\lambda_i}e_j)
(\sqrt{\lambda_j}e_i+\sqrt{\lambda_i}e_j)^*\succeq0.
\tag{4}
\]
Indeed the diagonal entry on the left is \(1-\lambda_i=\sum_{j\ne i}\lambda_j\), and the off-diagonal \((i,j)\) entry is \(\sqrt{\lambda_i\lambda_j}\), exactly as on the right. Thus \(2\Lambda-I_d\preceq vv^*\).

**3. Nonnegative depolarizing coefficient \(a\ge0\).** Equations (2) and (4) imply
\[
Z_{\rm diag}\preceq\alpha b I_d+a\alpha vv^*.
\tag{5}
\]
The right side has one eigenvalue \(\alpha^2\) and the remaining \(d-1\) eigenvalues equal to \(\alpha b\). Equation (3) gives \(z_{ij}\le\alpha b\), since \(\lambda_i+\lambda_j\le1\). Equation (1) also gives \(Z\succeq b^2I_{d^2}\), because \(a,b\ge0\). Hence the largest eigenvalue of \(Z\) is at most \(\alpha^2\), every eigenvalue except possibly the largest is at most \(\alpha b\), and every eigenvalue is at least \(b^2\). For \(1\le k\le 2d-1\), the sum of the largest \(k\) eigenvalues is at most \(\alpha^2+(k-1)\alpha b\). For \(2d-1\le k\le d^2\), subtracting the \(d^2-k\) smallest eigenvalues gives an upper bound \(1-(d^2-k)b^2\). These are exactly the corresponding two pieces of the pure-product Lorenz curve.

**4. Negative depolarizing coefficient \(a=-c<0\).** Physical complete positivity gives
\[
0<c\le\frac1{d^2-1},\qquad b=\frac{1+c}{d},
\qquad\frac cb\le\frac1d,\qquad\alpha=b-c>0.
\tag{6}
\]
On the diagonal subspace, (2) and (4) yield the **lower** rank-one bound
\[
Z_{\rm diag}\succeq\alpha b I_d-c\alpha vv^*.
\tag{7}
\]
This has one eigenvalue \(\alpha^2\) and \(d-1\) eigenvalues \(\alpha b\). By (3), all off-diagonal eigenvalues obey \(z_{ij}\ge\alpha b\). Therefore \(Z\) has *at most one* eigenvalue below \(\alpha b\), and its smallest eigenvalue is at least \(\alpha^2\).

To upper-bound the entire spectrum, set \(T=\Lambda\otimes I_d+I_d\otimes\Lambda\). If \(r\le d\) is the number of nonzero Schmidt coefficients, the Cauchy–Schwarz inequality gives, for every vector \(u\),
\[
|\langle\psi,u\rangle|^2=\left|\sum_{\lambda_i>0}\sqrt{\lambda_i}\,u_{ii}\right|^2
\le r\sum_i\lambda_i|u_{ii}|^2\le\frac d2\langle u,Tu\rangle.
\]
Thus \(|\psi\rangle\langle\psi|\preceq(d/2)T\). In view of (6),
\[
Z-b^2I_{d^2}=-bcT+c^2|\psi\rangle\langle\psi|
\preceq\left(-bc+\frac{dc^2}{2}\right)T\preceq0.
\tag{8}
\]
So **every** eigenvalue is at most \(b^2\). For \(1\le k\le(d-1)^2\), the largest \(k\) sum to at most \(kb^2\). For \(k>(d-1)^2\), set \(m=d^2-k\le2d-2\); the smallest \(m\ge1\) eigenvalues sum to at least \(\alpha^2+(m-1)\alpha b\), by (7), while \(m=0\) is the trace equality. These bounds match the pure-product Lorenz curve. Hence majorization holds also for \(a<0\).

**5. Mixed inputs.** For a decomposition \(\rho=\sum_s q_s|\psi_s\rangle\langle\psi_s|\), the Ky Fan variational characterization gives
\[
\mathcal K_k((\mathcal D\otimes\mathcal D)(\rho))
\le\sum_s q_s\mathcal K_k((\mathcal D\otimes\mathcal D)(|\psi_s\rangle\langle\psi_s|))
\le\mathcal K_k(\tau^{\otimes2}).
\]
Traces equal one. This completes the proof for all stated \(d,p,\rho\).

## Verification

The derivation above is finite-dimensional and algebraic; no random enumeration or floating-point result is needed for the theorem. The standalone `verify.py` checks the exact Gram identity with rational Schmidt amplitudes and exercises all Ky Fan inequalities numerically for random pure inputs in dimensions \(2,3,4,5,7\), including \(p=0,1\) and the maximal physical \(p\). Run `python3 verify.py` with NumPy installed. This tests examples and endpoints, **not** the universally quantified assertion, which rests on steps (1)–(8).

## Relationship to prior work

Song, Wang, Tomamichel and Fang [1] formulate exactly this majorization ordering for arbitrary tensor power \(n\), prove a log-determinant ordering for every \(n\), and derive asymptotic approximate majorization; they do not give a two-use exact majorization theorem. King's earlier work [2] proves multiplicativity of output Schatten norms and capacity additivity for all copies, but those norm inequalities alone do not give the individual Ky Fan partial sums. Lami and Huber [3] exhibit the bipartite Schmidt-block form and classify positivity/entanglement-annihilation properties of a broad class of maps, but do not establish this Lorenz-curve ordering. The present proof uses a rank-one Gram inequality to control **both** the high and low ends of the two-use spectrum, including the \(a<0\) completely positive regime.

## Limitations

The result proves a two-use instance, not the full arbitrary-copy conjecture; it does not give a nonzero stability gap or a constructive mixed-unitary converter. The Schmidt decomposition and local unitary covariance require identical finite local dimensions and the same depolarizing channel on both sides. The result is exact for the entire physical parameter interval, but makes no assertion about positive non-completely-positive parameters or unequal channels. Priority is assessed against the sources actually inspected; a mathematically equivalent result in additional literature may exist.

## References

[1] Z. Song, X. Wang, M. Tomamichel, and K. Fang, *Approximate majorization and high-order capacity of quantum depolarizing channels*, arXiv:2609.37240v1 (first public 2026-09-29), https://arxiv.org/html/2609.37240v1 .

[2] C. King, *The capacity of the quantum depolarizing channel*, arXiv:quant-ph/0204172v2 (2002), https://arxiv.org/html/quant-ph/0204172v2 .

[3] L. Lami and M. Huber, *Bipartite depolarizing maps*, arXiv:1603.02158v1 (2016), https://arxiv.org/html/1603.02158v1 .
