# The equivariant Stong core of two-point configurations of finite crowns

## Finding
For every integer \(n\ge2\), the ordered finite-space two-point configuration space of the \(2n\)-point crown strongly deformation retracts onto the subposet of **incomparable ordered pairs**, which is its precise Stong core. The retraction commutes with every crown order automorphism and with interchange of the two particles.

The resulting core has
\[
\lvert K_n\rvert=2n(2n-3)
\]
points and is obtained by deleting exactly \(4n\) down beat points. For \(n=2\), it is isomorphic to the four-point crown. For every \(n\ge3\), its height is three, not two; therefore the configuration space is **not homotopy equivalent as a finite topological space to any crown**, despite the previously established weak homotopy equivalence to a circle.

## Assumptions and scope
Identify finite \(T_0\)-spaces with their specialization posets. Let
\[
C_n=\{a_i,b_i:i\in\mathbb Z/n\mathbb Z\},\qquad
 a_i<b_j\ \Longleftrightarrow\ j\in\{i,i+1\}.
\]
All \(a_i\) are minimal and all \(b_j\) maximal. Define
\[
F_n=F_2(C_n)=\{(x,y)\in C_n\times C_n:x\ne y\},
\qquad
K_n=\{(x,y)\in F_n:x\not\le y\ \text{and}\ y\not\le x\}.
\]
Both have the induced coordinatewise order. The two involutions \(x\leftrightarrow y\) and crown order automorphisms act naturally on these posets. A **down beat point** is an element whose strict lower set has a greatest element; an **up beat point** is defined dually. A Stong core is a beat-point-free strong deformation retract, unique up to isomorphism for finite \(T_0\)-spaces.

## Proof
**1. The deleted pairs and their canonical beat witnesses.** Distinct comparable crown elements are precisely the incidences \(a_i<b_j\). Hence the complement \(F_n\setminus K_n\) consists of the \(2n\) pairs \((a_i,b_j)\) with \(a_i<b_j\) and the \(2n\) reversed pairs \((b_j,a_i)\). All these \(4n\) pairs are mutually incomparable in \(F_n\): they have product ranks \((0,1)\) or \((1,0)\), and within either rank they are incomparable unless equal.

Each \(b_j\) has exactly two lower neighbors, \(a_j\) and \(a_{j-1}\), also when \(n=2\). For an incidence \(a_i<b_j\), denote its *other* lower neighbor by \(a_k\), where \(\{i,k\}=\{j,j-1\}\). The strict lower set of \((a_i,b_j)\) inside \(F_n\) is the singleton \(\{(a_i,a_k)\}\); \((a_i,a_i)\) is excluded by the deleted diagonal. Dually, the strict lower set of \((b_j,a_i)\) is the singleton \(\{(a_k,a_i)\}\). These are in \(K_n\). Thus each of the \(4n\) excluded points is a down beat point, and since the excluded points are pairwise incomparable, they can be deleted in any order with their witnesses unchanged.

**2. Explicit equivariant deformation retraction.** Define \(r:F_n\to K_n\) to fix \(K_n\) and send each comparable point to the unique predecessor just described. Its values satisfy \(r(p)\le p\). It is order preserving: if \(p<q\) and \(q\notin K_n\), the strict lower set of \(q\) consists only of \(r(q)\), so \(p=r(q)\) and \(r(p)=r(q)\); if \(q\in K_n\), then \(r(p)\le p<q=r(q)\). The equality case is immediate. Consequently the natural transformation \(r\le\mathrm{id}_{F_n}\) is a finite-space homotopy fixing \(K_n\) throughout, so \(K_n\hookrightarrow F_n\) is a strong deformation retract. The witness for each deleted incidence is intrinsically its only strict predecessor, and incomparability is invariant under order automorphisms. Hence \(r\) commutes with the diagonal action of \(\operatorname{Aut}(C_n)\) and with the coordinate swap, proving equivariance.

**3. Minimality of the survivor.** For \(n\ge3\), the sets \(N(a_i)=\{b_i,b_{i+1}\}\) are distinct when \(i\) varies. Consider a point \((a_i,a_j)\in K_n\) with \(i\ne j\). Choose \(b_s\in N(a_j)\setminus N(a_i)\) and \(b_t\in N(a_i)\setminus N(a_j)\). Its strict upper set in \(K_n\) contains the incomparable points \((a_i,b_s)\) and \((b_t,a_j)\). Any common lower bound of these two points above \((a_i,a_j)\) would have to equal \((a_i,a_j)\); hence their upper set has no least point. The opposite-order argument treats each \((b_i,b_j)\) with \(i\ne j\). For a surviving mixed point \((a_i,b_j)\), the incomparability means \(b_j\notin N(a_i)\): it has two incomparable strict predecessors \((a_i,a_j)\), \((a_i,a_{j-1})\), and two incomparable strict successors \((b_i,b_j)\), \((b_{i+1},b_j)\), with no common greatest predecessor or least successor. The same argument applies to \((b_j,a_i)\) by particle swap. Thus no point of \(K_n\) is a beat point. For \(n=2\), \(K_2\) consists of the two distinct ordered minimal-minimal pairs and the two distinct ordered maximal-maximal pairs, with all four cross-level incidences; it is a four-point crown, also without beat points. Therefore \(K_n\) is a Stong core in every case.

**4. Cardinality and sharp homotopy distinction.** The original deleted product has \(2n(2n-1)\) points, so \(\lvert K_n\rvert=2n(2n-1)-4n=2n(2n-3)\). When \(n=2\), the first-coordinate projection \(K_2\to C_2\) is an order isomorphism. When \(n\ge3\), choose distinct \(i,j\), let \(b_s\in N(a_j)\setminus N(a_i)\), and choose any \(b_t\in N(a_i)\). Then
\[
(a_i,a_j)<(a_i,b_s)<(b_t,b_s)
\]
is a strict three-point chain in \(K_n\). No four-point chain exists because the two coordinates each change strict order at most once. Hence its height is exactly three, whereas every crown has height two and is already a Stong core. By uniqueness of finite-space cores, \(F_n\) is not finite-space homotopy equivalent to any crown for \(n\ge3\). The previously known weak homotopy equivalence to \(S^1\) does not contradict this stronger finite-space distinction.

## Verification
The accompanying dependency-free `verify.py` reconstructs all pointwise orders and maps for every \(2\le n\le12\). For each parameter it checks: the deleted-product and core cardinalities; the unique greatest strict predecessor for **every** removed point; incomparability of all removed points; global monotonicity, pointwise inequality, and retraction identity for \(r\); absence of both types of beat points throughout the entire core; equivariance under rotation, reflection, and particle interchange; and the sharp height-two/height-three threshold. Its direct execution on the packaged source returned `VERIFY_OK`, including \(552\) original points, \(48\) deleted points, and a \(504\)-point core at \(n=12\).

The finite checks are stress tests only: the quantified statement and exact equivariance for all \(n\ge2\) are established in the preceding symbolic proof.

## Relationship to prior work
Minian, *Morse theory of Bestvina–Brady type for posets and matchings* (first public May 23, 2022; primary MSC 55U05), develops relative Morse and matching methods on finite posets, but does not state the present crown-deleted-product core or its equivariant retraction. Barmak and Minian's *Minimal Finite Models* develops finite-space cores and beat-point theory, without treating these configuration spaces.

The published same-object result *Two-point configurations of finite crowns retain the circle weak type* establishes that \(F_2(C_n)\to C_n\) is a **weak** homotopy equivalence and explicitly leaves finite-space homotopy equivalence unproved. Its conclusion alone does not identify the Stong core or determine whether any finite-space homotopy equivalence exists: the present result proves this fails for \(n\ge3\) while giving the exact equivariant core. The related published result *The two-point configuration of a minimal finite sphere has the same core* treats sphere models in dimensions at least two; its posets are not crowns. The published product-core rigidity theorem applies to the **entire** Cartesian product, not the complement of its diagonal. Wiltshire-Gordon's models address configuration spaces of geometric realizations of simplicial complexes, not this Alexandrov deleted product.

## Limitations
Only ordered configurations of two distinct points of finite Alexandrov crowns are treated; no statement is made for geometric circle configurations, unordered quotient spaces, three or more particles, or arbitrary finite models of a circle. The core is unique up to order isomorphism, not a unique labeled subset under arbitrary presentations. The height-based non-equivalence concerns homotopy of finite \(T_0\)-spaces, not ordinary weak homotopy types or geometric realizations. No claim of absolute novelty is inferred from search absence; an unindexed older equivalent formulation remains a residual literature risk.

## References
1. E. G. Minian, *Morse theory of Bestvina–Brady type for posets and matchings*, arXiv:2205.11062v1 (May 23, 2022), doi:10.1017/prm.2023.4. Publisher classification: primary MSC 55U05.
2. J. A. Barmak and E. G. Minian, *Minimal Finite Models*, arXiv:math/0611156v1 (November 6, 2006).
3. J. D. Wiltshire-Gordon, *Models for Configuration Space in a Simplicial Complex*, arXiv:1706.06626v1 (June 20, 2017).
4. *Two-point configurations of finite crowns retain the circle weak type*, published mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-two-point-configurations-of-finite-crowns-retain-the-circle-weak--1687da25925a .
5. *The two-point configuration of a minimal finite sphere has the same core*, published mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-two-point-configuration-of-a-minimal-finite-sphere-has-the-s--6aba10e53959 .
6. *Cartesian-product rigidity of cores of finite spaces*, published mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-cartesian-product-rigidity-of-cores-of-finite-spaces--cffeb409c28e .
