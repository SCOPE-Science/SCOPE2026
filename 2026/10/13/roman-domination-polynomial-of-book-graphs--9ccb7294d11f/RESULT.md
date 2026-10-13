# Roman domination polynomial of book graphs
## Finding
For every integer \(n\ge 1\), let \(B_n=K_{1,n}\mathbin{\square}P_2\) be the square \(n\)-page book graph. Write its two spine vertices as \(u,v\), and for each page \(i\) write the other two vertices as \(a_i,b_i\), with edges \(uv,ua_i,a_ib_i,b_iv\).

A Roman dominating function is a map \(f:V(B_n)\to\{0,1,2\}\) such that every vertex labeled \(0\) has a neighbor labeled \(2\). Its weight is \(w(f)=\sum_{z\in V(B_n)}f(z)\), and the Roman domination polynomial is
\[
R(B_n;x)=\sum_f x^{w(f)},
\]
where the sum is over all Roman dominating functions.

Define
\[
A(x)=x^2(x^2+2x+3),\qquad A_0(x)=x^2(x+2),\qquad B(x)=x(x^3+2x^2+3x+1).
\]
Then
\[
R(B_n;x)=(1+x)^2A(x)^n-2(1+x)A_0(x)^n+x^{2n}+2x^2(1+x)B(x)^n+x^4(1+x+x^2)^{2n}.
\]
In particular, the total number of Roman dominating functions is
\[
R(B_n;1)=4\cdot6^n-4\cdot3^n+1+4\cdot7^n+9^n.
\]
The minimum-weight layer is also explicit: \(\gamma_R(B_1)=3\) with four minimum functions; \(\gamma_R(B_2)=4\) with five minimum functions; and for every \(n\ge3\), \(\gamma_R(B_n)=4\) with a unique minimum function. For \(n\ge3\), that unique minimum function labels both spine vertices \(2\) and every page vertex \(0\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The notation \(B_n\) refers specifically to the square book \(K_{1,n}\mathbin{\square}P_2\), not to the alternative triangular-book convention sometimes used in the literature. The formula counts all Roman dominating functions by weight, not only minimum functions.

The case \(n=1\) is retained because \(B_1\cong C_4\) and is a genuine boundary case: its Roman domination number is \(3\), while the family has Roman domination number \(4\) from \(n=2\) onward.

## Proof
Condition on the ordered pair of spine labels \((f(u),f(v))\). For one page, write its labels as \((f(a_i),f(b_i))\).

First suppose neither spine label is \(2\). Local feasibility on a page requires a zero at \(a_i\) to be paired with label \(2\) at \(b_i\), and a zero at \(b_i\) to be paired with label \(2\) at \(a_i\). Introduce markers \(y,z\) for the events \(f(a_i)=2\) and \(f(b_i)=2\). The one-page weight polynomial is
\[
P(x;y,z)=x^2\bigl(x^2yz+xy+xz+y+z+1\bigr).
\]
Hence
\[
P(x;1,1)=A(x),\qquad P(x;0,1)=P(x;1,0)=A_0(x),\qquad P(x;0,0)=x^2.
\]
If the spine labels are \((0,0)\), then \(u\) needs at least one incident \(a_i\) labeled \(2\), and \(v\) needs at least one incident \(b_i\) labeled \(2\). Inclusion-exclusion therefore gives
\[
A(x)^n-2A_0(x)^n+x^{2n}.
\]
For spine labels \((0,1)\) or \((1,0)\), exactly one such global requirement remains, giving \(x(A(x)^n-A_0(x)^n)\) in each orientation. For \((1,1)\), there is no global requirement, giving \(x^2A(x)^n\). Summing these four cases gives
\[
(1+x)^2A(x)^n-2(1+x)A_0(x)^n+x^{2n}.
\]

Now suppose exactly one spine vertex is labeled \(2\). If, for example, \(f(u)=2\) and \(f(v)\in\{0,1\}\), then \(a_i\) may have any label, while a zero at \(b_i\) is allowed only when \(a_i=2\). The one-page weight polynomial is
\[
B(x)=x+3x^2+2x^3+x^4=x(x^3+2x^2+3x+1).
\]
The zero-labeled spine vertex, when present, is already dominated by the other spine vertex labeled \(2\), so no cross-page condition remains. The four ordered spine choices with exactly one label \(2\) contribute
\[
2x^2(1+x)B(x)^n.
\]

Finally, if both spine vertices are labeled \(2\), every page label is unrestricted. This contributes
\[
x^4(1+x+x^2)^{2n}.
\]
The three regimes are disjoint and exhaustive, proving the displayed polynomial.

Setting \(x=1\) gives the total count. Inspecting the least nonzero power of \(x\) gives the minimum-weight statements. For \(n\ge3\), only the both-spines-labeled-\(2\) regime contributes at weight \(4\), and its weight-\(4\) term is unique.

## Verification
The accompanying `verify.py` independently constructs \(B_n\), enumerates every labeling in \(\{0,1,2\}^{V(B_n)}\) for \(1\le n\le5\), tests the Roman condition directly from adjacency, and compares the complete weight histogram with the closed formula coefficient by coefficient. It also checks the minimum weight, the number of minimum functions, and the closed total count.

A replay gives:

`VERIFY_OK n_range=1..5 labelings=597861 rdf_functions=180730 coefficient_checks=66 minimum_checks=5 total_checks=5 max_order=12`

The finite computation is corroborative; the proof above establishes the formula for every \(n\ge1\).

## Relationship to prior work
Yero and Rodríguez-Velázquez study the Roman domination number of Cartesian products. Their public preprint explicitly states that the bound \(\gamma_R(P_m\mathbin{\square}S_{1,r})\le 2m\) is tight for every \(r\ge2\). Setting \(m=2\) and using commutativity of the Cartesian product gives the already-known scalar value \(\gamma_R(B_r)=4\) for every \(r\ge2\). That scalar value is therefore not claimed as new here.

Gangabylaiah, Indiramma, Soner, and Alwardi introduce the Roman domination polynomial and compute it for several families and operations. The inspected full text treats complete graphs, stars, wheels, complete bipartite graphs, certain firefly graphs, joins, and a corona family. Full-text searches found no occurrence of “book” or “Cartesian,” and the listed operations do not specialize to the square book product in a way that yields the displayed formula.

Targeted database searches under “book graph,” “square book,” “star prism,” and \(K_{1,n}\mathbin{\square}P_2\) found no statement implying the all-weight formula. The closest returned polynomial results concern chain graphs and complete multipartite graphs, neither of which contains the square-book family as a special case for general \(n\).

## Limitations
The theorem concerns only the standard square-book family and ordinary Roman domination. It does not address triangular books, generalized books with a longer spine, total Roman domination, perfect Roman domination, or other Roman variants. The finite verifier covers only \(1\le n\le5\); it checks the symbolic argument but is not used as an infinite proof.

The literature comparison cannot exclude every differently named or poorly indexed treatment. In particular, “book graph” has multiple conventions, so residual bibliographic risk remains for sources indexed only under product or prism terminology. No such source was found in the targeted alias and implication searches, and the closest same-object product paper covers the scalar minimum rather than the all-weight distribution.

## References
1. I. G. Yero and J. A. Rodríguez-Velázquez, “Roman domination in Cartesian product graphs and strong product graphs,” arXiv:1111.3517v1 (2011); later published in *Applicable Analysis and Discrete Mathematics* 7 (2013), 262–274.
2. G. Deepak, M. H. Indiramma, N. D. Soner, and A. Alwardi, “On the Roman Domination Polynomial of Graphs,” *Bulletin of the International Mathematical Virtual Institute* 11(2) (2021), 355–365, DOI 10.7251/BIMVI2102355G.
