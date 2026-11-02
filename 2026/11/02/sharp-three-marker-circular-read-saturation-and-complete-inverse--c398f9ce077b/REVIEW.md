# Self-review

**Claim examined.** For complete cyclic binary length-\(k\) factor multispectra at Hamming weight three and \(n\ge3k-1\), the number of distinct profiles is \(k+(k-1)^2-\lfloor(k-1)^2/4\rfloor-\mathbf1_{\{n=3k-1\}}\); four explicitly described families give every inverse-fiber size.

## Correctness — PASS

The source domain, read orientation, factor multiplicity, and indexed-versus-necklace convention are defined in RESULT.md. Exact factor counts are invertible from all subset-incidence correlations. The inequality \(n>3(k-1)\) forces a gap of length at least \(k\); nonzero three-position correlations expose the ordered short-gap pair when it sums to less than \(k\), while otherwise pair correlations expose the unordered short gaps. No fifth case is possible. Each fiber size follows from placements and weak-composition counts; the periodic all-long case is handled by a three-marker double count. The independent literal-window verifier passed on 53,325 indexed source words in 36 cases, and the exact symbolic fiber sums passed for 492 other parameter choices. The proof, not finite enumeration, establishes the all-length statement.

## Originality — PASS, with residual priority risk

The original preprints by Gabrys–Milenkovic (arXiv:1804.04548) and Marcovich–Yaakobi (arXiv:1912.11108) establish and develop read-multiset reconstruction, including coded and noisy settings, without supplying this exact fixed-weight circular family. Kiah–Puleo–Milenkovic (arXiv:1502.00517) gives a profile-flow framework but does not state the variable-read-length exact count with all sparse inverse fibers. Already known fixed-read-length-three profile counts and three-marker global-injectivity thresholds are strict projections, not a statement of this theorem. OEIS A022338 coincides numerically for an initial prefix but records a different object and later diverges. A stronger unindexed general cyclic-profile enumeration remains a possible source of implicit coverage; absence from search alone is not relied on as novelty evidence.

## Mathematical value — PASS

The exact capacity is a natural invariant of a fully specified sequence-assembly channel. The sharp permanent length boundary and explicit positive fiber sizes quantify information loss and orientation ambiguity over a two-parameter infinite family, improving substantially on an isolated count or a routine special case.

## Limits

Only noiseless complete ordered cyclic observations, binary weight three, and \(n\ge3k-1\) are proved. Earlier lengths, other weights, missing reads and reverse-complement-invariant reads are not settled. Computational checks are finite. The scientific conclusions await external independent audit.

Self-review: passed. Independent audit: not yet performed.
