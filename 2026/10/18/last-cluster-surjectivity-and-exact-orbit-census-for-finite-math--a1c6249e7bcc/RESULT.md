# Last-cluster surjectivity and exact orbit census for finite \(\mathsf{S4.3}\) bounded morphisms

## Finding
Let \(P=\mathcal C(a_1,\ldots,a_h)\) and \(Q=\mathcal C(b_1,\ldots,b_k)\) be nonempty finite linear preorders, with all cluster sizes positive. The number of **globally surjective bounded morphisms** \(P\to Q\), and their orbits under independent source and target automorphisms, admit complete closed finite formulas.

A surjective function is a bounded morphism if and only if its induced map on the ordered cluster chains is a weakly increasing surjection and, for each target cluster, **the last source cluster assigned to it maps onto the entire target cluster**. Explicitly, it determines a unique sequence
\[
0=e_0<e_1<\cdots<e_k=h
\]
such that source levels \(e_{j-1}+1,\ldots,e_j\) map into target level \(j\), and the restriction of the map from source level \(e_j\) onto target level \(j\) is surjective. Restrictions from the other source levels in the same segment are arbitrary.

Define the number of onto maps between finite labeled sets by
\[
U(n,b)=\sum_{s=0}^{b}(-1)^s\binom{b}{s}(b-s)^n.
\]
The number of labeled surjective bounded morphisms is exactly
\[
L(\mathbf a,\mathbf b)=\sum_{0=e_0<\cdots<e_k=h}\prod_{j=1}^{k}
 b_j^{\sum_{i=e_{j-1}+1}^{e_j-1}a_i}U(a_{e_j},b_j).
\]
Here the sum is empty and has value zero when \(k>h\).

For \(r\ge1\), \(b\ge1\), and positive \(u_1,\ldots,u_r\), put
\[
\mathcal Q_b(u_1,\ldots,u_r)=
[t^b x_1^{u_1}\cdots x_r^{u_r}]
\prod_{\substack{(v_1,\ldots,v_r)\in\mathbb N^r\\v_r\ge1}}
(1-tx_1^{v_1}\cdots x_r^{v_r})^{-1}.
\]
The multivariate coefficient is well defined: in its computation, it suffices to retain vectors with \(0\le v_i\le u_i\). The exact number of **two-sided automorphism orbits** of such maps is
\[
\boxed{\mathcal O(\mathbf a,\mathbf b)=
\sum_{0=e_0<\cdots<e_k=h}
\prod_{j=1}^{k}\mathcal Q_{b_j}(a_{e_{j-1}+1},\ldots,a_{e_j}).}
\]
This is also a bijective classification: the orbit invariant is a cut sequence together with, for each target level, an unordered multiset of \(b_j\) nonnegative integer column vectors, with prescribed row sums and strictly positive final coordinate.

Existence of an onto bounded morphism is equivalent to the existence of indices \(1\le e_1<\cdots<e_k=h\) for which \(a_{e_j}\ge b_j\) for all \(j\). If \(h=k\), letting \(p_b(n)\) denote the number of integer partitions of \(n\) into precisely \(b\) positive parts, the orbit count simplifies to
\[
\mathcal O(\mathbf a,\mathbf b)=\prod_{j=1}^{k}p_{b_j}(a_j).
\]
When all target clusters are singletons, both the map count and the orbit count are \(\binom{h-1}{k-1}\) for \(h\ge k\).

## Assumptions and scope
For a positive vector \(\mathbf a=(a_1,\ldots,a_h)\), \(\mathcal C(\mathbf a)\) is the Kripke frame with a disjoint union of nonempty sets \(A_1,\ldots,A_h\), of sizes \(a_i\), and relation \(xRy\) exactly when the cluster index of \(x\) is at most that of \(y\). In particular, **all two points of one cluster are mutually accessible**, including reflexive loops; this is not the ordinal sum of antichains regarded as an antisymmetric partial order. These are finite total preorders, also called linear quasi-orders, a standard frame class for \(\mathsf{S4.3}\).

A bounded morphism \(f:(P,R)\to(Q,S)\) is a function satisfying forth \(xRy\Rightarrow f(x)Sf(y)\) and back: whenever \(f(x)Sz\), some \(y\) with \(xRy\) satisfies \(f(y)=z\). Equivalently, \(f[R(x)]=S(f(x))\) for every source vertex \(x\). Only genuinely globally surjective maps are counted, with no vertex valuations or extra constants. The orbit equivalence is \(g=\beta\circ f\circ\alpha^{-1}\), where \(\alpha\in\operatorname{Aut}(P)\) and \(\beta\in\operatorname{Aut}(Q)\).

All sizes, heights, and parameters are positive integers; both frames are finite and nonempty. \(\mathbb N\) in the product denotes the nonnegative integers. Products over empty sets are one.

## Proof
**Cluster reduction.** Write \(i(x)\) for the source cluster index and \(j(z)\) for the target index. Two vertices lie in one cluster if and only if they are mutually accessible. Forth therefore maps each source cluster into exactly one target cluster. If source cluster \(i\) is below cluster \(i'\), forth implies its target index is at most the index of cluster \(i'\). A globally onto map consequently induces a weakly increasing surjection \([h]\to[k]\), uniquely represented by endpoints \(e_1,\ldots,e_k\). Every automorphism preserves every ordered cluster and permutes its points freely, giving \(\operatorname{Aut}(P)=\prod_i S_{a_i}\) and \(\operatorname{Aut}(Q)=\prod_j S_{b_j}\).

**The last-cluster condition.** Fix a target cluster \(B_j\), and its last preimage source cluster \(A_{e_j}\). For \(x\in A_{e_j}\), its accessible successors comprise \(A_{e_j}\) and all later source clusters, whose images lie entirely in target clusters strictly above \(B_j\). But \(S(f(x))\) contains *every* point of \(B_j\). Thus back forces \(f[A_{e_j}]=B_j\). Conversely, assume this condition for every \(j\). Given \(x\in A_i\) assigned to \(B_j\), for every target cluster \(B_\ell\) with \(\ell\ge j\), its endpoint source cluster \(A_{e_\ell}\) lies in \(R(x)\) and maps onto all of \(B_\ell\). Forth places no image below \(B_j\). Hence \(f[R(x)]=S(f(x))\) for every \(x\), proving the characterization.

**Labeled enumeration and existence.** Once endpoints are fixed, every earlier source cluster in a segment may map arbitrarily to the corresponding target cluster, giving \(b_j^{\sum_{i=e_{j-1}+1}^{e_j-1}a_i}\) possibilities, whereas the final source cluster must map onto \(B_j\), giving \(U(a_{e_j},b_j)\) choices by inclusion--exclusion. Multiply the independent factors, then sum over cuts. Since a surjection from an \(a\)-point set to a \(b\)-point set exists exactly when \(a\ge b\), the stated endpoint criterion follows.

**Orbit classification.** Fix a cut sequence. For target cluster \(B_j\), define for each \(z\in B_j\) its *fiber-count vector* \(v(z)=(|A_{e_{j-1}+1}\cap f^{-1}(z)|,\ldots,|A_{e_j}\cap f^{-1}(z)|)\). These are nonnegative integer vectors whose row sums are the source cluster sizes. The final coordinate of each vector is positive exactly because \(A_{e_j}\to B_j\) is onto. Permuting each source cluster changes a function without changing these counts, and conversely any two functions with identical labeled count vectors differ by permutations inside each source cluster. Permuting the target cluster independently of other target clusters removes the ordering of the \(b_j\) column vectors. Thus two bounded morphisms are equivalent under the two automorphism groups precisely when their cuts and per-target-level column multisets agree. The formal generating series for unordered multisets of vectors \(v\) is the product of geometric series \(\prod_v(1-t\mathbf x^v)^{-1}\); coefficient extraction fixes the column count and row sums. Multiply across target clusters and sum over cuts, which are invariant under all frame automorphisms.

**Boundary specializations.** When \(h=k\), every segment contains one source cluster, so its count vectors are positive integers adding to \(a_j\); unordered vectors are precisely integer partitions with \(b_j\) parts. If every \(b_j=1\), the unique target point in each cluster forces the function once the cut sequence is chosen, and there are \(\binom{h-1}{k-1}\) cut sequences.

## Verification
Two standalone Python programs are included. `artifacts/verify_bruteforce.py` enumerates all globally onto functions on finite labeled sets for 395 ordered composition-pairs (source size at most five and target size at most four), independently checks the complete successor-image equality at every point, and compares both map counts and orbit-profile counts with the explicit formulas. It reports 1,550 bounded morphisms and 247 total orbits across these test cases. `artifacts/verify_group_actions.py` computes *actual orbits* using generators for independent source/target cluster permutations in 22 further cases and confirms the formula; no presumed fiber classification is used to build those group-action orbits.

Reproduce with Python 3 using `python3 artifacts/verify_bruteforce.py` and `python3 artifacts/verify_group_actions.py`; both use only the standard library. Example counts are \(L((2,2,2),(2,2))=32\), \(\mathcal O((2,2,2),(2,2))=4\), and \(L((3,2,3),(2,2))=240\), \(\mathcal O((3,2,3),(2,2))=5\). The proofs above, not these finite experiments, establish the general statements.

## Relationship to prior work
The classical forth/back definition and its modal truth-preservation role are given by Goranko and Otto, *Model Theory of Modal Logic*, Section 2.2, particularly Definition 15. Finite linear preorders are standard \(\mathsf{S4.3}\) frames; Fine's earlier work and Shapirovsky's work on sums of modal frames supply the broader context. These sources provide the underlying semantics and frame decomposition rather than the present per-cluster surjectivity criterion with a full two-sided orbit count.

A separately published result on **maps of weak-order finite \(T_0\)-spaces** counts continuous order-preserving maps between ordinal sums of antichains. Its objects are antisymmetric, with points in one level incomparable, and its maps need not satisfy modal back or global surjectivity. Hence its cardinality recurrence does not imply this theorem for linear *preorders whose clusters are full equivalence relations*. Likewise a previously established enumeration of surjective bounded morphisms between **ordinal sums of antichains** and a separate two-sided orbit classification for **unstructured \(\mathsf{S5}\) equivalence frames** address different structures: the former has no mutual accessibility inside a level and the latter has no linear ordering between distinct clusters. None of those statements contains this mixed cross-cluster last-surjectivity and orbit formula.

## Limitations
The formula counts unvalued, finite, **globally onto** frame maps and their automorphism orbits; it does not count arbitrary monotone maps, non-onto bounded morphisms, modal valuations, non-total preorder skeletons, or mappings of infinite frames. It is an explicit coefficient formula rather than an asserted polynomial-bit-complexity algorithm. The literature and research-record comparisons do not certify publication priority; specialized cluster-map enumerations may not be indexed. The most closely matching older frame-sums conference note was available only in partially indexed text, not in a fully inspected paper, so specialized overlap remains a documented risk.

## References
1. V. Goranko and M. Otto, *Model Theory of Modal Logic*, Section 2.2, in the *Handbook of Modal Logic* (2007), accessible author PDF at https://www.mathematik.tu-darmstadt.de/~otto/papers/Chapter5_02_05_06.pdf .
2. PlanetMath, *p-morphism*, first published 2013-03-22, https://planetmath.org/pmorphism .
3. K. Fine, *The Logics Containing S4.3*, *Mathematical Logic Quarterly* 17 (1971), 371--376, DOI: 10.1002/malq.19710170141 .
4. I. Shapirovsky, *Modal logics of ordered sums of frames* (2009), https://www.researchgate.net/publication/241782900_Modal_logics_of_ordered_sums_of_frames .
5. I. Shapirovsky, *Truth-Preserving Operations on Sums of Kripke Frames*, *Advances in Modal Logic* 12 (2018), 541--558, https://www.aiml.net/volumes/volume12/Shapirovsky.pdf .
6. *Exact cardinality recurrence for mapping spaces between finite weak orders* (published 2026-10-04), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-cardinality-recurrence-for-mapping-spaces-between-finite-w--1cee64311a06 .
