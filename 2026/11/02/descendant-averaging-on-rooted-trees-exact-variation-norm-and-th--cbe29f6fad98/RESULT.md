# Descendant averaging on rooted trees: exact variation norm and sharp linear growth

## Finding
For every finite rooted tree on \(N\ge2\) vertices, the normalized descendant-average operator has an **exact** graph-total-variation seminorm given by a single subtree-column maximum. The operator is nonexpansive for all real vertex signals **exactly when the unrooted tree is a path**. Optimized over all rooted trees on \(N\) vertices, its norm has the sharp asymptotic growth
\[
\lim_{N\to\infty}\frac{\mathcal K_N}{N}=\frac1e.
\]
A family of branched-spine trees approaches this coefficient, showing that positivity and preservation of constants do not prevent order-\(N\) amplification of signal variation.

## Assumptions and scope
Let \(T=(V,E)\) be a finite, simple, connected tree on \(N\ge2\) vertices, with distinguished root \(r\). Each nonroot vertex \(v\) has parent \(p(v)\); its descendant subtree \(T_v\) includes \(v\). Write \(s_v=|T_v|\) and \(b_v\) for the number of children of \(v\). Every vertex carries counting measure, and every edge has variation weight one. Define, for every real vertex function \(f\),
\[
(Af)(v)=\frac1{s_v}\sum_{u\in T_v}f(u),\qquad
V(f)=\sum_{v\ne r}|f(v)-f(p(v))|.
\]
The seminorm is zero exactly on constant signals, and \(A\mathbf 1=\mathbf 1\), so \(A\) induces an operator on the quotient modulo constants. Its norm is the supremum of \(V(Af)/V(f)\) over \(V(f)>0\). For \(v\ne r\), write \(a\prec v\) if \(a\) is a strict ancestor of \(v\). Let \(\mathcal K_N\) be the maximum of these operator norms over all choices of an \(N\)-vertex tree and root.

The exact formula is
\[
\boxed{\displaystyle
\|A\|_{V\to V}=\max_{v\ne r}
\left[1+s_v\left(\sum_{a\prec v}\frac{b_a-1}{s_a}-\frac1N\right)\right].}
\]
For every particular \(v\), its displayed summand is attained by \(f=\mathbf1_{T_v}\), so there is no limiting-extremizer qualification.

## Proof
**1. Reduction to descendant indicators.** Every signal has the identity
\[
f=f(r)\mathbf1+\sum_{v\ne r}(f(v)-f(p(v)))\mathbf1_{T_v}.
\]
Indeed, the terms along the path from \(r\) to a given vertex telescope, and all other terms vanish there. These edge increments are independent coordinates, and \(V(f)\) is their \(\ell^1\)-norm. Since \(A\mathbf1=\mathbf1\), the triangle inequality gives
\[
V(Af)\le \max_{v\ne r}V(A\mathbf1_{T_v})\,V(f).
\]
Taking an individual subtree indicator proves equality for the operator norm, because \(V(\mathbf1_{T_v})=1\).

**2. Exact column variation.** Fix \(v\ne r\), write \(t=s_v\), and let \(g=A\mathbf1_{T_v}\). Inside \(T_v\) every value of \(g\) is one; outside all strict ancestors of \(v\) and \(T_v\), every value is zero. On a strict ancestor \(a\), the value is exactly \(g(a)=t/s_a\).

All edges along the ancestral path from the root to \(v\) have nonnegative increments, and their absolute increments telescope to \(1-t/N\). At each strict ancestor \(a\), the edges leading into its \(b_a-1\) off-path child subtrees each contribute exactly \(t/s_a\) in absolute difference. Every other edge contributes zero. Hence
\[
V(g)=1-\frac{t}{N}+t\sum_{a\prec v}\frac{b_a-1}{s_a}.
\]
This proves the exact formula and its attainment for every finite rooted tree.

**3. Path-only contraction.** If the unrooted tree is a path and \(r\) is an endpoint, all strict ancestors have at most one child, so each column is \(1-s_v/N<1\). If the root lies in the interior of a path, it has exactly two children while every other nonleaf vertex has one child, so each column equals \(1\). Conversely, suppose the tree is not a path. A vertex has unrooted degree at least three. If the root has at least three children, select any child \(v\): its ancestral sum has at least \(2/N\), which is greater than \(1/N\), so its column exceeds one. Otherwise choose a nonroot branching vertex \(a\) with at least two children and select a child \(v\). Since \(s_a<N\), the term \((b_a-1)/s_a\ge1/s_a>1/N\); all other terms in the ancestral sum are nonnegative. Thus the selected column again exceeds one. Therefore nonexpansivity is equivalent to the unrooted path property.

**4. Upper asymptotic bound.** Fix \(v\), and list its strict ancestors from root to parent as \(a_0,\ldots,a_{h-1}\), with \(a_h=v\). Put \(S_i=s_{a_i}\), so \(S_0=N\), \(S_h=t\). Each strict ancestor has a continuation child, while its \(b_{a_i}-1\) other children lead to nonempty, disjoint subtrees. Consequently
\[
b_{a_i}-1\le S_i-S_{i+1}-1
\quad\text{and}\quad
\frac{S_i-S_{i+1}}{S_i}\le\log\frac{S_i}{S_{i+1}}.
\]
Summing and telescoping the logarithms yields
\[
\|A\|_{V\to V}\le1+\max_{1\le t<N}t\log(N/t)\le1+N/e.
\]
Here the last inequality is the elementary maximum of the continuous function \(t\mapsto t\log(N/t)\) for \(0<t<N\).

**5. Matching explicit construction.** For sufficiently large \(N\), set \(h=\lfloor\sqrt N\rfloor\) and \(t=\lfloor N/e\rfloor\). Take a chain of \(h\) strict ancestors, place a path subtree containing \(t\) vertices at its terminal child, and distribute the remaining \(N-t-h\) vertices as single-leaf siblings among those \(h\) ancestors as equally as possible. Let \(q_i\) be the number of leaf siblings of ancestor \(a_i\). Thus \(\sum_iq_i=N-t-h\), and all \(q_i\) differ by at most one. Put \(\Delta_i=S_i-S_{i+1}=q_i+1\); then \(S_0=N\), \(S_h=t\), and \(\Delta_{\max}=O(\sqrt N)\).

For \(0<\Delta_i<S_i\), direct integration gives
\[
0\le\log\frac{S_i}{S_{i+1}}-\frac{\Delta_i}{S_i}
\le\frac{\Delta_i^2}{S_iS_{i+1}}.
\]
Furthermore,
\[
\sum_i\frac{\Delta_i^2}{S_iS_{i+1}}
\le\Delta_{\max}\sum_i\left(\frac1{S_{i+1}}-\frac1{S_i}\right)
=\Delta_{\max}\left(\frac1t-\frac1N\right).
\]
Since \(q_i=\Delta_i-1\) and \(\sum_i1/S_i\le h/t\), the chosen subtree-indicator column satisfies
\[
\begin{aligned}
V(A\mathbf1_{T_v})
&=1-\frac tN+t\sum_i\frac{q_i}{S_i}\\
&\ge1-\frac tN+t\log(N/t)
-\Delta_{\max}(1-t/N)-h\\
&=\frac Ne-O(\sqrt N).
\end{aligned}
\]
The matching upper and lower bounds prove \(\mathcal K_N=N/e+O(\sqrt N)\), and hence the asserted limit. The \(O(\sqrt N)\) notation concerns a universal absolute constant as \(N\to\infty\), not a numerically optimized finite-size error.

## Verification
The standalone standard-library program `verify_tree_subtree_bv.py` constructs each operator directly from descendant averages and independently compares all subtree-indicator column variations with the closed formula, using exact rational arithmetic. It exhausts all rooted labeled trees of orders two through six (8,726 cases), tests a further 250 random rooted trees of larger orders, checks the path-only nonexpansivity classification in the exhaustive cases, and computes concrete lower-construction ratios at four growing sizes. The program passed these diagnostics, including 5,957 noncontractive cases among the exhaustive tests. Its finite computations do not prove the unrestricted theorem or the asymptotic limit; those follow from the algebra above. Execute with `python verify_tree_subtree_bv.py` in a standard Python 3 environment.

## Relationship to prior work
The rooted-tree Hardy summation literature establishes estimates for weighted ancestor-sum operators between vertex \(\ell^p\) spaces. In particular, Vasil'eva's 2013 preprint and 2015 companion study analyze weighted summation norms; the displayed operators act on vertex-valued \(\ell^p\) data rather than on functions modulo constants with the **edge-variation seminorm**. The functional, descendant orientation, exact subtree-column norm, path-only contraction characterization, and extremal \(1/e\) coefficient are therefore not directly implied by those theorems.

Tree-structured averaging also occurs in multiscale signal transforms, notably Mishne and collaborators' partition-tree averaging transform, which maps leaf data to averages indexed by hierarchical folders. The present statement instead averages vertex data over every rooted descendant subtree and measures differences on the **same original tree edges**. The relation is close enough that implicit prior coverage in hierarchical-transform literature is a residual originality risk; full-text access to that particular follow-up was not obtained. The novelty assertion is evidence-limited rather than a claim of exhaustive uniqueness.

## Limitations
Only finite unweighted trees with counting vertex measure and descendant sets including their root are considered. The path-only criterion is for the stated operator, not arbitrary hierarchical smoothing, graph-ball averages, ancestor averages, or weighted Hardy operators. No exact formula is claimed for the finite-size maximum \(\mathcal K_N\), beyond its asymptotic coefficient and constructive error order. The asymptotic extremal family has growing branching, and no analogous infinite-tree boundedness assertion follows. Independent mathematical audit has not been performed.

## References
1. A. A. Vasil'eva, *Estimates for norms of two-weighted summation operators on a tree under some conditions on weights*, arXiv:1311.0375v1 (2 November 2013), https://arxiv.org/abs/1311.0375.
2. A. A. Vasil'eva, *Estimates for norms of two-weighted summation operators on trees for \(1<p<q<\infty\)*, arXiv:1509.06974v1 (18 September 2015), https://arxiv.org/abs/1509.06974.
3. W. D. Evans, D. J. Harris, and L. Pick, *Weighted Hardy and Poincaré inequalities on trees*, J. London Math. Soc. 52 (1995), 121–136, https://doi.org/10.1112/jlms/52.1.121.
4. G. Mishne, R. Talmon, I. Cohen, R. R. Coifman, and Y. Kluger, *Data-Driven Tree Transforms and Metrics*, arXiv:1708.05768 (2017), https://arxiv.org/abs/1708.05768.
