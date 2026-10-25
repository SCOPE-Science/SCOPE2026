# Scientific review: sharp one-edge conductance amplification

## Correctness — PASS

The proof fixes a precise Euclidean-orthogonal weighted-incidence projector on ordinary edge-coordinate \(\ell_1\). The unweighted complete-bipartite projection has the explicit row-plus-column kernel; the weighted Laplacian differs by a rank-one form on the mean-zero vertex space. The displayed inverse update is valid for every positive conductance, and the signs and multiplicities of the affected column are exact. The two exceptional column norm functions are optimized analytically by a two-dimensional Rayleigh quotient (or differentiation). Uniform bounds strictly below \(5\) for ordinary cut columns and \(6\) for ordinary cycle columns, combined with the exact inequality \(L_r>6\) when \(r\ge29\), establish that no other column can overtake the exceptional one at any conductance. The same analysis gives unique maximizing weights and the sharp asymptotic constant. Independent exact-rational incidence-matrix reconstruction was performed for 38,124 entries; these computations corroborate rather than replace the proof.

## Originality — PASS, subject to bibliographic uncertainty

The closest sources are Schild–Rao–Srivastava (2017), arXiv:1708.01632, which bounds spectral norms of entrywise absolute weighted transfer-current operators and gives a distinct parallel-path lower-bound example; Dilworth–Kutzarova–Ostrovskii (2023), arXiv:2305.12582, which develops mainly unweighted invariant/minimal cycle projections on tori and Hamming graphs; and Gurel-Gurevich–Nachmias–Sachdeva (2026), arXiv:2605.24130, which establishes an improved spectral-norm localization estimate for the absolute symmetrized transfer-current matrix. The spectral norm of that nonnegative matrix differs from the maximum absolute column sum optimized here. Unweighted complete-bipartite projection formulas and a single-edge deletion formula concern static or zero-conductance cases and do not establish the conductance-optimized sharp \(\sqrt r\) law. The rank-one inverse identity is known; no novelty is asserted for it. Public research-record searches and available same-subject claims identified no dominating exact weighted-endpoint theorem, but incomplete indexing and equivalent representations in electrical-network literature remain risks.

## Mathematical value — PASS

The phenomenon is a sharp, unbounded endpoint-norm amplification caused by changing a single conductance in an otherwise dense, regular graph whose uniform-weight norms stay below \(4\). The exact optimization distinguishes cut and cycle: their optimal weights differ but obey a nontrivial product identity, even though the maximum values agree. This separates individual column localization from spectral localization in a natural family and gives explicit examples with sharp leading \(\sqrt r\) growth. The sufficient threshold \(r\ge29\) is not claimed optimal, nor are all nonorthogonal projections classified.

## Limitations and residual risks

The theorem addresses only one tunable conductance on balanced complete bipartite networks, ordinary edge-coordinate endpoint norms, and canonical Euclidean-orthogonal projections. The cited electrical localization papers do not state the precise claim in the portions examined, but a less-indexed source could use an equivalent electrical or matrix-norm formulation. No human mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
