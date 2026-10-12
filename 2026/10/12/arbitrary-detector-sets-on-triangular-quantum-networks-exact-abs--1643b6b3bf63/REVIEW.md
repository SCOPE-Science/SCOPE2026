# Scientific assessment: arbitrary detector sets on triangular quantum networks

## Correctness — PASS

The claim has a closed analytical proof for every integer \(N\ge3\), every nonempty detector placement, arbitrary nonzero uniform real hopping, every strictly positive choice of local loss rates, and every normalized initial state (also every density matrix). The incidence factorization \(A=B^{\mathsf T}B-2I\) yields three distinct spectral sectors; the unsigned-incidence kernel lemma computes each sector's detector-restriction rank. Their sum is exactly \(1+N-b(F)-u(F)+|D|-b(G)\). Dissipativity and positivity identify the complementary dark subspace with the actual infinite-time survival subspace, including the possibility of defective decaying modes. The tree/odd-unicyclic criterion and sharp detector minimum are derived from nonnegative componentwise nullities and explicit universal witnesses. The package's executable checker was run successfully: \(\texttt{VERIFY_OK spectral_ranks=1760 threshold_checks=14 loss_spectrum=80}\). Finite verification corroborates, but is not used to prove, the infinite-family theorem.

## Originality — PASS, with stated priority risk

The closest inspected work does not already state or imply the evaluated theorem as a corollary without additional new rank analysis. Agliari (arXiv:1102.3994, §2.3) formulates irreversible multi-trap walks on random graphs, not this arbitrary-detector exact triangular-graph classification. Wong (arXiv:1601.04212, §§1–2) studies unitary single-mark spatial search on Johnson graphs, a different dynamical problem. Vorob'ev, Mogilnykh and Valyuzhenich (arXiv:1706.03987, §§1–2) classify minimum **individual eigenfunction supports**, which does not determine whether a prescribed detector set simultaneously meets every nonzero eigenvector of each eigenspace. Novo et al. (Scientific Reports 5, 13304, 2015) and Razzoli, Paris and Bordone (arXiv:2011.13794, §§4–5) give projection-based transport approaches, chiefly for one trap; the latter identifies multiple traps as a further question. Abiad, Simoens and Zeijlemaker (arXiv:2302.07757, Corollary 9) establish the ordinary zero-forcing number, which is **different by two** from the exact minimum for this particular Hamiltonian and does not classify all absorbing placements. These are substantive distinctions of quantified statements and implication, not title comparisons.

Targeted mathematical-record and published-literature searches did not identify an identical arbitrary-placement theorem. The mathematical-record search is not a completeness guarantee, and there remains priority risk from broader control-theoretic studies of line-graph observability or unlocated literature. No independent human priority assessment is claimed.

## Value — PASS

This result answers a well-motivated quantum-transport design question: exactly which sets of lossy vertices destroy all dark states in the entire infinite family \(J(N,2)\)? The criterion handles **all** nonempty placements via simple graph-component invariants, and the constructive minimum \(\binom N2-N\) for \(N\ge5\) is sharp. The two-detector separation from the graph's ordinary zero-forcing number is a useful structural distinction between a fixed physical Hamiltonian and graph-uniform forcing guarantees. It provides a practical detector-design test without large-scale diagonalization and is more than a computation of a narrow arbitrary case.

## Closest sources and limits

The proof uses standard incidence and spectral facts, as well as established non-Hermitian trap dynamics; it does not claim those ingredients as novel. The quantitative classification is limited to homogeneous triangular graphs and irreversible local losses with strictly positive rates. No universal finite-time convergence constants, robust perturbation theorem, or exact sitewise formula for general detectors is established. Broader equivalent treatment in literature not inspected remains a residual priority risk.

Self-review: passed. Independent audit: not yet performed.
