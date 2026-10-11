# Review of exact gingerbreadman short-period spectrum

## Correctness (C): PASS
For each period \(p\le11\), the map's periodicity condition reduces on each of its \(2^p\) closed sign cells to a finite rational linear system plus exactly the appropriate sign inequalities. Rational elimination and exact Fourier–Motzkin projection decide every case; both choices at a zero coordinate prevent boundary omissions. The checker, `verify_periods.py`, returns exact feasible-branch and isolated-orbit counts for all eleven lengths. Explicit five-, six-, and eleven-cycle witnesses are checked by direct iteration. Products of exact \(2\)-by-\(2\) branch matrices yield the stated return traces. The claim asserts neither an unproved infinite classification nor uniqueness at period six.

## Originality (O): PASS with specified residual risk
The 2009 Abu-Saris–Al-Jubouri paper, inspected in full, identifies the gingerbreadman slice and derives general periodicity criteria and periods two and three, but does not count the two five-cycles or the two eleven-cycles or eliminate the intervening primitive lengths. MathWorld's listed outer five-cycle is only one of the two global five-orbits; the second has a different exact Jacobian type and is not a relabeling. The modern Cima–Gasull–Mañosa–Mañosas family has a second absolute-value term absent here, so its stronger general-map theorems do not cover this exact conservative map. The complete text of Devaney's 1984 founding article was not accessible; a full comparison with that original and unindexed sources remains a residual originality risk. Searches do not establish uniqueness on their own.

## Value (V): PASS
The finite cutoff at \(11\) is dictated by the first primitive period after the familiar five- and six-cycle regions; no new primitive length appears at \(7,8,9,10\). Exact global enumeration reveals a second five-cycle with hyperbolic, rather than elliptic, local geometry and two further hyperbolic eleven-cycles, supplying a natural finite invariant of the well-studied map rather than an arbitrary numerical slice. The no-gap and exact-class counts provide an independently reproducible benchmark for symbolic-dynamics and orbit-counting arguments.

## Evidence boundaries
The finite calculation is exact only because the complementary proof reduces real periodicity to finitely many rational linear-feasibility systems. The 1984 publication year predates the first separately verified day-stamped public artifact; no unverified day of first publication has been supplied. No independent review has occurred.

Same-model review: passed. Independent audit: not yet performed.
