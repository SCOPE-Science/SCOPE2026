# Sparse minimal double-total-domination spectra in three-layer clique paths

## Finding
Let \(n\geq 6\), and let \(G_n=K_n\square P_3\). A double total dominating set \(S\) contains at least two *neighbors* of every vertex, including the vertices of \(S\) themselves. Write \(\mathcal M_n(z)=\sum_S z^{|S|}\), summed over all inclusion-minimal double total dominating sets (minimal under deletion, not necessarily of minimum cardinality).

Define
\[
q=\binom{n-2}{2},\qquad r=2q+\binom{n-2}{3},\qquad h=\binom{n-3}{3},\qquad j=\binom{n-3}{2}.
\]
Then
\[
\boxed{\begin{aligned}
\mathcal M_n(z)={}&\binom n2 z^6
+\left(2\binom n2 r+n(n-1)(n-2)\right)z^7\\
&+\left(2\binom n2 q^2+\binom n2\binom{n-2}{2}\right)z^8\\
&+\binom n3\left(h^2+6hj+3j^2\right)z^9\\
&+n\left(2^{n-1}-2n\right)z^{n+2}+z^{2n}.
\end{aligned}}
\]
Coincident exponents are combined (at \(n=6,7\)). Exactly \(\binom n2\) minimal sets have minimum size \(6\). Exactly one minimal set has largest size \(2n\), namely the union of the two outer clique layers. Thus
\[
\gamma_{\times2,t}(G_n)=6,\qquad \Gamma_{\times2,t}(G_n)=2n.
\]
For \(n\geq8\), the possible cardinalities of inclusion-minimal sets are exactly \(\{6,7,8,9,n+2,2n\}\), and the upper-minus-lower gap is \(2n-6\).

## Assumptions and scope
The graph is finite, undirected, simple, with vertex set \(\{(i,\ell):i\in[n],\ell\in\{1,2,3\}\}\). Vertices are adjacent when they are distinct within the same clique layer or have the same column index in consecutive layers. No diagonal between outer layers exists. The theorem is asserted for all integers \(n\geq6\), with no assertion that its formula extends to smaller orders. Binomial coefficients have their usual combinatorial meaning. Minimality means that deleting any one selected vertex destroys double total domination; this is equivalent to inclusion-minimality because the property is upward closed.

## Proof
Write \(A,B,C\subseteq[n]\) for the selected column indices in the first, middle, and third layers, and write \(a=|A|\), \(b=|B|\), \(c=|C|\), \(N=[n]\). The numbers of selected neighbors of vertices in column \(i\), respectively, are
\[
a-\mathbf 1_{i\in A}+\mathbf 1_{i\in B},\quad
b-\mathbf 1_{i\in B}+\mathbf 1_{i\in A}+\mathbf 1_{i\in C},\quad
c-\mathbf 1_{i\in C}+\mathbf 1_{i\in B}.
\]
Consequently, feasibility is equivalent to \(a,c\geq2\), with \(A\subseteq B\) when \(a=2\) and \(C\subseteq B\) when \(c=2\), together with these middle-layer conditions:
\[
\begin{array}{c|l}
b&\text{additional condition}\\\hline
0&A=C=N\\
1&B\subseteq A\cap C,\quad A\cup C=N\\
2&B\subseteq A\cup C\\
\geq3&\text{none}.
\end{array}
\]
We classify deletion-minimal feasible triples according to \(b\). The inequalities used below all require \(n\geq6\).

**Case \(b=0\).** The sole feasible triple is \((N,\varnothing,N)\). Removing either outer-layer vertex breaks the middle-layer requirement in its column. It contributes \(z^{2n}\).

**Case \(b=1\).** Let \(B=\{i\}\). Feasibility requires \(i\in A\cap C\), \(A\cup C=N\), and \(a,c\geq3\). A minimal triple has \(A\cap C=\{i\}\): if another common column is present, at least one outer layer has at least four vertices and its vertex in that column can be deleted. Conversely, when the only common column is \(i\), every outer deletion destroys coverage of the middle layer or removes a necessary neighbor at \(i\); deleting \(i\) from the middle layer is also invalid. The \(n-1\) other columns are partitioned between \(A\setminus\{i\}\) and \(C\setminus\{i\}\), each receiving at least two. There are \(n(2^{n-1}-2n)\) such sets, all of size \(n+2\).

**Case \(b=2\).** Write \(B=\{i,j\}\). To prohibit deletion in an outer layer, its index set must be either \(B\) itself (size two) or a three-set having at least two indices outside \(B\). Indeed, a four-set contains a deletable element outside \(B\), while deleting the unique outside element from a three-set meeting \(B\) twice would leave the feasible two-set \(B\). The middle condition also requires \(B\subseteq A\cup C\). Removing a middle-layer vertex cannot produce a feasible singleton middle layer: it would require a common column and \(A\cup C=N\), but \(a,c\leq3\) makes their union have at most five elements when nonempty intersection exists. Thus the listed outer conditions and middle coverage are sufficient for minimality. With \(r=2\binom{n-2}{2}+\binom{n-2}{3}\), the options are: \(A=C=B\) (one choice per \(B\), size six); exactly one outer set equal to \(B\) and the other one of \(r\) admissible three-sets (\(2r\) per \(B\), size seven); or two three-sets covering the two indices of \(B\) using different singleton intersections with \(B\) (\(2\binom{n-2}{2}^2\) per \(B\), size eight).

**Case \(b=3\).** Minimality forces \(a,c\leq3\), since a larger outer set has a deletable index outside \(B\). A two-set must be contained in \(B\). A three-set must meet the complement of \(B\) in at least two indices to prevent reduction to a feasible two-set. If both outer sets are two-sets, they must be different: otherwise the extra middle vertex is deletable. Hence \(B=A\cup C\), the sets meet once, and there are \(n(n-1)(n-2)\) such triples of size seven. A two-set combined with a three-set is never minimal, since the middle vertex outside the two-set can be removed, leaving a feasible \(b=2\) triple. If both are three-sets, deleting one middle vertex is possible exactly when at least two indices of \(B\) belong to \(A\cup C\). Thus the minimal pairs have \(|B\cap(A\cup C)|\leq1\). For fixed \(B\), let \(h=\binom{n-3}{3}\) count outer three-sets avoiding \(B\), and let \(j=\binom{n-3}{2}\) count those containing a specified one index of \(B\) and two outside. The ordered choices are: neither meets \(B\) (\(h^2\)); only one meets \(B\) (\(6hj\)); or both meet the same one index (\(3j^2\)). This gives \(\binom n3(h^2+6hj+3j^2)\) size-nine triples.

**Case \(b=4\).** Minimality requires both outer sets to have size two. Every middle vertex is essential precisely when \(B=A\cup C\), which forces \(A\cap C=\varnothing\). There are \(\binom n2\binom{n-2}{2}\) such size-eight triples.

**Case \(b\geq5\).** Some middle vertex can always be deleted: a size-two outer set depends on at most two specified middle vertices, and with both outer sets size two they depend on at most four; a larger outer set imposes no such dependency. Thus no minimal triples occur.

Adding the disjoint contributions gives the displayed polynomial. Its degree is \(2n\) and its lowest degree is six, with the respective stated coefficients. For \(n\geq8\), all six displayed exponents are distinct and have strictly positive coefficients, proving the support assertion.

## Verification
The standalone `verify.py` uses the graph's definition to check all \(3n\) selected-neighbor inequalities directly. For every subset at \(n=3,4,5,6,7\), it determines feasibility and checks whether removal of each selected vertex destroys feasibility. At \(n=6,7\), it additionally checks the separate structural classification and the formula coefficient by coefficient. Its cumulative comparison domain comprises \(2^{9}+2^{12}+2^{15}+2^{18}+2^{21}=2,396,672\) vertex subsets. The generalized theorem is proved above independently of these finite checks.

## Relationship to prior work
Kazemi, Pahlavsay and Stones give bounds on \(k\)-tuple total domination of Cartesian products and an exact minimum formula for rook graphs \(K_n\square K_m\). Because \(K_n\square P_3\) is a spanning subgraph of \(K_n\square K_3\), their minimum result implies a lower bound of six for the present graph; the six-vertex construction attains it. The scalar minimum is therefore not asserted to be a novel isolated result. Carballosa and Wisby give later total-\(k\) product results and again focus on products of complete graphs. Li, Yue and Zhang study double total domination numbers for products of two paths, not clique-path products. None of these inspected claims determines the inclusion-minimal polynomial or its large-cardinality spectrum. This is a comparison of identified statements, not a claim of exhaustive publication priority.

## Limitations
The formula is proved for \(n\geq6\), not for small exceptional orders. The work does not classify all (nonminimal) feasible sets by cardinality. Independent mathematical audit has not been performed; unindexed, equivalent, or later literature may affect novelty priority. Finite enumeration is corroboration only.

## References
1. A. P. Kazemi, B. Pahlavsay and R. J. Stones, "Cartesian product graphs and k-tuple total domination," arXiv:1509.08208 (first public 2015-09-28), Filomat 32 (2018), 6713–6731. https://arxiv.org/abs/1509.08208
2. W. Carballosa and J. Wisby, "Total k-domination in Cartesian product of complete graphs," arXiv:2001.07850 (first public 2020-01-22), Discrete Applied Mathematics (2023). https://arxiv.org/abs/2001.07850
3. L. Li, J. Yue and X. Zhang, "Double total domination number of Cartesian product of paths," AIMS Mathematics 8 (2023), 9506–9519, first public 2023-02-20. https://doi.org/10.3934/math.2023479
