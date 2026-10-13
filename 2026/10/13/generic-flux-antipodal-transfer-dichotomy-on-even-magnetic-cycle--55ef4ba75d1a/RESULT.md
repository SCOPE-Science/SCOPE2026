# Generic-flux antipodal transfer dichotomy on even magnetic cycles

## Finding
Let \(n\ge 4\) be even and let \(H_\phi\) be the nearest-neighbor magnetic Hamiltonian on the cyclic vertex set \(\mathbb Z/n\mathbb Z\), with uniform unit-modulus directed hopping phase \(e^{i\phi}\). Define pretty good state transfer (PGST) in the usual continuous-time sense, with one overall physically irrelevant scalar phase.

**Theorem.** For every real \(\phi\), a pair of distinct vertices can have PGST only when the vertices are antipodal. If \(n\) has an odd prime factor, no pair has PGST, for any \(\phi\). More quantitatively, for each odd prime \(p\mid n\), every \(t\in\mathbb R\) satisfies
\[
\big|\langle a+n/2|e^{-itH_\phi}|a\rangle\big|\le 1-\frac1{pn}.
\]
If \(n=2^r\) with \(r\ge2\) and \(\tan\phi\) is transcendental, then PGST occurs between every pair of antipodes, but perfect state transfer (PST) occurs between no distinct vertices. Consequently PGST between antipodes holds for Lebesgue-almost-every flux parameter when and only when the even cycle order is a power of two; the exceptional set in the positive case is at most countable.

There are genuine exceptional phases in the positive orders: at \(\phi=\pi/n\), antipodal transfer amplitude is identically zero at every time. This special cancellation is a known type of zero-transfer phenomenon and is not claimed as a separate new discovery.

## Assumptions and scope
Let \(T\) be the cyclic right shift, \(Te_j=e_{j+1}\), and set
\[
H_\phi=e^{i\phi}T+e^{-i\phi}T^{-1},\qquad U_\phi(t)=e^{-itH_\phi}.
\]
The graph has \(n\ge4\) vertices and all hopping magnitudes are one; no onsite potentials or other edges are present. A pair \(a\ne b\) has PGST if for every \(\varepsilon>0\) there are \(t>0\) and \(\gamma\in\mathbb C\) with \(|\gamma|=1\) for which \(\|U_\phi(t)e_a-\gamma e_b\|<\varepsilon\). Equivalently an appropriate sequence approaches a fixed overall phase after passing to a subsequence. PST means exact equality at some \(t>0\). The phase \(\phi\) may be any real number; only the positive-case hypothesis excludes algebraic or undefined \(\tan\phi\).

The uniform Peierls phase has gauge-invariant total magnetic flux \(n\phi\pmod{2\pi}\). The first-public motivating source is Coutinho et al., *Irrational quantum walks*, arXiv:2208.08971 (2022-08-18, primary MSC 81P68). Its general number-theoretic viewpoint motivates this magnetic specialization, but its integral-Hamiltonian algorithm is not being claimed as a new lemma.

## Proof
**Fourier reduction.** Put \(\zeta=e^{2\pi i/n}\), and \(f_k(j)=n^{-1/2}\zeta^{kj}\), for \(0\le k<n\). These vectors form an orthonormal eigenbasis of \(H_\phi\), with
\[
\lambda_k=2\cos\!\left(\phi+\frac{2\pi k}{n}\right),\qquad
\lambda_{k+n/2}=-\lambda_k.
\]
By translation symmetry it suffices to study transfer from \(0\) to \(j\). Fourier expansion shows that PGST requires and is equivalent to simultaneous approximation
\[
e^{-it\lambda_k}\longrightarrow\gamma\zeta^{-jk}\quad(0\le k<n)
\]
along some times, with an overall phase \(\gamma\). For any integer vector \(\ell\) satisfying \(\sum_k\ell_k=0\) and \(\sum_k\ell_k\lambda_k=0\), multiplying these phase conditions implies
\[
\zeta^{j\sum_k k\ell_k}=1.\tag{1}
\]
Conversely, all such conditions (1) suffice by the continuous-time version of Kronecker's approximation theorem applied to the frequency differences \(\lambda_k-\lambda_0\), \(1\le k<n\). Indeed, an integer relation among those differences corresponds precisely to a balanced relation \(\ell\) above. This treatment of overall phase also handles coincident eigenvalues.

**Only antipodes.** For any \(k,l\), choose the balanced relation \(\ell=e_k+e_{k+n/2}-e_l-e_{l+n/2}\), interpreted as a vector on Fourier indices. It annihilates the frequency vector at every \(\phi\). Its weighted index sum is \(2(k-l)\). Taking \(k=0,l=1\) in (1) gives \(n\mid 2j\). Since \(0<j<n\) and \(n\) is even, \(j=n/2\).

**Odd-prime obstruction and its quantitative form.** Suppose an odd prime \(p\) divides \(n\), and put \(d=n/p\), which is even. For every \(k\), the geometric-series identity
\[
\sum_{h=0}^{p-1}\zeta^{k+hd}=0
\]
implies \(\sum_h\lambda_{k+hd}=0\), for every real \(\phi\). Subtract the identity at \(k=1\) from the one at \(k=0\). The resulting relation is balanced, while \(\sum_k k\ell_k=-p\). At the antipode \(j=n/2\), condition (1) would demand \((-1)^{-p}=1\), which is false. Thus no PGST exists at any phase.

For the asserted uniform bound, write \(z_k=e^{-it\lambda_k}\) and \(A=n^{-1}\sum_k(-1)^k z_k\). Choose \(\gamma=A/|A|\) if \(A\ne0\), or an arbitrary unit scalar otherwise, and set \(w_k=\overline\gamma(-1)^kz_k\). Since both \(p\)-term frequency sums vanish, \(\prod_hz_{hd}=\prod_hz_{1+hd}=1\). Since \(d\) is even and \(p\) is odd, the two products \(\prod_hw_{hd}\) and \(\prod_hw_{1+hd}\) are opposite complex unit numbers. Therefore
\[
2\le\sum_{h=0}^{p-1}\bigl(|w_{hd}-1|+|w_{1+hd}-1|\bigr)
\le\sqrt{2p}\sqrt{\sum_{k=0}^{n-1}|w_k-1|^2}.
\]
But \(\sum_k|w_k-1|^2=2n(1-|A|)\). Hence \(2\le2\sqrt{pn(1-|A|)}\), yielding \(|A|\le1-1/(pn)\).

**Generic power-of-two sufficiency.** Now let \(n=2^r\), \(r\ge2\), and \(\tan\phi\) be transcendental. Suppose integers \(\ell_k\) obey \(\sum_k\ell_k\lambda_k=0\). Writing \(\theta_k=2\pi k/n\) and expanding the cosines gives
\[
\sum_k\ell_k\cos\theta_k-\tan\phi\sum_k\ell_k\sin\theta_k=0.
\]
Both sums are algebraic real numbers (they lie in the cyclotomic field). Since \(\tan\phi\) is transcendental, both sums must separately vanish. Therefore the integer polynomial \(P(x)=\sum_{k=0}^{n-1}\ell_kx^k\) satisfies \(P(\zeta)=0\). The minimal polynomial of \(\zeta\) is exactly \(\Phi_n(x)=x^{n/2}+1\). Polynomial division over the rationals, or direct comparison of coefficients, now gives
\[
\ell_{k+n/2}=\ell_k\qquad(0\le k<n/2).\tag{2}
\]
If this relation is also balanced, (2) implies \(\sum_{k\ \mathrm{odd}}\ell_k\) is even, because \(n/2\) is even. At the antipode the phase compatibility (1) is exactly \((-1)^{\sum_{k\,\mathrm{odd}}\ell_k}=1\). Hence every balanced frequency relation is compatible, and Kronecker's theorem yields PGST. Translation symmetry gives the same statement for every antipodal pair.

**Generic nonexistence of exact transfer.** At exact antipodal transfer, the Fourier phase targets at indices \(0,n/2\) coincide, as do those at \(n/4,3n/4\), since \(n/2\) is even. Their respective eigenvalue pairs are \(\{2\cos\phi,-2\cos\phi\}\) and \(\{-2\sin\phi,2\sin\phi\}\). Thus PST at \(t>0\) would force \(4t\cos\phi\in2\pi\mathbb Z\) and \(4t\sin\phi\in2\pi\mathbb Z\). As \(\cos\phi\ne0\), their ratio makes \(\tan\phi\) rational, contradiction. No other target pair admits PGST, so none admits PST.

**Exceptional half flux.** At \(\phi=\pi/n\), \(\lambda_k=\lambda_{n-1-k}\) and the indices \(k\) and \(n-1-k\) have opposite parity. Pairing the terms of \(A=n^{-1}\sum_k(-1)^k e^{-it\lambda_k}\) gives \(A=0\) for all \(t\). Finally, the real algebraic values and poles of tangent form an at most countable set of phases modulo \(2\pi\); this establishes the almost-everywhere assertion.

## Verification
A standalone Python 3 script `verify.py` checks finite instances of the integer cycle-factor identities, parity obstruction, exact Fourier eigenvector relations, the uniform quantitative bound, and the half-flux cancellation. Representative search trajectories at \(\phi=\arctan(e)\) numerically approach antipodal transfer on the four- and eight-cycles. Since \(e\) is transcendental, this is an admissible test phase. All infinite-order and arbitrarily accurate conclusions are proved analytically above; numerical samples and finite algebraic checks are only supplementary diagnostics.

## Relationship to prior work
Pal and Bhattacharjya (2016 preprint; 2017 journal) prove the power-of-two antipodal criterion for **unphased real symmetric cycles** and related ordinary circulants. Cameron et al. (2013 preprint; 2014 journal) give general Hermitian-circulant transfer principles and an oriented **prime-order** family with universal PGST. Acuaviva et al. (2023) give general Hermitian spectral PGST criteria and rooted-product examples. Coutinho et al. (2022) give Kronecker-based decision methods for **integral** Hamiltonians. These tools and results are credited, not claimed new. Their theorems as stated do not decide arbitrary real uniform magnetic flux on every even cycle, nor imply the explicit phase-uniform odd-prime quantitative obstruction without a new implication argument. Sett et al. (2019) already demonstrate phase-induced zero transfer on even cycles, including a four-cycle example; the half-flux cancellation here is included only as a boundary illustration.

## Limitations
The theorem does not classify the exceptional algebraic-tangent phases on power-of-two rings. The bound \(1-1/(pn)\) is not claimed sharp. It treats only the uniform nearest-neighbor, unit-magnitude Hermitian cycle and does not give constructive bounds on the first approximate-transfer time for arbitrary precision. Literature comparisons do not constitute proof against unindexed equivalent results. 

## References
1. G. Coutinho, P. Ferreira Baptista, C. Godsil, T. J. Spier, R. Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first posted 2022-08-18), https://arxiv.org/html/2208.08971v1.
2. H. Pal and B. Bhattacharjya, *Pretty Good State Transfer on Circulant Graphs*, arXiv:1607.03598v1 (2016), https://arxiv.org/html/1607.03598v1.
3. S. Cameron, S. Fehrenbach, L. Granger, O. Hennigh, S. Shrestha, C. Tamon, *Universal State Transfer on Graphs*, arXiv:1310.3885v1 (2013), https://arxiv.org/html/1310.3885v1.
4. A. Acuaviva et al., *State Transfer in Complex Quantum Walks*, arXiv:2301.01473v1 (2023), https://arxiv.org/html/2301.01473v1.
5. A. Sett, H. Pan, P. E. Falloon, J. B. Wang, *Zero Transfer in Continuous Time Quantum Walks*, arXiv:1902.11115v1 (2019), https://arxiv.org/html/1902.11115v1.
