# Coefficientwise balancing of bounded-class nilpotent partial-injection semigroups

## Finding
Let \(\mathcal I_n\) denote the symmetric inverse monoid on a labeled \(n\)-point set and let \(0\) be its empty map. For integers \(n\ge k\ge3\), consider subsemigroups \(S\subseteq\mathcal I_n\) with \(S^k=\{0\}\). Put \(\operatorname{rk}(f)=|\operatorname{dom}f|\). For a subsemigroup \(S\), its rank polynomial is \(P_S(t)=\sum_{f\in S}t^{\operatorname{rk}f}\).

Let \(q=\lfloor n/k\rfloor\), \(r=n-kq\), and let \(\mathbf b\) be any length-\(k\) sequence containing \(k-r\) entries \(q\) and \(r\) entries \(q+1\). For an ordered partition \(X=X_1\sqcup\cdots\sqcup X_k\) with positive sizes \(\mathbf a=(a_1,\ldots,a_k)\), let \(M(\mathbf a)\) contain all partial injections whose arrows point from a lower-indexed to a strictly higher-indexed block, including the empty map. Define \(P_{\mathbf a}(t)=P_{M(\mathbf a)}(t)\).

**Theorem.** For each subsemigroup \(S\) with \(S^k=\{0\}\), the coefficientwise inequality \(P_S(t)\preceq P_{\mathbf b}(t)\) holds. Moreover,
\[
\sum_{a_1,\ldots,a_k\ge0}P_{\mathbf a}(t)\prod_{i=1}^k\frac{z_i^{a_i}}{a_i!}
=\exp\!\left(\sum_{\varnothing\ne J\subseteq[k]}t^{|J|-1}\prod_{j\in J}z_j\right).
\]
In particular the largest cardinality of a subsemigroup with \(S^k=\{0\}\) is \(P_{\mathbf b}(1)\). Equality in cardinality holds exactly for the complete upward-layer semigroups associated with balanced ordered partitions; there are
\[
\binom{k}{r}\frac{n!}{(q!)^{k-r}((q+1)!)^r}
\]
such subsemigroups. At \(k=3\) the maxima for \(n=3,\ldots,10\) are \(5,10,27,87,235,778,2971,9754\).

## Assumptions and scope
Every arrow \(x\mapsto f(x)\) of a map in \(M(\mathbf a)\) satisfies \(x\in X_i\), \(f(x)\in X_j\), \(i<j\). The operations are ordinary compositions of partial injections, the zero is the empty map, and \(S^k=\{0\}\) means all products of \(k\) elements are the empty map. The integer conditions are \(n\ge k\ge3\). The polynomial order \(\preceq\) is coefficientwise, not an order on evaluations at negative \(t\).

## Proof
**1. Established structural reduction.** Ganyushkin and Mazorchuk, *On classification of maximal nilpotent subsemigroups*, Theorem 5.15 and Section 6.1, identify the maximal subsemigroups satisfying \(S^k=\{0\}\) in \(\mathcal I_n\): they are exactly the complete upward-layer semigroups \(M(\mathbf a)\) for ordered partitions into \(k\) nonempty blocks, and different ordered partitions give different semigroups. Every candidate \(S\) lies in one of these maximal subsemigroups. The structural reduction and the number of all maximal bounded-class subsemigroups are prior literature, not part of the asserted originality.

**2. Rank-preserving chain/partition bijection.** A partial injection whose arrows strictly increase the layer index has no directed cycle. Its functional digraph is a union of directed paths, including isolated vertices; each path contains at most one vertex from each layer. Conversely, a set partition into blocks meeting each layer at most once determines one map: order the vertices in each set-partition block by their layer indices and join consecutive vertices by arrows. These constructions are mutually inverse. A block containing \(j\) vertices contributes \(j-1\) arrows to the rank. Consequently the exponential formula for labeled set partitions, with one possible vertex from each chosen nonempty subset \(J\subseteq[k]\), gives exactly the displayed multivariate rank generating function. No asymptotic approximation is used.

**3. A coefficientwise balancing lemma.** Fix all layer sizes except those of two colors, say \(a\) and \(b\) with \(a\ge b+2\), and fix a rank \(d\). In the partition model, further stratify by \(h\), the number of blocks containing one vertex of each of the two colors. Temporarily distinguish a common labeled ground set of \(a+b\) vertices and choose which \(a\) of these receive the first color, keeping every other color class fixed. Write \(F_{a,b,h,d}\) for the number of such colored partitions. There are \(a-h\) first-color vertices not sharing a block with the second color; recoloring one of them changes sizes to \((a-1,b+1)\), preserves validity, the number \(h\), every block size, and hence rank \(d\). In the reverse direction, there are \(b+1-h\) eligible second-color vertices. Marking the recolored vertex makes these moves inverse, giving
\[
(a-h)F_{a,b,h,d}=(b+1-h)F_{a-1,b+1,h,d}.
\]
If \(N_{a,b,h,d}\) denotes the number for any one prescribed allocation of the labels to the two colors, then \(F_{a,b,h,d}=\binom{a+b}{a}N_{a,b,h,d}\), and likewise after transfer. Thus
\[
\frac{N_{a-1,b+1,h,d}}{N_{a,b,h,d}}=
\frac{(b+1)(a-h)}{a(b+1-h)}\ge1
\]
when both quantities are positive. The weak inequality follows from \(h(a-b-1)\ge0\). This is a counting identity rather than an assumption that every term is nonzero. Summation over \(h\) proves coefficientwise increase of the rank polynomial when an imbalanced pair is made more balanced. Iterate until the sizes differ by at most one.

**4. Strictness and equality.** For every pair of nonempty layers there is at least one partition containing one block with a vertex from each of those two colors and singleton blocks elsewhere. This has \(h=1\), \(d=1\), and positive count. Whenever \(a\ge b+2\), the balancing ratio above is then strictly larger than one, so the coefficient of \(t\) increases strictly. Therefore an unbalanced ordered partition cannot maximize cardinality. Every balancing step preserves the total number of vertices, and all balanced size vectors are permutations of one another; the rank polynomial is symmetric in the layer sizes by its exponential formula. This establishes the coefficientwise upper bound and characterizes equality. For any prescribed balanced vector there are \(n!/\prod a_i!\) ordered partitions, and there are \(\binom{k}{r}\) choices for the positions of larger blocks. Distinct ordered partitions give distinct maximal subsemigroups by the cited structural theorem, proving the stated count.

## Verification
The accompanying standard-library program `verify_balanced_nilpotent.py` independently generates partial injections and directly counts the permitted maps, checking every ordered composition for \(2\le n\le6\) and \(2\le k\le\min(n,4)\). It uses a separate recursive counting method for rank-weighted transversal set partitions and verifies coefficientwise balancing and all extremal size vectors through \(n=12\), \(k\le5\). It prints `VERIFY_OK_BALANCED_NILPOTENT_LAYERS` on success. The proof above applies for all integers in scope; the finite checks are corroboration, not a proof of the infinite statement.

## Relationship to prior work
Ganyushkin and Mazorchuk (2005), building on 1994 and 1995 classifications, establish the complete ordered-partition description of maximal bounded-class nilpotent subsemigroups of symmetric inverse monoids. The present theorem **uses** that structural result, and makes no novelty claim for it. Araújo, Bentz, and Konieczny (2012) determine the maximum size of a *commutative* nilpotent subsemigroup; their balanced null-semigroup result covers the \(k=2\) case, which is therefore excluded from the claimed new extremal statement. Cameron et al. (2021) study nilpotent subsemigroups of the **full transformation semigroup**, which permits many-to-one mappings and does not imply these partial-injection rank coefficients or their balancing order. The rank-sensitive transversal-partition formula, coefficientwise balancing for \(k\ge3\), and associated sharp maximum-cardinality counts are the assessed contributions.

## Limitations
This result concerns finite labeled sets and subsemigroups with products of exactly \(k\) factors always equal to the *empty* partial injection; an abstract nilpotent semigroup represented with a nonempty zero is not included. The all-classes structural reduction and the null case are prior results. Although relevant full primary texts from 2005 and 2012 were inspected, the older 1994/1995 classification papers were not read in full, and potential equivalent unpublished or less-indexed enumerations remain a historical-priority risk. Independent mathematical validation is not claimed.

## References
1. O. Ganyushkin and V. Mazorchuk, *On classification of maximal nilpotent subsemigroups* (2005), arXiv:math/0510372, especially Theorem 5.15 and Section 6.1. First posted 18 October 2005.
2. J. Araújo, W. Bentz and J. Konieczny, *The Commuting Graph of the Symmetric Inverse Semigroup* (2012), arXiv:1205.1664, Section 4 and Theorem 4.19. First posted 8 May 2012.
3. P. J. Cameron et al., *Minimum degrees of finite rectangular bands, null semigroups, and variants of full transformation semigroups* (2021), arXiv:2110.09701, especially Section 4 and Theorem 4.15. This later source is used only for comparison.
4. O. Ganyushkin and collaborators, *On nilpotent subsemigroups of a finite symmetric inverse semigroup* (1994), and *The structure of nilpotent subsemigroups of a finite inverse symmetric semigroup* (1995), as referenced by Ganyushkin–Mazorchuk; primary full texts not independently inspected.