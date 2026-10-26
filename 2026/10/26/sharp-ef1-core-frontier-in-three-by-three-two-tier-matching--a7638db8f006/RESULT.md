# Sharp EF1–core frontier in three-by-three two-tier matching

## Finding

**Theorem.** Fix a real \(0<\delta\le1\). There are exactly three firms and exactly three indivisible workers. The values \(a_{ij}\) of worker \(j\) to firm \(i\) belong to \(\{\delta,1\}\), and every worker has maximum firm value one: \(\max_i a_{ij}=1\). All firm valuations are additive; matching is complete; firms may employ any number of workers; and payments are transferable, nonnegative and locally financed.

Let \(\alpha(X)\) be the maximal approximate-core factor supported by a matching \(X\), and let EF1 mean envy-freeness up to one worker on the firm side. The exact worst-instance value is

\[
H^{\mathrm{two\mbox{-}tier}}_{3,3}(\delta)
:=\inf_A\max_{X:\mathrm{EF1}}\alpha(X)
=\frac{1+2\delta}{3}.
\]

An explicit three-case construction uses only the maximum matching size \(\nu\) of the bipartite graph of valuation-one edges. It gives core factors \(1\) for \(\nu=3\), at least \((1+\delta)/2\) for \(\nu=2\), and \((1+2\delta)/3\) for \(\nu=1\). Thus it yields the exact restricted frontier even in the parameter range \(\delta>1/2\), where the motivating paper does not determine its unrestricted three-firm frontier.

## Assumptions and scope

Write \(F=W=\{1,2,3\}\). A matching \(X\) partitions workers among the firms, and \(B_i=\sum_{j\in X_i}a_{ij}\) is firm \(i\)'s production. It is EF1 when, for every ordered pair \(i,k\) with \(X_k\ne\varnothing\), there exists \(g\in X_k\) such that \(B_i\ge\sum_{j\in X_k\setminus\{g\}}a_{ij}\).

A locally financed outcome has wages \(y_j\ge0\), profits \(x_i\ge0\), and \(x_i+\sum_{j\in X_i}y_j=B_i\). For a nonempty coalition of firms \(I\) and any worker subset \(T\), its productive value is \(v(I,T)=\sum_{j\in T}\max_{i\in I}a_{ij}\). The outcome is in the \(\alpha\)-core when \(x(I)+y(T)\ge\alpha v(I,T)\) for all such coalitions. We take \(0\le\alpha\le1\). These are the definitions used in Qin (2026, §2), not claims of newly introduced terminology.

For a vector of *normalized* wages \(z\ge0\), set

\[
D_i(X,z)=\sum_{j\in X_i}z_j+\sum_{j=1}^{3}(a_{ij}-z_j)_+,
\quad (t)_+=\max\{t,0\}.
\]

If \(D_i(X,z)\le B_i/\alpha\) for all firms, set actual wages \(y_j=\alpha z_j\) and profits \(x_i=B_i-\sum_{j\in X_i}y_j\). The inequality makes profits nonnegative and gives \(x_i\ge\sum_j(\alpha a_{ij}-y_j)_+\). Partitioning each deviating worker subset by its best coalition firm proves every coalition inequality, hence \(\alpha\)-core support. We use this published financing criterion with explicit newly constructed wages.

## Proof

**Case 1: \(\nu=3\).** Assign each worker to a distinct firm along three disjoint valuation-one edges. Give every worker normalized wage \(z_j=1\). Each firm produces \(B_i=1\), has \(D_i=1\), and supports the exact core \(\alpha=1\). Since each firm gets one worker, EF1 is automatic.

**Case 2: \(\nu=2\).** Choose two disjoint valuation-one edges, assign those workers to their respective firms, and assign the remaining worker \(j_0\) to the remaining firm \(i_0\). The last edge must have valuation \(\delta\), for otherwise it would extend the matching of valuation-one edges to size three. All three firms have one worker, so EF1 holds. Use

\[
z_j=1\quad(j\ne j_0),\qquad z_{j_0}=\frac{2\delta}{1+\delta},\qquad \alpha=\frac{1+\delta}{2}.
\]

For the remaining firm, \(B_{i_0}=\delta\), the first two workers have values at most their unit normalized wages, and its own worker has value at most \(z_{j_0}\) because \(\delta\le z_{j_0}\). Thus \(D_{i_0}=z_{j_0}\), so \(D_{i_0}/B_{i_0}=2/(1+\delta)=1/\alpha\). Each of the other firms has production one, normalized wage one on its assigned worker, and at most one positive deviation term, namely \((1-z_{j_0})_+\). Hence \(D_i\le 2-z_{j_0}=2/(1+\delta)=B_i/\alpha\). This supports the stated core factor. Since \(0<\delta\le1\),

\[
\frac{1+\delta}{2}\ge\frac{1+2\delta}{3}.
\]

**Case 3: \(\nu=1\).** Each worker has a valuation-one edge. If two such edges had distinct firm endpoints, their worker endpoints could be chosen distinct unless all valuation-one edges met at one worker; the latter is impossible because each of the three worker columns has a valuation-one edge. Equivalently, a bipartite graph whose maximum matching has size one has all edges incident to a common vertex, and the column condition forces that vertex to be a firm. Therefore some firm values **every** worker at one, and the other two firms value every worker at \(\delta\). Assign exactly one worker per firm. Set

\[
z_j=\frac{3\delta}{1+2\delta}\ \text{ for all }j,\qquad
\alpha=\frac{1+2\delta}{3}.
\]

The common normalized wage \(z\) lies between \(\delta\) and one. The high-valuing firm has \(B=1\) and \(D=z+3(1-z)=3/(1+2\delta)\). Each low-valuing firm has \(B=\delta\) and \(D=z\), giving \(D/B=3/(1+2\delta)\) for all three firms. The financing inequalities therefore hold with equality at \(\alpha=(1+2\delta)/3\). The one-worker bundles are EF1.

**Sharpness.** Consider exactly this common-top-firm instance. Because \(\delta>0\), no EF1 matching can leave a firm empty: another firm would then receive at least two workers, and removing only one would leave positive value for the empty firm. Hence every EF1 matching has one worker per firm and produces welfare \(1+2\delta\). Unrestricted optimal welfare is three, achieved by assigning all workers to the high-valuing firm. For the grand coalition, local financing and the \(\alpha\)-core inequality give \(\operatorname{SW}(X)\ge\alpha\operatorname{OPT}\). Consequently \(\alpha\le(1+2\delta)/3\) for every EF1 matching on this instance. The constructed wages achieve this value, proving the exact minimax identity.

## Verification

The included `verify_three_by_three.py` uses only Python's standard library and exact rational arithmetic. It enumerates all \(343\) binary high-edge incidence matrices with a high edge in every worker column. Among them the sizes of the maximum high-edge matching have counts \(3,93,247\) for sizes one, two and three, respectively. At each of five rational quality levels \(\delta\in\{1/10,1/2,3/4,9/10,1\}\), it reconstructs the explicit assignment, normalized wages, scaled real wages and local profits; independently checks EF1; and checks the approximate-core inequality for every nonempty firm subset and every worker subset, exactly, without using an LP solver. All \(1715\) certificates passed. These finite checks are cross-checks, not a replacement for the preceding continuum proof.

Reproduce with `python3 verify_three_by_three.py`. Its success line begins `ALL EXACT CHECKS PASSED`.

## Relationship to prior work

Qin (2026) provides the general financing–stability identity, its coalition interpretation and the unrestricted three-firm EF1–core bounds. Theorem 9 of that work proves the unrestricted three-firm sharp frontier when \(\delta\le1/2\) and leaves a small gap when \(\delta>1/2\). Its Theorem 8 already supplies the common-top-firm worst-case construction and grand-coalition upper bound. Both are credited rather than claimed as new. The present contribution is the **matching-number classification and explicit all-quality-level lower certificates under simultaneous restrictions to three workers and two value levels**; these yield a complete restricted frontier without resolving the unrestricted gap. This restricted statement is not a logical consequence of the paper's lower bound for general matrices at \(\delta>1/2\): the bound there is strictly smaller than the value proved here.

Other two-sided many-to-one matching research (Igarashi et al., 2025) studies participant/team fairness and strategyproofness with different coalition and transfer assumptions; the accessible abstract does not establish this exact payment-supported stability frontier. This is a scope comparison, not a full-text exclusion claim.

## Limitations

The exact equality is proved only for **three workers, three firms, and globally common two-level positive valuations** with each worker's maximum one. It does not determine the analogous restricted frontier for four or more workers, matrices with intermediate values, zero-valued edges, firm capacity constraints, or the motivating paper's unrestricted \(H_3(\delta)\) when \(\delta>1/2\). The wage certificates are constructive, but no incentive-compatibility claim about choosing or reporting values is made. Literature comparison is necessarily nonexhaustive; an equivalent specialized theorem may exist elsewhere. Independent validation has not been performed.

## References

1. Genjie Qin, *Fairness–Stability Trade-offs in Many-to-One Matching*, arXiv:2608.17295 (first public 2026-08-18). https://arxiv.org/html/2608.17295. Relevant material: §§2–3, Theorems 8–9, Appendix A.
2. Ayumi Igarashi, Naoyuki Kamiyama, Yasushi Kawase, Warut Suksompong, Hanna Sumita and Yu Yokoi, *Two-Sided Fairness in Many-to-One Matching*, arXiv:2509.24111 (2025), https://arxiv.org/abs/2509.24111. Background on related fairness benchmarks, not a source for the theorem's financing statements.
