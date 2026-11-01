# Independent mathematical audit

## correctness

PASS

Under the existential k-distance definition, selected vertices must be pairwise Manhattan-separated by at most k=2 or3. Therefore their unique occupied bounding box has height and width at most k+1, hence <=4. Every shortest grid path is coordinate-monotone inside its endpoint bounding box; moving an anchored configuration to a larger rectangle does not change visibility. The given 16 h,w profiles for each k exhaust all nonempty anchored sets, verified with two independent shortest-route algorithms and a fresh independent Python enumeration of all 32 local box cases. Every ambient set has a UNIQUE translated anchored box, with exactly (m-h+1)_+ (n-w+1)_+ placements. Summing yields the complete cardinality polynomials for all m,n>=2; k2 degree<=4 and k3 degree<=6. The 3x3 coefficient vectors are k2 (1,9,26,24,1), k3 (1,9,34,64,29,4), and 4x4 k3 (1,16,90,212,140,32,4). No extrapolation from finite grid sizes is needed once the bounding-box lemma is proved.

## originality

PASS

The notion of visibility polynomial is prior and prior k=3 grid optimization/maximum-set count is not claimed new. The complete k=2 and k=3 *bounded-distance* cardinality distribution for every rectangular grid, including low-degree coefficients, is not stated or implied by the inspected unrestricted visibility polynomial studies or grid maxima. Exact exhaustive anchored enumeration has mathematically proved finite locality and hence supplies a natural missing full profile.

## value

PASS

The original k-distance mutual-visibility problem specifically motivates rectangular grids. The natural simplicial-complex size distribution for the two first nontrivial path-radius bounds is a complete classification for all side lengths, not an arbitrary finite grid slice. Lower-size counts and exact thresholds are independent of known maxima, and the clean 4x4 locality argument turns finite certificates into uniform global formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
