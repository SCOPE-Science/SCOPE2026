# Total Roman \(\{2\}\)-domination weight polynomial of half graphs

## Finding

For each integer \(n\ge2\), consider the half graph \(H_n\) with vertices \(a_1,\ldots,a_n,b_1,\ldots,b_n\) and an edge \(a_i b_j\) exactly when \(i\le j\). A **total Roman \(\{2\}\)-dominating function** is a map \(f:V(H_n)\to\{0,1,2\}\) such that every vertex labeled zero sees a sum of neighboring labels at least two and every positively labeled vertex has a positively labeled neighbor. Denote its weight by \(w(f)=\sum_v f(v)\), and let \(R_n(z)=\sum_f z^{w(f)}\) over all such functions.

Set \(A(z)=(1+z+z^2)^2\) and \(B(z)=z+z^2\). Then, with an empty sum interpreted as zero, the following holds for every \(n\ge2\):

\[
R_n(z)=z^4 A(z)^{n-1}
+2z^3\left(B(z)^{n-1}+\sum_{r=1}^{n-1}A(z)^{r-1}B(z)^{n-r+1}\right)
+z^2\left((n-1)B(z)^n+\sum_{d=0}^{n-3}(n-2-d)A(z)^dB(z)^{n+1-d}\right),
\]

Moreover, the ordinary generating function in graph size is the rational expression

\[
\sum_{n\ge2}R_n(z)u^{n-2}=
\frac{z^4A}{1-Au}
+2z^3\left(\frac{B}{1-Bu}+\frac{B^2}{(1-Au)(1-Bu)}\right)
+z^2\left(\frac{B^2}{(1-Bu)^2}+\frac{B^4u}{(1-Au)(1-Bu)^2}\right),
\]
where \(A=A(z)\) and \(B=B(z)\).

In particular, the exact number of functions is

\[
R_n(1)=\frac{121\cdot9^n+(189n-72)2^n}{441},
\]
so the probability that a uniformly random labeling by \(\{0,1,2\}\) qualifies converges to \(121/441\). The least possible weight is four. Exactly four minimum-weight functions exist when \(n=2\); for every \(n\ge3\), exactly one exists: assign label two to \(a_1\) and \(b_n\) and label zero everywhere else.

## Assumptions and scope

All graphs are finite, simple and undirected. The graph \(H_n\) is labeled by its two indexed bipartition classes, with \(n\ge2\). No connectedness assumptions beyond its explicit construction or restrictions on the internal vertex labels are imposed. Counting functions, rather than their automorphism orbits, is essential. The \(\{2\}\) in the parameter name refers to the required neighbor-label sum at zeros; this is distinct from ordinary Roman domination, which requires a neighbor labeled two.

## Proof

**Endpoint lemma.** Every valid function labels \(a_1\) and \(b_n\) positively. Indeed, \(b_1\) has sole neighbor \(a_1\). If \(a_1\) had label zero, then a positive \(b_1\) would lack a positive neighbor, while a zero \(b_1\) would have neighbor-label sum zero. Hence \(a_1>0\), and the symmetric degree-one argument forces \(b_n>0\). Conversely, when both endpoints are positive, every vertex having a positive label has a positive neighbor: each \(a_i\) is adjacent to \(b_n\), and each \(b_j\) is adjacent to \(a_1\). Thus the total-support condition is automatic, and only the inequalities at zero vertices remain.

Partition valid functions by their ordered endpoint labels \((f(a_1),f(b_n))\in\{1,2\}^2\).

**Case \((2,2)\).** Every zero on either side is adjacent to an endpoint labeled two. The remaining \(2n-2\) vertex labels may be chosen freely, contributing \(z^4(1+z+z^2)^{2n-2}=z^4A^{n-1}\).

**Case \((2,1)\).** Every zero on the \(b\)-side is already protected by \(a_1=2\). Let \(r\) be the largest index less than \(n\) for which \(f(b_r)>0\), taking \(r=0\) if there is none. If \(r=0\), each \(a_i\) for \(i\ge2\) must be positive because its only positive \(b\)-neighbor is \(b_n=1\); the contribution is \(z^3B^{n-1}\). If \(1\le r\le n-1\), every \(a_i\) with \(i>r\) is forced positive, while every \(a_i\) with \(2\le i\le r\) is unrestricted: its \(b\)-suffix contains the positive \(b_r\) and the positive \(b_n\). The vertices \(b_1,\ldots,b_{r-1}\) are unrestricted; \(b_r\) is positive and \(b_{r+1},\ldots,b_{n-1}\) are zero. This contributes \(z^3A^{r-1}B^{n-r+1}\). The case \((1,2)\) has the same contributions by the index-reversing side-interchange automorphism.

**Case \((1,1)\).** Since \(a_n\) has only the \(b_n\) neighbor of label one, \(a_n\) must be positive; likewise \(b_1\) is positive. Define \(L\) as the smallest index in \(\{2,\ldots,n\}\) of a positive \(a\)-vertex and \(R\) as the largest index in \(\{1,\ldots,n-1\}\) of a positive \(b\)-vertex. The labeling is valid exactly when \(L\le R+1\): a zero \(a_i\) below \(L\) needs the positive \(b_R\) in addition to \(b_n\), whereas a zero \(b_j\) above \(R\) needs the positive \(a_L\) in addition to \(a_1\). The two constraints are both equivalent to the displayed inequality. When \(L=R+1\), all \(n\) interior labels are forced positive, with \(n-1\) choices of \(R\), contributing \(z^2(n-1)B^n\). Otherwise, write \(d=R-L\ge0\). For each \(d\in\{0,\ldots,n-3\}\), there are \(n-2-d\) choices of \(L\), exactly \(2d\) interior labels are unrestricted and \(n+1-d\) are forced positive. The contribution is \(z^2(n-2-d)A^d B^{n+1-d}\). These cases partition all valid labelings uniquely and prove the finite-sum formula.

To obtain the rational expression, sum the first contribution as a geometric series in \(Au\); the \(B^{n-1}\) term as a geometric series in \(Bu\); the indexed products as convolutions of the two geometric series; and the linearly weighted terms as derivatives of geometric series. The resulting six terms combine exactly as displayed. Set \(z=1\), so \(A=9\) and \(B=2\), and perform partial fractions (or evaluate the finite geometric sums) to obtain \(R_n(1)\). Dividing by \(3^{2n}=9^n\) gives the probability limit. Finally \(A\) has constant term one and \(B\) has smallest exponent one; all terms except the \((2,2)\) term have order at least five for \(n\ge3\), so its single coefficient at \(z^4\) is the unique minimizer. At \(n=2\), direct extraction from the formula gives coefficient four at \(z^4\).

## Verification

The included `verify.py` uses only Python's standard library. It computes exact integer coefficient arrays from the finite-sum formula, separately enumerates and checks every one of the \(3^{2n}\) labelings directly against graph neighborhoods for \(2\le n\le7\), and independently computes the polynomial with a nine-boundary-state transfer method for \(2\le n\le18\). These methods agreed. There were 5,380,830 exhaustively tested direct assignments. The captured output in `verification_output.txt` includes the tested ranges and assertions. Finite checks corroborate but do not replace the proof for arbitrary \(n\).

## Relationship to prior work

The 2019 foundational paper and the 2021 open manuscript on total Roman \(\{2\}\)-domination establish the underlying concept and scalar relationships; these definitions and earlier bounds are not new here. Previously published weight enumerators for ordinary Roman domination on chain graphs and Roman \(\{2\}\)-domination on complete multipartite graphs consider different constraints or different graph classes. Unlike the former, the present polynomial permits two neighboring ones to protect a zero and imposes total support; unlike the latter, the half graph has strictly nested, nonidentical bipartite neighborhoods for \(n\ge3\). The present result counts the whole distribution of total Roman \(\{2\}\)-dominating functions, not merely the minimum weight. No mathematical priority or independent certification is asserted.

## Limitations

The formulas apply specifically to labeled half graphs \(H_n\) for \(n\ge2\); they do not furnish an equivalent polynomial for arbitrary chain graphs or other Italian/Roman domination variants. The originality comparison uses the accessible primary-paper text and pertinent published summaries; an unindexed or implicitly equivalent earlier enumerator is possible. Exact computational verification ends at \(n=18\) (direct exhaustive enumeration at \(n=7\)).

## References

1. J. A. Cabrera García, A. Cabrera Martínez, F. A. Hernández Mira, and I. G. Yero, *Total Roman \(\{2\}\)-domination in graphs*, published online 28 November 2019, DOI: 10.2989/16073606.2019.1695230. Preprint arXiv:2101.02537.
2. H. G. Ahangar, M. Chellali, S. M. Sheikholeslami, and J. C. Valenzuela-Tripodoro, *Total Roman \(\{2\}\)-Dominating Functions in Graphs*, DOI: 10.7151/dmgt.2316.
3. *Roman domination polynomial of chain graphs*, published mathematical research record (2026).
4. *Weight enumerator of all Roman \(\{2\}\)-dominating functions on complete multipartite graphs*, published mathematical research record (2026).
5. *Exact weight enumerator of total Roman dominating functions on complete multipartite graphs*, published mathematical research record (2026).
