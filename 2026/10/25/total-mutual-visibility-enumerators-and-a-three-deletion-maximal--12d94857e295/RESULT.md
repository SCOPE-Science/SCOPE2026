# Total mutual-visibility enumerators and a three-deletion maximality transition in matching-deficient bicliques

## Finding

Let \(p,q\ge3\) and \(1\le t<\min\{p,q\}\). Delete a matching of \(t\) edges from \(K_{p,q}\) to form \(G_{p,q,t}\). For \(r\ge3\), put
\[
 F_{r,t}(z)=(1+z)^r-z^r-tz^{r-1}-\binom{t}{2}z^{r-2}.
\]
The **complete bipartition-refined total mutual-visibility polynomial**, counting each total mutual-visibility set by its numbers of selected vertices in the two parts, is
\[
 \mathcal T_{p,q,t}(x,y)=F_{p,t}(x)F_{q,t}(y).
\]
The total number of such sets is
\[
 \bigl(2^p-1-t-\binom t2\bigr)\bigl(2^q-1-t-\binom t2\bigr).
\]
Writing \(u=p-t\), \(v=q-t\), and \(c=\binom t3\), the complete polynomial of **inclusion-maximal** total mutual-visibility sets is
\[
 \mathcal M_{p,q,t}(x,y)
 =\bigl(u x^{p-1}+c x^{p-3}\bigr)
  \bigl(v y^{q-1}+c y^{q-3}\bigr).
\]
In particular there are \((u+c)(v+c)\) inclusion-maximal sets. Every maximum set has \(p+q-2\) vertices. If \(t\le2\), every inclusion-maximal set has this size; if \(t\ge3\), their possible sizes are exactly \(p+q-2\), \(p+q-4\), and \(p+q-6\), in multiplicities \(uv\), \(c(u+v)\), and \(c^2\), respectively. Hence the **lower total mutual-visibility number** jumps down by four at the third deleted edge:
\[
 \mu_{\mathrm t}^{-}(G_{p,q,t})=
 \begin{cases}p+q-2,&t\le2,\\p+q-6,&t\ge3.\end{cases}
\]
The upper total mutual-visibility number remains \(\mu_{\mathrm t}(G_{p,q,t})=p+q-2\). Thus, for \(t\ge3\), inclusion-maximal sets of three distinct sizes occur, with a two-unit gap between consecutive sizes.

For example, \(G_{6,6,3}\) has \(3249\) total mutual-visibility sets, and its inclusion-maximal cardinality polynomial is \(9z^{10}+6z^8+z^6\).

## Assumptions and scope

All graphs are finite, simple, and undirected. Label the two bipartition classes \(A=\{a_1,\ldots,a_p\}\) and \(B=\{b_1,\ldots,b_q\}\); the removed edges are exactly \(a_i b_i\) for \(1\le i\le t\). The unmatched vertices are \(U_A=\{a_{t+1},\ldots,a_p\}\) and \(U_B=\{b_{t+1},\ldots,b_q\}\), both nonempty by hypothesis. The graph is connected and has distance two between any distinct vertices of the same part, and distance three between the endpoints of a deleted edge.

A set \(S\subseteq V(G)\) is **total mutual-visible** when for *every* two vertices \(a,b\) of \(G\), not merely vertices of \(S\), at least one shortest \(a,b\)-path has no internal vertices in \(S\). An inclusion-maximal such set cannot be enlarged by adding any vertex. The polynomial \(\mathcal T\) sums \(x^{|S\cap A|}y^{|S\cap B|}\) over all such \(S\); \(\mathcal M\) sums the same monomial over inclusion-maximal such \(S\). Here \(\mu_{\mathrm t}\) is the *largest* size, and \(\mu_{\mathrm t}^{-}\) the *smallest size among inclusion-maximal sets*.

The theorem concerns proper, nonempty matching deletions; the undeleted biclique and full perfect-matching crowns are not included. It makes no claim about ordinary mutual-visibility sets, which require visibility only between selected vertices.

## Proof

**1. Exact visibility test.** Put \(X=A\setminus S\) and \(Y=B\setminus S\). We prove that \(S\) is total mutual-visible if and only if
\[
 (X\cap U_A\ne\varnothing\quad\text{or}\quad|X|\ge3),
 \qquad
 (Y\cap U_B\ne\varnothing\quad\text{or}\quad|Y|\ge3).
 \tag{1}
\]
Indeed, for distinct \(a_i,a_j\in A\), every shortest path between them has length two, and its possible middle vertices are all of \(B\) except \(b_i\) if \(i\le t\) and \(b_j\) if \(j\le t\). Thus every pair from \(A\) admits a shortest path with its middle vertex outside \(S\) if \(Y\) contains one unmatched vertex, or at least three vertices of any kind. Conversely, if \(Y\) contains no unmatched vertex and at most two matched vertices, choose two distinct vertices of \(A\) whose missing partners cover \(Y\) (when \(Y\) has one matched vertex, use its partner and any other vertex of \(A\); when \(Y\) is empty, any pair suffices). That pair has no admissible middle vertex. The case of two vertices in \(B\) is symmetric, giving both necessary conditions in (1).

For completeness, (1) also guarantees visibility of every opposite-part pair. Adjacent pairs have a one-edge geodesic. If \(a_i b_i\) is a deleted edge, its shortest paths have the form \(a_i-b_j-a_k-b_i\), with distinct matched exclusions \(j\ne i\), \(k\ne i\), and an existing middle edge \(a_kb_j\). If \(Y\) contains an unmatched vertex, choose that \(b_j\), and choose any \(a_k\in X\setminus\{a_i\}\), which exists by (1) because an unmatched \(X\)-vertex is not \(a_i\), or \(|X|\ge3\). If \(Y\) has no unmatched vertex, choose \(b_j\in Y\setminus\{b_i\}\), with at least two choices, and choose \(a_k\in X\setminus\{a_i\}\) different from the mate of \(b_j\); the latter exists because either \(X\) contains an unmatched vertex or it has at least three matched vertices. This constructs the required three-edge path with both internal vertices outside \(S\). Therefore (1) is necessary and sufficient for *all* vertex pairs, not merely pairs at distance two.

**2. Factorized enumeration.** In each part, a set of omitted vertices \(X\) is permitted precisely if it has an unmatched vertex or contains at least three vertices. The only forbidden omissions are subsets of the \(t\) matched vertices of sizes \(0,1,2\). Choosing all subsets of an \(r\)-vertex part and subtracting these disallowed subsets gives \(F_{r,t}(z)\), where the exponent counts *selected*, not omitted, vertices. Conditions on \(A\) and \(B\) are independent, so the full bivariate generating function factors. Evaluation at \(x=y=1\) gives the total count.

**3. Inclusion-maximal classification.** Adding vertices to \(S\) removes them from \(X\) or \(Y\). Thus \(S\) is inclusion-maximal if and only if both \(X\) and \(Y\) are inclusion-minimal among allowed omitted sets. The minimal allowed subsets of a part are exactly a singleton unmatched vertex (\(r-t\) choices) or a three-element set of matched vertices (\(\binom t3\) choices). The two parts can be chosen independently. A singleton omitted vertex leaves \(r-1\) selected vertices and a three-element omission leaves \(r-3\). Multiplying these two weighted possibilities gives \(\mathcal M\). Expanding the product yields the three cardinality layers and their exact multiplicities. Because \(p-t,q-t>0\), the largest layer \(p+q-2\) always occurs; for \(t\ge3\) every layer has positive multiplicity, giving smallest layer \(p+q-6\). This proves the asserted extremal values and gap.

## Verification

The accompanying `verify.py` constructs the graph for every \(3\le p,q\le5\) and every \(0\le t\le\min(p,q)\), independently enumerates shortest paths with breadth-first search, tests the definition against every vertex subset, tests inclusion maximality, and compares all coefficients against the formulas. It additionally compares the membership test (1) on all subsets. These \(41\) parameter instances, including boundary controls outside the claimed scope, pass. This finite test is independent corroboration; the proof above establishes the infinite family.

## Relationship to prior work

Cicerone, Di Stefano, Klavžar, and Yero (arXiv:2210.07835, first released 2022-10-14) introduced total mutual-visibility sets in the setting of strong graph products. Brešar and Yero (arXiv:2307.02951, 2023) introduced and studied the lower total mutual-visibility number. Bujtás, Klavžar, and Tian (arXiv:2412.03066, first released 2024-12-04) give a general distance-two/common-neighborhood characterization (Theorem 5.2) and total-visibility polynomials for the **undeleted** balanced complete bipartite graphs (Proposition 3.2); the general criterion is a previously known tool, not claimed as new. The 2026 OEIS entry A390404 by Howroyd counts ordinary mutual-visibility sets of **full-matching** deleted crown graphs, a different visibility notion and a boundary family excluded here. The present assertion is the exact product enumeration and the complete inclusion-maximal spectrum for a **proper nonempty partial matching deletion**.

## Limitations

Only \(p,q\ge3\) with \(1\le t<\min(p,q)\) are claimed. The formula is not a new general criterion for arbitrary graph total mutual-visibility. Its novelty is conditional on published and indexed evidence examined: unpublished or differently indexed results could overlap. Existing full-crown ordinary mutual-visibility counts and the undeleted balanced-biclique case should not be conflated with the asserted total mutual-visibility enumeration. The verification script is exhaustive only for the stated finite test domain, not a substitute for the infinite proof. No independent mathematical audit has been performed.

## References

1. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, “Mutual-visibility in strong products of graphs via total mutual-visibility,” arXiv:2210.07835 (initial version 2022-10-14). https://arxiv.org/abs/2210.07835
2. B. Brešar, I. G. Yero, “Lower (total) mutual visibility in graphs,” arXiv:2307.02951 (initial version 2023-07-06). https://arxiv.org/abs/2307.02951
3. C. Bujtás, S. Klavžar, J. Tian, “Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets,” arXiv:2412.03066 (initial version 2024-12-04), especially Proposition 3.2 and Theorem 5.2. https://arxiv.org/abs/2412.03066
4. A. Howroyd, “Visibility polynomial of the n-crown graph,” OEIS A390404, referenced January 2026. https://oeis.org/A390404
