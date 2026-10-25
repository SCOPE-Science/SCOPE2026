# A gap-free size spectrum and exact enumerator of multipartite subset repairs

## Finding
Let \(r\ge 2\) and let \(V=V_1\sqcup\cdots\sqcup V_r\) be a finite labelled partition with \(|V_i|=a_i\ge1\) and \(n=\sum_i a_i\). Form the binary relation \(T\) consisting of **all ordered cross-part pairs** \((u,v)\) with \(u\in V_i\), \(v\in V_j\), and \(i\ne j\). Consider the integrity constraints
\[
\operatorname{dep}(x;y):\quad (x,y),(x,z)\in P\Longrightarrow y=z,
\qquad
x\subseteq y:\quad \pi_x(P)\subseteq\pi_y(P).
\]
Here a *repair* is an inclusion-maximal subset \(P\subseteq T\) satisfying both constraints, and its size is its number of tuples.

**Structural classification.** The repairs are precisely the subrelations representing permutations on nonempty supports \(S\subseteq V\) whose permutation arrows connect distinct parts, and whose omitted set \(V\setminus S\) is either empty or contained in one part. Equivalently, if \(s_i=|S\cap V_i|\), then the necessary and sufficient support conditions are
\[
\sum_i s_i>0,\qquad
2\max_i s_i\le\sum_i s_i,
\qquad
\#\{i:s_i<a_i\}\le1.
\]

**Exact polynomial.** For any vector \(\boldsymbol s\) of nonnegative integers, put \(s=\sum_i s_i\) and define
\[
D(\boldsymbol s)=\sum_{0\le j_i\le s_i}
(-1)^{\sum_i j_i}\bigl(s-\sum_i j_i\bigr)!
\prod_{i=1}^r\binom{s_i}{j_i}^{\!2}j_i!.
\]
This counts labelled permutations of a support with part sizes \(\boldsymbol s\) that send every element to a *different* part, with \(D(\boldsymbol 0)=1\) by convention. Writing \(\boldsymbol e_i\) for the coordinate unit vector, the repair-size enumerator is
\[
\boxed{\displaystyle
R_{\boldsymbol a}(z)=
D(\boldsymbol a)z^n+
\sum_{i=1}^r\sum_{t=1}^{a_i}
\binom{a_i}{t}D(\boldsymbol a-t\boldsymbol e_i)z^{n-t}.}
\]
Zero-valued terms automatically exclude impossible supports; no empty repair is counted, since \(r\ge2\).

**Sharp, gap-free spectrum.** Relabel the parts so that \(a_1\ge a_2\ge\cdots\ge a_r\), and set \(b=n-a_1\). The support of the polynomial consists of every *consecutive integer* in the interval
\[
\boxed{\displaystyle
\{\,|P|:P\text{ is a repair}\,\}=
\{L,L+1,\ldots,U\},\qquad
L=\max\{b,2a_2\},\qquad U=\min\{n,2b\}.}
\]
In particular, all inclusion-maximal repairs of a complete bipartite instance have exactly \(2\min\{a_1,a_2\}\) tuples, whereas three or more parts can admit an entire interval of sizes.

For example, for \((a_1,a_2,a_3)=(3,2,2)\), the exact polynomial is
\[
R_{(3,2,2)}(z)=4z^4+48z^5+384z^6+288z^7.
\]

## Assumptions and scope
The universe is finite and *labelled*, \(r\ge2\), and every part is nonempty. The relation contains both orientations for every cross-part unordered edge, but neither loops nor within-part pairs. The constraints are exactly one source-to-target functional dependency and one source-in-target inclusion dependency; no other constraints or tuple insertions are permitted. The same object can be read as a finite team on variables \(x,y\) satisfying a dependence atom and an inclusion atom. Inclusion maximality refers to subsets of the **original** relation \(T\), not largest cardinality and not edit distance. The formula counts distinct sets of ordered tuples, not isomorphism classes. No claim is made for asymmetric relations, general database schemas, arbitrary dependencies, or quotienting by permutations of world labels.

## Proof
**1. Consistent subsets are partial directed cycle covers.** Let \(P\subseteq T\) satisfy the functional dependency and put \(S=\pi_x(P)\). Each \(u\in S\) has exactly one outgoing tuple, so \(P\) is the graph of a function \(f:S\to V\) and \(|P|=|S|\). The inclusion dependency says \(S\subseteq\pi_y(P)=f(S)\). The finite sets obey \(|f(S)|\le|S|\), hence equality throughout: \(f(S)=S\), and \(f\) is a bijection \(S\to S\). Because \(P\subseteq T\), every arrow crosses the partition. Therefore nonempty consistent sets are precisely collections of pairwise vertex-disjoint directed cycles, with each arrow crossing parts. Conversely, every such partial permutation satisfies both constraints.

**2. Inclusion-maximality detects one omitted part.** Fix such a partial permutation on \(S\). Any consistent strict extension \(P'\supsetneq P\) must preserve every existing outgoing tuple by functionality. By the argument in step 1, its additional tuples form a permutation on a nonempty subset of the unused vertices \(V\setminus S\). If two unused vertices lie in different parts, the two reverse cross-part tuples form a disjoint directed two-cycle that can be added. Hence such a \(P\) cannot be maximal. Conversely, if all unused vertices lie in one part, no nonempty cycle can be formed entirely from them, so no extension exists. This proves the maximality characterization, including the case of no unused vertices. Since \(r\ge2\), the empty set is never maximal: it can be extended by a two-cycle.

**3. Exact existence of an allowed permutation on a support.** Write \(s=|S|>0\) and \(m=\max_i s_i\). Because each vertex in part \(i\) must have an image outside that part, \(s_i\le s-s_i\), and thus \(2m\le s\) is necessary. Conversely, if \(2m\le s\), arrange the \(s\) vertices around a circle so that each part occupies a consecutive block (of length at most \(m\)). Define a permutation by sending the vertex in cyclic position \(h\) to the vertex in cyclic position \(h+m\pmod s\). The two cyclic separations between those positions have lengths \(m\) and \(s-m\), both at least \(m\). No part occupies more than \(m\) consecutive positions; therefore the source and image cannot lie in the same part. This constructs the needed permutation. Combining steps 1–3 proves the three stated support conditions.

**4. Exact enumeration.** Given a labelled support with part occupancy vector \(\boldsymbol s\), start from the \(s!\) permutations of \(S\) and exclude all forbidden arrows whose source and image lie in the same part. In part \(i\), the number of ways to specify \(j_i\) pairwise nonattacking forbidden arrows is \(\binom{s_i}{j_i}^2j_i!\). Because these forbidden blocks have disjoint row and column sets, multiply their rook counts and apply inclusion-exclusion. With \(j=\sum_i j_i\) fixed forbidden arrows, there are \((s-j)!\) completions. This proves exactly the displayed formula for \(D(\boldsymbol s)\).

By step 2, every repair either uses all vertices or omits exactly \(t\ge1\) labelled vertices, all in a unique part \(i\). For fixed \(i,t\), choose the omitted set in \(\binom{a_i}{t}\) ways, then choose one of \(D(\boldsymbol a-t\boldsymbol e_i)\) allowed permutations on the retained support. These families are disjoint, proving the polynomial formula. No inclusion-exclusion across omitted-part families is needed.

**5. Every intermediate cardinality, and sharp endpoints.** Sort parts by \(a_1\ge a_2\ge\cdots\). Consider repairs that omit vertices *only from the largest part* \(V_1\); the zero-omission option is allowed. Let \(u\) be the number retained in \(V_1\), so that all \(b=n-a_1\) vertices outside it are retained and the support size is \(b+u\). Step 3 gives the exact conditions
\[
0\le u\le a_1,\qquad u\le b,\qquad 2a_2\le b+u.
\]
Consequently, these repairs realize exactly all integers from \(\max\{b,2a_2\}\) through \(b+\min\{a_1,b\}=\min\{n,2b\}\), with no gaps.

For the reverse inclusion, any repair omits vertices from at most one part. It retains at least \(n-a_1=b\) vertices, since no part is larger than \(a_1\). If it omits from \(V_1\), the balance bound for the untouched second-largest part gives total size at least \(2a_2\), and its size is at most \(2b\) by balancing retained largest-part vertices against the other \(b\). If it omits from some other part, it retains *all* \(a_1\) vertices of \(V_1\), so the balance condition forces its total size to be at least \(2a_1\ge2a_2\). Such a repair is possible only if \(a_1\le n/2\), in which case \(n\le2b\), so the claimed upper bound is simply \(n\). Thus **every** repair size lies in the interval already realized by largest-part omissions. This proves the exact spectrum and completes the theorem.

## Verification
Run `python3 checker.py` using Python 3.10 or later; it uses only the standard library. The checker implements the displayed inclusion-exclusion, independently counts all allowed permutations on supports of up to six vertices, independently enumerates all possible subrelations and tests inclusion-maximality for the smallest profiles, and independently enumerates partial functions satisfying both constraints for additional profiles. It checks the polynomial and exact interval for every integer partition of total size two through seven into at least two positive parts. The observed output was:

```
ALL_CHECKS_OK
multipartite_profiles= 37
forbidden_permutation_subprofiles= 1131
independent_powerset_repair_checks= 7
independent_function_assignment_checks= 35
example_(3,2,2)= [(4, 4), (5, 48), (6, 384), (7, 288)]
```

The finite checks are regression evidence only; steps 1–5 constitute the proof for all permitted parameters.

## Relationship to prior work
Mahmood, Virtema, Barlag and Ngonga Ngomo (2026) develop an argumentation-theoretic account of subset repairs for functional and inclusion dependencies and broader constraints, extending their 2024 construction. The present instance belongs to that general integrity-constraint setting but asks a different, quantitative question: classify every maximal repair's labelled tuples, enumerate them by size, and determine whether possible repair sizes have gaps. Neither the inspected 2026 open-access text nor the inspected 2024 paper states this multipartite cycle-cover result. General complexity and correspondence theorems do not specify its size enumerator or sharp support interval.

Kimelfeld, Livshits and Peterfreund (2020) investigate counting and enumeration for **preferred** database repairs in the presence of priorities, especially under functional dependencies. Their published counting dichotomies and algorithms concern a different constraint/instance regime; no inspected claim gives the polynomial for a simultaneous functional and inclusion dependency on an all-cross-part relation.

The established theorem *Paired-domination polynomial of complete multipartite graphs* (published mathematical result) characterizes balanced even-cardinality support sets that admit undirected perfect matchings. Its balance lemma overlaps the necessity of a part-size bound in step 3, but its polynomial does not count directed permitted permutations, odd-length cycles or inclusion-maximal repairs. In particular, it does not imply the displayed size enumerator or gap-free interval. The inclusion-exclusion step is the classical rook-polynomial method for forbidden positions and is not claimed as a new counting technique. The originality claim is the **combined repair classification, exact labelled repair polynomial, and interval theorem** for this dependency-specified multipartite family.

## Limitations
These formulas require the complete **bidirected** cross-part relation and exactly the two specified constraints. In particular, they do not extend merely by replacing the relation with an arbitrary multipartite digraph. The counts are labelled, not up to graph or database isomorphism. There is a remaining literature-priority risk of an equivalent theorem stated as a maximal partial cycle-cover or block-restricted partial-permutation enumeration in older combinatorics work. Independent validation of priority and proof has not been performed.

## References
1. Y. Mahmood, J. Virtema, T. Barlag and A.-C. Ngonga Ngomo, “Inconsistent Databases and Argumentation Frameworks with Collective Attacks,” arXiv:2605.03954v1 (first public 2026-05-05), https://arxiv.org/abs/2605.03954 ; open-access journal text: https://www.maxapress.com/article/id/6a422088fa6c5874a0a1a9e6 .
2. Y. Mahmood, J. Virtema, T. Barlag and A.-C. Ngonga Ngomo, “Computing Repairs Under Functional and Inclusion Dependencies via Argumentation,” arXiv:2312.01973 (first public 2023-12-04), later FoIKS 2024, https://eprints.whiterose.ac.uk/id/eprint/211186/ .
3. B. Kimelfeld, E. Livshits and L. Peterfreund, “Counting and Enumerating Preferred Database Repairs,” *Theoretical Computer Science* 837 (2020), 115–157, https://doi.org/10.1016/j.tcs.2020.05.016 .
4. “Paired-domination polynomial of complete multipartite graphs,” published RESULT.md, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-paired-domination-polynomial-of-complete-multipartite-graphs--ea2bc935cbba .
