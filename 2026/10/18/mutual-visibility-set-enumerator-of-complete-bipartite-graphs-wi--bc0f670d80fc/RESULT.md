# Mutual-visibility set enumerator of complete bipartite graphs with a deleted matching

## Finding

Let \(a,b\ge 3\) and \(1\le t<\min\{a,b\}\) be integers. In a complete bipartite graph with named vertex classes \(A=\{a_1,\dots,a_a\}\) and \(B=\{b_1,\dots,b_b\}\), delete the matching \(\{a_i b_i:1\le i\le t\}\), obtaining \(G_{a,b,t}\). A set \(S\) is *mutually visible* when every two members admit a shortest connecting path whose internal vertices avoid \(S\). Set
\[
\mathcal V_{a,b,t}(z)=\sum_{S\ \mathrm{mutually\ visible}}z^{|S|}.
\]

There is a complete five-parameter classification, and hence the following explicit finite formula for every coefficient of this polynomial. For integers \(0\le x,y\le t\), \(\max\{0,x+y-t\}\le c\le\min\{x,y\}\), \(0\le u\le a-t\), and \(0\le v\le b-t\), put
\[
 p=x+u,\quad q=y+v,\quad r=a-p,\quad s=b-q,\quad e=t-x-y+c.
\]
Let \(\varepsilon(x,y,c,u,v)\) equal \(1\) precisely when all three conditions hold:
\[
\begin{aligned}
&\neg\bigl(p\ge2\ \land\ s\le2\ \land\ x-c=s\bigr),\\
&\neg\bigl(q\ge2\ \land\ r\le2\ \land\ y-c=r\bigr),\\
&\neg\bigl(c\ge1\ \land\ [r=0\ \lor\ s=0\ \lor\ (r=s=e=1)]\bigr).
\end{aligned}
\]
Then
\[
\boxed{\mathcal V_{a,b,t}(z)=
\sum_{x=0}^{t}\sum_{y=0}^{t}
\sum_{c=\max\{0,x+y-t\}}^{\min\{x,y\}}
\sum_{u=0}^{a-t}\sum_{v=0}^{b-t}
\varepsilon(x,y,c,u,v)
\frac{t!}{c!(x-c)!(y-c)!e!}
\binom{a-t}{u}\binom{b-t}{v}z^{p+q}.}
\]
The same predicate classifies every mutually visible subset: \(x\) and \(y\) count selected matched-side vertices, \(c\) counts selected complete matching-index pairs, and \(u,v\) count selected unmatched vertices on each side.

Moreover, the maximum possible size and its **exact multiplicity** are
\[
\boxed{\mu(G_{a,b,t})=a+b-2,\qquad
[z^{a+b-2}]\mathcal V_{a,b,t}(z)
=(a-t)(b-t)+\mathbf1_{\{t=1\}}\bigl(1+2\mathbf1_{\{a=3\}}+2\mathbf1_{\{b=3\}}\bigr).}
\]
Here \(\mathbf1\) is the indicator function. The formula supplies the entire distribution, not only the largest size.

## Assumptions and scope

Graphs are finite, simple, undirected, and vertex-labeled. The missing edges form a matching of size strictly smaller than both part sizes, so there is an untouched vertex on each side. The labels of the vertices matter for counting subsets, but the matching can be chosen as written without loss of generality. No restriction \(a\le b\) is needed. The formula is exact for all integers in the displayed range, not an asymptotic or numerical approximation. The boundary \(t=0\) (a complete bipartite graph) can be substituted into the counting predicate for comparison, but is not part of the new theorem's stated domain. The full-matching crown-graph case \(t=a=b\) is also outside the stated domain.

## Proof

**Distances and possible obstructions.** Since \(a,b\ge3\), any two distinct vertices in the same bipartition class have distance exactly two: at most two vertices in the opposite class fail to be common neighbors. All cross-class pairs are adjacent except the deleted pairs \(a_i,b_i\), whose distance is exactly three. To see the latter, take one untouched vertex from each opposite class as internal vertices; these untouched vertices are adjacent to one another.

Write \(I=\{i\le t:a_i\in S\}\), \(J=\{i\le t:b_i\in S\}\). Thus \(|I|=x\), \(|J|=y\), \(|I\cap J|=c\). Let the selected untouched vertices number \(u\) on the \(A\)-side and \(v\) on the \(B\)-side. The total selected-side sizes are \(p,q\); the numbers outside the selected set are \(r,s\). Exactly \(e=t-x-y+c\) matching indices have **both endpoints omitted**.

**Pairs in \(A\).** For distinct selected vertices \(a_i,a_j\), a length-two geodesic has middle vertex \(b_k\) adjacent to both. An unselected \(b_k\) can fail to be their common neighbor only if it is the deleted partner of one of these two selected vertices. Hence some selected pair of \(A\)-vertices fails mutual visibility exactly when there are at least two selected \(A\)-vertices and *all* \(s\) unselected \(B\)-vertices are deleted partners of at most two selected \(A\)-vertices. This is possible precisely when \(s\le2\) and \(x-c=s\): the \(x-c\) vertices are precisely the selected matched \(A\)-vertices whose deleted \(B\)-partners are unselected. If \(s=0\), any two selected \(A\)-vertices fail; if \(s=1\), take the matching endpoint and any other selected \(A\)-vertex; if \(s=2\), take the two matching endpoints. Conversely, when this condition does not hold, every selected \(A\)-pair has an unselected common neighbor. This is the first test in the predicate.

**Pairs in \(B\).** Interchanging the two classes gives the second test: every selected \(B\)-pair is visible if and only if it is not the case that \(q\ge2\), \(r\le2\), and \(y-c=r\).

**Cross-class pairs.** All present edges are automatically visible. The remaining selected cross-class pairs are exactly those \(a_i,b_i\) with \(i\in I\cap J\); there are \(c\) of them. Each such pair has distance three. Its middle two vertices must be an unselected \(B\)-vertex and an unselected \(A\)-vertex joined by an edge. Since both endpoints of the pair are selected, no other restriction affects the first and last edges of such a path. Thus a clean shortest path exists if and only if both omitted classes are nonempty and they are **not** singleton classes consisting of opposite endpoints of the same deleted matching edge. The forbidden cases are exactly \(r=0\), \(s=0\), or \(r=s=e=1\). When \(c=0\), no such cross-class condition is required. This proves the third test.

Together these tests are separately necessary and jointly sufficient for every selected pair to be mutually visible. This establishes the classification.

**Counting.** For fixed \(x,y,c\), partition the \(t\) named matching indices into four classes: selected on both sides (size \(c\)), selected only on the first side (size \(x-c\)), selected only on the second (size \(y-c\)), and selected on neither (size \(e\)). The multinomial factor in the formula counts those choices. Independently choose \(u\) among the \(a-t\) untouched \(A\)-vertices and \(v\) among the \(b-t\) untouched \(B\)-vertices. Every selected set has one and only one such record, and the indicator retains exactly the valid records. Multiplying by \(z^{p+q}\) proves every coefficient.

**Largest sets.** A mutually visible set cannot omit fewer than two vertices: otherwise one side is entirely selected and the other contains at least two selected vertices with no unselected common neighbor. Thus \(\mu\le a+b-2\). Omitting one untouched vertex from each side attains this bound: both omissions are universal to the opposite class, and every deleted selected cross-pair has a clean length-three path through the two omitted vertices. Hence \(\mu=a+b-2\).

To count equality cases, exactly two vertices must be omitted. If one is omitted from each side, any omitted matched vertex must have its deleted partner omitted as well, by the same-side-pair test. Therefore either both omissions are untouched (\((a-t)(b-t)\) choices) or the two omissions form one deleted matching pair. In the latter situation all other deleted pairs have both endpoints selected, so the two omitted vertices cannot form a length-three connecting path; this pattern is valid exactly when \(t=1\), giving one additional set.

If both omissions lie in \(A\), then all of \(B\) is selected. There can be at most one selected vertex in \(A\), forcing \(a=3\). When \(t=1\), either of the two untouched \(A\)-vertices may be that one selected vertex, giving two more sets. When \(t=2\), omitting the two matched \(A\)-vertices blocks visibility of their selected \(B\)-partners; all other choices either fail this test or leave a selected deleted cross-pair with no omitted \(B\)-vertex. Thus there are no such sets for \(t=2\). The symmetric case with both omissions in \(B\) contributes two precisely when \(b=3,t=1\). These disjoint cases exhaust equality and prove the leading coefficient.

**Deletion monotonicity.** For fixed \(a,b\), the sets represented by the polynomial are nested as one deletes additional edges of the same matching: deleting such an edge never adds a common neighbor for a same-class pair, never creates a new distance-three geodesic for an already deleted cross-pair, and replaces an originally adjacent cross-pair by a new condition. Thus \(\mathcal V_{a,b,t+1}\) is coefficientwise at most \(\mathcal V_{a,b,t}\) whenever both parameters lie in the stated range. This assertion concerns this family, not arbitrary edge deletion.

## Verification

The standalone `verify_visibility_matching.py` builds the actual graph, computes shortest-path distances by breadth-first search, and independently checks every selected vertex pair after removing all other selected vertices. It compares the resulting exact cardinality distribution with the five-index formula; **40** graph profiles with \(3\le a\le b\le6\) and \(0\le t<\min\{a,b\}\) were checked, encompassing **49,984** candidate subsets. It also carried out **210** additional algebraic parameter checks, over \(3\le a\le b\le11\) and \(1\le t<\min\{a,b\}\), of the degree, leading coefficient, and coefficientwise deletion monotonicity. The recorded output is `verification_output.txt`. Run `python verify_visibility_matching.py` with Python 3.10 or later from the directory containing both files.

For example, \(\mathcal V_{4,5,2}(z)=1+9z+36z^2+84z^3+125z^4+112z^5+49z^6+6z^7\). The exhaustive computation agrees coefficient by coefficient. Finite computations are corroboration, not a substitute for the unrestricted combinatorial proof.

## Relationship to prior work

Di Stefano introduced graph mutual visibility and determined \(\mu(K_{a,b})=a+b-2\) for \(a,b\ge3\) [1]. Bujtás, Klavžar, and Tian introduced the visibility polynomial and computed it for balanced complete bipartite graphs [2, Proposition 3.2]. Tonny and Shikhi also treated the complete bipartite polynomial for arbitrary sides [3, Theorem 14], while their subsequent paper studies additional families including wheels [4]. The complete perfect-matching-deleted crown-graph visibility polynomial is tabulated in [5]. These results cover either \(t=0\) or the perfect-matching boundary; they do not supply the present three-parameter structural classification for \(1\le t<\min\{a,b\}\). Related publicly indexed results on matching-deleted bicliques concern geodesic subpath counts or maximal-clique/stable-set intersections rather than mutual-visibility subset enumerators.

## Limitations

The graph sizes require \(a,b\ge3\), and the deletion must be a matching that leaves at least one untouched vertex on each side. The theorem does not assert an expression for arbitrary edge-deleted bicliques or other visibility variants (total, outer, or dual). This is a mathematical proof supported by exact finite checks; it does not imply that every possible mathematical repository has been searched. In particular, the publicly tabulated crown-graph result and less-indexed literature remain important bibliographic comparators.

## References

1. Gabriele Di Stefano, *Mutual Visibility in Graphs*, arXiv:2105.02722 (first posted 2021-05-06), later *Applied Mathematics and Computation* 419 (2022), 126850. https://arxiv.org/abs/2105.02722
2. Csilla Bujtás, Sandi Klavžar, Jing Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066 (2024). https://arxiv.org/abs/2412.03066
3. Tonny K. B. and Shikhi M., *On the Visibility Polynomial of Graphs*, arXiv:2507.01851 (2025), especially Theorem 14. https://arxiv.org/abs/2507.01851
4. Tonny K. B. and Shikhi M., *Visibility Polynomial of Some Graph Classes*, arXiv:2509.22571 (2025). https://arxiv.org/abs/2509.22571
5. OEIS A390404, *Number of mutual-visibility sets in the n-crown graph*, including the crown visibility polynomial attributed to Andrew Howroyd (2026). https://oeis.org/A390404
