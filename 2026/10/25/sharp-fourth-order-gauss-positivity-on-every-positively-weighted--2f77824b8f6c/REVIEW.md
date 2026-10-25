# Self-review

## Correctness — PASS

The exact scope is every finite star with at least two leaves, strictly positive arbitrary edge weights, and the completed order-four two-stage Gauss–Legendre diffusion step. The proof explicitly reduces the off-diagonal signs to complex-resolvent imaginary parts. The block Schur complement is checked against the weighted star Laplacian. The center-to-leaf entry has the sign of \(\Phi_i\); its minimum occurs at maximum-conductance spokes. A sector argument then proves every distinct-leaf entry strictly positive whenever the center entries are nonnegative. Positive definiteness proves diagonal positivity; a strict scalar monotonicity certificate yields the sharp unique finite cutoff or unconditional case, including equality and tied maxima.

The standalone `verify.py` was executed against the included source with `VERIFY_OK`, using exact arithmetic for 87 weighted-star matrices and 846 off-diagonal matrix entries, plus symbolic scalar identities and exact resolvent comparisons on diagnostic four-vertex cases. Finite checks are corroboration only. The analytical argument handles all positive real conductances and arbitrary finite star size. A failed step is not confused with spectral instability or negative internal stages.

## Originality — PASS, with residual risks

The closest general literature provides strong-stability-preserving method restrictions (Gottlieb–Shu–Tadmor, 2001) and linear-operator SSP timestep analysis (Gottlieb–Gottlieb, 2003). The relevant full-text sections contain neither a weighted-star two-stage Gauss classification nor the one-equation nonreentry result. Blanes–Iserles–Macnamara (2022) treats graph-Laplacian exponential-based positivity-preserving methods, which differ from the fixed Gauss rational update studied here.

A prior complete-multipartite result covers constant-weight stars but not arbitrary conductance vectors. A prior three-site classification includes two-spoke weighted stars but has no statement for three or more spokes. The present arbitrary-size criterion \(w_*\sum_i1/w_i\le m+1\) and the exact monotone finite-horizon classification do not follow from these restricted cases. Published-record searches also addressed equivalent resolvent, inverse-conductance, Padé, graph diffusion and Markov-chain formulations. No mathematically dominating coverage was found. Residual risks include specialized graph-filter literature not indexed by the searches and the possibility of an equivalent theorem formulated with complex resolvents rather than time integrators.

## Value — PASS

The criterion distinguishes an explicit dimensionless region of unconditional positivity from sharp finite-step failure for arbitrary numbers of heterogeneous spokes, with a unique, computable root and a precise identification of the first negative transitions. Weighted stars are natural hub-and-spoke diffusion and transport models. The four-site cases with conductances \((2,2,3)\) and \((2,2,4)\) exhibit a sharp meaningful boundary without any topological change. The result provides a reusable test for a standard fourth-order implicit integrator, not merely a finite lookup or a special-case restatement.

## Scope and remaining limitations

This review evaluates the theorem as written, not its unknown priority outside the inspected references. Individual implicit stage positivity, directed edges, zero edge weights, nonstar graphs and variable-coefficient dynamics are excluded. The published search and same mathematical model proof check are not independent expert validation.

Self-review: passed. Independent audit: not yet performed.
