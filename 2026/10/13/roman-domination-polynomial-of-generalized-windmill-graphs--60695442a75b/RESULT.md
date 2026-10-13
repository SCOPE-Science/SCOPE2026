# Roman domination polynomial of generalized windmill graphs
## Finding
For integers \(n\ge 2\) and \(m\ge 2\), let \(W_{n,m}=K_1\vee nK_m\). Thus \(W_{n,m}\) has one center \(c\) adjacent to every other vertex, while the remaining \(nm\) vertices are partitioned into \(n\) pairwise anticomplete cliques of order \(m\), called blades.

A Roman dominating function is a labeling \(f:V(W_{n,m})\to\{0,1,2\}\) such that every vertex labeled \(0\) has a neighbor labeled \(2\). Its weight is \(\omega(f)=\sum_{v\in V}f(v)\). Define the full weight enumerator
\[
R(W_{n,m};x)=\sum_{f}x^{\omega(f)},
\]
where the sum is over all Roman dominating functions, and put
\[
Q_m(x)=(1+x+x^2)^m-(1+x)^m+x^m.
\]
Then
\[
R(W_{n,m};x)=x^2(1+x+x^2)^{nm}+(1+x)Q_m(x)^n-x^{nm}.
\]
In particular,
\[
\gamma_R(W_{n,m})=2,
\]
the minimum-weight Roman dominating function is unique, and the total number of Roman dominating functions is
\[
3^{nm}+2(3^m-2^m+1)^n-1.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The theorem is stated for \(n\ge2\) and \(m\ge2\), the nondegenerate generalized windmill range with at least two clique blades and at least one edge inside every blade. No claim is made here about minimal Roman dominating functions in the pointwise order; the enumerator counts every Roman dominating function, grouped only by weight.

## Proof
Let
\[
A_m(x)=(1+x+x^2)^m.
\]
This is the weight enumerator of all \(3^m\) labelings of one blade. Suppose first that the center is not labeled \(2\). A blade labeling is locally admissible exactly when either it has no vertex labeled \(0\), or it contains at least one vertex labeled \(2\). The forbidden blade labelings therefore use only labels \(0\) and \(1\) and contain at least one \(0\). Their weight enumerator is
\[
(1+x)^m-x^m.
\]
Hence the admissible blade polynomial is
\[
Q_m(x)=A_m(x)-((1+x)^m-x^m).
\]

Now partition all Roman dominating functions according to \(f(c)\).

If \(f(c)=2\), every peripheral vertex is already protected by the center, so all \(nm\) peripheral labels are free. This contributes
\[
x^2(1+x+x^2)^{nm}.
\]

If \(f(c)=1\), every blade must be admissible in the preceding sense, independently of all other blades. This contributes
\[
xQ_m(x)^n.
\]

If \(f(c)=0\), the same blade condition is necessary and sufficient for every peripheral zero-vertex. In addition, the center itself must have a neighbor labeled \(2\). Among the assignments counted by \(Q_m(x)^n\), the only assignment with no label \(2\) anywhere is the all-ones peripheral assignment: if a blade has no label \(2\), admissibility forbids label \(0\), so that entire blade is labeled \(1\). Its weight is \(nm\). Thus the center-zero contribution is
\[
Q_m(x)^n-x^{nm}.
\]

Adding the three disjoint cases gives
\[
R(W_{n,m};x)=x^2(1+x+x^2)^{nm}+(1+x)Q_m(x)^n-x^{nm}.
\]

For \(n\ge2\) and \(m\ge2\), the first term contributes exactly one function of weight \(2\), namely \(f(c)=2\) and all peripheral labels \(0\). The other two cases have larger weight, because every one of the at least two blades must satisfy the center-not-two admissibility condition. Therefore \(\gamma_R(W_{n,m})=2\) and the minimum function is unique. Finally, substituting \(x=1\) gives \(Q_m(1)=3^m-2^m+1\), yielding the stated total count.

## Verification
A standalone exhaustive checker constructs \(W_{n,m}\), enumerates every \(\{0,1,2\}\)-labeling, directly tests the Roman condition, and compares the resulting coefficient vector with the closed formula. It verifies parameter pairs \((n,m)=(2,1),(3,1),(4,1),(2,2),(3,2),(2,3)\), totaling \(4968\) labelings; the boundary values with \(m=1\) are included only as additional stress tests, not as part of the theorem's stated novelty domain. The checker also verifies the minimum weight, its uniqueness, and the closed total-count formula. The finite computation is a stress test, not the proof of the all-orders statement.

## Relationship to prior work
Cockayne, Dreyer, Hedetniemi, and Hedetniemi introduced and studied the Roman domination invariant in the form used here. Later Roman-domination literature places the topic primarily in MSC \(05C69\). The same generalized windmill family has been studied for total and paired domination, but those parameters do not determine Roman dominating functions or their weight distribution.

A recent enumeration line studies **minimal** Roman dominating functions and gives algorithms on broad graph classes such as split and cobipartite graphs. The present polynomial instead counts **all** Roman dominating functions by weight. Moreover, for \(m\ge2\), generalized windmills are neither split in general nor complete multipartite in the way required by existing complete-multipartite Roman-polynomial formulas: vertices inside one blade are adjacent, while vertices in distinct blades are nonadjacent. Targeted searches under the aliases “windmill”, “generalized windmill”, “friendship graph”, and the join description \(K_1\vee nK_m\) did not locate an equivalent all-weight formula.

## Limitations
The theorem is confined to generalized windmills with \(n\ge2\) and \(m\ge2\). It does not classify pointwise-minimal Roman dominating functions, nor does it assert a general formula for arbitrary block graphs or arbitrary joins. The literature comparison is necessarily finite: an unindexed source could contain an equivalent formula, although the checked same-object and broader enumeration sources do not imply it.

## References
1. E. J. Cockayne, P. A. Dreyer Jr., S. M. Hedetniemi, and S. T. Hedetniemi, “Roman domination in graphs,” *Discrete Mathematics* 278 (2004), 11–22. DOI: 10.1016/j.disc.2003.06.004.
2. E. W. Chambers, W. B. Kinnersley, N. Prince, and D. B. West, “Extremal Problems for Roman Domination,” *SIAM Journal on Discrete Mathematics* 23 (2009), 1575–1586. DOI: 10.1137/070699688.
3. P. Eakawinrujee and N. Trakultraipruk, “Total and paired domination numbers of windmill graphs,” *Asian-European Journal of Mathematics* (2023). DOI: 10.1142/S1793557123501231.
4. F. N. Abu-Khzam, H. Fernau, and K. Mann, “Roman Census: Enumerating and Counting Roman Dominating Functions on Graph Classes,” arXiv:2208.05261.
