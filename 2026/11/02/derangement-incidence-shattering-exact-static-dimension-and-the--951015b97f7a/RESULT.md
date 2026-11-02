# Derangement incidence shattering: exact static dimension and the first adaptive gap

## Finding
Let \(n\ge2\). Let \(\mathcal D_n\) consist of all fixed-point-free permutations \(\pi\) of \([n]=\{0,\ldots,n-1\}\), viewed as Boolean concepts on the query domain \(Q_n=\{(i,j):i,j\in[n],\ i\ne j\}\), with \(c_\pi(i,j)=1\) precisely when \(\pi(i)=j\). Then
\[
\operatorname{VCdim}(\mathcal D_n)=n-2\quad(n\ge2).
\]
The first strict adaptive-versus-static shattering gap within this family occurs at \(n=5\). More precisely, the respective pairs \((\operatorname{VCdim},\operatorname{Ldim})\) for \(n=2,3,4,5\) are
\[
(0,0),\ (1,1),\ (2,2),\ (3,4).
\]
At five elements a complete binary query tree of depth four is explicitly certified. Its sixteen leaves are realized by sixteen distinct fixed-point-free permutations. There is no depth-five shattered query tree.

Equivalently, these concepts are the edge-incidence vectors of perfect matchings of the crown graph obtained from the complete bipartite graph on two sets of \(n\) vertices by deleting one prescribed perfect matching.

## Assumptions and scope
All sets are finite, all queries are individual allowed ordered pairs, and every concept is a full derangement; queries are not comparisons between elements or yes/no questions about entire matchings. A support \(S\subseteq Q_n\) is VC-shattered when every Boolean labeling of \(S\) is realized by some \(c_\pi\). The Littlestone dimension is the maximum depth of a complete binary tree whose internal nodes are labeled by adaptively selected queries and for which each root-to-leaf labeling is realized by a member of \(\mathcal D_n\). The empty or singleton query domain with one nonempty concept has both dimensions zero.

## Proof
**Upper bound for the VC dimension.** Suppose a support \(S\) with \(n-1\) queries is shattered. The all-positive labeling forces \(S\) to be a partial permutation: its queried edges have pairwise distinct row and column coordinates. Let \(u\) be the unused row and \(v\) the unused column. The all-positive labeling must complete with the edge \((u,v)\), so \(u\ne v\). Because \(v\ne u\), there is an edge \((v,w)\in S\). Now prescribe the labeling that makes all edges of \(S\) positive except \((v,w)\), which must be negative. The last two unassigned rows are \(u,v\) and the last two columns are \(v,w\). The only completion avoiding \((v,w)\) uses the forbidden diagonal edge \((v,v)\), a contradiction. Thus no \((n-1)\)-support is shattered. By heredity of shattering, no larger support is shattered. For \(n=2\), the unique derangement gives the same upper bound zero.

**Lower bound for the VC dimension.** For every \(n\ge3\) take
\[
S_n=\{(i,i+1):0\le i\le n-3\},
\]
where entries are elements of \([n]\), so \(|S_n|=n-2\). Given any positive subset \(A\subseteq S_n\), enforce the edges in \(A\) and forbid the other edges of \(S_n\). Remove the rows and columns used by \(A\), leaving \(m=n-|A|\ge2\) on each side. The forbidden edges in the residual bipartite graph are subsets of the identity matching together with the cyclic-shift matching \(i\mapsto i+1\pmod n\). Their union is one cycle of length \(2n\). In particular, every residual vertex has at most two forbidden neighbors, and the forbidden bipartite graph has no four-cycle when \(n\ge3\).

If \(m\ge4\), every residual vertex has at least \(m-2\ge m/2\) *allowed* neighbors. Hall's condition follows: for a row subset of at most half the rows its neighbor set has size at least \(m/2\); for a larger row subset, a missing column neighbor would have degree smaller than \(m/2\), impossible. If \(m=3\), every row has an allowed neighbor; two rows cannot have only one allowed neighbor between them, since the two other columns would form a forbidden four-cycle with these rows; all three rows see all three columns since each column has at most two forbidden neighbors. Thus Hall's condition again holds. Finally, \(m=2\) happens only when \(A=S_n\); the remaining rows are \(n-2,n-1\), the remaining columns are \(n-1,0\), and the two allowed edges \((n-2,n-1)\), \((n-1,0)\) complete the cyclic permutation. Therefore every labeling of \(S_n\) extends to a derangement. This proves the VC formula, including \(n=2\).

**Adaptive bounds for orders at most five.** Write \(D_n=|\mathcal D_n|\). Directly enumerating the permutations gives \(D_2=1\), \(D_3=2\), \(D_4=9\), and \(D_5=44\). Each allowed query has the same number of positive concepts, namely \(D_n/(n-1)\), by relabeling symmetry and double-counting the \(n\) selected edges in every permutation. The positive branch of the root of a complete depth-\(d\) tree must contain at least \(2^{d-1}\) distinct concepts. For \(n=4\) every positive branch has three concepts, ruling out depth three; the VC lower bound gives adaptive depth two. For \(n=5\), every positive branch has eleven concepts, ruling out depth five. The accompanying tree is a complete depth-four tree, verified at every leaf against a distinct derangement. Thus \(\operatorname{Ldim}(\mathcal D_5)=4\). The cases \(n=2,3\) follow from cardinality and the VC lower bounds. The first strict gap is consequently at five.

## Verification
The standalone `verify_derangement_learning.py` tests all query supports for the VC dimensions at orders two through five; separately checks all \(2^{n-2}\) labelings of the explicit cyclic supports through order eight; independently validates every query answer along every root-to-leaf path of `derangement_depth4_witness.json`; and verifies eleven positive concepts per allowed five-element query. Executing `python verify_derangement_learning.py derangement_depth4_witness.json` produces the supplied `verification_output.txt`, ending in `DERANGEMENT_SHATTERING_ALL_CHECKS_PASS`.

The all-orders VC theorem is proved above without reliance on finite enumeration. The five-element adaptive lower bound depends on a complete, transparent finite witness, not on a claim that a time-limited search exhausted a larger space.

## Relationship to prior work
Chase and Freitag, *Model Theory and Machine Learning* (initial public preprint January 19, 2018), gives the general relationship between model-theoretic stability and online learnability; its relevant sections define online shattering rather than determining this fixed-point-free permutation incidence class. Bucić, Devlin, Hendon, Horne, and Lund, *Perfect matchings and derangements on graphs* (first public June 13, 2019), studies intersections of perfect matchings, permanents, and graph derangements. In its full arXiv-rendered text, Theorems 1–7 and Sections 2–8 do not establish the VC or Littlestone dimension of all fixed-point-free permutation incidence vectors. The present question instead requires realizing both positive and negative edge-membership constraints, followed by adaptive shattering.

The prior matroid-base incidence result, although also about edge membership, does not imply the theorem: perfect matchings of a crown graph are common bases of *two* partition matroids and do not in general form the bases of one matroid. Prior finite analyses of path/cycle matchings or pairwise-comparison query systems concern different concept classes and cannot yield the exact fixed-point-free incidence statements by renaming parameters.

## Limitations
No formula for the Littlestone dimension at six or more elements is claimed. The finite tree certificate establishes the five-element lower bound only; it is not a proof about all larger orders. Historical novelty beyond the inspected works and accessible research records is not independently certified. The claim is about offline/adaptive shattering dimensions, not noisy learning complexity or efficient identification algorithms.

## References
1. H. Chase and J. Freitag, *Model Theory and Machine Learning*, arXiv:1801.06566v1 (January 19, 2018), https://arxiv.org/html/1801.06566v1.
2. M. Bucić, P. Devlin, M. Hendon, D. Horne, and B. Lund, *Perfect matchings and derangements on graphs*, arXiv:1906.05908v1 (June 13, 2019), https://arxiv.org/abs/1906.05908.
3. P. Hall, *On Representatives of Subsets*, Journal of the London Mathematical Society (1935), for the standard matching criterion.
