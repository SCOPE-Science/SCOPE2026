# The 76 minimal-obstruction types for three ternary constancy disjuncts

## Finding
Let \(A=\{0,1,2\}\), let \(x,y,z\) be distinct variables, and evaluate
\[
\Phi=\operatorname{dep}(x)\lor\operatorname{dep}(y)\lor\operatorname{dep}(z)
\]
under lax team semantics on arbitrary teams \(T\subseteq A^3\). An **obstruction** is an inclusion-minimal team failing \(\Phi\). There are exactly **58,131** labelled obstructions, partitioned into exactly **76** isomorphism classes under arbitrary, independent renamings of the three coordinate value sets and permutations of the three coordinates. Their complete cardinality distribution is:

| Assignments in obstruction | Labelled obstructions | Isomorphism classes |
| ---: | ---: | ---: |
| \(5\) | \(54\) | \(1\) |
| \(6\) | \(3,672\) | \(10\) |
| \(7\) | \(36,612\) | \(41\) |
| \(8\) | \(17,793\) | \(24\) |
| **Total** | **58,131** | **76** |

There are no smaller or larger minimal obstructions. In particular, the least failing ternary team has **five** assignments, rather than the four assignments possible if four different values are allowed per coordinate. The unique isomorphism class at size five is represented by
\[
\{(0,0,0),(0,1,1),(1,0,1),(1,1,0),(2,2,2)\}.
\]
The attached `ORBIT_CLASSES.csv` specifies one canonical member and orbit size for *each* of the 76 classes, not merely their counts.

## Assumptions and scope
The coordinate symbols name no algebraic operations on \(A\); its elements are three distinct labels. A team is an ordinary *set* of assignments, without multiplicity. The dependence atom \(\operatorname{dep}(x)\) means that all members of its subteam assign the same value to \(x\). The empty subteam satisfies every constancy atom. The ternary disjunction is left- or right-associated arbitrarily: lax splitting semantics makes both equivalent. The result concerns exactly three named output variables, a three-element value set, and no additional formulas or constraints. The numbers do not claim any general classification for larger arities or alphabets.

Let \(H(t)\) for \(t\in A^3\) be the set of selectors
\[
H(t)=\{c\in A^3: c_1=t_1\ \text{or}\ c_2=t_2\ \text{or}\ c_3=t_3\}.
\]
A selector \(c\) represents the three coordinate hyperplanes used to split the team. Consequently,
\[
T\models\Phi\quad\Longleftrightarrow\quad\bigcap_{t\in T}H(t)\ne\varnothing,
\]
where the empty intersection is \(A^3\). A minimal obstruction is therefore exactly a set whose selector-set intersection is empty, while every single deletion makes the intersection nonempty.

Equivalently, regard \(A^3\) as the vertex set of the direct graph product of three copies of \(K_3\), with two triples adjacent precisely when they differ in every coordinate. The obstructions are exactly the inclusion-minimal **total dominating sets** of this 27-vertex graph. This translation is used for literature comparison, not as an independent new theorem.

## Proof
**Semantic reduction.** Suppose \(T\) admits a lax decomposition into three subteams, each constant in its respective variable. Choose that constant for each nonempty part, arbitrarily for an empty part. The resulting selector \(c\) lies in every \(H(t)\). Conversely, from a selector \(c\) in the intersection, collect all rows matching its first, second, or third coordinate value into the corresponding subteams. They cover \(T\) and satisfy the three constancy atoms. The graph interpretation follows by taking complements of the \(H(t)\).

**No minimal obstruction has more than eight rows.** Let \(S\) be a finite minimal obstruction. For each \(t\in S\), choose a selector \(c(t)\) covering \(S\setminus\{t\}\). Since \(S\) fails, \(t_i\ne c_i(t)\) for all three coordinates. Consider the multilinear polynomial
\[
P_t(X_1,X_2,X_3)=\prod_{i=1}^3(X_i-c_i(t))
\]
over \(\mathbb Q\), interpreting the three labels as \(0,1,2\). Evaluated on \(S\), \(P_t\) is nonzero at \(t\) but vanishes at every other row. Thus the \(|S|\) evaluation vectors of these polynomials are linearly independent. The vector space of polynomials separately of degree at most one in each variable has dimension eight; therefore \(|S|\le8\). This short rank argument is an upper-bound ingredient, not the new enumeration.

**No four rows can fail.** Given any four triples over \(A\), pigeonhole yields a coordinate having the same value in two rows. Cover those two with one coordinate hyperplane, and cover the other two rows using the other two coordinate hyperplanes. The same reasoning handles fewer rows. Hence every failing set has at least five rows.

**Five rows suffice.** Consider the displayed five-row team. Its four \(\{0,1\}\)-valued rows have even coordinate parity, hence their projection to any two coordinates contains all four binary pairs. If a selector uses \(2\) in some coordinate, the other two selector hyperplanes cannot cover those four rows. If it uses only \(0\) or \(1\) in all coordinates, the all-\(2\) row is uncovered. Hence the team fails, while every proper subteam is coverable by the preceding four-row argument.

**Finite exhaustive classification.** Index a labelled tuple \((a,b,c)\) by \(9a+3b+c\), an integer from \(0\) through \(26\). Its selector compatibility set \(H(t)\) is stored as a 27-bit mask. `ternary_constancy_census.cpp` enumerates every \(k\)-subset of the 27 vertices for each \(1\le k\le8\). For each, it computes the intersection of compatibility masks and all single-deletion intersections, using prefix and suffix intersections to avoid omission or redundant work. It records a subset precisely if the full intersection is empty and every single-deletion intersection is nonempty. This is an exact finite decision test of the definition, not sampling. The rank bound proves that all minimal obstructions occur within the enumerated range. Enumeration produces exactly the labelled counts in the table.

**Isomorphism classification.** The natural relabelling group is
\[
G=(S_3)^3\rtimes S_3,
\qquad |G|=6^3\cdot6=1296.
\]
The six within-coordinate generators (a transposition and a 3-cycle for each coordinate), together with one coordinate transposition and one coordinate 3-cycle, generate the entire group. The checker applies these eight generators to each enumerated minimal obstruction and performs an orbit traversal. The resulting orbit counts are \(1,10,41,24\), proving the asserted 76 classes. The program writes, under `--classes`, the 76 sorted triples `(team_size, canonical_mask, orbit_size)`. Here `canonical_mask` is the least 27-bit integer in its orbit, formatted in seven hexadecimal digits, and the set it represents consists of exactly those indexed tuples whose bits are one. The enclosed `ORBIT_CLASSES.csv` is that exact output. For each orbit the checker verifies that traversal stays within the enumerated minimal family, and the disjoint orbit sizes add to the labelled counts.

## Verification
Run the supplied standard C++17 source with a C++17 compiler supporting the usual optimized integer bit operations:

```sh
g++ -O3 -std=c++17 ternary_constancy_census.cpp -o census
./census
./census --classes > reproduced_classes.csv
diff -u ORBIT_CLASSES.csv reproduced_classes.csv
python3 verify_size5.py
```

The complete run checks respectively \(\binom{27}{k}\) candidates for \(k=1,\ldots,8\). The size-eight layer contains \(2,220,075\) distinct subsets. Its total is \(58,131\) minimal failing sets in 76 orbits; the independent Python neighborhood-union calculation (rather than the selector-intersection calculation) reproduces the \(54\) size-five obstructions. The code and complete orbit-list artifact are packaged with this result. The mathematical proof of exhaustiveness combines a proved size bound with complete finite enumeration; the finite checker is not represented as a proof of an unrelated infinite-domain assertion.

## Relationship to prior work
Fröhlich, Kolaitis, and Meier prove the four-element coherence threshold for **two** constancy disjuncts in their 2025 preprint / CSL 2026 paper (Corollary 23) and analyze disjunctions of two general dependence atoms (Theorems 22–30). Barlag and collaborators' 2026 paper develops the general coherence framework and explicitly treats disjunctions of multiple constancy atoms in complexity reductions (Theorem 5.4), but neither inspected paper lists the minimal ternary three-attribute obstructions or classifies them by relabelling orbits. The general eight-row obstruction bound is accessible by a multilinear rank argument and does not itself determine the enumeration. Classical total-domination terminology supplies the graph-theoretic equivalent, but no exact census of this particular direct product was identified in the checked sources. The claim is the **finite, domain-sensitive complete orbit census**, not the general constancy-disjunction coherence theorem.

## Limitations
This is an exact finite classification for a fixed natural 27-vertex object, not an asymptotic statement, a new general coherence theorem, or a complexity dichotomy. The executable and class-list certify the stated finite calculations subject to the correctness of the straightforward bitmask implementation and group generators; the separate independent count checks the smallest layer only. Equivalent enumerations may exist in older, poorly indexed literature on graph products or database constraints, so priority should be independently checked before publication. No external independent scientific audit has been performed.

## References
1. N. Fröhlich, P. G. Kolaitis, and A. Meier, *Disjunctions of Two Dependence Atoms* (first posted 22 August 2025), arXiv:2508.16146; CSL 2026, DOI: 10.4230/LIPIcs.CSL.2026.10. https://arxiv.org/abs/2508.16146 ; https://drops.dagstuhl.de/storage/00lipics/lipics-vol363-csl2026/html/LIPIcs.CSL.2026.10/LIPIcs.CSL.2026.10.html
2. T. Barlag, N. Fröhlich, M. Hannula, P. G. Kolaitis, J. Kontinen, A. Meier, and J. Väänänen, *Aspects of Coherence in Dependence Logic* (first posted 29 May 2026), arXiv:2605.31269. https://arxiv.org/abs/2605.31269
3. M. A. Henning, *A survey of selected recent results on total domination in graphs*, Discrete Mathematics **309** (2009), 32–63, for the standard total-domination terminology and product context; no exact 27-vertex obstruction table is attributed to this source.
