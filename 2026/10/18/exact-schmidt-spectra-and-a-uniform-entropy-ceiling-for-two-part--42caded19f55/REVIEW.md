# Scientific review

## Correctness — PASS

The specified walk is the ordinary Grover walk on the product graph, restricted by the initial state to its balanced complete-bipartite component. A direct two-step reflection argument establishes period four. The coefficient matrix at step two is a reshaped Kronecker product of a rectangular matrix \(G\) and its transpose, and at odd steps its active nonzero block is \(G\) up to permutations. Trace and two-by-two minors of \(G\) give the exact two eigenvalues \(\mu_\pm\), from which all reduced-density spectra, entropies, rank restrictions and saturation conditions follow. The fixed-edge balancing inequality and large-size expansion are elementary consequences of those eigenvalues. The standalone script checks the **full tensor-arc update**, not the proof's reduced matrix, for both exchange symmetry signs; 90 independent time/size/sign comparisons passed. These finite checks are supporting evidence rather than an all-size proof.

## Originality — PASS, with stated limits

The closest primary paper, Kubota–Matsubara–Segawa, arXiv:2607.09066v1, defines the walk and proves an entropy-saturation classification for the special regular graphs \(K_{n,n}\). That regular-case statement and the paper's intermediate amplitude calculations are prior work. The assessed extension is the complete reduced-density spectrum and entropy formula on **all irregular \(K_{m,n}\)** as well as the sharp uniform rank/entropy ceiling, fixed-edge balancing law and large-size behavior. The relevant 2015 paper by Carson–Loke–Wang, arXiv:1511.04828v1, investigates a locally modified tensor-product coin, not the Grover reflection on the graph product. Claim-directed record and literature searches found no identical statement. An unlocated derivation from a broader framework or unindexed publication remains possible; this is not an independence certificate or a claim that searching proves uniqueness.

## Value — PASS

For the emerging two-particle Grover construction, the original literature asks when full Hilbert-space entanglement is obtained. An exact spectrum is a natural and more informative invariant than a yes/no saturation test. It exposes a **constant eight-dimensional Schmidt support** even when the particle Hilbert-space dimension grows without bound, quantifies the decay of extra entropy for large bicliques, and determines which bipartite aspect ratios maximize entanglement for a fixed edge count. These statements address scalable quantum-walk correlation generation and a natural graph-structure dependence, rather than arbitrary numerical instances.

## Relationship to the closest literature and limitations

Sources inspected as material primary text: https://arxiv.org/html/2607.09066v1 (model, evolution, section 4 formulas, theorem and discussion) and https://arxiv.org/html/1511.04828v1 (sections on interaction coin, graph examples and conclusions). The present result retains the same initial opposite-edge states and entropy convention as the first paper. It does not apply to other initial states, coins, or graph classes, and the particle-factor entropy for indistinguishable particles need not equal an operational LOCC resource. Possible implicit derivability from a general theorem is the main residual originality risk.

Self-review: passed. Independent audit: not yet performed.
