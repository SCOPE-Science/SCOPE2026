# Independent mathematical audit

## correctness

PASS

For all labeled total orders, a depth-d complete comparison tree has 2^d distinct consistent leaves, giving floor(log2 n!) bound. Independently constructed exact permutation-incidence bitsets and evaluated the full OR-over-comparisons/AND-over-answer-branches dynamic recurrence for n=1 through n=7. Recovered Littlestone dimensions (0,1,2,4,6,9,11), with 77,927 exact cached seven-item state/depth evaluations; thus depth twelve is impossible, depth eleven attainable. The source supplies an additional 2048-leaf complete witness and a distinct transitive-poset linear-extension DP. VC dimension n-1 follows because arbitrary orientations of a forest extend to linear orders while a cyclic orientation does not. Grafting independent six-item shattered blocks yields Ldim(6s)>=9s and gap>=3s+1 for every s>=1.

## originality

PASS

Known VC dimension of permutation comparisons follows from forest supports and is expressly background. Alon–Moran–Moran 2026 studies sorting when the learner proposes a *whole permutation* and receives a counterexample, not a single adaptively chosen pairwise query. Agarwal et al. analyze limited-round top-k ranking with different resources; Littlestone closure bounds are not exact classifications. Resultary semantic lookup found no same seven-element decision-tree table. Earlier balanced comparison/poset literature could contain an equivalent finite classification, hence qualified originality.

## value

PASS

The first entropy-bound failure at seven alternatives is a natural exact extremal threshold of adaptive comparison learning. Its exhaustive finite obstruction is a complete classification, while the block construction yields an unbounded adaptive-versus-static shattering separation in a canonical concept class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
