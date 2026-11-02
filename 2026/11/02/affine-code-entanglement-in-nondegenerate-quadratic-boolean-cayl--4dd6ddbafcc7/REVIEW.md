# Self-review

## Correctness — PASS

The exact claim is a full flat-spectrum classification of affine-flat cuts in nondegenerate quadratic Boolean Cayley graph states. The graph-state character sum reduces the complete reduced spectrum to a rectangular binary cut rank; taking row differences makes the polar pairing visible. On codimension-at-least-two flats, the complement affinely spans the ambient vector space, and the nondegenerate quadratic weight bound excludes the remaining nonlinear row from the affine-linear row span. Nonisotropic subspaces contribute an additional constant row. On hyperplanes, the restricted polar form has radical dimension one, and a non-affine row adds the final dimension. These steps prove all stated dimensions, offsets and quadratic refinements, not merely small cases. A standalone checker corroborated the rank formula in \(8952\) exact finite cases and confirmed eight direct sixteen-qubit reduced spectra, with maximum absolute error \(4.1633\times10^{-17}\). The numerical tests are supporting checks, not the infinite proof.

## Originality — PASS on examined evidence, with residual priority risk

Hein, Eisert and Briegel provide the **general** cut-rank identity, but do not supply the all-affine-flat symplectic isotropy dichotomy for quadratic Boolean Cayley graphs in the examined text. Leopardi discusses quadratic bent Cayley graphs and their equivalence classes, but does not establish the graph-state entanglement classification in the inspected sections or text searches. Brouwer and van Eijl study ranks of **whole** strongly regular adjacency matrices; that does not imply the spectrum of a rectangle indexed by a chosen affine subspace and its complement. Grassl, Klappenecker and Rötteler analyze graph-quadratic-code connections without the examined cut formula. Results on dual symplectic Fourier sampling on quadrics concern a different operator. Earlier affine-cut and Hamming graph-state results concern different graphs or cuts; neither implies this formula.

The unresolved historical-priority risk is a possibly unlocated theorem on modular cross-ranks of bent Cayley graphs, or a specialized pre-2016 quantum-network analysis; the 1999 Bernasconi–Codenotti work was retrieved only as metadata/abstract. No claim of a uniquely first result is made, and a negative search alone is not treated as proof of novelty.

## Mathematical value — PASS

The quadratic Boolean Cayley graph is a canonical natural strongly regular family with \(2^d\) qubits. Affine linear codes are natural subsystem index sets. The formula classifies their **complete** Schmidt spectra at every dimension and distinguishes symplectic isotropy by one exact ebit, despite a large ambient quantum Hilbert space. It shows that inequivalent graph types of different valence may nevertheless have indistinguishable affine-flat entanglement profiles. This is an all-parameter structural classification and quantum-network benchmark, not an arbitrary numerical slice or a routine restatement of generic cut-rank methods.

## Examined sources and limitations

Closest sources: Hein, Eisert and Briegel (arXiv:quant-ph/0307130, proposition on cut ranks); Leopardi (arXiv:1705.04507, bent-function Cayley graph classification); Brouwer and van Eijl (1992, whole strongly regular adjacency ranks); Grassl, Klappenecker and Rötteler (quadratic-form/code connections); Bernasconi and Codenotti (1999, abstract only). The proof applies only to nondegenerate quadratic forms in even dimension at least four, pure unit-weight qubit graph states, and affine-flat cuts. Wider cuts and other local dimensions are not treated. Independent expert and historical-priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
