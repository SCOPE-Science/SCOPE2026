# Exact consensus and persistent-disagreement law for weighted majority-rule sunflowers

## Finding

A connected three-uniform hypergraph can fail to reach unanimous agreement under repeated asynchronous majority interactions, even when every hyperedge continues to be sampled forever. For the entire family of weighted sunflower hypergraphs, the following theorem gives all eventual outcomes and exact consensus probabilities.

**Theorem.** Fix an integer \(m\ge1\). The vertices are a hub \(v\) and \(m\) disjoint pairs \(\{a_j,b_j\}\), with hyperedges \(e_j=\{v,a_j,b_j\}\). At each discrete update choose \(e_j\) independently with probability \(\pi_j>0\), with \(\sum_{j=1}^m\pi_j=1\), and replace its three binary opinions by their local majority. Define an initially pure petal to mean \(a_j=b_j\), and an initially mixed petal to mean \(a_j\ne b_j\). Then:

1. Every initially pure petal stays unchanged. Each initially mixed petal becomes pure, with color equal to the then-current hub opinion, on its first activation and never changes thereafter. Almost surely every petal becomes pure in finite time.
2. If initially pure petals of both colors are present, global consensus has probability zero. If all petals are initially mixed, global consensus has probability one, and its color is the initial hub color. If initially pure petals have only color \(\sigma\), then eventual consensus has probability one when the hub initially has color \(\sigma\), and otherwise has probability exactly \(\sum_{j:a_j=b_j=\sigma}\pi_j\). In the last case any consensus must have color \(\sigma\).
3. If all opinions are independent Bernoulli-\(p\) variables, \(0\le p\le1\), the eventual consensus probabilities are

\[
\Pr(\mathrm{consensus\ at\ }0)=(1-p)^2(1+2p)(1-p^2)^{m-1},
\]
\[
\Pr(\mathrm{consensus\ at\ }1)=p^2(3-2p)[p(2-p)]^{m-1}.
\]

These probabilities do not depend on the positive weight vector \(\pi\). In particular, if \(p=1/2\),

\[
\boxed{\Pr(\mathrm{ever\ reaching\ consensus})=(3/4)^{m-1}.}
\]

For fixed \(0<p<1\), consensus becomes exponentially unlikely as \(m\to\infty\). If \(p=\lambda/\sqrt m\) for fixed \(\lambda\ge0\) and sufficiently large \(m\), the total consensus probability tends to \(e^{-\lambda^2}\).
4. After the first activation of every initially mixed petal, if the pure petals have both colors, all leaf opinions are constant forever while the future hub opinions are independent draws with conditional probability \(\sum_{j:a_j=b_j=1}\pi_j\) of opinion 1. Both hub opinions occur infinitely often almost surely.
5. Under uniform selection \(\pi_j=1/m\), put \(H_r=\sum_{k=1}^r1/k\) and \(H_0=0\), and let \(T\) be the first global-consensus update count. When all petals initially are mixed, \(\mathbb E T=mH_m\). When exactly \(r\) petals initially are mixed and all pure petals have common color \(\sigma\), \(\mathbb E T=mH_r\) if the hub initially equals \(\sigma\). If the hub initially opposes \(\sigma\), then \(\mathbb E[T\mid T<\infty]=1+mH_r\). These formulas include \(r=0\).

## Assumptions and scope

The graph is a **sunflower of three-vertex hyperedges with a one-vertex core**. Distinct petals have no vertices in common; every vertex belongs to a hyperedge, and the two-section graph is connected. No adaptive rewiring, external noise, simultaneous multiple-edge update, or edge-dependent opinion preference is present. The positive edge probabilities are fixed across time; they need not be equal. The random initial law in part 3 is independent and identically distributed on the hub and all leaf vertices, with common parameter \(p\). Parts 1, 2, and 4 apply to every deterministic initial binary state. Time formulas in part 5 count discrete edge draws, including draws that do not change any opinion.

## Proof

**Local transition and freezing.** Fix an edge \(e_j\). If its leaf pair is monochromatic, its two leaves form the strict majority regardless of the hub opinion. Consequently, the leaves are unchanged and the hub becomes their color. If its leaf pair is mixed, exactly one leaf agrees with the hub, and that opinion is the strict majority. The hub remains unchanged and both leaves acquire its color. Thus a petal is irrevocably pure after its first activation; a pure petal never changes. Since every \(\pi_j>0\), the probability that some initially mixed edge has not been selected by time \(t\) is at most \(\sum_{j=1}^m(1-\pi_j)^t\to0\). This proves finite-time freezing almost surely.

**Deterministic-state outcome classification.** Initially pure petals of both colors are permanently inconsistent, so global consensus is impossible. If every petal starts mixed, no selected edge can flip the hub, and every pair ultimately copies its fixed opinion; unanimity follows. Otherwise, let \(\sigma\) be the only initially pure-petal color and let \(M\) be the set of mixed petals. If the hub starts as \(\sigma\), every update preserves its color and all pairs eventually equal \(\sigma\). If it starts as \(1-\sigma\), the very first chosen edge decides: selecting an initially pure \(\sigma\) petal flips the hub to \(\sigma\) before any mixed petal is imprinted, after which consensus is certain; selecting a mixed petal first permanently imprints the incompatible color \(1-\sigma\) and consensus becomes impossible. The probability of the former event is precisely the total selection weight of pure \(\sigma\) petals.

**The independent-initialization law.** Put \(u=(1-p)^2\), \(v=p^2\), and \(w=2p(1-p)\) for the probabilities that a leaf pair begins pure 0, pure 1, or mixed. Eventual consensus at 0 occurs if the hub initially equals 0 and no petal starts pure 1, or if the hub initially equals 1, the very first selected petal starts pure 0, and every other petal is either pure 0 or mixed. Since the initial pair states are independent and \(\sum_j\pi_j=1\),

\[
\begin{aligned}
\Pr(\mathrm{consensus\ at\ }0)
&=(1-p)(u+w)^m+p\sum_{j=1}^m\pi_j u(u+w)^{m-1}\\
&=(1-p)^2(1+2p)(1-p^2)^{m-1}.
\end{aligned}
\]

Interchanging 0 and 1 yields the second formula. Notice that every edge-selection weight disappears from the resulting averages, although deterministic-state probabilities generally depend on these weights. At \(p=1/2\), each consensus color has probability \(\tfrac12(3/4)^{m-1}\). For fixed interior \(p\), both exponential bases \(1-p^2\) and \(p(2-p)\) lie strictly below 1. For \(p=\lambda/\sqrt m\), the first prefactor tends to 1, \((1-p^2)^{m-1}\to e^{-\lambda^2}\), and the second contribution vanishes, giving the stated limit.

**Persistent disagreement.** Almost surely there is a finite time \(\tau\) by which every pair has become pure. Its color \(c_j\) is fixed thereafter. For every update strictly after \(\tau\), the selected pure pair is the strict majority, so the hub's new opinion equals \(c_{J_t}\), where the future indices \(J_t\) are independent with law \(\pi\). Conditional on the final pair colors and the update history through \(\tau\), these post-\(\tau\) hub opinions are independent Bernoulli variables of parameter \(\sum_{j:c_j=1}\pi_j\). If both colors occur, this parameter is strictly between 0 and 1, making infinitely many occurrences of each color almost sure. The leaf disagreement itself cannot disappear.

**Consensus times.** When the hub remains aligned with the only pure-petal color, global consensus is first achieved when every initially mixed petal has been selected. For \(r\) designated petals under uniform independent edge draws, the successive stages with \(k\) unseen designated petals take geometric waiting times of means \(m/k\); their sum is \(mH_r\). If the initial hub opposes the only pure-petal color but eventual consensus succeeds, the first edge is necessarily pure and flips the hub in one draw. By independence of later draws, the remaining expected collection time is \(mH_r\). When all petals start mixed, the same coupon-collection argument applies with \(r=m\). For \(r=0\) the aligned state is already unanimous, while the opposed hub becomes aligned after the first draw. This completes the proof.

## Verification

The companion standard-library program `verify_std.py` solves the exact rational first-step Markov equations for every binary initial state of each one-hub sunflower with \(1\le m\le6\). It tests both uniform and nonuniform positive selection weights and compares every resulting hitting probability with the theorem's deterministic-state formula. It also sums the exact hitting probabilities under independent Bernoulli initial laws for five parameters and checks an independent binomial decomposition. Run `python3 verify_std.py`; the recorded result is `PASS 21906 exact rational finite-state/initial-law comparisons`. These finite checks support the structural analysis but are not the proof for arbitrary \(m\).

## Relationship to prior work

Noonan and Lambiotte (2021) introduce and investigate exactly the asynchronous three-agent majority-update rule on complete, tripartite, modular, and degree-heterogeneous hypergraphs, primarily using diffusion approximations. They explicitly motivate exact analysis of small structured hypergraphs and consensus times. Their complete-hypergraph exit probability is not an exit formula for a sunflower with frozen disjoint leaf pairs. Lanchier and Neufer (2013) define general hypergraph majority-update stochastic dynamics and derive results for blocks on spatial lattices; their general generator specifies the process but does not identify the present family-specific outcome or independent-initialization formulas. Golovin, Mölter, and Kuehn (2024) study majority propagation with adaptive hyperedge rewiring and mean-field motif equations; that different model does not entail an exact law for a fixed, weighted one-core sunflower. Relevant published-result searches for `hyperstar`, `sunflower`, `three-body majority`, `exact exit probability`, `frozen petals`, and the formula \((3/4)^{m-1}\) did not reveal an equivalent exact theorem. This negative search observation is not a uniqueness proof.

## Limitations

The theorem assumes disjoint two-vertex petals, strict three-agent binary majority, independent stationary positive selection probabilities, and, for the closed unconditional law, independent identically distributed initial opinions. Its formulas need not hold when petals overlap, weights vanish, group sizes differ, or update mechanisms introduce noise or rewiring. The theorem addresses eventual unanimity, not cessation of all opinion changes: when both pure-petal colors survive, the hub fluctuates forever. Exhaustive rational checks cover only \(m\le6\); the infinite family follows from the local-invariance and first-selection proof. The literature comparison cannot exclude an unindexed equivalent result, and the theorem has not undergone independent external validation.

## References

1. J. Noonan and R. Lambiotte, *Dynamics of Majority Rule on Hypergraphs*, arXiv:2101.03632v1 (first publicly posted 2021-01-10), *Physical Review E* **104**, 024316 (2021), https://arxiv.org/abs/2101.03632, https://doi.org/10.1103/PhysRevE.104.024316.
2. N. Lanchier and J. Neufer, *Stochastic Dynamics on Hypergraphs and the Spatial Majority Rule Model*, *Journal of Statistical Physics* **151**, 21–45 (2013), https://doi.org/10.1007/s10955-012-0543-5; preprint https://arxiv.org/abs/1301.0151.
3. A. Golovin, J. Mölter, and C. Kuehn, *Polyadic Opinion Formation: The Adaptive Voter Model on a Hypergraph*, *Annalen der Physik* **536**, 2300342 (2024), https://doi.org/10.1002/andp.202300342.
