# Minimum field size \(11\) for \([6,3]\)-\(\mathrm{MDS}(3)\) codes
## Finding
The smallest finite-field order for which a \([6,3]\)-\(\mathrm{MDS}(3)\) code exists is \(11\). Equivalently, no such code exists over fields of orders \(2,3,4,5,7,8,9\), while over \(\mathbb F_{11}\) one example has generator-matrix columns
\[
(1,0,0),(0,1,0),(0,0,1),(1,1,1),(1,2,3),(1,7,4).
\]

This is the first length at which the order-three MDS condition is genuinely stronger than the ordinary MDS condition in dimension three: with fewer than six projective points there cannot be three joining lines from three disjoint pairs.

## Assumptions and scope
The term \(\mathrm{MDS}(3)\) is used in the higher-order MDS sense of Brakensiek, Gopi, and Makam. For a \([n,3]\) code, their geometric characterization says that the projective generator columns must satisfy two conditions: no three are collinear, and every three lines obtained by joining three disjoint pairs are nonconcurrent.

Only finite fields are considered. Thus every possible field order below \(11\) is one of \(2,3,4,5,7,8,9\).

## Proof
Let six projective generator columns satisfy the ordinary MDS condition. Any four of them are a projective frame. After choosing an ordering of four columns, a projective transformation sends that frame to
\[
(1,0,0),(0,1,0),(0,0,1),(1,1,1).
\]
Projective transformations preserve both collinearity and concurrence, so this normalization loses no configurations relevant to the \(\mathrm{MDS}(3)\) property.

For each field order \(q\in\{2,3,4,5,7,8,9\}\), enumerate every projective point of \(\mathrm{PG}(2,q)\), discard the fixed frame and every point collinear with a pair of frame points, and then test every unordered pair of remaining points. The resulting candidate counts are respectively
\[
0,0,2,6,20,30,42,
\]
so the numbers of normalized unordered pairs tested are
\[
0,0,1,15,190,435,861.
\]
For every one of these \(1502\) pairs, at least one required condition fails: either some triple is collinear or one of the \(15\) perfect matchings of the six points yields three concurrent joining lines. Therefore no \([6,3]\)-\(\mathrm{MDS}(3)\) code exists over a field of order below \(11\).

Over \(\mathbb F_{11}\), the six displayed points pass all \(20\) no-three-collinear determinants and all \(15\) nonconcurrence determinants. Hence they form the projective columns of a \([6,3]\)-\(\mathrm{MDS}(3)\) code. Combining existence at \(11\) with exhaustive exclusion of every smaller finite-field order proves the claim.

## Verification
The standalone `verify.py` performs exact finite-field arithmetic. It constructs \(\mathbb F_4\) as \(\mathbb F_2[x]/(x^2+x+1)\), \(\mathbb F_8\) as \(\mathbb F_2[x]/(x^3+x+1)\), and \(\mathbb F_9\) as \(\mathbb F_3[u]/(u^2+1)\), and it exhaustively checks the field axioms used by the calculation.

For each relevant field it constructs all \(q^2+q+1\) projective points, applies the frame normalization, and tests every normalized pair against all \(20\) triples and all \(15\) perfect matchings. It confirms zero good normalized pairs below \(11\). Over \(\mathbb F_{11}\) it finds \(72\) good normalized pairs, including the displayed witness.

The exhaustive search is finite and symmetry-complete because every ordinary-MDS six-point configuration contains an ordered projective frame, and every ordered projective frame is projectively equivalent to the fixed frame used by the verifier.

## Relationship to prior work
Brakensiek, Gopi, and Makam give the exact projective-plane characterization used here and identify explicit small-field constructions of \((n,3)\)-\(\mathrm{MDS}(3)\) codes as an open direction. Their first public version appeared on 2022-06-10.

Brakensiek, Dhar, and Gopi subsequently describe \([n,3]\)-\(\mathrm{MDS}(3)\) as the smallest nontrivial higher-order MDS case. They prove the general lower bound
\[
|\mathbb F|\ge \binom{n-2}{k-1}-1,
\]
which yields only \(|\mathbb F|\ge5\) at \((n,k)=(6,3)\), and give an explicit asymptotic construction over fields of size \(O(n^3)\). The inspected full text does not state the exact six-column threshold \(11\).

Searches using the native \([6,3]\)-\(\mathrm{MDS}(3)\) notation, minimum-field-size language, six-point arc language, and nonconcurrent-disjoint-secants formulation found no prior statement implying the exact threshold. This search evidence does not rule out an unindexed equivalent formulation in older finite-geometry literature.

## Limitations
The reduction from higher-order MDS to the projective collinearity-and-concurrence criterion is taken from the cited primary source rather than reproved from the subspace-intersection definition. The package independently verifies every finite-field computation after that reduction.

The originality conclusion is necessarily literature-relative. In particular, an older finite-geometry source could encode the same six-point configuration under terminology not captured by the checked aliases.

## References
1. J. Brakensiek, S. Gopi, and V. Makam, “Generic Reed-Solomon Codes Achieve List-decoding Capacity,” arXiv:2206.05256, first public version 2022-06-10; later SIAM Journal on Computing, DOI 10.1137/23M1598064.
2. J. Brakensiek, M. Dhar, and S. Gopi, “Improved Field Size Bounds for Higher Order MDS Codes,” arXiv:2212.11262, first public version 2022-12-21.
