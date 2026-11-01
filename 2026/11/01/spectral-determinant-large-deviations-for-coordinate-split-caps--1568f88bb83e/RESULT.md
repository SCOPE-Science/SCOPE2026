# Spectral determinant large deviations for coordinate-split caps in multivariate Fock spaces

## Finding

Fix integers \(d\ge3\) and \(1\le \ell<d\), and \(0<\tau<1\). Let \(\mathcal F^2(\mathbb C^d)\) be the Gaussian holomorphic Fock space with probability measure \(\pi^{-d}e^{-|z|^2}\,dV(z)\). Let \(\mathcal H_m\) be its subspace of homogeneous polynomials of total degree \(m\). Define the coordinate-split cone
\[
E_{d,\ell,\tau}=\left\{z\ne0:\frac{|z_1|^2+\cdots+|z_\ell|^2}{|z_1|^2+\cdots+|z_d|^2}>\tau\right\},
\]
and let \(T_m=P_m M_{\mathbf1_E}|_{\mathcal H_m}\) be the positive Toeplitz compression, where \(P_m\) is orthogonal projection onto \(\mathcal H_m\). For all integers \(m\ge0\), its eigenvalues and multiplicities, indexed by \(0\le k\le m\), are exactly
\[
\lambda_{m,k}=\sum_{j=0}^{k+\ell-1}\binom{m+d-1}{j}\tau^j(1-\tau)^{m+d-1-j},\qquad
w_{m,k}=\binom{k+\ell-1}{\ell-1}\binom{m-k+d-\ell-1}{d-\ell-1}.
\]
All eigenvalues lie strictly between zero and one. With \(\Delta_m=\det T_m=\prod_{k=0}^m\lambda_{m,k}^{w_{m,k}}\) and binary relative entropy
\[
I_\tau(x)=x\log\frac{x}{\tau}+(1-x)\log\frac{1-x}{1-\tau},\quad 0\le x\le1,
\]
using continuous endpoint values, the following **sharp log-determinant law** holds:
\[
-\log\Delta_m=\frac{m^d}{(\ell-1)!(d-\ell-1)!}\int_0^\tau x^{\ell-1}(1-x)^{d-\ell-1}I_\tau(x)\,dx+O_{d,\ell,\tau}\!\left(m^{d-1}\log(m+2)\right).
\]
The explicit leading coefficient is strictly positive. In particular, for \(d=3\), \(\ell=2\), \(\tau=1/2\),
\[
\lim_{m\to\infty}\frac{-\log\Delta_m}{m^3}=\frac{\log2}{6}-\frac5{48}>0.
\]

## Assumptions and scope

The dimension \(d\), split \(\ell\), and threshold \(\tau\) are fixed as \(m\to\infty\). The projector \(P_m\) acts on a **single** finite-dimensional homogeneous Fock sector, of dimension \(\binom{m+d-1}{d-1}\); this is not a statement about a Toeplitz operator on the entire Fock space. The cap is invariant under the diagonal circle and independent rotations of the two coordinate blocks. Strict inequality at the angular boundary makes no difference to Gaussian integrals.

## Proof

**Exact diagonalization.** The normalized monomials \(e_\alpha(z)=z^\alpha/\sqrt{\alpha!}\), with \(|\alpha|=m\), are orthonormal. Invariance under all coordinate phases forces the compression matrix to be diagonal in this basis. Let \(k=\alpha_1+\cdots+\alpha_\ell\). Under the density \(|e_\alpha(z)|^2\pi^{-d}e^{-|z|^2}\,dV(z)\), the variables \(|z_j|^2\) are independent gamma variables of shapes \(\alpha_j+1\) and common unit rate. Therefore the two coordinate-block sums have respective gamma shapes \(k+\ell\) and \(m-k+d-\ell\). Their ratio is beta distributed with those parameters. Its upper tail at \(\tau\), by the beta-binomial identity, equals the displayed binomial CDF with \(N=m+d-1\) trials and cutoff \(j=k+\ell-1\). Weak compositions within the two blocks give the multiplicity formula.

**Uniform logarithmic binomial tail estimate.** For \(X\sim\mathrm{Bin}(N,\tau)\), any \(0\le j\le N\) with \(j/N\le\tau\) satisfies
\[
\frac{e^{-N I_\tau(j/N)}}{N+1}\le \Pr\{X\le j\}\le e^{-N I_\tau(j/N)}.
\]
The lower bound uses the single mass \(\Pr\{X=j\}\) and the elementary method-of-types estimate \(\binom Nj(j/N)^j(1-j/N)^{N-j}\ge1/(N+1)\), including the endpoints by continuity. The upper bound is the binomial Chernoff inequality. If \(j/N>\tau\), the CDF includes a mode of the binomial law, so \(1/(N+1)\le\Pr\{X\le j\}\le1\). These give an all-index estimate
\[
-\log\lambda_{m,k}=N I_\tau\!\left(\frac{k+\ell-1}{N}\right)\mathbf1_{\{(k+\ell-1)/N\le\tau\}}+O(\log(N+1)),
\]
where \(0\le k\le m\) and the constant is absolute. For fixed \(d,\ell,\tau\), replacing \((k+\ell-1)/N\) by \(k/m\), and \(N\) by \(m\), changes the right side by at most \(O_{d,\ell,\tau}(\log(m+2))\), uniformly in \(k\): the binary relative entropy has modulus of continuity \(O(h\log(1/h))\) for increments \(h\downarrow0\), and is zero at \(x=\tau\), making the cutoff continuous. Thus for \(m\ge1\),
\[
-\log\lambda_{m,k}=m I_\tau(k/m)\mathbf1_{\{k/m<\tau\}}+O_{d,\ell,\tau}(\log(m+2)).
\]

**Weighted Riemann sum.** Uniform expansion of the exact binomial multiplicities gives
\[
w_{m,k}=\frac{m^{d-2}}{(\ell-1)!(d-\ell-1)!}(k/m)^{\ell-1}(1-k/m)^{d-\ell-1}+O_d(m^{d-3}),
\]
valid for every \(0\le k\le m\), including boundaries (the convention \(x^0=1\) applies). The function \(x^{\ell-1}(1-x)^{d-\ell-1}I_\tau(x)\mathbf1_{\{x<\tau\}}\) has bounded variation on \([0,1]\): its endpoint logarithmic derivative singularities are integrable, and it vanishes continuously at \(\tau\). Its Riemann-sum error is \(O(1/m)\). Since \(\sum_kw_{m,k}=\binom{m+d-1}{d-1}=O_d(m^{d-1})\), the uniform eigenvalue error contributes \(O(m^{d-1}\log(m+2))\). The multiplicity remainder contributes \(O(m^{d-1})\). Summing establishes the theorem.

**Positivity and example.** For \(x<\tau\), \(I_\tau(x)>0\), and the weight is positive for \(0<x<\tau\); hence the integral is positive. Elementary integration at \((d,\ell,\tau)=(3,2,1/2)\) yields \(\log2/6-5/48\). At \(m=1\), the eigenvalues are \(1/2\) once and \(7/8\) twice, giving \(\Delta_1=49/128\).

## Verification

The companion standard-library script `verify.py` checks exact beta-to-binomial identities, block multiplicity sums, the rational finite-degree example, the analytically evaluated coefficient, and supplementary numerical convergence for four parameter triples. Invoke `python3 verify.py` from the extracted package. These finite tests are supporting consistency checks; the uniform Chernoff/method-of-types bounds and weighted Riemann-sum argument establish the limit for all \(m\).

## Relationship to prior work

González-Flores, Dupont-García, López-Martínez, and Hérnandez-Zamora (2023) obtain operator decompositions for circle-invariant Toeplitz symbols on multivariate Fock space; the present spectral eigenvalue and logarithmic-determinant asymptotics impose the additional two-block cap geometry. Charles and Estienne (2018) prove spectral-window and regular trace asymptotics for discontinuous Berezin-Toeplitz symbols; these do not determine the present singular \(\log T_m\) trace, whose very small eigenvalues produce an order-\(m^d\) term. Byun and Park (2024) give asymptotics for spherical ensemble gaps on a complex Riemann surface; the present dimension \(d\ge3\) has a different multivariate degree-multiplicity structure. Quiroga-Barranco and Sánchez-Nungaray (2016) study torus-invariant projective-space Toeplitz operators and exact diagonalization, without the stated cap determinant rate. The possibility of an implication from a more general higher-dimensional gap large-deviation theorem remains a historical-priority risk.

## Limitations

This is a finite-sector spectral determinant law with fixed parameters, not a theorem for a growing complex dimension, a varying cap threshold, or general non-toric symbols. The error bound is not asserted to be optimal; no boundary-layer correction or limiting distribution for individual eigenvalues is claimed. The exact coefficient may be implicit in a more general determinantal-ensemble large-deviation principle, and no historical-priority certification or independent validation is claimed.

## References

1. C. González-Flores, L. A. Dupont-García, R. R. López-Martínez, and F. G. Hérnandez-Zamora, *Toeplitz Operators on Fock Space over Cn with Invariant Symbols under the Action of the Unit Circle*, Axioms 12 (2023), 1080. DOI: 10.3390/axioms12121080; first public 2023-11-25.
2. L. Charles and B. Estienne, *Entanglement entropy and Berezin-Toeplitz operators*, arXiv:1803.03149 (2018).
3. S.-S. Byun and S. Park, *Large gap probabilities of complex and symplectic spherical ensembles with point charges*, arXiv:2405.00386 (2024).
4. R. Quiroga-Barranco and A. Sánchez-Nungaray, *Separately radial and radial Toeplitz operators on the projective space and representation theory*, arXiv:1606.07379 (2016).
5. R. Berman, *Determinantal point processes and fermions on complex manifolds: large deviations and bosonization*, arXiv:0812.4224 (2008); broad background on determinantal large deviations.
