# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The proof extends the exact reduction of Essayag--Zabokritskiy by one redundancy level. Their established cases reduce redundancy fifteen to a finite set of parameter tuples. Exact-integer evaluation of their dimension cap and binomial covering test leaves exactly the binary tuple \((q,t,R_t)=(2,3,6)\), consistent with the tuple explicitly singled out in their conclusion.

For that tuple, a violation gives \(d_3(C)\ge15\). The dual-weight argument is checked directly: a 4-dimensional dual subcode supported on at most \(k+1\) coordinates would leave fourteen parity-check columns in an 11-dimensional kernel, yielding nullity at least three and therefore \(d_3(C)\le14\). Thus \(d_4(C^\perp)\ge k+2\).

Shortening the dual on nine coordinates corresponding to independent parity-check columns gives a binary \([N,6]\) code with \(N=k+6\) and \(d_4\ge N-4\). The generator-column interpretation of \(d_4\) then says every 2-dimensional subspace of \(\mathbb F_2^6\) contains at most four columns counted with multiplicity. A direct 31-line incidence sum proves \(N\le64\), including the cases of zero or repeated generator columns. This agrees with the established generalized Griesmer bound for fourth generalized Hamming weight.

Hence the original code has \(n\le73\). The necessary covering-ball inequality requires \(V_8(n,6)\ge2^{45}\), while exact arithmetic gives \(V_8(73,6)=20,282,523,983,828<35,184,372,088,832=2^{45}\). The contradiction closes the sole residual tuple. `artifacts/verify.py` independently reproduces all finite parameter arithmetic with exact integers.

Potential failure modes checked include the direction of the generalized-weight inequality under shortening, zero columns in the shortened generator matrix, multiplicities in the projective incidence count, strictness of the binomial exclusion, and monotonicity of the covering-ball volume in the length.

## Originality

**PASS, to the best of our knowledge.** The most relevant source is Essayag--Zabokritskiy, arXiv:2609.19098v1, submitted 16 September 2026. It proves the conjecture universally through redundancy fourteen and explicitly identifies \(\rho=15,t=3,R_3=6\) as the first binary triple not excluded by its reductions, with dimension cap \(k\le78\). The present result closes that triple and verifies that the same reduction excludes every other redundancy-fifteen tuple, raising the universal threshold to fifteen.

Searches used “generalized packing-covering conjecture” together with “redundancy fifteen” / “redundancy 15”, the residual parameter triple, and generalized Hamming-weight/generalized covering-radius formulations. Repository searches used the same mathematical terms. No earlier statement of the redundancy-fifteen theorem was located.

The generalized Griesmer theorem is prior work and is not claimed as new. The direct six-dimensional incidence argument is included as a self-contained special-case proof, not as an originality claim. The finite reduction, dual-weight framework, covering-ball inequality, and known exceptional parameter cases are also inherited from the cited source.

No specific inaccessible paper was identified as especially likely to contain the exact redundancy-fifteen theorem. Residual risk is unusually time-sensitive because the main source is very recent: a simultaneous or unindexed follow-up could independently close the same first residual triple. Accordingly the originality statement is strictly qualified and no guarantee of first discovery is asserted.

## Value

**PASS.** The result resolves the first parameter regime explicitly left open by the newest universal bounded-redundancy theorem and advances the field-independent threshold from fourteen to fifteen. The additional argument is short, structural, and reusable: the previously coarse dimension cap is sharpened in the exceptional binary case by a six-dimensional generalized-weight obstruction before the exact covering-ball bound is applied.

## Access and residual uncertainty

The current arXiv source was inspected through its theorem, reduction, dimension-cap, and conclusion statements. The generalized Griesmer statement and its geometric formulation were also inspected in the cited public source. No scientifically material source needed for the proof remained inaccessible.

No independent validation is asserted.
