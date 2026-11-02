# Rational-resonance and site-selective absorption laws on two-coupling quantum hypercubes

## Finding

For every pair of integers \(a,b\ge1\), consider a continuous-time single-excitation quantum walk on the Boolean hypercube \(\{0,1\}^{a+b}\). Edges changing one of the first \(a\) bits have hopping strength \(J>0\), while edges changing one of the remaining \(b\) bits have hopping strength \(J\rho\), where \(\rho>0\). An absorbing sink of any positive rate is placed at the all-zero vertex.

**Exact resonance classification.** The sink-accessible (bright) subspace has dimension \((a+1)(b+1)\) except at the finite set of reduced positive ratios \(\rho=u/v\), with \(1\le u\le a\), \(1\le v\le b\), and \(\gcd(u,v)=1\). At such a ratio its dimension is exactly
\[
D_{u/v}=(a+1)(b+1)-(a+1-u)(b+1-v).
\]
Thus the eventual absorption probability from a maximally mixed single-excitation state is \(D_\rho/2^{a+b}\). The number of distinct exceptional positive ratios is
\[
R(a,b)=\sum_{m=1}^{\min(a,b)}\mu(m)\left\lfloor\frac a m\right\rfloor\left\lfloor\frac b m\right\rfloor,
\]
where \(\mu\) is the Möbius function.

**Capture from an arbitrary vertex.** Write \(r\) for the Hamming weight of the first block and \(s\) for the second. For \(0\le k\le a\), define
\[
K_k(r;a)=\sum_{j=\max\{0,k-a+r\}}^{\min\{k,r\}}(-1)^j\binom rj\binom{a-r}{k-j}.
\]
Let \(\mathcal F_\rho\) be the partition of \(\{0,\ldots,a\}\times\{0,\ldots,b\}\) into equal-value fibers of \(k+\rho l\). Then the exact eventual absorption probability is
\[
\eta_\rho(r,s)=\frac1{2^{a+b}}\sum_{F\in\mathcal F_\rho}
\frac{\left(\sum_{(k,l)\in F}K_k(r;a)K_l(s;b)\right)^2}
{\sum_{(k,l)\in F}\binom ak\binom bl}.
\]
For a nonexceptional coupling all fibers are singletons, and the formula factors into the product of the corresponding two blockwise Krawtchouk sums.

**Exact complete-capture sites.** At nonexceptional \(\rho\), exactly four starting vertices are absorbed with certainty: the four block corners \((\epsilon_1 1^a,\epsilon_2 1^b)\), with \(\epsilon_1,\epsilon_2\in\{0,1\}\). At an exceptional ratio \(\rho=u/v\), exactly two of those corners remain completely captured, precisely those satisfying
\[
\epsilon_1u+\epsilon_2v\equiv0\pmod2.
\]
At every exceptional ratio, absorption from each vertex is no greater than the corresponding probability at any nonexceptional ratio. In particular, the resonance reduces average absorption strictly.

## Assumptions and scope

The single-excitation Hilbert space is \(\mathbb C^{2^{a+b}}\). With \(X_i\) denoting the coordinate-flip operator, define
\[
H_\rho=J\sum_{i=1}^{a}X_i+J\rho\sum_{i=a+1}^{a+b}X_i.
\]
Let \(o=0^{a+b}\), and for an absorption parameter \(\kappa>0\) put
\[
H_{\mathrm{eff}}=H_\rho-i\frac\kappa2|o\rangle\langle o|,
\qquad
\eta_\rho(z)=1-\lim_{t\to\infty}\|e^{-itH_{\mathrm{eff}}}|z\rangle\|^2.
\]
All statements concern the infinite-time limit; \(J,\kappa\) can be any positive numbers and do not change that limit. \(\eta_\rho(r,s)\) denotes \(\eta_\rho(z)\) for any vertex with blockwise Hamming weights \((r,s)\).

## Proof

**1. Spectral projectors and capture.** For a binary frequency \(\omega=(\alpha,\beta)\), the normalized Walsh character \(2^{-(a+b)/2}(-1)^{\alpha\cdot x+\beta\cdot y}\) is an eigenvector of \(H_\rho\) with eigenvalue \(J[(a-2k)+\rho(b-2l)]\), where \(k=|\alpha|\), \(l=|\beta|\). Hence equal-energy frequency pairs are precisely the fibers of \(k+\rho l\). If \(P_F\) is the orthogonal projector onto one energy eigenspace, then
\[
\|P_F|o\rangle\|^2=2^{-(a+b)}\sum_{(k,l)\in F}\binom ak\binom bl>0.
\]
The vectors \(P_F|o\rangle\), over distinct fibers, are nonzero and mutually orthogonal. Their span \(\mathcal B\) is invariant under both \(H_\rho\) and \(H_{\mathrm{eff}}\); its orthogonal complement \(\mathcal D\) is invariant under \(H_\rho\) and is orthogonal to the sink. Therefore evolution on \(\mathcal D\) is unitary. An eigenvector of \(H_{\mathrm{eff}}\) with real eigenvalue must have zero sink amplitude, by taking the imaginary part of its inner-product eigenvalue equation. There is no such eigenvector in \(\mathcal B\), because within each eigenspace \(\mathcal B\) has only the direction \(P_F|o\rangle\), with nonzero sink overlap. Every eigenvalue of the finite matrix \(H_{\mathrm{eff}}|_{\mathcal B}\) consequently has strictly negative imaginary part. Evolution on \(\mathcal B\) decays to zero, including possible Jordan blocks. Thus
\[
\eta_\rho(z)=\|\Pi_{\mathcal B}|z\rangle\|^2
=\sum_F\frac{|\langle z|P_F|o\rangle|^2}{\|P_F|o\rangle\|^2}.
\]
This shows that \(D_\rho\), the number of fibers, is exactly \(\dim\mathcal B\), and also yields mixed-state capture \(D_\rho/2^{a+b}\).

**2. Count the spectral collisions.** Two distinct rectangle points \((k,l)\), \((k',l')\) share a fiber only when \(k-k'=-\rho(l-l')\). As the differences are integers with \(|k-k'|\le a\), \(|l-l'|\le b\), this is possible exactly for reduced positive ratios \(\rho=u/v\) with \(1\le u\le a\), \(1\le v\le b\). At such a ratio the energy index is \(vk+ul\); successive lattice points on any fiber differ by the primitive step \((u,-v)\). Every fiber is a single unbranched lattice chain. Among the \((a+1)(b+1)\) lattice points there are \((a+1-u)(b+1-v)\) forward chain edges, so subtracting edges from vertices gives the stated number of components/fibers. Möbius inversion on \(\gcd(u,v)=1\) gives the exceptional-ratio count.

**3. Derive every site probability.** The Walsh character sum over all frequencies with block weights \((k,l)\) evaluated at a vertex \((x,y)\) of weights \((r,s)\) is \(K_k(r;a)K_l(s;b)\). Therefore
\[
\langle z|P_F|o\rangle=2^{-(a+b)}\sum_{(k,l)\in F}K_k(r;a)K_l(s;b).
\]
Substitution into the orthogonal projection identity in Step 1 gives the asserted exact rational formula, including its normalization. For singleton fibers, the product decomposition follows by separating the two sums. Within a merged fiber, Cauchy–Schwarz gives
\[
\frac{(\sum_F A_{kl})^2}{\sum_F B_{kl}}
\le \sum_F\frac{A_{kl}^2}{B_{kl}},\quad
A_{kl}=K_k(r;a)K_l(s;b),\ B_{kl}=\binom ak\binom bl>0,
\]
so no site's capture probability can increase at resonance compared with nonresonant coupling.

**4. Classify complete capture.** Since \(\Pi_{\mathcal B}\) is an orthogonal projector, \(\eta_\rho(z)=1\) exactly when \(|z\rangle\in\mathcal B\). Even at resonance, the spectral subspaces of weight pairs \((1,0)\) and \((0,1)\) contain independent Fourier modes within each class. In each such class the projection of \(|z\rangle\) is parallel to that of \(|o\rangle\) only if all bits in the corresponding coordinate block agree (for a one-bit block this requirement is automatic). Thus \(z\) must be one of the four block corners. Conversely, at such a corner every Walsh frequency with weights \((k,l)\) has sign \((-1)^{\epsilon_1k+\epsilon_2l}\). At nonexceptional ratios there is no merging of distinct pairs, so all four corners are bright. At \(\rho=u/v\), a chain step changes this sign by \((-1)^{u\epsilon_1+v\epsilon_2}\), making the corner bright exactly under the displayed parity condition. Since \(\gcd(u,v)=1\), this nonzero linear functional over \(\mathbb F_2^2\) has a two-element kernel. Exactly two corners therefore remain fully captured. This proves all assertions.

## Verification

Two standalone Python programs accompanying this result independently calculate exact rational spectral-fiber projectors and numerical full-Walsh projectors, and additionally propagate the non-Hermitian evolution. They test a finite range of block sizes, coupling ratios, initial sites, ranks and complete-capture conditions. Reproduction requires Python 3, NumPy and SciPy; execute `python3 check_resonances.py` and `python3 check_evolution.py` in the directory containing the programs. Expected output from these exact files is recorded in `CHECKS.txt`. Finite experiments do not establish the arbitrary-dimensional result, which is proved above.

For \(a=2,b=3\), generic coupling has \(D_\rho=12\) of 32 states bright and four fully captured corners; the exceptional ratio \(\rho=1\) has \(D_\rho=6\) and two fully captured corners; at \(\rho=1/2\), it has \(D_\rho=8\) and two fully captured corners.

## Relationship to prior work

Moore and Russell (2001) diagonalize uniform continuous-time hypercube walks using Fourier characters and establish the underlying product-walk structure; that diagonalization, not the new resonance count, is known. Le, Donati, Severini and Caruso (2017) analyze the dark-state obstruction and the benefit of breaking degeneracies on general quantum networks. Razzoli, Paris and Bordone (2021) provide the general transport/Krylov-subspace viewpoint and examples of absorbent graph families. Makmal and collaborators (2015) study nonlocal and nonsymmetric **discrete-time coined** hypercube walks. The present theorem differs by classifying every positive **two-block hopping ratio** for a one-sink continuous-time hypercube, the exact rank loss at each arithmetic resonance, and the per-site and complete-capture parity laws. The possibility of a specialized prior result on the same two-block spectral model remains a priority risk; independent novelty review is outstanding.

## Limitations

Only one irreversible point sink, coherent single-excitation evolution, two uniform positive classes of coordinate hopping, a finite Boolean hypercube and infinite-time capture are considered. The formula does not give the finite-time absorption rate or behavior under disorder, dephasing, multiple sinks, or more than two independently tuned coupling classes. Independent scientific audit has not been performed.

## References

1. C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137v1 (first public 2001-04-29), https://arxiv.org/abs/quant-ph/0104137.
2. T. P. Le, L. Donati, S. Severini and F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482 (2017), https://arxiv.org/abs/1707.07482.
3. L. Razzoli, M. G. A. Paris and P. Bordone, *Transport Efficiency of Continuous-Time Quantum Walks on Graphs*, *Entropy* **23** (2021), 85, https://doi.org/10.3390/e23010085.
4. A. Makmal and collaborators, *Quantum walks on embedded hypercubes: Nonsymmetric and nonlocal cases*, arXiv:1510.08388 (2015), https://arxiv.org/abs/1510.08388.
