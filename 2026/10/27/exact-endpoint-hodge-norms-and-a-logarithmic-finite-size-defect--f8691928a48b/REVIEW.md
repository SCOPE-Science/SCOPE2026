# Scientific review

## Correctness — PASS

The full proof starts from the exact factorization \(L=(3I+A)L_C\) and a cyclic resolvent with exponentially decaying alternating kernel. It obtains every cut-projection edge column for both displacement classes and the diagonal effective resistances. The universal kernel inequalities bound the short-edge norm, a five-current lower estimate handles the long-edge norm, and exact strict dominance follows analytically for \(n\ge17\) (cut) and \(n\ge36\) (cycle). Exact rational elimination checks all smaller admissible integers; the separate direct graph-Laplacian replay checks the current formulas. The two infinite geometric tails establish the logarithmic asymptotics. The checked executable is `checker.py`; no floating-point experiments replace proof. The claim excludes nonorthogonal projection optimization and general cycle powers.

## Originality — PASS, with residual bibliographic risk

The principal eligible framework is Dilworth--Kutzarova--Ostrovskii, arXiv:2305.12582 (first posted 2023-05-21), on invariant cycle projections and torus/Hamming examples. The strongest same-object comparison is the published squared-cycle pairwise hitting-time formula of Doi et al., arXiv:2110.12614, together with Chair's exact effective resistances, arXiv:1401.5628. Their data can recover each electrical projection entry by polarization, but do not by themselves select the maximizing edge orbit or evaluate its absolute norm and logarithmic finite-size defect. Those are the precise additional statements proved here. Indexed research-record searches covered the same graph, Cayley generator presentation, Hodge/transfer-current aliases, absolute column sums, and logarithmic corrections. An equivalent calculation in less-indexed network literature remains possible; the older circulant paper DOI:10.1002/qua.21068 was not fully inspected.

## Mathematical value — PASS

The graph \(C_n^2\) is the first nontrivial power of a cycle with two edge directions, a natural test of endpoint behavior beyond cycles, tori and Hamming graphs. The result simultaneously gives all finite-size norms, proves the strict direction of the maximum for both complementary projections, and identifies a nonstandard common \(\log n/n\) correction with an explicit coefficient. That correction originates in the alternating Green-kernel sign threshold, rather than in elementary spectral or effective-resistance averages.

## Scope and limitations

Only real, unweighted, canonical Euclidean-orthogonal cut/cycle projections on squared cycles with at least seven vertices are covered. The finite certificate covers exactly 29 integer sizes; the infinite tail uses the written analytical inequalities. The full published source landscape cannot be exhaustively certified, and independent mathematical evaluation is pending.

Self-review: passed. Independent audit: not yet performed.
