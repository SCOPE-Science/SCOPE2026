# Independent mathematical audit

## correctness

PASS

For image sets E,F, the ordered product has image e(F∩dom e). Shared roots contribute h deterministically, and the s−h marked nonroots must hit exactly t−h additional roots. Counting assignments by inclusion–exclusion gives the first formula; alternatively restrict selected elements to those mapped to a chosen set of allowed roots or left undefined, then extract the coefficient of selected-set size by inclusion–exclusion. Both count the choices outside F and the (s+1)^(n−s) idempotents with image F. Partial identities realize each admissible intersection, including zero and n=0. At fixed ranks the root sets are independent uniform subsets, so the hypergeometric variance is O(n) and H/n→ab. Conditional on H the remaining independent choices change occupancy by at most one apiece, giving uniform concentration (m=0 is deterministic). The unattained-root probability is (1−1/(r+1))^(s−H), which yields the stated limit and the two unequal values. Direct composition tested 299,755 ordered pairs through n=5, including the swapped histograms (0,800,5950)/(0,1080,5670). An independent occupancy recursion and polynomial multiplication matched for 5,440 admissible-range triples through n=14. Replay: python3 /workspace/branches/replay_3_4_5.py 5. These tests corroborate the finite identities, not the limiting proof.

## originality

PASS

The fixed-image-root representation, product-image identity and occupancy tools are known. The assessed claim is the unrestricted ordered three-rank law in the full partial transformation semigroup together with its explicit macroscopic order asymmetry. The strongest earlier comparisons either count one map, restrict the product or the pair, or use a different semigroup. No compared source supplies both the unrestricted (partial or common-sink equivalent) spectrum and the prescribed-density limit, nor was an earlier coverage of either contribution established.

## value

PASS

Product-image rank is a natural invariant of the semigroup and the all-rank census identifies both the complete feasible range and an exact computable law beyond one-factor enumeration. The same statistic shows a macroscopic order effect for independent fixed-rank factors: swapping densities changes the positive limiting fraction, so orientation is not just a rare finite-size pathology. These are useful finite and asymptotic facts about arbitrary partial idempotents; no novelty is assigned to inclusion–exclusion itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
