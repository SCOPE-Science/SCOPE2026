# Sharp worst-pair resistance design for complete graphs with priced matching links

## Finding

For every integer \(m\ge2\), let \(M\) be a fixed perfect matching of the complete graph \(K_{2m}\). Each edge in \(M\) has per-unit conductance price \(P>0\); each other edge has price \(Q>0\). Fix a total budget \(B>0\). Independently assign nonnegative conductances to all edges, require the resulting positive-conductance network to be connected, and minimize its **resistance diameter**
\[
\mathcal D=\max_{u\ne v}(e_u-e_v)^\mathsf{T}L^\dagger(e_u-e_v),
\]
where \(L\) is the weighted graph Laplacian.

Put \(r=P/Q\) and \(r_-=2(m-1)/(2m-1)\). A globally optimal allocation always exists in which all matching edges have common conductance \(x_*\), all other edges have common conductance \(y_*>0\), and \(t_*=x_*/y_*\) is
\[
t_*=\begin{cases}
\sqrt{m(m-1)(2/r-1)}-(m-1),&0<r<r_-,\\
1,&r_-\le r<2,\\
0,&r>2.
\end{cases}
\]
At \(r=2\), every \(t\in[0,1]\) gives a globally optimal orbit-constant allocation. In every case the weights are recovered exactly by
\[
y_*=\frac{B}{m(Pt_*+2(m-1)Q)},\qquad x_*=t_*y_*.
\]
The global optimal resistance diameter is
\[
\boxed{\mathcal D_*=
\begin{cases}
\dfrac{\bigl(\sqrt{mP}+\sqrt{(m-1)(2Q-P)}\bigr)^2}{2B},&0<P/Q<r_-,\\[6pt]
\dfrac{P+2(m-1)Q}{B},&r_-\le P/Q\le2,\\[6pt]
\dfrac{2mQ}{B},&P/Q\ge2.
\end{cases}}
\]
The formulas agree at both boundaries. **Every unrestricted global optimizer removes all matching edges if \(P>2Q\); no unrestricted global optimizer removes them all if \(P<2Q\).** At equality \(P=2Q\), both zero-matching and positive-matching optimal allocations exist. Uniqueness of unrestricted optimizers is not asserted.

In particular, throughout the nontrivial price interval \(r_-\le P/Q<2\), an optimal network uses **exactly equal conductances on every edge**, despite the unequal prices. The upper support threshold \(P/Q=2\) is independent of graph size, whereas \(r_-=1-1/(2m-1)\). For fixed real \(\delta\), in the lower critical price window \(P/Q=1+\delta/m\), the canonical orbit-constant optimum satisfies
\[
\lim_{m\to\infty}t_*=\max\{1,\tfrac12-\delta\}.
\]

## Assumptions and scope

The graph is exactly a complete graph on an even number of vertices with a *fixed* perfect matching distinguished only by price. Prices are positive and constant within the two edge classes. Conductances are independent, real, and nonnegative, and the full budget is available. Connectivity is required so that all effective resistances are finite. Every statement concerns the worst resistance between **all** unordered vertex pairs, not the sum or average of those resistances, shortest-path distance, maximum commute time under variable stationary normalization, or a fixed-topology sparsification cardinality constraint. The result allows individual asymmetry and does not initially restrict the optimizer to edge-orbit weights.

## Proof

**Convex unrestricted reduction.** Let \(R_{uv}(w)\) be the effective resistance for a feasible conductance vector \(w\). With \(J=\mathbf1\mathbf1^\mathsf T/(2m)\), its connected-network representation is
\[
R_{uv}(w)=(e_u-e_v)^\mathsf T(L(w)+J)^{-1}(e_u-e_v).
\]
The inverse quadratic form is convex on positive-definite matrices; because \(L(w)+J\) is affine in \(w\), each \(R_{uv}\) is convex. Their maximum \(\mathcal D(w)\) is convex. It is invariant under any permutation of the \(m\) pairs and independent swaps within the pairs. This price-preserving automorphism group is transitive on the \(m\) matching edges and on the \(2m(m-1)\) other edges. Averaging any feasible \(w\) over the group cannot increase \(\mathcal D\), preserves its budget and connectivity, and produces two orbit weights \(x,y\). A finite optimal value is attained (the objective diverges on disconnection); any optimizer spends the whole budget because scaling all weights up decreases all resistances. As \(m\ge2\), the graph supported only on the matching is disconnected, so \(y>0\). Thus a global optimum is achieved by the two-orbit problem, not merely approximated by it.

**Exact electrical spectrum.** Write \(N=2m\) and \(A=N-2\). The weighted Laplacian of an orbit-constant allocation is
\[
L=yL(K_N)+(x-y)L(M).
\]
On vectors antisymmetric within each pair (dimension \(m\)), its eigenvalue is \(\lambda_a=2x+A y\). On vectors constant within each pair and of total sum zero (dimension \(m-1\)), it is \(\lambda_b=Ny\); constants form the nullspace. A matched vertex difference has squared norm two in the first eigenspace, hence
\[
R_{\rm match}=\frac{2}{\lambda_a}.
\]
A nonmatched vertex difference projects with squared norm one onto *each* nonzero eigenspace, hence
\[
R_{\rm other}=\frac1{\lambda_a}+\frac1{\lambda_b}.
\]
No other resistance types exist. The larger resistance is \(R_{\rm match}\) for \(0\le x/y\le1\), and \(R_{\rm other}\) for \(x/y\ge1\).

**One-variable optimization including boundaries.** Let \(t=x/y\ge0\). There are \(m\) matching edges and \(mA\) other edges; full expenditure yields
\[
y=\frac{B}{m(Pt+AQ)}.
\]
For \(0\le t\le1\), the worst resistance and its derivative are
\[
F_1(t)=\frac{2m(Pt+AQ)}{B(2t+A)},\qquad
F_1'(t)=\frac{2mA(P-2Q)}{B(2t+A)^2}.
\]
For \(t\ge1\), they are
\[
F_2(t)=\frac{m(Pt+AQ)}B\left(\frac1{2t+A}+\frac1N\right),\qquad
F_2'(t)=\frac mB\left[\frac{A(P-2Q)}{(2t+A)^2}+\frac PN\right].
\]
The functions agree at \(t=1\). If \(P<2Q\), \(F_1\) decreases, and \(F_2'\) increases strictly with \(t\). The sign of \(F_2'(1)\) is that of \((A+N)P-2AQ\), so its sign changes at \(P/Q=r_-=2A/(A+N)\). If \(P/Q<r_-\), \(F_2'\) has a unique zero at
\[
2t+A=\sqrt{AN(2Q/P-1)},
\]
which lies strictly above \(t=1\). Otherwise, for \(r_-\le P/Q<2\), the minimum occurs at \(t=1\). At \(P=2Q\), \(F_1\) is constant on \([0,1]\) while \(F_2\) increases beyond one. If \(P>2Q\), \(F_1\) and \(F_2\) are both strictly increasing on their respective intervals, so \(t=0\) uniquely minimizes the orbit-constant objective. Substituting the minimizing weights into \(F_1,F_2\) gives the three asserted closed formulas. The positive-edge graph at \(t=0\) is \(K_{2m}\) minus a perfect matching, which is connected for \(m\ge2\).

**Unrestricted support consequences.** If \(P>2Q\) and an unrestricted optimum had a positive matching conductance, its automorphism average would have \(x>0\) and attain the same optimal value, contradicting the unique orbit-constant minimizer \(x=0\). If \(P<2Q\), an unrestricted optimum with all matching conductances zero would average to an orbit-constant optimum with \(x=0\), contradicting the unique orbit-constant minimizer \(t\ge1\). At \(P=2Q\), the already proved continuum supplies examples both with and without matching conductance.

**Lower-price asymptotics.** Since \(r_-=1-1/(2m-1)\), when \(r=1+\delta/m\) and \(\delta<-1/2\), eventually \(r<r_-\), and
\[
\sqrt{m(m-1)(2/r-1)}-(m-1)=\tfrac12-\delta+O(m^{-1}).
\]
For \(\delta>-1/2\), eventually \(r\ge r_-\) and \(t_*=1\); at the boundary \(\delta=-1/2\) the same limit holds. This proves the claimed critical-window limit.

## Verification

Run `python verify.py` after installing dependencies in `REQUIREMENTS.txt`. The script tests exact rational full-matrix effective resistance identities for sizes \(m=2,\ldots,6\), symbolic derivative and threshold identities, numerical minimization of the one-variable expression over many costs, independent feasible full-matrix samples, both phase boundaries, and the critical-window limit. Its result is `PASS 2497 exact algebraic / numerical assertions` in the reviewed environment. Finite checks corroborate, but do not replace, the preceding general proof.

## Relationship to prior work

Ghosh, Boyd and Saberi (MTNS 2006, and an expanded SIAM Review article, 2008) establish the convex effective-resistance design framework and explicitly formulate minimizing the **maximum** pair resistance as a general convex semidefinite-programming problem. Their stated graph-specific analytical solutions concern other structures; the full-text sections inspected did not supply this two-price perfect-matching classification. The cocktail-party graph is the graph \(K_{2m}\setminus M\), and its combinatorial structure and geodesic betweenness are already established in the graph literature; these are not asserted as new.

The mean-resistance allocation for a complete graph with *one* distinguished edge and the mean-resistance/spanning-tree allocations for a **bipartite** complete graph with a priced perfect matching are different optimization statements and do not imply the resistance-diameter thresholds here. The new result concerns the price-insensitive worst-case plateau and the dimension-independent deletion threshold, not the general convexity theorem or the cocktail-party graph definition.

## Limitations

The claim establishes the optimal value and existence of orbit-constant global optimizers and the stated universal support conclusions. It does not classify every unrestricted optimizer or prove unrestricted uniqueness. The critical-window statement is a limit as the integer \(m\) tends to infinity, not a finite-size equality. The prices are constant within two classes and the budget has no per-edge caps or fixed installation charges. Priority is assessed against the specified inspected literature and searchable records; unknown specialized coverage remains possible. No independent external mathematical audit has been performed.

## References

1. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006, Kyoto, proceedings paper TuP12.2 (Tuesday, 25 July 2006), https://stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf ; especially §§II, IV, V and VII.
2. A. Ghosh, S. Boyd and A. Saberi, *Minimizing Effective Resistance of a Graph*, SIAM Review 50(1) (2008), 37–66, https://doi.org/10.1137/050645452 ; author-hosted full text https://stanford.edu/~boyd/papers/pdf/eff_res.pdf, especially §§2, 5 and 8.
3. S. K. Raghavan Unnithan, B. Kannan and M. Jathavedan, *Betweenness Centrality in Some Classes of Graphs*, International Journal of Combinatorics (2014), article 241723, https://doi.org/10.1155/2014/241723 ; §3.4 defines and studies cocktail-party graphs under a different invariant.
