# Exact four-fold total-domination witnesses of the Heawood graph

## Finding
Let \(H\) be the Heawood graph, the bipartite incidence graph of the Fano plane. Label four total dominating sets \(T_1,T_2,T_3,T_4\) by the distinct names \(1,2,3,4\), and require every vertex of \(H\) to belong to **exactly two** of them. There are exactly
\[
1{,}016{,}064=1008^2
\]
such ordered four-tuples. All four sets are distinct in every tuple, so there are exactly
\[
42{,}336=1008^2/24
\]
unordered families of four sets satisfying the same condition.

More precisely, consider a seven-point Fano-plane labeling assigning a two-element subset of \([4]\) to each point, with the union of the three labels on every Fano line equal to \([4]\). There are exactly \(1008\) such labelings. Every one of them uses all six two-element subsets of \([4]\), with exactly one subset used twice and each other subset once. The duplicated subset occupies an unordered pair of points; the third point on their line has its complementary subset. For each choice of duplicated point pair and duplicated label, exactly eight completions exist. Furthermore, all \(1008\) labelings form one orbit under Fano-plane collineations and permutations of \([4]\).

## Assumptions and scope
The Fano plane is the incidence structure with points the seven nonzero vectors of \(\mathbb F_2^3\) and lines \(\{u,v,u+v\}\) for distinct nonzero vectors \(u,v\). The Heawood graph has fourteen distinguishable vertices, one for each Fano point and one for each Fano line, with incidence as adjacency. A subset \(T\subseteq V(H)\) is *total dominating* when every vertex has a neighbor in \(T\), including vertices inside \(T\). The four sets are named in the first count and unlabelled in the second; they are not assumed disjoint. Distinctness is proved, not assumed.

A \((4{:}2)\)-labeling is a function \(c:V(H)\longrightarrow\binom{[4]}2\). It is *admissible* if
\[
\bigcup_{u\in N_H(v)}c(u)=[4]\qquad\text{for every }v\in V(H).
\]
The correspondence \(c\mapsto(T_i)_{i=1}^4\), with \(T_i=\{v:i\in c(v)\}\), is a bijection from admissible labelings to the ordered four-tuples counted above. The problem is finite and exact, with no asymptotic or probabilistic qualification.

## Proof
**1. Factorization through the two Fano classes.** Every neighbor of a point-vertex of \(H\) is a line-vertex, and every neighbor of a line-vertex is a point-vertex. Thus the admissibility conditions imposed at line-vertices involve only the seven point labels, whereas conditions at point-vertices involve only the seven line labels. The incidence dual is again a Fano plane. The two seven-point problems are independent, so the total number is the square of the one-sided count.

**2. Normalize a repeated label.** A one-sided labeling has seven points and only six possible two-element labels, so some two distinct points \(p,q\) have the same label \(\pi\). Let \(r\) be the third point on their unique line. Because the three labels on that line must cover all four names, \(c(r)=[4]\setminus\pi\). By a permutation of the four names, put \(\pi=\{1,2\}\), so \(c(r)=\{3,4\}\).

Let the other four points be \(a,b,c,d\). The two Fano lines through \(p\) besides \(pqr\), together with the two through \(q\), define the four edges of a four-cycle on \(\{a,b,c,d\}\). The two remaining lines through \(r\) pair opposite vertices of this four-cycle. This is the complete list of the Fano lines not equal to \(pqr\): four lines \(\{p,x,y\}\) or \(\{q,x,y\}\) corresponding to cycle edges, and two lines \(\{r,x,y\}\) corresponding to its diagonals.

**3. Eight completions.** Every edge of the four-cycle must have at least one endpoint whose label contains \(3\), and at least one whose label contains \(4\), because the corresponding Fano line contains \(p\) or \(q\) with label \(\{1,2\}\). Thus each of \(3\) and \(4\) occurs on at least two of the four off-line points. Likewise, on each of the two diagonal pairs, the labels must collectively contain \(1\) and \(2\), since the third point is \(r\) with label \(\{3,4\}\). Each of \(1\) and \(2\) therefore occurs at least twice off the line \(pqr\).

There are only eight incidences between four off-line points and the two names in each of their labels. The four lower bounds just established sum to eight. Consequently each name occurs **exactly twice** there. The two occurrences of \(3\) form a minimum vertex cover of the four-cycle, and thus are opposite vertices; the same holds for \(4\). These two opposite pairs cannot coincide: otherwise one diagonal pair has both labels equal to \(\{3,4\}\) and fails to cover \(1,2\) on its line with \(r\). They must therefore be the two different diagonal pairs. Each off-line point then receives exactly one of \(3,4\), with two possible assignments. On each diagonal pair, the vertices must receive different members of \(\{1,2\}\), independently giving two choices on each pair. Exactly \(2\cdot2\cdot2=8\) completions result, and all satisfy the six remaining line conditions.

These four off-line labels are precisely \(\{1,3\},\{1,4\},\{2,3\},\{2,4\}\), once each. Together with \(c(p)=c(q)=\{1,2\}\) and \(c(r)=\{3,4\}\), this shows that the repeated label and its repeated point pair are unique. Every admissible labeling therefore arises **exactly once** by choosing one of the \(\binom72=21\) unordered point pairs, one of the six duplicated labels, and one of the eight completions. Hence there are \(21\cdot6\cdot8=1008\) one-sided labelings.

**4. One orbit on a Fano class.** The Fano-plane collineation group \(\operatorname{GL}(3,2)\), of order \(168\), is transitive on unordered pairs of distinct points. The permutation group of the four names is transitive on the six possible duplicated labels. Once these choices are fixed, the subgroup of collineations preserving the repeated unordered point pair has order \(168/21=8\). It acts freely on the eight completions: a stabilizing collineation must fix each of the four off-line points because they carry distinct labels, and these four vectors span \(\mathbb F_2^3\), so the collineation is the identity. An action by a group of order eight on eight objects that is free is transitive. Thus all one-sided labelings lie in a single orbit under collineations and name permutations.

**5. Two classes and unlabelled families.** Independence of the point and line restrictions gives \(1008^2=1{,}016{,}064\) admissible labeled assignments to the fourteen vertices. Every one-sided assignment uses all six two-element labels. In particular, no two of the four total dominating sets coincide: each pair of names has different membership on at least one vertex. Furthermore, no nonidentity permutation of the four names fixes a labeled assignment, since all six two-element labels occur. The name-permutation action is therefore free and has orbits of size \(4!=24\). This gives \(1{,}016{,}064/24=42{,}336\) unlabelled families.

## Verification
The standalone `verify.py`, requiring only the Python 3 standard library, independently enumerates all \(6^7=279{,}936\) possible one-sided labelings against the seven Fano line conditions. It confirms exactly \(1008\) successes and the unique repeated-label multiplicity profile. A separate four-point enumeration under the normalized repeated pair confirms exactly eight completions. It constructs all \(168\) linear collineations and all \(24\) name permutations and confirms the claimed single orbit. Finally, it checks the squared and unlabelled counts. The recorded run in `verify_output.txt` ends `VERIFY_OK`. The mathematical argument above is a complete finite proof independent of executing the checker.

## Relationship to prior work
Kwon, Park and Sano (arXiv:2610.19450, initially public 14 October 2026) prove that every cubic graph has four total dominating sets with every vertex in exactly two, and formulate the equivalent \((4{:}2)\)-labeling condition. They give explicit colorings for the Fano/Heawood building blocks. That is an **existence theorem**; the claim here is the complete structural census, symmetry classification of the one-sided Fano problem and exact multiplicity for the Heawood graph. The older work of Goddard and Henning established the thoroughly dispersed coloring framework and examined fractional total domination, including the exceptional role of Heawood. Existence and fractional bounds do not numerically determine the number of admissible families. The counting proof here uses only the elementary Fano incidence structure and does not infer novelty solely from title or number searches.

## Limitations
The census is specific to the labeled fourteen-vertex Heawood graph, with exactly two memberships at each vertex; it does not enumerate all generally allowed families with at-most-two memberships, nor classify witnesses on every cubic graph. The unlabelled count quotients only the four **set names**, not the automorphisms of the graph. A prior unindexed enumeration or an equivalent count under different terminology remains a publication-priority possibility. Accessible comparisons included the motivating article's introduction and its Fano constructions, but access to the remainder of that article and to the complete original 2017/2018 thoroughly dispersed coloring paper was limited. Independent audit has not been performed.

## References
1. H. Kwon, B. Park and Y. Sano, *Every cubic graph has four total dominating sets covering each vertex at most twice*, arXiv:2610.19450 (first posted 14 October 2026), https://arxiv.org/abs/2610.19450 ; accessible HTML: https://arxiv.org/html/2610.19450v1 .
2. W. Goddard and M. A. Henning, *Thoroughly dispersed colorings*, Journal of Graph Theory 88 (2018), 174–191, DOI:10.1002/jgt.22204, https://doi.org/10.1002/jgt.22204 .
3. W. Goddard and M. A. Henning, *Fractional Domatic, Idomatic, and Total Domatic Numbers of a Graph*, in *Structures of Domination in Graphs*, Springer (2021), DOI:10.1007/978-3-030-58892-2_4 (Heawood/Fano neighborhood-hypergraph discussion).
