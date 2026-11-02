# Scientific review of the dyadic-complete-hypergraph cut-spectrum theorem

## Correctness (PASS)

The complete quantum state is defined without implicit normalization or gauge convention. The phase of a weight-\(w\) word is \((-1)^{\binom{w}{k}}\); Lucas' theorem gives exactly bit \(j\) when \(k=2^j\). Its two-block carry is a local-unitary-invariant residue sign \(F_{r,s}\). The orthonormal residue vector compression is exact; every residue occurs for block size at least \(k-1\), and adjacent row differences show \(|\det F|=2^{k-1}\). Consequently the Schmidt rank and finite nonzero spectrum are rigorous. The roots-of-unity filter handles arbitrary sequences of increasing block sizes, and the antiperiodic Laplacian identity diagonalizes the limit. The limiting purity and entropy constant follow from convergent sums. A direct independent small-state singular-value calculation and separate integer/trigonometric matrix checks have been replayed from `checker.py`; logs by themselves are not offered as a proof. The simultaneous \(k,a,b\) regime is specifically unproved.

## Originality (PASS on examined evidence, residual historical risk)

The exact claim was compared at the level of its finite cut matrix, all-positive rank, limiting cosecant-square spectrum, purity and iterated finite-entropy limit. The original hypergraph-state framework (Rossi et al., 2012), local one-site entropy law (Qu et al., 2013), general entanglement classifications (Gühne et al., 2014), geometric symmetric-state measure and special odd-cardinality decompositions (Nöller et al., 2023), random CCZ purity (Zhou and Hamma, 2021), and residual-free bilinear-core rank certificates (Fajardo and Paraschiv, 2026) were considered. The most relevant full papers were inspected to distinguish their result statements from ingredients usable in an additional calculation. A general real-coefficient-matrix framework does **not** itself prove this particular explicit spectrum; nor does a lower bound on Schmidt rank determine the density eigenvalues. No inspected work states or directly implies the combined dyadic all-cut formulas and the unusual finite-entropy limit. This is a best-knowledge literature comparison, not proof of historical uniqueness. Boolean-matrix / symmetric-state literature remains the main risk.

## Mathematical value (PASS)

The complete uniform hypergraph family is a canonical permutation-invariant many-body gate resource. General entanglement bounds leave its cut-spectrum and scaling law undetermined. Exact \(k\)-dimensional compression replaces a \(2^a\)-by-\(2^b\) quantum amplitude problem; the antiperiodic Fourier law reveals a persistent nonflat spectrum, purity approaching \(1/3\), and finite von Neumann entanglement when interaction arity and Schmidt rank diverge. This sharp limit is useful for assessing correlations and tensor-network entanglement cost, beyond a tiny fixed example or routine computation.

## Closest sources and remaining limitations

The closest direct comparators are Nöller et al., arXiv:2302.01695 (especially the sections on symmetric complete hypergraph states, geometric entanglement and local-unitary representations), and Fajardo--Paraschiv, arXiv:2602.21016 (especially its rank-certificate theorem and discussion). Their analyses do not state the exact finite-cut dyadic spectrum or the iterated finite-entropy limit. All conclusions are restricted to unweighted qubit complete hypergraphs, dyadic hyperedge size, eligible cuts and iterated limits. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
