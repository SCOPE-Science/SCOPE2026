# Total Roman weight enumerator of crown graphs

## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-M_n
\]
be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted perfect matching \(\{a_i b_i:1\le i\le n\}\). A total Roman dominating function is a labeling \(f:V(\operatorname{Cr}_n)\to\{0,1,2\}\) in which every vertex labeled \(0\) has a neighbor labeled \(2\), and the vertices with positive labels induce a graph without isolated vertices. Its weight is \(\omega(f)=\sum_v f(v)\).

Define
\[
A_n(x)=(1+x)^n-1-nx,
\]
\[
C_n(x)=x^2\big((1+x)^{n-1}-1\big),
\]
\[
H_n(x)=(1+x+x^2)^n-(1+x)^n-nx^2(1+x)^{n-1},
\]
and
\[
R_n(x)=x(1+x)\big((1+x+x^2)^{n-1}-(1+x)^{n-1}\big)-(n-1)x^3(1+x)^{n-2}.
\]
Then the complete weight enumerator
\[
\mathcal T_n(x)=\sum_f x^{\omega(f)}
\]
over all total Roman dominating functions on \(\operatorname{Cr}_n\) is
\[
\begin{aligned}
\mathcal T_n(x)={}&x^{2n}+2n x^{n+2}\big((1+x)^{n-1}-1\big)+2x^nA_n(x)^2\\
&+n x^4\big((1+x)^{n-1}-1\big)^2+n(n-1)x^6(1+x)^{2n-4}\\
&+2nC_n(x)R_n(x)+H_n(x)^2.
\end{aligned}
\]
Consequently,
\[
\gamma_{tR}(\operatorname{Cr}_n)=6
\]
for every \(n\ge3\). The coefficient of \(x^6\), equivalently the number of minimum-weight functions, is \(31\) for \(n=3\), and
\[
n^2(n-1)
\]
for every \(n\ge4\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The result is for the standard crown graph \(K_{n,n}-M_n\) with \(n\ge3\). The polynomial variable records total Roman weight, not cardinality of the positive support.

The formula counts every feasible labeling, not only minimum ones. Finite exhaustive computation is used only as a regression check; the arbitrary-order statement is established by the case analysis below.

## Proof
For a labeling \(f\), let \(t_A\) and \(t_B\) be the numbers of vertices labeled \(2\) in \(A\) and \(B\), respectively. Two elementary facts drive the classification.

First, zero protection across the deleted matching is controlled only by the opposite number of label-\(2\) vertices. If \(t_B=0\), then no vertex of \(A\) may be labeled \(0\). If \(t_B=1\), say the unique label \(2\) is \(b_j\), then the only vertex of \(A\) not adjacent to that defender is \(a_j\), so \(a_j\) must be positive. If \(t_B\ge2\), every zero in \(A\) sees a label \(2\). The symmetric statement holds with \(A\) and \(B\) interchanged.

Second, the positive support has no isolated vertex exactly when every positive vertex sees a positive vertex in the opposite part. If the opposite part has at least two positive vertices, this is automatic because each vertex misses only its matched partner. If the opposite part has exactly one positive vertex, at index \(j\), then a positive vertex at the same index on the first side would be isolated.

Partition the labelings by \((t_A,t_B)\in\{0,1,\ge2\}^2\).

1. If \(t_A=t_B=0\), zero protection forces every vertex to be positive, hence every label is \(1\). The contribution is \(x^{2n}\).

2. Suppose \(t_A=0\) and \(t_B=1\), with the unique label \(2\) at \(b_j\). The whole of \(B\) must be positive. On \(A\), the vertex \(a_j\) must be positive, and at least one further vertex must be positive so that \(b_j\) is not isolated. Thus the contribution for this orientation is
\[
nx^{n+2}\big((1+x)^{n-1}-1\big).
\]
The transpose doubles it.

3. Suppose \(t_A=0\) and \(t_B\ge2\). Again all of \(B\) is positive. The side \(A\) must contain at least two positive vertices; its enumerator is
\[
A_n(x)=(1+x)^n-1-nx.
\]
The fully positive side \(B\) with at least two labels \(2\) has enumerator \(x^nA_n(x)\). The two orientations therefore contribute \(2x^nA_n(x)^2\).

4. Suppose \(t_A=t_B=1\), and the two labels \(2\) have the same index. Each of them is nonadjacent to the other, so each side needs at least one additional positive vertex. This contributes
\[
nx^4\big((1+x)^{n-1}-1\big)^2.
\]

5. Suppose \(t_A=t_B=1\), at distinct indices \(i\) and \(j\). Zero protection forces \(a_j\) and \(b_i\) to be labeled \(1\); after that, each side already has two positive vertices, so the remaining \(2n-4\) vertices are independently labeled \(0\) or \(1\). This contributes
\[
n(n-1)x^6(1+x)^{2n-4}.
\]

6. Suppose one side has exactly one label \(2\), at index \(i\), and the other side has at least two. On the single-defender side, at least one additional positive vertex is required, giving
\[
C_n(x)=x^2\big((1+x)^{n-1}-1\big).
\]
On the multi-defender side, the vertex at the distinguished index \(i\) must be positive. Its enumerator is
\[
\begin{aligned}
R_n(x)={}&x^2\big((1+x+x^2)^{n-1}-(1+x)^{n-1}\big)\\
&+x\big((1+x+x^2)^{n-1}-(1+x)^{n-1}-(n-1)x^2(1+x)^{n-2}\big)\\
={}&x(1+x)\big((1+x+x^2)^{n-1}-(1+x)^{n-1}\big)\\
&-(n-1)x^3(1+x)^{n-2}.
\end{aligned}
\]
There are \(n\) choices of \(i\) and two orientations, producing \(2nC_n(x)R_n(x)\).

7. Finally, if \(t_A,t_B\ge2\), both zero protection and the no-isolated-positive condition are automatic. The one-side enumerator for a labeling with at least two labels \(2\) is
\[
H_n(x)=(1+x+x^2)^n-(1+x)^n-nx^2(1+x)^{n-1},
\]
so this case contributes \(H_n(x)^2\).

The seven contributions are disjoint and exhaustive, proving the polynomial identity.

Every term has degree at least \(6\). The two singleton-defender cases in items 4 and 5 contribute at weight \(6\) for every \(n\ge3\), so \(\gamma_{tR}(\operatorname{Cr}_n)=6\). For \(n\ge4\), the coefficient of \(x^6\) is
\[
n(n-1)^2+n(n-1)=n^2(n-1).
\]
When \(n=3\), the all-one labeling contributes one additional weight-\(6\) function, and item 2 contributes \(2n(n-1)=12\) more. Together with the \(18\) singleton-defender functions, this gives \(31\).

## Verification
The standalone checker `artifacts/verify.py` independently enumerates every labeling of \(\operatorname{Cr}_n\) for \(3\le n\le6\), tests the total Roman predicate directly from adjacency, recomputes the closed polynomial from the displayed formula, and compares all coefficients and the minimum layer.

Its expected terminal line is:

`VERIFY_OK n_range=3..6 labelings=597780 valid_functions=410530 coefficient_checks=52 minimum_checks=4 max_order=12`

The computation covers \(597780\) labelings, but it is finite corroboration only. The proof for arbitrary \(n\) is the exhaustive symbolic classification above.

## Relationship to prior work
Liu and Chang introduced total \((a,b)\)-Roman domination in a general setting and proved complexity and algorithmic results, including bipartite graphs and strongly chordal graphs. Their publisher record was first public on 10 April 2012. Ahangar, Henning, Samodivkin, and Yero subsequently developed total Roman domination as a named graph parameter, proving general bounds and relationships with domination, total domination, and Roman domination; their paper uses MSC 05C69.

The closest broader coefficientwise comparison is the complete-bipartite case, but deleting a perfect matching changes the local defender condition at every paired index. In particular, for \(K_{n,n}\) one label \(2\) in each part gives total Roman weight \(4\), whereas the crown graph has minimum weight \(6\). The present formula records the full change at every weight rather than only this minimum shift.

The complete 2016 article was inspected for crown or complete-bipartite family formulas; neither phrase occurs in the searchable full text. A later complete article by Thakkar and Badiyani characterizes minimal total Roman dominating functions and studies vertex removal, but likewise contains no searchable crown or complete-bipartite occurrence. Targeted searches under crown, biclique-minus-matching, and all-function/weight-enumerator formulations did not locate an earlier crown-specific formula. This search evidence is supportive but not, by itself, a proof of historical uniqueness.

## Limitations
A poorly indexed source could use different terminology for the crown graph or for total Roman domination. The 2012 source was available here as publisher metadata and abstract rather than complete full text, so no whole-document noncoverage claim is made for it. The 2016 article was available in full text and was searched directly. The finite checker reaches order \(12\); it does not replace the arbitrary-order proof.

## References
C.-H. Liu and G. J. Chang, “Roman domination on strongly chordal graphs,” *Journal of Combinatorial Optimization* 26 (2013), 608–619. DOI: 10.1007/s10878-012-9482-y. First published online 10 April 2012.

H. Abdollahzadeh Ahangar, M. A. Henning, V. Samodivkin, and I. G. Yero, “Total Roman Domination in Graphs,” *Applicable Analysis and Discrete Mathematics* 10 (2016), 501–517. DOI: 10.2298/AADM160802017A.

D. K. Thakkar and S. M. Badiyani, “Total Roman Domination Number of Graphs,” *TWMS Journal of Applied and Engineering Mathematics* 12(2) (2022), 445–455.
