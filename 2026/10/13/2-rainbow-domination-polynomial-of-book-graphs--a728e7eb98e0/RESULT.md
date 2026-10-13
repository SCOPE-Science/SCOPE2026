# 2-rainbow domination polynomial of book graphs

## Finding
For every integer \(n\ge1\), let \(B_n=K_{1,n}\mathbin{\square}P_2\) be the \(n\)-page square book graph. A \(2\)-rainbow dominating function is a map
\[
f:V(B_n)\longrightarrow \{\emptyset,\{1\},\{2\},\{1,2\}\}
\]
such that every vertex \(v\) with \(f(v)=\emptyset\) satisfies
\[
\bigcup_{u\in N(v)}f(u)=\{1,2\}.
\]
Its weight is \(w(f)=\sum_{v\in V(B_n)}|f(v)|\), and define
\[
\mathcal R_2(B_n;x)=\sum_f x^{w(f)}.
\]

Put
\[
A_0(x)=x^4+4x^3+6x^2,\qquad A_1(x)=x^3+3x^2,
\]
\[
B_j(x)=x^4+4x^3+6x^2+jx\quad (j\in\{1,2,3\}),\qquad B_4(x)=(1+x)^4.
\]
Then
\[
\mathcal R_2(B_n;x)
=A_0(x)^n-4(1+x)A_1(x)^n+6x^{2n}
+4xB_1(x)^n+6x^2B_2(x)^n+4x^3B_3(x)^n+x^4B_4(x)^n.
\]

At \(x=1\), the exact total number of \(2\)-rainbow dominating functions is
\[
11^n-8\cdot4^n+6+4\cdot12^n+6\cdot13^n+4\cdot14^n+16^n.
\]
The minimum weight and the number of minimum functions are
\[
(\gamma_{r2}(B_n),m_n)=
\begin{cases}
(2,4),&n=1,\\
(3,4),&n=2,\\
(4,5),&n=3,\\
(4,1),&n\ge4.
\end{cases}
\]

There is also an equivalent ordinary-domination statement. For every graph \(G\), selecting \((v,i)\) in the \(K_2\)-fiber exactly when \(i\in f(v)\) is a weight-preserving bijection between \(2\)-rainbow dominating functions on \(G\) and dominating sets of \(G\mathbin{\square}K_2\). Since \(P_2=K_2\) and \(K_2\mathbin{\square}K_2=C_4\), the displayed polynomial is also the ordinary domination polynomial of \(K_{1,n}\mathbin{\square}C_4\).

## Assumptions and scope
Graphs are finite, simple, and undirected. The book graph has spine vertices \(s,t\) joined by an edge and, for each page \(i\), vertices \(a_i,b_i\) with edges \(sa_i\), \(a_ib_i\), and \(b_it\). The formula counts every \(2\)-rainbow dominating function by total label cardinality; it is not merely a formula for the minimum weight.

The statement is proved for every integer \(n\ge1\). No asymptotic assumption or computation-dependent cutoff is used.

## Proof
Encode \(\emptyset,\{1\},\{2\},\{1,2\}\) by their color subsets. Fix the spine labels \(p=f(s)\) and \(q=f(t)\). For one page write \(\alpha=f(a_i)\) and \(\beta=f(b_i)\). The two degree-two page vertices impose exactly
\[
\alpha=\emptyset\Longrightarrow p\cup\beta=\{1,2\},
\qquad
\beta=\emptyset\Longrightarrow q\cup\alpha=\{1,2\}.
\]
Once \(p,q\) are fixed, these are page-local conditions. The only nonlocal conditions occur when a spine label is empty:
\[
p=\emptyset\Longrightarrow q\cup\bigcup_i\alpha_i=\{1,2\},
\qquad
q=\emptyset\Longrightarrow p\cup\bigcup_i\beta_i=\{1,2\}.
\]
Thus the pages become independent after inclusion-exclusion over colors missing from the two displayed unions.

A direct enumeration of the sixteen ordered choices for \((p,q)\), with inclusion-exclusion only when a spine label is empty, gives the following grouped contributions:
\[
\begin{array}{c|c}
\text{spine-label type}&\text{contribution over all \(n\) pages}\\ \hline
(\emptyset,\emptyset)&A_0(x)^n-4A_1(x)^n+6x^{2n}\\
\text{one empty, one singleton}&4x\bigl(B_1(x)^n-A_1(x)^n\bigr)\\
\text{one empty, one doubleton, or two singletons}&6x^2B_2(x)^n\\
\text{one singleton, one doubleton}&4x^3B_3(x)^n\\
\text{two doubletons}&x^4B_4(x)^n.
\end{array}
\]
For example, when both spine labels are empty, the local page polynomial before the two global coverage conditions is \(A_0(x)\). Forbidding one specified color from one required page-side union gives \(A_1(x)\); the four single-color omissions contribute \(-4A_1(x)^n\), and the six two-omission intersections contribute \(6x^{2n}\). The analogous one-spine-empty calculation gives \(B_1(x)^n-A_1(x)^n\). When neither relevant global coverage condition remains, the local page polynomials are \(B_2,B_3,B_4\) according to total spine-label weight. Summing the five rows yields the claimed formula.

Substituting \(x=1\) gives
\[
A_0(1)=11,\quad A_1(1)=4,\quad B_1(1)=12,\quad B_2(1)=13,\quad B_3(1)=14,\quad B_4(1)=16,
\]
which yields the total-count formula.

For \(n=1,2,3\), expansion of the proved polynomial gives lowest nonzero terms \(4x^2\), \(4x^3\), and \(5x^4\), respectively. For \(n\ge4\), the terms involving \(A_0,A_1,x^{2n},B_1,B_2,B_3\) all have degree at least \(5\), whereas \(x^4B_4(x)^n\) has constant-in-\(B_4\) contribution exactly \(x^4\). Hence the minimum term is exactly \(x^4\) with coefficient \(1\).

Finally, for the prism correspondence, from a \(2\)-rainbow function \(f\) on \(G\) form
\[
D_f=\{(v,i):i\in f(v)\}\subseteq V(G\mathbin{\square}K_2).
\]
If \(f(v)\ne\emptyset\), every unselected point in the fiber over \(v\) is adjacent to a selected point in that fiber. If \(f(v)=\emptyset\), both fiber points are dominated precisely when both colors occur among labels of neighbors of \(v\). Therefore \(f\mapsto D_f\) is a weight-preserving bijection with dominating sets.

## Verification
A standalone checker performs two independent finite consistency checks. First, it enumerates all \(4^{2+2n}\) labelings directly for \(1\le n\le4\), tests the graph definition vertex by vertex, and compares every polynomial coefficient with the closed form. Second, a page-state dynamic program tracks the two page-side color unions without inclusion-exclusion and compares every coefficient with the same closed form for \(1\le n\le10\). It also checks the ten minimum layers and seven displayed total counts.

Running `python3 verify.py` returns:

`VERIFY_OK brute_n=1..4 labelings=1118464 state_n=1..10 coefficient_checks=330 minimum_checks=10 total_checks=7 max_order=22`

These finite checks are not used as the proof for arbitrary \(n\); the all-\(n\) proof is the fixed-spine decomposition and inclusion-exclusion above.

## Relationship to prior work
Brešar, Henning, and Rall introduced rainbow domination in the graph-product setting in 2005. Brešar and Kraner Šumenjak subsequently stated the \(2\)-rainbow/prism equivalence and studied minimum \(2\)-rainbow domination numbers, including exact values for several graph classes. The present statement is an all-function weight enumerator, not merely a minimum-number calculation.

The prism equivalence makes the closest equivalent formulation the ordinary domination polynomial of \(K_{1,n}\mathbin{\square}C_4\). Searches under both the rainbow-domination language and this Cartesian-product domination-polynomial language did not locate a statement implying the displayed all-\(n\) polynomial. A published \(2\)-rainbow criticality paper on paths and cycles lists Mathematics Subject Classification \(05C69\), confirming the graph-domination classification used here.

A relevant public search result for complete multipartite graphs gives an all-function \(2\)-rainbow enumerator there, but book graphs \(B_n\) for \(n\ge2\) are not complete multipartite, so that result does not specialize to this family.

## Limitations
The 2007 paper most directly associated with the prism equivalence was available here through its abstract and bibliographic record, not through readable full text. Its abstract advertises exact minimum numbers rather than all-function weight polynomials, so it does not by itself imply the present enumerator; nevertheless, an unindexed or inaccessible family-specific enumeration remains a residual literature risk.

The result concerns \(2\)-rainbow domination only. It does not assert analogous formulas for \(k\)-rainbow domination with \(k>2\), nor for independent, total, or Roman rainbow variants.

## References
1. B. Brešar, M. A. Henning, D. F. Rall, “Paired-domination of Cartesian products of graphs and rainbow domination,” *Electronic Notes in Discrete Mathematics* 22 (2005), 233–237. DOI: 10.1016/j.endm.2005.06.059. Public publication date: 2005-10-15.
2. B. Brešar, T. Kraner Šumenjak, “On the 2-rainbow domination in graphs,” *Discrete Applied Mathematics* 155 (2007), 2394–2400. DOI: 10.1016/j.dam.2007.07.018.
3. B. Brešar, M. A. Henning, D. F. Rall, “Rainbow domination in graphs,” *Taiwanese Journal of Mathematics* 12 (2008), 213–225.
4. A. Bouchou, M. Blidia, “Criticality indices of 2-rainbow domination of paths and cycles,” *Opuscula Mathematica* 36 (2016), 563–574. DOI: 10.7494/OpMath.2016.36.5.563. Mathematics Subject Classification: 05C69.
