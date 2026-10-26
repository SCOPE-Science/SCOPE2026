# Self-review

## Correctness — PASS

Each payoff is strictly concave in its player's own contribution; differentiating gives the unique response \(x_i=\max(0,\theta_i-x_{f(i)})\). The cycle reduction is exhaustive for outdegree-at-most-one loopless digraphs. The clipped-affine composition lemma is checked algebraically with an exact parameter recursion, and the fixed-set classification is obtained by solving the two possible clipped linear equations. Unique backward propagation proves no missing equilibria; compactness and continuous coordinate inversion establish the stated topology. The generic uniqueness result uses finitely many proper alternating-sum hyperplanes. The independent affine-piece checker exhausts 3276 parameterized cycles and matches the full fixed sets. Assumptions, parity, endpoints, and the balanced singleton case are handled. Risk: rational finite tests do not independently establish the universal algebraic proof; real-valued arithmetic-operation complexity omits bit-size costs.

## Originality — PASS (bounded best-knowledge comparison)

The primary Huang–Sun–Xu–Zhao paper arXiv:2512.23193v1 was inspected in Sections 2–5 and its relevant appendix. Its Theorem 1 is an equivalence between **specialized** equilibria and graph kernels, with a directed 3-cycle example; it does not state the heterogeneous one-out-neighbor **all-equilibrium** interval classification. Papadimitriou–Peng arXiv:2106.00718v2 develops complexity classifications and bounded-treewidth approximate computation for general public-goods games, not an explicit exact cycle-geometry and measure-zero genericity theorem. Deligkas et al. arXiv:2511.11475v1 addresses binary shareable goods, not continuous threshold contributions. General complementarity-matrix results cover some component-level linear-equation reasoning but do not by themselves provide the present exact full geometry as a stated theorem. Targeted full-text and research-record searches revealed no equivalent/dominating statement. An inaccessible 2022 paper on constrained heterogeneous public goods and possible implicit LCP treatments remain priority risks; priority is not certified.

## Mathematical value — PASS

This is a natural complete classification for a sparse but economically interpretable directed spillover class, in which specialized-equilibrium existence can fail on odd cycles. It solves the **entire** continuous equilibrium correspondence in explicit linear arithmetic time, identifies the precise codimension-one degeneracy set, and demonstrates discontinuous equilibrium selection under tiny heterogeneous shocks. The singleton balanced example shows that alternating balance alone is not sufficient and that the positivity boundary matters. These outcomes answer structural and comparative-static questions not supplied by a routine existence argument. No claims are made for denser graphs or dynamic stability.

Self-review: passed. Independent audit: not yet performed.
