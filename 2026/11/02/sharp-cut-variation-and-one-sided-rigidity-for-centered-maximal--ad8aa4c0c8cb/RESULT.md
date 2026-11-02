# Sharp cut-variation and one-sided rigidity for centered maximal averages on complete bipartite graphs

## Finding

For every pair of integers \(m,n\ge2\), let \(K_{m,n}\) have independent vertex classes \(A\) and \(B\) of orders \(m\) and \(n\), respectively. Write \(N=m+n\), define the centered graph-ball maximal operator \(M\) and edge variation by
\[
(Mf)(v)=\max_{r=0,1,2}\frac{1}{|B(v,r)|}\sum_{w\in B(v,r)}|f(w)|,
\qquad
\operatorname{Var}(f)=\sum_{u\in A}\sum_{v\in B}|f(u)-f(v)|.
\]
For the natural class of nontrivial cut signals \(\mathbf1_S\), with \(\varnothing\ne S\subsetneq A\cup B\), the exact sharp variation gain is
\[
\boxed{\displaystyle
\mathcal C_{\mathrm{cut}}(m,n)=\max\{R_A,R_B\},\quad
R_A=\frac{m}{m+1}+\frac{(m-1)(n-1)}{(m+1)(m+n)},\quad
R_B=\frac{n}{n+1}+\frac{(m-1)(n-1)}{(n+1)(m+n)}.}
\]
An indicator of a single vertex of \(A\) realizes \(R_A\), and one of \(B\) realizes \(R_B\). More strongly, the sharp variation gain over **all nonzero real inputs supported on \(A\)** is exactly \(R_A\), with equality only when the support has one vertex; interchanging the classes gives \(R_B\).

There is an exact contraction/amplification phase boundary:
\[
\mathcal C_{\mathrm{cut}}(m,n)\begin{cases}
<1,&(m-2)(n-2)<3,\\
=1,&(m-2)(n-2)=3,\\
>1,&(m-2)(n-2)>3.
\end{cases}
\]
The equality boundary consists of \((m,n)=(3,5),(5,3)\). In the amplifying regime, when \(m<n\) a spike in the **smaller** class maximizes the gain; below the boundary a spike in the larger class does. Equal class orders give a tie. In particular, the centered maximal function can amplify graph total variation on the dense graphs \(K_{3,6}\) and \(K_{4,4}\). For balanced classes \(\mathcal C_{\mathrm{cut}}(r,r)\to3/2\), while
\[
\sup_{m,n\ge2}\mathcal C_{\mathrm{cut}}(m,n)=2,
\]
with the supremum not attained at any finite \((m,n)\).

There is also quantitative rigidity for inputs supported on one class. If \(f\ne0\) is supported on \(A\), set \(T=\sum_{u\in A}|f(u)|\), \(p_u=|f(u)|/T\), \(a=1/N\), \(b=1/(m+1)\), and
\[
\kappa_A=\min\{1-2b+a,\ 2b-a\}>0.
\]
Then
\[
\boxed{\displaystyle
R_A-\frac{\operatorname{Var}(Mf)}{\operatorname{Var}(f)}
\ge\kappa_A\sum_{u\in A}\min\{p_u,1-p_u\}.}
\]
In particular, a deficit less than \(\kappa_A\) forces one coordinate to carry at least half the absolute mass; its missing mass is at most the deficit divided by \(2\kappa_A\).

## Assumptions and scope

The graph is finite, simple, undirected, unweighted, and complete bipartite, with both classes nonempty and in the new theorem of order at least two. A graph ball uses combinatorial shortest-path distance and counting measure. The maximal operator averages \(|f|\), not signed \(f\). Variation counts every edge exactly once, without normalization. The cut problem ranges over every nonempty proper vertex subset. The one-sided problem ranges over every real-valued nonzero function vanishing identically on the opposite class. No statement about the full variation norm over arbitrary real signals supported on both classes is made.

## Proof

**1. All graph-ball averages.** For a nonnegative function taking values \(x_u\) on \(A\) and \(y_v\) on \(B\), let \(X=\sum_Ax_u\), \(Y=\sum_By_v\), and \(\mu=(X+Y)/N\). Since the graph has diameter two,
\[
(Mf)(u)=\max\{x_u,(x_u+Y)/(n+1),\mu\},\quad u\in A,
\]
\[
(Mf)(v)=\max\{y_v,(y_v+X)/(m+1),\mu\},\quad v\in B.
\]
These identities apply to arbitrary real inputs after replacing their values by absolute values.

**2. Exact gain for cut signals.** Put \(k=|S\cap A|\) and \(\ell=|S\cap B|\). The input variation is
\[
D=k(n-\ell)+(m-k)\ell>0.
\]
Every occupied vertex has maximal value one. Every unoccupied vertex of \(A\) has maximal value \(\alpha=\max\{\ell/(n+1),(k+\ell)/N\}\), and every unoccupied vertex of \(B\) has maximal value \(\beta=\max\{k/(m+1),(k+\ell)/N\}\). Write \(\mu=(k+\ell)/N\). The strict inequalities \(\alpha>\mu\) and \(\beta>\mu\) cannot both hold: they would require
\[
\ell(m-1)>k(n+1),\qquad k(n-1)>\ell(m+1),
\]
which are incompatible for nonnegative \(k,\ell\). If both equal \(\mu\), then \(\operatorname{Var}(M\mathbf1_S)/D=1-\mu\le1-1/N\le\max(R_A,R_B)\); the final inequality follows, for \(m,n\ge2\), from
\[
R_A-(1-1/N)=\frac{(m-2)(n-1)}{(m+1)N}\ge0
\]
and its class-swapped counterpart.

Suppose \(\alpha>\mu=\beta\). Counting the four kinds of cross-edges gives
\[
\frac{\operatorname{Var}(M\mathbf1_S)}D
=1-\mu+\frac{(m-k)(n-2\ell)}D(\alpha-\mu),
\qquad
\alpha-\mu=\frac{\ell(m-1)-k(n+1)}{(n+1)N}.
\]
If \(n-2\ell\le0\), the preceding baseline bound applies. Otherwise \(\ell\ge1\), \(D\ge(m-k)\ell\), and \(\alpha-\mu\le\ell(m-1)/((n+1)N)\); hence
\[
\frac{\operatorname{Var}(M\mathbf1_S)}D
\le 1-\frac{\ell}{N}+\frac{(n-2\ell)(m-1)}{(n+1)N}
\le 1-\frac1N+\frac{(n-2)(m-1)}{(n+1)N}=R_B.
\]
(The middle expression decreases strictly with \(\ell\).) If \(\beta>\mu=\alpha\), symmetry gives the bound \(R_A\). This proves the upper bound for **every** cut signal. A single occupied vertex in \(A\), respectively \(B\), has gain exactly \(R_A\), respectively \(R_B\), by direct substitution in the three averaging radii; thus the maximum is attained.

**3. Every real input supported on one class.** Suppose \(f|_B=0\) and \(f\ne0\), and set \(p_u=|f(u)|/T\), so \(\sum_Ap_u=1\). The three-radius formula reduces to
\[
(Mf)(u)=T\max\{p_u,a\},\qquad (Mf)(v)=Tb,
\quad a=1/N,\ b=1/(m+1).
\]
Since \(\operatorname{Var}(f)=nT\), the gain is \(\sum_{u\in A}g(p_u)\), where \(g(s)=|\max\{s,a\}-b|\), \(0\le s\le1\), and \(0<a<b\le1/3\). The chord \(c(s)=(1-s)g(0)+sg(1)\) lies strictly above \(g(s)\) for all \(0<s<1\): explicitly,
\[
c(s)-g(s)=
\begin{cases}
(1-2b+a)s,&0\le s\le a,\\
(2-2b+a)s-a,&a\le s\le b,\\
(2b-a)(1-s),&b\le s\le1.
\end{cases}
\]
Every branch is nonnegative and strictly positive in its open interior. Summing \(g(p_u)\le c(p_u)\) yields
\[
\sum_Ag(p_u)\le(m-1)g(0)+g(1)
=(m-1)(b-a)+1-b=R_A.
\]
Equality requires every \(p_u\in\{0,1\}\), hence a single nonzero coordinate. The analogous proof on \(B\) gives \(R_B\). Moreover, the displayed piecewise deficit satisfies
\[
c(s)-g(s)\ge\min\{1-2b+a,2b-a\}\min\{s,1-s\},
\]
which gives the claimed quantitative rigidity after summation. If the total deficit is below \(\kappa_A\), not all \(p_u\) can be below one half. For a coordinate with \(p_u\ge1/2\), the sum of the displayed minima is \(2(1-p_u)\), as asserted.

**4. Phase boundary and limits.** Elementary simplification gives
\[
R_A-1=\frac{\Delta}{(m+1)N},\qquad
R_B-1=\frac{\Delta}{(n+1)N},\quad
\Delta=(m-2)(n-2)-3,
\]
\[
R_A-R_B=\frac{(n-m)\Delta}{(m+1)(n+1)N}.
\]
These identities give the exact threshold, the two integer equality pairs, and the maximizing side. For balanced orders \(m=n=r\), the formula tends to \(3/2\). For finite \(m,n\), \(R_A<(2m-1)/(m+1)<2\) and similarly for \(R_B\), while the sequence \(m=j\), \(n=j^2\), \(j\to\infty\), makes \(R_A\to2\).

## Verification

The standalone `check_biclique.py` performs exact-rational tests of the graph-ball formulas, every cut-size pair on \(2\le m\le8\), \(2\le n\le9\), one-sided integer-coordinate signals on additional grids, and both phase-factor identities on \(2\le m,n\le100\). It completed 136,524 assertions. These finite checks test the hypotheses and algebra; they do not replace the all-integer and all-real proof above. Run with `python3 check_biclique.py` using Python's standard library only.

## Relationship to prior work

Soria and Tradacete (2014) develop the centered maximal operator on finite graphs and exact \(\ell^p\)/restricted-type **magnitude norms**, but do not establish the present \(\mathrm{BV}\) cut-variation invariant. Kurka (2012) studies variation bounds for centered maxima on the real line, not complete bipartite graph cuts. González-Riquelme and Madrid (2020) prove sharp graph-variation inequalities for complete and star graphs, including their \(p=1\) results; the star cases here are consistent boundary cases, not new claims. The later paper of Liu and Xue on finite-graph variation was located by bibliographic data and abstracts, but its complete primary text could not be inspected; this leaves a publication-priority risk concerning possible hidden equivalent calculations. The present claim is specifically the exact **all-cut-signal** norm and the separate **all-one-sided-real-signal** norm, with the sharp bipartite threshold and rigidity; it is not an assertion of the full \(\mathrm{BV}\) operator norm.

## Limitations

No full all-input \(\mathrm{BV}\) inequality on \(K_{m,n}\) is proved or claimed. Cut signals and one-sided signals are special input classes, although each is maximized over completely and naturally motivated by graph cuts and bipartite concentration. The theorem uses unweighted counting measure and centered graph balls; it does not address unequal vertex weights, fractional maximal averages, uncentered balls, or variations with nonunit edge weights. Earlier unindexed or inaccessible specialist literature may contain equivalent formulas; independent publication-priority confirmation remains open.

## References

1. O. Kurka, *On the variation of the Hardy–Littlewood maximal function*, arXiv:1210.0496, initial posting 2012-10-01; Ann. Acad. Sci. Fenn. Math. 40 (2015), 109–133.
2. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204, initial posting 2014-10-22; J. Math. Anal. Appl. 436 (2016), 661–682.
3. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146, initial posting 2020-05-06; J. Geom. Anal. 31 (2021), 9708–9744.
4. F. Liu and Q. Xue, *On the variation of the Hardy–Littlewood maximal functions on finite graphs*, Collect. Math. 72 (2021), 333–349, DOI:10.1007/s13348-020-00290-6. Full text was not available for inspection.
