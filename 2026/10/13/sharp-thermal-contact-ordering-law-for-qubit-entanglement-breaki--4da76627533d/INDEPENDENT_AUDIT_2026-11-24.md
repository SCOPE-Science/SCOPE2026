# Independent mathematical audit

## correctness

PASS

Composing the affine population maps gives slope R and offset s_pi; the offset weights telescope to Gamma, whence 0<=s_pi<=Gamma/2. Coherences acquire the factor sqrt(R). The normalized partial transpose has nonnegative scalar blocks and one block (1/2)*[[s,sqrt(R)],[sqrt(R),Gamma-s]]. Its trace is Gamma/2 and its determinant is (s(Gamma-s)-R)/4. The negative part of its smaller eigenvalue is the stated negativity; the qubit Choi PPT criterion gives exactly the stated entanglement-breaking test. A swap from (b,a) to (a,b) shifts the final offset by D*gamma_a*gamma_b*(nu_b-nu_a), with D the strictly positive suffix slope. Sorting yields both extrema because s(Gamma-s) increases and the negativity decreases weakly on the allowed half interval. If Gamma^2<4R the test fails everywhere; otherwise the lower root is the inclusive threshold, including the double-root case, and checking the sorted extremal offsets gives all three regimes. For two contacts the offsets are g/2 and g(1-g)/2; the determinant yields the two stated cubics (cancelling 1-g in the second). The derivative signs and opposite endpoint signs give unique roots, and the larger cold-first offset gives the strictly earlier transition. The second root is below 3/4; the hot single channel cannot break there since g^2/4<1-g, and the cold one cannot break for g<1. At g=2/3 the hot-first block has the eigenvalue (4-3 sqrt(2))/18; the cold-first block is positive. The two strict signs in the interior persist by continuity within the allowed parameter domain.

## originality

PASS

The supported distinct result is the sharp control-free opposite-status window for physical cold and infinite-temperature contacts, neither individually entanglement breaking, with stability away from the endpoints. Do not count the affine sorting rule, local commutator, single-channel Choi test, or the resulting sorted phase test as independent innovations; the latter follows by combining known affine ordering and the single-channel Choi region. The strongest checked order-sensitive quantum example requires an interposed unitary and does not imply the thermal window. No verified earlier classification of that window or control-free witness under these hypotheses was found. This distinguishes new content from known coverage, not historical priority.

## value

PASS

The sharp reversal is a motivated boundary, not merely a new name for affine sorting. For physically distinguished zero and infinite bath temperatures at equal strength, it quantifies exactly when temporal order alone determines survival of reference entanglement, without either contact already being entanglement breaking. The open strict-inequality regime distinguishes a stable effect from an isolated test point. The general phase test provides a usable prediction for a prescribed multiset even though its ingredients are established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
