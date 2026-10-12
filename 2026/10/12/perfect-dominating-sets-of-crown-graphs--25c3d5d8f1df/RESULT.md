# Perfect dominating sets of crown graphs
## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-M_n
\]
have bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), with deleted matching edges \(a_i b_i\). A set \(D\subseteq V(\operatorname{Cr}_n)\) is called perfect dominating when every vertex outside \(D\) has exactly one neighbor in \(D\).

Write
\[
I=\{i:a_i\in D\},\qquad J=\{i:b_i\in D\}.
\]
Then the complete classification is:

1. \(D=V(\operatorname{Cr}_n)\);
2. \(D=\{a_i,b_i\}\) for exactly one \(i\in[n]\); or
3. \(n\in\{3,4\}\), \(|I|=|J|=2\), and \(I\cup J=[n]\).

There are exactly six sets of type 3 for each of \(n=3\) and \(n=4\), and there are no other perfect dominating sets. Hence the perfect domination polynomial is
\[
D_p(\operatorname{Cr}_n;x)=
\begin{cases}
nx^2+6x^4+x^{2n},&n\in\{3,4\},\\
nx^2+x^{2n},&n\ge5.
\end{cases}
\]
In particular,
\[
\gamma_p(\operatorname{Cr}_n)=2,
\]
and the \(n\) minimum perfect dominating sets are precisely the deleted-matching pairs \(\{a_i,b_i\}\).

The classification also exposes a sharp connectivity boundary. Every size-two perfect dominating set is disconnected. For \(n=3,4\), each of the six exceptional size-four sets induces a connected subgraph. For every \(n\ge5\), the full vertex set is the only connected perfect dominating set.

## Assumptions and scope
Graphs are finite, simple, and undirected. The crown graph is connected for \(n\ge3\). Perfect domination uses the standard convention that only vertices outside the selected set are required to have exactly one selected neighbor; vertices of \(D\) are unrestricted internally. The polynomial counts all perfect dominating sets by cardinality.

The statement is only for the ordinary crown family \(K_{n,n}-M_n\) with \(n\ge3\). It does not claim an analogous formula for arbitrary bipartite graphs or for efficient domination, where selected vertices must also be dominated uniquely.

## Proof
Let \(a=|I|\) and \(b=|J|\). Because \(a_i\) is adjacent to every vertex of \(B\) except \(b_i\), every \(i\notin I\) satisfies
\[
|N(a_i)\cap D|=b-\mathbf 1_{\{i\in J\}}.
\]
Similarly, every \(j\notin J\) satisfies
\[
|N(b_j)\cap D|=a-\mathbf 1_{\{j\in I\}}.
\]
Thus \(D\) is perfect dominating if and only if
\[
b-\mathbf 1_{\{i\in J\}}=1\quad(i\notin I),
\qquad
a-\mathbf 1_{\{j\in I\}}=1\quad(j\notin J).
\]

First suppose \(I=[n]\). If \(J\ne[n]\), choose \(j\notin J\). The second equation becomes \(n-1=1\), impossible for \(n\ge3\). Hence \(J=[n]\), so \(D=V(\operatorname{Cr}_n)\). The same argument with the sides interchanged shows that if either side is completely selected, then both sides are.

Now suppose both complements are nonempty. The displayed equations force \(a,b\in\{1,2\}\). If \(a=b=1\), the first equation gives \(J\subseteq I\), while the second gives \(I\subseteq J\). Hence \(I=J=\{i\}\) for some \(i\), producing exactly the deleted-matching pair \(\{a_i,b_i\}\).

If \((a,b)=(1,2)\), the first equation forces \([n]\setminus I\subseteq J\), while the second forces \(I\subseteq J\). Hence \(J=[n]\), contradicting \(b=2<n\). The case \((a,b)=(2,1)\) is symmetric.

Finally let \(a=b=2\). The first equation is equivalent to \([n]\setminus I\subseteq J\), and the second to \([n]\setminus J\subseteq I\). Together they are equivalent to
\[
I\cup J=[n].
\]
Because \(|I|=|J|=2\), this is possible only for \(n\le4\). For \(n=3\), it means that \(I\) and \(J\) are distinct two-subsets, giving \(3\cdot2=6\) ordered pairs. For \(n=4\), it means \(J=[4]\setminus I\), giving \(\binom42=6\) choices. This proves the classification and the polynomial.

For connectivity, a matched pair \(\{a_i,b_i\}\) is a deleted edge and therefore disconnected. When \(n=3\), the condition \(|I|=|J|=2\) and \(I\ne J\) makes the induced four-vertex graph connected; when \(n=4\), \(J=[4]\setminus I\) makes the induced graph \(K_{2,2}\). For \(n\ge5\) no proper perfect dominating set other than a disconnected matched pair exists, so the full connected crown graph is the only connected perfect dominating set.

## Verification
The proof above is all-parameter and supplies the infinite result. The accompanying `verify.py` independently enumerates every vertex subset for \(3\le n\le8\), tests the defining outside-neighbor condition directly, compares the resulting cardinality distribution with the formula, checks the index-set classification, and separately checks induced connectivity.

A replay of the packaged script returns:

`VERIFY_OK n_range=3..8 subset_checks=87360 perfect_sets=51 coefficient_checks=72 classification_checks=51 connectivity_checks=51 max_order=16`

The finite enumeration is a consistency check, not a proof for arbitrary \(n\).

## Relationship to prior work
The definition used here is the standard perfect-domination convention. The first source listed below gives that definition explicitly and has public arXiv v1 date 2007-11-27. A later open paper introducing the perfect domination polynomial defines the coefficient of \(x^i\) as the number of perfect dominating sets of size \(i\) and treats several standard families, including complete bipartite and complete multipartite graphs. Its searchable full text contains no crown-graph occurrence. The crown graph is not complete bipartite: it is obtained from \(K_{n,n}\) by deleting a perfect matching, and those missing adjacencies are exactly what create the \(n\) size-two sets and the two small exceptional layers.

A 2013 paper on graphs with no proper perfect dominating set proves a complete-multipartite result for at least three parts and discusses edge perturbations of that regime. Its accessible abstract and first-page material do not place the two-part crown family under that theorem. A complete comparison of every edge-perturbation estimate in that paper could not be made through the available full-text route, so this remains the principal literature residual risk rather than being treated as negative evidence.

Searches were also run under the equivalent descriptions “crown graph”, “\(K_{n,n}\) minus a perfect matching”, “perfect 1-domination”, “perfect domination polynomial”, and connected perfect domination. No source or prior result located stated the classification or polynomial above.

## Limitations
The theorem does not address \(n=2\), where the matching-deleted graph is disconnected. It does not classify weighted, efficient, total-perfect, Roman, or other variants. The direct proof depends on the exact crown adjacency rule and does not automatically extend to arbitrary regular bipartite graphs.

The literature search cannot exclude an unindexed or differently named family-specific result. In particular, the 2013 edge-perturbation paper was not fully readable through the available route during this check; only its abstract and accessible first-page material were compared.

## References
1. I. J. Dejter and A. A. Delgado, “Perfect domination in rectangular grid graphs,” arXiv:0711.4345v1, 27 Nov 2007.
2. S. R. Nayaka, B. Ashwini, B. Sharada, and Puttaswamy, “Perfect Domination Polynomial of a Graph,” International Journal of Mathematics Trends and Technology 67(4), 110–113 (2021), DOI: 10.14445/22315373/IJMTT-V67I4P515.
3. A. Dalal and P. Johnson, “On graphs with no proper perfect dominating set,” Tamkang Journal of Mathematics 44(4), 359–364 (2013), DOI: 10.5556/j.tkjm.44.2013.975.
