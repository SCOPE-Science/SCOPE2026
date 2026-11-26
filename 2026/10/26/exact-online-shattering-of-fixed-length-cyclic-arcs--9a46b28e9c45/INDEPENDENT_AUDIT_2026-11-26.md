# Independent mathematical audit

## correctness

PASS

Complementation reduces to s≤n/2 without changing either dimension. Every root query has exactly s positive centers, so complete depth d requires 2^(d−1)≤s. On m≤s consecutive centers, query u+t−1 to split the first t from the rest: the two involved integer blocks fit in an interval of at most s+m≤n points, so cyclic reduction creates no extra positive centers. After the initial split both branches contain a block of 2^floor(log₂ s) centers, each bisected recursively; this also handles s=1 with depth-zero children. Adjacent points yield all four traces if s≥2, but a triple inside an s-arc cannot realize the two outer positives without its middle point, since the opposite circular path needs at least n−s+1 edges. For s=1 the singleton class shatters a point but not a pair. Taking s=floor(n/2) gives the claimed maximum with the stated attainment threshold. Independently validated every path of the supplied data-only n=128,k=64 witness: 128 leaves of depth seven, all distinct centers, each satisfying its entire path.

## originality

PASS

The complete parameter-dependent formula is distinct from the earlier literature and the same-date four-point census inspected. The audit found and credits an exact full duplicate of these finite dimensions in a later-dated Resultary record; that is genuine equivalent coverage in the current catalogue, but not evidence of prior coverage against this frozen October 26 finding. No claim of unique discovery or exhaustive priority is made.

## value

PASS

The exact width-dependent online dimension is a useful calibration for a natural translate class: despite VC dimension at most two, it ranges from one to the whole-class information bound. The theorem says exactly when that bound is attained and provides a constructive witness; its contribution is not just computing the largest certificate or exhibiting some VC/Littlestone separation already available from other classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
