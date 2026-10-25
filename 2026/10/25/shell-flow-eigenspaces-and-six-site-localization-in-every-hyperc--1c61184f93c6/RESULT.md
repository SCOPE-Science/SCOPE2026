# Shell-flow eigenspaces and six-site localization in every hypercube dimension

## Finding

Consider the spin-coupled, discrete-time Grover walk on the \(d\)-dimensional Boolean hypercube in the all-positive spin sector, with the position-dependent phase \(\exp(-i\pi |v|/d)\). For **every integer \(d\ge3\)**, this walk has explicitly constructible localized eigenvectors, including in every **odd** dimension. In particular, each adjacent pair of nontrivial Hamming shells carries two flow eigenspaces whose dimensions are given by an exact cycle-rank formula. A six-vertex cycle provides an eigenstate with time-independent position probabilities equal to \(1/6\) on six vertices and zero everywhere else.

**Theorem.** Let \(d\ge3\) and \(1\le m\le d-2\). Define
\[
\mu_{m,\pm}=\pm\exp\!\left(-\frac{i(2m+1)\pi}{2d}\right),\qquad
r_{d,m}=(d-m)\binom dm-\binom dm-\binom d{m+1}+1.
\]
Then the reduced walk has, at each eigenvalue \(\mu_{m,\pm}\), a linear subspace of dimension \(r_{d,m}\) consisting of eigenvectors supported on vertices in Hamming shells \(m\) and \(m+1\). Every nonzero vector in these subspaces has a nonuniform position marginal. The eigenvalues \(\mu_{m,\pm}\) are pairwise distinct as \(m\) and the sign vary, so these subspaces are mutually orthogonal. The total number of linearly independent eigenvectors thereby exhibited is
\[
L_d=2\sum_{m=1}^{d-2}r_{d,m}=(d-4)2^d+2d+4.
\]
Relative to the \(d2^d\)-dimensional position-coin Hilbert space, their proportion is
\[
\frac{L_d}{d2^d}=1-\frac4d+\frac{2d+4}{d2^d}\longrightarrow1.
\]
This is a **constructive lower bound**, not a claim that the listed eigenspaces exhaust every eigenspace at the corresponding eigenvalues.

## Assumptions and scope

A hypercube vertex is a subset \(v\subseteq\{0,\ldots,d-1\}\), and \(|v|\) is its Hamming weight. The coin space is \(\mathbb C^d\) with distinguished basis indexed by directions \(k\in\{0,\ldots,d-1\}\). Write \(\psi_{v,k}\) for its amplitudes and \(G=2J/d-I\) for the Grover coin, where \(J\) is the all-ones matrix. In the all-positive spin configuration of Wang's spin-coupled model (arXiv:2609.07267v1, Eq. (3.14)), its reduced unitary operator is defined by
\[
(U_d\psi)_{v\triangle\{k\},k}=e^{-i\pi |v|/d}(G\psi_v)_k
\]
for every vertex \(v\) and direction \(k\); \(\triangle\) denotes symmetric difference. The phase multiplies the source vertex **before** the Grover coin and shift, as in the cited model. Eigenvalues are taken for this exact convention.

The statement concerns pure states in a fixed conserved spin sector, not a spin-averaged ensemble. Its localization conclusion is in the precise sense of a nonuniform stationary (hence nonuniform time-averaged) position marginal for a normalized eigenstate. Neither Anderson localization of generic states nor localization from every initially position-localized state is asserted.

## Proof

**1. The zero-sum coin sector.** For each vertex define \(s_v=\sum_k\psi_{v,k}\). If \(s_v=0\), then \(G\psi_v=-\psi_v\). Consequently, for a vector with zero sum at every vertex, the eigenvector equation \(U_d\psi=\mu\psi\) becomes the edgewise relation
\[
\mu\psi_{w,k}=-p_v\psi_{v,k},\quad w=v\triangle\{k\},\qquad p_v=e^{-i\pi |v|/d}.
\]
This also shows that amplitudes outside a chosen set of directed edges remain zero if each local coin sum is zero.

**2. An exact shell-flow eigenspace.** Fix \(m\) as in the theorem. Let \(H_{d,m}\) be the bipartite graph whose left vertices are the \(m\)-subsets, whose right vertices are the \((m+1)\)-subsets, and whose edges connect subsets that differ by adding one element. Write \(E(H_{d,m})\) for its edges. For any complex edge function \(f\), impose the incidence equations
\[
\sum_{e\ni v} f_e=0\qquad\text{at every vertex of }H_{d,m}.
\]
Choose either \(\mu=\mu_{m,+}\) or \(\mu=\mu_{m,-}\), put \(p_m=e^{-im\pi/d}\), and define the coin amplitudes supported on the two orientations of the edges of \(H_{d,m}\) by
\[
\psi_{v,k}=f_{\{v,w\}},\quad
\psi_{w,k}=-\frac{p_m}{\mu}f_{\{v,w\}}
\]
whenever \(|v|=m\), \(|w|=m+1\), and \(w=v\triangle\{k\}\). Set all remaining coin amplitudes to zero. The incidence conditions ensure \(s_v=0\) at both shells. The eigenvector equation from the low to the high shell holds by definition. The reverse equation holds because
\[
\mu^2=p_m p_{m+1}=e^{-i(2m+1)\pi/d}.
\]
Thus this construction maps the incidence kernel injectively onto an eigenspace (a specified subspace, not necessarily the whole spectral eigenspace) of \(U_d\).

**3. Exact dimension.** The bipartite graph \(H_{d,m}\) is connected: two \(m\)-subsets differing by one exchange can be joined through their \((m+1)\)-element union, and such exchanges connect all \(m\)-subsets. Every \((m+1)\)-subset is incident to an \(m\)-subset. Therefore, over \(\mathbb C\), its unsigned vertex-edge incidence matrix has rank \(|V(H_{d,m})|-1\): negating the right-hand vertex rows converts it into the usual oriented incidence matrix of a connected graph. Here
\[
|E(H_{d,m})|=(d-m)\binom dm,\qquad
|V(H_{d,m})|=\binom dm+\binom d{m+1}.
\]
Rank-nullity proves the formula for \(r_{d,m}\). Its positivity follows from the explicit six-cycle below (or from the presence of cycles in every interior layer). The eigenvalues \(\mu_{m,\pm}\) are distinct because their squares are distinct for different \(m\), and the two signs give distinct roots at fixed \(m\). Eigenspaces of the finite-dimensional unitary \(U_d\) for different eigenvalues are orthogonal.

Finally, summing the edge and vertex counts over \(m=1,\ldots,d-2\) and adding the \(d-2\) connected-component terms yields
\[
\sum_{m=1}^{d-2}r_{d,m}=(d-4)2^{d-1}+d+2,
\]
which gives the claimed mode count and proportion. Since every vector constructed for an interior pair of shells is zero at the empty and full vertices, while its total norm is positive, its position marginal cannot be uniform.

**4. Uniform six-site localized state.** Choose a base set \(B\) of size \(m-1\) and three distinct indices \(a,b,c\notin B\). The following is a six-cycle in \(H_{d,m}\):
\[
B\cup\{a\}\to B\cup\{a,b\}\to B\cup\{b\}
\to B\cup\{b,c\}\to B\cup\{c\}\to B\cup\{a,c\}
\to B\cup\{a\}.
\]
Assign alternating values \(+1,-1,+1,-1,+1,-1\) to its six successive *undirected* edges, and zero to every other edge. At each of its six vertices the two incident values sum to zero, so this is a nonzero incidence-kernel vector. In the lifted coin state, each of the six vertices has exactly two nonzero coin components of modulus one (because \(|p_m/\mu|=1\)). Hence the squared norm is \(12\). After dividing by \(\sqrt{12}\), the position distribution is exactly \(1/6\) at each listed vertex and zero at every other vertex, for all discrete times. The existence of a base set and three spare indices is assured by \(1\le m\le d-2\). In particular \(d=3\), \(m=1\) already yields this construction in an odd-dimensional hypercube.

## Verification

The companion `check_cycle.py` uses only the Python standard library. Execute `python3 check_cycle.py`. It constructs the six-cycle vector and applies the independently written Grover update in finite dimensions \(3\le d\le9\), for every interior Hamming-shell pair and both eigenvalue branches. It checks local zero-sum constraints, eigenvector residuals, exact support and probabilities, graph connectivity, edge and vertex counts, cycle ranks and the total dimension formula. The script reported **546 successful finite sanity checks**. Independent dense-matrix calculations, separate from the companion script, also verified unitarity and the predicted eigenvalues with at least the asserted multiplicities in dimensions \(3,4,5\). These checks corroborate the proof but are not substituted for its all-dimensional argument.

## Relationship to prior work

Ce Wang, *Spectral Criterion for Disorder-Free Localization of Quantum Walks on Hypercube: QBN Approach* (arXiv:2609.07267v1, 2026), supplies the model, the spin-sector reduction and its general spectral localization criterion. It exhibits nonuniform **eigenvalue-one fixed points** in dimensions \(4\) and \(6\), conjectures fixed points for larger even dimensions and notes that eigenvalues other than one must also be examined to understand odd dimensions. The present theorem does **not** settle the fixed-point conjecture. Rather, it explicitly constructs non-unit-eigenvalue localized states in every dimension \(d\ge3\), including odd dimensions, and provides an extensive family of shell-flow eigenspaces with exact dimensions.

Cycle-flow or birth eigenstates of ordinary Grover walks are established techniques; notably, Higuchi, Portugal, Sato and Segawa (arXiv:1811.02116v1) describe cycle-space eigenspaces for two-tessellable walks. The present calculation adapts that structural mechanism to the specific **source-vertex Hamming-phase operator** of Wang, where eigenphases differ across adjacent shell pairs. The earlier theorem's fixed-angle two-tessellation dynamics does not state this model-specific phase spectrum or the dimension sum above. Work of Arkhipov, Minganti and Nori (Phys. Rev. Research 7, 033002, 2025) studies localized states of a different, continuous-time hypercube Hamiltonian. Sekido and Segawa (arXiv:2607.14797v2, 2026) study small magnetic-vector-potential perturbations of periodic Grover walks, not this fixed vertex-phase family.

## Limitations

The result is restricted to the all-positive conserved spin sector and the stated Grover coin/phase convention; it does not claim generic spin-state localization. The exhibited eigenvectors have eigenvalues different from one, so the source's fixed-point existence question is still open outside its proved cases. The formula \(L_d\) counts an explicitly constructed **orthogonal subfamily**; other eigenvectors may share the same eigenvalues (as numerical checks in small odd dimensions indicate). The six-vertex state is a deliberately prepared eigenstate, and no transport assertion is made for arbitrary starting vectors.

The relationship to broad graph-quantum-walk cycle-space theorems remains a priority limitation: general spectral results may imply this specific construction once their hypotheses are translated to the present phased operator. No claim of independent external certification or publication is made.

## References

1. Ce Wang, *Spectral Criterion for Disorder-Free Localization of Quantum Walks on Hypercube: QBN Approach*, arXiv:2609.07267v1 (2026), especially Eqs. (3.14), (4.2) and Sec. 4.1. https://arxiv.org/html/2609.07267v1
2. Y. Higuchi, R. Portugal, I. Sato and E. Segawa, *Eigenbasis of the Evolution Operator of 2-Tessellable Quantum Walks*, arXiv:1811.02116v1 (2018), Sec. 4.3. https://arxiv.org/html/1811.02116v1
3. I. I. Arkhipov, F. Minganti and F. Nori, *How to realize compact and noncompact localized states in disorder-free hypercube networks*, Physical Review Research 7, 033002 (2025), https://doi.org/10.1103/4s2w-y1xx
4. H. Sekido and E. Segawa, *Robustness of periodicity in Grover walks under a magnetic vector potential*, arXiv:2607.14797v2 (2026), https://arxiv.org/html/2607.14797v2
