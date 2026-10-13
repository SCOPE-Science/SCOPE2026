# Single-trap capture universality and detector thresholds on prime four-regular cycles

## Finding

Consider the four-regular circulant graph \(G(p,m)\) with the vertices \(\mathbb Z_p\) for an odd prime \(p\ge5\), and edges at offsets \(\pm1\) and \(\pm m\), where \(2\le m\le(p-1)/2\). Let \(S\) be ANY nonempty set of \(r\) absorbing vertices, with strictly positive but otherwise arbitrary local absorption rates. Define
\[
d=\begin{cases}4,&m^2\equiv-1\pmod p,\\2,&\text{otherwise.}\end{cases}
\]
Then the absorbing-subspace dimension is **exactly**
\[
R(p,m,r)=1+\frac{p-1}{d}\min(r,d).
\]
Thus absorption eventually occurs with probability one for EVERY initial density matrix if and only if \(r\ge d\). The absorbing probability from the completely mixed state \(I/p\) is \(R(p,m,r)/p\), and from an incoherent uniform mixture of the \(p-r\) non-sink basis states, when \(r<p\), it is \((R(p,m,r)-r)/(p-r)\).

The stronger **sitewise universality** assertion holds for one sink \(S=\{s\}\): for each \(x\ne s\),
\[
P_{\mathrm{abs}}(|x\rangle\langle x|)=\frac1d;
\qquad P_{\mathrm{abs}}(|s\rangle\langle s|)=1.
\]
In particular, any one non-sink site is captured with probability exactly \(1/2\) for generic chord length, and \(1/4\) for the arithmetic exceptional chord length, irrespective of distance to the sink. The exceptional case occurs for precisely one permitted \(m\) when \(p\equiv1\pmod4\), and never when \(p\equiv3\pmod4\).

## Assumptions and scope

The Hilbert space is \(\mathcal H=\mathbb C^p\), with orthonormal vertex states \(|x\rangle\). Hopping on each of the four distinct edges has real common amplitude one. Its Hamiltonian is the adjacency matrix \(H=A(G(p,m))\); replacing it by the regular-graph Laplacian \(4I-H\) does not change the absorbing subspace. For local detector rates \(\gamma_s>0\), set
\[
\Gamma=\sum_{s\in S}\gamma_s|s\rangle\langle s|,\qquad H_{\mathrm{eff}}=H-\frac{i}{2}\Gamma,
\qquad T_t=e^{-itH_{\mathrm{eff}}}.
\]
The eventual absorption probability of an initial density matrix \(\rho\) is \(1-\lim_{t\to\infty}\operatorname{Tr}(T_t\rho T_t^\dagger)\). The model is finite-dimensional, with no alternative loss or dephasing channels. No claim is made about convergence rates, disorder, or composite-order networks.

## Proof

**(1) Exact spectrum, including every accidental collision.** Write \(\zeta=e^{2\pi i/p}\) and \(f_k(x)=p^{-1/2}\zeta^{kx}\). The Fourier modes \(f_k\), \(0\le k<p\), form a unitary eigenbasis with
\[
\lambda_k=\zeta^k+\zeta^{-k}+\zeta^{mk}+\zeta^{-mk},\qquad\lambda_0=4.
\]
For two indices \(k,\ell\) with \(\lambda_k=\lambda_\ell\), subtract their expressions to form an integer polynomial \(F(X)\) of degree at most \(p-1\), with \(F(\zeta)=0\) and \(F(1)=0\). Minimality of the cyclotomic polynomial \(\Phi_p(X)=1+X+\cdots+X^{p-1}\) implies \(F=c\Phi_p\) over \(\mathbb Q\). Evaluating at one gives \(cp=0\), so \(F=0\). Thus the four exponent multisets \(\{k,-k,mk,-mk\}\) and \(\{\ell,-\ell,m\ell,-m\ell\}\) coincide modulo \(p\), not merely their sums of roots. For \(k\ne0\) the four exponents are distinct because \(m\not\equiv\pm1\pmod p\). Therefore \(\ell\in\{\pm k,\pm mk\}\); the extra identifications \(\lambda_k=\lambda_{mk}\) are consistent precisely when \(m^2\equiv-1\pmod p\), since \(m^2\equiv1\pmod p\) is excluded. There are \((p-1)/d\) distinct nontrivial eigenvalues, each of multiplicity \(d\), and the eigenvalue four is simple. This known spectral classification is explicitly credited to Harrison–Pruss, Proposition 3 (2024); the argument is reproduced to fix hypotheses and to support the subsequent detector calculation.

**(2) Every detector placement has the same restricted rank.** For an eigenspace with Fourier-frequency set \(K\subset\mathbb Z_p\), the restriction map to detector coordinates \(S\) is the \(r\)-by-\(|K|\) matrix \(p^{-1/2}(\zeta^{sk})_{s\in S,k\in K}\). Chebotarev's prime Fourier minor theorem says that **every square minor** of this matrix is nonzero. It follows that its rank is \(\min(r,|K|)\), including whenever \(S\) is arbitrarily and asymmetrically placed. Since the rate matrix is positive on the detector coordinates, the space of undetectable eigenvectors in eigenspace \(E_\lambda\) is precisely \(E_\lambda\cap\ker\Gamma\), of codimension \(\min(r,\dim E_\lambda)\). Summing over the one simple eigenspace and the \((p-1)/d\) higher-multiplicity eigenspaces yields the claimed \(R(p,m,r)\).

**(3) Spectral invisibility is exactly permanent quantum survival.** Set \(\mathcal D=\bigoplus_\lambda(E_\lambda\cap\ker\Gamma)\), and let \(Q\) be its orthogonal projector. This subspace reduces both the Hermitian matrix \(H\) and \(\Gamma\); on it, \(H_{\mathrm{eff}}=H\) is unitary dynamics. On \(\mathcal D^\perp\), suppose \(H_{\mathrm{eff}}v=zv\). Taking imaginary parts of the inner product gives
\[
\operatorname{Im}z=-\frac{\langle v,\Gamma v\rangle}{2\|v\|^2}\le0.
\]
Equality would force \(\Gamma v=0\) and \(Hv=zv\); then \(v\in\mathcal D\), contrary to the restriction. Thus all eigenvalues on the orthogonal complement lie in the **open** lower half-plane. Its matrix exponential decays to zero, even in the presence of Jordan blocks. Consequently \(\lim_{t\to\infty}\operatorname{Tr}(T_t\rho T_t^\dagger)=\operatorname{Tr}(Q\rho)\) for every density matrix, proving the exact rank-based absorption statements and independence from positive sink strengths.

**(4) Sitewise uniformity requires an additional character-sum identity.** Put the unique sink at \(s=0\) by translation. When \(m^2\equiv-1\pmod p\), let \(G=\{1,-1,m,-m\}\subset\mathbb F_p^\times\), a multiplicative subgroup of order \(d=4\); otherwise take \(G=\{1,-1\}\), of order \(d=2\). In either case, the nonzero spectral classes are precisely cosets \(K=kG\). Their normalized detector-bright eigenvectors are \(b_K=d^{-1/2}\sum_{j\in K}f_j\), while \(f_0\) is also bright. The bright projector is
\[
B=|f_0\rangle\langle f_0|+\sum_K|b_K\rangle\langle b_K|.
\]
At a vertex \(x\ne0\), the diagonal entry is
\[
\langle x|B|x\rangle=\frac1p+\frac1{pd}\sum_K\left|\sum_{j\in K}\zeta^{jx}\right|^2.
\]
Expand the square and write the second index as \(hj\) for \(h\in G\). Every nonzero frequency \(j\) occurs once across the cosets; character orthogonality gives
\[
\sum_K\left|\sum_{j\in K}\zeta^{jx}\right|^2
=\sum_{h\in G}\sum_{j=1}^{p-1}\zeta^{jx(1-h)}
=(p-1)-(d-1)=p-d,
\]
because \(x\ne0\). Therefore \(\langle x|B|x\rangle=1/p+(p-d)/(pd)=1/d\). At the sink, every Fourier class is entirely bright at that coordinate, so \(\langle0|B|0\rangle=1\). Translation proves the claimed sitewise formulas for general \(s\). Finally, \(m^2\equiv-1\) has solutions modulo \(p\) exactly when \(p\equiv1\pmod4\), and the pair of roots \(\pm m\) supplies exactly one permitted representative in the stated interval.

## Verification

A standalone finite verifier is included as `verify.py` with dependencies `requirements.txt`. Run `python verify.py` in an environment with NumPy and SciPy. The completed run reported `VERIFY_OK graph_detector_cases=1079 prime_step_models=57 sitewise_capture=1348 loss_eigenspectrum=4`. It checks all admissible chord lengths for eight primes, 1,079 detector-subset cases by independent numerical Hermitian eigenspaces and SVD, 1,348 non-sink sitewise probabilities, and four non-Hermitian loss spectra. These are **finite numerical cross-checks only**. The infinite theorem follows from the exact cyclotomic and character-sum proof plus Chebotarev's full-spark theorem.

## Relationship to prior work

Xu's 2008 long-range interacting cycle model uses the same four-regular graphs and investigates trapping numerically, without the present prime-order detector-rank and sitewise capture statements. The complete prime-order four-regular circulant **spectral multiplicity classification** is already contained in Harrison and Pruss (2024), Proposition 3; **this classification is not claimed as novel**. The nonsingularity of every prime Fourier minor is classical Chebotarev (proofs by Tao and Frenkel). Novo and collaborators, and Razzoli and collaborators, establish the general bright/dark spectral picture for coherent quantum transport. The present contribution is the evaluated detector-placement theorem and, in particular, the distance-independent sitewise \(1/2\)-versus-\(1/4\) capture law derived by the coset character sum. The theorem is a synthesis of established spectral tools, and broader unpublished or unlocated coverage remains a genuine priority risk.

## Limitations

The model uses identical real hopping on all four edges, prime graph order, positive but otherwise arbitrary local irreversible absorber rates, no dephasing or onsite disorder, and infinite-time survival. Finite-time absorption rates, perturbative robustness near exceptional chord parameters, composite-order graphs, and arbitrary initial coherent-state survival beyond the given projector formula are not determined. A source search does not prove absolute publication novelty; the 2024 spectrum result is a particularly close antecedent. No independent external audit has been performed.

## References

1. T. Tao, *An uncertainty principle for cyclic groups of prime order*, arXiv:math/0308286 (first publicly posted 2003-08-29), https://arxiv.org/pdf/math/0308286.
2. P. E. Frenkel, *Simple proof of Chebotarev's theorem on roots of unity*, arXiv:math/0312398 (2003-12-22), https://arxiv.org/pdf/math/0312398.
3. X.-P. Xu, *Coherent exciton transport and trapping on long-range interacting cycles*, arXiv:0812.3452v1 (2008-12-18), https://arxiv.org/pdf/0812.3452.
4. L. Novo et al., *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209, https://arxiv.org/pdf/1412.7209.
5. L. Razzoli, M. G. A. Paris, and P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794, https://arxiv.org/pdf/2011.13794.
6. J. Harrison and C. Pruss, *Circulant graphs as an example of discrete quantum unique ergodicity*, arXiv:2411.09028, Proposition 3, https://arxiv.org/pdf/2411.09028.
