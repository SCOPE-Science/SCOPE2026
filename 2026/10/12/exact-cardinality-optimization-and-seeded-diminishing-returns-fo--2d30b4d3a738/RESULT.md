# Exact cardinality optimization and seeded diminishing returns for Rao diversity on ultrametric trees

## Finding

Let \(T\) be a rooted binary tree with \(n\ge2\) tips, strictly positive rational edge lengths, and common root-to-tip height \(H>0\). For every nonempty tip set \(S\), define the **maximally reweighted Rao quadratic diversity**
\[
F_T(S)=\max_{p_i\ge0,\ \sum_{i\in S}p_i=1}
\sum_{i,j\in S}p_i p_j\,d_T(i,j).
\]
All maximizers for each \(S\) are unique and assign positive weight to every tip in \(S\). Let \(R_T(S)\) denote the effective electrical resistance from the root to the set of selected tips shorted together, with tree-edge resistance equal to branch length. Then
\[
\boxed{F_T(S)=2\bigl(H-R_T(S)\bigr).}
\]

For every nonempty \(A\subsetneq B\subseteq X\) and every tip \(x\notin B\), the marginal diversity gains obey the **strict seeded diminishing-returns law**
\[
0<F_T(B\cup\{x\})-F_T(B)
<F_T(A\cup\{x\})-F_T(A).
\]
In contrast, setting \(F_T(\varnothing)=0\) makes this set function non-submodular on the entire power set: two distinct singleton sets have value zero, but their union has strictly positive value.

For every target \(1\le k\le n\), both \(\max_{|S|=k}F_T(S)\) and an optimizing subset with its unique maximizing weights can be computed **exactly in \(O(nk^2)\) rational arithmetic operations** by the tree knapsack described below. This is a result about one objective: maximum Rao diversity after freely optimizing abundances and choosing at most a fixed number of conserved species.

## Assumptions and scope

All tip-to-tip distances are tree-path lengths, so every distinct pair satisfies \(d_T(i,j)>0\), and all tips are the same distance \(H\) from the root. There are no costs, abundance ceilings, or unequal species eligibility constraints. The subset size is exactly \(k\); because strict monotonicity holds, the same best value is obtained with an at-most-\(k\) constraint. A rooted binary tree has two children at each internal vertex. Exact rational edge lengths permit rational-arithmetic output; the mathematical identities themselves hold for arbitrary positive real branch lengths. The electric root/selected-leaf network is only a representation of the ecological optimization, not an assumed biological dispersal process.

## Proof

**Step 1: covariance/energy identity.** For tips \(i,j\), let \(t_{ij}\) be the root-to-most-recent-common-ancestor length, taking \(t_{ii}=H\). Ultrametricity gives \(d_T(i,j)=2(H-t_{ij})\). Writing \(D(e)\) for the descendant tips of edge \(e\), and \(m_e=\sum_{i\in S\cap D(e)}p_i\), the shared-ancestry identity is
\[
\sum_{i,j\in S}p_i p_j t_{ij}
=\sum_{e\in E(T)}\ell_e\left(\sum_{i\in S\cap D(e)}p_i\right)^2
=\sum_{e\in E(T)}\ell_e m_e^2.
\]
Since total tip mass is one, Rao diversity equals \(2H-2\sum_e\ell_e m_e^2\). Every admissible tip-mass vector yields a unit flow from the root to the shorted selected tips, with current \(m_e\) on edge \(e\). Conversely, every such feasible directed unit flow yields its nonnegative terminal masses. Thomson's least-energy principle, or the elementary series/parallel minimization \(\min_{z_1+z_2=z}(r_1z_1^2+r_2z_2^2)=z^2(r_1^{-1}+r_2^{-1})^{-1}\), proves that the minimum energy is \(R_T(S)\).

Because every edge resistance is strictly positive and the selected leaves are sinks at a common potential, the unique unit electrical flow distributes strictly positive current to every selected terminal. Indeed each child branch containing a selected leaf has finite positive effective resistance and therefore positive current; repeat this argument along every selected root-to-tip path. Strict convexity also follows directly because each tip has its own positive-length pendant edge, so the unique minimizing probability vector has full support. This proves the identity and uniqueness.

**Step 2: exact cardinality recursion.** At each vertex \(v\) let \(R_v(j)\) be the smallest resistance between \(v\) and any set of exactly \(j\) descendant leaves, shorted to a common sink; interpret no selected leaves as infinite resistance. At a leaf \(v\), set \(R_v(0)=+\infty\) and \(R_v(1)=0\). At a binary internal vertex with children \(u,w\) and incident lengths \(a,b>0\), the exact recurrence, for \(j\ge1\), is
\[
\boxed{
R_v(j)=\left[\max_{\substack{j_u+j_w=j\\0\le j_u\le n_u,\ 0\le j_w\le n_w}}
\left(\frac{\mathbf 1_{j_u>0}}{a+R_u(j_u)}+
\frac{\mathbf 1_{j_w>0}}{b+R_w(j_w)}\right)\right]^{-1},}
\]
where terms with zero selected leaves are defined as zero conductance; set \(R_v(0)=+\infty\). Series resistances add; the two child branches combine in parallel. Because conductance is decreasing in each child resistance, independently optimizing each child conditional on its leaf count is legitimate. Induction on the subtree verifies the recurrence and reconstructs an optimal subset. For target \(k\), there are at most \(O(nk^2)\) split evaluations and \(O(nk)\) stored values. Backtracking recovers the maximizing set, and electrical current division uniquely recovers its positive optimal abundances. With exact rational inputs all entries and comparisons are rational.

**Step 3: strict diminishing returns away from the empty set.** Put \(C_v(S)=1/R_v(S)\) for a nonempty selected descendant set, and \(C_v(\varnothing)=0\). For an edge of length \(a>0\), the child branch conductance is \(h_a(C_v(S))\), where
\[
h_a(z)=\frac{z}{1+az},\qquad z\ge0.
\]
A leaf's branch conductance is simply \(a^{-1}\) when that leaf is selected and zero otherwise. This is a monotone submodular set function. More generally, composition of any nonnegative monotone submodular function with a nondecreasing concave scalar function is again monotone submodular: if \(s\le t\) and \(u\ge v\ge0\), concavity and monotonicity imply \(h(s+u)-h(s)\ge h(t+v)-h(t)\). Since \(h_a\) is strictly increasing and concave, induction from leaves and summation over children proves that the root conductance \(C_T(S)\) is monotone submodular.

It is also strictly increasing whenever a new distinct tip is selected. Adding that tip strictly raises conductance in its pendant branch, and strict monotonicity of every \(h_a\), together with addition across child branches, propagates the strict increase to the root. For \(\varnothing\ne A\subsetneq B\) and \(x\notin B\), write \(c_A=C_T(A)\), \(c_B=C_T(B)\) and \(\Delta_A=C_T(A\cup\{x\})-c_A\), \(\Delta_B=C_T(B\cup\{x\})-c_B\). Then \(0<c_A<c_B\) and \(\Delta_A\ge\Delta_B>0\). Consequently
\[
\frac1{c_A}-\frac1{c_A+\Delta_A}
=\frac{\Delta_A}{c_A(c_A+\Delta_A)}
>
\frac{\Delta_B}{c_B(c_B+\Delta_B)}
=\frac1{c_B}-\frac1{c_B+\Delta_B}>0.
\]
Multiplication by two and the identity in Step 1 prove the asserted strict seeded diminishing returns. Finally \(F_T(\{i\})=F_T(\{j\})=0\) but \(F_T(\{i,j\})=d_T(i,j)/2>0\), so the empty-set submodularity inequality fails.

## Verification

The included `verify.py` is executable with standard Python 3 and uses exact fractions throughout. For all \(2\le n\le7\), it constructs 15 reproducible randomly generated positive-rational ultrametric binary trees of each size. For all nonempty tip subsets it compares effective conductance with an **independently solved positive-definite shared-ancestry linear system** and directly recomputes the quadratic objective at its maximizing weights. It compares each knapsack value with exhaustive subset minimization and checks strict diminishing returns for every relevant triple of subsets and an added tip. The completed run reported:

```text
VERIFY_OK direct_KKT_vs_conductance=3690 knapsack_optima=405 strict_marginal_triples=83970
```

A transparent four-tip check uses a root with two child edges of length \(2\) and \(1\); two pendant edges of length \(1\) hang below the first child and two of length \(2\) below the second. The ultrametric height is \(H=3\). Shorting all tips gives branch resistances \(5/2\) and \(2\), hence \(R=10/9\) and \(F_T(X)=34/9\). The unique maximizing tip weights are \((2/9,2/9,5/18,5/18)\). These checks corroborate but are not the proof of statements quantified over arbitrary finite trees.

## Relationship to prior work

Rao (1982) introduced the distance-weighted quadratic entropy. Pavoine, Ollier and Pontier (2005) specifically showed that for ultrametric dissimilarities the maximizing distribution does not eliminate any category, consistent with the full-support statement here. Their accessible abstract concerns a *fixed* category set. The distinction here is simultaneous **exact selection of a cardinality-constrained set and optimal continuous reweighting**, together with a strict diminishing-returns classification for nonempty initial sets. The 2005 article's full text could not be inspected, so stronger coverage cannot be excluded from the abstract alone.

Steel (2005) proves greedy exact maximization for Faith's phylogenetic diversity, defined as *the total length of the induced subtree*. Its full author-posted article, including theorem, proof and extensions, concerns that edge-union objective rather than Rao's optimized pairwise-distance expectation; neither the latter's global failure of submodularity nor the electrical knapsack follows from the stated Faith-PD theorem. General-purpose software documents computation or maximization of Rao entropy for fixed species sets, not the exact cardinality-constrained tree recursion. General network grounded-resistance results may contain broader implicit specializations, and remain a residual originality risk.

## Limitations

The theorem assumes strictly positive edges and ultrametricity; unequal tip depths invalidate the constant \(2H\) transformation. Zero-length edges can destroy strictness and the uniqueness assertion. The algorithm is exact for rational edge lengths and unconstrained abundances; imposing minimum, maximum, or discrete abundances changes the problem. The seeded diminishing-returns law **does not make** the globally normalized set function submodular at the empty set, nor does it prove that greedy selection attains the global cardinality optimum. No statement about observed ecological abundance constraints is made. Independent validation has not been performed.

## References

1. C. R. Rao (1982), *Diversity and dissimilarity coefficients: a unified approach*, Theoretical Population Biology **21**, 24–43.
2. S. Pavoine, S. Ollier and D. Pontier (2005), *Measuring diversity from dissimilarities with Rao's quadratic entropy: are any dissimilarities suitable?*, Theoretical Population Biology **67**, 231–239. DOI: `10.1016/j.tpb.2005.01.004`.
3. M. Steel (2005), *Phylogenetic Diversity and the Greedy Algorithm*, Systematic Biology **54**, 527–529. DOI: `10.1080/10635150590947023`.
4. S. Pavoine and M. B. Bonsall (2009), *Biological diversity: distinct distributions can lead to the maximization of Rao's quadratic entropy*, Theoretical Population Biology **75**, 153–163. DOI: `10.1016/j.tpb.2009.01.008`.
5. `DescTools`, CRAN reference manual, *Maximal value of Rao's diversity coefficient also called quadratic entropy* (fixed-set computational benchmark).
