# Self-review

## Correctness

**PASS.** The parity-pattern injection is valid for all positive caps because the minimum of equally-paritied integers retains that parity. The binary-prefix embedding has identity Gram matrix, proving the linear bound. Four- and eight-vector witnesses satisfy all diagonal and pairwise congruences. The finite exact six-orbit claim uses exhaustive one-candidate-per-odd-pattern recursion: all eight groups have sixteen candidates, every allowable candidate is visited, and branches are discarded only on infeasibility. The independent clique algorithm gives the same sharp maxima for all three- and four-coordinate cases through cap three. Direct-sum padding proves the stated bound for all larger coordinate counts. The standalone embedded checker was executed successfully; infinite conclusions rest on the proofs, not on extrapolation.

## Originality

**PASS with historical priority risk.** Banerjee–Dewan, arXiv:2610.21636v1, treats the same multiset intersection but the **even-diagonal Eventown** requirement, which cannot imply the present odd-diagonal classification. The classical binary Oddtown embedding yields an upper bound, not the new cap-three witness and orbit. An earlier two-bounded Oddtown result establishes the cap-two values, including the value six for four coordinates, but does not cover the new value eight at cap three or the doubled-family amplification. Targeted mathematical-record queries and literature comparisons found no equivalent formulation or stronger coverage. Non-detection is not uniqueness proof; possible older bounded-lattice parity work remains a risk.

## Mathematical value

**PASS.** The work identifies the first saturated small-dimensional parity-pattern cases under a genuine multiplicity cap, completely classifies the labelled four-coordinate cap-three optimizers, and yields a uniform lower bound whose leading coefficient doubles the one-bounded Oddtown optimum. These are intrinsic extremal questions in the same coordinate-minimum multiset model, not an arbitrary parameter slice. The exact larger-coordinate maximum and priority beyond inspected sources remain unresolved.

## Closest literature and limitations

Primary scientific comparison: Anirban Banerjee and Abisek Dewan, *An Eventown Result for Multisets*, arXiv:2610.21636v1 (first submitted 2026-10-15); Umesh Shankar, *Oddtown and eventown theorems for lattice paths*, arXiv:2607.23117v1; Berlekamp's classical Oddtown theorem; Sudakov–Vieira, *Two remarks on Eventown and Oddtown problems* (2018). The cap-two special case was established separately and is not claimed new. Exactly six optimal families are established only for cap three and ground-set size four; for larger ground sets the construction is only a lower bound. No independent audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
