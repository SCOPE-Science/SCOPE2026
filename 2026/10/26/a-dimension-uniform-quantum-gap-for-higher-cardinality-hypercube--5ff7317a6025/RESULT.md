# A dimension-uniform quantum gap for higher-cardinality hypercube rendezvous

## Finding

Let \(d\) and \(t\) be integers with \(t\ge 2\) and \(d>2t\). In the uniform balanced rendezvous game on the binary \(d\)-cube, two noncommunicating players receive vertices at Hamming distance \(2t\), each changes exactly \(t\) coordinates, and win when their final vertices coincide. Write \(\omega_{\mathrm Q}(d,t)\) for the supremum of success probabilities over all finite-dimensional entangled strategies and \(\omega_{\mathrm{NS}}(d,t)\) for the no-signalling value. Then

\[
\boxed{\displaystyle
\omega_{\mathrm Q}(d,t)\le
\frac{\binom{2t}{t}}{\binom{d}{t}}
-\frac{\binom{2t}{t}(d-2t)}{512(d-t)\binom{d}{t}^{4}}
<\omega_{\mathrm{NS}}(d,t)=\frac{\binom{2t}{t}}{\binom{d}{t}}.}
\]

The positive gap is independent of the local Hilbert-space dimensions. For example, the \((d,t)=(5,2)\) game satisfies \(\omega_{\mathrm Q}(5,2)\le 0.599999609375<\omega_{\mathrm{NS}}(5,2)=0.6\). Thus a previously known obstruction to *attaining* the no-signalling value is strengthened to an obstruction to *approaching* it with finite-dimensional strategies of arbitrarily large dimension.

## Assumptions and scope

Identify vertices with subsets of \([d]=\{1,\ldots,d\}\), let \(\sigma\triangle\tau\) be their symmetric difference, and write \(\Omega_t=\{A\subseteq[d]:|A|=t\}\). The ordered inputs \((\sigma,\tau)\) are uniform over \(|\sigma\triangle\tau|=2t\). Alice outputs \(A\in\Omega_t\), Bob outputs \(B\in\Omega_t\), and success means \(\sigma\triangle A=\tau\triangle B\). Local measurements may depend on the received input. Arbitrary shared finite-dimensional states, POVMs, entanglement dimensions, and shared randomness are allowed. A quantum strategy can be purified and simultaneously Naimark-dilated to a common pure bipartite unit state \(\psi\) and local input-indexed projective measurements. The proof uses only this representation.

Set

\[
N=2^d,\qquad k=\binom dt,\qquad c=\binom{d-t}{t},\qquad \ell=\binom d{2t},\qquad
\theta=\frac{c(d-2t)}{d-t}>0.
\]

The identity \(c/\ell=\binom{2t}{t}/k\) and the no-signalling benchmark are established by the elementary counting construction in Wang's Lemma 5.1 and Appendix A [1]. We also derive the upper bound directly below.

## Proof

**1. An exact quantum-score deficit identity.** Label a local output by its final vertex \(\zeta\) rather than by the flipped subset. For \(|\sigma\triangle\zeta|=t\), let \(E_{\sigma,\zeta}\) and \(F_{\sigma,\zeta}\) be Alice's and Bob's projectors, with each local \(t\)-sphere of projectors summing to the identity. Define vectors in the **same** bipartite Hilbert space by

\[
a_{\sigma,\zeta}=(E_{\sigma,\zeta}\otimes I)\psi,
\qquad b_{\tau,\zeta}=(I\otimes F_{\tau,\zeta})\psi.
\]

Each local family of vectors is orthogonal and sums to \(\psi\); hence its squared norms sum to one. Commutation of the two local projections gives the success-branch probability

\[
\mathbb P(\zeta,\zeta\mid\sigma,\tau)
=\langle a_{\sigma,\zeta},b_{\tau,\zeta}\rangle\ge0.
\]

For a fixed meeting vertex \(\zeta\), the admissible successful input pairs are \((\zeta\triangle A,\zeta\triangle B)\) for \(A,B\in\Omega_t\) with \(A\cap B=\varnothing\). Introduce the nonnegative mismatch energy

\[
\mathcal E=\sum_{\zeta\subseteq[d]}
\sum_{\substack{A,B\in\Omega_t\\A\cap B=\varnothing}}
\big\|a_{\zeta\triangle A,\zeta}-b_{\zeta\triangle B,\zeta}\big\|^2.
\]

Every local output appears in exactly \(c\) disjoint-pair branches. Expanding all squares, using local normalization and counting the \(N\ell\) ordered input pairs, yields the **exact** identity

\[
\boxed{\quad \frac c\ell-\omega=\frac{\mathcal E}{2N\ell}.\quad}\tag{1}
\]

Here \(\omega\) is the success probability of the given strategy. In particular, \(\omega\le c/\ell\) without any separate appeal to the no-signalling theorem. The known no-signalling construction attains \(c/\ell\) [1].

**2. A quantified Kneser-graph consistency estimate.** The Kneser adjacency matrix \(K\) on \(\Omega_t\) has \(K_{A,B}=\mathbf1_{A\cap B=\varnothing}\), and degree \(c\). Its eigenvalues belong to

\[
\lambda_j=(-1)^j\binom{d-t-j}{t-j},\qquad 0\le j\le t.
\]

For completeness, on the subset-incidence functions \(f_S(A)=\mathbf1_{S\subseteq A}\) with \(|S|=j\), inclusion-exclusion gives

\[
K f_S=\binom{d-t-j}{t-j}\sum_{T\subseteq S}(-1)^{|T|}f_T.
\]

The nested spans of these functions are \(K\)-invariant and end at the full function space when \(j=t\). Their successive quotients have the displayed scalar eigenvalues. Since \(d>2t\), the constant eigenvalue \(c\) is simple and every other eigenvalue has magnitude at most \(\binom{d-t-1}{t-1}=c-\theta\). Applying this bound to the two-color incidence form gives, for arbitrary Hilbert-space vectors \((x_A),(y_A)\),

\[
\sum_{A\cap B=\varnothing}\|x_A-y_B\|^2
\ge\theta\sum_{A\in\Omega_t}
\big(\|x_A-v\|^2+\|y_A-v\|^2\big),
\quad v=\frac1{2k}\sum_A(x_A+y_A).\tag{2}
\]

Indeed, subtract the two means from \(x,y\), use the operator-norm bound on the mean-zero subspace, and note that the remaining mean-difference mode has energy-to-variance ratio \(2c\ge\theta\). Applied independently at each \(\zeta\), (2) bounds \(\mathcal E\) in terms of the deviations from the meeting-vertex mean.

**3. Translation symmetrization and a uniform stability parameter.** Average over simultaneous translations of both inputs and both outputs by uniformly shared \(g\subseteq[d]\). This preserves the score and is a valid finite-dimensional quantum strategy (put \(g\) in correlated classical registers, purify those registers, and use projective measurements controlled by the local register). We may therefore work with a translation-covariant vector representation. Set

\[
v_\zeta=\frac1{2k}\sum_{A\in\Omega_t}
\big(a_{\zeta\triangle A,\zeta}+b_{\zeta\triangle A,\zeta}\big).
\]

By translation covariance, \(p=\|v_\zeta\|\) is independent of \(\zeta\). Likewise there is an \(h\ge0\) such that, for **every** \(\zeta\) and **every** input \(\sigma\), respectively,

\[
\sum_{A\in\Omega_t}\|a_{\zeta\triangle A,\zeta}-v_\zeta\|^2=h^2,
\qquad
\sum_{\substack{\zeta:\,|\sigma\triangle\zeta|=t}}
\|a_{\sigma,\zeta}-v_\zeta\|^2=h^2.\tag{3}
\]

Summing (2) over meeting vertices and retaining just Alice's deviations gives

\[
\mathcal E\ge\theta N h^2.\tag{4}
\]

At each input \(\sigma\), the orthogonal local vectors \(a_{\sigma,\zeta}\) have squared norms summing to one. The triangle inequality in the direct sum of the \(k\) output spaces, followed by (3), yields \(\sqrt{k}\,p\ge1-h\). Completeness also yields

\[
\left\|\psi-\sum_{|\sigma\triangle\zeta|=t}v_\zeta\right\|\le\sqrt{k}\,h.\tag{5}
\]

For any two distinct final vertices \(\zeta,\zeta'\) belonging to a common \(t\)-sphere about \(\sigma\), Alice's corresponding projective branches are orthogonal. Comparing them with the two \(v\)-vectors using (3) gives

\[
|\langle v_\zeta,v_{\zeta'}\rangle|\le2ph+h^2.\tag{6}
\]

**4. An extra Hamming layer forces nonzero error.** Fix \(\zeta_0\in\Omega_{t-2}\) and let \(\sigma_0=\varnothing\). Then \(\zeta_0\notin\Omega_t\), the \(t\)-sphere centered at \(\sigma_0\). For every \(\zeta\in\Omega_t\), the distance \(|\zeta_0\triangle\zeta|=2s\) is even and lies between \(2\) and \(2t-2\). To find a common sphere containing \(\zeta_0,\zeta\), choose \(s\) coordinates from their difference and \(t-s\) outside it. This is possible since \(d>2t\), and yields a vertex at distance \(t\) from both. Thus (6) applies to \(v_{\zeta_0}\) and every \(v_\zeta\) with \(\zeta\in\Omega_t\).

Write \(F_\sigma=\sum_{|\sigma\triangle\zeta|=t}v_\zeta\). Using (5)--(6) at \(\sigma_0\) gives

\[
|\langle v_{\zeta_0},\psi\rangle|\le k(2ph+h^2)+p\sqrt{k}\,h.
\]

Now choose any \(\sigma_1\) at distance \(t\) from \(\zeta_0\); its sphere contains \(\zeta_0\). Using (5)--(6) again gives

\[
|\langle v_{\zeta_0},\psi\rangle-p^2|
\le(k-1)(2ph+h^2)+p\sqrt{k}\,h.
\]

Combining these inequalities,

\[
p^2\le(2k-1)(2ph+h^2)+2p\sqrt{k}\,h.\tag{7}
\]

If \(h\ge1/2\), then already \(h\ge1/(16k^{3/2})\). Otherwise, \(p\ge(1-h)/\sqrt{k}\ge1/(2\sqrt{k})\). Divide (7) by \(p^2\); since \(k\ge\binom52=10\), it follows that

\[
1\le12k^{3/2}h+8k^2h^2.
\]

For \(h<1/(16k^{3/2})\) the right side is strictly less than \(3/4+1/(32k)<1\), a contradiction. Therefore

\[
\boxed{\displaystyle h^2\ge\frac1{256k^3}.}\tag{8}
\]

**5. Dimension-free conclusion.** Combining (1), (4), and (8) gives

\[
\frac c\ell-\omega\ge\frac{\theta}{512k^3\ell}
=\frac{\binom{2t}{t}(d-2t)}{512(d-t)k^4}.
\]

The estimate holds for every finite-dimensional strategy with the same positive constant, so it holds for their supremum. This is the claimed theorem. \(\square\)

## Verification

The script `verify.py` and its dependency specification `requirements.txt` (Python 3 and NumPy) are included with this result. Install the listed dependency if necessary with `python -m pip install -r requirements.txt`. Running `python verify.py` checks the Kneser spectra and spectral gaps for seven parameter choices, the two-layer common-sphere lemma, integer/binomial identities, and the exact deficit/energy/Poincaré inequalities for forty independent symmetrized deterministic protocols and six noncommuting entangled-qubit protocols. It reports **861 passing finite assertions**. The infinite family and arbitrary quantum dimension are established by the analytic proof, not by finite experimentation. For reproducibility, recompute the displayed combinatorial constants from integer binomial coefficients and follow proof steps (1)--(8).

## Relationship to prior work

Wang [1], especially Lemma 5.1, Theorem 5.5, Theorem 6.4, and Appendix A, proves the no-signalling benchmark and rules out **exact finite-dimensional attainment** for \(t\ge2\), \(d>2t\), while explicitly leaving strict inequality between the *quantum supremum* and no-signalling value open. The present bound fills precisely that distinction by controlling approximate saturation uniformly across all finite dimensions. Wang's projective-resolution argument and the standard Kneser spectrum are used as antecedents, not claimed as new. The quantum perfect-matching games studied by Cui and collaborators [2] use a different winning predicate and their perfect-strategy results do not determine the value of this uniform hypercube rendezvous game. Earlier mobile-agent rendezvous papers [3,4] motivate entanglement-assisted coordination, but the present quantitative claim concerns the specific fixed-cardinality game and open supremum question in [1].

## Limitations

The constant is explicit but almost certainly not sharp; it is designed to prove a positive separation, not to optimize the true quantum value. The method does not determine whether \(\omega_{\mathrm Q}(d,t)>\omega_{\mathrm C}(d,t)\). It assumes \(t\ge2\), \(d>2t\), uniform ordered input pairs and a single exact-cardinality update. It does not assert the same separation when \(t=1\), \(d=2t\), the input law changes, or communication is allowed. Independent external validation and literature-wide priority certification have not been performed.

## References

[1] C. Wang, *Quantum-assisted rendezvous on hypercubes: a quantum Bernoulli noise approach*, arXiv:2610.12949v1 (public 2026-10-09), https://arxiv.org/html/2610.12949v1 .

[2] D. Cui, L. Mančinska, S. S. Nezhadi, D. E. Roberson, *Quantum Perfect Matchings*, Annales Henri Poincaré (2025), https://doi.org/10.1007/s00023-025-01632-5 .

[3] G. Viola and P. Mironowicz, *Quantum Strategies for Rendezvous and Domination Tasks on Graphs with Mobile Agents*, Physical Review A 109, 042201 (2024), https://arxiv.org/abs/2311.11817 .

[4] J. Tucker et al., *Quantum Nonlocal Games on Graph Ensembles*, arXiv:2606.16784 (2026), https://arxiv.org/abs/2606.16784 .
