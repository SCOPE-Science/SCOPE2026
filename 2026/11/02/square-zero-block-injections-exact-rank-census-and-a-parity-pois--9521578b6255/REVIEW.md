# Scientific review: square-zero block injections

## Correctness — PASS

The square-zero condition is equivalent to disjoint domain and image sets of whole blocks. The order constraint fixes their pairing, and each active block bijection has \(m!\) choices; this gives the stated exact formula. The iid ternary-label conditioning and lattice local central limit theorem prove the fixed-block Gaussian regime and sharp full-monoid probability. Ratios of successive parity-allowed vacancy masses, together with a summable uniform majorant, establish the factorial-critical Poisson law in total variation. All 17 direct map-enumeration tests and the independent asymptotic diagnostics pass. Finite checks are corroboration rather than infinite proofs.

## Originality — PASS relative to inspected primary literature

Caneco–Fernandes–Quinteiro, arXiv:1905.11489v1 (2019), defines the monoid and gives its total size, but the inspected source does not give the square-zero block-rank law and its factorial-critical double limit. Garba (1994) and Laradji–Umar (2015) treat nilpotents of ordinary unblocked order-preserving partial injections. The m=1 scalar central-trinomial count is known (OEIS A002426), and the full factorial-weighted scalar sum is expressible as a generalized trinomial coefficient; those algebraic identities are not claimed as new. Kachalla–Madu–Ngulde (2024) investigates nilpotent factorizations, not this distribution. The older Garba/Laradji–Umar full texts were unavailable here, so their complete implications could not be ruled out. Prior generalized-trinomial local-limit results may also cover a reformulation. Publication priority is not independently certified.

## Mathematical value — PASS

The number of block-internal bijections is \(m!\), creating a natural parameter controlling the square-zero rank distribution. The result determines this invariant for an infinite family and gives two concrete regimes: \(O(k)\) normally fluctuating vacant blocks at fixed block size versus a parity-conditioned Poisson number at the critical factorial scale \(m!symp k^2\). This behavior is not supplied by the monoid's total size. No general theory of all nilpotents or external significance is claimed.

## Verification and limitations

`verify.py` enumerates actual partial maps, checks exact distributions, and tests both critical parities and fixed-block variance scaling. The argument concerns square-zero elements, not every nilpotent; all infinitely indexed conclusions rest on the paper proof. Equivalence to a previously published stronger weighted-trinomial theorem remains a residual priority risk.

Self-review: passed. Independent audit: not yet performed.
