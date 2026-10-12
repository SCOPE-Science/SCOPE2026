# Roman domination polynomial of crown graphs
## Finding
For every integer \(n\ge 3\), let the crown graph \(\operatorname{Cr}_n\) have bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
with every edge between \(A\) and \(B\) except the matching edges \(a_i b_i\). Equivalently, \(\operatorname{Cr}_n=K_{n,n}-M_n\).

A Roman dominating function is a map \(f:V(\operatorname{Cr}_n)\to\{0,1,2\}\) such that every vertex with label \(0\) has a neighbor with label \(2\). Its weight is \(w(f)=\sum_v f(v)\), and
\[
R(\operatorname{Cr}_n;x)=\sum_f x^{w(f)}
\]
sums over all Roman dominating functions.

Define
\[
H_n(x)=(1+x+x^2)^n-(1+x)^n-nx^2(1+x)^{n-1}
\]
and
\[
Q_n(x)=(x+x^2)(1+x+x^2)^{n-1}-(x+x^2)(1+x)^{n-1}-(n-1)x^3(1+x)^{n-2}.
\]
Then
\[
\begin{aligned}
R(\operatorname{Cr}_n;x)={}&x^{2n}+2n x^{n+2}(1+x)^{n-1}
+2x^n(1+x)^n\bigl((1+x)^n-1-nx\bigr)\\
&+n x^4(1+x)^{2n-2}+n(n-1)x^6(1+x)^{2n-4}\\
&+2n x^2(1+x)^{n-1}Q_n(x)+H_n(x)^2.
\end{aligned}
\]
In particular,
\[
\gamma_R(\operatorname{Cr}_n)=4,
\]
and exactly \(n\) Roman dominating functions have minimum weight: for each \(i\), label \(a_i\) and \(b_i\) by \(2\) and every other vertex by \(0\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The result is stated for \(n\ge 3\), where \(\operatorname{Cr}_n\) is connected. The exceptional graph \(\operatorname{Cr}_2\cong 2K_2\) is deliberately excluded from the minimum-function statement.

For a labeling \(f\), put
\[
p=|\{i:f(a_i)=2\}|,\qquad q=|\{i:f(b_i)=2\}|.
\]
The deleted matching is indexed: \(a_i\) is adjacent to every \(b_j\) except \(b_i\), and symmetrically for \(b_i\).

## Proof
The Roman condition can be read side by side. If \(q=0\), then no vertex of \(A\) may receive label \(0\). If \(q=1\), say \(b_j\) is the unique vertex of \(B\) carrying label \(2\), then the only vertex of \(A\) not adjacent to a \(2\) in \(B\) is \(a_j\), so \(a_j\) must be nonzero and every other vertex of \(A\) is unrestricted. If \(q\ge2\), then every \(a_i\) sees some \(2\) in \(B\), so \(A\) is unrestricted. The same three statements hold after exchanging \(A\) and \(B\). These conditions are necessary and sufficient.

Partition all Roman dominating functions by the pair \((p,q)\).

When \((p,q)=(0,0)\), every vertex is nonzero and the contribution is \(x^{2n}\).

When exactly one of \(p,q\) equals \(1\) and the other equals \(0\), choosing the unique \(2\), forcing the opposite side to be entirely nonzero, and leaving the remaining vertices on the \(2\)-side in \(\{0,1\}\) gives
\[
2n x^{n+2}(1+x)^{n-1}.
\]

When one of \(p,q\) is \(0\) and the other is at least \(2\), the side with no \(2\) is entirely nonzero while the other side is any \(\{0,1,2\}\)-labeling containing at least two \(2\)'s. This gives
\[
2x^n(1+x)^n\bigl((1+x)^n-1-nx\bigr).
\]

Suppose \(p=q=1\). If the two unique \(2\)'s have the same deleted-matching index, the two matched vertices already are nonzero and all other vertices may be \(0\) or \(1\), contributing
\[
n x^4(1+x)^{2n-2}.
\]
If their indices are different, each unique \(2\) leaves its matched opposite vertex undefended, so those two vertices must be nonzero. This contributes
\[
n(n-1)x^6(1+x)^{2n-4}.
\]

The polynomial \(H_n(x)\) counts arbitrary labelings of one side with at least two vertices labeled \(2\): subtract from \((1+x+x^2)^n\) the labelings with no \(2\), and those with exactly one \(2\). Hence the regime \(p,q\ge2\) contributes \(H_n(x)^2\).

Finally, fix a distinguished vertex on one side that is forced nonzero because it is matched to the unique \(2\) on the other side. The polynomial \(Q_n(x)\) counts labelings of that side with the distinguished vertex nonzero and at least two \(2\)'s. Indeed, start with \((x+x^2)(1+x+x^2)^{n-1}\), subtract the no-\(2\) labelings \((x+x^2)(1+x)^{n-1}\), and subtract the exactly-one-\(2\) labelings whose unique \(2\) is not distinguished, namely \((n-1)x^3(1+x)^{n-2}\). Therefore the two asymmetric regimes \((1,\ge2)\) and \((\ge2,1)\) contribute
\[
2n x^2(1+x)^{n-1}Q_n(x).
\]
Adding the seven disjoint regimes gives the displayed formula.

For \(n\ge3\), every displayed regime has weight at least \(4\). Weight \(4\) occurs only in the equal-index \((1,1)\) regime, by choosing no additional positive labels. There are exactly \(n\) choices of the common index. This proves both \(\gamma_R(\operatorname{Cr}_n)=4\) and the minimum-function count.

## Verification
The standalone checker `verify.py` enumerates every labeling \(V(\operatorname{Cr}_n)\to\{0,1,2\}\) for \(3\le n\le6\), tests the Roman condition directly from adjacency, constructs the claimed polynomial by integer polynomial arithmetic, and compares every coefficient. It also checks the minimum nonzero degree and its coefficient.

A replay of the packaged checker produced:

`VERIFY_OK n_range=3..6 labelings=597780 coefficient_checks=76 minimum_checks=4 max_order=12`

This finite replay is a stress test, not the proof for arbitrary \(n\); the all-orders argument is the preceding disjoint case classification.

## Relationship to prior work
Cockayne, Dreyer, Hedetniemi, and Hedetniemi introduced and studied Roman domination in the foundational 2004 paper cited below. Gangabylaiah, Indiramma, Soner, and Alwardi later introduced the Roman domination polynomial and gave formulas for several graph families and operations. Their full text includes a formula for the complete bipartite graph \(K_{n,m}\), but the crown graph is not complete bipartite: deleting one perfect matching creates the index-sensitive exceptional vertices used in the proof above. A full-text search of that paper found no crown-graph treatment.

Targeted searches under the aliases “crown graph,” “\(K_{n,n}\) minus a perfect matching,” and “complete bipartite graph minus a one-factor” did not locate a published formula equivalent to the theorem above. A published restrained-domination profile for crown graphs concerns a different invariant and does not imply the Roman-function weight enumerator. These searches reduce, but do not eliminate, the possibility of differently indexed prior work.

## Limitations
The theorem does not address \(n=2\), other deleted matchings in unbalanced complete bipartite graphs, or other Roman-domination variants. The originality comparison is necessarily limited by indexing and access: literature using an unexpected synonym for crown graphs could have escaped the searches. No claim of uniqueness in the literature is made.

## References
1. E. J. Cockayne, P. A. Dreyer Jr., S. M. Hedetniemi, and S. T. Hedetniemi, “Roman domination in graphs,” *Discrete Mathematics* 278 (2004), 11–22. DOI: 10.1016/j.disc.2003.06.004.
2. D. Gangabylaiah, I. M. H., N. D. Soner, and A. Alwardi, “On the Roman domination polynomial of graphs,” *Bulletin of the International Mathematical Virtual Institute* 11(2) (2021), 355–365. DOI: 10.7251/BIMVI2102355G.
