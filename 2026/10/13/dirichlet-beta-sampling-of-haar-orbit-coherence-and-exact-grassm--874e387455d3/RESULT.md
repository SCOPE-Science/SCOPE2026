# Dirichlet–Beta sampling of Haar-orbit coherence and exact Grassmannian rank laws

## Finding

Let \(d\ge2\), let \(\Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_d)\) be any fixed real diagonal matrix, and draw \(U\) from normalized Haar measure on \(\mathrm U(d)\). Write \(M=U\Lambda U^\dagger\), and let \(P=(P_1,\ldots,P_d)\) have the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. Define the nonnegative spectral variance
\[
 V_\Lambda(P)=\sum_{j=1}^d\lambda_j^2P_j-\left(\sum_{j=1}^d\lambda_jP_j\right)^2.
\]
There is an **exact factorization in distribution**
\[
 |M_{12}|^2\ \overset{\mathrm{law}}=\ V_\Lambda(P)Y,
\]
where \(Y\) is independent of \(P\), distributed as \(\operatorname{Beta}(1,d-2)\) if \(d\ge3\), and equal to one almost surely if \(d=2\). The same law holds for every ordered pair of distinct matrix entries. This factorization applies to **every prescribed spectrum**, including repeated eigenvalues, not only to rank-constrained projections.

For any two-level density matrix
\[
 \rho=a\Pi+b(I_d-\Pi),\qquad
 \operatorname{rank}\Pi=k,\quad1\le k\le d-1,\quad a,b\ge0,\quad ka+(d-k)b=1,
\]
put \(\Delta=a-b\). Then, for an independent \(X\sim\operatorname{Beta}(k,d-k)\),
\[
 |(U\rho U^\dagger)_{12}|^2\ \overset{\mathrm{law}}=\ \Delta^2X(1-X)Y.
\]
For every real \(s>0\), all absolute off-diagonal moments are consequently
\[
 \mathbb E\left[|(U\rho U^\dagger)_{12}|^s\right]
 =|\Delta|^s\frac{B(k+s/2,d-k+s/2)}{B(k,d-k)}
 \frac{\Gamma(1+s/2)\Gamma(d-1)}{\Gamma(d-1+s/2)}.
\]
Here \(B\) is Euler's beta function. If \(a=b\), the moments of positive order vanish, as the formula indicates.

For the natural Grassmannian family \(\rho=\Pi/k\), let \(C_{\ell_1}(\sigma)=\sum_{i\ne j}|\sigma_{ij}|\). The **exact mean coherence over all measurement bases** is
\[
 \boxed{\mathbb E_U C_{\ell_1}(U\Pi U^\dagger/k)
 =\frac{d-1}{k}\frac{\sqrt\pi}{2}\frac{\Gamma(d-1)}{\Gamma(d-1/2)}
 \frac{\Gamma(k+1/2)\Gamma(d-k+1/2)}{\Gamma(k)\Gamma(d-k)}.}
\]
It depends only on \(d\) and \(k\), not on the particular projector. Its asymptotic rank laws, as \(d\to\infty\), include
\[
 \begin{aligned}
 &k\ \text{fixed}:&&\frac{\mathbb E C_{\ell_1}}d\longrightarrow
 \frac{\sqrt\pi\,\Gamma(k+1/2)}{2k\,\Gamma(k)},\\
 &k/d\to\alpha\in(0,1):&&\frac{\mathbb E C_{\ell_1}}{\sqrt d}\longrightarrow
 \frac{\sqrt\pi}{2}\sqrt{\frac{1-\alpha}{\alpha}},\\
 &d-k=m\ \text{fixed}:&&\mathbb E C_{\ell_1}\longrightarrow
 \frac{\sqrt\pi\,\Gamma(m+1/2)}{2\Gamma(m)}.
 \end{aligned}
\]
Thus the average grows linearly for fixed rank, as the square root of dimension for a positive rank fraction, and remains bounded for fixed corank. For the pure and one-dimensional-corank endpoints, these means are exactly \(\pi(d-1)/4\) and \(\pi/4\), respectively.

## Assumptions and scope

All Hilbert spaces are complex; Haar measure on \(\mathrm U(d)\) has total mass one. The off-diagonal factorization permits any real eigenvalues \(\lambda_j\); positivity and trace one are needed only for the coherence interpretation. The two-level formula allows both pure and mixed states, and the gamma asymptotics require precisely the rank regimes displayed. For \(d=2\), the beta factor \(Y\) is interpreted as a degenerate unit point mass, not as a beta law with zero shape parameter. The object is the unnormalized sum-of-off-diagonal-moduli convention for \(C_{\ell_1}\), not a distance minimized over basis choices.

## Proof

By Haar invariance, the first row \(x=(U_{11},\ldots,U_{1d})\) is uniform on the unit sphere in \(\mathbb C^d\). Representing it by independent circular complex Gaussians normalized by their Euclidean length gives \(P_j=|x_j|^2\sim\operatorname{Dirichlet}(1,\ldots,1)\).

Conditional on \(x\), the second row \(w\) is uniform on the unit sphere of the complex \((d-1)\)-dimensional orthogonal complement of \(x\). Set \(\mu=\sum_j\lambda_jP_j\) and \(z=(\Lambda-\mu I_d)x\). Then \(z\perp x\), and
\[
 \|z\|^2=\sum_j(\lambda_j-\mu)^2P_j=V_\Lambda(P),\qquad
 M_{12}=\sum_j\lambda_jx_j\overline{w_j}=\langle w,z\rangle.
\]
For \(V_\Lambda(P)>0\), rotate coordinates inside \(x^\perp\) so that the first unit vector is \(z/\|z\|\). A uniformly random unit vector in \(\mathbb C^{d-1}\) has the squared modulus of its first coordinate distributed as \(\operatorname{Beta}(1,d-2)\) for \(d\ge3\), and identically one for \(d=2\). This conditional distribution is the same for every \(x\), so the factor can be chosen independent of \(P\). If \(V_\Lambda(P)=0\), both sides vanish. This proves the general law, including all degeneracies and the scalar case.

If \(\Lambda\) has eigenvalues \(a\) and \(b\) with multiplicities \(k\) and \(d-k\), additivity of independent gamma numerators in the Dirichlet representation gives \(X=\sum_{j:\lambda_j=a}P_j\sim\operatorname{Beta}(k,d-k)\). Elementary expansion gives \(V_\Lambda(P)=(a-b)^2X(1-X)\). Independence of \(X\) and \(Y\) follows from independence of \(P\) and \(Y\). The standard beta-integral identity
\[
 \mathbb E[X^{s/2}(1-X)^{s/2}]
 =\frac{B(k+s/2,d-k+s/2)}{B(k,d-k)}
\]
and the corresponding \(s/2\)-moment of \(Y\) give the moment formula (the latter is also one for \(d=2\)).

For \(\rho=\Pi/k\), the spectral gap is \(1/k\). Every off-diagonal matrix entry has the same modulus distribution and there are \(d(d-1)\) ordered off-diagonal entries. Multiply the \(s=1\) moment by \(d(d-1)\) and use \(B(k+1/2,d-k+1/2)/B(k,d-k)=\Gamma(k+1/2)\Gamma(d-k+1/2)/(d\Gamma(k)\Gamma(d-k))\) to obtain the boxed formula. Finally, \(\Gamma(t+1/2)/\Gamma(t)\sim\sqrt t\) and \(\Gamma(d-1)/\Gamma(d-1/2)\sim d^{-1/2}\), with fixed-factor gamma ratios retained at the edges, give the three asymptotic limits. No finite sample or numerical approximation enters the proof.

## Verification

The exact second-moment consequence for every Hermitian spectrum is
\[
 \mathbb E|M_{12}|^2=
 \frac{d\sum_j\lambda_j^2-(\sum_j\lambda_j)^2}{d(d^2-1)}.
\]
It follows independently by evaluating Dirichlet second moments \(\mathbb EP_iP_j=(1+\mathbf1_{i=j})/[d(d+1)]\) and \(\mathbb EY=1/(d-1)\). For \(\rho=\Pi/k\) it becomes \((d-k)/[kd(d^2-1)]\), the standard unitary-invariant covariance value. Exact gamma simplification yields, for instance, \(9\pi/20\) at \((d,k)=(4,2)\), \(9\pi/14\) at \((5,2)\), and \(25\pi/42\) at \((6,3)\). The accompanying standalone script independently checks these identities and runs seeded Haar-unitary Monte Carlo as a non-proof diagnostic. The general spectrum and rank formulas are established by the analytic argument above.

## Relationship to prior work

Cheng and Hall, *Complementarity relations for quantum coherence* (arXiv:1508.03240, Sec. IV A, equations (25)–(30)), define the Haar mean of \(\ell_1\)-coherence and obtain purity-based bounds; they do not give its exact value on the full two-level spectral family. Singh, Zhang and Pati (arXiv:1509.08939) treat Haar-random **pure** states and other coherence measures; the \(k=1\) endpoint here is included as a consistency case, not claimed as a new pure-state formula. Zhang, Singh and Pati (arXiv:1510.08859) average relative-entropy coherence in random mixed-state ensembles rather than the fixed-spectrum \(\ell_1\) orbit. Zhang (arXiv:1607.02294) develops exact relative-entropy coherence formulas in a Wishart-induced random mixed-state ensemble rather than a fixed-spectrum orbit or its \(\ell_1\) coherence. Meckes and Meckes (arXiv:1711.02710) provide Gaussian approximation theorems for entries on prescribed-eigenvalue orbits, not the stated finite-dimensional Dirichlet–Beta independence representation.

Classical Jacobi/matrix-beta distributions for blocks of Haar projections and Gelfand–Tsetlin/orbital-corner laws contain related finite-dimensional spectral information. These frameworks may be another route to selected marginal distributions, and the present result does not assert their absence or mathematical independence. Its claim is the explicit universal factorization with its exact coherence moment evaluation and three natural rank regimes, rather than new Haar invariance or new matrix-beta theory.

## Limitations

The beta-product closed-form absolute moments require two distinct eigenvalue levels. For an arbitrary spectrum the exact factorization still holds, but evaluating the residual Dirichlet expectation of a noninteger power may require integration; no universal elementary formula is asserted. The result concerns mean \(\ell_1\)-coherence, not concentration of its full sum, optimal coherence over bases, or operational monotonicity. It proves no claim for real orthogonal Haar matrices, whose beta parameters differ. Preexisting general orbital-corner distribution theory and possible later restatements under random-projection terminology are meaningful literature-overlap risks.

## References

1. S. Cheng and M. J. W. Hall, *Complementarity relations for quantum coherence*, arXiv:1508.03240 (2015), Sec. IV A. https://arxiv.org/abs/1508.03240
2. U. Singh, L. Zhang and A. K. Pati, *Average coherence and its typicality for random pure states*, arXiv:1509.08939 (2015), Secs. III–IV. https://arxiv.org/abs/1509.08939
3. L. Zhang, U. Singh and A. K. Pati, *Average subentropy, coherence and entanglement of random mixed quantum states*, arXiv:1510.08859 (2015), Sec. IV. https://arxiv.org/abs/1510.08859
4. L. Zhang, *Average coherence and its typicality for random mixed quantum states*, arXiv:1607.02294 (2016), Sec. 4. https://arxiv.org/abs/1607.02294
5. E. S. Meckes and M. W. Meckes, *Random matrices with prescribed eigenvalues and expectation values for random quantum states*, arXiv:1711.02710 (2017), Thm. 2. https://arxiv.org/abs/1711.02710
6. C. Cuenca, *Universal behavior of the corners of orbital beta processes*, arXiv:1807.06134 (2018), introduction and orbital-corners framework. https://arxiv.org/abs/1807.06134
