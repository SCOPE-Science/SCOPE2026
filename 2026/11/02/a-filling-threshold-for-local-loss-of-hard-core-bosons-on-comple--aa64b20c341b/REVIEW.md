# Review: A filling threshold for local loss of hard-core bosons on complete quantum networks

## Correctness — PASS

The result concerns an initial maximally mixed fixed-\(k\) occupation sector on a complete \(N\)-site graph, with one strictly positive local first-jump rate and nonzero real uniform hopping. The maximal invariant zero-occupation space gives the infinite-time survival fraction. For hard-core bosons, the escaping-amplitude map is the Boolean down operator \(D_k\), and its kernel is invariant under the remaining-site Johnson adjacency \(U_{k-1}D_k-kI\). The up/down commutator proves the exact rank of \(D_k\). For fermions, exterior-power diagonalization of the one-particle all-to-all Hamiltonian and contraction at the loss site determine the other dark dimension. These are analytic finite-dimensional arguments for all \(N\ge4\), \(1\le k<N\). They give the two capture probabilities and threshold exactly. The included numerical checker independently constructs the occupation-sector matrices: 66 spectral-sector tests and 48 dissipative matrix-exponential tests passed. Numerical checks alone would not prove the theorem, and no such inference is used.

## Originality — PASS, with historical-priority risk

The accessible research-record and primary-literature searches found studies of two-particle 1D quantum walks (Qin et al., arXiv:1402.3349), hard-core-boson state transfer on weighted paths (Large–Underwood–Feder, arXiv:1412.1022), Johnson graph coherent single-vertex search (Wong, arXiv:1601.04212), general dark-state suppression in single-excitation transport (Le et al., arXiv:1707.07482), statistics-dependent loss in 1D optical lattices (Malo et al., arXiv:1709.03464), and fermionic entanglement on Johnson physical graphs (Bernard–Crampé–Vinet, arXiv:2104.11581). Their useful techniques and distinct subject matter are acknowledged; none of the inspected claims implies the paired all-filling capture formulas. A published two-coordinate Johnson-face concentration result was also read in full; its cumulative low-degree compression is a different operator, not the one-coordinate local-loss dark projector. Previously recorded single-particle sink formulas likewise do not imply the \(k\)-particle statistics comparison. Uninspected specialized many-body dissipative or Johnson-scheme work may still contain equivalent statements. Independent historical-priority certification is not claimed.

## Mathematical value — PASS

The contrast of first-loss survival between hard-core bosons and spinless fermions on the *same* complete physical network is a natural exchange-statistics diagnostic. The exact bosonic probability \(\min\{2k/N,1\}\) reaches certainty at half filling, while the half-filled fermionic uncaptured weight approaches \(1/4\). The strict gap for interior fillings and exact underlying dark-space dimensions are structural results across an infinite network family, not merely isolated numerical data or a routine parameter optimization.

## Scope and limits

The conclusion concerns eventual occurrence of the first jump from the specified maximally mixed initial ensemble. It does not determine finite-time waiting-time laws, multiple jumps, site disorder, broken uniformity or interactions beyond hard-core exclusion. Calculations on a bounded set of small sectors are corroborative only.

Self-review: passed. Independent audit: not yet performed.
