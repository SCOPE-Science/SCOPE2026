# Strong alliance polynomial of dumbbell graphs
## Finding
Let \(r,s\ge3\), and let \(D_{r,s}\) be formed from disjoint cliques \(K_r\) and \(K_s\) by adding a single bridge \(uv\), with \(u\) in the left clique and \(v\) in the right clique. Put
\[
h_m=\left\lceil\frac{m+1}{2}\right\rceil,
\qquad
g_m=\left\lceil\frac{m+2}{2}\right\rceil.
\]
Define
\[
E_m(x)=\sum_{k=h_m}^{m-1}\binom{m-1}{k}x^k,
\]
\[
J_m(x)=\sum_{k=g_m}^{m}\binom{m-1}{k-1}x^k,
\qquad
I_m(x)=\sum_{k=h_m}^{m}\binom{m-1}{k-1}x^k.
\]
Then the strong alliance polynomial is
\[
a(D_{r,s};x)=E_r(x)+J_r(x)+E_s(x)+J_s(x)+I_r(x)I_s(x).
\]
In particular,
\[
a(D_{r,s})=\min\{h_r,h_s\}.
\]
There is also a complete unimodality classification. After interchanging the two clique orders if necessary so that \(r\le s\), the coefficient sequence of \(a(D_{r,s};x)\), starting at its minimum exponent and ending at degree \(r+s\), is unimodal if and only if
\[
(r,s)\in\{(3,3),(3,5),(3,7)\}.
\]
Thus the formula classifies every contributing set and, unlike the path, cycle, complete-bipartite, and double-star examples emphasized in the founding paper, produces an infinite canonical family in which non-unimodality is the generic behavior.

## Assumptions and scope
Graphs are finite and simple. A strong defensive alliance is a nonempty vertex set \(S\) such that every \(w\in S\) has at least as many neighbors in \(S\) as outside \(S\). The standard strong alliance polynomial counts strong defensive alliances for which the induced subgraph \(G[S]\) is connected, with exponent \(|S|\).

The restriction \(r,s\ge3\) keeps both clique sides in the genuine dumbbell regime and avoids small path identifications. The bridge endpoints are denoted by \(u\) and \(v\).

## Proof
Let a candidate set select \(a\) vertices from the left clique. For a selected nonbridge left vertex, the number of selected neighbors is \(a-1\), while the number of unselected neighbors is \(r-a\). Thus its strong-alliance inequality is
\[
a-1\ge r-a,
\]
which is equivalent to \(a\ge h_r\).

Suppose now that the left bridge endpoint \(u\) is selected. Let \(\beta\in\{0,1\}\) record whether the opposite endpoint \(v\) is selected. Then \(u\) has \(a-1+\beta\) neighbors inside the set and \(r-a+1-\beta\) outside. Hence its inequality is
\[
a-1+\beta\ge r-a+1-\beta,
\]
or equivalently \(a+\beta\ge g_r\).

Consider first a contributing set contained entirely in the left clique. If \(u\) is omitted, only the nonbridge inequality appears, so \(a\ge h_r\), and there are \(\binom{r-1}{a}\) such sets. If \(u\) is selected, then \(\beta=0\), so \(a\ge g_r\), and there are \(\binom{r-1}{a-1}\) such sets. These are exactly the terms \(E_r(x)+J_r(x)\). The same reasoning gives \(E_s(x)+J_s(x)\) on the right.

Finally suppose the set meets both cliques. Since \(uv\) is the only edge between the two clique sides, connectedness of the induced subgraph forces both \(u\) and \(v\) to be selected. Thus \(\beta=1\) at either endpoint. The nonbridge inequalities give \(a\ge h_r\) and \(b\ge h_s\), where \(b\) is the selected count on the right. These bounds also imply the endpoint inequalities with the opposite endpoint selected. For fixed \(a,b\), the number of such sets is
\[
\binom{r-1}{a-1}\binom{s-1}{b-1},
\]
so their generating function is \(I_r(x)I_s(x)\).

The five displayed summands count disjoint cases and exhaust all connected strong defensive alliances, proving the polynomial. A cross-clique alliance has at least \(h_r+h_s\) vertices, whereas a one-clique alliance realizes \(h_r\) or \(h_s\); therefore the minimum exponent is \(\min\{h_r,h_s\}\).

For unimodality, assume \(r\le s\), and write \(p_k=[x^k]a(D_{r,s};x)\). First suppose \(r\ge4\), and put
\[
K=h_r+h_s,
\qquad
A_m=\binom{m-1}{h_m-1}.
\]
The product \(I_r(x)I_s(x)\) begins in degree \(K\), with coefficient \(A_rA_s\). For \(k=K-2,K-1\), the product contributes nothing. Since \(h_r\ge3\), both indices lie beyond the one-clique threshold on every side that can contribute, so with the convention \(\binom{m}{k}=0\) for \(k>m\),
\[
p_{K-2}=\binom r{K-2}+\binom s{K-2},
\qquad
p_{K-1}=\binom r{K-1}+\binom s{K-1}.
\]
The relevant binomial coefficients are on their strictly decreasing side, and the \(s\)-term at degree \(K-2\) is nonzero, hence \(p_{K-2}>p_{K-1}\).

It remains to see that the sequence rises again at degree \(K\). If \(r\ge5\), then \(A_r,A_s\ge6\). Since \(A_m\) is a largest coefficient in row \(m-1\) of Pascal's triangle, every \(\binom m j\le2A_m\). Therefore
\[
p_{K-1}\le2A_r+2A_s<A_rA_s\le p_K.
\]
If \(r=4\), then \(A_r=3\) and the \(r\)-side contribution to \(p_{K-1}\) is zero; moreover \(p_{K-1}=\binom{s}{h_s+2}<2A_s<3A_s\le p_K\). Thus every case \(r\ge4\) has a strict descent followed by a strict ascent and is not unimodal.

Now let \(r=3\). Then
\[
E_3(x)+J_3(x)=x^2+x^3,
\qquad
I_3(x)=2x^2+x^3.
\]
If \(s\ge9\) is odd, then \(h_s\ge5\), so \(p_3>0\), \(p_4=0\), and a later coefficient is positive; unimodality fails. If \(s=2q\ge4\) is even, let \(K=h_3+h_s=q+3\). Before the product starts,
\[
p_{K-2}>p_{K-1}=\binom{s}{h_s+1},
\]
while its first product coefficient is \(2A_s\), and \(\binom{s}{h_s+1}<2A_s\le p_K\). Hence every even \(s\ge4\) is non-unimodal. The only remaining pairs are \((3,3)\), \((3,5)\), and \((3,7)\); direct substitution gives coefficient sequences
\[
(2,2,4,4,1),
\qquad
(1,5,5,13,14,6,1),
\qquad
(1,1,15,21,47,51,27,8,1),
\]
respectively, all unimodal. This proves the classification.

## Verification
The proof is symbolic and holds for every \(r,s\ge3\). As an independent finite consistency check, `verify.py` exhaustively enumerates every nonempty vertex subset for all \(3\le r,s\le7\), tests induced connectivity and the defining strong defensive inequalities directly, and compares every coefficient with the formula. It also checks the minimum exponent. Separately, the closed formula is evaluated for every ordered-by-size pair \(3\le r\le s\le40\) and its coefficient sequence is checked against the proved unimodality classification.

The replay result is recorded in `verify_output.txt`:

`VERIFY_OK pairs=25 subset_checks=61479 coefficient_checks=275 minimum_checks=25 formula_unimodality_checks=741 max_order=14`

The finite enumeration corroborates the proof; it is not used to infer the infinite family.

## Relationship to prior work
Carballosa, Hernández-Gómez, Rosario, and Torres-Núñez introduced the strong alliance polynomial and reported exact computations for paths, cycles, complete graphs, stars, complete bipartite graphs, and double stars. Those families do not contain the dumbbells \(D_{r,s}\) with \(r,s\ge3\). A later defensive-alliance-polynomial paper explicitly relates its bivariate invariant to the strong alliance polynomial and treats further standard families including friendship and book graphs, but no dumbbell or barbell formula was located in its accessible full text.

The closest published exact formula located is for complete multipartite graphs. It does not imply the present result: a dumbbell with both clique orders at least three is not complete multipartite, and here the single bridge simultaneously changes the endpoint degree inequalities and makes induced connectedness depend on selecting both bridge endpoints.

## Limitations
The claim is restricted to the standard strong alliance polynomial and to \(r,s\ge3\). It does not address weak defensive alliances, global alliances, or modified alliance polynomials. The founding arXiv full text and a later open full text were inspected directly for the standard definition, family coverage, and the terms `dumbbell` and `barbell`. As with any literature search, an unindexed or differently named family-specific result could remain undiscovered.

## References
1. W. Carballosa, J. C. Hernández-Gómez, O. Rosario, and Y. Torres-Núñez, *Computing the strong alliance polynomial of a graph*, arXiv:1507.08654v1, 2015; *Investigación Operacional* 37(2) (2016), 115–123.
2. H. Ibrahim, *Defensive alliance polynomial*, arXiv:1811.10089v1; *Journal of Combinatorial Mathematics and Combinatorial Computing* 115 (2020), 35–60.
