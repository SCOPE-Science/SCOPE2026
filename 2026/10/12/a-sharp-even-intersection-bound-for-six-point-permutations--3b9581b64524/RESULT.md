# A sharp even-intersection bound for six-point permutations

## Finding
Let \(S_6\) be the permutations of \(\{1,2,3,4,5,6\}\). Call a family \(\mathcal F\subseteq S_6\) *even-intersecting* when every two distinct members have an even number of equal images (agreements). Define \(M(6)\) as the maximum possible cardinality. Then

\[
\boxed{M(6)=48.}
\]

A lower-bound example is the subgroup preserving a partition into three unordered pairs. A two-class weighted character-theoretic upper bound establishes optimality, without exhaustive maximum-clique search.

## Assumptions and scope
Permutations are bijections of six labeled positions. Agreement means \(\left|\{i:\sigma(i)=\tau(i)\}\right|\) for two permutations \(\sigma,\tau\). The requirement concerns distinct members only; the six self-agreements of a permutation are automatically even. All groups and vector spaces in the proof are finite, and adjacency matrices act on real-valued functions on \(S_6\). The claim concerns degree six alone, not all even degrees or the classification of all optimizers.

## Proof
**Lower bound.** Fix the partition \(\{\{1,2\},\{3,4\},\{5,6\}\}\). The subgroup \(H\) permuting the three blocks and independently swapping the elements inside them is the wreath product \(S_2\wr S_3\) and has cardinality \(2^3 3!=48\). Each \(h\in H\) has an even number of fixed positions: a moved block contributes none, while each block fixed as a set contributes either zero or two. For any \(\sigma,\tau\in H\), the number of agreements is the number of fixed positions of \(\tau^{-1}\sigma\in H\), hence is even. Thus \(M(6)\ge48\).

**A nonnegative forbidden-difference matrix.** Write \(A_{\mu}\) for the adjacency matrix on \(S_6\) with \((A_{\mu})_{\sigma,\tau}=1\) precisely when \(\sigma^{-1}\tau\) has cycle type \(\mu\); in particular its diagonal is zero for the types used below. Both types \((5,1)\) and \((3,2,1)\) have exactly one fixed point, and each cycle type is invariant under inversion. Consequently

\[
W=3A_{(5,1)}+2A_{(3,2,1)}
\]

is real symmetric, has nonnegative entries, and vanishes on every ordered pair of members of any even-intersecting family (including diagonal entries). The two conjugacy classes have sizes \(144\) and \(120\) respectively, so every row of \(W\) sums to \(d=3\cdot144+2\cdot120=672\).

**Exact spectrum.** The class sums are central in the group algebra. If \(\lambda\vdash6\) indexes an irreducible character \(\chi^\lambda\) of degree \(f^\lambda=\chi^\lambda(1^6)\), Schur's lemma yields the eigenvalue

\[
\theta_\lambda=\frac{432\chi^\lambda(5,1)+240\chi^\lambda(3,2,1)}{f^\lambda}
\]

with multiplicity \((f^\lambda)^2\) in the regular representation. The complete evaluation is:

| \(\lambda\) | \(f^\lambda\) | \(\chi^\lambda(5,1)\) | \(\chi^\lambda(3,2,1)\) | \(\theta_\lambda\) |
|:--|--:|--:|--:|--:|
| \((6)\) | 1 | 1 | 1 | 672 |
| \((5,1)\) | 5 | 0 | 0 | 0 |
| \((4,2)\) | 9 | -1 | 0 | -48 |
| \((4,1,1)\) | 10 | 0 | -1 | -24 |
| \((3,3)\) | 5 | 0 | 1 | 48 |
| \((3,2,1)\) | 16 | 1 | 0 | 27 |
| \((3,1,1,1)\) | 10 | 0 | 1 | 24 |
| \((2,2,2)\) | 5 | 0 | -1 | -48 |
| \((2,2,1,1)\) | 9 | -1 | 0 | -48 |
| \((2,1,1,1,1)\) | 5 | 0 | 0 | 0 |
| \((1,1,1,1,1,1)\) | 1 | 1 | -1 | 192 |

The character values follow from the Murnaghan–Nakayama rim-hook rule or independently from the Jacobi–Trudi identity and the power-sum expansion of the complete symmetric functions; both exact procedures are provided in `verify.py`. There are eleven partitions, and \(\sum_{\lambda\vdash6}(f^\lambda)^2=720\), so this accounts for every eigenvalue. The least eigenvalue is exactly \(-48\).

**Sharp ratio bound.** For an even-intersecting family of size \(a\), let \(x\in\{0,1\}^{720}\) be its indicator. Since every member pair has forbidden weight zero, \(x^\mathsf TWx=0\). Decompose \(x=(a/720)\mathbf1+y\) with \(y\perp\mathbf1\). Regularity and the least-eigenvalue bound give

\[
0=x^\mathsf TWx\ge\frac{672a^2}{720}-48\left(a-\frac{a^2}{720}\right)=a(a-48).
\]

Thus \(a\le48\). The lower-bound subgroup gives equality, proving \(M(6)=48\).

## Verification
Run `python3 verify.py` with a Python 3 standard-library interpreter. The script enumerates all \(720\) permutations to confirm both conjugacy-class sizes, derives the eleven character rows twice (rim hooks and an independent power-sum Jacobi–Trudi determinant), checks \(\sum_\lambda(f^\lambda)^2=720\), computes the weighted eigenvalues and ratio, builds the \(48\)-element subgroup, and directly checks even agreement for every ordered pair of its members. The recorded output ends in `VERIFY_OK`. The proof above establishes the infinite search-free upper bound on all \(720\)-vertex candidate families; the computation checks its finite character table and example explicitly rather than assuming a failed search proves optimality.

## Relationship to prior work
Banerjee, Dewan and Mishra introduce the same even-agreement extremal quantity and prove asymptotic bounds for even degrees, including the wreath-product lower construction. Their bounds do not assert sharpness at degree six; the present weighted class-sum certificate supplies the missing upper bound there. Cameron, Deza and Frankl study permutation families with prescribed Hamming distances, the general framework from which this question arose. A separately reported sharp finite result for \(S_5\) concerns odd degree and does not imply the degree-six bound. The even-*cycle*-intersecting condition studied by Lindzey is different: it requires a shared even-cycle property rather than an even number of equal images.

## Limitations
Only \(M(6)\) is determined. Neither uniqueness of extremal families nor sharpness of the wreath-product construction for \(S_8\) or larger even degrees is claimed. The weighted matrix ignores some other odd-agreement differences, which is harmless for a valid upper bound. The full 1988 Cameron–Deza–Frankl source could not be materially compared beyond its available metadata and abstract; an unindexed or unexamined equivalent small-degree result remains a literature risk. No independent external audit has been performed.

## References
- A. Banerjee, A. Dewan, R. Mishra, *Even-Intersecting Families of Permutations*, arXiv:2609.21645v1 (first public version September 18, 2026), https://arxiv.org/abs/2609.21645 .
- P. J. Cameron, M. Deza, P. Frankl, *Intersection theorems in permutation groups*, Combinatorica 8 (1988), 249–260, https://doi.org/10.1007/BF02126798 .
- N. Lindzey, *An Eventown Result for Permutations*, arXiv:2601.12613 (2026), https://arxiv.org/abs/2601.12613 .
