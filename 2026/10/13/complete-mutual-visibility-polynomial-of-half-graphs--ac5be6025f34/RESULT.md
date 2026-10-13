# Complete mutual-visibility polynomial of half graphs

## Finding
For each integer \(n\ge3\), the **half graph** \(H_n\) has vertex classes \(\{a_1,\ldots,a_n\}\) and \(\{b_1,\ldots,b_n\}\), and the edge \(a_i b_j\) exists precisely when \(i\le j\). A subset \(S\) is a **mutual-visibility set** if every two distinct selected vertices have a shortest path whose internal vertices are unselected. The **visibility polynomial** \(\mathcal V_n(z)\) counts such sets by cardinality.

Put \(s=1+z\). For integers \(1\le q,p\le n\), define
\[
F_{q,p}(z)=
\begin{cases}
z^2s^{q-1+n-p},&q<p,\\[2pt]
z^2\bigl(s^{q-1}-z^ps^{q-p-1}\bigr)
\bigl(s^{n-p}-z^{n-q+1}s^{q-p-1}\bigr),&q>p,\\[2pt]
z^2s^{n-1}-z^{n-p+2}(s^{p-1}-1)
-z^{p+1}(s^{n-p}-1)
+\mathbf 1_{\{2\le p\le n-1\}}z^{n+1},&q=p.
\end{cases}
\]
Then the **complete all-cardinality formula** is
\[
\boxed{\mathcal V_n(z)=2(1+z)^n-1+\sum_{q=1}^{n}\sum_{p=1}^{n}F_{q,p}(z).}
\]
It has the following exact consequences (the maximum-size/uniqueness statements were obtained previously and are included here only for consistency):
\[
\boxed{\mathcal V_n(1)=\frac{4^{n+1}+24n-13}{9},\qquad
\deg\mathcal V_n=2n-2,\qquad [z^{2n-2}]\mathcal V_n(z)=1.}
\]
The previously established unique maximum mutual-visibility set is all vertices **except** \(a_1\) and \(b_n\). The new claims are the complete polynomial and its closed total-set count, not this maximum-size fact.

## Assumptions and scope
Graphs are finite, simple, undirected and unweighted. The theorem concerns the connected half graphs \(H_n\) for every integer \(n\ge3\); the indeterminate \(z\) marks selected vertices and the empty set contributes one. The terms with \(q<p\), \(q=p\), and \(q>p\) are polynomial expressions, with nonnegative exponents throughout their stated ranges. This is **existential geodesic visibility**, not the stronger requirement defining general-position sets. The formula is a finite expression, not a computational approximation.

## Proof
**1. Pairwise geodesics.** Write \(A=\{i:a_i\in S\}\) and \(B=\{j:b_j\in S\}\). Vertices \(a_i,a_k\) have distance two and common neighbors precisely \(b_j\) for \(j\ge\max\{i,k\}\). Vertices \(b_j,b_l\) have distance two and common neighbors precisely \(a_i\) for \(i\le\min\{j,l\}\). A mixed pair \(a_i,b_j\) is adjacent when \(i\le j\); otherwise it has distance three. For \(i>j\), its geodesics are precisely paths
\[
a_i-b_k-a_l-b_j\qquad (k\ge i,\ l\le j),
\]
because \(l\le j<i\le k\) makes every indicated edge present. Such a pair is visible with respect to \(S\) precisely when there is an omitted \(b_k\) with \(k\ge i\) **and** an omitted \(a_l\) with \(l\le j\).

If either \(A\) or \(B\) is empty, all selected pairs on the remaining side have an unselected common neighbor. The contribution from these two, overlapping at the empty set, is \(2s^n-1\).

Suppose both sides are nonempty, and set \(q=\max A\), \(p=\min B\). This boundary pair is unique. If \(q<p\), every mixed pair is adjacent; the omitted vertices \(b_q\) and \(a_p\) respectively provide a geodesic between any same-side selected pair. Therefore every choice with boundaries \(q,p\) works.

If \(q>p\), the mixed selected pair \(a_q,b_p\) is nonadjacent. Its visibility requires an omitted \(a_l\) with \(l\le p\) and an omitted \(b_k\) with \(k\ge q\). Conversely, these two omissions witness visibility for **all** selected nonadjacent mixed pairs, because each selected \(a_i\) has \(i\le q\) and each selected \(b_j\) has \(j\ge p\). The same omitted vertices also witness all same-side pairs. Hence these two missing-interval conditions are simultaneously necessary and sufficient.

If \(q=p=t\), all selected mixed pairs are adjacent. A same-side pair from \(A\), if one exists, requires an omitted vertex in the \(B\)-suffix \(\{t,\ldots,n\}\). Such a witness does not exist exactly when **all** that suffix is selected. Similarly, a same-side pair from \(B\) requires an omitted vertex in the \(A\)-prefix \(\{1,\ldots,t\}\). Thus precisely two kinds of failures must be excluded: \(|A|\ge2\) together with selection of every \(b_t,\ldots,b_n\), and \(|B|\ge2\) together with selection of every \(a_1,\ldots,a_t\).

**2. Weighted counting.** For \(q<p\), the boundary vertices \(a_q,b_p\) are selected and the other \(q-1+n-p\) eligible vertices are unrestricted. This gives \(z^2s^{q-1+n-p}\). For \(q>p\), after selecting \(a_q\), the choices below \(q\) number \(s^{q-1}\), but those containing the entire prefix through \(p\) contribute \(z^p s^{q-p-1}\) and are forbidden. Likewise, after selecting \(b_p\), the choices above \(p\) number \(s^{n-p}\), but those containing the entire suffix from \(q\) contribute \(z^{n-q+1}s^{q-p-1}\) and are forbidden. Independence between the two sides gives the stated product.

For \(q=p=t\), the unrestricted boundary choices contribute \(z^2s^{n-1}\). The first failure from Step 1 contributes \(z^{n-t+2}(s^{t-1}-1)\), the second contributes \(z^{t+1}(s^{n-t}-1)\). Their intersection consists of one set, with \(n+1\) selected vertices, exactly when \(2\le t\le n-1\). Inclusion-exclusion gives the diagonal formula. Distinct boundary pairs cannot overlap, so their sum and the empty-side contribution prove the polynomial identity.

**3. Total number of sets.** Substituting \(z=1\), the empty-side, \(q<p\), and \(q=p\) contributions respectively become
\[
2^{n+1}-1,\qquad (n-2)2^{n-1}+1,\qquad (n-4)2^{n-1}+3n.
\]
For \(q>p\), put \(d=q-p\) and \(k=n-d\). Summing the products of the two side counts at \(z=1\) gives
\[
\sum_{k=1}^{n-1}4^{n-k-1}\bigl((k-2)2^{k+1}+k+4\bigr).
\]
The two geometric-arithmetic sums in this expression are respectively
\[
-(n-1)2^n \quad\text{and}\quad \frac{4^{n+1}-3n-13}{9}.
\]
Adding all four contributions and cancelling the powers of two gives \(\mathcal V_n(1)=(4^{n+1}+24n-13)/9\), as asserted.

**4. Maximum sets.** Any mutual-visibility set of size \(2n-1\) would contain at least two vertices on each side and all vertices of one side. Same-side selected pairs on the opposite side could not have an unselected common neighbor, so this is impossible. For a set of size \(2n-2\), omitting both vertices from the same class also fails: if \(n\ge4\), the other class is full and the incomplete class has at least two selected vertices; if \(n=3\), the incomplete class has one selected vertex, which either prevents visibility of the pair \(b_1,b_j\) (or its symmetric counterpart) or makes a nonadjacent mixed pair without an available internal vertex. More uniformly, in the first exceptional case \(n=3\) with \(B\) full and \(|A|=1\), visibility of the \(B\)-pairs requires \(a_1\) omitted, so the unique selected \(a_i\) satisfies \(i>1\), and the mixed pair \(a_i,b_1\) has no omitted \(B\)-vertex. The reversed case is symmetric.

Therefore a size-\(2n-2\) set must omit one vertex from each class, say \(a_h,b_k\). Since both selected parts have size at least two, their same-side pairs require \(k\ge q=\max A\) and \(h\le p=\min B\). The first condition excludes \(k=1\) because \(q\ge2\); hence \(p=1\), forcing \(h=1\). Thus \(q=n\), forcing \(k=n\). Conversely, omitting \(a_1,b_n\) satisfies the two missing-interval conditions for \(q=n>p=1\), so it is feasible. The maximum cardinality is \(2n-2\) and its set is unique. This completes the proof.

## Verification
The standalone file `verify.py` constructs \(H_n\) directly and, for each selected set, checks existence of a shortest connecting path with no selected interior by breadth-first search. This definition-based checker is compared with the boundary criterion, and the full coefficient arrays are compared with a separate implementation of the displayed counting formula. The exhaustive test covers **87,360 subsets** across every \(n\) from 3 to 8. For every \(n\) from 3 to 50 the program also compares the polynomial's coefficient sum with the stated total-count formula and tests the top three coefficient positions and the first three coefficients. Exact captured results are in `verification_output.txt`. Execute `python3 verify.py` using Python 3; no external dependencies are required. These finite checks support, but do not replace, the proof for arbitrary \(n\).

## Relationship to prior work
Di Stefano introduced mutual visibility on graphs and established the maximum number for complete bipartite graphs, along with other families [1]. Cicerone and Di Stefano's work on distance-hereditary graphs provides a general optimization algorithm rather than a cardinality enumerator [2]. Bujtás, Klavžar, and Tian introduced visibility polynomials and evaluated them on complete bipartite graphs [3]; Tonny and Shikhi later treated general complete bipartite graphs and several graph operations [4,5]. A half graph is not a complete bipartite graph: its nested-neighborhood ordering changes precisely which length-two and length-three geodesics remain available. The complete half-graph polynomial and its closed total count do not follow from those complete-bipartite formulas. The maximum cardinality and uniqueness for this half-graph family were established separately before this enumeration and are not claimed as new. The relationship is by related definitions, not claimed equality or novelty of the foundational invariant.

## Limitations
The theorem is restricted to the canonical half graph with one vertex per neighborhood level, not all chain graphs with repeated neighborhood twins. Its counting formulas do not classify visibility polynomials of arbitrary bipartite graphs. Literature comparison cannot rule out an unindexed equivalent formula or a derivation implicit in a broader combinatorial model. No independent external audit or mathematical certification has been performed.

## References
[1] G. Di Stefano, *Mutual Visibility in Graphs*, arXiv:2105.02722, first posted 2021-05-06, https://arxiv.org/abs/2105.02722 .

[2] S. Cicerone and G. Di Stefano, *Mutual-visibility in distance-hereditary graphs: a linear-time algorithm*, arXiv:2307.10661 (2023), https://arxiv.org/abs/2307.10661 .

[3] C. Bujtás, S. Klavžar and J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066 (2024), https://arxiv.org/abs/2412.03066 .

[4] K. B. Tonny and M. Shikhi, *On the Visibility Polynomial of Graphs*, arXiv:2507.01851 (2025), https://arxiv.org/abs/2507.01851 .

[5] K. B. Tonny and M. Shikhi, *Visibility Polynomial of Some Graph Classes*, arXiv:2509.22571 (2025), https://arxiv.org/abs/2509.22571 .
