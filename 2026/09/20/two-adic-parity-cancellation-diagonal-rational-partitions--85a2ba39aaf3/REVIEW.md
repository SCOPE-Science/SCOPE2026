# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS. The trace identity follows directly from character orthogonality. Even numerators force the odd part O of L_N to divide 2j+1; the remaining characters are exactly the Galois conjugates of a primitive 2D-th root, with D the largest power of two not exceeding N. Odd-numerator/even-denominator geometric sums reduce to the displayed finite factors, and cyclotomic trace kills every reduced monomial except the constant term. The N=8 reduction is an exact calculation in Z[x]/(x^8+1). A separate bounded-residue computation gives A_8(-1)=0 and A_8'(-1)=-592704000. The denominator multiplicities then give a pole of order 10 at -1, while all other nontrivial roots have raw order at most 7, proving s_8=10 and the stated parity contribution in degree 9. Exact integer verification reproduces the published N=3,...,7 values and the cancellation census through N=100.

## Originality

PASS, to the best of our knowledge. The motivating September 2026 preprint gives the residue numerator and pole framework and tabulates A_N(-1) only for N=3,...,7, where N=4 is the sole cancellation. Its accessible main text does not state the 2-adic trace reduction, the N=8 cancellation, s_8=10, the degree-9 parity amplitude, or the larger exact census. Searches using the paper title, A_N(-1), parity/root-of-unity cancellation, residue numerator, rational-partition Ehrhart terminology, and period-collapse/Fourier-Dedekind terminology did not locate prior coverage of these claims. General Fourier-Dedekind and Ehrhart period-collapse literature is methodologically related but does not by itself imply the specific formula.

The principal residual originality risk is the ancillary source archive of arXiv:2609.18945. The accessible paper says that an `anc/` directory contains a finite arithmetic certificate for the displayed small-N computations, but that ancillary material was not inspected. It may contain broader code or additional finite evaluations. The main-text theorem and the result here remain mathematically distinct, but the finite census originality should therefore be read with this limitation. Concurrent work on the very recent preprint is another residual risk.

## Value

PASS. The result turns a cancellation question involving an L_N-character Fourier sum into exact arithmetic in a cyclotomic ring whose degree is only the largest power of two at most N. It shows that the N=4 cancellation visible in the motivating paper is not isolated: N=8 is already a second example, and the exact census through 100 contains eleven further post-table cases. At N=8 this has a concrete quasipolynomial consequence: the maximal raw parity pole drops by one, making one additional leading coefficient constant and yielding an explicit parity oscillation in the first nonconstant coefficient.

## Limitations

No classification of all N is claimed, no infinite cancellation family is proved, and roots of unity other than -1 are not classified. The exact value of s_N is proved here only for N=8 among the new census entries. The census stops at N=100. No independent validation, independent audit, or formal proof-assistant verification is asserted.
