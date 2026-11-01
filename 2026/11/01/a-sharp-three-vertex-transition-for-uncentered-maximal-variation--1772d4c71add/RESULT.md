# A sharp three-vertex transition for uncentered maximal variation on balanced bicliques

## Finding

For each integer \(r\ge 2\), let \(K_{r,r}\) be the simple complete bipartite graph with both vertex classes of size \(r\), unit edge lengths, and counting measure on vertices. Let \(\widetilde M\) be the **uncentered graph-ball Hardy–Littlewood maximal operator**, so that
\[
(\widetilde M f)(v)=\max_{c\in V,\,s\in\{0,1,2\}:\,v\in B(c,s)}
\frac{1}{|B(c,s)|}\sum_{u\in B(c,s)}|f(u)|.
\]
For any vertex function \(h\), set \(\operatorname{Var}(h)=\sum_{uv\in E}|h(u)-h(v)|\). Among all nonconstant indicator functions \(\mathbf1_S\), the following exact variation gain holds:
\[
\boxed{\mathcal C_r^{\mathrm{cut}}:=\max_{\varnothing\ne S\subsetneq V}
\frac{\operatorname{Var}(\widetilde M\mathbf1_S)}{\operatorname{Var}(\mathbf1_S)}
=\max\left\{\frac r{r+1},\frac{4r^2-11r+8}{(r+1)(3r-4)}\right\}.}
\]
For \(2\le r\le5\), precisely the singleton indicators (up to graph automorphism) attain the maximum. For \(r\ge6\), precisely the indicators containing **one vertex of one class and two of the other** (up to graph automorphism and swapping classes) attain the maximum. Consequently,
\[
\boxed{\mathcal C_r^{\mathrm{cut}}<1\ (2\le r\le8),\qquad
\mathcal C_r^{\mathrm{cut}}>1\ (r\ge9).}
\]
The sequence is strictly increasing and approaches \(4/3\) from below. In particular, for every \(r\ge9\) the uncentered maximal operator fails edge-variation contraction even on indicator data, despite the graph being regular and bipartite.

## Assumptions and scope

The graph is finite, simple and unweighted. Every graph ball includes its center. Radius \(s=0\) gives a singleton, radius \(s=1\) gives one center plus all vertices in the opposite class, and radius \(s=2\) gives the whole graph. Uncentered means the ball center need only have the evaluation vertex in its ball. Edge variation counts each undirected edge once without normalization. The sharp optimization is **only over indicators** \(\mathbf1_S\); it is not an assertion about the sharp variation norm on arbitrary real inputs. Constant indicators are excluded because their variation vanishes.

## Proof

Write the two vertex classes as \(A\) and \(B\). Suppose \(\mathbf1_S\) is one on \(a\) vertices of \(A\) and \(b\) vertices of \(B\), where \(0\le a,b\le r\) and the data are nonconstant. By class symmetry suppose \(a\le b\). The input variation is
\[
D(a,b)=a(r-b)+b(r-a)=r(a+b)-2ab>0.
\]
Each input-one vertex has maximal value \(1\), because its radius-zero average is \(1\) and all indicator averages are at most \(1\). At an input-zero vertex in class \(A\) the possible maximal averages reduce to
\[
\alpha=\max\left\{\frac b{r+1},\frac{a+\mathbf1_{b>0}}{r+1},\frac{a+b}{2r}\right\};
\]
at an input-zero vertex in \(B\) they reduce to
\[
\beta=\max\left\{\frac a{r+1},\frac{b+\mathbf1_{a>0}}{r+1},\frac{a+b}{2r}\right\}.
\]
The terms arise from radius-one balls centered at the evaluation vertex, radius-one balls centered in the opposite class, and the radius-two whole-graph ball. No other ball is possible.

If \(a=0\) and \(1\le b\le r\), then \(\alpha=\beta=b/(r+1)\) wherever a zero input occurs, hence
\[
\frac{\operatorname{Var}(\widetilde M\mathbf1_S)}{\operatorname{Var}(\mathbf1_S)}
=1-\frac b{r+1}\le\frac r{r+1},
\]
with equality exactly for \(b=1\). If \(a=b\ge1\), with \(a=b=r\) excluded, then \(\alpha=\beta=(a+1)/(r+1)\). Indeed \(a/r\le(a+1)/(r+1)\) for \(a\le r\). The gain equals \((r-a)/(r+1)<r/(r+1)\).

It remains to consider \(1\le a<b\le r\). In this case
\[
\frac{a+b}{2r}\le\frac{b+1}{r+1},
\]
because \(2r(b+1)-(r+1)(a+b)\ge2(r-b)\ge0\). Therefore \(\beta=(b+1)/(r+1)\), while \(b/(r+1)\le\alpha\le\beta\). Summing the differences for the four kinds of bipartite edges gives
\[
\begin{aligned}
\operatorname{Var}(\widetilde M\mathbf1_S)
&=a(r-b)(1-\beta)+(r-a)b(1-\alpha)
+(r-a)(r-b)(\beta-\alpha)\\
&=D(a,b)+(r-b)(r-2a)\beta-r(r-a)\alpha.
\end{aligned}
\]
Since \(\alpha\ge b/(r+1)\), the gain is bounded by
\[
1+\frac{P(a,b)}{(r+1)D(a,b)},\qquad
P(a,b)=(r-b)(r-2a)(b+1)-r(r-a)b.
\]
The following **two exact polynomial identities** supply the global comparison; they can also be checked by direct expansion:
\[
\begin{aligned}
P(a,b)D(1,b)-P(1,b)D(a,b)&=-r^2(a-1)(r-b)\le0,\\
P(1,b)D(1,2)-P(1,2)D(1,b)
&=-(b-2)\big[b(3r-4)(r-2)+r(r^2-2)\big]\le0.
\end{aligned}
\]
All denominators \(D(a,b)\), \(D(1,b)\), and \(D(1,2)=3r-4\) are positive in the present range. Thus every mixed cut with \(a<b\) satisfies
\[
\frac{\operatorname{Var}(\widetilde M\mathbf1_S)}{\operatorname{Var}(\mathbf1_S)}
\le1+\frac{P(1,2)}{(r+1)D(1,2)}
=\frac{4r^2-11r+8}{(r+1)(3r-4)},
\]
using \(P(1,2)=r^2-10r+12\). For \(r\ge3\), the \((a,b)=(1,2)\) cut attains this bound: its zero-class values are exactly \(\alpha=2/(r+1)\), \(\beta=3/(r+1)\). For \(r=2\) this second bound need not be attained, but it is below the singleton value and does not affect the maximum.

Finally, subtracting the singleton branch from the mixed branch gives
\[
\frac{4r^2-11r+8}{(r+1)(3r-4)}-\frac r{r+1}
=\frac{r^2-7r+8}{(r+1)(3r-4)}.
\]
This is negative for integer \(2\le r\le5\) and positive for \(r\ge6\), establishing the sharp classification. Equality in the comparison for \(r\ge6\) forces \(b=2\) and \(a=1\); all remaining cases are strictly smaller. For \(r\le5\), the singleton bound is strictly larger than the mixed bound, and the singleton case is uniquely sharp up to automorphisms.

The sharp mixed branch exceeds \(1\) exactly when \(r^2-10r+12>0\) in the range \(r\ge6\), namely for integers \(r\ge9\). Moreover,
\[
\frac43-\frac{4r^2-11r+8}{(r+1)(3r-4)}
=\frac{29r-40}{3(r+1)(3r-4)}>0,
\]
whereas its consecutive difference is
\[
\frac{29r^2-51r+12}{(r+1)(r+2)(3r-4)(3r-1)}>0\qquad(r\ge2).
\]
Together with the increasing singleton branch, this proves strict monotonicity of the sharp constants and the unattained limit \(4/3\).

## Verification

The standalone standard-library program `verify_biclique.py` independently enumerates *all* metric balls for representative cuts on \(K_{r,r}\) with \(2\le r\le8\), and checks the four-orbit formulas against direct averaging with exact rational arithmetic. It separately checks every pair of cut occupancies for \(2\le r\le45\) against the theorem and substitutes rational integers in both polynomial comparison certificates. Its recorded run passed 280 exact direct-ball comparisons, 33,418 cut-count comparisons, and 11,480 certificate substitutions. These finite checks corroborate but do not replace the all-order algebraic proof above. Examples: \(\mathcal C_5^{\mathrm{cut}}=5/6\), \(\mathcal C_6^{\mathrm{cut}}=43/49\), \(\mathcal C_8^{\mathrm{cut}}=44/45\), and \(\mathcal C_9^{\mathrm{cut}}=233/230\).

## Relationship to prior work

The continuous interval theorem of Aldaz and Pérez Lázaro and the one-dimensional discrete theorem of Bober, Carneiro, Hughes, and Pierce give sharp uncentered variation contraction on an interval or \(\mathbb Z\), respectively. Their graph/domain hypotheses do not cover regular balanced bicliques. Soria and Tradacete investigate finite graph **centered** maximal \(\ell^p\) bounds; González-Riquelme and Madrid, and later González-Riquelme, Kovač and Madrid, study **centered** graph-ball variation estimates. They do not state the present uncentered balanced-biclique indicator classification in the inspected materials. Earlier unpublished or unindexed equivalents remain possible. The unrestricted real-input BV norm on \(K_{r,r}\) is not settled here.

## Limitations

The cut supremum is not the full operator variation norm over all real-valued graph signals. The theorem covers only unweighted **balanced** complete bipartite graphs, counting averages, graph metric balls, and first-order edge total variation. It does not claim the same constants for unbalanced bipartite graphs, vertex weights, other averaging families, higher variation exponents, or arbitrary non-indicator inputs. No independent review or external certification has been performed.

## References

1. J. M. Aldaz and J. Pérez Lázaro, *Functions of bounded variation, the derivative of the one dimensional maximal function, and applications to inequalities*, arXiv:math/0601044 (first posted January 3, 2006), Theorem 2.5.
2. J. Bober, E. Carneiro, K. Hughes, and L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030 (first posted May 17, 2010), Theorem 1.
3. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204 (first posted October 22, 2014).
4. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (first posted May 6, 2020).
5. C. González-Riquelme, V. Kovač, and J. Madrid, *Sharp variational inequalities for the Hardy–Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462 (first posted March 12, 2026).
6. F. Liu and Q. Xue, *On the variation of the Hardy–Littlewood maximal functions on finite graphs*, Collectanea Mathematica 72 (2021), 333–349, DOI:10.1007/s13348-020-00290-6 (full text not inspected).
