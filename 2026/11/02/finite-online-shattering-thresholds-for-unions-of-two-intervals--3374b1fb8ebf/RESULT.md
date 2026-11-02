# Finite online-shattering thresholds for unions of two intervals

## Finding
Fix an ordered set \([n]=\{1,\ldots,n\}\). Let \(\mathcal U_{n,2}\) contain the empty set and all subsets expressible as a union of at most two nonempty consecutive intervals. Every query specifies a point \(i\in[n]\) and returns whether \(i\) belongs to the unknown set.

For every integer \(1\le n\le14\), the exact Littlestone dimensions, in increasing order, are
\[
(1,2,3,4,4,5,5,6,6,7,7,8,8,9).
\]
Their VC dimensions are \(\min\{n,4\}\). The first strict adaptive-versus-static separation is at \(n=6\), where \(\operatorname{VCdim}=4\) and \(\operatorname{Ldim}=5\). The cardinality bound \(\operatorname{Ldim}\le\lfloor\log_2|\mathcal U_{n,2}|\rfloor\) is attained for every \(n\le6\), but first fails at \(n=7\):
\[
|\mathcal U_{7,2}|=99,\qquad \operatorname{Ldim}(\mathcal U_{7,2})=5<6=\lfloor\log_2 99\rfloor.
\]
At the largest certified size, \(|\mathcal U_{14,2}|=1471\) and \(\operatorname{Ldim}=9\), whereas the cardinality ceiling is \(10\). No numerical formula beyond \(n=14\) is asserted.

## Assumptions and scope
The domain consists of \(n\) distinctly ordered points and there are no geometric endpoint choices between points; different unions giving the same subset count once. The empty concept is included, and singleton intervals are allowed. A binary tree of depth \(d\) is shattered when every one of its \(2^d\) answer strings has a single consistent concept witness. The Littlestone dimension is the maximal such depth; the VC dimension is the maximal cardinality of a fixed shattered query support.

A binary subset has at most two runs of ones exactly when it belongs to \(\mathcal U_{n,2}\). Choosing the \(2j\) transitions of a word with \(j\) positive runs among the \(n+1\) boundary gaps gives
\[
|\mathcal U_{n,2}|=\sum_{j=0}^{2}\binom{n+1}{2j},
\]
where impossible binomial coefficients are zero.

## Proof
For VC dimension, any four ordered points admit every binary labeling by at most two positive runs, with all nonqueried points labeled zero. Thus \(\operatorname{VCdim}\ge4\) when \(n\ge4\); for \(n<4\), all binary words are permitted. Conversely, a five-point support cannot realize alternating answers \((1,0,1,0,1)\), which require three disjoint positive runs. This proves \(\operatorname{VCdim}=\min\{n,4\}\) for all \(n\ge1\).

For the adaptive dimension, write \(H_n\) for the explicitly enumerated set of all admissible masks. For a subset \(S\subseteq H_n\), a query \(i\in[n]\), and a bit \(b\in\{0,1\}\), put \(S_{i,b}=\{h\in S:h(i)=b\}\). Define a Boolean predicate \(P(S,d)\) by
\[
P(S,0)\iff S\ne\emptyset,
\]
\[
P(S,d)\iff\bigvee_{i=1}^{n}\Big(P(S_{i,0},d-1)\wedge P(S_{i,1},d-1)\Big),\qquad d\ge1.
\]
This is an exact theorem, not a heuristic: a shattered depth-\(d\) tree has some root query, and its two restricted subtrees have depth \(d-1\); conversely, a root query with two shattered restricted trees combines to give a shattered depth-\(d\) tree. Induction proves equivalence for every finite \(S\) and every \(d\). The pruning rule \(|S|<2^d\Rightarrow\neg P(S,d)\) is valid because the tree's leaves require distinct complete hypothesis witnesses.

The supplied dependency-free checker enumerates every binary mask, retains exactly the masks with at most two one-runs, computes every query fiber by exact integer bit operations, and recursively applies this predicate with memoization. For each \(1\le n\le14\), it establishes \(P(H_n,d_n)\) and \(\neg P(H_n,d_n+1)\), where \((d_1,\ldots,d_{14})\) is the displayed sequence. These two Boolean evaluations prove both directions of each equality. At \(n=14\), the exact decision procedure evaluates 179260 distinct memoized predicate states; at \(n=7\), it evaluates 802.

In addition to the recurrence, explicit full trees are included at \(n=7\) and \(n=14\). They contain respectively 31 and 511 internal point queries and 32 and 512 distinct complete-path witnesses. Each witness is an admissible two-run mask whose queried bits reproduce its entire root-to-leaf answer string. Their independent replay establishes the constructive half of the two principal cases. The full recursive search, rather than extrapolation from those trees, establishes their upper bounds.

## Verification
Run `python3 check_two_runs.py --full --certificate depth5_tree.json` and `python3 check_two_runs.py --full --certificate depth9_tree.json`; both commands check every size through fourteen, then replay the indicated depth certificate. Run `python3 crosscheck_two_runs.py` for a distinct string-set, non-bitmask implementation of the exact dimension recurrence through eight points. All arithmetic and enumerations use Python integers, with no external library or solver and no time-limit conclusions.

The first-query obstruction at seven points can also be checked pointwise: for possible root queries in increasing order, the truth values of \(P(S_{i,1},5),P(S_{i,0},5)\) are respectively \((0,1),(1,0),(0,1),(1,0),(0,1),(1,0),(0,1)\). Thus no query has two depth-five children, proving the absence of depth six. In the same way no point query at fourteen has two children satisfying depth nine.

## Relationship to prior work
Alon, Beimel, Moran, and Stemmer's 2020 study of online-prediction closure properties treats arbitrary Boolean aggregation of hypothesis classes; its bounds are not an exact finite-chain classification. Ghazi, Golowich, Kumar, and Manurangsi (2020/2021) sharpen these general composition bounds but likewise do not tabulate finite two-interval classes. Chase, Freitag, and Reyzin (2023) discuss Littlestone dimension and an example of a class of pairwise disjoint intervals, which is a different concept family with dimension one. The elementary VC bound four for two unions is standard and is not claimed as new. The new content is the certified finite adaptive threshold sequence and first cardinality-bound shortfall for the exact discrete model.

## Limitations
The conclusion is confined to \(1\le n\le14\), with the empty concept included. It makes no prediction for larger sizes, for half-open real intervals, or for a different query alphabet. The exact recurrence has exponential state complexity and is not a closed-form unrestricted dimension theorem. Priority is assessed against accessible literature and research records; differently named online segmentation or bounded-run results could imply some entries, and independent historical verification remains necessary. The program checks finite mathematical claims, not broader asymptotic conjectures.

## References
1. N. Alon, A. Beimel, S. Moran, U. Stemmer, *Closure Properties for Private Classification and Online Prediction*, arXiv:2003.04509, first public 2020-03-10; Proceedings of COLT 2020. https://arxiv.org/abs/2003.04509
2. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668, first public 2020-07-07; ALT 2021. https://arxiv.org/abs/2007.03668
3. H. Chase, J. Freitag, L. Reyzin, *Applications of Littlestone Dimension to Query Learning and to Compression*, arXiv:2310.04812v1, 2023-10-07. https://arxiv.org/html/2310.04812v1
