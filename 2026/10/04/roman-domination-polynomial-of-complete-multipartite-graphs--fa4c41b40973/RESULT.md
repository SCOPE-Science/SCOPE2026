# Roman domination polynomial of complete multipartite graphs
## Finding
For a connected complete multipartite graph \(G=K_{n_1,\ldots,n_r}\) with \(r\ge 2\), write \(N=\sum_i n_i\). A Roman dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that each vertex with value \(0\) has a neighbor with value \(2\). Define its weight by \(w(f)=\sum_{v\in V(G)}f(v)\), and define the weight enumerator
\[
R_G(x)=\sum_{f\text{ Roman dominating}}x^{w(f)}.
\]
For each part put
\[
A_i=(1+x+x^2)^{n_i},\qquad B_i=(1+x)^{n_i},\qquad C_i=(x+x^2)^{n_i}.
\]
Then
\[
R_G(x)=\prod_i A_i-\prod_i B_i-\sum_i(A_i-B_i)\prod_{j\ne i}B_j+x^N+\sum_i(C_i-x^{n_i})\prod_{j\ne i}B_j.
\]

There is also a complete structural classification. Let \(T(f)\) be the set of part indices containing at least one vertex labeled \(2\). The function \(f\) is Roman dominating if and only if one of the following holds: \(T(f)=\varnothing\) and every vertex has label \(1\); \(|T(f)|\ge2\); or \(T(f)=\{i\}\) and no vertex of part \(i\) has label \(0\).

As immediate coefficient consequences,
\[
\gamma_R(G)=
\begin{cases}
2,&\min_i n_i=1,\\
3,&\min_i n_i=2,\\
4,&\min_i n_i\ge3.
\end{cases}
\]
If \(s_t\) denotes the number of parts of size \(t\), then the number of minimum-weight Roman dominating functions is \(3\) for \(K_2\); for every other graph with \(s_1>0\) it is \(s_1\); when \(s_1=0<s_2\) it is \(2s_2\); and when every part has size at least \(3\) it is
\[
\sum_{i<j}n_i n_j+3s_3.
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The graph is complete multipartite with at least two nonempty parts. The polynomial counts labeled functions, not isomorphism classes of functions. Part order is immaterial.

## Proof
Two vertices in a complete multipartite graph are adjacent exactly when they lie in different parts. Fix an assignment \(f:V(G)\to\{0,1,2\}\), and let \(T(f)\) be the parts that contain a label \(2\).

If \(T(f)=\varnothing\), any label \(0\) would have no neighboring label \(2\). Thus the assignment is Roman dominating exactly when every vertex has label \(1\), giving the term \(x^N\).

If \(|T(f)|\ge2\), then every vertex with label \(0\) lies in some part and sees a label \(2\) in another part. Hence every such assignment is Roman dominating. The generating polynomial for all assignments is \(\prod_i A_i\). Those with no label \(2\) contribute \(\prod_i B_i\). Those whose labels \(2\) occur in exactly one part \(i\) contribute \((A_i-B_i)\prod_{j\ne i}B_j\). Subtracting these cases gives the first three terms of the displayed formula.

Finally suppose \(T(f)=\{i\}\). A vertex labeled \(0\) outside part \(i\) sees a label \(2\) in part \(i\), while a vertex labeled \(0\) inside part \(i\) sees no label \(2\) at all. Therefore the assignment is Roman dominating exactly when part \(i\) uses only labels \(1\) and \(2\), with at least one \(2\), and every other part uses only labels \(0\) and \(1\). Its contribution is \((C_i-x^{n_i})\prod_{j\ne i}B_j\). Summing over \(i\) proves the polynomial identity and the structural classification.

For the minimum-weight statements, the classification leaves only the lightest possibilities. A singleton part permits one label \(2\) and zeros elsewhere, except that \(K_2\) also has the all-one function of weight \(2\). With no singleton but a size-two part, a unique label \(2\) in that part must be accompanied by one label \(1\), giving weight \(3\) and two choices per size-two part. If all parts have size at least \(3\), weight \(4\) is achieved either by one label \(2\) in each of two distinct parts, or by one label \(2\) and two labels \(1\) in a size-three part. These alternatives are disjoint and yield the stated count.

## Verification
The accompanying `verify.py` exhaustively checks every complete multipartite isomorphism type of order at most \(10\): all integer partitions of each order into at least two parts. It enumerates every \(3^N\) labeling, compares the Roman condition with the structural classification, compares every coefficient with the closed polynomial, and checks the minimum-weight coefficient formulas. A replay of the packaged script returns:

`VERIFY_OK graph_types=128 labelings=3169350 coefficient_checks=2230 max_order=10`

The computation verifies the finite test range only; the general result rests on the proof above.

## Relationship to prior work
Cockayne, Dreyer, Hedetniemi, and Hedetniemi introduced Roman domination and the standard \(0,1,2\)-label definition. Pushpam and Padmapriea later studied forcing Roman domination and, for complete multipartite graphs, analyzed minimum-weight Roman dominating functions to determine the forcing parameter. Their result concerns \(\gamma_R\)-functions rather than all Roman dominating functions and does not give the weight enumerator above. Recent work has used the name Roman domination polynomial for the weight enumerator on other graph families. Searches for complete multipartite, complete bipartite, Roman domination polynomial, weight enumerator, and all Roman dominating functions did not locate this all-function classification or its product-sum formula.

## Limitations
The literature comparison is evidence of noncoverage, not a proof that no equivalent formula has ever appeared under different terminology. In particular, older Roman-domination literature is extensive and some sources may be poorly indexed. The formula is for ordinary Roman domination only; signed, total, perfect, double, strong, and other Roman variants obey different conditions. The exhaustive checker is finite and is not a substitute for the general proof.

## References
1. E. J. Cockayne, P. A. Dreyer Jr., S. M. Hedetniemi, S. T. Hedetniemi, “Roman domination in graphs,” *Discrete Mathematics* 278 (2004), 11–22. DOI: 10.1016/j.disc.2003.06.004.
2. P. Roushini Leely Pushpam, S. Padmapriea, “Forcing Roman Domination in Graphs,” *Asian Journal of Mathematics and Computer Research* 25(7) (2018), 441–453.
3. A. Alqesmah, D. Gangabylaiah, “On the roman domination polynomial of the commuting and non-commuting graphs associated to the dihedral groups,” *Annals of Mathematics and Computer Science* 27 (2025). DOI: 10.56947/amcs.v27.482.
