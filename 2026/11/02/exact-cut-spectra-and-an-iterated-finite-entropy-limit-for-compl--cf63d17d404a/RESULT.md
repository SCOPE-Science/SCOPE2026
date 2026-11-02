# Exact cut spectra and an iterated finite-entropy limit for complete dyadic-uniform hypergraph states

## Finding

For an integer \(j\ge1\), let \(k=2^j\). Prepare the complete \(k\)-uniform \(n\)-qubit hypergraph state by applying a controlled sign on every \(k\)-element subset to \(|+\rangle^{\otimes n}\). For **every** bipartition into \(a\) and \(b\) qubits with \(a,b\ge k-1\) and \(n=a+b\), define the residue counts
\[
N_\ell(r)=\sum_{\substack{0\le t\le\ell\\t\equiv r\ (\mathrm{mod}\ k)}}\binom{\ell}{t},\qquad 0\le r<k.
\]
Define the real \(k\)-by-\(k\) matrix
\[
K_{r,s}=2^{-n/2}\sqrt{N_a(r)N_b(s)}\bigl(1-2\mathbf1_{\{r+s\ge k\}}\bigr),\qquad 0\le r,s<k.
\]
Then **the complete nonzero spectrum of the reduced state** is exactly the spectrum of \(KK^{\mathsf T}\). There are precisely \(k\) strictly positive eigenvalues (Schmidt rank exactly \(k\)); the other \(2^a-k\) eigenvalues are zero. This is an exact finite-size result with arbitrary eligible, unequal block sizes.

For fixed \(k\), when \(a,b\to\infty\), these \(k\) eigenvalues, in any order, tend to the explicitly known multiset
\[
\boxed{\lambda_h(k)=\frac{1}{k^2\sin^2\bigl((2h-1)\pi/(2k)\bigr)},\qquad h=1,\ldots,k.}
\]
The limiting purity is exactly
\[
\boxed{P_k=\frac13+\frac{2}{3k^2}.}
\]
There is a striking large-interaction-arity consequence: with this **iterated order of limits** (first both block sizes, then \(k=2^j\to\infty\)), the von Neumann entropy does **not** diverge despite the unbounded Schmidt rank. In bits it converges to the finite constant
\[
\boxed{S_\infty=\log_2\!\frac{\pi^2}{4}-\frac23-\frac{12\zeta'(2)}{\pi^2\ln2}=2.2808853887532333\ldots\ .}
\]
For instance, the fixed-\(k\) limiting entropies are \(1\), \(1.6008760366928561\ldots\), and \(1.9306072928196487\ldots\) bits at \(k=2,4,8\), respectively. The finite spectra are not generally flat: entropy is not simply the logarithm of Schmidt rank.

## Assumptions and scope

All qubits have local dimension two, every \(k\)-hyperedge carries **exactly one** unit controlled-phase gate with phase \(-1\) on the all-one basis configuration, and no other gates or noise are applied. The state is pure. The cut is any bipartition into two groups of sizes \(a,b\ge k-1\), which exist for all \(n\ge2k-2\). The choice of which qubits enter each group is immaterial by the full permutation symmetry. Throughout, \(j\in\{1,2,3,\ldots\}\) and \(k=2^j\). All statements concern Schmidt singular values and positive eigenvalues counted with multiplicity. The large-block limit holds for every sequence with both sizes independently diverging at fixed \(k\); the large-arity assertion is an iterated limit, not a claim uniform in varying \(k,a,b\).

## Proof

**1. Phase and carry reduction.** A basis vector with \(w\) ones receives exactly \(\binom wk\) factors of \(-1\). Hence its amplitude is \(2^{-n/2}(-1)^{\binom wk}\). For dyadic \(k=2^j\), Lucas' binomial congruence implies
\[
\binom{w}{2^j}\equiv\operatorname{bit}_j(w)\pmod2.
\]
For a bipartition, write \(u\) and \(v\) for the two Hamming weights; let \(r=u\bmod k\) and \(s=v\bmod k\). Addition of \(u\) and \(v\) generates a carry into bit \(j\) exactly when \(r+s\ge k\). Thus
\[
\operatorname{bit}_j(u+v)\equiv\operatorname{bit}_j(u)+\operatorname{bit}_j(v)+\mathbf1_{\{r+s\ge k\}}\pmod2.
\]
The two single-block bit signs are removed by diagonal local unitaries, leaving the sign \(F_{r,s}=1-2\mathbf1_{\{r+s\ge k\}}\), which depends only on the two residues.

**2. Isometric residue compression.** For each cut side and residue \(r\), let the normalized vector \(|r;\ell\rangle\) be the equal superposition of all \(\ell\)-bit strings with Hamming weight congruent to \(r\pmod k\). These vectors are orthonormal for distinct residues and have positive normalizers \(N_\ell(r)\) whenever \(\ell\ge k-1\). After the local phase unitaries of Step 1, the bipartite state is exactly
\[
\sum_{r,s=0}^{k-1}K_{r,s}|r;a\rangle\otimes|s;b\rangle.
\]
Consequently the physical coefficient matrix is an isometric embedding of \(K\) and the positive reduced-state spectrum equals that of \(KK^{\mathsf T}\). Normalization follows from the original unit state, equivalently \(\sum_{r,s}K_{r,s}^2=1\).

**3. Rank with no genericity assumption.** Consecutive rows of \(F\) differ in exactly one column, with difference \(\pm2\). Subtract adjacent rows and expand the remaining all-one row to obtain \(|\det F|=2^{k-1}\). Both diagonal residue-normalization matrices have strictly positive entries for \(a,b\ge k-1\). Therefore \(\det K\ne0\) and exactly \(k\) Schmidt coefficients are positive, even for unequal block sizes and at the boundary \(a=k-1\) or \(b=k-1\).

**4. Limiting spectral diagonalization.** The roots-of-unity filter gives, for \(\omega=e^{2\pi i/k}\),
\[
\frac{N_\ell(r)}{2^\ell}=\frac1k\sum_{m=0}^{k-1}\left(\frac{1+\omega^m}{2}\right)^\ell\omega^{-mr}.
\]
Every nonzero-frequency factor has magnitude at most \(\cos(\pi/k)<1\), so each normalized residue weight tends exponentially to \(1/k\) as \(\ell\to\infty\). Accordingly \(K\to F/k\) entrywise and hence in every matrix norm. The limiting reduced matrix is \(T/k^2\), where straightforward summation gives
\[
T_{r,s}=(FF^{\mathsf T})_{r,s}=k-2|r-s|.
\]
Consider the antiperiodic discrete cycle Laplacian \(L\): second-difference diagonal \(2\), nearest-neighbor coefficients \(-1\), and the coefficient at the seam between \(0\) and \(k-1\) is \(+1\). For \(k=2\), the ordinary nearest-neighbor and seam contributions cancel and \(L=2I\). Direct evaluation of the second differences of \(k-2|r-s|\), including the two seam rows, yields
\[
LT=4I.
\]
The antiperiodic Fourier eigenmodes \(e^{i(2h-1)\pi r/k}\) have \(L\)-eigenvalues \(4\sin^2((2h-1)\pi/(2k))\). Inverting \(L\) gives precisely the displayed \(\lambda_h(k)\); no eigenvalue vanishes. Taking the Frobenius trace
\[
\mathrm{tr}(T^2)=\sum_{r,s=0}^{k-1}(k-2|r-s|)^2=\frac{k^4+2k^2}{3}
\]
proves the limiting purity formula. The limiting entropy is the finite sum \(-\sum_h\lambda_h(k)\log_2\lambda_h(k)\).

**5. Infinite-arity entropy limit.** For each fixed positive odd integer \(q=2h-1\), both eigenvalues indexed by \(h\) and by \(k-h+1\) approach \(4/(\pi^2q^2)\) as \(k\to\infty\). The elementary bound \(\sin x\ge2x/\pi\) for \(0\le x\le\pi/2\) bounds these paired probabilities by a constant multiple of \(q^{-2}\), and their entropy summands by a summable multiple of \((1+\log q)q^{-2}\). Dominated convergence therefore gives the limiting twofold odd-integer spectrum
\[
\left\{\frac4{\pi^2q^2},\frac4{\pi^2q^2}:q=1,3,5,\ldots\right\}.
\]
It has total weight one because \(\sum_{q\text{ odd}}q^{-2}=\pi^2/8\). Differentiating the elementary odd-number Dirichlet series \(\sum_{q\text{ odd}}q^{-s}=(1-2^{-s})\zeta(s)\) at \(s=2\), and evaluating its Shannon entropy, yields exactly the claimed expression involving \(\zeta'(2)\). This establishes the iterated limit.

## Verification

`checker.py` independently constructs the full \(2^a\)-by-\(2^b\) computational-basis coefficient matrix using literal binomial counts, independently constructs the compressed residue matrix, and compares singular-value squares, their ranks and normalization. It also builds the antiperiodic Laplacian, verifies \(LT=4I\), compares the exact trigonometric eigenvalues and purity for eight dyadic sizes, and checks the roots-of-unity filter directly. The code requires Python 3 and NumPy: run `python checker.py` from the directory containing this document. Recorded output is in `CHECK_OUTPUT.txt`. Numerical comparisons provide reproducibility checks; the all-size statements are proved in Steps 1–5, not inferred from finite tests.

## Relationship to prior work

Rossi, Huber, Bruß and Macchiavello (2012 preprint) introduced quantum hypergraph states and \(k\)-uniformity; these definitions and the controlled-phase amplitude rule are foundational here, not new. Qu and coauthors (2013) characterize local single-qubit entropic measures via adjacent subhypergraphs rather than a complete arbitrary-cut spectrum. Gühne and coauthors (2014) develop hypergraph entanglement classification and nonclassicality. Nöller, Gühne and Gachechiladze (2023 preprint) treat **symmetric complete hypergraphs** and geometric multipartite entanglement, including explicit local-unitary representations for certain odd hyperedge sizes; the present proof does not claim that their symmetry machinery or general state representation is novel. Their analyzed quantity and treated cardinalities do not give the dyadic-arity all-block Schmidt spectrum, antiperiodic Laplacian spectrum or finite iterated finite-entropy limit as a stated result. Zhou and Hamma (2021) analyze average entanglement of **random** hypergraph ensembles, so their volume-law result does not imply the deterministic subextensive dyadic sequence. Fajardo and Paraschiv (2026 preprint) offer general Schmidt-rank **lower-bound certificates** from restricted bilinear cores for arbitrary hypergraph states; those bounds are neither an exact full-spectrum computation nor a determination of its entropy, and their paper expressly distinguishes the two problems. All comparisons are about logical coverage, not only topic/title similarity. Earlier special cases, general REW phase cleaning, Lucas' congruence, Fourier diagonalization and standard spectral calculus are acknowledged ingredients. No claim of independent external validation or priority certainty is made.

## Limitations

The result excludes arbitrary hyperedge sizes, weighted or random hyperedges, mixed and noisy states, and cuts with fewer than \(k-1\) qubits on either side. The trigonometric spectrum holds after taking both cut blocks to infinity at fixed \(k\), rather than for general finite block sizes. The constant \(S_\infty\) is an iterated large-block / large-arity limit and is not asserted for simultaneous limits without growth conditions. The full finite spectra are specified via an explicit small matrix, not asserted to have elementary radical expressions for every \(k,a,b\). A specialized earlier symmetric-state or Boolean-matrix result might imply some portion of this theorem; complete historical priority is not certified.

## References

- M. Rossi, M. Huber, D. Bruß, C. Macchiavello, *Quantum Hypergraph States*, arXiv:1211.5554 (first public 2012-11-23), https://arxiv.org/abs/1211.5554.
- R. Qu, Y.-P. Ma, Y.-R. Bao, J. Wang, Z.-S. Li, *Entropic measure and hypergraph states*, arXiv:1305.0662 (2013-05-03), https://arxiv.org/abs/1305.0662.
- O. Gühne et al., *Entanglement and nonclassical properties of hypergraph states*, arXiv:1404.6492 (2014), https://arxiv.org/abs/1404.6492.
- Y. Zhou, A. Hamma, *Entanglement of random hypergraph states*, arXiv:2110.07158 (2021), https://arxiv.org/abs/2110.07158.
- J. Nöller, O. Gühne, M. Gachechiladze, *Symmetric hypergraph states: Entanglement quantification and robust Bell nonlocality*, arXiv:2302.01695 (first public 2023-02-03), https://arxiv.org/abs/2302.01695.
- C. Fajardo, M. Paraschiv, *Restriction-Based Certificate of Bipartite Schmidt Rank in Hypergraph States*, arXiv:2602.21016 (first public 2026-02-24), https://arxiv.org/abs/2602.21016.
