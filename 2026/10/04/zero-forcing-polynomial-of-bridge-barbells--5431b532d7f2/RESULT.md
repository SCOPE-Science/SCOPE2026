# Zero forcing polynomial of bridge barbells
## Finding
Let \(B_{a,b}\), with \(a,b\ge3\), be the graph obtained from disjoint cliques \(K_a\) and \(K_b\) by adding one bridge \(uv\), where \(u\in K_a\) and \(v\in K_b\). Put \(A=V(K_a)\setminus\{u\}\) and \(C=V(K_b)\setminus\{v\}\). A set \(S\subseteq V(B_{a,b})\) is zero forcing exactly when \(|S\cap A|\ge a-2\), \(|S\cap C|\ge b-2\), and it is not simultaneously true that \(u,v\notin S\), \(|S\cap A|=a-2\), and \(|S\cap C|=b-2\). Consequently \[\mathcal Z(B_{a,b};x)=x^{a+b-3}\bigl(x^3+(a+b)x^2+(ab+a+b-2)x+(2ab-a-b)\bigr).\] In particular, \(Z(B_{a,b})=a+b-3\), there are \(2ab-a-b\) minimum zero forcing sets, and the total number of zero forcing sets is \(3ab+a+b-1\).

## Assumptions and scope
All graphs are finite, simple, and undirected. For integers \(a,b\ge3\), let \(B_{a,b}\) be formed from disjoint cliques \(K_a\) and \(K_b\) by adding a single bridge \(uv\), with \(u\) in the left clique and \(v\) in the right clique. Write
\[
A=V(K_a)\setminus\{u\},\qquad C=V(K_b)\setminus\{v\}.
\]

A zero forcing set is an initially blue set from which repeated applications of the color-change rule—any blue vertex with exactly one white neighbor forces that neighbor blue—eventually color every vertex blue. The zero forcing polynomial is
\[
\mathcal Z(G;x)=\sum_{k=1}^{|V(G)|}z(G;k)x^k,
\]
where \(z(G;k)\) counts zero forcing sets of size \(k\).

## Proof
First, every zero forcing set \(S\) must satisfy
\[
|S\cap A|\ge a-2.
\]
Indeed, if at least two vertices of \(A\) start white, then both have all their neighbors inside the left clique, and every blue vertex that could force either one sees both as white until one of them is forced. Thus neither can be the first of the pair to be forced. The same argument gives
\[
|S\cap C|\ge b-2.
\]

Now suppose that both inequalities are equalities and that \(u,v\notin S\). Then the left clique has exactly two white vertices, namely \(u\) and one vertex of \(A\), while the right clique has exactly two white vertices, namely \(v\) and one vertex of \(C\). Every initially blue vertex lies inside one of the cliques and sees both white vertices of that clique. Hence no force is available at the initial step, so this configuration is not zero forcing.

Conversely, assume
\[
|S\cap A|\ge a-2,\qquad |S\cap C|\ge b-2,
\]
and exclude the single threshold configuration just described.

If \(u\) is blue, then because \(a\ge3\), at least one vertex of \(A\) is blue. Such a vertex sees at most one white vertex in the left clique, so it can force that vertex if necessary. Once the left clique is entirely blue, \(u\) forces \(v\) if \(v\) is still white. After \(v\) is blue, a blue vertex of \(C\) similarly forces the only possible remaining white vertex in the right clique. The same argument applies with the two sides reversed when \(v\) is initially blue.

If both \(u\) and \(v\) are initially white, the excluded threshold configuration guarantees that one side, say the left, has all of \(A\) blue. Then any vertex of \(A\) has \(u\) as its unique white neighbor and forces \(u\), reducing to the previous case. This proves the stated characterization.

For enumeration, selections from \(A\) contributing at least \(a-2\) vertices have generating polynomial
\[
x^a - 2(a-1+x),
\]
and similarly the right ordinary vertices contribute
\[
x^b - 2(b-1+x).
\]
The bridge endpoints are independently optional, giving a factor \((1+x)^2\). This counts exactly one forbidden structural type: both bridge endpoints omitted and exactly one ordinary vertex omitted from each clique. There are \((a-1)(b-1)\) such sets, each of size \(a+b-4\). Therefore
\[
\mathcal Z(B_{a,b};x)
=
x^a + b - 4\left((1+x)^2(a-1+x)(b-1+x)-(a-1)(b-1)\right).
\]
The constant term in the bracket cancels, and expansion gives
\[
\mathcal Z(B_{a,b};x)
=
x^a + b - 3\left(
x^3+(a+b)x^2+(ab+a+b-2)x+(2ab-a-b)
\right).
\]

The least exponent is \(a+b-3\), so
\[
Z(B_{a,b})=a+b-3,
\]
and the number of minimum sets is \(2ab-a-b\). Evaluating at \(x=1\) gives
\[
\mathcal Z(B_{a,b};1)=3ab+a+b-1.
\]

## Verification
The included checker constructs the two cliques and bridge directly for all \(3\le a,b\le7\). It tests every vertex subset using the zero forcing color-change rule, independently tests the structural criterion above, and compares the resulting coefficient vector with the closed formula.

The finite computation checks the proof on a nontrivial parameter grid; it is not used to infer the all-parameter theorem.

## Relationship to prior work
The paper introducing the zero forcing polynomial gives exact formulas for several families and explicitly asks for characterizations of zero forcing sets in further nontrivial graph families, including trees, as well as splitting formulas based on cut vertices or separating sets. The bridge barbell is a basic connected graph built from two highly symmetric blocks joined by one separating edge, so its exact enumeration is a natural instance of that program.

Later work on zero forcing-set counts studies how graph operations affect the coefficients and proves coefficientwise path-extremality for broad classes such as trees and outerplanar graphs. Those results give inequalities, not the exact coefficient vector above. A still later distance-hereditary result similarly proves path-extremal inequalities using twin and leaf mechanisms. Targeted searches for “barbell”, “two cliques joined by a bridge”, and the exact coefficient form did not locate an equivalent enumeration.

## Limitations
The theorem uses the single-bridge barbell with both clique orders at least three. Cases with a clique of order two have different small-graph behavior and are not included. The claim is an exact enumeration only; no general bridge-splitting theorem for arbitrary graphs is asserted. Search coverage cannot exclude a differently phrased or non-indexed barbell formula.

## References
1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910v1, 26 January 2018; Discrete Applied Mathematics 258 (2019), 35–48, DOI 10.1016/j.dam.2018.11.033.
2. K. Menon, A. Singh, “Exploring the Influence of Graph Operations on Zero Forcing Sets,” arXiv:2405.01423v1, 2 May 2024; Discrete Mathematics 348(8) (2025), 114516, DOI 10.1016/j.disc.2025.114516.
3. S. German, “The Path-Extremal Conjecture for Zero Forcing: Distance-Hereditary Graphs and a Split-Decomposition Reduction,” arXiv:2605.10836v1, 11 May 2026.
