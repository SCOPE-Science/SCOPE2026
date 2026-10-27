# Two-detector absorption ranks on all finite Hamming graphs

## Finding

Let \(q\ge2\) and \(d\ge1\) be integers, and let \(u\ne v\) be vertices of the Hamming graph \(H(d,q)=K_q^{\square d}\). In the continuous-time one-excitation walk with two strictly positive local irreversible absorbers at \(u,v\), define the transport efficiency of a density matrix \(\rho\) by
\[
\eta(\rho)=1-\lim_{t\to\infty}\operatorname{tr}(e^{-itH_{\mathrm{eff}}}\rho e^{itH_{\mathrm{eff}}^\dagger}).
\]
Write \(h=\operatorname{dist}(u,v)\). The exact dimension \(R\) of the subspace ultimately absorbed is
\[
\boxed{R=\begin{cases}
2d+1,&q\ge3,\\
d+1,&q=2,\ h=d,\\
2d,&q=2,\ 1\le h<d.
\end{cases}}
\]
Thus the uniform-initial-vertex average is \(\overline\eta=R/q^d\). The rate parameters do not enter this formula. For \(q\ge3\), **every** distinct pair of absorbers is equally efficient on average, irrespective of its Hamming distance. In the binary cube, antipodal absorbers are perfectly redundant at the level of accessible spectral modes: the second adds no absorbing modes, whereas every nonantipodal second absorber adds exactly \(d-1\) modes beyond the single-absorber dimension \(d+1\).

There is also an exact individual-vertex formula. Define the generalized Krawtchouk integers
\[
K_k(s)=\sum_{j=0}^{k}(-1)^j(q-1)^{k-j}\binom{s}{j}\binom{d-s}{k-j},
\quad B_k=\binom dk(q-1)^k,
\]
where out-of-range binomial coefficients vanish. Put \(a=\operatorname{dist}(x,u)\), \(b=\operatorname{dist}(x,v)\), and \(c_k=K_k(h)\). For each level with \(|c_k|<B_k\), set
\[
E_k(x)=\frac{B_k(K_k(a)^2+K_k(b)^2)-2c_kK_k(a)K_k(b)}{q^d(B_k^2-c_k^2)}.
\]
For each level with \(|c_k|=B_k\), instead set \(E_k(x)=K_k(a)^2/(q^dB_k)\). Then
\[
\boxed{\eta(|x\rangle\langle x|)=\sum_{k=0}^d E_k(x).}
\]
In particular, for \(q=2\) and \(h=d\), this specializes to \(\eta(|x\rangle\langle x|)=1/\binom d a\). For a binary adjacent pair, choose coordinates \(u=(0,0,\ldots,0)\) and \(v=(1,0,\ldots,0)\); then \(\eta(|x\rangle\langle x|)=1/\binom{d-1}{s}\), where \(s\) counts nonzero entries among the last \(d-1\) coordinates. Both expressions remain valid at the small-size boundaries (including \(d=1\)).

For \(q^d>2\), the average conditioned on starting outside the two absorbing vertices is exactly \((R-2)/(q^d-2)\).

## Assumptions and scope

The vertices are words in \((\mathbb Z/q\mathbb Z)^d\), with an edge whenever two words differ in exactly one coordinate. All edge hopping strengths are one. Let \(A\) be the real symmetric adjacency matrix and define
\[
H_{\mathrm{eff}}=A-\frac i2\left(\gamma_u|u\rangle\langle u|+\gamma_v|v\rangle\langle v|\right),\qquad \gamma_u,\gamma_v>0.
\]
The dynamics is \(\psi(t)=e^{-itH_{\mathrm{eff}}}\psi(0)\), with norm loss corresponding to irreversible absorption. Absorption fractions are infinite-time limits. There is no time-dependent hopping, disorder, dephasing, external replenishment, or additional monitored vertex. Arbitrarily small but strictly positive absorber strengths are permitted; at zero strength the theorem's two-monitor hypothesis is not satisfied.

## Proof

**1. General bright-space lemma.** For any finite Hermitian \(A\) with spectral projectors \(P_\lambda\), and any positive diagonal loss supported on a set \(T\) of basis vertices, define
\[
\mathcal B=\bigoplus_\lambda\operatorname{span}\{P_\lambda|w\rangle:w\in T\}.
\]
Its orthogonal complement consists exactly of eigenvectors of \(A\) annihilated by all monitored bras. Both \(\mathcal B\) and \(\mathcal B^\perp\) are invariant under \(A\) and the loss matrix. On \(\mathcal B^\perp\), evolution is unitary. Any eigenvector \(z\) of \(H_{\mathrm{eff}}|_{\mathcal B}\) with an eigenvalue of zero imaginary part would satisfy \(\langle z,\Gamma z\rangle=0\); positivity implies \(\Gamma z=0\) and then \(Az\) is a real scalar multiple of \(z\). This would place \(z\) in \(\mathcal B^\perp\), a contradiction. Consequently all eigenvalues on \(\mathcal B\) have strictly negative imaginary parts, and the finite-dimensional exponential tends to zero there even in the presence of Jordan blocks. Hence \(\eta(\rho)=\operatorname{tr}(P_{\mathcal B}\rho)\), regardless of the positive rates.

**2. Hamming eigenspaces and Gram matrices.** Under Fourier characters of \((\mathbb Z/q\mathbb Z)^d\), the adjacency eigenvalues are \(\lambda_k=d(q-1)-qk\), for \(0\le k\le d\), corresponding to characters nontrivial in exactly \(k\) coordinates. Their multiplicities are \(B_k=\binom dk(q-1)^k\). Character orthogonality gives the exact spectral-projector kernel
\[
\langle x|P_k|y\rangle=q^{-d}K_k(\operatorname{dist}(x,y)).
\]
Thus the Gram matrix of the projected monitor vectors \(P_k|u\rangle,P_k|v\rangle\) is \(q^{-d}\begin{pmatrix}B_k&K_k(h)\\K_k(h)&B_k\end{pmatrix}\). Its rank is two exactly when \(|K_k(h)|<B_k\), and otherwise one. The global bright dimension is the sum of those ranks over distinct \(k\).

**3. Every strictness case.** At \(k=0\), the Fourier character is constant, giving rank one. If \(q\ge3\), take any coordinate in which \(u\) and \(v\) differ. For every \(1\le k\le d\), choose a Fourier character with that coordinate active, then vary just its nontrivial frequency. Two such characters have different relative phases on \(u,v\), because the coordinate difference is nonzero and \(q\ge3\). Therefore not all character phases coincide, and the triangle inequality is strict: \(|K_k(h)|<B_k\). The ranks sum to \(1+2d\).

For \(q=2\), when \(h=d\), every character at level \(k\) has the same relative phase \((-1)^k\). Hence all \(d+1\) levels have rank one. If \(1\le h<d\), at each \(1\le k\le d-1\), choose one active coordinate in the differing support and one in its complement. Two size-\(k\) character supports can be chosen by exchanging these coordinates, keeping the other \(k-1\) coordinates fixed. Their relative phases have opposite signs. Therefore all interior levels have rank two, whereas the one-dimensional extreme levels \(k=0,d\) have rank one. The sum is \(2+2(d-1)=2d\).

**4. Initial-state formula and special cases.** For an invertible two-column Gram matrix, the squared norm of the orthogonal projection of \(|x\rangle\) onto the two projected monitor vectors is the stated quadratic form \(E_k(x)\); if the columns are collinear, the squared projection is \(K_k(a)^2/(q^d B_k)\). Orthogonality of distinct spectral levels allows summation. For binary antipodal monitors, the generated bright space is the one-monitor radial subspace spanned by normalized Hamming-weight shells around \(u\); this gives \(1/\binom da\) for a basis-vertex initial state. For an adjacent binary pair, the bright subspace is all of the first-coordinate factor \(\mathbb C^2\) tensored with the radial subspace of the remaining \(d-1\) coordinates; this gives \(1/\binom{d-1}s\). Finally, for the maximally mixed state \(q^{-d}I\), \(\eta=\operatorname{tr}P_{\mathcal B}/q^d=R/q^d\). Each monitored basis state lies in \(\mathcal B\), proving the outside-monitors conditional average.

## Verification

The accompanying executable \(verify_two_monitor.py\) constructs independent full adjacency matrices, builds every spectral projector by a polynomial in that matrix, and compares projector ranks and every initial-vertex absorption probability with the explicit formulas. In an execution using NumPy and SciPy, all 23 two-monitor distance cases across nine graph families passed, totaling 394 site-level comparisons. A separate full non-Hermitian matrix exponential at time \(t=900\) for \(H(2,3)\), positive and unequal loss rates, gave average survival \(0.4444444444443397\), agreeing with the exact \(4/9\). These finite checks corroborate, rather than replace, the proof for all integers \(q,d\).

## Relationship to prior work

Novo et al. (first public preprint 2014-12-22; journal 2015) established the invariant/Krylov-subspace method and derived single-absorber hypercube efficiency \((d+1)/2^d\). Their hypercube calculation places one trap at a corner and does not classify two positive absorbers or nonbinary Hamming graphs. The present theorem uses the known bright-space principle but determines the new two-vertex spectral rank for every alphabet, dimension and monitor separation. Razzoli, Paris and Bordone (2020 preprint, 2021 article) consider a single trap on graphs and explicitly identify multiple traps and their locations as a direction for further work. These general approaches make the calculation possible, but neither cited source supplies the evaluated two-monitor classification. The model is continuous-time coherent transport with irreversible local loss; it is distinct from discrete-time coined multi-marked quantum search.

## Limitations

The result concerns ideal homogeneous Cartesian powers of complete graphs, precisely two distinct vertices with strictly positive localized absorption, and infinite-time absorption probability. It does not determine conditional absorption times or optimize loss strengths, and it does not apply directly to decoherence, disorder, multiple excitations, or more than two absorbers. Spectral-rank comparisons with other treatments of multi-monitor observability may exist; an exhaustive bibliography-level priority search and independent mathematical audit have not been performed.

## References

1. L. Novo, S. Chakraborty, M. Mohseni, H. Neven, Y. Omar, *Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs*, arXiv:1412.7209 (first submitted 2014-12-22); *Scientific Reports* **5**, 13304 (2015), doi:10.1038/srep13304.
2. L. Razzoli, M. G. A. Paris, P. Bordone, *Transport efficiency of continuous-time quantum walks on graphs*, arXiv:2011.13794 (2020 preprint; 2021 article).
3. T. Yamasaki, H. Kobayashi, H. Imai, *Analysis of absorbing times of quantum walks*, *Physical Review A* **68**, 012302 (2003), doi:10.1103/PhysRevA.68.012302. This is discrete-time coined absorption rather than the present model.
