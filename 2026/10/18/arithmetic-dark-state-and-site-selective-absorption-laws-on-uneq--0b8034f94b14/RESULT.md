# Arithmetic dark-state and site-selective absorption laws on unequal-arm quantum spiders

## Finding

For a uniformly coupled finite spider with an absorbing central vertex, the exact number of nondecaying one-particle modes and the infinite-time survival probability from **every individual noncentral vertex** are given by divisor sums. In particular, an irregular spider can retain dark modes yet completely absorb a particle launched at certain vertices; the exact locations are determined by least common multiples of pairwise greatest common divisors of its arm lengths plus one.

Let the graph have \(B\ge3\) arms with \(L_i\ge1\) sites on arm \(i\), counting outward from the common vertex. Set \(m_i=L_i+1\). For every integer \(q\ge2\) dividing at least one \(m_i\), define
\[
I_q=\{i:q\mid m_i\},\qquad r_q=|I_q|,\qquad W_q=\sum_{j\in I_q}\frac1{m_j}.
\]
Let \(\varphi(q)\) denote Euler's totient and \(c_q(d)\) the Ramanujan sum
\[
c_q(d)=\sum_{\substack{1\le p<q\\\gcd(p,q)=1}}\cos\!\left(\frac{2\pi pd}{q}\right)
=\sum_{h\mid\gcd(q,d)}h\,\mu(q/h).
\]
Here \(\mu\) is the Möbius function. The full nondecaying subspace has dimension
\[
\boxed{\mathcal D=\sum_{\substack{q\ge2\\r_q\ge2}}\varphi(q)(r_q-1).}
\]
For a unit excitation initially at distance \(d\), \(1\le d\le L_i\), on arm \(i\), its infinite-time unabsorbed probability is exactly
\[
\boxed{\mathcal S_{i,d}=\sum_{\substack{q\mid m_i\\q\ge2}}\frac{\varphi(q)-c_q(d)}{m_i}\left(1-\frac1{m_iW_q}\right).}
\]
Each summand is nonnegative, and the formula is rational. With
\[
g_i=\operatorname{lcm}_{j\ne i}\gcd(m_i,m_j),
\]
**complete eventual absorption** from vertex \((i,d)\) occurs if and only if \(g_i\mid d\). Consequently, complete absorption from **every** noncentral vertex occurs if and only if the integers \(m_1,\ldots,m_B\) are pairwise coprime. All assertions hold for every positive hopping and positive loss strength.

## Assumptions and scope

The graph is the tree formed by identifying one endpoint of \(B\ge3\) finite paths, with all \(L_i\) counted *excluding* their common endpoint \(o\). Edges have identical real hopping \(J>0\); all onsite energies vanish except for a central loss potential. On the one-particle Hilbert space define
\[
K=J A-\frac{i\gamma}{2}|o\rangle\langle o|,\qquad \gamma>0,
\]
where \(A\) is the unweighted adjacency matrix. An initial basis state \(|i,d\rangle\) evolves without a quantum jump as \(\psi(t)=e^{-iKt}|i,d\rangle\). The survival probability is the **norm squared** \(\|\psi(t)\|^2\), and \(\mathcal S_{i,d}=\lim_{t\to\infty}\|\psi(t)\|^2\). Its complementary probability \(1-\mathcal S_{i,d}\) is total absorption at the hub. The statement concerns coherent single-particle no-jump dynamics and has no disorder, detuning, additional sinks, or other dephasing.

## Proof

**1. Only the hub-nodal eigenspace survives.** Let \(K v=zv\), \(v\ne0\). Taking the imaginary part of the scalar inner-product identity gives
\[
\operatorname{Im}z=-\frac\gamma2\frac{|\langle o|v\rangle|^2}{\|v\|^2}\le0.
\]
A real eigenvalue therefore has \(\langle o|v\rangle=0\), and \(Kv=JAv=zv\). Conversely, any eigenvector of \(A\) zero at \(o\) is a real-energy eigenvector of both \(K\) and \(K^*\). Their full span \(\mathscr D\) thus *reduces* \(K\), and \(K|_{\mathscr D}\) is Hermitian. The complementary finite-dimensional block has no real eigenvalues by the same implication and hence has eigenvalues in the strictly lower half-plane. Even allowing Jordan blocks, its exponential decays in norm to zero. Thus the survival limit exists and equals \(\|P_{\mathscr D}|i,d\rangle\|^2\), with \(P_{\mathscr D}\) the orthogonal dark projector. This also proves independence from \(\gamma>0\).

**2. Dirichlet paths and rational frequency labels.** Enforcing zero hub amplitude decouples all arms. Arm \(i\) has normalized Dirichlet eigenvectors
\[
f_{i,k}(d)=\sqrt{\frac2{m_i}}\sin\!\left(\frac{\pi k d}{m_i}\right),\quad 1\le k<m_i,
\]
with eigenvalues \(2J\cos(\pi k/m_i)\). Since cosine is strictly decreasing on \((0,\pi)\), equal energies on different arms occur precisely when the fractions \(k/m_i\) agree. Write this fraction uniquely as \(p/q\), where \(q\ge2\), \(1\le p<q\), and \(\gcd(p,q)=1\). Exactly the arms in \(I_q\) then carry the corresponding mode, one on each arm; the same \(p/q\) occurs with \(k=p m_i/q\).

**3. The matching condition at the hub.** The only remaining eigenvector equation, at the central vertex, requires the sum of the first-site amplitudes to vanish. With one normalized Dirichlet mode on each arm \(i\in I_q\), the first-site amplitude is
\[
\sqrt{\frac2{m_i}}\sin\!\left(\frac{\pi p}{q}\right).
\]
The sine is nonzero, so the dark vectors for this single frequency form the orthogonal complement, inside \(\mathbb C^{r_q}\), of the weight vector \(b_q=(m_i^{-1/2})_{i\in I_q}\). Its squared norm is \(W_q\), and its orthogonal projector is \(I-b_qb_q^*/W_q\). Hence the dimension of this dark frequency space is \(r_q-1\), and it is zero when \(r_q=1\). There are exactly \(\varphi(q)\) distinct primitive numerators \(p\) for every denominator \(q\). Since different fractions yield different energies, their spectral eigenspaces are mutually orthogonal; summing dimensions proves the formula for \(\mathcal D\).

**4. The local survival projector.** For source vertex \((i,d)\), the diagonal weight of the projector for a fixed reduced frequency \(p/q\) is
\[
\frac2{m_i}\sin^2\!\left(\frac{\pi pd}{q}\right)
\left(1-\frac{m_i^{-1}}{W_q}\right).
\]
For \(q\nmid m_i\), this weight is zero. Summing over primitive \(p\) uses the exact identity
\[
2\sum_{\substack{1\le p<q\\\gcd(p,q)=1}}\sin^2\!\left(\frac{\pi pd}{q}\right)=\varphi(q)-c_q(d).
\]
This yields the displayed formula for \(\mathcal S_{i,d}\). Its rationality follows from the integer Ramanujan-sum identity and rational \(W_q\). The trace identity additionally gives
\[
\sum_{i=1}^{B}\sum_{d=1}^{L_i}\mathcal S_{i,d}=\mathcal D,
\]
so a uniformly randomized noncentral launch has average survival \(\mathcal D/(\sum_i L_i)\).

**5. Exactly which source vertices are completely absorbed?** For \(r_q\ge2\), the second factor is strictly positive. The first factor is a sum of nonnegative squared sines and vanishes precisely if \(q\mid d\): indeed the primitive term \(p=1\) vanishes only under that divisibility, and if \(q\mid d\) then every term vanishes. Therefore \(\mathcal S_{i,d}=0\) exactly when every \(q\ge2\) dividing \(m_i\) and some other \(m_j\) also divides \(d\). The least common multiple of all such common divisors equals \(\operatorname{lcm}_{j\ne i}\gcd(m_i,m_j)=g_i\), proving the site criterion. If all \(m_i\) are pairwise coprime, no dark frequency exists. Conversely, any nontrivial pairwise gcd supplies a shared prime denominator and a nonzero dark subspace, so complete absorption from every vertex fails.

**6. Sharp nonuniform example.** For three arms of lengths \((L_1,L_2,L_3)=(2,5,7)\), one has \((m_1,m_2,m_3)=(3,6,8)\). The dark dimension is \(3\). The length-seven arm has exact successive survival probabilities
\[
\left(\frac17,\,0,\,\frac17,\,0,\,\frac17,\,0,\,\frac17\right).
\]
Thus this single connected tree has a nontrivial dark subspace and nonetheless absorbs with probability one from three specifically identified starting vertices. The assertion is exact, not a numerical extrapolation.

## Verification

The self-contained script `verify_spider.py` constructs the full adjacency matrix independently and obtains the complete hub-nodal dark projector from full-matrix eigenspaces. It compares that projector with the rational divisor-sum expression. In a finite exhaustive parameter sweep of \(321\) small spiders (including \(2904\) vertices), it verified all survival probabilities and dark-space dimensions; the largest floating-point discrepancy was \(2.0\times10^{-15}\). It separately checked the divisibility condition and reported exact rational values in illustrative asymmetric configurations. The computer tests cover finite small instances only; the proof above supplies the all-integer statement.

Run `python verify_spider.py` in an environment with Python 3, NumPy, SciPy, and SymPy. No external data are needed.

## Relationship to prior work

Yalouz and Pouthier's equal-length, finite-arm, centrally absorbing star model (arXiv:2210.17524v1) is the closest direct antecedent. Their analysis exploits rotational symmetry and investigates peripheral energy defects and absorption speedup; the unequal-length graphs and exact arithmetic, site-resolved limiting probabilities here have no such symmetry. In the equal-length, zero-defect specialization, the present formula yields the expected survival fraction \((B-1)/B\) for any nonhub localized launch; that special case is not claimed new.

Their earlier two-generation star studies [2,3] treat a differently branched architecture and central trapping; they establish the physical motivation and dark-state interpretation, rather than this arbitrary-length classification. Le and collaborators [4] define dark-state subspaces generically and give standard path-mode formulas; their framework conceptually underlies the projector method here, but does not present the least-common-multiple vertex criterion or the Ramanujan-sum probability law for unequal-arm spiders. Existing path eigenvalue theory also underlies the proof. The contribution is the complete explicit specialization and its site-selective consequence, not the general notion of dark states.

## Limitations

The theorem makes no statement about finite-time relaxation rates, the large-arm limit, disordered hoppings, nonuniform onsite energies, multiple lossy vertices, driven systems, many-particle dynamics, or the spectral gap of a full Lindblad operator. Small numerical checks do not independently certify the infinite family. The literature comparison is statement-based but nonexhaustive: an equivalent formulation in older spectral-graph or optical-network literature is a residual priority risk, especially outside the searched terminology. Independent mathematical and priority audits have not been performed.

## References

[1] S. Yalouz and V. Pouthier, *The extended star graph as a light-harvesting-complex prototype: excitonic absorption speedup by peripheral energy defect tuning*, arXiv:2210.17524v1, first posted 14 October 2022. https://arxiv.org/abs/2210.17524

[2] S. Yalouz and V. Pouthier, *Continuous-time quantum walk on an extended star graph: Disorder-enhanced trapping process*, Phys. Rev. E **101**, 012310 (2020), https://doi.org/10.1103/PhysRevE.101.012310 ; deposited as HAL hal-02434409 on 10 January 2020.

[3] S. Yalouz and V. Pouthier, *Continuous-time quantum walk on an extended star graph: Trapping and superradiance transition*, Phys. Rev. E **97**, 022304 (2018), https://doi.org/10.1103/PhysRevE.97.022304 .

[4] T. P. Le, L. Donati, S. Severini, and F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482v1 (2017), https://arxiv.org/abs/1707.07482 .
