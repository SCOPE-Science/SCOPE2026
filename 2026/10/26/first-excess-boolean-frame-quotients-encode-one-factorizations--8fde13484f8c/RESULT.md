# First-excess Boolean-frame quotients encode one-factorizations

## Finding
For integers \(m\ge2\) and \(n\ge0\), let \(B_n\) be the reflexive inclusion frame of all subsets of \([n]\). Let \(Q_m\) be the reflexive three-level frame with a least point \(\bot\), a greatest point \(\top\), and exactly \(m\) pairwise incomparable intermediate points \(a_1,\ldots,a_m\), with \(\bot<a_i<\top\). Thus \(Q_m\) has **three order levels** and \(m+2\) worlds. All worlds and the intermediate target labels are distinguished; different maps are counted separately.

A **bounded morphism** \(f:B_n\to Q_m\) is a function satisfying (i) forth: \(x\subseteq y\) implies \(f(x)\le f(y)\), and (ii) back: for every \(x\in B_n\) and every \(q\ge f(x)\), some \(y\supseteq x\) has \(f(y)=q\). Write \(N(n,m)\) for the number of *surjective* bounded morphisms.

**Sharp threshold:** \(N(n,m)=0\) for \(n<m\), while \(N(m,m)=m!\); such morphisms exist for every \(n\ge m\).

For every even \(z\ge2\), write \(F_z\) for the number of proper edge-colourings of the complete graph on the **fixed labelled vertex set** \([z]\), using the **fixed labelled palette** of exactly \(z-1\) colours, with different colours on adjacent edges. Equivalently, \(F_z\) is \((z-1)!\) times the number of one-factorizations on the fixed labelled vertices with unordered factors. Then
\[
\boxed{N(m+1,m)=m!\left((m+1)^2+(m+1)+\sum_{\substack{2\le z\le m+1\\z\ \mathrm{even}}}\binom{m+1}{z}\frac{F_z}{(z-1)!}\right).}
\]
More precisely, among these morphisms the number \(z\) of singleton Boolean worlds that map to \(\bot\) can only be \(0\), \(1\), or a positive even integer. Their contributions are
\[
\begin{aligned}
 z=0:&\quad m!(m+1)^2,\\
 z=1:&\quad m!(m+1),\\
 z\ge2\ \mathrm{even}:&\quad\binom{m+1}{z}\frac{m!}{(z-1)!}F_z.
\end{aligned}
\]
In particular \(N(3,2)=30\), \(N(4,3)=162\), \(N(5,4)=1080\), and \(N(6,5)=9360\). The correspondence with one-factorizations is an **actual bijection** after specifying the zero singleton set and the colours of all nonzero singleton worlds.

## Assumptions and scope
All relations are reflexive and transitive, and no additional predicates are present. The graph's vertices and edge-colour names in \(F_z\) are fixed; the number is **not** a graph-isomorphism-class count. The theorem assumes \(m\ge2\). It concerns globally onto bounded morphisms, not arbitrary monotone functions, and does not assert a formula for \(N(n,m)\) for arbitrary \(n>m+1\).

## Proof
**1. The frontier obstruction.** For every onto order-preserving map \(f:B_n\to Q_m\), the least and greatest Boolean elements necessarily map to \(\bot\) and \(\top\), respectively. Let \(Z=f^{-1}(\{\bot\})\), a nonempty proper downset. Choose a maximal \(s\in Z\). By back-lifting, each intermediate \(a_i\) has a preimage \(y_i\supseteq s\). Along a saturated Boolean chain from \(s\) to \(y_i\), the first strict successor \(s\cup\{j\}\) is outside \(Z\) and has image at most \(a_i\). As it is not \(\bot\), its image must equal \(a_i\). Distinct \(i\) require distinct immediate successors of \(s\); hence \(n-|s|\ge m\). Therefore \(n\ge m\), and whenever \(n=m+1\), every maximal member of \(Z\) has Boolean rank at most one.

**2. Threshold equality.** If \(n=m\), the obstruction forces \(Z=\{\varnothing\}\). The \(m\) Boolean singleton worlds must receive the \(m\) distinct middle labels bijectively. Every Boolean world of rank at least two dominates two differently labelled singleton worlds, so must map to \(\top\). Conversely all \(m!\) maps so obtained satisfy both conditions: \(\bot\) sees each intermediate label at rank one, and every intermediate-valued world sees \(\top\). To obtain maps for \(n>m\), precompose one such map with the coordinate projection \(B_n\to B_m\); that projection is onto and satisfies back-lifting.

**3. The zero frontier at first excess.** Now put \(n=m+1\). From step 1, either \(Z=\{\varnothing\}\), or \(Z\) is \(\{\varnothing\}\) together with a nonempty set \(S\subseteq[n]\) of singleton worlds. Write \(z=|S|\). If \(z\ge1\), each zero singleton \(\{i\}\) has exactly \(n-1=m\) immediate Boolean successors, and each intermediate label must occur above it. By the frontier argument these \(m\) successors receive the middle labels **each once**. In particular, all rank-two worlds containing an index of \(S\) map to a middle label, never to \(\top\).

**4. No zero singleton.** If \(z=0\), each middle label must occur at a singleton: any first successor on a chain from \(\varnothing\) to a witness of that middle label is nonzero and cannot have a different intermediate or top image. There are \(m+1\) singleton worlds and \(m\) required middle labels. Either exactly one singleton is top-valued and the others have distinct intermediate labels, yielding \((m+1)m!\) maps, or exactly one middle label occurs twice and every other middle label once. There are \(m\binom{m+1}{2}(m-1)!\) assignments in the second case. Only the rank-two world formed by the two identically labelled singleton worlds has a choice: it may have that middle label or \(\top\). All other rank-two worlds and every world of rank at least three must be top-valued. Hence the second case contributes \(2m!\binom{m+1}{2}\), and the total for \(z=0\) equals \(m!(m+1)^2\).

**5. At least one zero singleton and factorization.** Fix \(S\) with \(|S|=z\ge1\). Every singleton \(\{j\}\) with \(j\notin S\) has an intermediate image: for any \(i\in S\), its rank-two union with \(\{i\}\) has a middle image, so the nonzero singleton below it has the same image. These \(m+1-z\) singleton images are pairwise different, since the corresponding rank-two successors of \(\{i\}\) all have different labels. Choose them in \(m!/(z-1)!\) ways. The remaining \(z-1\) middle labels are used on the rank-two worlds \(\{i,j\}\) with \(i,j\in S\). At each \(i\in S\), all remaining labels must occur exactly once on the incident edges. Thus these ranks define precisely a proper edge-colouring of \(K_z\) with its \(z-1\) **specified** available labels. Such a colouring exists only when \(z=1\) (empty edge set), or when \(z\ge2\) is even: each colour then forms a perfect matching, whereas an odd vertex count admits no perfect matching. The counts are \(1\) for \(z=1\) and \(F_z\) for even \(z\ge2\).

Every Boolean world of rank three or more must be top-valued. Indeed, any three-coordinate subset contains either two nonzero singleton worlds of distinct middle labels; or a nonzero singleton and two zero singleton worlds, whose rank-two labels include both a nonzero and a remaining middle label; or three zero singleton worlds, whose two edges incident at one vertex have distinct middle labels. In every case that rank-three world lies above two differently middle-labelled worlds and so can only map to \(\top\). Larger worlds inherit the top image.

Conversely, every assignment described above produces a monotone map. Each zero singleton sees all \(m\) intermediate labels on its immediate successors, and so does the empty Boolean world; every intermediate-valued world has the full Boolean top above it. These are all nontrivial back-lifting requirements. Hence each assignment gives exactly one onto bounded morphism, without overcounting.

Choose \(S\) in \(\binom{m+1}{z}\) ways, choose singleton intermediate labels in \(m!/(z-1)!\) ways, and choose a proper \(K_z\) edge-colouring in \(F_z\) ways. Summing these mutually disjoint cases, together with step 4, proves the stated formula and the parity classification.

## Verification
The accompanying `verification/verify.py` enumerates **all** monotone target assignments for \((n,m)=(2,2),(3,2),(4,3)\), then checks onto-ness and each back condition directly on upper cones. This independent enumeration gives respectively \(2,30,162\) maps. It separately enumerates proper edge-colourings of \(K_2,K_4,K_6\), obtaining \(F_2=1,F_4=6,F_6=720\). The formula then yields \(30,162,1080,9360\) for \(m=2,3,4,5\). All computations are exact integer arithmetic; only the first three small frame cases are exhaustively checked independently of the proof. The general theorem rests on the frontier and factorization bijections, not on finite enumeration.

## Relationship to prior work
Bounded morphisms of finite Kripke frames are standard in modal and intuitionistic semantics. Kudinov and Shapirovsky (2015) study partitions and filtrations of finite-height Kripke frames, not the enumeration of onto bounded morphisms from Boolean inclusion frames onto the targets here. Previously studied Boolean-frame quotients onto a three-world **chain**, and onto the four-world **diamond** \(Q_2\), supply neighboring special cases; the latter overlaps the \(m=2\) part of the present scope. Neither supplies the all-\(m\) first-excess classification or its labelled \(K_z\) factorization decomposition. Kaski, de Souza Medeiros, Östergård, and Wanless (2014) study one-factorizations and switching graphs; their definition of a factorization as a proper complete-graph edge colouring exactly matches the construction in step 5 after fixing the unused intermediate target labels. Their work does not study Boolean-frame bounded morphisms. The novelty asserted here is the **cross-structure bijection and exact first-excess quotient census**, not the known one-factorization numbers or the standard bounded-morphism definition.

## Limitations
Only \(n=m\) and \(n=m+1\) admit explicit counts here. No efficient algorithm for computing arbitrary \(F_z\) is claimed. The term \(F_z\) is an existing combinatorial invariant, not a newly evaluated sequence. There may be older specialized bounded-morphism enumerations absent from the located literature, especially sources accessible only by abstract. The \(m=2\) specialization overlaps prior four-world diamond work and is included to show the natural boundary of the formula, not as an independent novelty claim. No external proof certification or independent mathematical audit is asserted.

## References
1. P. Kaski, A. de Souza Medeiros, P. R. J. Östergård, and I. M. Wanless, *Switching in One-Factorisations of Complete Graphs*, Electronic Journal of Combinatorics **21** (2014), P2.49, published 2014-06-09, DOI: 10.37236/3606. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v21i2p49
2. A. Kudinov and I. Shapirovsky, *On partitioning Kripke frames of finite height*, arXiv:1511.09092 (first public version 2015-11-29). https://arxiv.org/abs/1511.09092
3. E. Mendelsohn and A. Rosa, *One-factorizations of the complete graph—A survey*, Journal of Graph Theory **9** (1985), 43–65, DOI: 10.1002/jgt.3190090104. (Used for historical background; the available abstract does not address frame morphisms.)
