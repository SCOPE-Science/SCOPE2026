# An exact dominant-price threshold for resistance-diameter design on stars

## Finding

Consider a weighted star with \(m\geq2\) leaves. All individual edge conductances are decision variables, with positive unit prices \(c_1,\ldots,c_m\) and a fixed budget \(B>0\). Let \(C=\sum_i c_i\), \(a=\max_i c_i\), and \(R=C-a>0\). The objective is the resistance diameter, the maximum effective resistance between any two distinct vertices. Its **global minimum and unique optimizer** are

\[
\Delta_*=
\begin{cases}
2C/B,&a\le R,\\
(\sqrt a+\sqrt R)^2/B,&a>R.
\end{cases}
\]

When \(a\le R\), every conductance is \(w_i=B/C\), regardless of heterogeneity among the prices. When \(a>R\), there is a unique most expensive edge \(j\). With \(s=\sqrt a\) and \(t=\sqrt R\), its conductance is \(w_j=B/[s(s+t)]\), and every other edge has conductance \(w_i=B/[t(s+t)]\). The formulas coincide on the boundary \(a=R\).

The optimal diameter improves upon the equal-conductance diameter by a factor strictly between \(1\) and \(2\) in the dominant-price regime, and this factor tends to \(2\) as \(a/R\to\infty\). Thus the design changes sharply from entirely equal weights to a single distinct expensive edge exactly when one edge's unit price exceeds the sum of all others.

## Assumptions and scope

The graph is the finite star \(K_{1,m}\), with one hub and \(m\ge2\) labeled leaves. Conductances \(w_i>0\) are assigned independently to the edges from the hub to leaf \(i\). Prices \(c_i>0\) are fixed; \(\sum_i c_iw_i\le B\), where \(B>0\). The effective resistance \(\mathcal R(u,v)\) is the voltage difference for a unit current between \(u\) and \(v\) in the corresponding electrical network. Define \(\Delta(w)=\max_{u\ne v}\mathcal R(u,v)\). If any conductance vanishes, the disconnected graph is assigned infinite resistance diameter. An optimum spends the entire budget, since increasing all conductances strictly reduces all finite effective resistances.

On a tree, resistances add along the unique path. Consequently the leaf-to-hub resistances are \(1/w_i\), while the leaf-to-leaf resistances are \(1/w_i+1/w_j\). As \(m\ge2\), the maximum is always attained on a leaf pair, and

\[
\Delta(w)=\max_{1\le i<j\le m}\left(\frac1{w_i}+\frac1{w_j}\right).
\]

## Proof

**Reduction to a normalized convex allocation.** Let \(T=\Delta(w)>0\) and set \(x_i=1/(Tw_i)>0\). For every pair of distinct indices, \(x_i+x_j\le1\). Budget expenditure obeys

\[
\sum_i c_iw_i=\frac1T\sum_i\frac{c_i}{x_i}.
\]

We therefore first minimize \(F(x)=\sum_i c_i/x_i\) over the domain \(x_i>0\) subject to \(x_i+x_j\le1\) for all \(i\ne j\). Denote the minimum by \(F_*\). The budget inequality yields \(BT\ge F(x)\ge F_*\), so \(T\ge F_*/B\). Conversely, a minimizer \(x\) can be converted into conductances \(w_i=B/(F_*x_i)\), provided its largest pair sum is \(1\), giving equality. We now find the complete minimizer set and prove that property.

**Case I: no normalized resistance exceeds one half.** If \(x_i\le1/2\) for every \(i\), then \(F(x)\ge2C\), and equality is possible only when every \(x_i=1/2\). This all-half vector is feasible and has maximum pair sum \(1\).

**Case II: one normalized resistance exceeds one half.** At most one coordinate can exceed \(1/2\) because every pair sums to at most \(1\). If \(x_j=u>1/2\), every other coordinate satisfies \(x_i\le1-u<1/2\). Because \(c_i/x_i\) is strictly decreasing in \(x_i>0\), any minimizer with this \(u\) must set each other \(x_i=1-u\). Its cost is therefore bounded by

\[
F(x)\ge f_j(u)=\frac{c_j}{u}+\frac{C-c_j}{1-u},\qquad \frac12<u<1,
\]

with equality only at these common remaining coordinates. The strictly convex function \(f_j\) has an unconstrained minimum at

\[
u_j=\frac{\sqrt{c_j}}{\sqrt{c_j}+\sqrt{C-c_j}}.
\]

This point lies above \(1/2\) exactly when \(c_j>C-c_j\). If \(c_j\le C-c_j\), then \(f_j(u)>f_j(1/2)=2C\) for every \(u>1/2\). Otherwise the unique minimizer is \(u_j\), and

\[
f_j(u_j)=\bigl(\sqrt{c_j}+\sqrt{C-c_j}\bigr)^2<2C.
\]

At most one index can satisfy \(c_j>C/2\), because all prices are strictly positive. Thus, if \(a\le R\), the unique minimizer of \(F\) is the all-half vector with \(F_*=2C\); if \(a>R\), it is the unique vector \(x_j=s/(s+t)\), \(x_i=t/(s+t)\) for every \(i\ne j\), and \(F_*=(s+t)^2\). In both cases the largest pair sum equals \(1\), proving that the preceding lower bound on the original resistance diameter is attained. The correspondence \(w_i=B/(F_*x_i)\) gives precisely the conductance formulas in the finding and also proves their uniqueness among *all* independently chosen edge weights.

**Sharp improvement factor.** The equal-conductance allocation has diameter \(2C/B\). For \(a>R\), its ratio to the optimum is

\[
\frac{2(a+R)}{(\sqrt a+\sqrt R)^2}
=\frac{2}{1+2\sqrt{aR}/(a+R)}.
\]

It is strictly greater than \(1\) and less than \(2\), and tends to \(2\) as \(a/R\to\infty\). The ratio is exactly \(1\) at the threshold. This completes the classification, including all boundary cases.

## Verification

`verify.py` reconstructs the formula on 54 independently selected positive-price instances with two through seven leaves, checks 8,100 seeded arbitrary feasible allocations, and compares with 54 independent constrained numerical convex optimizations in the normalized resistance variables. It also checks 21 leaf-pair effective resistances by exact reduced-Laplacian inversion on four rational-weight star networks, plus the sharp nearly-two-fold ratio. Run `python verify.py` with Python 3 and installed SciPy, NumPy, and SymPy. A deterministic expected result is in `verification_output.json`.

These tests do not establish the theorem for arbitrarily many leaves or all real prices; the proof above does that. Floating-point checks do not constitute exact global certificates for the optimization problem. The exact matrix checks validate the electrical normalization on selected examples.

## Relationship to prior work

Ghosh, Boyd, and Saberi (2006; revised journal version 2008) establish convex conductance optimization for total effective resistance, including a general tree formula. They also identify minimizing *maximum* pairwise effective resistance as another convex problem admitting an SDP formulation, but do not solve the heterogeneously priced star's resistance-diameter allocation in either inspected version. Their star example is the **total-resistance** problem with equal unit prices; it is not the price-dependent minimax theorem stated here. The previously known tree path-resistance formula is used as a premise and is not claimed as new. General convexity and SDP solvability are also already known. For contrast, minimizing *total* pairwise effective resistance on the same star with the same heterogeneous prices yields conductances proportional to \(1/\sqrt{c_i}\), specifically \(w_i=B/[\sqrt{c_i}\sum_k\sqrt{c_k}]\); this follows from the published tree-total-resistance identity and Cauchy–Schwarz, and is not claimed as new. The minimax theorem instead prescribes **equal conductances across all edges** throughout the large price-nondominance regime, despite unequal prices. The contribution is the full exact, unique, price-dependent maximum-resistance optimizer, its dominant-price transition, and its sharp worst-case performance separation from equal weighting.

## Limitations

The result assumes a fixed star topology with at least two leaves, strictly positive linear prices, independent conductance choices, and a total cost constraint. It does not classify general trees, cyclic networks, nonlinear cost models, or different objectives such as total/average effective resistance or algebraic connectivity. Prior literature may contain equivalent formulas in less directly indexed network-design or minimax-resource-allocation work; the surveyed sources and database searches do not prove absolute novelty. The scientific assessment has not undergone independent audit.

## References

1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems (Kyoto, July 24–28, 2006), pp. 1185–1196, https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf. Section on extensions (p. 1195) identifies the maximum-resistance SDP.
2. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1), 37–66 (2008), https://doi.org/10.1137/050645452. A lawful full-text copy is at https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf; see the tree/star examples and the extensions section.
