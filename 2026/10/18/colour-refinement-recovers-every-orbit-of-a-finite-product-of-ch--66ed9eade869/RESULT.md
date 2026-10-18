# Colour refinement recovers every orbit of a finite product of chains

## Finding
Let \(d\geq1\) and \(m_1,\ldots,m_d\geq2\) be integers, and let \(P=\prod_{i=1}^d\{0,\ldots,m_i-1\}\), regarded as a structure with **one strict binary relation** \(x<y\) if \(x_i\leq y_i\) in every coordinate and \(x\neq y\). Start bidirectional counting colour refinement with a single colour. Put \(H=\sum_i(m_i-1)\). After at most \(H+1\) rounds the colours are **exactly** the orbits of \(\operatorname{Aut}(P)\). More precisely, two vertices have the same colour if and only if for every factor length \(m\) they have the same multiset of coordinate values drawn from factors of length \(m\).

Writing \(r_m=|\{i:m_i=m\}|\), the exact number of stable classes is
\[
\prod_{m:r_m>0}\binom{r_m+m-1}{m-1}.
\]
For a class described by integers \(c_{m,a}\geq0\), with \(\sum_{a=0}^{m-1}c_{m,a}=r_m\), its cardinality is
\[
\prod_{m:r_m>0}\frac{r_m!}{\prod_{a=0}^{m-1}c_{m,a}!}.
\]

## Assumptions and scope
The factors are **nonempty finite chains of length at least two**, not Hasse graphs, and the input relation is the full **transitive strict order**. A refinement round recolours each point by its old colour together with multisets of colours of its strict predecessors and its strict successors. Including counts of incomparable points gives the same partition. A one-vertex product (\(d=0\)) is trivially a singleton but is not needed. The theorem concerns automorphism orbits within \(P\), **not identification of \(P\) among all finite posets** by two-variable counting logic.

## Proof
**1. Rank is available to refinement.** Set \(\rho(x)=\sum_i x_i\) and \(H=\sum_i(m_i-1)\). The unique bottom element has rank zero. For each integer \(s\geq0\), the assertion \(\rho(x)\geq s+1\) is equivalent to the existence of a strict predecessor \(y<x\) with \(\rho(y)\geq s\). Consequently the round-\(s\) partition separates vertices according to whether \(\rho(x)\geq s\), by induction on \(s\). By round \(H\), the exact rank of every vertex is recovered. This argument is the usual recursive two-variable formula with alternation of its bound variable; no numerical parameters from the displayed coordinates are supplied as unary colours.

**2. Principal-ideal and principal-filter cardinalities are visible.** At the first round (and hence subsequently), the colour of \(x=(a_i)_i\) determines its numbers of strict predecessors and successors. Define the *inclusive* sizes
\[
D(x)=1+|\{y:y<x\}|=\prod_i(a_i+1),\qquad
U(x)=1+|\{y:x<y\}|=\prod_i(m_i-a_i).
\]
Write \(b_i=m_i-1-a_i\); thus \(U(x)=\prod_i(b_i+1)\).

**3. The next round recovers each coordinate type by cover ratios.** At round \(H+1\), a vertex \(x\) knows the multiset of the previous-round triples \((\rho(y),D(y),U(y))\) for all \(y<x\), and similarly for all \(y>x\). In \(P\), the strict predecessors with rank \(\rho(x)-1\) are *exactly* the lower covers \(y=x-e_i\) for indices with \(a_i>0\). For each such cover,
\[
\frac{D(y)}{D(x)}=\frac{a_i}{a_i+1},\qquad
\frac{U(y)}{U(x)}=\frac{b_i+2}{b_i+1}.
\]
Both parameters are therefore recovered as integers:
\[
a_i=\frac{D(y)}{D(x)-D(y)},\qquad
b_i=\frac{U(x)}{U(y)-U(x)}-1.
\]
The multiset of these lower-cover ratios gives every pair \((a_i,b_i)\) for which \(a_i>0\), *including multiplicity*.

The strict successors with rank \(\rho(x)+1\) are precisely \(z=x+e_i\), for \(b_i>0\). For each upper cover,
\[
\frac{D(z)}{D(x)}=\frac{a_i+2}{a_i+1},\qquad
\frac{U(z)}{U(x)}=\frac{b_i}{b_i+1};
\]
hence
\[
a_i=\frac{D(x)}{D(z)-D(x)}-1,\qquad
b_i=\frac{U(z)}{U(x)-U(z)}.
\]
Retain exactly those upper-cover pairs with recovered \(a_i=0\). Every coordinate with \(a_i=0\) has \(b_i>0\), since \(m_i\geq2\), and appears exactly once among these selected upper covers. Thus the union of the lower-cover multiset and the selected upper-cover multiset reconstructs **all** coordinate pairs \((a_i,b_i)\). Since \(m_i=a_i+b_i+1\), it recovers the coordinate-value multiset separately for every chain length. This argument includes bottom, top, and mixed boundary vertices.

**4. These are precisely the automorphism orbits.** The join-irreducible elements of the product lattice form a disjoint union of chains, one of length \(m_i-1\) for each factor. Any poset automorphism preserves lattice joins and permutes these join-irreducible chains of equal length; such permutations induce all automorphisms of the product. Hence two vertices are in the same orbit exactly when their coordinates agree as multisets within each equal-length family. The refinement partition cannot split an automorphism orbit, while Step 3 shows that it cannot merge two different orbits. The stated bound and equality follow.

**5. Enumeration.** For every distinct length \(m\), a multiset of \(r_m\) values from \(\{0,\ldots,m-1\}\) is an \(m\)-part weak composition of \(r_m\), giving the binomial orbit count. Its orbit size is the corresponding multinomial coefficient. Factors of different lengths act independently, so the formulas multiply.

## Verification
Two independently coded exhaustive finite checks are supplied. `check_chain_products.py` tested 112 distinct factor multisets (9,403 total vertices, largest 216), checked exact stable colour/orbit equivalence and class-size formulas, and separately recovered every coordinate type using the four cover ratios; see `check_chain_products.log`. `check_group_orbits.py` tested 56 factor multisets (2,425 total vertices), comparing colours pairwise against the *explicit coordinate-permutation automorphism action*; see `check_group_orbits.log`.

The finite tests do not replace Steps 1–5. As a useful witness that even rank and first-round counts are sometimes insufficient, in the 24-element product \([2]\times[3]\times[4]\), the vertices \((0,2,1)\) and \((1,0,2)\) have equal rank \(3\) and equal inclusive ideal/filter sizes \(6,6\), yet are in different singleton automorphism orbits. The subsequent refinement does distinguish them. In \([3]\times[3]\times[4]\), 36 vertices fall into exactly 24 stable classes, not a discrete partition.

To reproduce: run `python3 check_chain_products.py` and `python3 check_group_orbits.py` in a directory containing the scripts. Both use only the Python standard library.

## Relationship to prior work
Duffus–Thayer (2012), Section 1, explicitly describe the coordinate-permutation automorphisms of arbitrary finite chain products and study symmetric-chain decompositions of their quotients. Their result justifies the familiar group side of Step 4; the **counting-refinement reconstruction in Steps 1–3 is a different statement** and is not a conclusion of symmetric-chain decomposition.

Kiefer–Schweitzer–Selman (2015), Sections 1 and 5, explain the interpretation of two-variable counting logic by colour refinement and classify structures identified by that logic. Arvind–Köbler–Rattan–Verbitsky (2015), Sections 1 and 8, investigate general relationships among colour refinement, automorphisms, and graph identification. Neither inspected treatment gives the all-dimension chain-product orbit-recovery formula or cover-ratio proof. The present statement also extends the special two-factor product and Boolean-product situations; it does **not** claim that such products are necessarily identified by counting logic.

## Limitations
The \(H+1\)-round bound is a general upper bound and need not be sharp. The theorem does not give an efficient coordinate recovery algorithm when the full order relation is not supplied, does not apply verbatim to arbitrary distributive lattices or to unordered comparability graphs, and does not assert identification against nonisomorphic structures. The literature comparison is not an independent priority or originality guarantee; specialized earlier coverage is possible. Independent scientific audit has not been performed.

## References
1. Dwight Duffus and Kyle Thayer, *Symmetric Chain Decompositions of Quotients of Chain Products by Wreath Products*, arXiv:1209.2579 (first version 12 September 2012), especially Introduction and Section 2. https://arxiv.org/abs/1209.2579
2. Sandra Kiefer, Pascal Schweitzer and Erkal Selman, *Graphs Identified by Logics with Counting*, arXiv:1503.08792 (30 March 2015), Sections 1, 2 and 5. https://arxiv.org/abs/1503.08792
3. V. Arvind, Johannes Köbler, Gaurav Rattan and Oleg Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255 (first public version 4 February 2015), Sections 1 and 8. https://arxiv.org/abs/1502.01255
