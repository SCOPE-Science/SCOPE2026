# Independent mathematical audit

## correctness

PASS

For \(\rho=0\), setting \(a=r+1\) and \(b=g-D+r\) gives \(ab=g\) and the classical Castelnuovo count \(N_g(a,b)=g!\prod_{i=0}^{a-1} i!/(b+i)!\). Its denominator is the hook product of the \(a\times b\) rectangle. The package's cumulative hook-count formula is correct in each threshold range. For \(1\le a<c\le e<b\) with \(ab=ce\), the more balanced rectangle has at least as many hooks below every threshold and strictly more at some threshold, so after sorting its hooks coordinatewise they are no larger and at least one is smaller. Hence its hook product is strictly smaller and its tableau/Castelnuovo count is strictly larger. Iterating over divisor pairs proves the closest-divisor maximizer, while transposition gives exactly the Serre-dual tie. The finite genus-300 checker is corroborative only and is not needed for the quantified proof.

## originality

PASS

The classical and modern Brill–Noether sources inspected this round give the pointwise zero-dimensional count for a fixed numerical type, not a fixed-genus ordering across all divisor rectangles. Resultary returned the assigned record as the only exact fixed-genus balancing hit, and targeted searches under rectangular standard-tableau, hook-product, fixed-area, balance, and closest-divisor formulations did not locate an earlier theorem. The balancing lemma is not mechanically implied by merely knowing the hook-length formula: it supplies a new strict comparison across distinct factor shapes. Best-of-knowledge originality therefore passes, with an explicit risk that an equivalent rectangle-monotonicity theorem may exist under older algebraic-combinatorics terminology.

## value

PASS

The result gives a complete fixed-genus extremal classification for a classical zero-dimensional enumerative invariant and identifies the only tie as Serre duality. It compares a natural family of all \(\rho=0\) linear-series problems rather than an arbitrary slice, and the cross-shape balancing lemma is independently meaningful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
