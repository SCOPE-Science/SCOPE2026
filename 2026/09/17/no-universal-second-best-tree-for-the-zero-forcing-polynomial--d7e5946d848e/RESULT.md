# No universal second-best tree for the zero forcing polynomial

> **Review status: same-model review.** Correctness, originality and value were assessed by the same-model review, not an independent reviewer. Originality is claimed only to the best of our knowledge; consult REVIEW.md for search evidence and inaccessible sources. Publication is not peer review or a guarantee of priority.

## Claim

All graphs here are finite, simple and undirected. A zero forcing process starts with a set of blue vertices; a blue vertex with exactly one white neighbor may color that neighbor blue. A set is zero forcing if this process can color every vertex. Write

\[
z(G;k)=|\{S\subseteq V(G): |S|=k,\ S\text{ is zero forcing}\}|,
\qquad Z(G;x)=\sum_{k=0}^{|V(G)|}z(G;k)x^k.
\]

For graphs of the same order, write \(G\preceq H\) when \(z(G;k)\le z(H;k)\) for every \(k\). Let \(S(a,b,c)\) be the tree consisting of a center and three internally disjoint arms of lengths \(a,b,c\), measured in edges (equivalently, in noncentral vertices).

**Theorem.** For every integer \(n\ge11\), the nonpath trees on \(n\) vertices have no greatest element under \(\preceq\). More explicitly, put

\[
A_n=S(2,2,n-5),\qquad B_n=S(2,4,n-7).
\]

For every nonpath tree \(T\) on \(n\) vertices, there are \(U\in\{A_n,B_n\}\) and \(k\in\{2,3,n-4\}\) such that \(z(T;k)<z(U;k)\).

Equivalently, no nonpath tree simultaneously maximizes the probability that a uniformly chosen \(k\)-vertex set is zero forcing, for all \(k\). After identifying trees with equal zero forcing polynomials, the finite poset of nonpath trees has at least two maximal elements. In the poset of all trees of order \(n\), there are therefore at least two coatoms below the path. These assertions concern the tree subposet, not the poset of all graphs. They do not identify all maximal elements or assert that both displayed witnesses are maximal.

## Motivation and prior boundary

Menon and Singh [1, Proposition 3.13] prove that concatenating two paths hanging at the same vertex weakly increases every coefficient of the zero forcing polynomial. Their Corollary 3.14 gives strict path domination of nonpath trees for the indicated small cardinalities, and their Section 4 asks about the polynomial poset and its coatoms below the path. The present problem is an inferred, restricted residual of that discussion: does the tree subposet have a single universal runner-up? It is not presented in [1] as that exact conjecture.

The result answers this residual negatively for every \(n\ge11\). It gives a fixed pair of witnesses and three cardinalities sufficient to defeat any proposed runner-up. The source transformation reduces the issue to spiders but does not compare spiders with three arms. The proof below resolves that remaining competition between small forcing sets and small fort obstructions. No optimality of the threshold 11 is claimed.

## Proof

### 1. Reduction to three arms

We use the following established result of [1, Proposition 3.13]. If paths \(a_1,\ldots,a_p\) and \(b_1,\ldots,b_q\) hang at a vertex \(v\), deleting \(vb_1\) and adding \(a_pb_1\) produces a graph \(G'\) with \(G\preceq G'\). Here the terminal vertices are leaves and all other vertices of the hanging paths have degree two. The source proves this by an injection between forcing sets of each cardinality.

Every tree with more than three leaves has a branch vertex with two hanging paths: root at any branch vertex and take a branch vertex farthest from the root; if it is the root, all its branches are hanging paths. Apply the transformation at such a vertex. It preserves the order and the tree property and decreases the number of leaves by exactly one. Repeating until three leaves remain gives

\[
T\preceq S(a,b,c),\qquad a,b,c\ge1,\quad a+b+c=n-1.
\tag{1}
\]

Indeed, the degree identity \(L=2+\sum_{\deg(v)\ge3}(\deg(v)-2)\) shows that a three-leaf tree has exactly one vertex of degree three and no higher-degree vertices.

### 2. Two low coefficients of a spider

We will use

\[
z(S(a,b,c);2)=9-2t,\qquad t=|\{i:a_i=1\}|,
\tag{2}
\]

where \((a_1,a_2,a_3)=(a,b,c)\), and, when all three arms have length at least two,

\[
z(S(a,b,c);3)=13n-66+2r,\qquad r=|\{i:a_i=2\}|.
\tag{3}
\]

Equation (2) is already in the proof of Boyer et al. [2, Theorem 22, Claim 4]. The argument also covers \(t=0\), although the displayed range for their parameter omits zero. We give a counting derivation including this case; no originality is claimed for (2).

Let \(I_m(x)\) be the independence polynomial of the path with \(m\) vertices, with \(I_{-1}(x)=I_0(x)=1\). Number an arm's vertices \(1,\ldots,l\) outward from the center. Call an initially chosen subset of this arm active if it contains vertex \(l\) or contains two consecutive vertices. An active arm can color its entire arm and the center without any force from the center. If it is inactive, it has neither of these features and cannot make a first force while the center is white.

For \(l\ge2\), partition inactive arm subsets according as vertex 1 is absent or present, with generating polynomials

\[
E_l=I_{l-2},\qquad D_l=xI_{l-3}.
\]

Write \(P_l=(1+x)^l\) and \(Q_l=P_l-E_l\). The sets counted by \(Q_l\) are precisely active sets and inactive sets containing vertex 1. Once the center is blue, either type can finish coloring its arm without a force from the center. An \(E_l\) arm cannot do so. For length one, the same classification uses \(E_1=1,D_1=0,Q_1=x\).

If the center is initially blue, success occurs exactly when at least two arms are of type \(Q\): the center can supply the remaining arm, but cannot start two unfinished arms. If the center is initially white, the same condition is necessary, and at least one arm must also be active to start the process. These conditions are sufficient by first completing the active arm, then the other \(Q\) arms, and finally any remaining arm using the center. Thus, with indices running through the three arms, set

\[
H=Q_aQ_bQ_c+Q_aQ_bE_c+Q_aQ_cE_b+Q_bQ_cE_a,
\]
\[
J=D_aD_bD_c+D_aD_bE_c+D_aD_cE_b+D_bD_cE_a.
\]

Here \(J\) counts the center-white cases with at least two \(Q\) arms but no active arm. The full polynomial is

\[
Z(S(a,b,c);x)=(1+x)H-J.
\tag{4}
\]

For length one, \([x]Q_l=1,[x]D_l=0\); for every other length, these coefficients are 2 and 1. All \(E_l\) have constant term 1; all \(Q_l,D_l\) have constant term 0. Consequently the degree-two coefficient in (4) is
\(\sum_{i<j}([x]Q_i[x]Q_j-[x]D_i[x]D_j)=9-2t\), proving (2).

Now suppose every arm has length at least two. Directly from the independent-set counts on a path,

\[
[x]E_l=l-2,\quad [x]Q_l=2,\quad
[x^2]Q_l=3l-6+\mathbf1_{l=2},
\]
\[
[x]D_l=1,\qquad [x^2]D_l=l-3+\mathbf1_{l=2}.
\]

For example, \([x^2]E_l\) counts nonadjacent pairs in the \((l-2)\)-vertex path; the indicator accounts for the boundary case \(l=2\). Substituting and using \(a+b+c=n-1\) gives

\[
[x^2]H=12,\quad [x^3]H=16n-104+4r,
\quad [x^2]J=3,\quad [x^3]J=3n-26+2r.
\]

For clarity, the cubic terms in \(H\) are \(8+4\sum_l(3l-6+\mathbf1_{l=2})+4\sum_l(l-2)\); those in \(J\) are \(1+2\sum_l(l-3+\mathbf1_{l=2})+\sum_l(l-2)\). Equation (4) now proves (3).

### 3. A high coefficient distinguishes the competing spiders

A fort is a nonempty set \(F\) such that no vertex outside \(F\) has exactly one neighbor in \(F\). A set \(S\) is zero forcing if and only if its complement contains no fort. For completeness, a process cannot make its first force into a disjoint fort: the forcing vertex would have at least two white neighbors in the fort. Conversely, when an exhaustive forcing process stops without coloring everything, its nonempty white set is a fort. This standard duality also appears in [4,5].

In \(A_n\), the four vertices on its two length-two arms form a fort: the center has two neighbors in it, and every other outside vertex has zero. Therefore

\[
z(A_n;n-4)<\binom n4.
\tag{5}
\]

We claim that \(B_n=S(2,4,n-7)\) has no fort of size at most four. Its last two arms have length at least four. The following elementary bounds verify the claim.

If the center is outside a fort, every nonempty intersection with an arm of length \(l\) contains both the first vertex and the leaf. Otherwise the predecessor of its first vertex, or the successor of its last vertex, is outside the fort with exactly one neighbor in it. Between those endpoints there cannot be two consecutive vertices outside the fort, since the outside vertex bordering the fort would have exactly one neighbor in it. Thus a nonempty arm intersection has size at least \(\lceil(l+1)/2\rceil\). At least two arms have nonempty intersections, because the center cannot have exactly one fort neighbor. In \(B_n\) this requires at least \(2+3=5\) vertices.

If the center is in a fort, every arm must end in a fort vertex, and, along the path starting at the center, no two consecutive vertices can be outside the fort. Otherwise the first outside vertex of such a run has exactly one fort neighbor; a terminal outside run is also impossible. Hence the arm of length \(l\) contributes at least \(\lceil l/2\rceil\) vertices. The total in \(B_n\), including the center, is at least \(1+1+2+2=6\). This proves the claim, and consequently

\[
z(B_n;n-4)=\binom n4.
\tag{6}
\]

These fort estimates are elementary consequences of the fort definition, consistent with the stronger minimal-fort description in [4, Theorem 17]; they are not a separate novelty claim.

### 4. Completion

Given \(T\), choose a dominating spider \(C=S(a,b,c)\) from (1). If an arm of \(C\) has length one, (2) gives
\(z(T;2)\le z(C;2)<9=z(A_n;2)\).

Otherwise all arms have length at least two. For \(n\ge11\), at most two arms have length two. If fewer than two do, (3) gives
\(z(T;3)\le z(C;3)<13n-62=z(A_n;3)\).

If exactly two do, \(C\) is isomorphic to \(A_n\). Equations (5)-(6) then give
\(z(T;n-4)\le z(A_n;n-4)<z(B_n;n-4)\).
This proves the explicit theorem, and thus nonexistence of a greatest nonpath tree.

In a finite poset, a unique maximal element is a greatest element, since every element lies below a maximal element. Quotienting by equality of polynomials makes \(\preceq\) a poset, so at least two maximal nonpath classes exist. The path dominates every tree by continued path concatenation, and is distinguished from nonpaths by its positive degree-one coefficient. Thus these maximal nonpath classes are exactly the coatoms in the tree poset. Finally the uniform-cardinality probability is \(z(T;k)/\binom nk\), proving the probability reformulation. This does not assert the analogous statement for independent Bernoulli sampling of vertices.

## Reproducible checks

Run `python3 output/artifacts/spider_check.py` from the workspace. It uses only the Python standard library. The analytic proof above applies to every stated order; computation is a check, not the basis of the quantifier over all orders.

The script enumerates all initial sets and applies the color-change rule. A second implementation enumerates forts directly from their defining adjacency predicate and checks the complement-obstruction equivalence for every initial set. It compares the complete coefficient vector with (4) for all 41 nonisomorphic three-arm spiders of orders 4 through 12, including length-one arms and balanced arms. It checks (2)-(3), and separately compares path counts with [2, Proposition 5] for every coefficient at orders 2 through 12. All checks passed.

Additional full-polynomial and fort checks for the witnesses produced:

| n | z(A;3) | z(B;3) | z(A;n-4) | z(B;n-4) = binomial(n,4) | minimum fort sizes A/B |
|---|---:|---:|---:|---:|---:|
| 11 | 81 | 79 | 329 | 330 | 4 / 5 |
| 12 | 94 | 92 | 494 | 495 | 4 / 5 |
| 13 | 107 | 105 | 714 | 715 | 4 / 5 |
| 14 | 120 | 118 | 1000 | 1001 | 4 / 5 |
| 15 | 133 | 131 | 1364 | 1365 | 4 / 5 |

## Relationship to existing results and limitations

The claimed contribution is the incompatibility theorem, with (3) providing the needed low-cardinality extremal comparison. It is not the known path maximum, the known two-vertex spider count, or the known fort duality. Equation (4) is supplied to make the counting proof transparent; no priority claim is made for a general arm-state enumeration technique.

[1, Proposition 3.13] yields a dominating three-arm spider but loses the comparison when another merge makes a path. Its proof does not choose a best three-arm spider. [2, Theorem 22, Claim 4] supplies (2), in a proof about recognizing cycle polynomials; (2) alone leaves every spider with all arms at least two tied. [3, Theorem 1] establishes path domination for the larger class of distance-hereditary graphs, and Theorem 2 gives a conditional split-decomposition extension. Those path comparisons do not determine the second level after excluding paths.

[4, Theorem 17 and proof] describes and counts minimal forts of spiders. [5, Theorem 1] bounds the total number of minimal forts in trees and forests, while its Lemma 4 characterizes individual minimal forts. Specializing [4] also supplies the small-fort distinction used above, but counts of minimal forts do not determine the number of fixed-cardinality sets intersecting all forts. The remaining step is the low-coefficient optimization forcing \(S(2,2,n-5)\), followed by its incompatibility with that distinction. The examples in *Minimal Zero Forcing Sets*, arXiv:2204.01810v2, Propositions 2-3, concern counts of inclusion-minimal sets, not simultaneous maxima of all coefficients.

The contribution is a narrow extremal result, not a classification of all coatoms or a resolution of the path-extremal conjecture for arbitrary graphs. Its value is that it rules out a universal runner-up throughout an infinite family of orders and isolates the conflicting cardinalities. This document and the audit are one researcher's same-model assessment, not independent validation.

## Originality scope and inaccessible sources

To the best of our knowledge, within the documented search scope and accessible literature, no equivalent or stronger prior result was found. This is not an exhaustive guarantee of novelty.

**ACCESS_LIMITATION:** Baoxin Li, Yahan Cao and Shengjin Ji (2025), *The Extremal Results for Forcing Problem of Trees*, DOI [10.1007/s00373-025-02925-6](https://doi.org/10.1007/s00373-025-02925-6). Its tree-extremal subject makes it a possible threat to the exact claim. Full text was not obtained through available channels: acquisition job `480a2d6ff25b698cf17026f2fc9b5887` discovered a Springer PDF link, but CORE and OA-location acquisition produced no usable content, and OpenAlex metadata timed out. A final DOI request with paid fallback permitted returned the same failed acquisition. The recorded metadata item is `s5dd07a6212324ebd`. Available snippets concern extremal minimum cardinalities of forcing, connected forcing and total forcing sets; they provide only possible relevance, not concrete evidence of coefficientwise coverage. Whether the full text contains any relevant counting theorem remains unverified. This limitation is not a finding of noncoverage. A later covering source would require revision of the assessment.

## References and evidence locations

1. Krishna Menon and Anurag Singh, *Exploring the influence of graph operations on zero forcing sets*, DOI [10.1016/j.disc.2025.114516](https://doi.org/10.1016/j.disc.2025.114516). Inspected arXiv:2405.01423v1; Proposition 3.13, Corollary 3.14, Section 4. Full-text job `95c8c4887e7a937cd31cf8806c3b1775`, relevant extracted offsets 20500-27000 and 28900-30000.
2. K. Boyer et al., *The zero forcing polynomial of a graph*, Discrete Applied Mathematics 258 (2019), 35-48, DOI [10.1016/j.dam.2018.11.033](https://doi.org/10.1016/j.dam.2018.11.033). Inspected arXiv:1801.08910v1; Proposition 5; Theorem 22, Claim 4. Job `05560c8432ef7af3eb354f67337e676e`, offsets around 13500 and 44600-46500.
3. German, *The Path-Extremal Conjecture for Zero Forcing: Distance-Hereditary Graphs and a Split-Decomposition Reduction*, [arXiv:2605.10836](https://arxiv.org/abs/2605.10836), 2026. Theorems 1-2 and proofs. Job `ed5480dcbcb1a023b7876a05ec4d0960`, inspected offsets 14500-38000.
4. Paul Becker, Thomas R. Cameron, Derek Hanely, Boon Ong and Joseph P. Previte, *On the number of minimal forts of a graph*, Graphs and Combinatorics 41 (2025), 25, DOI [10.1007/s00373-025-02891-z](https://doi.org/10.1007/s00373-025-02891-z). Inspected arXiv:2404.05963v1, Theorem 17 and proof. Job `0be79076b50a5fed80ccf51d7148bb7c`, offsets 28200-32400.
5. Nguyen Hoang Dat and Franklin H. J. Kenter, *On the Number of Zero Forcing Minimal Forts on Trees*, [arXiv:2605.07298v1](https://arxiv.org/abs/2605.07298), May 2026. Theorem 1 and Lemma 4 with proof. Job `6deb40844af4a9a932b8287b661ab9b9`, offsets 0-6500 and 16500-21900.

Source theorem numbering refers to the inspected versions, which need not be identical to final publisher versions. Further search scope and the residual beyond prior consequences are recorded in REVIEW.md.
