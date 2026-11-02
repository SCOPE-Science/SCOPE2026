# Self-review

**Finding under review.** For a symmetric continuous-time Markov star with \(k\ge3\) leaves, independently chosen positive bidirectional rates, arbitrary positive linear prices and budget \(B\), the unique minimizer of the maximum ordered-pair mean first-hitting time is equal-rate unless the largest price exceeds \(k\) times the sum of the remaining prices. In the premium regime only the maximally priced edge is slowed, with the precise ratio and objective shown in `RESULT.md`.

## Correctness — PASS

First-step hitting equations independently derive \(H_{ij}=1/r_i+k/r_j\) for distinct leaves, with center-to-leaf and leaf-to-center times also computed. Thus the objective is exactly \(kx_{(1)}+x_{(2)}\), for reciprocal rates \(x_i=1/r_i\). An order-statistic replacement argument proves that all waiting times except possibly the largest are equal; exchanging the exceptional leaf proves it must be a maximally priced leaf. The remaining ratio optimization has positive second derivative \(2p/(Bt^3)\), giving the sharp threshold, strict optimizer uniqueness and closed value. A rational Gaussian-elimination test and deterministic rate-design probes replayed successfully (249020 checks). The proof, not those samples, covers all real prices and all sizes in scope.

## Originality — PASS on inspected evidence, with specified risk

The existing Markov-chain literature provides hitting-time identities (Aldous–Fill) and budgeted **spectral-gap** optimization (Sun–Boyd–Xiao–Diaconis). Neither inspected statement entails the sharp minimax **mean hitting-time** allocation under arbitrary positive prices. Zeng's weighted-tree theorem optimizes **average** hitting time over graph structures with a *fixed weight multiset*, not independently variable rates on a fixed star. Berman's older convex project-resource optimization is a broader methodological predecessor; only its abstract was accessible, not the full article, so direct derivation from that work cannot be categorically excluded. No inspected exact published table or equivalent threshold was found, but a negative search is not proof of absolute priority. The claim's originality assessment concerns the complete unique-optimizer classification, not generic convex optimization or standard hitting-time formulas.

## Mathematical value — PASS

The sharp concentration threshold \(p=kP\) is a structural bifurcation of optimal rate design: even highly heterogeneous individual costs are immaterial until one cost overwhelms the aggregate of all others. The exact benefit \((\sqrt p-\sqrt{kP})_+^2/B\) quantifies when paying for nonuniformity becomes advantageous. The complete result works for every star size and arbitrary positive prices, with an elementary reproducible proof and a direct robust-latency interpretation. It is not a mere change of notation for a known average-hitting or spectral-gap problem.

## Sources, comparisons and limitations

Aldous and Fill, Chapters 2.2, 3.7 and 5.3, provide hitting-time identities and unweighted-tree extremal comparisons; https://www.stat.berkeley.edu/users/aldous/RWG/Book_Ralph/book.html . Sun et al. (2006) optimize the weighted Laplacian spectral gap under a linear budget; https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf . Zeng (2021) optimizes average hitting time for weighted-tree topology and weight-multiset problems; https://arxiv.org/abs/2109.09249 . Berman (1964) discusses generic PERT time-cost allocation; https://doi.org/10.1287/mnsc.10.4.734 . The latter full text was not inspected. The theorem does not assert any result for general tree topologies, nonuniform stationary masses or asymmetric rate control. Further independent originality and proof assessments may change the scientific status.

Self-review: passed. Independent audit: not yet performed.
