# Independent mathematical audit

## correctness

PASS

For Z zeros, K ones, and surplus s=Z-(n-1), a marker at zero-rank a covers exactly [a-s,a] clipped to [0,n-1]. Covering all offsets requires K(s+1)≥n, and the host restriction gives Z≤2(K+1). For n≥4, s=0 is strictly too expensive; s=1 gives the asserted lower bound; s≥2 can attain it only at s=2 for odd n. At even length, the s=1 intervals must tile the target offsets in pairs. At odd length the s=2 word saturates all zero runs; at s=1 the first and last ranks must lie in {0,1} and {2m,2m+1}, respectively, and each gap is at most two. The feasible endpoint differences 2m and 2m-1 give precisely two end variants and the m single-short-gap variants. Each listed word meets the host constraint, covers the target offsets, has the required length, and in fact avoids 11. The boundary n=4 is included.

## originality

PASS

This pass is for the output-constrained minimum and full equality classification. The strongest indexed comparison already solves the same target family without the output constraint. That is material overlap in the target family and rank method, but the unrestricted optimization is not the same, and its optimum can be strictly smaller (for example, 22 versus 24 at n=16). No equivalent constrained classification or stronger implication was found in the inspected passages.

## value

PASS

A forbidden host factor changes the optimum for the natural all-offset, one-marker test family. The exact equality classification explains the parity effect and distinguishes the saturated zero runs from the near-tiling cases, supplying an explicit benchmark for constrained supersequence theory rather than a small-instance census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
