# Convex-order inflation and a sharp branching index for final-size risk in tree SIR epidemics

## Finding

**Theorem.** Fix a finite rooted tree \(G=(V,E)\) with \(n\ge3\) vertices and root \(r\), and a common mean per-neighbor transmissibility \(q\in(0,1)\). Consider the individual-period susceptible–infectious–removed (SIR) model defined below, with an independent transmissibility \(P_v\) for each vertex and the same law at all vertices. Let \(Z_P\) be its final number infected, including the root; let \(Z_q\) be the corresponding constant-transmissibility model. Then:

1. If \(P^{(1)}\) and \(P^{(0)}\) have mean \(q\) and \(P^{(1)}\) is larger in convex order than \(P^{(0)}\), then \(Z_{P^{(1)}}\) is larger in convex order than \(Z_{P^{(0)}}\). In particular \(Z_P\) is larger in convex order than \(Z_q\). That is, for every convex real function \(\varphi\) on \(\{1,\ldots,n\}\),
   \[\mathbb E\varphi(Z_{P^{(1)}})\ge\mathbb E\varphi(Z_{P^{(0)}}).\]
2. The mean is independent of transmissibility variability:
   \[\mathbb E Z_P=\mathbb E Z_q=\sum_{v\in V}q^{d(v)},\]
   where \(d(v)\) is the distance from \(r\).
3. The *exact* variance excess is
   \[\operatorname{Var}(Z_P)-\operatorname{Var}(Z_q)=B_G(q)\operatorname{Var}(P),\]
   with the intrinsic rooted-tree branching index
   \[B_G(q)=2\!\sum_{\substack{\{u,v\}\subset V\\u,v\ \text{incomparable}}}q^{d(u)+d(v)-d(\operatorname{lca}(u,v))-2}.\]
   Here incomparable means neither vertex is an ancestor of the other, and \(\operatorname{lca}\) is the lowest common ancestor. The exponents are nonnegative integers.
4. The sharp topology and distribution bound is
   \[0\le \operatorname{Var}(Z_P)-\operatorname{Var}(Z_q)\le B_G(q)q(1-q)\le(n-1)(n-2)q(1-q).\]
   For \(0<q<1\), \(B_G(q)=0\) exactly for a rooted path with the root at an endpoint; \(B_G(q)=(n-1)(n-2)\) exactly for the star rooted at its center. The first variance inequality is strict for nonconstant \(P\) on every other rooted tree. The final bound is a **supremum** over finite infectious-period laws, approached as a positive period becomes arbitrarily long; it need not be attained by finite periods.

For example, on the four-vertex center-rooted star, let \(q=1/2\) and let each individual \(P\) be \(1/4\) or \(3/4\), equally likely. Both models have expected final size \(5/2\), but their variances are respectively \(3/4\) (constant transmissibility) and \(9/8\) (heterogeneous transmissibility), with exact excess \(3/8\).

## Assumptions and scope

The underlying graph is a finite **undirected tree**, the root \(r\) is the sole initial infected individual, other individuals are initially susceptible, and recovered individuals never become susceptible again. Each newly infected vertex \(v\) remains infectious for an independent duration \(T_v\ge0\), almost surely finite. While infectious, vertex \(v\) directs infectious contacts to each neighbor according to independent rate-\(\beta>0\) Poisson processes. Infectious periods are identically distributed independently of all contacts, and all contacts directed from a vertex are conditionally independent given its own duration. Define \(P_v=1-e^{-\beta T_v}\in[0,1)\). Thus, conditioned on \(P_v\), its transmissions to its as-yet-susceptible children are independent Bernoulli variables of success probability \(P_v\). The constant-\(q\) comparison uses deterministic duration \(-\log(1-q)/\beta\).

The convex-order comparison also holds with vertex-dependent independent transmissibility laws, when the distributions at each vertex are separately increased in convex order while preserving their respective means; the explicit index and universal extremizers are asserted in the identical-law case.

## Proof

**Directed-tree representation.** Orient every edge away from the unique root. No infection can reach a vertex from a descendant before the vertex is itself infected: on a tree with only the root infected initially, any infection of vertex \(v\ne r\) must travel along its unique ancestral path. For every directed parent-to-child edge introduce a potential successful-contact indicator. Conditional on the parent variable \(P_v=p\), its outgoing indicators are independent Bernoulli variables with parameter \(p\); indicators at different parents are independent. The infected set is precisely the root-reachable set in this random oriented tree. In particular the root-to-vertex path uses different parents, so its success probability is \(q^{d(v)}\). Summation proves the mean formula.

**Convex-order assertion.** Change the law of a single parent variable \(P_w\), conditioning on all other individual variables and all potential directed contacts other than the edges leaving \(w\). If \(w\) is not root-reachable without its outgoing edges, the total infected size does not depend on \(P_w\). Otherwise write the infected count as \(c+\sum_{j=1}^s A_jX_j\), where each \(A_j\ge0\) is the fixed root-reachable size of the descendant component beyond child \(j\), while conditioned on \(P_w=p\) the \(X_j\) are independent Bernoulli \(p\). For convex \(\varphi\), set \(f(p)=\mathbb E[\varphi(c+\sum_j A_jX_j)\mid P_w=p]\). Its second derivative is a sum over **ordered distinct** child pairs of expected mixed differences
\[\varphi(x+a+b)-\varphi(x+a)-\varphi(x+b)+\varphi(x),\]
with \(a,b\ge0\). Each is nonnegative by monotonicity of the forward increment of a convex function. Hence \(f\) is convex on \([0,1]\). Increasing \(P_w\) in convex order therefore cannot decrease the expectation of any convex \(\varphi(Z)\). Iterate over all vertices, using independence and the law of total expectation. The means remain fixed; this proves convex order. A constant variable \(q\) is minimal in convex order among variables with mean \(q\).

**Pairs and the variance.** Let \(I_u\) be the indicator that \(u\) is ever infected. For an ancestral pair \(u,v\), the joint infection probability depends only on the deeper endpoint's ancestral path and therefore is identical to the constant-\(q\) model. For an incomparable pair with lowest common ancestor \(w\), the union of both root paths contains two outgoing edges at \(w\) and one outgoing edge at each of its other source vertices. Therefore
\[\Pr(I_u=I_v=1)=q^{d(u)+d(v)-d(w)-2}\mathbb E[P^2].\]
Under constant transmissibility, the corresponding expression replaces \(\mathbb E[P^2]\) by \(q^2\). Individual indicator variances and ancestral-pair covariances cancel in the difference of \(\operatorname{Var}(\sum_vI_v)\), leaving exactly \(2\operatorname{Var}(P)\) times the stated sum.

**Sharpness.** Every exponent in \(B_G(q)\) is nonnegative. There are at most \(\binom{n-1}{2}\) unordered incomparable pairs because the root is ancestral to every vertex. Hence \(B_G(q)\le2\binom{n-1}{2}\). No incomparable pair exists precisely when all vertices are ordered by ancestry, that is, a rooted chain. A center-rooted star makes all non-root pairs incomparable and every exponent zero, attaining the upper bound. Conversely, equality forces all non-root pairs to be incomparable, hence every other vertex is a child of the root. Finally, \(\operatorname{Var}(P)\le q(1-q)\) because \(0\le P\le1\). For finite periods, choose \(P\in\{0,h\}\), with probabilities \(1-q/h\) and \(q/h\), where \(q<h<1\); then \(\operatorname{Var}(P)=q(h-q)\uparrow q(1-q)\) as \(h\uparrow1\). All corresponding periods \(-\log(1-P)/\beta\) are finite. These constructions prove the sharp supremum and the equality claims.

## Verification

The standalone `verify.py` uses only the Python standard library and exact rational arithmetic. Run `python verify.py` in the directory containing this report and the script. It enumerates all \(1,441\) labeled trees with \(2\le n\le6\) and root label zero (via Prüfer codes), computes the full final-size distribution by a recursive offspring polynomial, and checks exact expectations, variance differences, convex stop-loss inequalities, and branching bounds. It reports **15,684 exact-rational checks passed**. The four-vertex star values above are also checked. The script is a finite independent computation of examples, not an exhaustive or computer-assisted proof of the theorem for arbitrary \(n\); the preceding argument supplies the universal proof.

## Relationship to prior work

Hall and Siebert's rooted-tree epidemic formulation (first public arXiv version 2021-08-16) gives exact Markovian tree **node-state marginal trajectories**, not this finite-tree convex-order comparison of final size across independent infectious-period laws nor the explicit lowest-common-ancestor variance index [1]. Kenah and Robins established that variable infectious periods induce dependent outgoing contact indicators and defeat naive independent-bond outbreak distributions; their more general epidemic-percolation representation underlies the setup here, but does not state the convex-order domination or this exact rooted-tree variance law and extremal classification [2]. Wilkinson and Sharkey proved comparison principles for *probabilities infection reaches specified subsets* under infectious-period variability; such subset probabilities are not convex functions of total outbreak size and their direction does not by itself imply the present convex order [3]. Ramírez-Ramírez and coauthors treated final-size variance in random-network outbreak approximations, including common individual infectious periods, rather than the exact formula for each finite rooted tree [4]. Ball's configuration-model asymptotic epidemic-variance results concern random graphs in a large-population limit [5]. These background connections leave a possible reduction of the specific index to existing general moment or percolation formulas as a publication-priority risk.

## Limitations

This is an exact finite-tree result for a single initially infected root, homogeneous edge contact rate, and independent individual infectiousness variables. Cycles, multiple imported cases, shared/global infectiousness shocks, correlated periods across individuals, time-varying edges, and susceptibility heterogeneity are not covered. Comparing infectious *periods by their mean* alone is insufficient: the theorem compares the induced transmissibility \(P=1-e^{-\beta T}\) at a **fixed mean transmissibility**. Convex ordering does not imply that every outbreak tail probability is larger. The sharp maximum with \(P=1\) would require an infinite infectious period, so the stated finite-period bound is a supremum. Prior-work coverage was investigated but independent publication-priority assessment has not been performed.

## References

[1] C. L. Hall and B. A. Siebert, *Exact solutions and bounds for network SIR and SEIR models using a rooted-tree approximation*, arXiv:2108.07128 (initially public 2021-08-16); Journal of Mathematical Biology 86, 22 (2023), DOI:10.1007/s00285-022-01854-9.

[2] E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, arXiv:q-bio/0610057 (2006), Physical Review E 76, 036113 (2007).

[3] R. R. Wilkinson and K. J. Sharkey, *Impact of the infectious period on epidemics*, arXiv:1710.05730 (2017), Physical Review E 97, 052403 (2018).

[4] L. L. Ramírez-Ramírez and colleagues, *Applications of the Variance of Final Outbreak Size for Disease Spreading in Networks*, Methodology and Computing in Applied Probability (2013).

[5] F. Ball, *Central limit theorems for SIR epidemics and percolation on configuration model random graphs*, arXiv:1812.03105 (2018).
