# Sharp weighted variation of the centered maximal operator on a three-vertex path

## Finding

On the three-vertex path \(a-c-b\), put strictly positive vertex masses \(u,h,v\) at \(a,c,b\). For the centered Hardy–Littlewood maximal operator \(M\) formed from mass-weighted averages over graph-metric balls and the **unweighted edge total variation**
\[\operatorname{Var}(f)=|f(a)-f(c)|+|f(b)-f(c)|,\]
the best constant over all real vertex data is
\[\boxed{C(h,u,v)=\max\left\{1-\frac{L}{h+U+L},\ \frac{U(h+2L)}{(h+2U)(h+L)}\right\}},\]
where \(U=\max\{u,v\}\), \(L=\min\{u,v\}\). The constant is attained by explicitly described nonnegative inputs.

For fixed \(U,L>0\), these two branches cross once at the unique positive zero of
\[h^3+(2U+L)h^2+U^2h-2UL^2=0.\]
The crossing is the unique optimal choice of center mass when leaf masses are fixed. If \(u=v=w\), the optimal mass ratio is \(h/w=(\sqrt5-1)/2\) and the optimally balanced norm is \((\sqrt5-1)/2\). The counting-measure case \(h=u=v\) gives the known value \(2/3\).

## Assumptions and scope

All three vertex masses are finite and strictly positive. Graph balls include the center vertex and use radii \(0,1,2\). For a nonempty vertex set \(E\), its average is \(\sum_{z\in E}\mu(z)|f(z)|/\sum_{z\in E}\mu(z)\). At a vertex \(z\), \(Mf(z)\) is the largest average of a centered metric ball. No mass weights are inserted into the two edge differences of \(\operatorname{Var}\). Constant inputs have zero variation and are excluded from the quotient defining the optimal constant.

## Proof

**Reduction and exact kernel.** Since \(M f=M|f|\) and \(\operatorname{Var}|f|\le\operatorname{Var}f\), nonnegative data suffice. All such data can be translated by a common real constant while remaining nonnegative; the output translates by the same constant, leaving variation unchanged. More generally every signed pair \(x=f(a)-f(c)\), \(y=f(b)-f(c)\) is realizable by first adding a sufficiently large common baseline. Thus take center coordinate zero when calculating differences. Set
\[W=h+u+v,\quad \alpha=\frac{u}{h+u},\quad \beta=\frac{v}{h+v},\quad H=\frac{ux+vy}{W}.\]
The maximal-function values, measured relative to the baseline, are
\[M_c=\max(0,H),\quad M_a=\max(x,\alpha x,H),\quad M_b=\max(y,\beta y,H).\]
Consequently the gain quotient for \((x,y)\ne(0,0)\) is \((|M_a-M_c|+|M_b-M_c|)/(|x|+|y|)\). It is enough to maximize on the diamond \(|x|+|y|=1\).

**Nonnegative and opposite-sign quadrants.** If \(x,y\ge0\), then \(M_c=H\), \(M_a=\max(x,H)\), \(M_b=\max(y,H)\), and the output variation equals \((x-H)_++(y-H)_+\). This is a convex function of \((x,y)\), so its maximum on \(x+y=1\) is at an endpoint, of values \(1-u/W\) and \(1-v/W\). If \(x\ge0\) and \(y=-t\le0\), the output variation equals \(x-H\) when \(H\ge0\), and equals \(x+|H|\) when \(H<0\): in the latter case, \(|H|<\beta t\), so the negative leaf's maximal output is \(H\). Both formulas simplify to \((1-u/W)x+(v/W)t\), bounded by \(1-u/W\), because \(v/W<1-u/W\). The symmetric opposite-sign quadrant is bounded by \(1-v/W\). This yields \(C_+=1-L/W\), attained by the unit positive spike at a leaf with mass \(L\).

**Negative quadrant.** Write \(x=-s\), \(y=-t\), with \(s,t\ge0\) and \(s+t=1\). Then \(M_c=0\) and the output variation is
\[F(s,t)=\min\left\{\alpha s,\frac{us+vt}{W}\right\}+\min\left\{\beta t,\frac{us+vt}{W}\right\}.\]
Its only interior branch switches occur at \(s=\beta/(1+\beta)\) and \(s=1/(1+\alpha)\), in that order because \(\alpha\beta<1\). Between these points \(F=\alpha s+\beta t\); on the two outside intervals the remaining active expressions are linear. Therefore the maximum is attained among \(s=0,1\) and the two switches. Its four candidate values are \(v/W\), \(u/W\), \(\beta(1+\alpha)/(1+\beta)\), and \(\alpha(1+\beta)/(1+\alpha)\). The first two are no larger than \(C_+\). If \(u\ge v\), then \(\alpha\ge\beta\), and
\[\frac{\alpha(1+\beta)}{1+\alpha}-\frac{\beta(1+\alpha)}{1+\beta}=\frac{(\alpha-\beta)(1-\alpha\beta)}{(1+\alpha)(1+\beta)}\ge0.\]
Thus the remaining sharp candidate is
\[C_-=\frac{\alpha(1+\beta)}{1+\alpha}=\frac{U(h+2L)}{(h+2U)(h+L)}.\]
When \(u=U\), choose \(x=-(h+U)/(h+2U)\), \(y=-U/(h+2U)\); with a sufficiently large common baseline the resulting nonnegative data attain \(C_-\). Exchange leaves when \(v=U\). Taking the maximum with \(C_+\) proves the claimed norm.

**Unique mass transition.** The branch \(C_+=1-L/(h+U+L)\) increases strictly in \(h\). Since \(\alpha,\beta\) decrease strictly in \(h\), and \(\alpha(1+\beta)/(1+\alpha)\) increases strictly in each of \(\alpha,\beta\), the branch \(C_-\) decreases strictly in \(h\). As \(h\downarrow0\), the two branches tend respectively to \(U/(U+L)<1\) and \(1\); as \(h\to\infty\), they tend respectively to \(1\) and \(0\). Hence exactly one crossing exists and minimizes their maximum. Algebraically the branch difference has the same sign as
\[h^3+(2U+L)h^2+U^2h-2UL^2\]
because its denominator \((h+2U)(h+L)(h+U+L)\) is positive. For \(U=L=w\), the crossing polynomial factors as \((h+2w)(h^2+hw-w^2)\), giving the stated golden-ratio value.

## Verification

The attached standalone `verify.py` rederives every candidate breakpoint from the six linear switching relations and checks the best exact-rational value against the displayed formula for \(216\) positive mass triples (six distinct rational masses per coordinate), without numerical tolerances. It also checks direct extremizers and positive/negative branch comparisons. This finite computation supports but does not replace the symbolic proof above. Execute with `python3 verify.py` (standard library only).

## Relationship to prior work

Soria and Tradacete (2014) define the graph centered maximal operator with counting measure and study sharp \(\ell^p\) bounds, rather than weighted-vertex total variation. González-Riquelme and Madrid (2020) study sharp graph \(p\)-variation using counting-measure averages; their \(p=1\) star theorem contains the equal-mass three-vertex value \(2/3\). The present result instead permits all strictly positive vertex averaging masses and optimizes over the center mass. The new mass-dependent negative-input branch and sharp phase transition are not consequences of the unweighted scalar constant alone.

## Limitations

This is the three-vertex **centered** maximal operator, with unweighted edge variation. The result does not assert weighted edge variation bounds, larger stars, non-atomic graphs, uncentered maximal operators, or general \(p\)-variation constants. No exhaustive survey of historical weighted-maximal-operator literature is claimed, and any equivalent earlier treatment would affect publication priority.

## References

1. J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, first public arXiv version 22 October 2014, arXiv:1410.6204, https://arxiv.org/abs/1410.6204 .
2. C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs*, first public arXiv version 6 May 2020, arXiv:2005.03146, https://arxiv.org/html/2005.03146v3 .
