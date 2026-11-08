# An improved dimension-free quantitative gap in balanced hypercube rendezvous

## Final claim and priority boundary

Fix integers \(t\ge2\) and \(d>2t\), and put \(k=\binom dt\), \(c=\binom{d-t}{t}\), and \(\ell=\binom d{2t}\). In the uniform balanced rendezvous game, Alice and Bob receive uniformly distributed ordered cube vertices \(\sigma,\tau\in\{0,1\}^d\) at Hamming distance \(2t\); each changes exactly \(t\) coordinates, and they win when their final vertices agree. Their noncommunicating finite-dimensional entangled strategies can use arbitrary shared states, local POVMs, dimension, and shared randomness. Then

\[
\boxed{\quad\omega_{\mathrm{NS}}(d,t)-\omega_{\mathrm Q}(d,t)
\ge\frac{\binom{2t}{t}(d-2t)}{512(d-t)\binom dt^4}>0,\qquad
\omega_{\mathrm{NS}}(d,t)=\frac{\binom{2t}{t}}{\binom dt}.\quad}
\]

**The qualitative strict separation is not new.** An earlier proof, publicly recorded on 12 October 2026 in *HypercubeRendezvousQuantumGap* and *RendezvousVectorSystemGap* [2], already established the same uniform-in-dimension strict quantum/no-signalling inequality for every such \((d,t)\). In fact [2] proves the quantitative relative deficit
\[
1-\frac{\omega_{\mathrm Q}}{\omega_{\mathrm{NS}}}\ge
\frac1{k^4(4\sqrt2\,t+2)^2}.
\]
The claim made here is **only the stronger quantitative stability estimate**
\[
\boxed{\quad1-\frac{\omega_{\mathrm Q}}{\omega_{\mathrm{NS}}}
\ge \frac{d-2t}{512(d-t)k^3}.\quad}
\]
It improves the known polynomial dependence on \(k\) by one full power, and is stronger numerically for every admissible \(d,t\). It does not claim to be sharp or to solve the quantum-versus-classical advantage problem. The method is a Kneser spectral Poincaré estimate combined with a two-Hamming-layer near-orthogonality contradiction, rather than the earlier exchange-chain bound.

To compare the two explicit estimates, their ratio (new deficit divided by the previous deficit) is
\[
 R(d,t)=\frac{k(d-2t)(4\sqrt2\,t+2)^2}{512(d-t)}.
\]
For fixed \(t\), \(\binom dt(d-2t)/(d-t)\) strictly increases with \(d\ge2t+1\). At the minimal \(d=2t+1\), both \(\binom{2t+1}{t}/(t+1)\) and \((4\sqrt2\,t+2)^2\) increase with \(t\ge2\). Thus \(R(d,t)\ge R(5,2)=(1320+320\sqrt2)/1536>1\).

## Proof of the improved bound

Write a cube vertex as a subset of \([d]\), with coordinate addition given by symmetric difference \(\triangle\), and let \(\Omega_t=\{A\subseteq[d]:|A|=t\}\). By simultaneous purification and Naimark dilation, a finite-dimensional strategy is represented by a common unit bipartite vector \(\psi\) and projective measurements \(\{E_{\sigma,\zeta}:|\sigma\triangle\zeta|=t\}\) and \(\{F_{\tau,\zeta}:|\tau\triangle\zeta|=t\}\). Here each output is indexed by the resulting vertex \(\zeta\), and the projectors for each local input sum to the identity. Define vectors in the same bipartite Hilbert space by
\[
 a_{\sigma,\zeta}=(E_{\sigma,\zeta}\otimes I)\psi,\qquad
 b_{\tau,\zeta}=(I\otimes F_{\tau,\zeta})\psi.
\]
Their local families are orthogonal and sum to \(\psi\). The probability of a successful branch with common final vertex \(\zeta\) is the real nonnegative inner product \(\langle a_{\sigma,\zeta},b_{\tau,\zeta}\rangle\), because the two local projections commute.

**Exact score-deficit identity.** Let \(N=2^d\). For each \(\zeta\), successful branches correspond bijectively to ordered disjoint \(A,B\in\Omega_t\), with input pair \((\zeta\triangle A,\zeta\triangle B)\). Define
\[
\mathcal E=\sum_{\zeta}\sum_{A\cap B=\varnothing}
 \|a_{\zeta\triangle A,\zeta}-b_{\zeta\triangle B,\zeta}\|^2.
\]
For a fixed local input and output, exactly \(c\) opposite-side outputs are disjoint. Expanding squared norms and using the completeness relations therefore gives \(\mathcal E=2Nc-2N\ell\,\omega\), where \(\omega\) is the success probability. Hence
\[
\boxed{\frac{c}{\ell}-\omega=\frac{\mathcal E}{2N\ell}.}\tag{1}
\]
The known no-signalling construction [1, §5 and Appendix A] attains \(c/\ell=\binom{2t}{t}/k\), as follows by extending the complement map on \(t\)-subsets of a prescribed \(2t\)-set to a permutation of \(\Omega_t\) and choosing the first output uniformly.

**Kneser expansion.** Let \(K\) be the \(k\)-by-\(k\) disjointness adjacency matrix on \(\Omega_t\). Every row has sum \(c\), and its distinct eigenvalues are
\[
\lambda_j=(-1)^j\binom{d-t-j}{t-j},\quad 0\le j\le t.
\]
One elementary proof uses the incidence functions \(f_S(A)=\mathbf1_{S\subseteq A}\) for \(|S|=j\). Their nested spans are invariant because inclusion-exclusion gives
\[
K f_S=\binom{d-t-j}{t-j}\sum_{T\subseteq S}(-1)^{|T|}f_T.
\]
Thus the action on the successive quotients is multiplication by \(\lambda_j\); when \(j=t\) these spans cover all functions on \(\Omega_t\). Since \(d>2t\), the eigenvalue \(c\) is simple and every other eigenvalue has absolute value at most
\(\binom{d-t-1}{t-1}=c-\theta\), with
\[
\theta=c\frac{d-2t}{d-t}>0.
\]
Consequently, for arbitrary Hilbert-space vectors \(x_A,y_A\), putting \(v=(2k)^{-1}\sum_A(x_A+y_A)\),
\[
\sum_{A\cap B=\varnothing}\|x_A-y_B\|^2\ge
\theta\sum_A\left(\|x_A-v\|^2+\|y_A-v\|^2\right).\tag{2}
\]
Indeed, split the two families into their constant means and mean-zero components. The singular norm of \(K\) on mean-zero components is at most \(c-\theta\), giving coefficient \(\theta\) for their variance. The difference-of-means component has energy-to-variance ratio \(2c\ge\theta\), proving (2).

**Symmetrization and common deviation.** Average any strategy over simultaneous translations \(g\in\{0,1\}^d\) of the two inputs and their final vertices. One may implement the average by shared uniform classical registers and then purify those registers. The resulting strategy is finite-dimensional, remains projective, and has the same score. For it, define
\[
 v_\zeta=\frac1{2k}\sum_{A\in\Omega_t}\left(a_{\zeta\triangle A,\zeta}+b_{\zeta\triangle A,\zeta}\right).
\]
Translation covariance makes \(p=\|v_\zeta\|\) independent of \(\zeta\). It also makes the following two Alice deviation totals equal to a common \(h^2\), independently of \(\zeta\) and \(\sigma\), respectively:
\[
\sum_{A\in\Omega_t}\|a_{\zeta\triangle A,\zeta}-v_\zeta\|^2=h^2,
\qquad
\sum_{|\sigma\triangle\zeta|=t}\|a_{\sigma,\zeta}-v_\zeta\|^2=h^2.\tag{3}
\]
Apply (2) at every meeting vertex \(\zeta\), retaining the Alice terms, to get
\[
\mathcal E\ge N\theta h^2.\tag{4}
\]
For a fixed input \(\sigma\), the orthogonal vectors \(a_{\sigma,\zeta}\) have total squared norm one. The reverse triangle inequality in their \(k\)-fold Hilbert direct sum, with (3), yields
\(\sqrt{k}\,p\ge1-h\). Also, because \(\sum_\zeta a_{\sigma,\zeta}=\psi\), Cauchy–Schwarz and (3) give
\[
\left\|\psi-\sum_{|\sigma\triangle\zeta|=t}v_\zeta\right\|\le\sqrt{k}\,h.\tag{5}
\]
For any distinct \(\zeta,\zeta'\) in one radius-\(t\) sphere about some \(\sigma\), their two Alice vectors are orthogonal. Write each as its respective \(v\)-vector plus an error with norm at most \(h\) by (3). It follows that
\[
|\langle v_\zeta,v_{\zeta'}\rangle|\le2ph+h^2.\tag{6}
\]

**Incompatible extra layer.** Fix a vertex \(\zeta_0\) of Hamming weight \(t-2\) and let \(\sigma_0=\varnothing\). Then \(\zeta_0\) lies outside the radius-\(t\) sphere about \(\sigma_0\). For any \(\zeta\) of weight \(t\), the distance \(|\zeta\triangle\zeta_0|=2s\) is an even integer between \(2\) and \(2t-2\). Select \(s\) coordinates in this symmetric difference and \(t-s\) outside it. This is possible since \(d>2t\); toggling the chosen \(t\) coordinates from \(\zeta_0\) gives a center at distance \(t\) from both vertices. Thus (6) applies to \(\zeta_0\) and every member of the sphere about \(\sigma_0\). Pairing (5) with \(v_{\zeta_0}\) gives
\[
|\langle v_{\zeta_0},\psi\rangle|\le k(2ph+h^2)+p\sqrt{k}\,h.
\]
Choose now any \(\sigma_1\) at distance \(t\) from \(\zeta_0\), so its radius-\(t\) sphere contains \(\zeta_0\). The analogous estimate separates its own \(v_{\zeta_0}\) term and yields
\[
|\langle v_{\zeta_0},\psi\rangle-p^2|
\le(k-1)(2ph+h^2)+p\sqrt{k}\,h.
\]
Their combination is
\[
p^2\le(2k-1)(2ph+h^2)+2p\sqrt{k}\,h.\tag{7}
\]
If \(h\ge1/2\), then \(h\ge1/(16k^{3/2})\) trivially, since \(k\ge10\). If \(h<1/2\), our earlier estimate implies \(p\ge1/(2\sqrt{k})\). Divide (7) by \(p^2\) and bound the coefficients to obtain
\[
1\le12k^{3/2}h+8k^2h^2.
\]
If \(h<1/(16k^{3/2})\), the right side is less than \(3/4+1/(32k)<1\), a contradiction. Hence
\[
\boxed{h^2\ge1/(256k^3).}\tag{8}
\]
Combining (1), (4), and (8),
\[
\frac c\ell-\omega\ge\frac{\theta}{512k^3\ell}
=\frac{\binom{2t}{t}(d-2t)}{512(d-t)k^4}.
\]
This bound holds uniformly for every finite-dimensional quantum strategy and so for their supremum. This proves the improved quantitative theorem. \(\square\)

## Verification and limitations

The companion `verify.py` and `requirements.txt` contain finite diagnostic checks of Kneser spectra, common-sphere geometry, score-deficit identities, and sample strategies; the analytic proof above does not rely on treating those tests as an exhaustive quantum search. Independently reproduced finite checks also cover small Kneser matrices, disjointness identities, and random deterministic strategies. The bound is conservative, not optimal, and the exact quantum value and strict quantum-versus-classical advantage remain open. There is no claim for \(t=1\), \(d=2t\), nonuniform input pairs, or protocols with communication. We assert no external attestation or worldwide priority certification.

## References and comparison

[1] C. Wang, *Quantum-assisted rendezvous on hypercubes: a quantum Bernoulli noise approach* (2026), arXiv:2610.12949v1, Theorem 5.5, Theorem 6.4, Section 7, Appendix A; https://arxiv.org/abs/2610.12949 . This paper proves exact finite-dimensional nonattainment and poses the strict-supremum question.

[2] *The quantum value of balanced hypercube rendezvous is strictly below its no-signalling value* (public proof recorded 2026-10-12), https://www.trureturing.org/research/wang-2026-hypercube-rendezvous-quantum-gap/ ; formal source `D5/S3/Quantum/Entanglement/HypercubeRendezvousQuantumGap.lean` in https://github.com/the-omega-institute/trureturing/commit/e49cc795f9ba7da8af100046ca34dd602be46c05 . This prior work resolves the qualitative supremum question and establishes the weaker explicit relative bound \(k^{-4}(4\sqrt2\,t+2)^{-2}\). The stricter order-\(k^{-3}\) relative bound above is the present quantitative contribution.

[3] D. Cui, L. Mančinska, S. S. Nezhadi, D. E. Roberson, *Quantum Perfect Matchings* (2025), https://doi.org/10.1007/s00023-025-01632-5 . It treats other matching-game predicates and does not imply the stated strengthened fixed-distance Hamming-rendezvous estimate.

[4] G. Viola and P. Mironowicz, *Quantum Strategies for Rendezvous and Domination Tasks on Graphs with Mobile Agents* (2024), https://arxiv.org/abs/2311.11817 . The graph-edge setting differs from this conditioned fixed-cardinality game.
