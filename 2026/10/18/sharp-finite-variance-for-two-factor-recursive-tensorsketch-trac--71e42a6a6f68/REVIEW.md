# Independent mathematical audit

## correctness

PASS

On expanding the squared norm, diagonal terms sum to one, and every nontrivial effective sign character has mean zero after conditioning on the hashes and internal signs. Independence up to four coordinates per leaf is sufficient to ensure orthogonality of the single-factor and two-factor pair characters. A composed hash difference is zero with probability q and takes each nonzero value with probability s. For the two-factor pair character, the two orientations have independent-factor collision probability q²+(m−1)s² each, and their intersection has probability q²+(g−1)s² because 2Δ=0 mod m; thus the expected squared sum of their indicators is 2U, not just twice the single collision probability. Summing the paired squares gives 2q(a+b)+2Uab (including m=1). Positive coefficients and Cauchy–Schwarz force both factors to have constant coordinate magnitude at equality. The limits mq→2 and mU→1 give the stated sequential limiting constant, not a uniform cap of 10. Independent exact replay: python -B /workspace/review_replay.py 2 enumerates all composed hash images and effective relative signs, with exact rational factors at d=2 and widths 1–5, and directly reconstructs each four-entry tensor sketch and its moments. The proof, not this finite example, covers arbitrary fixed unit factors and widths.

## originality

PASS

Best-of-knowledge pass for the exact law and sharp benchmark of this real three-layer separable rank-one estimator. The sketch, moment method and nonrecursive collisions are not claimed as contributions. The inspected prior bounds and alternative probes do not provide the displayed variance.

## value

PASS

The variance is a directly relevant accuracy measure for a published estimator. This is a natural low-rank input class rather than an arbitrary parameter slice. The parity-sensitive exact law and attaining inputs give researchers a finite-width benchmark for cost of recursion and for assessing general upper bounds; a coarse bound or a nonrecursive benchmark would not serve that purpose.

The dated certificate retains the supplied scientific assessment, sources and limitations.
