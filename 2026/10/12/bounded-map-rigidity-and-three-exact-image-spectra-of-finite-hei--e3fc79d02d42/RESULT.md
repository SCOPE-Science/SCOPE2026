# Bounded-map rigidity and three exact image spectra of finite height-two S4 frames

## Finding
Let \(P_{p,q}=A_p\oplus B_q\), where \(p,q\geq1\), the two disjoint levels are antichains of sizes \(p,q\), and every point of \(A_p\) lies below every point of \(B_q\). Give this poset the reflexive ancestor relation, and let \(\mathcal A_{p,q}=(\mathcal P(P_{p,q}),\Diamond)\) be its complex Boolean S4 modal algebra. A *bounded map* is a function \(f:P_{p,q}\to P_{p,q}\) satisfying \(f[\uparrow x]=\uparrow f(x)\) at each point; its inverse-image map is a modal-algebra endomorphism.

There is a sharp dichotomy according to whether the upper antichain is a singleton. If \(q\geq2\), every bounded endomorphism is **either** a level-preserving map with an arbitrary restriction \(A_p\to A_p\) and a permutation on \(B_q\), **or** a constant map to one of the \(q\) points of \(B_q\). If \(q=1\), the upper point is fixed and each lower point may independently map anywhere in the frame.

For every \(k\geq0\), define the onto-function coefficients
\[
U_{p,k}=\sum_{j=0}^{k}(-1)^j\binom{k}{j}(k-j)^p,\qquad
V_{p,k}=\sum_{j=0}^{k}(-1)^j\binom{k}{j}(k+1-j)^p.
\]
Use the conventions \(U_{p,0}=0\) for \(p\geq1\), and \(V_{p,0}=1\). Also define the rooted-forest number
\[
T(N,r)=\begin{cases}1,&N=r,\\rN^{N-r-1},&1\leq r<N.\end{cases}
\]
Let \(E_{p,q}(z)\), \(I_{p,q}(z)\), and \(H_{p,q}(z)\) count, respectively, all endomorphisms, idempotent endomorphisms, and all endomorphisms by their **eventual image cardinality** under iteration; for \(E\) and \(I\), the exponent is the one-step algebra-image cardinality.

For \(q\geq2\), all three spectra have exact closed forms:
\[
E_{p,q}(z)=qz^2+q!\sum_{k=1}^{p}\binom pk U_{p,k}z^{2^{q+k}},
\]
\[
I_{p,q}(z)=qz^2+\sum_{k=1}^{p}\binom pk k^{p-k}z^{2^{q+k}},
\]
\[
H_{p,q}(z)=qz^2+q!\sum_{k=1}^{p}\binom pk k!T(p,k)z^{2^{q+k}}.
\]
For the exceptional singleton upper level \(q=1\), they instead are
\[
E_{p,1}(z)=\sum_{k=0}^{p}\binom pk V_{p,k}z^{2^{k+1}},
\]
\[
I_{p,1}(z)=\sum_{k=0}^{p}\binom pk(k+1)^{p-k}z^{2^{k+1}},
\]
\[
H_{p,1}(z)=\sum_{k=0}^{p}\binom pk k!T(p+1,k+1)z^{2^{k+1}}.
\]
In particular, every algebraic image rank in \(\{2,2^{q+1},\ldots,2^{q+p}\}\) occurs when \(q\geq2\), and every rank in \(\{2,2^2,\ldots,2^{p+1}\}\) occurs when \(q=1\). The three spectra have identical supports, despite different multiplicities. There are exactly \(q+2^p-1\) possible **dual-frame retraction supports** if \(q\geq2\), and \(2^p\) if \(q=1\). The ordinary endomorphism counts are \(q!p^p+q\) and \((p+1)^p\), respectively.

For example, on the five-world frame \(P_{3,2}\),
\[
E_{3,2}(z)=2z^2+6z^8+36z^{16}+12z^{32},
\]
\[
I_{3,2}(z)=2z^2+3z^8+6z^{16}+z^{32},
\]
\[
H_{3,2}(z)=2z^2+18z^8+24z^{16}+12z^{32}.
\]
Its \(32\)-element complex modal algebra has \(56\) endomorphisms and \(12\) idempotents. Their one-step and eventual-image distributions differ.

## Assumptions and scope
The poset elements are labeled only for counting individual maps; the isomorphism class of the frame depends on \(p,q\). A Kripke bounded map here need not be surjective onto the entire original frame. The exact condition is equality of successor cones at **every** point. The modal algebra has exactly \(2^{p+q}\) elements and uses \(\Diamond S=\{x:\exists y\geq x\text{ with }y\in S\}\). The eventual image of a self-map is the stable set \(\bigcap_{t\geq1}f^t[P_{p,q}]\), while the eventual image of an algebra endomorphism is its stabilized image under iteration. Because inverse image of \(f^t\) is the corresponding iterated algebra map, the eventual algebra-image cardinality is \(2^{|\cap_t f^t[P_{p,q}]|}\).

The count of distinct retraction supports counts subsets of the **dual Kripke frame**, not distinct embedded retract subalgebras or abstract isomorphism types.

## Proof
**1. Normal form.** For every maximal point \(b\in B_q\), its successor set is the singleton \(\{b\}\). The bounded-map equation therefore forces \(f(b)\) to have singleton successor set; equivalently \(f(b)\in B_q\). If a lower point \(a\in A_p\) maps to another lower point \(a'\), then
\[
f[\{a\}\cup B_q]=\{a'\}\cup B_q.
\]
Since \(f(B_q)\subseteq B_q\), this means \(f(B_q)=B_q\). On the finite \(q\)-element set, \(f|_{B_q}\) is therefore a permutation. Conversely, any arbitrary lower-to-lower map together with an upper permutation satisfies the bounded-map condition.

If some lower point maps to an upper point \(b\), its bounded-map equation instead forces \(f(B_q)=\{b\}\). If \(q\geq2\), this cannot coexist with a lower-to-lower image (which would require \(f(B_q)=B_q\)). Thus all lower points map to \(b\), making \(f\) constant. If \(q=1\), the unique upper point is automatically fixed, and a lower point mapped anywhere automatically satisfies its successor-cone condition. This proves both cases of the normal form and the total-map counts.

**2. One-step image spectra.** In the \(q\geq2\) level-preserving case, the image is \(B_q\cup C\), where \(C\subseteq A_p\) has some cardinality \(k\geq1\). There are \(\binom pk\) choices of \(C\), \(U_{p,k}\) surjections from \(A_p\) onto \(C\), and \(q!\) independent upper permutations. Each of the \(q\) constant maps has a one-point image. If \(q=1\), the image is \(\{b\}\cup C\), where \(C\subseteq A_p\) may be empty, and inclusion-exclusion gives \(V_{p,k}\) lower-domain maps in which all \(k\) selected lower image points occur while the upper point may also occur. Inverse-image duality converts a frame image of size \(s\) to an algebra endomorphism image of cardinality \(2^s\), proving both formulas for \(E\).

**3. Idempotents and retraction supports.** The inverse-image map is idempotent precisely when \(f^2=f\). An idempotent permutation of \(B_q\) must be the identity. When \(q\geq2\), a level-preserving idempotent whose lower image is a fixed \(k\)-set \(C\) fixes \(C\) pointwise and freely sends each of the other \(p-k\) lower points to one of the \(k\) fixed ones, giving \(k^{p-k}\) choices. Each upper constant is idempotent. When \(q=1\), fixing \(b\) and the chosen \(k\)-set \(C\) permits each remaining lower point to choose any of \(k+1\) fixed target points, giving \((k+1)^{p-k}\) choices. The same constructive classification establishes the asserted dual-frame retraction supports and proves the two formulas for \(I\).

**4. Eventual images.** Any finite function decomposes into directed cycles and rooted in-trees. The stable image consists exactly of its periodic points. For a level-preserving map with \(q\geq2\), all \(q\) upper points remain periodic because the upper map is a permutation. Choose \(k\) lower periodic points \(C\); arrange them in any permutation (\(k!\) choices). Every other lower point belongs to an oriented forest rooted in \(C\). For \(N\) labeled vertices and a specified set of \(r\) roots, the number of such forests is \(T(N,r)\): when \(r<N\), deleting root rows and columns from the complete-graph Laplacian gives the matrix \(NI_{N-r}-J_{N-r}\), whose determinant is \(rN^{N-r-1}\); when all vertices are roots, only the empty forest occurs. Thus the lower-domain count is \(\binom pk k!T(p,k)\), times \(q!\) upper permutations. Constants stabilize on one upper point.

When \(q=1\), the upper point \(b\) is a fixed periodic root. Choose \(k\) additional lower periodic points and permute them; the remaining lower points form a directed forest flowing to the specified \(k+1\) roots in the \(p+1\)-vertex set. This contributes \(\binom pk k!T(p+1,k+1)\). The forest derivation proves both \(H\) formulas. The explicit normal forms and the positivity of the displayed coefficients also prove all support assertions, completing the theorem.

## Verification
The standalone `verify.py` exhaustively enumerates every function on each \(P_{p,q}\) with \(p,q\geq1\) and \(p+q\leq6\), checks the cone-equality condition directly, tests algebraic modal preservation independently for all functions on frames with at most four points, tests idempotence directly, computes stabilized images from iterates, and compares all three coefficient tables against the formulas. It also checks total identities for \(1\leq p\leq19\), \(1\leq q\leq7\). Its exact output begins:

`VERIFY_OK cases=15 candidate_functions=246606 bounded_maps=9514 direct_modal_checks=826 exact_comparisons=444`

These finite experiments are checks of the proof, not a substitute for the all-parameter arguments. Reproduce with `python3 verify.py` using only the Python standard library.

## Relationship to prior work
Shapirovsky's 2020-first-public study of sums of Kripke frames describes the skeleton/cluster decomposition of finite preorders and the central role of p-morphisms in preserving modal truth. The frame \(P_{p,q}\) is the two-level sum of singleton clusters over the complete bipartite order; the paper studies satisfiability reductions rather than endomorphism or idempotent rank distributions.

Earlier calculations for this **same underlying finite poset** concern all continuous, order-preserving self-maps and their finite-space homotopy classes. Such maps strictly outnumber the bounded maps counted here: boundedness requires the full successor-cone equality, not just monotonicity. The inspected two-level mapping-space results give neither the permutation/constant dichotomy nor the exact modal-algebra image, idempotent, and stabilized-image spectra. Similarly, general weak-order retract criteria concern arbitrary continuous retractions, not Kripke bounded retractions. The forest factor is the classical labeled rooted-forest enumeration; no originality is claimed for that identity.

## Limitations
The theorem concerns complete two-level posets and their particular Boolean modal algebras. It does not enumerate bounded maps of arbitrary height-two posets with missing comparabilities, multi-level sums, or arbitrary finite preorders. The formulas classify supports and cardinalities, not the complete isomorphism types of all embedded algebraic images. The originality searches include closely related finite-space mapping results, but do not exclude unindexed equivalent formulas in older transformation-semigroup or modal-algebra literature. Independent mathematical audit has not been performed.

## References
1. Ilya B. Shapirovsky, *Satisfiability problems on sums of Kripke frames*, arXiv:2012.15347v1, first public 2020-12-30; ACM Transactions on Computational Logic 23 (2022), Article 15, DOI:10.1145/3508068. See Sections 2–3 (p-morphisms and sums).
2. *Mapping-space decomposition for complete height-two finite models*, publicly accessible mathematical research record 2026-10-04, published-finding corpus record `2026/10/4/SCOPE-mapping-space-decomposition-for-complete-height-two-finite-model--3ed4bcca9e63`; comparison is to ordinary continuous maps, not bounded maps.
3. *Self-homotopy and homology-action classification of complete height-two finite graph models*, publicly accessible mathematical research record 2026-10-04, published-finding corpus record `2026/10/4/SCOPE-self-homotopy-and-homology-action-classification-of-complete-hei--903a0da3472e`; comparison is to order-preserving self-maps and their homology actions.
4. *Singleton-gap criterion for retracts and eventual images of finite weak orders*, publicly accessible mathematical research record 2026-10-04, published-finding corpus record `2026/10/4/SCOPE-singleton-gap-criterion-for-retracts-and-eventual-images-of-fini--4d39f7ca58cd`; comparison is to continuous retractions.
5. J. W. Moon, *Counting Labelled Trees*, Canadian Mathematical Congress, 1970. Classical rooted-forest count is also proved above by the matrix-tree determinant.
