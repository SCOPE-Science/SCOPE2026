# Exact price-triangle phase diagram for minimax effective resistance on double stars

## Finding

Let \(D_{p,q}\) be the double-star tree with two adjacent hubs, \(p\ge2\) leaves at the left hub and \(q\ge2\) leaves at the right hub. Independently choose a nonnegative conductance on every edge. A left spoke has positive unit-conductance price \(a\), a right spoke price \(b\), and the bridge price \(c\). The available budget is \(B>0\). The objective is the resistance diameter: the maximum effective resistance over all unordered pairs of distinct vertices, with disconnected pairs assigned infinite resistance.

Write
\[
 A=pa,\quad D=qb,\quad C=c,\qquad
 U=\sqrt A,\quad V=\sqrt D,\quad W=\sqrt C.
\]
Define a positive triple \((x,y,z)\) and a scalar \(F\) as follows.

* If \(U>V+W\), let
\[
 (x,y,z)=\left(\frac12,\frac{V}{2(V+W)},\frac{W}{2(V+W)}\right),
 \qquad F=2A+2(V+W)^2.
\]
* If \(V>U+W\), let
\[
 (x,y,z)=\left(\frac{U}{2(U+W)},\frac12,\frac{W}{2(U+W)}\right),
 \qquad F=2D+2(U+W)^2.
\]
* Otherwise, including either equality boundary, let
\[
 (x,y,z)=\frac{(U,V,W)}{U+V+W},
 \qquad F=(U+V+W)^2.
\]

**Theorem.** The unique global minimizer among *all independently adjustable edge conductances*, not merely among symmetric allocations, gives every left spoke conductance \(B/(Fx)\), every right spoke conductance \(B/(Fy)\), and the bridge conductance \(B/(Fz)\). All are strictly positive, and the exact minimum resistance diameter is
\[
 \boxed{\mathcal D_*=F/B.}
\]

The price-triangle condition \(\lvert\sqrt{pa}-\sqrt{qb}\rvert<\sqrt c\) is equivalent to the statement that **every diametral vertex pair uses the bridge**; in that regime the diametral pairs are exactly the \(pq\) pairs with one leaf in each star. When \(\sqrt{pa}\ge\sqrt{qb}+\sqrt c\), the left-side leaf pairs also attain the diameter; analogously \(\sqrt{qb}\ge\sqrt{pa}+\sqrt c\) adds the right-side leaf pairs. At the equality boundaries the indicated extra pairs tie, and there are no other diametral pairs.

For unit price on each edge, fix any \(q\ge2\) and let \(p\to\infty\). The ratio between the resistance diameter under equal conductances and the optimum tends to \(3/2\). Thus the support-class transition yields an asymptotic \(50\%\) improvement relative to equal conductances, measured as the ratio of the two objective values.

## Assumptions and scope

The graph is finite, undirected, connected before edge removal, and has exactly the \(p+q+1\) edges described. All prices and the total budget are strictly positive; \(p,q\) are integers at least two. The budget constrains the sum of price times conductance. A zero conductance disconnects this tree, giving infinite effective resistance between some vertex pairs; consequently every finite optimum has positive conductances. Electrical effective resistance uses the standard unit-current, weighted combinatorial-Laplacian normalization, so a tree's effective resistance is the sum of reciprocal conductances along the unique joining path. No stochastic commute-time normalization is asserted when total conductance is price-dependent.

The symmetry of prices within each spoke class does **not** constrain the admissible conductances: each edge is initially a separate optimization variable. The theorem gives the unique result after global optimization.

## Proof

**1. Resistance normalization and uniqueness without imposed symmetry.** For any positive conductance vector \(w\), let \(r_e=1/w_e\). On a tree,
\[
 \mathcal D(w)=\max_{u\ne v}\sum_{e\in P_{uv}}r_e.
\]
Consider the normalized convex set
\[
 \mathcal P=\left\{\rho_e>0:\ \sum_{e\in P_{uv}}\rho_e\le1
 \text{ for every distinct }u,v\right\},
\]
and the reciprocal-cost minimization
\[
 M=\min_{\rho\in\mathcal P}\sum_e\frac{c_e}{\rho_e},
\]
where \(c_e\) is \(a,b,\) or \(c\), as appropriate. The set is nonempty. Every coordinate of its closure lies in \([0,1]\), and the objective tends to infinity as any coordinate tends to zero. A minimizer therefore exists with all coordinates positive. Since each function \(c_e/\rho_e\) is strictly convex on the positive half-line, the minimizer is unique.

Let \(t=\mathcal D(w)\). The normalized vector \(\rho=r/t\) belongs to \(\mathcal P\) and obeys
\[
 \sum_e\frac{c_e}{\rho_e}=t\sum_ec_ew_e\le tB,
\]
so \(t\ge M/B\). Conversely, scaling the unique normalized minimizer to \(r_e=(M/B)\rho_e\) assigns conductance \(w_e=B/(M\rho_e)\), spends exactly \(B\), and achieves diameter \(M/B\): the normalized resistance diameter must equal one, since otherwise simultaneously increasing all \(\rho_e\) would strictly lower the objective while retaining feasibility. Thus the original optimum is exactly \(M/B\), and its conductances are unique.

Each permutation of the left leaves, and each permutation of the right leaves, preserves both the normalized constraints and the reciprocal-price objective. Uniqueness implies invariance under these permutations. Hence the unique normalized minimizer has common resistance \(x\) on left spokes, common resistance \(y\) on right spokes, and resistance \(z\) on the bridge. This proves symmetry as a conclusion, rather than assuming it.

**2. The three path families.** Because both leaf classes have at least two vertices, the longest resistance among paths is
\[
 \max\{2x,\ 2y,\ x+y+z\}.
\]
Every path between hubs or between a hub and a leaf is strictly shorter than one of these three families. Thus the normalized problem becomes
\[
 \min_{x,y,z>0}\left(\frac A x+\frac D y+\frac C z\right)
 \quad\text{subject to}\quad
 2x\le1,\ 2y\le1,\ x+y+z\le1.
\]
The final constraint is necessarily an equality at optimum: otherwise increasing \(z\) lowers \(C/z\) without violating any constraint. Substitute \(z=1-x-y\).

**3. Exact KKT classification.** Without the caps \(x,y\le1/2\), the sharp Cauchy--Schwarz inequality yields
\[
 \frac A x+\frac D y+\frac C z
 \ge (\sqrt A+\sqrt D+\sqrt C)^2
\]
for positive \(x+y+z=1\), with equality uniquely at \((x,y,z)=(U,V,W)/(U+V+W)\). This point respects both caps exactly when \(U\le V+W\) and \(V\le U+W\). It therefore gives the stated triangle regime, including its boundaries.

Suppose \(U>V+W\). The uncapped point violates \(x\le1/2\). On the face \(x=1/2\), the remaining positive coordinates must satisfy \(y+z=1/2\); Cauchy--Schwarz uniquely minimizes their cost at
\[
 y=\frac{V}{2(V+W)},\qquad z=\frac{W}{2(V+W)}.
\]
The derivative of the reduced cost \(A/x+D/y+C/(1-x-y)\) in the \(x\)-direction at this point is \(4[(V+W)^2-A]<0\); its \(y\)-derivative is zero, and \(y<1/2\). Hence its multiplier for the upper bound on \(x\) is positive, with all remaining KKT conditions satisfied. Convexity proves global optimality; strict convexity proves uniqueness. Its value is \(F=2A+2(V+W)^2\). The case \(V>U+W\) is symmetric. The two strict cap regimes cannot coexist because \(W>0\).

Finally the scaling result in step 1 gives exactly the conductances and optimum stated in the theorem. In the strict triangle regime \(2x,2y<1=x+y+z\), so only cross-leaf pairs attain the diameter. On or beyond a cap boundary, the corresponding within-class leaf paths have resistance \(2x=1\) or \(2y=1\) as well; all other pair types have strictly smaller resistance. This proves the complete diametral-pair classification.

**4. Asymptotic price of uniform allocation.** When all prices equal one and \(q\ge2\) is fixed, the aggregate prices are \(A=p\), \(D=q\), \(C=1\). For \(\sqrt p>\sqrt q+1\), the exact optimal value is \([2p+2(\sqrt q+1)^2]/B\). Equal conductances must each be \(B/(p+q+1)\), and their resistance diameter is \(3(p+q+1)/B\). Their ratio is
\[
 \frac{3(p+q+1)}{2p+2(\sqrt q+1)^2}\longrightarrow\frac32
 \quad (p\to\infty).
\]

## Verification

The accompanying standalone program `check.py` independently builds grounded weighted graph Laplacians, obtains all pairwise resistances by matrix inversion, and compares their maxima to the closed-form optimum. It also checks arbitrary nonsymmetric feasible allocations and solves the full-dimensional reciprocal-cost program numerically, without imposing spoke symmetry. Running it with Python 3, NumPy, and SciPy produced:

```text
Exact rational branch/boundary cases: 5
Independent grounded-Laplacian resistance comparisons: 225
Asymmetric feasible allocation inequalities: 14625
Independent full-dimensional numerical minimizations: 54
Regime sample counts: {'triangle': 80, 'left_cap': 76, 'right_cap': 69}
All implemented checks passed; infinite-domain proof is analytic.
```

These finite checks do not certify the infinite parameter domain; that claim is established by the strict-convexity, normalization and KKT proof above. The exact-rational checks cover representative branch and equality cases but do not exhaust all rational instances.

## Relationship to prior work

Ghosh, Boyd and Saberi (2006/2008) explicitly identify minimization of maximum pairwise effective resistance as a convex program admitting a semidefinite formulation. Their inspected treatment supplies the general problem and the tree resistance formula, but does not present this priced-double-star, sharp price-triangle classification. The claim here is **not** novelty of the general convex program, path-resistance identity, or Cauchy--Schwarz inequality; it is the explicit unique allocation and exact switch in which path families are worst.

Ellens and coauthors (2011) optimize the **sum** of effective resistances under topology and graph-diameter restrictions, not the resistance diameter under a reciprocal-conductance budget. The edge-reduction tree-diameter problem of Hambrusch and Lim (1998/1999) is a plausible older analogue; its available abstract describes costs of edge reductions, but its inaccessible full text could not be checked against the present reciprocal-conductance price model. A known heterogeneous-price star minimax result is not an implication for the present two-hub family: the bridge creates a third mutually competing path family. A separate earlier double-star spectral-gap problem concerns a different eigenvalue objective.

## Limitations

All spokes within the same hub must have the same **unit price**, although their conductances are independently optimized. The statement does not claim arbitrary leaf-by-leaf heterogeneous prices, graphs with additional cycles, zero or negative prices, or a bound on electrical commute times when the sum of conductances changes. The independence of the result from a specialized historical treatment is not established; particularly, the full Hambrusch--Lim paper remains an uninspected plausible source. No independent mathematical audit or external certification has been performed.

## References

1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, Proceedings of the 17th International Symposium on Mathematical Theory of Networks and Systems, Kyoto, July 24--28, 2006; conference version: https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf. Expanded journal version: *SIAM Review* 50(1), 37--66 (2008), DOI:10.1137/050645452, https://web.stanford.edu/~boyd/papers/pdf/eff_res.pdf.
2. W. Ellens, F. M. Spieksma, P. Van Mieghem, A. Jamakovic, R. E. Kooij, *Effective graph resistance*, *Linear Algebra and its Applications* 435 (2011), 2491--2506, DOI:10.1016/j.laa.2011.02.024, https://www.nas.ewi.tudelft.nl/people/Piet/papers/LAA_2011_EffectiveResistance.pdf.
3. S. E. Hambrusch and H.-S. Lim, *Minimizing the Diameter in Tree Networks Under Edge Reductions*, Purdue technical report 98-022 (1998), *Parallel Processing Letters* 9(3), 361--371 (1999), DOI:10.1142/S0129626499000335. Full-text comparison not completed.
