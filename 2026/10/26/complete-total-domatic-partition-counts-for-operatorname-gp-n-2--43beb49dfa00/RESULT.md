# Complete total-domatic partition counts for \(\operatorname{GP}(n,2)\)

## Finding
For each integer \(n\ge5\), let \(G_n=\operatorname{GP}(n,2)\). Write \(D_r(n)\) for the number of **unordered** partitions of \(V(G_n)\) into exactly \(r\) nonempty total dominating sets. Then \(D_1(n)=1\), \(D_r(n)=0\) for \(r\ge4\), and
\[
D_2(n)=-\frac12[z^n]\frac{zF'(z)}{F(z)},\qquad
D_3(n)=\begin{cases}1&3\mid n,\\0&3\nmid n.\end{cases}
\]
Here the completely explicit polynomial of degree \(64\) is
\[
F(z)=(1-z^2)^4(1-2z^2-z^6)(1+2z^4-z^6)P_{20}(z)P_{24}(z),
\]
with
\[
\begin{aligned}
P_{20}(z)={}&1-z+z^2-4z^3-5z^4-8z^5-9z^6-13z^7-17z^8-22z^9\\
&-42z^{10}-22z^{11}-17z^{12}-13z^{13}-9z^{14}-8z^{15}-5z^{16}\\
&-4z^{17}+z^{18}-z^{19}+z^{20},\\[3pt]
P_{24}(z)={}&1-z+5z^2-8z^3+25z^4-26z^5+85z^6-75z^7+172z^8\\
&-145z^9+269z^{10}-192z^{11}+323z^{12}-192z^{13}+269z^{14}\\
&-145z^{15}+172z^{16}-75z^{17}+85z^{18}-26z^{19}+25z^{20}\\
&-8z^{21}+5z^{22}-z^{23}+z^{24}.
\end{aligned}
\]
In particular the numbers of ordered two-colour valid assignments for \(n=5,\ldots,14\) are
\(12,116,226,1286,2486,5172,13202,23232,48128,121844\); divide each by two for \(D_2(n)\). The sole three-class partition when \(3\mid n\) consists of the three index-residue classes, each containing both vertices with the corresponding residue modulo three.

## Assumptions and scope
The vertices are \(u_i,v_i\) for \(i\in\mathbb Z/n\mathbb Z\). The edges are \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\) (undirected, with indices modulo \(n\)). For \(n\ge5\) this is a simple cubic graph. A total dominating set meets the **open** neighborhood of every vertex. A partition is unordered with no unnamed colours; its three-class version exists precisely when each of the three colours appears in each open neighborhood. All claims concern the fixed graph \(G_n\), not arbitrary generalized Petersen graphs.

## Proof
**Binary partitions and a finite transfer.** Give each vertex a colour in \(\{0,1\}\). The two colour classes are both total dominating exactly if, for every \(i\), neither of the triples
\[
(c(u_{i-1}),c(u_{i+1}),c(v_i)),\qquad
(c(u_i),c(v_{i-2}),c(v_{i+2}))
\]
is monochromatic. Encode one column \((c(u_i),c(v_i))\) by a symbol from \(\{0,1,2,3\}\), with the low bit the outer colour. Define an integer \(256\)-square zero-one matrix \(T\), whose states are four successive columns \((w_0,w_1,w_2,w_3)\). There is a directed transition to \((w_1,w_2,w_3,w_4)\) exactly when the two triples centred on \(w_2\) are nonmonochromatic in the five-column window. Thus every cyclic assignment of \(n\) columns, for \(n\ge5\), corresponds bijectively to one closed length-\(n\) walk in the state digraph, starting at its specified indexed column. If \(A_n\) denotes the number of named two-colour assignments, then
\[
A_n=\operatorname{tr}(T^n)\quad(n\ge5).
\]
The finite determinant identity
\[
\det(I-zT)=\exp\!\left(-\sum_{n\ge1}\operatorname{tr}(T^n)\frac{z^n}{n}\right)
\]
shows that \(\sum_{n\ge1}\operatorname{tr}(T^n)z^n=-z(\det(I-zT))'/\det(I-zT)\). The exact integer computation detailed in the verification file evaluates \(\det(I-zT)\) as the polynomial \(F(z)\) above. The computation uses Newton's identities for all \(256\) coefficients: with \(s_j=\operatorname{tr}(T^j)\), \(c_0=1\),
\[
c_k=-\frac1k\sum_{j=1}^k c_{k-j}s_j\quad(1\le k\le256).
\]
Its explicit finite algorithm constructs the \(256\) states, their \(576\) valid transitions, all integer power traces, and checks every coefficient against the displayed factors, including the zero coefficients after degree \(64\). This is an exact finite computation, not an extrapolation from initial terms. Exchanging the two colours acts without fixed points on a valid assignment; hence \(D_2(n)=A_n/2\).

**Three-class rigidity.** A valid named three-colour assignment uses each colour exactly once in every open neighbourhood. Identify colours with \(\mathbb F_3\) and put \(a_i=c(u_i)\), \(b_i=c(v_i)\). Summing colours in the two neighbourhoods gives
\[
b_i=-a_{i-1}-a_{i+1},\qquad
 a_i+b_{i-2}+b_{i+2}=0.
\]
Consequently \(a_i\) satisfies the invertible order-six recurrence
\[
a_{i+6}=a_{i+3}-a_{i+4}-a_{i+2}-a_i\pmod3.
\]
Its characteristic polynomial in \(\mathbb F_3[t]\) is
\[
t^6+t^4-t^3+t^2+1=(t-1)^2(t^4-t^3+t^2-t+1),
\]
and divides \(t^{30}-1\). Therefore every bi-infinite solution is \(30\)-periodic and determined by six consecutive values. Enumerating the \(3^6=729\) such initial sextuples, and checking the non-monochromatic constraints over a complete period, leaves exactly six sequences: \(a_i=b_i=\alpha+\beta i\pmod3\) with \(\alpha\in\mathbb F_3\) and \(\beta\in\{1,2\}\). The complete finite enumeration is reproduced in the standalone verifier. Such a sequence descends to indices modulo \(n\) exactly when \(3\mid n\). These six named colourings are colour permutations of the same unordered partition, proving the assertion for \(D_3(n)\).

No simple cubic graph admits four or more nonempty total-dominating colour classes, since every open neighbourhood has only three vertices. The one-class partition is valid because \(G_n\) has no isolated vertices. This finishes the complete partition census.

## Verification
Run \(\texttt{python3 verify_gp2.py}\) from the directory containing the standalone checker. Only the Python standard library is used. The checker builds the transfer matrix, calculates its exact determinant by all Newton identities, matches the degree-\(64\) factorization, and independently brute-forces every binary assignment for \(5\le n\le9\). It separately verifies the \(729\) universal ternary recurrence states. The observed output ends with `ALL_CHECKS_PASSED`. The finite ternary calculation establishes an all-order theorem because the recurrence itself forces period \(30\); the finite binary determinant establishes an all-order theorem through the trace identity.

## Relationship to prior work
Zelinka's 2002 treatment of generalized Petersen graphs establishes domatic and total-domatic *numbers*, including existence of two total dominating classes; it does not enumerate all two-class partitions. Zhao and coauthors (2020) discuss minimum total dominating sets and some related totals, but not the displayed two-class count for \(\operatorname{GP}(n,2)\). Minyard and Sepanski's 2024 preprint / 2026 paper classify generalized Petersen graphs that admit neighborhood 3-balanced colourings, proving the existence classification that is sharpened here to an exact count of three-class partitions. Choi, Kwon, and Park's September 2026 paper places two-coupon colourings and total-domatic number in the modern theory of cubic graphs, but does not present the present transfer enumerator. The rational two-class generating function is the central additional assertion; the three-class rigidity completes its interpretation as a full partition census. Independent historical priority verification is not claimed.

## Limitations
The proof does not give an equally compact formula for arbitrary \(\operatorname{GP}(n,k)\), nor for arbitrary cubic graphs, and it does not enumerate arbitrary total dominating sets individually. The degree-\(64\) factorization relies on the fully specified finite exact-integer computation rather than a conceptual spectral decomposition. The short initial values alone do not prove the factorization. Historical priority may depend on literature not found in the cited searches, and no independent audit is asserted.

## References
1. M. Choi, H. Kwon and B. Park, *Det-extremal cubic graphs and the total domatic number*, arXiv:2609.33902v1, first posted 2026-09-27, especially Section 1.2.
2. B. Zelinka, *Domination in generalized Petersen graphs*, Czechoslovak Mathematical Journal 52 (2002), 11–16, DOI:10.1023/A:1021759001873, especially Theorems 4–5.
3. T. Zhao, G. Ali, N. Hameed, S. I. A. Shah, Y.-M. Chu, *The Numerical Invariants concerning the Total Domination for Generalized Petersen Graphs*, Journal of Mathematics 2020, article 5473675, DOI:10.1155/2020/5473675.
4. M. Minyard and M. R. Sepanski, *Neighborhood Balanced 3-Coloring*, arXiv:2410.05422v1 (first posted 2024-10-07); published as *Neighborhood 3-Balanced Graphs*, Graphs and Combinatorics 42 (2026), article 50, DOI:10.1007/s00373-026-03038-4, Section 4.
