# Independent mathematical audit

## correctness

PASS

Checked the stated estimators and reconstructed RESULT.md:22–69. A useful residual p may appear at multiple positions; choosing one witnessed prefix length j suffices for the whole ball, since a path of length t from p can be prepended by this prefix and extended at its useful target. Assigning a shortest path to each noncentral state gives the layer bound even when residuals repeat across positions. For 0≤i≤D each neighboring available layer is nonempty, h0=1, and D≥1, so h_i≤U; with layers zero-padded past D the pair bound h_i+h_(i+1)≤U+1 still holds. One-step determinism gives q. Even radii give (U+1)/2 before taking ceilings; odd radii 2m+1 (m≥1) give [m(U+1)+U]/(2m+1), bounded by (2U+1)/3, including the U=1 boundary. Integer rounding gives strict inequality when U>max(q,3). For fixed q and cutoff R, balls of radius <R are uniformly bounded by the number of positive-length words up to R−1, and radius ≥R averages are at most (U+1)/2+(U−1)/(2R). The one-unit ceiling error vanishes after division; take the upper-tail supremum and then R→∞. In the binary family, distinct first-copy prefixes have disjoint possible second copies, hence distinct residuals. The k=2^d singleton residuals across the T+1 plateau levels are all distinct (including across levels by length); after entering the second copy the number of distinct suffixes is 2^(d−s). Thus U=2k−1 and the initial radius d+T contains at least k(T+1) states besides the center. Taking T=d² gives a ratio lower bound tending to 1/2 with U unbounded; the same languages work over any larger fixed alphabet. Independent suffix-set and BFS replay for (d,T)=(1,1),(2,4),(3,9),(4,16),(5,25) gave (U,B)=(3,2),(7,4),(15,8),(31,15),(63,29); each satisfies the asserted lower witness and upper cap. The uploaded checker and recorded output were evidence only, not executed; the finite replay does not prove the limits. The result is about the two estimators, not their ratio to the exact minimum bandwidth.

## originality

PASS

The primary paper gets credit for both estimators, their correctness as bounds, a depth-dependent comparison and an equality example at growing alphabet size. The distinct supported result is the quantitative fixed-alphabet separation for large U and the sharp asymptotic ratio 1/2, not a complete resolution of fixed-alphabet equality at bounded U.

## value

PASS

The result quantifies a limitation of using two inexpensive estimators in place of exact deterministic bandwidth: at large width and fixed alphabet, the lower estimate can reach at most asymptotically half of the upper estimate, and that factor cannot be improved uniformly. This answers the growing-width part of the motivating equality question and supplies a sharp binary family, rather than a small normalization discrepancy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
