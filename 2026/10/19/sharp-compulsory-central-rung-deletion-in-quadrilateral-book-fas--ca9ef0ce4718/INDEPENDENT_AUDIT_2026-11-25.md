# Independent mathematical audit

## correctness

PASS

Averaging by simultaneous page permutations and layer exchange preserves the centered-projector norm upper bound and feasibility, and yields exactly three off-diagonal weights. Resolving layer parity and page differences gives the two nonstationary page-difference eigenvalues 1−b and 1−b−2c (each multiplicity m−1), the even mean eigenvalue 1−(m+1)b, and the odd 2-by-2 block in RESULT.md. In the odd block the off-diagonal is √m b and the diagonal is (1−2a−mb,1−b−2c), so the lower bound is max(1−b,√m b). At m=2 its unique minimum has b=√2−1. Equality in the odd-block norm bound forces both diagonals to vanish, giving the claimed a and c and a feasible optimum. At m≥3 the degree constraint forces μ≥T=1−1/m. Taking b=1/m, a=0, c=T/2 attains it since 1/√m≤T. Any invariant optimum must have b=1/m and a=0. The remaining odd block has diagonal (0,T−2c) and its norm is at most T exactly when |T−2c|≤T−1/(mT), giving the stated feasible interval and also bounding the odd differences. The central edge entry is invariant under averaging even for a non-invariant P, and the nonnegative hub holds average to zero when m≥3, so both holds must vanish. Inspected RESULT.md lines 26–56, VERIFICATION.md and verify.py; the bundled finite symbolic/full-matrix and grid evidence was not rerun and is not needed for the general proof.

## originality

PASS

The FMMC convex program and orbit averaging are prior tools. The closest same-graph catalogue overlap reports the same qualitative deletion cutoff for a different objective, and discusses the FMMC cutoff as already known. No independent predecessor giving the exact unrestricted symmetric SLEM optimization, the invariant interval and the fixed entries of all minimizers was established in the inspected evidence.

## value

PASS

This exact optimization reveals that an allowed communication edge must be used at two pages and must be suppressed in every optimum from three pages onward. It quantifies non-factorization on a natural graph product and distinguishes the complete invariant optimizer interval from the conclusions valid without invariance. These are design constraints not supplied by a generic SDP formulation or the spectrum of a fixed product walk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
