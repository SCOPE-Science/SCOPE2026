# Degree-to-part-size reversal under intrinsic dephasing on complete bipartite quantum networks

## Finding
Consider the same connected weighted graph for a classical continuous-time random walk and a quantum walk with energy-basis (intrinsic) dephasing, at the same hopping normalization. Define their quantum–classical distance using squared Uhlmann fidelity, with arbitrary common initially diagonal density matrix. For every positive dephasing rate, every non-star unbalanced complete bipartite graph \(K_{m,n}\) with \(2\le m<n\) has a **forced reversal of the optimal initial vertex class**: at all sufficiently short positive times the optimum lies in the smaller class (whose vertices have higher degree), whereas at all sufficiently late times the optimum lies in the larger class. At least one finite-time transition is therefore unavoidable, independently of the positive dephasing rate.

The conclusion follows from two exact laws. First, on any finite loopless connected undirected weighted graph, a localized initial vertex \(j\) with incident weights \(w_{jk}\ge0\) has the short-time distance
\[
D_j(t)=\left[s_1(j)+\gamma s_2(j)-2\sqrt{\gamma s_3(j)}\right]t+o(t),\qquad s_r(j)=\sum_{k\ne j}w_{jk}^{r},\quad \gamma>0.
\]
For simple unweighted graphs, its slope becomes \(c_\gamma(d)=(1+\gamma)d-2\sqrt{\gamma d}\), strictly increasing with integer degree \(d\ge1\).

Second, for unit-edge \(K_{m,n}\), let \(N=m+n\). For a localized vertex in a class of size \(a\in\{m,n\}\), with opposite class size \(b=N-a\), the exact asymptotic distance is
\[
D_a(\infty)=1-\frac{1}{N}\left(\frac{1}{\sqrt N}+\sqrt{\frac{b}{aN}}+\sqrt{\frac{a-1}{a}}\right)^2.
\]
For \(2\le m<n\), the larger class has strictly larger asymptotic distance, opposite to the early-time ordering. At fixed total size \(N\ge4\), the star \(K_{1,N-1}\) uniquely maximizes the optimized asymptotic distance among complete bipartite graphs, and the balanced bipartition \(K_{\lfloor N/2\rfloor,\lceil N/2\rceil}\) uniquely minimizes it (up to exchanging parts). The star maximum coincides with the previously established complete-graph value \(1-(1+\sqrt{N-1})^2/N^2\).

## Assumptions and scope
A graph has a finite vertex set \(V\), symmetric nonnegative edge weights \(w_{jk}=w_{kj}\), no loops, and a connected positive-weight support. Its positive graph Laplacian is \(L_{jj}=\sum_{k\ne j}w_{jk}\) and \(L_{jk}=-w_{jk}\) for \(j\ne k\). For any initial diagonal density \(\rho_0=\sum_j p_j|j\rangle\langle j|\), with \(p_j\ge0\) and \(\sum_jp_j=1\), define the classical density \(\sigma(t)=\operatorname{diag}(e^{-tL}p)\) and the quantum density solving
\[
\frac{d\rho}{dt}=-i[L,\rho]-\frac{\gamma}{2}[L,[L,\rho]],\qquad\rho(0)=\rho_0,\qquad\gamma>0.
\]
Here \(\hbar=1\) and the classical jump rate and quantum hopping energy are both normalized to one. Define squared fidelity \(F(\sigma,\rho)=(\operatorname{Tr}\sqrt{\sqrt\sigma\,\rho\,\sqrt\sigma})^2\) and optimized distance \(D(t)=1-\min_{p}F(\sigma(t),\rho(t))\). The conditional \(D_j(t)\) uses \(p_j=1\). All limits \(t\downarrow0\) keep \(\gamma>0\) fixed; all limits \(t\to\infty\) refer to strictly positive \(\gamma\). No assertion is made about the number or uniqueness of finite-time switching points.

## Proof
**1. Reduction to localized states.** Both dynamical maps depend linearly on the common initial probability vector \(p\). Joint concavity of the root fidelity gives
\[
\sqrt{F\big(\sum_jp_j\sigma_j(t),\sum_jp_j\rho_j(t)\big)}\ge\sum_jp_j\sqrt{F(\sigma_j(t),\rho_j(t))}\ge\min_j\sqrt{F(\sigma_j(t),\rho_j(t))}.
\]
Thus the minimum fidelity over all diagonal initial states is attained by at least one localized state, and \(D(t)=\max_jD_j(t)\).

**2. The weighted short-time law.** Fix a vertex \(j\), put \(P=|j\rangle\langle j|\) and \(Q=I-P\), and abbreviate \(s_r=s_r(j)\). For the classical diagonal state, \(\sigma_{jj}(t)=1-s_1t+O(t^2)\), each neighbor \(k\) has \(\sigma_{kk}(t)=w_{jk}t+O(t^2)\), and each nonneighbor has \(\sigma_{kk}(t)=O(t^2)\). The double commutator satisfies
\[
[L,[L,P]]=L^2P+PL^2-2LPL.
\]
Consequently, \(\rho_{jj}(t)=1-\gamma s_2t+O(t^2)\), while the first-order \(Q\)-block is \(Q\rho(t)Q=\gamma t|u\rangle\langle u|+O(t^2)\), where \(u=QL|j\rangle\) has coordinates \(u_k=-w_{jk}\). The commutator contribution vanishes in that \(Q\)-block.

Set \(M(t)=\sqrt{\sigma(t)}\,\rho(t)\,\sqrt{\sigma(t)}\), using the vertex basis. Its \(j,j\) entry is \(1-(s_1+\gamma s_2)t+O(t^2)\); the \(j,Q\) entries are \(O(t^{3/2})\). In the neighbor subspace, the \(Q,Q\) block has leading term \(\gamma t^2|v\rangle\langle v|\), where \(v_k=w_{jk}^{3/2}\). All other entries of that block are \(o(t^2)\). A Schur-complement comparison with the isolated eigenvalue tending to one therefore gives one eigenvalue \(1-(s_1+\gamma s_2)t+o(t)\), one smaller eigenvalue \(\gamma s_3t^2+o(t^2)\), and all remaining eigenvalues \(o(t^2)\). The case of a one-neighbor support uses the identical rank-one argument. Since the dimension is fixed, taking square roots and summing yields
\[
\operatorname{Tr}\sqrt{M(t)}=1-\tfrac12(s_1+\gamma s_2)t+\sqrt{\gamma s_3}\,t+o(t).
\]
Squaring proves the weighted short-time formula. For an unweighted graph \(s_1=s_2=s_3=d\). For \(d\ge1\),
\[
\frac{d}{dd}c_\gamma(d)=1+\gamma-\sqrt{\gamma/d}\ge1+\gamma-\sqrt\gamma>0,
\]
where the final strict inequality follows from \(1+\gamma>\sqrt\gamma\) for \(\gamma>0\). Hence \(c_\gamma\) is strictly increasing on \([1,\infty)\).

**3. Exact asymptotic pinching.** Write \(L=\sum_\lambda\lambda P_\lambda\) with distinct eigenvalues indexed by \(\lambda\). The master equation has solution
\[
\rho_j(t)=\sum_{\lambda,\mu}e^{-i(\lambda-\mu)t-\gamma(\lambda-\mu)^2t/2}\,P_\lambda|j\rangle\langle j|P_\mu.
\]
For \(\gamma>0\), it tends to \(\rho_j(\infty)=\sum_\lambda P_\lambda|j\rangle\langle j|P_\lambda\). These summands are orthogonal rank-one operators with eigenvalues \(\|P_\lambda|j\rangle\|^2\). Connectedness ensures the classical state tends to \(I/N\). By continuity of fidelity,
\[
D_j(\infty)=1-\frac1N\left(\sum_\lambda\|P_\lambda|j\rangle\|\right)^2.
\]

**4. Bipartite spectrum and part-size ordering.** For \(K_{a,b}\), the eigenvalues are \(0\), \(N\), \(b\) with dark multiplicity \(a-1\), and \(a\) with dark multiplicity \(b-1\). If \(a=b\) the two dark spectral sectors have the same eigenvalue, but for a vertex in one part the projection onto the other part's dark vectors vanishes, so the following weights remain valid. From a vertex of the \(a\)-part, the nonzero squared projection norms are exactly \(1/N\), \(b/(aN)\), and \((a-1)/a\). Their sum is one and substitution into Step 3 gives the displayed terminal formula.

Put
\[
T_N(a)=\frac1{\sqrt N}+\sqrt{\frac1a-\frac1N}+\sqrt{1-\frac1a},\qquad D_a(\infty)=1-\frac{T_N(a)^2}{N}.
\]
For \(2\le a<N\), differentiation yields
\[
T_N'(a)=\frac1{2a^2}\left(\frac1{\sqrt{1-1/a}}-\frac1{\sqrt{1/a-1/N}}\right)<0,
\]
because \(1-1/a>1/a-1/N\) for \(a\ge2\). Thus, whenever both parts have size at least two, \(D_a(\infty)\) strictly increases with the size \(a\) of the initial vertex's part.

**5. Reversal and topology extremizers.** In \(K_{m,n}\) with \(2\le m<n\), a vertex in the \(m\)-part has degree \(n\), so Step 2 makes its conditional distance strictly greater for all sufficiently small positive times. Step 4 makes the opposite, \(n\)-part, strictly optimal for all sufficiently late times. Both conditional distances are continuous for finite \(t\); their difference must vanish at a finite positive time by the intermediate value theorem. Since the optimized distance is their maximum, the maximizing initial class necessarily changes.

For fixed \(N\), Step 4 shows that among nonstar bipartitions the optimized terminal distance strictly increases as the larger class gets larger, yielding the balanced minimum. For a star, \(a=1\) at its center gives \(T_N(1)=1/\sqrt N+\sqrt{(N-1)/N}\). For any \(2\le a<N\), both radicals in \(T_N(a)\) are positive and their squares add to \((N-1)/N\); hence their sum is strictly greater than \(\sqrt{(N-1)/N}\). Thus every nonstar conditional distance is strictly smaller than the star-center value. The star center therefore gives the unique extremal graph up to isomorphism. Direct squaring yields its stated value, agreeing with the known complete/star formula.

## Verification
The standalone script `verify.py`, run with packages listed in `requirements.txt`, independently diagonalizes finite graph Laplacians, groups exact spectral degeneracies and reconstructs dephased terminal density matrices. It checks 576 localized sites across all \(1\le m,n\le8\); 9,998 fixed-order bipartite topology comparisons through order 200; 225 weighted-graph finite-time short-time slopes; and 12 nonstar examples with strict reversal. Its execution reports `VERIFY_OK pinching=576 topology=9998 weighted_short_time=225 reversal=12`. Numerical checks do not replace Steps 1–5 and do not establish a unique switching time.

## Relationship to prior work
Gualtieri, Benedetti and Paris introduced the fidelity-based quantum–classical distance, proved its localized-input reduction, and found the noiseless short-time degree coefficient; these are reused and credited. Bressanini, Benedetti and Paris studied intrinsic dephasing of continuous-time quantum walks, gave its general spectral pinching and exact complete-, cycle-, and star-graph asymptotics. In particular, their previously known equality of star- and complete-graph terminal distances is recovered here, not claimed as a separate discovery. The new claims are the weighted noisy short-time coefficient, the exact complete-bipartite two-class terminal formula, the forcing of a class reversal for every \(2\le m<n\) and every \(\gamma>0\), and the complete-bipartite topology extremum. Luppi, Benedetti and Smirne studied temporal nonclassicality under related dephasing dynamics, but their inspected results concern other observables and regular graph families, without the bipartite reversal classification. The older study of Ahmadi and collaborators concerns coherent mixing on balanced multipartite graphs, not this fidelity optimization.

## Limitations
The bipartite statements require unit, homogeneous edges. The weighted short-time lemma covers general symmetric weighted graphs, but the explicit terminal formula and reversal are proved only for complete bipartite networks. Dephasing must be energy-basis intrinsic decoherence with \(\gamma>0\); the \(\gamma=0\) quantum walk need not converge pointwise at late times. The proof establishes existence, not uniqueness or a closed-form location, of a finite-time initial-class transition. No statement is made about experimental error, noise in the vertex basis, correlated many-particle walks, or weighted bipartite extremal problems.

## References
1. G. J. Milburn, “Intrinsic decoherence in quantum mechanics,” Physical Review A **44**, 5401 (1991), doi:10.1103/PhysRevA.44.5401 (public 1991-11-01).
2. A. Ahmadi, R. Belk, C. Tamon and C. Wendler, “Mixing in Continuous Quantum Walks on Graphs,” arXiv:quant-ph/0209106 (first public 2002-09-18).
3. V. Gualtieri, C. Benedetti and M. G. A. Paris, “Quantum-classical dynamical distance and quantumness of quantum walks,” arXiv:1910.01563 (first public 2019-10-03), Physical Review A **102**, 012201 (2020).
4. G. Bressanini, C. Benedetti and M. G. A. Paris, “Decoherence and classicalization of continuous-time quantum walks on graphs,” arXiv:2204.01836 (first public 2022-04-04), Quantum Information Processing **21**, 317 (2022).
5. P. Luppi, C. Benedetti and A. Smirne, “Temporal nonclassicality in continuous-time quantum walks,” arXiv:2512.18873 (first public 2025-12-21), Physical Review A **113**, 042212 (2026).
