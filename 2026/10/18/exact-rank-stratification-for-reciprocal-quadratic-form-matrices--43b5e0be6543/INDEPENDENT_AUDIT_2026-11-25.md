# Independent mathematical audit

## correctness

PASS

Pass for the corrected full claim in /workspace/repairs/1/RESULT.md, not for the original cubic illustration. For an independent rank derivation, multiply each nonzero-index column j by j². The nonzero-index block becomes 1/f(i/j), with eigenvectors j^r for 0≤r≤p−2 and eigenvalue −h_r, where h_r is the r-th coefficient of the degree ≤p−2 interpolant of 1/f. The row at index zero, constant 1/d on those columns, detects only r=0 and is nonzero there; the column at index zero is i^(p−3) on nonzero rows and zero at its top. These two boundary components together give rank two regardless of h_0,h_(p−3). The remaining eigenvalues count independently. Partial fractions and α^p=β give h_r=(α^(p−1−r)+β^(p−1−r))/(α−β)², so zeros are z^k=−1 for k in [1,p−2] excluding 2. Counting the class k≡t/2 mod t for even t gives the four stated cases: for t=2 only the endpoint p would be lost from the p+1-period count; for t=4 both p−1 and 2 are lost; for even t≥6 no endpoint or excluded 2 can contribute. Mod-p nullity gives the stated Smith-normal-form lower bound, not an exact integer valuation. Independent elimination checked all 1595 irreducible parameter pairs at p=5,7,11,13,17,19,23,29,31 and verified the p=19 ranks 15 and 17. Bareiss elimination of the actual integer matrix yields D_19(1,2)/19² ≡15 mod 19, disproving the frozen cubic claim. The corrected illustration uses 19² and the boundary-block explanation specifies all overlapping rows/columns. Replay: python3 /workspace/reproductions/full_rank.py. The supplied verifier was inspected, not executed. The finite reproduction corroborates, but does not replace, the all-prime argument.

## originality

PASS

For the corrected claim, credit the prior coefficient folding and p² result. The distinct contribution established on the stated irreducible locus is the complete finite-field rank stratification on the full matrix, in particular the order-four exception, not the general divisibility theorem for nonsquare d or a claim of exact integer valuations.

## value

PASS

The full rank refines a natural determinant congruence question to identify every rank deficiency, explaining when a stronger guaranteed power of p can be read off without computing the integer determinant. The order-four exception depends on the zero row/column boundary of the actual full matrix and is not an arbitrary special instance. The correction restores the square bound in the order-twenty example while leaving the genuinely sharper fourth-power example and the invariant intact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
