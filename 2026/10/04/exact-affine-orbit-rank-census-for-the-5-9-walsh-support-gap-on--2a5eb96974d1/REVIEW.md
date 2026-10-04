# Same-model review

## Correctness
PASS. The claim reduces exact support \(5\) and exact Fourier support \(9\) to a finite row-space criterion for \(7\times5\) Walsh restrictions. The criterion is proved by annihilator duality and the fact that finitely many proper subspaces cannot cover a nonzero complex vector space. The affine generators exhaust all \(4368\) five-point supports in two orbits. Every rank-deficient representative case is recomputed over exact rational arithmetic; modular arithmetic is used only to certify full rank when a nonzero minor survives modulo a prime. The packaged verifier reproduces the orbit sizes, rank distributions and obstruction counts and ends with `VERIFY_OK`.

## Originality
PASS for the structural census stated in the Finding. Krahmer--Pfander--Rashkov provide the general rank criterion and a numerical support-pair diagram for groups of order at most \(16\), so novelty is not claimed for the bare plotted absence of \((5,9)\). The inspected primary text does not give the two five-support affine orbits, the exact \(3248\) and \(160\) deficient-set counts, the rank split, or the \(3184/64/160\) obstruction split. Targeted searches under Walsh, Hadamard, exact-support, affine-orbit and rank-deficient-submatrix terminology found no equivalent statement. Residual risk remains for an unindexed small-matrix census under different terminology.

## Value
PASS. This is a complete, natural finite classification of the mechanism behind a historically numerical uncertainty-diagram entry. It reduces all five-point supports to two affine types and distinguishes two substantive failure mechanisms: a forced zero coefficient in time or an unavoidable eighth Fourier zero. That structural compression is more informative than simply rerunning the original numerical support-pair test.

## Closest literature and limitations
The closest source is Krahmer--Pfander--Rashkov, arXiv:math/0611493, especially Lemma 3.4 and Figure 2. Meshulam's finite-Abelian uncertainty inequality supplies broader lower bounds but does not decide this exact support pattern. The result is finite and does not classify the full order-16 diagram or any infinite family.

Same-model review: passed. Independent audit: not yet performed.
