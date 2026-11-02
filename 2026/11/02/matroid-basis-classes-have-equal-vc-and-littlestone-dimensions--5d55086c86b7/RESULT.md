# Matroid basis classes have equal VC and Littlestone dimensions

## Finding

Let \(M\) be any finite matroid on a ground set \(E\), let \(M^*\) be its dual, and regard the family \(\mathcal B(M)\) of all bases as a Boolean concept class on \(E\) with membership queries. Then

\[
\operatorname{VCdim}(\mathcal B(M))
=\operatorname{Ldim}(\mathcal B(M))
=\max\{|S|:S\subseteq E,\ S\text{ independent in both }M\text{ and }M^*\}
=\min_{A\subseteq E}\bigl(r_M(A)+r_{M^*}(E\setminus A)\bigr).
\]

The common value is computable in polynomial time using matroid intersection (given an independence oracle), and an optimal deterministic online mistake strategy needs no dynamically recomputed version-space dimensions: choose a minimizing set \(A\) above, predict \(0\) for previously unseen elements of \(A\), predict \(1\) for previously unseen elements of \(E\setminus A\), and memorize each revealed label for repeated elements. This incurs at most the displayed common value of mistakes against any fixed unknown basis, for every query sequence.

For a finite connected graph \(G\), its graphic matroid gives the concrete specialization

\[
\operatorname{VCdim}(\mathcal T(G))=\operatorname{Ldim}(\mathcal T(G))
=\max\{|F|: F\subseteq E(G),\ F\text{ is a forest},\ G-F\text{ is connected}\},
\]

where \(\mathcal T(G)\) is the family of spanning-tree edge sets. Loops and parallel edges are permitted in the matroid statement; for the graph interpretation the same formula works for finite connected multigraphs, with the conventional definitions of cycles and forests.

## Assumptions and scope

A finite matroid is a nonempty family of equicardinal subsets, called bases, obeying basis exchange. Independence means containment in some basis. The dual matroid \(M^*\) has bases \(E\setminus B\) for \(B\in\mathcal B(M)\), and \(r_M\) denotes matroid rank. The VC dimension is the maximum size of a fixed subset \(S\) on which all \(2^{|S|}\) Boolean traces occur. The Littlestone dimension (also called thicket dimension) is the maximum depth of a complete binary decision tree whose internal nodes label elements of \(E\) and every root-to-leaf binary answer sequence is realized by some basis. A decision-tree query can depend on earlier answers; repeated queries are allowed in the definition but cannot occur twice along any path of a fully shattered tree. The depth of the single-leaf tree is zero. An online learner sees the queried element, guesses membership in a single unknown target basis, then sees its true label; the realizable worst-case mistake bound is minimized over deterministic learners and maximized over targets and query sequences. Finite ground sets include the empty set, for which each stated dimension is zero.

## Proof

**Step 1: fixed-coordinate shattering is exactly primal-dual independence.** Suppose \(S\subseteq E\) is shattered by bases. An all-one trace supplies a basis containing \(S\), so \(S\) is independent in \(M\). An all-zero trace supplies a basis disjoint from \(S\), whose complement is a dual basis containing \(S\), so \(S\) is independent in \(M^*\).

Conversely, suppose \(S\) is independent in both matroids. Fix an arbitrary binary trace represented by \(T\subseteq S\), the positions to be labelled one, and put \(D=S\setminus T\). Since \(D\) is independent in \(M^*\), some basis \(B_0\) of \(M\) is disjoint from \(D\). Thus the deletion \(M\setminus D\) has the same rank as \(M\). The set \(T\) is independent in the deletion because \(T\cap D=\varnothing\) and independence is hereditary under deletion. Extend \(T\) to a basis \(B\) of \(M\setminus D\). Its full rank makes \(B\) a basis of \(M\), and \(B\cap S=T\). This proves all traces occur, hence

\[
\operatorname{VCdim}(\mathcal B(M))=\max\{|S|:S\in\mathcal I(M)\cap\mathcal I(M^*)\}.
\]

**Step 2: a universal bound on adaptive shattering.** Fix an arbitrary partition \(E=A\sqcup(E\setminus A)\) and a shattered binary tree of depth \(d\). Follow its unique branch replying \(1\) whenever a node queries an element in \(A\), and \(0\) for elements of \(E\setminus A\). No element can appear twice on this path: a repeated query would make one of the two children after the repeat incompatible with the earlier answer, contradicting full shattering. Thus the path queries \(d\) distinct elements. A basis \(B\) witnesses the realized full branch. The path's \(1\)-queries constitute an independent subset of \(B\cap A\), of size at most \(r_M(A)\). The \(0\)-queries constitute an independent subset of the dual basis \(E\setminus B\) restricted to \(E\setminus A\), of size at most \(r_{M^*}(E\setminus A)\). Therefore

\[
d\le r_M(A)+r_{M^*}(E\setminus A)
\]

for every \(A\). Taking the minimum bounds Littlestone dimension. Every statically shattered \(S\) supplies a depth-\(|S|\) shattered tree by querying its elements in a fixed order, so \(\operatorname{Ldim}\ge\operatorname{VCdim}\).

**Step 3: sharpness by a classical min-max theorem.** Edmonds' matroid intersection theorem states, for any two matroids \(M_1,M_2\) on the same finite ground set,

\[
\max\{|S|:S\in\mathcal I(M_1)\cap\mathcal I(M_2)\}
=\min_{A\subseteq E}\bigl(r_{M_1}(A)+r_{M_2}(E\setminus A)\bigr).
\]

Applying it to \(M\) and \(M^*\) identifies the upper and lower bounds in Steps 1 and 2. This matroid intersection identity is an established theorem, not a novel contribution.

**Step 4: an optimal fixed-sign mistake strategy.** Take \(A\) attaining the minimum in Step 3. On each coordinate's first appearance, predict \(0\) on \(A\) and \(1\) outside, and on later appearances use its known label. For any target basis \(B\), each first-appearance mistake within \(A\) occurs on a point of \(B\cap A\), at most \(r_M(A)\) such points. Each mistake outside \(A\) occurs on a point of \((E\setminus B)\cap(E\setminus A)\), at most \(r_{M^*}(E\setminus A)\) such points. The total mistake bound equals the common dimension. Conversely, a shattered tree of that depth lets an adversary always return the opposite of each learner prediction; all branches admit a compatible final basis. Hence the worst-case realizable mistake bound is exactly this common dimension. The bound covers arbitrary query order, repetitions, loops, and coloops.

**Step 5: graphic specialization.** For a connected graph, independence in its graphic matroid means acyclicity, while independence of \(F\) in the dual means that a graphic basis, namely a spanning tree, avoids \(F\), equivalently that \(G-F\) is connected. Substituting into the equality proves the graph formula.

## Verification

The supplied pure-standard-library program `verify_matroid_bases.py` exhaustively generates all nonempty equal-rank basis families on labeled ground sets of orders \(0\) through \(5\) and filters them using the basis-exchange axiom. It compares four quantities calculated from definitions: static VC shattering, recursive online Littlestone dimension, largest primal-dual common independent-set size, and the minimum primal-dual rank-cut value. The labeled matroid counts are \(1,2,5,16,68,406\), totaling \(498\). It also independently enumerates spanning trees of \(K_3,K_4,K_5\), finding respectively \(3,16,125\) bases and dimensions \(1,3,4\). Invoke `python3 verify_matroid_bases.py`. These finite checks corroborate but do not replace the universal proof, which uses the classical matroid intersection theorem.

## Relationship to prior work

Bhaskar's *Thicket Density* (first public submission 2017-02-13) develops the thicket/Littlestone shattering formalism and supplies background on adaptive shattering. Manurangsi and Rubinstein (2017) study computational hardness of determining these dimensions for general explicitly presented concept classes; the present structured matroid-basis family has a polynomial-time exact formula. Edmonds' matroid intersection rank minimax is classical and is the decisive existing ingredient in Step 3. General matroid-basis online optimization over losses, as studied for example by Buchbinder and colleagues (2012), uses a different prediction model from identifying an unknown fixed basis through binary membership labels. Engström, Sanyal and Stump (2022) study standard complexes of the 0/1 basis configuration, including duality, but their accessible abstract does not assert the present combined VC/Littlestone formula. Full historical-priority certification has not been established, and the early literature on graph set-system VC dimension could contain a static graphic special case.

## Limitations

The statement is exact for matroid **basis** concepts, not arbitrary independent sets, general set systems, non-realizable/noisy online data, or online regret with adversarial losses. The algorithm assumes the matroid can be supplied via an independence oracle (or another representation admitting polynomial-time independence tests), so computational complexity depends on oracle costs. The lower bound is the standard realizable deterministic worst-case adversarial mistake bound. The matroid intersection theorem is imported as prior knowledge. Small-matroid exhaustive tests do not certify the theorem for larger ground sets. No claim is made that the result has independent verification or exhaustive historical-priority clearance.

## References

- S. Bhaskar, *Thicket Density*, arXiv:1702.03956, first posted 2017-02-13, https://arxiv.org/abs/1702.03956 .
- J. Edmonds, *Submodular Functions, Matroids, and Certain Polyhedra* (1970); the exact rank-minimax formula and polynomial algorithm are given in *Matroid Intersection*, Theorem 8.3.2, https://extremalcombinatorics.com/optimization/notes/sec_matroidIntersection.html .
- P. Manurangsi and A. Rubinstein, *Inapproximability of VC Dimension and Littlestone's Dimension*, 2017, https://proceedings.mlr.press/v65/manurangsi17a/manurangsi17a.pdf .
- Y. Bérczi, T. Király, Y. Yamaguchi and Y. Yokoi, *Matroid Intersection under Restricted Oracles*, arXiv:2209.14516, https://arxiv.org/abs/2209.14516 .
- N. Buchbinder, S. Chen, J. Naor and O. Shamir, *Unified Algorithms for Online Learning and Competitive Analysis*, 2012, https://jmlr.csail.mit.edu/proceedings/papers/v23/buchbinder12/buchbinder12.pdf .
- A. Engström, R. Sanyal and C. Stump, *Standard Complexes of Matroids and Lattice Paths*, 2022, https://link.springer.com/article/10.1007/s10013-021-00546-z .
