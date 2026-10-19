# Scientific assessment: marked butterfly-walk transfer

## Correctness — PASS

The object is the exactly defined flip-flop, discrete-time coined walk on \(P_2\square K_{1,m}\), with the two body coins negated, and normalized uniform *outgoing* arc vectors at sender and receiver. Bipartite tail parity establishes all even-time zeros. The eight-state permutation-invariant reduction for \(m\geq1\), its fully displayed matrix, the factored characteristic polynomial, and three direct initial amplitudes determine the odd-step sequence uniquely. The resulting cosine formula holds for every integer \(m\geq0\). The rational-algebraic-integer argument proves irrationality of the relevant angle for all \(m\geq2\), which rigorously distinguishes finite perfect transfer from unbounded fidelity supremum. Equidistribution proves the Cesàro limit. No numerical experiment is used as a substitute for the infinite family proof.

The standalone exact-arithmetic checker independently evolves full, unsymmetrized directed-edge systems for all \(0\leq m\leq15\) through 55 updates (880 exact comparisons), including the alternate incoming-target convention, and reproduces the \(m=3\), \(t=31\) exact rational fidelity. The proof does not rely on these finite examples.

## Originality — PASS with residual literature risk

The source of the butterfly graph, marked coin assignment, and numerical plots is Rani–Banerjee–Swami–Dutta, arXiv:2604.11620v1. In its \(B_3\) body-to-body setup, the source gives the same normalized outgoing vectors and coins and reports fidelity equal to unity at certain observed times. It does not derive the all-wing formula or prove exact versus pretty-good transfer. The present result yields exact fidelity strictly below unity at the reported \(t=31\), making that distinction substantive.

Štefaňák–Skoupý (arXiv:1608.00498) consider two marked leaves of a star rather than two high-degree body vertices of a star prism. Chan–Zhan (arXiv:2105.03762) give spectral criteria for a particular reflection-coin class; Xu–Zhan (arXiv:2511.06750) allow more general reflection coins but define transferred states at a vertex inside the \(+1\) coin eigenspace, while the uniformly outgoing states in this theorem are in the \(-1\) marked-coin eigenspaces. Bhakta–Bhattacharjya (arXiv:2508.09711) study unmarked Grover walks on abelian Cayley graphs, unlike these nonregular marked butterflies. Semantic claim searches and prior-results comparisons found no claim that directly subsumes the all-integer-wing trichotomy; absence of matches is not uniqueness proof. The residual possibility of an implicit deduction from broader quantum-walk transfer theory is acknowledged.

## Value — PASS

The classified observable is the natural sender-to-receiver state-transfer fidelity of a growing family of quantum communication networks. The exact all-size phase law resolves whether the near-unit numerical peaks are attained at finite time, shows a sharp one-wing obstruction, and proves arbitrarily high fidelity without any exact transfer for every number of wings above one. The resulting all-size trichotomy and closed long-time mean are structural and physically interpretable, rather than a small numerical increment or an arbitrarily chosen slice.

## Scope and residual risks

The theorem addresses only the noiseless two-body-vertex signed-Grover protocol, uniform outgoing source/target coin states, and integers \(m\geq0\). It makes no claim about transfer time at fixed tolerance or channels with noise. A different vertex-measurement convention or different marked vertices require separate analysis; incoming normalized target arcs are handled by an explicit one-step identity. General spectral transfer theory could provide another proof, but the inspected cited statements do not assert this same theorem. The findings have not undergone independent external assessment.

Self-review: passed. Independent audit: not yet performed.
